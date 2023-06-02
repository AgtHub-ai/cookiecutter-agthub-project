from fastapi import Depends, APIRouter, Body, Request
from loguru import logger
from agthub_sdk import Context
from agthub_sdk.models import AgentInitRequest, ConversationMapping, \
ConversationConfig, ConversationState, MessageInterface, AgentRequestContext, \
Ack, Message

from agthub_sdk.tools import msgs_cut_down
from agthub_sdk.tools import msg_token_count, msgs_token_count
from agthub_sdk.models import MessageInterface
from concurrent.futures import ThreadPoolExecutor

agent_conf = {
    'app_id': '',
    'app_secret': ''
}

def chat_agent(ctx: Context):
    with ctx.init_conversation(onetime_cache=False) as conversation:
        conversation_config: ConversationConfig = conversation.config
        conversation_state: ConversationState = conversation.state

        # start a new conversation if no conversation found
        if not conversation_config.conversation_id:
            conversation.start()

        user_input: Message = conversation_state.user_input
        # conv = conversation.get_conversation_info(conversation_config.conversation_id)

        hist_msgs: list[MessageInterface] = conversation.get_historical_msgs()
        full_msgs = [conversation_state.system_msg]
        if len(hist_msgs):
            # get maximum token counts
            user_msg_tokens = msgs_token_count(hist_msgs, model_name=conversation_config.model)
            sys_msg_tokens = msg_token_count(conversation_state.system_msg)
            remain_tokens = conversation.config.MAX_PROMPT_TOKENS - user_msg_tokens - sys_msg_tokens
            hist_msgs_clipped = msgs_cut_down(hist_msgs,
                                              cut_from_beginning=True,
                                              max_token=remain_tokens)
            full_msgs = [conversation_state.system_msg, *hist_msgs_clipped]

        streamer = conversation.create_stream(user_input, full_msgs)
        return streamer

router = APIRouter(tags=["agent"])

@router.post("/start", response_model=Ack)
async def start_agent(request: Request, init_req: AgentInitRequest = Body(
    example=AgentInitRequest(
                conversation_mapping=ConversationMapping(
                    config=ConversationConfig(
                        conversation_id='123e4567-e89b-12d3-a456-426614174000',
                        model='gpt-4'),
                    conversation_state=ConversationState(
                        doc_id='123e4567-e89b-12d3-a456-426614174000',
                        user_input=MessageInterface(
                            conversation_id="123e4567-e89b-12d3-a456-426614174000",
                            role='user',
                            content='1+1=?'),
                        system_msg=MessageInterface(
                            conversation_id="123e4567-e89b-12d3-a456-426614174000",
                            role='system',
                            content='You are a helpful assistant!')
                    )
                ),
        agent_id='d2a57dc1d883fd21fb9951699df71cc7'),
    description='')
):
    ctx = await Context.from_init_request(ctx=init_req,
                                      agent_requst_ctx= AgentRequestContext(app_id = agent_conf['app_id'], 
                                                                            app_secret = agent_conf['app_secret'], 
                                                                            user_data = '' ))
    chat_agent(ctx);
    # 异步执行
    # loop = asyncio.get_event_loop()
    # executor = ThreadPoolExecutor()
    # loop.run_in_executor(executor, chat_agent, ctx)
    return Ack(msg='Agent started')
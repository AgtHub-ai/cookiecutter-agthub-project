from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import Response
import io, functools, yaml, os
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .routers import user_router, item_router, agent_router
from .log import init_logging

init_logging()
# 自动建表 auto create table
Base.metadata.create_all(bind=engine)
app = FastAPI()

# 默认适配openai plugin配置输出, 如有需要修改.well_known文件下内容
# add endpoints
# additional yaml version of openapi.json
@app.get('/openapi.yaml', include_in_schema=False)
@functools.lru_cache()
def read_openapi_yaml() -> Response:
    openapi_json= app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s)
    return Response(yaml_s.getvalue(), media_type='text/yaml')

main_path = os.path.dirname(__file__)
openai_path = os.path.join(main_path, ".well_known")
app.mount("/.well_known", StaticFiles(directory=openai_path), name="static")

app.include_router(item_router.router)
app.include_router(user_router.router)
app.include_router(agent_router.router)
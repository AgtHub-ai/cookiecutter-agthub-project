# {{ cookiecutter.project_name }}

## Overview

{{ cookiecutter.project_description}}

**注意：** 项目支持 `Python >= 3.10` 。

## 项目使用
### 进入到项目中
```bash
cd my_project
```

### 初始化项目环境 (已安装的可略过)
#### 安装 python virtualenv 虚拟环境管理工具
```bash
pip install virtualenv
```
#### 使用 virtualenv 创建Python虚拟环境 并 进入虚拟环境中
```bash
virtualenv .venv
source .venv/bin/activate
```
<!-- # On Windows?
```bash
source .venv/Scripts/activate
``` -->
#### 如果使用了 poetry 则执行 poetry install -v 
```bash
poetry install -v
```

### 运行项目
#### 进入虚拟环境
```bash
poetry shell
```
#### 运行uvicorn
```bash
uvicorn src.{{cookiecutter.project_slug}}.main:app --reload
```

## 自定义开发llm agent 
### 添加langchain
```bash
poetry add langchain
```
### 在setting.yml中添加配置
```yml
openai.key: xxxxx
```
### 代码中使用
```python
from langchain.llms import OpenAI
from yourprojectname.config import settings
llm = OpenAI(openai_api_key=settings.get("openai.key"))
```

### Debug项目
**由于使用虚拟环境需要配置python运行环境, 需要作以下配置**
**使用VSCode Debug项目**
1. 打开运行与调试
2. 创建launch.json文件
3. 文件中填入以下内容
```json
{
  "version": "0.2.0",
  "configurations": [
      {
          "name": "Agent service",
          "type": "python",
          "request": "launch",
          "pythonPath": "${workspaceFolder}/.venv/bin/python",
          "cwd": "${workspaceFolder}",
          "module": "uvicorn",
          "justMyCode": false,
          "args": [
              "src.testpoe.main:app",
              "--host",
              "0.0.0.0",
              "--port",
              "8000",
              "--reload"
          ]
      }
  ]
}
```
4. 在运行调试菜单下, 执行 **Agent service** 配置
4. 打好断点, 访问相应的接口即可进入debug模式


### 单元测试 tox
```shell script
tox
```

### Build

Build this tag distribution package.

```shell script
poetry build
```

### Upload index server

Upload to pypi server, or pass `--repository https://pypi.org/simple` to specify index server.

```shell script
poetry publish
```

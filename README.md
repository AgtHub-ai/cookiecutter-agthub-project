# 快速开始

一个使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 工具生成 Python 工程化项目的模板。


## 特性

- 跨平台支持使用
- 支持自定义配置选项
- 默认使用 SRC 项目结构
- 初始化 PEP517 规范打包配置，默认使用 [poetry](https://python-poetry.org/) 打包。
- 可选初始化通用项目骨架

**注意：** 项目支持 `Python >= 3.10` 。

### 直接使用

```bash
# 升级最新 pip
pip install -U pip

# 安装或升级 cookiecutter
pip install -U cookiecutter

# 使用 cookiecutter 加载项目模板，生成项目
# 回车运行的时候，需要根据提示交互选择启用的功能。
# 如果使用默认配置，则一路回车就可以。
cookiecutter http://git.clicki.cn/ai/AgentCircle/AgentCircle_BackendBase
```

### 详细说明

#### 创建项目

```text
❯ cookiecutter http://git.clicki.cn/ai/AgentCircle/AgentCircle_BackendBase
project_name [My Project]: 
project_slug [my_project]: 
project_description [My Awesome Project!]: 
author_name [Author]: 
author_email [author@example.com]: 
version [0.1.0]: 
Select python_version:
1 - 3.11
2 - 3.10
Choose from 1, 2 [1]: 2
use_src_layout [y]: 
use_poetry [y]: 
use_docker [y]: 
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]: 
init_skeleton [y]: 
```

上述操作，全部使用了默认逻辑：

- 使用默认项目名： `My Project`
- 默认的项目目录和包名： `my_project`
- 默认的项目描述： `My Awesome Project!`
- 默认的用户： `author`
- 默认的邮箱： `author@example.com`
- 默认的版本号： `0.1.0`
- 默认的 Python 版本： `python 3.10`
- 默认的项目结构： SRC 结构
- 默认不使用 Docker 环境
- 默认不适用 CI 环境
- 默认不初始化项目骨架


目录中包含了一个完整项目所需要的内容。有项目打包用到的描述文件，记录项目依赖文件和一个简单的测试用例。

项目使用 SRC 目录结构，项目模块在 SRC 下。强烈建议开发前测试你的代码，可以避免因项目生成项目模板导致后期开发异常。

### 使用项目

进入项目目录：
```bash
cd my_project
```

#### 初始化项目环境

##### 安装 python virtualenv 虚拟环境管理工具(已安装的可略过)
```bash
pip install virtualenv
```
##### 使用 virtualenv 创建Python虚拟环境
```bash
virtualenv .venv
```
##### 进入虚拟环境中

```bash
source .venv/bin/activate
```
##### 如果使用了 poetry 则执行 poetry install -v 
```bash
poetry install -v
```
#### 运行项目
##### 进入虚拟环境
```bash
poetry shell
```
##### 运行项目
```bash
uvicorn src.{{projectname}}.main:app --reload
```


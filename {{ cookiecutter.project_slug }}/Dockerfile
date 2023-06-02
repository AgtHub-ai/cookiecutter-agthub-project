FROM python:{{ cookiecutter.python_version }}

LABEL name="{{ cookiecutter.project_name }}"
LABEL version="{{ cookiecutter.version }}"
LABEL description="{{ cookiecutter.project_description }}"

WORKDIR /app
# 安装环境
RUN pip install poetry
RUN pip install uvicorn

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 8000

{%- if cookiecutter.use_src_layout|lower == 'y' %} 
CMD ["uvicorn", "src.{{cookiecutter.project_slug}}.main:app", "--host", "0.0.0.0", "--port", "8000"]
{%- else %}  
CMD ["uvicorn", "{{cookiecutter.project_slug}}.main:app", "--host", "0.0.0.0", "--port", "8000"]
{%- endif %}

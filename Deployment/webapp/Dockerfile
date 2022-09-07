FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN pip install -U pip aiofiles==22.1.0 python-multipart jinja2 fastapi uvicorn==0.18.3
COPY /webapp /app

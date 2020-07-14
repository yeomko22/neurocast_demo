FROM python:3.7.8-alpine3.12

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./venv ./venv
CMD ["python", "venv/bfweb.py"]

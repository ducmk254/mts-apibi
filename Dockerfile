FROM python:3.11.1

COPY ./app /app

COPY ./requirements.txt /requirements.txt
COPY ./dw-mutosi-047c9c3d37a7.json /dw-mutosi-047c9c3d37a7.json
COPY ./.env /.env

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

EXPOSE 8082

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8082"]

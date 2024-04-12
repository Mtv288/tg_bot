FROM python:3.11.8-alpine

ENV PYTHONPATH "${PYTHONPATH}:/python_basic_diploma"




WORKDIR /bot_obuv

COPY . .
COPY bot_obuv/All.csv /bot_obuv/All.csv

RUN apk add --no-cache icu-libs \
    && python3 -m pip install -r requirements.txt

CMD ["python", "bot_obuv/main_run.py"]







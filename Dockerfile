FROM python:3.11.1

RUN mkdir /bot && apt-get update


WORKDIR /bot

COPY bot_obuv/ /bot_obuv/
COPY requirements.txt requirements.txt
COPY bot_obuv/main_run.py /main_run.py

RUN python -m pip install -r requirements.txt


COPY . .

CMD ["python", "bot_obuv/main_run.py"]
FROM python:3.11.1

RUN mkdir /bot && apt-get update


WORKDIR . .

COPY main_run.py /bot_obuv/main_run.py
COPY requirements.txt requirements.txt


RUN python -m pip install -r requirements.txt


COPY . .

CMD ["python", "bot_obuv/main_run.py"]
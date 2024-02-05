FROM python:3.11.1


RUN mkdir /bot


COPY . /bot

WORKDIR . /bot

COPY . /bot_obuv
COPY bot_obuv/ /All.csv
COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

CMD ["python", "bot_obuv/main_run.py"]
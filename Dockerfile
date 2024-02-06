FROM python:3.11.1


RUN mkdir /bot


COPY . /bot

WORKDIR /bot


COPY requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["python", "bot_obuv/main_run.py"]
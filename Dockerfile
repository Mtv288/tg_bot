FROM python:3.9

RUN mkdir /bot && apt-get update


WORKDIR /bot


COPY requirements.txt requirements.txt


RUN python -m pip install -r requirements.txt


COPY ./ /bot

CMD ["python", ".bot_obuv/main_run.py"]
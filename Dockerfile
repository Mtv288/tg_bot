FROM python:3.11.1


RUN mkdir /bot


COPY . /bot

WORKDIR . /bot


COPY requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["python", "main_run.py"]
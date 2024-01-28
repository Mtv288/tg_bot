FROM python:3.11

WORKDIR . .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "bot_obuv/main_run.py"]
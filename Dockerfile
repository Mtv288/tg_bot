FROM python:3.11.1



COPY . /python_basic_diploma



COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "python_basic_diploma/bot_obuv/main_run.py"]
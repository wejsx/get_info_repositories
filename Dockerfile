FROM python:3.11.1
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
WORKDIR /app
CMD ["uvicorn", "src.app:app", "--reload", "--port", "80"]
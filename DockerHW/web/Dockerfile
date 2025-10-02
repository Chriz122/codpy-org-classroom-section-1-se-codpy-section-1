# ./web/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 只複製 requirements.txt，避免被 volumes 蓋掉
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
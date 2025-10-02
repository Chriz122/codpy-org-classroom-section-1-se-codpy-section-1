# 導案結構樹

DockerHW/
├─ web/                 # 專案程式碼
│   ├─ main.py
│   ├─ requirements.txt
│   └─ ...
├─ docker-compose.yml

##

FROM python:3.11-slim       # 使用 Python 官方輕量版本

WORKDIR /app                # 設定容器內的工作目錄

COPY requirements.txt .     # 先複製 requirements，避免每次都重新安裝

RUN pip install --no-cache-dir -r requirements.txt  # 安裝依賴

CMD ["python", "main.py"]   # 預設執行 main.py

##

version: '3.9'

services:
  web:
    build: ./web          # 指定 build context
    container_name: web_app
    ports:
      - "5000:5000"       # 映射 port: host:container
    volumes:
      - ./web:/app        # 掛載本機程式碼，方便即時修改
    environment:
      - PYTHONUNBUFFERED=1
## 成功畫面

<img width="772" height="587" alt="image" src="https://github.com/user-attachments/assets/fd6b74ca-4dc1-4a90-addb-fb5a7c1f5897" />


FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Указываем, что контейнер будет слушать на порту 3762
EXPOSE 3762

# Запускаем uvicorn сервер
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "3762", "--reload"]

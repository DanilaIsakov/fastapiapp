# Используем официальный python-образ
FROM python:3.12.0

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY app /app/app
COPY model.pkl /app/model.pkl

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r app/requirements.txt

# Запускаем FastAPI с Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

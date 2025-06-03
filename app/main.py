from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Загружаем модель
model = joblib.load("model.pkl")


# Описание входных данных для предсказания
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(features: IrisFeatures):
    # Формируем массив признаков из полученных данных
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])

    # Получаем предсказание модели
    prediction = model.predict(data)

    # Возвращаем результат
    return {"predicted_class": int(prediction[0])}

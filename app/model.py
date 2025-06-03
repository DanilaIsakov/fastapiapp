from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Загружаем данные
data = load_iris()
X, y = data.data, data.target

# Обучаем модель
model = RandomForestClassifier()
model.fit(X, y)

# Сохраняем модель в файл model.pkl
joblib.dump(model, "model.pkl")

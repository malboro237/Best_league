import sys
import os
from sklearn.linear_model import LinearRegression
from traitement import X_train, y_train


# Initialiser et entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)


# Ajouter le chemin au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sklearn.metrics import mean_squared_error, r2_score
from traitement import X_test, y_test
#from my_model import model  # Importer depuis my_model

# Prédire sur l'ensemble de test
y_pred = model.predict(X_test)

# Calculer les métriques de performance
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print(f'RMSE: {rmse}')
print(f'R2 Score: {r2}')

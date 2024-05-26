from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

# Importer les données depuis traitement.py
from traitement import X_train, X_test, y_train, y_test

# Initialiser le modèle de forêt aléatoire
rf_model = RandomForestRegressor(random_state=42)

# Définir la grille des hyperparamètres
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Utiliser GridSearchCV pour trouver les meilleurs hyperparamètres
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Meilleur modèle
best_rf_model = grid_search.best_estimator_

# Prédire sur l'ensemble de test avec le meilleur modèle
y_pred_rf = best_rf_model.predict(X_test)

# Calculer les métriques de performance pour le modèle de forêt aléatoire
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = mse_rf ** 0.5
r2_rf = r2_score(y_test, y_pred_rf)

print(f'Random Forest RMSE: {rmse_rf}')
print(f'Random Forest R2 Score: {r2_rf}')

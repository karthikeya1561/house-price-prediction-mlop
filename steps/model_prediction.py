from zenml import step
from models.predict import prediction
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

@step
def predicting(model:DecisionTreeRegressor)->float:
    pk = prediction()
    predicted = pk.model_predict(model)
    print(predicted)
    return predicted
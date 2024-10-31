from zenml import step
from models.predict import prediction
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import models.end_values
import numpy
@step
def predicting(model:DecisionTreeRegressor,house_area:int, bedrooms:int)->float:
    pk = prediction()
    predicted = pk.model_predict(model,house_area,bedrooms)
    models.end_values.prediction_values = predicted
    print(predicted)
    return predicted
from zenml import step
from models.model_train import training_model
import pandas as pd
from typing import Tuple
from sklearn.tree import DecisionTreeRegressor

@step
def training(x: pd.DataFrame, y: pd.DataFrame) -> DecisionTreeRegressor:
    dt = training_model()
    dtree = dt.model_training(x, y)
    return dtree

def model_create(dr: DecisionTreeRegressor) -> DecisionTreeRegressor:
    pk = training_model()
    model = pk.model_create(dr)
    return model
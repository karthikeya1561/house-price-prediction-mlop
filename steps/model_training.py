from zenml import step
from models.model_train import training_model
import pandas as pd
from typing import Tuple
from sklearn.tree import DecisionTreeRegressor
from zenml.client import Client
import mlflow.sklearn
from mlflow.models.signature import infer_signature

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def training(x: pd.DataFrame, y: pd.DataFrame) -> DecisionTreeRegressor:
    dt = training_model()
    dtree = dt.model_training(x, y)
    mlflow.sklearn.log_model(artifact_path="model", sk_model=dtree, signature=infer_signature(x), registered_model_name="DecisionTreeRegressor")
    return dtree

def model_create(dr: DecisionTreeRegressor) -> DecisionTreeRegressor:
    pk = training_model()
    model = pk.model_create(dr)
    return model
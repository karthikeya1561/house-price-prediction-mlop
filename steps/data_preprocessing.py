from zenml import step
from models.preprocessing_data import data_preprocessing
import pandas as pd
from typing import Tuple
from typing import Annotated

@step
def preprocess(file:pd.DataFrame)->Tuple[Annotated[pd.DataFrame, "x"], Annotated[pd.DataFrame, "y"]]:
    d_preprocess = data_preprocessing(file)
    d_preprocess.preprocessing()
    x,y = d_preprocess.data_splitting()
    return x,y
    
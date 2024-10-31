from zenml import pipeline
from steps.data_ingestion import ingest
from steps.data_preprocessing import preprocess
from steps.model_training import training
from steps.model_training import model_create
from steps.model_prediction import predicting
import numpy as np
@pipeline
def pipeline_dev(data_path:str,house_area = 3000, bedrooms = 2):
    df = ingest(data_path)
    x,y = preprocess(df)
    dtree = training(x,y)
    #model = model_create(dtree)
    predicting(dtree,house_area, bedrooms)
    
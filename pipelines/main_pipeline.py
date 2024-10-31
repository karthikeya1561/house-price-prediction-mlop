from zenml import pipeline
from steps.data_ingestion import ingest
from steps.data_preprocessing import preprocess
from steps.model_training import training
from steps.model_training import model_create
from steps.model_prediction import predicting

@pipeline
def pipeline_dev(data_path):
    df = ingest(data_path)
    x,y = preprocess(df)
    dtree = training(x,y)
    #model = model_create(dtree)
    predicting(dtree)
    
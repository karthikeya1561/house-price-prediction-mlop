from zenml import step
from models.data_ingest import data_ingestion
import pandas as pd
@step
def ingest(data_path:str)->pd.DataFrame:
    dp = data_ingestion()
    data = dp.ingest_data(data_path)
    return data
    
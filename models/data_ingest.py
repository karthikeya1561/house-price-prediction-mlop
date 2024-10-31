import pandas as pd
class data_ingestion:
    def ingest_data(self,data_path:str)->pd.DataFrame:
        file = pd.read_csv(data_path)
        return file
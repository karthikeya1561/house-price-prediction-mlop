import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Tuple
from typing import Annotated
class data_preprocessing:
    def preprocessing(self)->pd.DataFrame:
        for index, row in self.file.iterrows():
            if row["area"] > 3000 and row["bedrooms"] > 4:
                self.file.drop(index, inplace=True)
    def data_splitting(self)->Tuple[Annotated[pd.DataFrame,"x"],Annotated[pd.DataFrame,"y"]]:
        x = self.file.iloc[:,1:3]
        y=self.file.iloc[:,0:1]
        return x,y
    def __init__(self,file):
        self.file = file
        
          
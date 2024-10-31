from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import pickle
import joblib
class training_model:
    def model_training(self,x:pd.DataFrame,y:pd.DataFrame)->DecisionTreeRegressor:
        dr=DecisionTreeRegressor()
        dtree = dr.fit(x,y)
        return dtree
    def model_create(self,dr:DecisionTreeRegressor)-> DecisionTreeRegressor:
        joblib.dump(dr, 'model.pkl')
        model = joblib.load('model.pkl')
        return model
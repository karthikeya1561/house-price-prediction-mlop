from sklearn.tree import DecisionTreeRegressor
import numpy 
class prediction:
    def model_predict(self,model:DecisionTreeRegressor,house_area:int, bedrooms:int)->DecisionTreeRegressor:
        prediction = model.predict([[house_area, bedrooms]])
        return prediction[0]
from sklearn.tree import DecisionTreeRegressor
class prediction:
    def model_predict(self,model:DecisionTreeRegressor)->DecisionTreeRegressor:
        prediction = model.predict([[3000,3]])
        return prediction[0]
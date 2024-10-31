from pipelines.main_pipeline import pipeline_dev
from flask import Flask
import models.end_values
app = Flask(__name__)


val = 0,
        

@app.route('/modeltest')
def get_results():
    data_path = r"Housing.csv"
    house_area = 3500
    bedrooms = 4
    pipeline_dev(data_path=data_path, house_area=house_area, bedrooms=bedrooms)
    
    return f"The Value is {models.end_values.prediction_values}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
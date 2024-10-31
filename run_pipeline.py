from zenml import pipeline, step
from pipelines.main_pipeline import pipeline_dev
from zenml.client import Client
if __name__ == "__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    pipeline_dev(data_path="Housing.csv")
 # mlflow ui --backend-store-uri "file:C:\Users\karth\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\Roaming\zenml\mlruns"  
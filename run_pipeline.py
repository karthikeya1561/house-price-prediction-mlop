from zenml import pipeline, step
from pipelines.main_pipeline import pipeline_dev

if __name__ == "__main__":
    pipeline_dev(data_path="Housing.csv")
    
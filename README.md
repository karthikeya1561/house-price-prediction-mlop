# House Price Prediction Model
## Table of Contents
- [Overview](#overview)
- [Business Case](#business-case)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Performance](#performance)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
## Overview
This repository contains a machine learning model which is designed to predict house prices based on two factors, which are area and bedrooms. This model is intended for real estate professionals, investors, and analysts seeking reliable price estimations to inform decision-making.
This project uses a modular approach, structured with pipelines and object-oriented programming (OOP) concepts to streamline data processing, model training, and deployment. Each step in the pipeline is encapsulated in a function, making it reusable and easy to debug. Classes represent different components of the model lifecycle, allowing for scalable and organized code.
## Business Case
Accurate price predictions provide a competitive advantage in the real estate market. This model assists stakeholders in:

- Making data-driven investment decisions.
- Optimizing property pricing strategies.
- Enhancing risk assessment in property acquisition and sales.
## Key Features
- Pipelines: Each stage of the data lifecycle is connected through defined pipeline steps, enhancing data flow and modularity.
- OOP Principles: Classes and objects represent various components, such as data ingestion, model training, and deployment, resulting in a clean, manageable code structure.
- Data-Driven Predictions: Leverages historical data to predict future house prices.
- Scalable for Multiple Markets: Adaptable to various regions and datasets.
- Quick Insights: Predicts house prices in seconds, enabling rapid decision-making.
## Project Structure
- Data Ingestion: Imports data from local files or cloud storage and preprocesses it for the model.
- Model Training: Utilizes a Decision Tree Regressor for prediction. This choice allows the model to handle non-linear relationships in the data effectively.
- Evaluation and Deployment: Offers performance metrics and a scalable deployment pipeline for model predictions.
## Installation
- Clone the repository: git clone https://github.com/karthikeya1561/house-price-prediction-mlop
- Install dependecies: pip install -r requirements.txt
- Set Up Environment Variables: Define variables such as data paths or API keys if required. Place these in a .env file in the root directory.
## Technical Details
- Model: Decision Tree Regressor
- Libraries: Scikit-learn, Pandas, Joblib, Numpy
- Framework: ZenML (for pipeline orchestration)
## Performance
The model achieves an R² score of 0.85 on our test data, indicating a high level of accuracy and reliability in predicting market-driven house prices.
## Future Enhancements
- Integrate Time-Series Analysis: For improved predictions with respect to seasonal trends.
- Expand Feature Set: Incorporate economic indicators and more property attributes.
- Automate Data Updates: Schedule regular updates to ensure predictions reflect the latest market data.
## Contributing
We welcome contributions! Please fork this repository, make changes, and submit a pull request.

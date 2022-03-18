# Information
This is a demo project showing how a machine learning model can be deployed to the Heroku cloud and interacted with using a flask webapp.

## Website
The actual example site can be browsed by clicking on this [link](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)

## Training Dataset
The model was trained using the Fish market dataset as obtainable from [https://www.kaggle.com/aungpyaeap/fish-market](https://www.kaggle.com/aungpyaeap/fish-market).

This dataset represents dimensions for common fish found in a local market. This dataset can be used for classification models (predicting the species of fish given the dimensions) or regression models (predicting the weight using the other dimensions).

## Machine Learning ModeL
The machine learning model used is Scikit-Learn's linear regression model to predict the weight of the fish. The model is trained using the dataset and the trained model is saved to be used by the web application for predictions.

## Web Application
A simple web application is created using Python Flask. This is a simple webpage form which takes the fish dimensions as inputs and displays the predictions.

## Cloud Platform
The web application is deployed to Heroku's free cloud platform.

# Instructions
## Environment Setup
Before proceeding, make sure `python` and `pip` are installed on your machine.

To setup your environment to test this application locally, run the following steps on a linux/unix terminal:

`git clone https://github.com/rencete/heroku_deploy.git`
`cd heroku_deploy`
`pip install -r requirementts.txt`

## Run Model Creation Code
The model creation code is a jupyter notebook found at `<STARTING_DIRECTORY>/heroku_deploy/model/fish_market_regression.ipynb`. Open and run this file using jupyter notebook, Google Colaboratory, or a similar tool. This jupyter notebook reads the `Fish.csv` dataset found in the same directory and writes the saved model as `model.pkl` also in the same directory.

## Run Web Application Locally
To run the web app locally, run the following steps on a linux/unix terminal when on the git cloned starting directory:
`gunicorn --chdir ./web "flask_app:app"`

The web application can now be browsed using any internet browser by browsing the url: `http://127.0.0.1:8000`
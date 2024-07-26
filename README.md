# Machine Learning API using FastAPI
Develop a Machine Learning API (Application Programming Interface) using FastAPI.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)

## Introduction

Welcome to data science project about sepsis prediction/classification and the API and streamlit application.

## Content

- A jupyter notebook for data cleaning/manipulation, EDA, visualisation and training of MAchine learning models
- 2 python files containing code for a streamlit application (Home page and Predict page)
- A python file for the API built with fastAPI
- A folder containing persisted machine learning models and encoder
- 3 Docker files which were used to containarise the application for docker hub

## Machine Learning

In this jupyter notebook you will find how the data was explored to find insights, and visualisations to make sense of the dataset. I made use of a pipeline to preprocess the data for the ML models. 8 models were trained in total. After balancing the dataset with SMOTE and hyperparameter tuning we selected the top 2 best performing models for our API.

## API with FastAPI

In the folder named API you will find the code for our API. It contains 3 endpoints, the first is a `get` that helps you get the staus of the API.

the other 2 endpoints are post endpoints where you find our two models, predictions are sent to a particular endpoint based on your model selection. The endpoints return a prediction, the probability of the prediction and a message based on the prediction.

## Frontend with Streamlit

In the Frontend folder you will find our home page python code and a folder containing the predict page where all the magic happens.

On the predict page we have a form where you input your patient's results and a submit button to send the form in a json format to the API. the APi then returns a prediction, probability and a little message.

## Docker files

The dockerfiles contain text on how the application should run and the requirements.txt with the dependencies.

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run Streamlit

Change directory into the frontend folder

`cd frontend`

Then run

`streamlit run Home_page.py`

## Run FastAPI

Change directory in the API folder:

`cd api`

Then run
          
`uvicorn api:app --reload`

## Docker Image

[Docker image](https://hub.docker.com/repository/docker/phannsi/sepsis_prediction/general)

## Medium Article

[Medium Article]()

## Author

- [Ezekiel Phannsi](https://www.linkedin.com/in/ezekielphannsi)



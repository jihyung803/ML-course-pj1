{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import os\n",
    "import pandas as pd\n",
    "import nbimporter\n",
    "from pred import preprocess_data\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_squared_error\n",
    "from sklearn.model_selection import train_test_split, GridSearchCV\n",
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"../cleaned_data/heart_disease_mortality_cleaned.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[[\"Year\", \"LocationAbbr\", \"LocationDesc\", \"GeographicLevel\", \"Data_Value_Unit\", \"Data_Value_Type\", \"Sex\", \"ethnicity\", \"LocationID\", \"Y_lat\", \"X_lon\", \"Georeference\"]]\n",
    "y = df[\"Heart Disease Mortality\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test, preprocessor= preprocess_data(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "rf_regressor = Pipeline([\n",
    "    (\"preprocessor\", preprocessor), \n",
    "    (\"regressor\", RandomForestRegressor(random_state = 42)),\n",
    "    ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "randomforest_search_grid = {\n",
    "    \"regressor__n_estimators\": [50, 100, 200],\n",
    "    \"regressor__max_depth\": [None, 1, 2, 3],\n",
    "    \"regressor__max_features\": [None, \"sqrt\", \"log2\"],\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = GridSearchCV(estimator = rf_regressor, param_grid = randomforest_search_grid, scoring = \"neg_root_mean_squared_error\", cv = 3, verbose = 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 36 candidates, totalling 108 fits\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=50;, score=-82.377 total time=   9.8s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=50;, score=-72.856 total time=   9.8s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=50;, score=-85.589 total time=   9.7s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=100;, score=-81.853 total time=  19.5s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=100;, score=-72.393 total time=  19.9s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=100;, score=-85.152 total time=  19.6s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=200;, score=-81.447 total time=  39.4s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=200;, score=-72.243 total time=  39.0s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=None, regressor__n_estimators=200;, score=-84.765 total time=  39.6s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-85.428 total time=   5.0s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-75.832 total time=   5.0s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-87.239 total time=   5.1s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-84.598 total time=  10.0s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-75.517 total time=  10.5s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-86.930 total time=  10.2s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-84.246 total time=  20.0s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-75.242 total time=  20.1s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-86.771 total time=  20.7s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=50;, score=-84.953 total time=   5.0s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=50;, score=-75.490 total time=   5.0s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=50;, score=-87.078 total time=   5.0s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=100;, score=-84.041 total time=  10.0s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=100;, score=-75.350 total time=  10.0s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=100;, score=-86.879 total time=  10.0s\n",
      "[CV 1/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=200;, score=-84.055 total time=  20.4s\n",
      "[CV 2/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=200;, score=-75.224 total time=  19.9s\n",
      "[CV 3/3] END regressor__max_depth=None, regressor__max_features=log2, regressor__n_estimators=200;, score=-86.769 total time=  20.0s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=50;, score=-145.858 total time=   0.3s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=50;, score=-144.758 total time=   0.4s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=50;, score=-150.014 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=100;, score=-145.856 total time=   0.5s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=100;, score=-144.758 total time=   0.4s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=100;, score=-150.015 total time=   0.4s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=200;, score=-145.858 total time=   0.8s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=200;, score=-144.759 total time=   0.7s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=None, regressor__n_estimators=200;, score=-150.017 total time=   0.7s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-148.041 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-147.217 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-153.703 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-148.720 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-147.348 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-153.961 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-148.678 total time=   0.3s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-147.211 total time=   0.3s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-153.920 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=50;, score=-150.377 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=50;, score=-148.117 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=50;, score=-155.754 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=100;, score=-150.762 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=100;, score=-148.914 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=100;, score=-155.886 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=200;, score=-150.446 total time=   0.2s\n",
      "[CV 2/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=200;, score=-148.582 total time=   0.2s\n",
      "[CV 3/3] END regressor__max_depth=1, regressor__max_features=log2, regressor__n_estimators=200;, score=-155.557 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=50;, score=-135.251 total time=   0.3s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=50;, score=-133.426 total time=   0.3s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=50;, score=-137.889 total time=   0.3s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=100;, score=-135.331 total time=   0.7s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=100;, score=-133.427 total time=   0.7s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=100;, score=-137.992 total time=   0.7s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=200;, score=-135.336 total time=   1.3s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=200;, score=-133.462 total time=   1.3s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=None, regressor__n_estimators=200;, score=-137.978 total time=   1.3s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-138.970 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-137.603 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-145.002 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-139.641 total time=   0.2s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-137.995 total time=   0.2s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-144.900 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-140.044 total time=   0.3s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-138.049 total time=   0.3s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-145.412 total time=   0.3s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=50;, score=-142.744 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=50;, score=-140.586 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=50;, score=-148.568 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=100;, score=-143.568 total time=   0.2s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=100;, score=-140.638 total time=   0.2s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=100;, score=-148.770 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=200;, score=-142.949 total time=   0.3s\n",
      "[CV 2/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=200;, score=-140.849 total time=   0.3s\n",
      "[CV 3/3] END regressor__max_depth=2, regressor__max_features=log2, regressor__n_estimators=200;, score=-147.852 total time=   0.3s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=50;, score=-123.496 total time=   0.5s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=50;, score=-121.001 total time=   0.5s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=50;, score=-128.355 total time=   0.5s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=100;, score=-123.621 total time=   0.9s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=100;, score=-120.954 total time=   0.9s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=100;, score=-128.617 total time=   0.9s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=200;, score=-123.554 total time=   1.8s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=200;, score=-121.031 total time=   1.8s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=None, regressor__n_estimators=200;, score=-128.423 total time=   1.8s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-130.894 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-130.273 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=50;, score=-137.189 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-132.136 total time=   0.2s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-130.067 total time=   0.2s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=100;, score=-137.819 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-132.656 total time=   0.5s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-130.605 total time=   0.4s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=sqrt, regressor__n_estimators=200;, score=-138.617 total time=   0.4s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=50;, score=-137.219 total time=   0.1s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=50;, score=-132.625 total time=   0.1s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=50;, score=-143.346 total time=   0.1s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=100;, score=-137.874 total time=   0.2s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=100;, score=-133.374 total time=   0.2s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=100;, score=-143.072 total time=   0.2s\n",
      "[CV 1/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=200;, score=-136.860 total time=   0.4s\n",
      "[CV 2/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=200;, score=-133.800 total time=   0.4s\n",
      "[CV 3/3] END regressor__max_depth=3, regressor__max_features=log2, regressor__n_estimators=200;, score=-141.930 total time=   0.4s\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=3,\n",
       "             estimator=Pipeline(steps=[(&#x27;preprocessor&#x27;,\n",
       "                                        ColumnTransformer(transformers=[(&#x27;num&#x27;,\n",
       "                                                                         Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                                          SimpleImputer(strategy=&#x27;median&#x27;)),\n",
       "                                                                                         (&#x27;scaler&#x27;,\n",
       "                                                                                          StandardScaler())]),\n",
       "                                                                         [&#x27;Year&#x27;,\n",
       "                                                                          &#x27;Y_lat&#x27;,\n",
       "                                                                          &#x27;X_lon&#x27;]),\n",
       "                                                                        (&#x27;cat&#x27;,\n",
       "                                                                         Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                                          SimpleImputer(strategy=&#x27;most_frequent&#x27;)),\n",
       "                                                                                         (&#x27;onehot&#x27;,\n",
       "                                                                                          OneHotEncoder(handle_unknown=&#x27;ignore&#x27;))]),\n",
       "                                                                         [&#x27;LocationAbbr&#x27;,\n",
       "                                                                          &#x27;GeographicLevel&#x27;,\n",
       "                                                                          &#x27;Sex&#x27;,\n",
       "                                                                          &#x27;ethnicity&#x27;])])),\n",
       "                                       (&#x27;regressor&#x27;,\n",
       "                                        RandomForestRegressor(random_state=42))]),\n",
       "             param_grid={&#x27;regressor__max_depth&#x27;: [None, 1, 2, 3],\n",
       "                         &#x27;regressor__max_features&#x27;: [None, &#x27;sqrt&#x27;, &#x27;log2&#x27;],\n",
       "                         &#x27;regressor__n_estimators&#x27;: [50, 100, 200]},\n",
       "             scoring=&#x27;neg_root_mean_squared_error&#x27;, verbose=3)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" ><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GridSearchCV</label><div class=\"sk-toggleable__content\"><pre>GridSearchCV(cv=3,\n",
       "             estimator=Pipeline(steps=[(&#x27;preprocessor&#x27;,\n",
       "                                        ColumnTransformer(transformers=[(&#x27;num&#x27;,\n",
       "                                                                         Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                                          SimpleImputer(strategy=&#x27;median&#x27;)),\n",
       "                                                                                         (&#x27;scaler&#x27;,\n",
       "                                                                                          StandardScaler())]),\n",
       "                                                                         [&#x27;Year&#x27;,\n",
       "                                                                          &#x27;Y_lat&#x27;,\n",
       "                                                                          &#x27;X_lon&#x27;]),\n",
       "                                                                        (&#x27;cat&#x27;,\n",
       "                                                                         Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                                          SimpleImputer(strategy=&#x27;most_frequent&#x27;)),\n",
       "                                                                                         (&#x27;onehot&#x27;,\n",
       "                                                                                          OneHotEncoder(handle_unknown=&#x27;ignore&#x27;))]),\n",
       "                                                                         [&#x27;LocationAbbr&#x27;,\n",
       "                                                                          &#x27;GeographicLevel&#x27;,\n",
       "                                                                          &#x27;Sex&#x27;,\n",
       "                                                                          &#x27;ethnicity&#x27;])])),\n",
       "                                       (&#x27;regressor&#x27;,\n",
       "                                        RandomForestRegressor(random_state=42))]),\n",
       "             param_grid={&#x27;regressor__max_depth&#x27;: [None, 1, 2, 3],\n",
       "                         &#x27;regressor__max_features&#x27;: [None, &#x27;sqrt&#x27;, &#x27;log2&#x27;],\n",
       "                         &#x27;regressor__n_estimators&#x27;: [50, 100, 200]},\n",
       "             scoring=&#x27;neg_root_mean_squared_error&#x27;, verbose=3)</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: Pipeline</label><div class=\"sk-toggleable__content\"><pre>Pipeline(steps=[(&#x27;preprocessor&#x27;,\n",
       "                 ColumnTransformer(transformers=[(&#x27;num&#x27;,\n",
       "                                                  Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                   SimpleImputer(strategy=&#x27;median&#x27;)),\n",
       "                                                                  (&#x27;scaler&#x27;,\n",
       "                                                                   StandardScaler())]),\n",
       "                                                  [&#x27;Year&#x27;, &#x27;Y_lat&#x27;, &#x27;X_lon&#x27;]),\n",
       "                                                 (&#x27;cat&#x27;,\n",
       "                                                  Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                                   SimpleImputer(strategy=&#x27;most_frequent&#x27;)),\n",
       "                                                                  (&#x27;onehot&#x27;,\n",
       "                                                                   OneHotEncoder(handle_unknown=&#x27;ignore&#x27;))]),\n",
       "                                                  [&#x27;LocationAbbr&#x27;,\n",
       "                                                   &#x27;GeographicLevel&#x27;, &#x27;Sex&#x27;,\n",
       "                                                   &#x27;ethnicity&#x27;])])),\n",
       "                (&#x27;regressor&#x27;, RandomForestRegressor(random_state=42))])</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-serial\"><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">preprocessor: ColumnTransformer</label><div class=\"sk-toggleable__content\"><pre>ColumnTransformer(transformers=[(&#x27;num&#x27;,\n",
       "                                 Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                  SimpleImputer(strategy=&#x27;median&#x27;)),\n",
       "                                                 (&#x27;scaler&#x27;, StandardScaler())]),\n",
       "                                 [&#x27;Year&#x27;, &#x27;Y_lat&#x27;, &#x27;X_lon&#x27;]),\n",
       "                                (&#x27;cat&#x27;,\n",
       "                                 Pipeline(steps=[(&#x27;imputer&#x27;,\n",
       "                                                  SimpleImputer(strategy=&#x27;most_frequent&#x27;)),\n",
       "                                                 (&#x27;onehot&#x27;,\n",
       "                                                  OneHotEncoder(handle_unknown=&#x27;ignore&#x27;))]),\n",
       "                                 [&#x27;LocationAbbr&#x27;, &#x27;GeographicLevel&#x27;, &#x27;Sex&#x27;,\n",
       "                                  &#x27;ethnicity&#x27;])])</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" ><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">num</label><div class=\"sk-toggleable__content\"><pre>[&#x27;Year&#x27;, &#x27;Y_lat&#x27;, &#x27;X_lon&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-5\" type=\"checkbox\" ><label for=\"sk-estimator-id-5\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SimpleImputer</label><div class=\"sk-toggleable__content\"><pre>SimpleImputer(strategy=&#x27;median&#x27;)</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" ><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">StandardScaler</label><div class=\"sk-toggleable__content\"><pre>StandardScaler()</pre></div></div></div></div></div></div></div></div><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-7\" type=\"checkbox\" ><label for=\"sk-estimator-id-7\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">cat</label><div class=\"sk-toggleable__content\"><pre>[&#x27;LocationAbbr&#x27;, &#x27;GeographicLevel&#x27;, &#x27;Sex&#x27;, &#x27;ethnicity&#x27;]</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-8\" type=\"checkbox\" ><label for=\"sk-estimator-id-8\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SimpleImputer</label><div class=\"sk-toggleable__content\"><pre>SimpleImputer(strategy=&#x27;most_frequent&#x27;)</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-9\" type=\"checkbox\" ><label for=\"sk-estimator-id-9\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">OneHotEncoder</label><div class=\"sk-toggleable__content\"><pre>OneHotEncoder(handle_unknown=&#x27;ignore&#x27;)</pre></div></div></div></div></div></div></div></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-10\" type=\"checkbox\" ><label for=\"sk-estimator-id-10\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestRegressor</label><div class=\"sk-toggleable__content\"><pre>RandomForestRegressor(random_state=42)</pre></div></div></div></div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "GridSearchCV(cv=3,\n",
       "             estimator=Pipeline(steps=[('preprocessor',\n",
       "                                        ColumnTransformer(transformers=[('num',\n",
       "                                                                         Pipeline(steps=[('imputer',\n",
       "                                                                                          SimpleImputer(strategy='median')),\n",
       "                                                                                         ('scaler',\n",
       "                                                                                          StandardScaler())]),\n",
       "                                                                         ['Year',\n",
       "                                                                          'Y_lat',\n",
       "                                                                          'X_lon']),\n",
       "                                                                        ('cat',\n",
       "                                                                         Pipeline(steps=[('imputer',\n",
       "                                                                                          SimpleImputer(strategy='most_frequent')),\n",
       "                                                                                         ('onehot',\n",
       "                                                                                          OneHotEncoder(handle_unknown='ignore'))]),\n",
       "                                                                         ['LocationAbbr',\n",
       "                                                                          'GeographicLevel',\n",
       "                                                                          'Sex',\n",
       "                                                                          'ethnicity'])])),\n",
       "                                       ('regressor',\n",
       "                                        RandomForestRegressor(random_state=42))]),\n",
       "             param_grid={'regressor__max_depth': [None, 1, 2, 3],\n",
       "                         'regressor__max_features': [None, 'sqrt', 'log2'],\n",
       "                         'regressor__n_estimators': [50, 100, 200]},\n",
       "             scoring='neg_root_mean_squared_error', verbose=3)"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_hat_train = model.predict(X_train)\n",
    "y_hat_test = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "776.5474802171799\n",
      "6099.035328371916\n",
      "{'regressor__max_depth': None, 'regressor__max_features': None, 'regressor__n_estimators': 200}\n"
     ]
    }
   ],
   "source": [
    "train_mse = mean_squared_error(y_train, y_hat_train)\n",
    "test_mse = mean_squared_error(y_test, y_hat_test)\n",
    "\n",
    "print(train_mse)\n",
    "print(test_mse)\n",
    "print(model.best_params_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

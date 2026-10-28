# California Housing Price Prediction Using Regression

## 1. Project Overview

The California Housing Price Prediction project is a machine learning project that predicts the median house value in California using housing-related information. The project uses the California Housing dataset, which contains features such as median income, house age, number of rooms, number of bedrooms, population, household size, geographical location, and ocean proximity.

The project applies three regression algorithms: Ordinary Least Squares (OLS), Ridge Regression, and Lasso Regression. Their performance is compared using RMSE, MAE, and R² scores to identify the most suitable model for predicting house prices.

## 2. Objectives

- Predict median house values using machine learning regression techniques.
- Handle missing values using appropriate imputation methods.
- Analyze relationships between numerical features using a correlation heatmap.
- Create interaction features to capture relationships between variables.
- Encode categorical variables and standardize numerical features.
- Analyze multicollinearity using correlation analysis and Variance Inflation Factor (VIF).
- Tune Ridge and Lasso models using GridSearchCV.
- Compare model performance using RMSE, MAE, and R².
- Visualize predicted versus actual values and residual error distributions.

## 3. Technologies Used

- Programming Language: Python
- Development Environment: Jupyter Notebook / Visual Studio Code
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn and Joblib
- Dataset: California Housing dataset
- Machine Learning Algorithms: OLS, Ridge Regression and Lasso Regression
- Hyperparameter Tuning: GridSearchCV

## 4. Project Workflow

### Step 1: Data Loading
Load the California Housing dataset from the `data/raw/housing.csv` file using Pandas.

### Step 2: Data Preprocessing
Inspect the dataset, identify missing values, and handle them using suitable imputation techniques. Separate the input features from the target variable, `median_house_value`.

### Step 3: Exploratory Data Analysis
Analyze the dataset using descriptive statistics and a correlation heatmap to understand relationships between numerical features.

### Step 4: Feature Engineering
Create interaction features from selected variables to capture additional relationships that may improve prediction performance.

### Step 5: Data Transformation
Standardize numerical features and encode categorical features, such as `ocean_proximity`, using suitable preprocessing techniques.

### Step 6: Multicollinearity Analysis
Use correlation analysis and Variance Inflation Factor (VIF) to identify highly correlated input features. Apply suitable feature-handling techniques where necessary.

### Step 7: Model Training
Train three regression models:

1. **OLS Regression:** Estimates coefficients by minimizing the sum of squared prediction errors.
2. **Ridge Regression:** Uses L2 regularization to reduce the impact of large coefficients.
3. **Lasso Regression:** Uses L1 regularization and can reduce some coefficients to zero.

### Step 8: Hyperparameter Tuning
Use GridSearchCV with five-fold cross-validation to identify suitable alpha values for Ridge and Lasso regression.

### Step 9: Model Evaluation
Evaluate the models using the following metrics:

- **RMSE:** Measures prediction error while penalizing larger errors more strongly.
- **MAE:** Measures the average absolute difference between actual and predicted house values.
- **R² Score:** Measures how much variation in the target variable is explained by the model.

Lower RMSE and MAE values indicate better predictions, while a higher R² score generally indicates a better fit.

### Step 10: Visualization and Model Saving
Generate predicted-versus-actual plots and residual distribution plots. Save the model comparison results and the selected trained model in the `artifacts` directory.

## 5. Project Folder Structure

```text
california-housing-regression/
│
├── data/
│   └── raw/
│       └── housing.csv
│
├── notebooks/
│   └── california_housing_regression.ipynb
│
├── src/
│   ├── __init__.py
│   └── housing_features.py
│
├── artifacts/
│   ├── best_model.joblib
│   └── model_comparison.csv
│
├── requirements.txt
└── README.md
```

## 6. Steps to Run the Project

### Prerequisites

Install Python 3.10 or a compatible version supported by the project's dependencies, Visual Studio Code, and the Jupyter extension.

### Step 1: Download and Extract
Download the project ZIP file and extract it to a folder on your computer.

### Step 2: Open the Project
Open Visual Studio Code, select **File → Open Folder**, and choose the extracted `california-housing-regression` folder.

### Step 3: Open the Terminal
In Visual Studio Code, select **Terminal → New Terminal**.

### Step 4: Create a Virtual Environment

Run the following command:

```powershell
python -m venv .venv
```

### Step 5: Activate the Virtual Environment

For Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 6: Install Required Libraries

Run:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Wait until the installation is complete.

### Step 7: Install the Jupyter Extension
Open the Extensions panel in VS Code using `Ctrl + Shift + X`. Search for **Jupyter** and install the extension published by Microsoft.

### Step 8: Open the Notebook
Open the following file from the VS Code Explorer:

```text
notebooks/california_housing_regression.ipynb
```

### Step 9: Select the Python Kernel
Click **Select Kernel** in the notebook toolbar and choose the Python interpreter from the project's `.venv` environment.

### Step 10: Execute the Notebook
Click **Run All** to execute all notebook cells from beginning to end. Wait for preprocessing, model training, hyperparameter tuning, evaluation, and visualization to finish.

### Step 11: View the Results
Review the model comparison table containing RMSE, MAE, and R² scores. Examine the correlation heatmap, predicted-versus-actual plots, and residual distributions.

### Step 12: Check the Output Files
After successful execution, check the `artifacts` folder for the saved model and model comparison CSV, as configured in the notebook.

## 7. Expected Output

The project produces:

- A comparison of OLS, Ridge, and Lasso regression models.
- RMSE, MAE, and R² evaluation scores.
- A correlation heatmap for numerical features.
- Multicollinearity diagnostics using VIF.
- Predicted-versus-actual plots.
- Residual distribution plots.
- A saved trained model and model comparison CSV.

The model with the lowest RMSE and MAE and a comparatively high R² score can be considered the best-performing model on the evaluation data.

## 8. Conclusion

The California Housing Price Prediction project demonstrates how regression algorithms can be used to estimate house values using housing and geographical attributes. Data preprocessing, feature engineering, multicollinearity analysis, and hyperparameter tuning help create a systematic machine learning workflow. Comparing OLS, Ridge, and Lasso regression using multiple evaluation metrics helps determine which model performs best on the test dataset.

The project also demonstrates the importance of data visualization and model evaluation in understanding prediction errors and assessing regression performance.
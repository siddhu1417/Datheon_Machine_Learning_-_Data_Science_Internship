
# Telecom Customer Churn Prediction Using Ensemble Machine Learning

## 1. Project Overview

This project predicts whether a telecom customer is likely to leave a service provider using machine learning. It uses customer subscription details, contract information, tenure, monthly charges, and other features to identify potential customer churn.

The project trains and compares two machine learning models: Random Forest and XGBoost. Their performance is evaluated using ROC-AUC, accuracy, confusion matrices, and classification reports.

## 2. Project Objectives

- Predict customer churn using historical telecom data.
- Clean and preprocess customer records.
- Encode categorical features using OneHotEncoder.
- Handle class imbalance using class weighting.
- Train and compare Random Forest and XGBoost.
- Evaluate model performance using cross-validation and ROC-AUC.
- Identify the top 10 important features influencing predictions.

## 3. Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost

## 4. Project Structure

```text
Telecom-Customer-Churn/
│
├── Telecom_Customer_Churn_Ready_To_Run.ipynb
├── Telco-Customer-Churn.csv
├── requirements.txt
├── README.md
│
├── cross_validation_results.csv
├── test_metrics.csv
└── feature_importances.csv
```

The three result CSV files are generated after running the relevant notebook cells.

## 5. Dataset Description

The project uses the Telco Customer Churn dataset.

It contains information about:
- Customer demographics
- Tenure and contract type
- Internet and phone services
- Monthly and total charges
- Payment methods
- Customer churn status

The `Churn` column is the target variable:
- `Yes` = Customer left the service.
- `No` = Customer stayed with the service.

The `customerID` column is excluded from model training because it is an identifier rather than a useful generalizable predictor.

## 6. Installation Requirements

Install Python 3.10 or newer.

Check your Python installation:

```bash
python --version
```

If Python is not installed, download it from:
https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH**.

## 7. How to Run the Project on Windows

### Step 1: Extract the project

Extract the downloaded ZIP file into a folder.

Make sure the notebook and `Telco-Customer-Churn.csv` are available in the project folder.

### Step 2: Open the project folder in a terminal

Open the extracted folder in File Explorer.

Click the address bar, type `cmd`, and press Enter.

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install the required libraries

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The project uses class weighting instead of SMOTE, so `imbalanced-learn` is not required.

### Step 6: Launch Jupyter Notebook

```bash
jupyter notebook
```

Your browser should open the Jupyter interface.

### Step 7: Open the notebook

Open:

`Telecom_Customer_Churn_Ready_To_Run.ipynb`

### Step 8: Execute the notebook

Select **Kernel → Restart Kernel and Run All Cells**, or run each cell from top to bottom.

Wait for the training and evaluation cells to finish.

## 8. Machine Learning Workflow

### Data Preprocessing

- Converts `TotalCharges` to numeric values.
- Handles missing values using imputation.
- Removes the customer identifier from model features.
- Encodes categorical features using OneHotEncoder.
- Splits data into training and testing sets.

### Class Imbalance Handling

The dataset may contain more customers who stay than customers who leave.

The project uses class weighting to give greater importance to the minority class during training.

- Random Forest uses `class_weight="balanced"`.
- XGBoost uses `scale_pos_weight`.

### Model Training

**Random Forest:** Combines predictions from multiple decision trees to classify customer churn.

**XGBoost:** Builds boosted decision trees sequentially, improving the model by learning from errors made by earlier trees.

Both models are evaluated using stratified 5-fold cross-validation on the training data.

## 9. Model Evaluation

The notebook generates the following outputs:

### ROC Curve and ROC-AUC

The ROC curve compares the true-positive rate with the false-positive rate at different classification thresholds.

ROC-AUC measures how well the model distinguishes between customers who churn and those who stay.

The project target is ROC-AUC greater than 0.80. This is a target, not a guaranteed result.

### Confusion Matrix

The confusion matrix displays:
- True positives: Churners correctly identified.
- True negatives: Customers who stay correctly identified.
- False positives: Customers incorrectly predicted to churn.
- False negatives: Churners missed by the model.

### Classification Report

Shows precision, recall, F1-score, and support for each class.

### Feature Importance

Displays the top 10 features that contribute most to the selected tree-based model's predictions.

## 10. Output Files

After running the relevant notebook cells, the project generates:

- `cross_validation_results.csv` — cross-validation performance.
- `test_metrics.csv` — test-set ROC-AUC and accuracy.
- `feature_importances.csv` — feature importance values.

The notebook also displays ROC curves, confusion matrices, and a feature importance bar chart.

## 11. Expected Outcome

The completed project should:
- Train Random Forest and XGBoost models.
- Compare their performance.
- Display ROC-AUC curves and confusion matrices.
- Identify the best-performing model on the held-out test set.
- Highlight the top 10 important features.

Actual model scores must be obtained by executing the notebook.

## 12. Applications

- Telecom customer retention
- Churn risk analysis
- Customer relationship management
- Data-driven marketing campaigns
- Customer subscription analysis

## 13. Conclusion

This project demonstrates how ensemble machine learning techniques can be used to predict telecom customer churn. By comparing Random Forest and XGBoost and analyzing important customer features, businesses can better understand churn patterns and develop customer retention strategies.

## 14. Author

Developed as a machine learning project for customer churn prediction.

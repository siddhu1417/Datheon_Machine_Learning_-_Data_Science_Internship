# Iris Classification Project

## 1. Project Explanation

The Iris Classification Project is a machine learning project that classifies Iris flowers into three species: Setosa, Versicolor, and Virginica. It uses the Iris dataset, which contains four numerical features: sepal length, sepal width, petal length, and petal width.

The project uses machine learning algorithms such as Logistic Regression and Decision Tree to train classification models and predict the species of Iris flowers. The models are evaluated using accuracy, precision, recall, F1-score, classification reports, and confusion matrix heatmaps.

**Objective:** To build and evaluate machine learning classification models that accurately predict the species of Iris flowers based on their measurements.

## 2. Technologies Used

- Programming Language: Python
- Environment: Jupyter Notebook
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, and Seaborn
- Dataset: Iris Flower Dataset
- Algorithms: Logistic Regression and Decision Tree

## 3. Step-by-Step Process to Run the Project

### Step 1: Download the Project

Download the complete project ZIP file and extract it to a folder on your computer.

### Step 2: Open the Project

Open the extracted `iris_classification_project` folder in Visual Studio Code or navigate to it using Command Prompt.

### Step 3: Install Python

Ensure that Python is installed on your computer. Check the installation by running:

```bash
python --version
```

### Step 4: Install Required Libraries

Open the terminal and execute the following command:

```bash
python -m pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

### Step 5: Start Jupyter Notebook

Run the following command in the terminal:

```bash
python -m notebook
```

Jupyter Notebook will open in your browser.

### Step 6: Open the Notebook

Open the file:

`iris_classification_evaluation.ipynb`

Select the appropriate Python kernel.

### Step 7: Execute the Notebook

Run all notebook cells using **Kernel → Restart & Run All**.

The notebook will load the dataset, explore the data, preprocess the features, train the classification models, and evaluate their performance.

### Step 8: View the Results

After execution, the notebook displays:

- Dataset information and exploratory data analysis
- Classification reports for each model
- Accuracy, precision, recall, and F1-score
- Confusion matrix heatmaps
- A comparison of model performance

## 4. Expected Output

The project generates classification reports and confusion matrix heatmaps for Logistic Regression and Decision Tree models. These outputs help evaluate how accurately each model classifies the three Iris flower species and identify incorrect predictions.

## 5. Conclusion

The Iris Classification Project demonstrates the application of supervised machine learning to a multiclass classification problem. It provides a practical understanding of data preprocessing, model training, performance evaluation, and confusion matrix visualization. The results can be used to compare classification algorithms and determine which model performs better on the test dataset.
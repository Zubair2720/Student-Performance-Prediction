# Student Performance Prediction

## Project Overview
Student Performance Prediction is a Machine Learning project that predicts whether a student will pass or fail based on factors such as study hours, attendance, past exam scores, gender, internet access at home, extracurricular activities, and parental education level.

The project uses Python, data analysis libraries, and classification algorithms to analyze student data and build a predictive model.

## Objectives
- Analyze student performance data using Exploratory Data Analysis (EDA).
- Clean and preprocess the dataset.
- Visualize numerical features and their correlations.
- Train and compare different Machine Learning classification models.
- Evaluate model performance using Accuracy and F1-score.
- Save the trained Support Vector Classifier (SVC) model for future predictions.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib

## Dataset
The project uses `student_performance_dataset.csv`.

### Features
- `Gender`
- `Study_Hours_per_Week`
- `Attendance_Rate`
- `Past_Exam_Scores`
- `Internet_Access_at_Home`
- `Extracurricular_Activities`
- `Parental_Education_Level`

### Target Variable
- `Pass_Fail`

The target variable contains two classes:
- `Pass` — 1
- `Fail` — 0

The `Student_ID` and `Final_Exam_Score` columns are removed before training.

## Project Workflow

### 1. Exploratory Data Analysis (EDA)
- Checked dataset dimensions and data types.
- Examined statistical summaries.
- Checked missing values.
- Visualized numerical features using histograms.
- Analyzed correlations using a heatmap.

### 2. Data Cleaning
- Removed duplicate records.
- Removed unnecessary columns.

### 3. Data Preprocessing
- Encoded categorical values into numerical values.
- Applied one-hot encoding to `Parental_Education_Level`.
- Converted dataset columns to integer types before scaling.

### 4. Feature Scaling
Used `StandardScaler` to scale the following numerical features:
- `Study_Hours_per_Week`
- `Attendance_Rate`
- `Past_Exam_Scores`

### 5. Train-Test Split
The dataset was split into:
- 80% training data
- 20% testing data

The split uses `random_state=42` for reproducibility.

### 6. Machine Learning Models
The following classification algorithms were used:

- Logistic Regression
- Decision Tree Classifier
- Gaussian Naive Bayes
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Random Forest Classifier
- AdaBoost Classifier
- Gradient Boosting Classifier
- XGBoost Classifier

### 7. Model Evaluation
Models are evaluated using:
- Accuracy Score
- F1-score

The SVC model is saved for future use.

## Model Saving
The trained SVC model and preprocessing information are saved in:

`student_model.pkl`

The file contains:
- Trained SVC model
- Fitted StandardScaler
- Feature column names

Joblib is used to save the model and associated information.

## Installation

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib xgboost
```

## How to Run
1. Clone or download this project.
2. Place `student_performance_dataset.csv` in the project directory.
3. Open the Jupyter Notebook or Python environment.
4. Run the notebook cells in sequence.
5. Train and evaluate the classification models.
6. Generate the `student_model.pkl` file.

## Future Improvements
- Build a Streamlit web application for predictions.
- Add a user-friendly interface for entering student information.
- Compare models using additional evaluation metrics.
- Improve model performance through hyperparameter tuning.
- Implement a prediction function that loads the saved model and scaler.

## Conclusion
This project demonstrates the complete Machine Learning workflow, from data exploration and preprocessing to model training, evaluation, and saving a trained model. It provides a foundation for predicting student pass/fail outcomes using academic and personal study-related features.

## Author
Machine Learning Project — Student Performance Prediction

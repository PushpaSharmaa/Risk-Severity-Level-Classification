🔍 Risk Severity Level Classification

This project focuses on predicting the severity level of incidents (CRITICAL, HIGH, MEDIUM, LOW) based on their short descriptions.
It uses machine learning models with hyperparameter tuning and compares multiple classifiers to identify the best-performing one.


📌 Objective

To build an automated classification system that processes incident text data, applies TF-IDF feature extraction, trains multiple models, evaluates performance metrics, and saves the best model for deployment or future use.


📂 Dataset

The project combines multiple CSV datasets containing enriched incident reports:
Key Columns:
	•	short_description → Incident description (text)
	•	severity → Target variable (CRITICAL, HIGH, MEDIUM, LOW)


 ⚙️ Workflow
	1.	Data Loading & Preprocessing
	•	Combines multiple CSV files
	•	Removes rows with missing values
 
	2.	Feature Engineering
	•	Applies TF-IDF Vectorization to convert text into numerical features
 
	3.	Model Training & Hyperparameter Tuning
	•	Models Used:
	•	Multinomial Naive Bayes
	•	Logistic Regression
	•	Random Forest
	•	Support Vector Classifier (SVC)
	•	Gradient Boosting
 
	4.	Evaluation
	•	Accuracy, Precision, Recall, F1-Score
	•	Confusion Matrices
	•	Class Distribution Visualization
 
	5.	Model Selection & Saving
	•	Saves best model (best_model.pkl) and TF-IDF vectorizer (tfidf.pkl)
	•	Exports performance metrics to model_scores.csv


 📊 Visualizations
	•	Severity distribution bar charts
	•	Confusion matrix heatmaps
	•	Comparison of model performance (Accuracy, Precision, Recall, F1)


 🛠️ Tech Stack
Python
pandas, numpy: Data manipulation
matplotlib, seaborn: Visualizations
scikit-learn: ML models, hyperparameter tuning, evaluation
joblib: Model serialization

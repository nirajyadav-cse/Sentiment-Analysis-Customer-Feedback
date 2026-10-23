# Project Report: Sentiment Analysis for Customer Feedback

## 1. Title
Sentiment Analysis for Customer Feedback using Artificial Intelligence

## 2. Abstract
Organizations receive customer feedback through reviews, surveys, and support messages. Reading every message manually can take considerable time. This project demonstrates a text-classification system that categorizes feedback into positive, negative, or neutral sentiment. It uses Natural Language Processing (NLP), TF-IDF feature extraction, and a Logistic Regression classifier. A Streamlit dashboard allows a user to enter feedback, view the predicted category, and inspect the distribution of labels in the sample dataset.

## 3. Problem Statement
A company receives a large volume of customer feedback and wants to understand the sentiments expressed in that feedback. The goal is to develop a system that automatically classifies feedback as positive, negative, or neutral and presents basic sentiment trends.

## 4. Objectives
1. Prepare and inspect labeled customer feedback.
2. Convert text into machine-readable features.
3. Train a supervised machine-learning model.
4. Classify new customer feedback.
5. Visualize sentiment distribution through a dashboard.

## 5. Scope
The prototype covers English text, three sentiment classes, offline model training, single-review predictions, and a basic dashboard. It does not yet connect to live customer databases or continuously retrain itself.

## 6. Tools and Technologies
- Python: implementation language.
- pandas: loading and handling the dataset.
- scikit-learn: train/test split, TF-IDF, Logistic Regression, and accuracy calculation.
- Streamlit: interactive web dashboard.
- Matplotlib: charting support.

## 7. Methodology
### Step 1: Data collection
A small example CSV dataset is included. Each row contains a feedback sentence and a sentiment label. For a real deployment, the company should use representative feedback with reliable human-assigned labels and appropriate privacy permissions.

### Step 2: Preprocessing and feature extraction
The text is lowercased and English stop words are removed by the TF-IDF vectorizer. TF-IDF assigns numerical weights to words and word pairs based on their usefulness in the documents.

### Step 3: Dataset split
The dataset is divided into training and testing portions using a fixed random seed and stratification so that the class proportions are approximately preserved.

### Step 4: Model training
A Logistic Regression classifier learns patterns from the TF-IDF features and known labels.

### Step 5: Evaluation
Accuracy is calculated on the held-out test set. Because the sample dataset is small and illustrative, this value is not a reliable estimate of performance on real customer feedback. A stronger evaluation should also report precision, recall, F1-score, and a confusion matrix on a larger test set.

### Step 6: Dashboard
The Streamlit application accepts a review, displays the predicted sentiment and model score chart, and visualizes the sample dataset's sentiment distribution.

## 8. System Architecture
Customer Feedback CSV / User Input → Text Processing and TF-IDF → Logistic Regression Classifier → Sentiment Label → Streamlit Dashboard and Visualizations.

## 9. Expected Output
For an input such as “The product is excellent and works perfectly,” the system is expected to predict positive sentiment. For “The item arrived broken,” it is expected to predict negative sentiment. Neutral examples should express factual or mixed/ordinary information without clear positive or negative wording. Predictions depend on the training data and can be wrong.

## 10. Results and Discussion
The application trains a model when launched and reports test accuracy on the included sample data. It displays the predicted class for a user-entered sentence and shows the sentiment distribution of the dataset. Since the dataset is intentionally small, the result is suitable for demonstrating the workflow, not for making business decisions. The final report should include a screenshot of the running dashboard and the actual accuracy shown by the app after you run it; do not invent or manually claim a result that has not been measured.

## 11. Limitations
- Small illustrative dataset.
- English-only examples.
- Sarcasm, slang, spelling mistakes, and context may confuse the model.
- Scores are model outputs and are not guaranteed to be calibrated confidence.
- No live customer-system integration or automatic data refresh.

## 12. Future Enhancements
- Collect a larger, diverse, permissioned dataset.
- Compare Logistic Regression with Naive Bayes and transformer-based models.
- Add precision, recall, F1-score, and a confusion matrix.
- Include time-based trend charts and filters by product.
- Add database storage, user authentication, and deployment.

## 13. Conclusion
This project demonstrates an end-to-end introductory AI workflow for customer-feedback sentiment analysis. Text is transformed into TF-IDF features, classified using Logistic Regression, and presented through a Streamlit dashboard. With a larger and carefully labeled dataset, more comprehensive evaluation, and appropriate privacy controls, the prototype could be extended toward a more useful business tool.

## 14. References
1. scikit-learn documentation: https://scikit-learn.org/
2. Streamlit documentation: https://docs.streamlit.io/
3. pandas documentation: https://pandas.pydata.org/docs/
4. Jurafsky, D. and Martin, J. H., Speech and Language Processing (online draft): https://web.stanford.edu/~jurafsky/slp3/

## Submission checklist
- Add student name, department, year, university, faculty name, and date to the cover page if required.
- Run the app and capture a genuine screenshot.
- Explain the workflow and limitations in your own words.
- Confirm your course's rules about AI assistance and cite assistance if required.

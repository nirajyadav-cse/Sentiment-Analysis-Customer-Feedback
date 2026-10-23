# Customer Feedback Sentiment Analysis

A beginner-friendly Artificial Intelligence project that classifies customer feedback as **positive**, **negative**, or **neutral** using Natural Language Processing (NLP) and machine learning. It includes a Streamlit dashboard for interactive predictions and visualizing the sample dataset.

## Objectives
- Prepare and inspect labeled customer feedback.
- Convert text into numerical features with TF-IDF.
- Train a Logistic Regression classifier.
- Predict sentiment for new feedback.
- Display a sentiment distribution dashboard.

## Tech stack
Python, pandas, scikit-learn, TF-IDF, Logistic Regression, Streamlit, Matplotlib.

## Project structure
```text
sentiment_analysis_project/
├── app.py
├── model.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── data/
    └── customer_feedback.csv
```

## Run locally
1. Install Python 3.10 or later.
2. Open Terminal in this project folder.
3. Create and activate a virtual environment (recommended):
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
4. Install packages: `pip install -r requirements.txt`
5. Launch the dashboard: `streamlit run app.py`
6. Open the local URL printed by Streamlit in your browser.

## How it works
1. `customer_feedback.csv` contains example feedback and labels.
2. `TfidfVectorizer` represents words and word pairs as numeric features.
3. Logistic Regression learns patterns that distinguish the three labels.
4. The app shows a prediction and score chart for a new review.

## Important limitation
The included dataset is small and illustrative, so model accuracy is only a demonstration and should not be treated as a reliable real-world benchmark. Replace it with a larger, representative, human-labeled dataset before drawing business conclusions.

## Future improvements
- Add more real, permissioned feedback data.
- Report precision, recall, F1-score, and a confusion matrix.
- Support multiple languages and spelling variations.
- Add date/product filters and store results in a database.
- Deploy the app to Streamlit Community Cloud.

## Author
Student project — add your name, course, university, and submission date before submitting.

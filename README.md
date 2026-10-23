# Customer Feedback Sentiment Analysis

Hi! 👋 Welcome to my project.

I built this project to explore how Artificial Intelligence can help us understand what customers think about a product or service. Companies receive a lot of reviews every day, and reading them one by one can take time. This project uses Machine Learning and Natural Language Processing (NLP) to classify customer feedback as positive, negative, or neutral.

The project also includes a simple Streamlit dashboard where you can enter a review and see the model's prediction.

## What does this project do?

- Classifies customer reviews into positive, negative, or neutral categories.
- Uses TF-IDF to convert text into numerical features.
- Trains a Logistic Regression model to predict sentiment.
- Displays basic information about the dataset and model accuracy.
- Provides an interactive dashboard for testing new reviews.

## 🚀 Live Dashboard

Try the application here:

[**Open Live Sentiment Analysis Dashboard**](https://sentiment-analysis-customer-feedback-pqctsrvkmxexafyyadce2g.streamlit.app)

Explore customer feedback and view sentiment analysis results through the interactive dashboard.

---


  

## Technologies I used

- **Python** — to build the project
- **Pandas** — to load and manage the dataset
- **Scikit-learn** — to train and evaluate the machine learning model
- **TF-IDF** — to represent customer feedback as numerical features
- **Streamlit** — to build the dashboard
- **Matplotlib** — for data visualization support

## Project structure

```text
Sentiment-Analysis-Customer-Feedback/
├── app.py
├── model.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── data/
    └── customer_feedback.csv
```

## How to run the project

You can run the project on your computer by following these steps.

**1. Clone the repository**

```bash
git clone https://github.com/nirajyadav-cse/Sentiment-Analysis-Customer-Feedback.git
```

**2. Open the project folder**

```bash
cd Sentiment-Analysis-Customer-Feedback
```

**3. Create a virtual environment (recommended)**

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**4. Install the required libraries**

```bash
python3 -m pip install -r requirements.txt
```

**5. Start the dashboard**

```bash
python3 -m streamlit run app.py
```

Open the local URL shown in your terminal to use the application.

## Try it yourself

Enter a review in the dashboard and click **Analyze sentiment**.

For example:

- Positive: "The product is excellent and works perfectly."
- Negative: "The item arrived broken."
- Neutral: "The product has basic functions."

The model predicts a sentiment based on patterns learned from the training data.

## What I learned

While working on this project, I explored text preprocessing, TF-IDF feature extraction, supervised machine learning, model evaluation, and building a simple interactive dashboard with Streamlit. It also helped me understand how Python libraries can work together to create an end-to-end AI application.

## Limitations and future improvements

This project currently uses a small sample dataset created for learning and demonstration. Because of this, the model may not classify every review correctly, and its reported accuracy should not be treated as real-world performance.

In the future, I would like to:
- Train the model on a larger and more diverse dataset.
- Compare different machine learning algorithms.
- Improve evaluation using precision, recall, F1-score, and a confusion matrix.
- Add more detailed sentiment charts.
- Deploy the dashboard online so others can try it.

## About me

I'm Niraj Yadav, a B.Tech student in Computer Science and Engineering with a specialization in Artificial Intelligence and Machine Learning.

I'm learning by building practical projects and exploring how AI and machine learning can solve real-world problems.

Thanks for visiting my project! ⭐

If you have suggestions for improvement, feel free to share them.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from model import train_model

st.set_page_config(page_title="Customer Sentiment Dashboard", page_icon="💬", layout="wide")
st.title("💬 Customer Feedback Sentiment Analysis")
st.caption("NLP + TF-IDF + Logistic Regression | Educational demonstration")

DATA_PATH = Path(__file__).parent / "data" / "customer_feedback.csv"
data = pd.read_csv(DATA_PATH)
model, accuracy, X_test, y_test, y_pred = train_model(data)

c1, c2, c3 = st.columns(3)
c1.metric("Sample reviews", len(data))
c2.metric("Sentiment categories", data["sentiment"].nunique())
c3.metric("Test accuracy", f"{accuracy:.1%}")

st.subheader("Analyze a customer review")
review = st.text_area("Enter feedback", placeholder="Example: The product is great and easy to use.")
if st.button("Analyze sentiment", type="primary"):
    if review.strip():
        prediction = model.predict([review])[0]
        probabilities = model.predict_proba([review])[0]
        class_names = model.classes_
        st.success(f"Predicted sentiment: **{prediction.title()}**")
        st.write("Model confidence scores (not guaranteed probabilities of truth):")
        st.bar_chart(pd.DataFrame({"Score": probabilities}, index=class_names))
    else:
        st.warning("Please enter a review first.")

st.divider()
st.subheader("Sentiment distribution in sample dataset")
counts = data["sentiment"].value_counts().reindex(["positive", "neutral", "negative"], fill_value=0)
st.bar_chart(counts)
st.subheader("Sample feedback data")
st.dataframe(data, use_container_width=True)

st.info("This is a learning prototype trained on a small example dataset. Its predictions may be inaccurate on real-world feedback. For production use, train and evaluate it on a larger, representative, labeled dataset.")

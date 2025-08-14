import streamlit as st
import joblib
import os

from text_preprocessing import preprocess_text

MODEL_PATH = os.path.join(os.path.dirname(__file__), "spam_classifier_voting_model.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "tfidf_vectorizer.pkl")   

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

st.set_page_config(page_title="Spam Detector", page_icon="📧")
st.title("📧 Spam vs Ham Email Classifier")
st.write("Enter or paste any email message below to see if it's classified as **spam** or **ham**.")

with st.expander("📚 Try Sample Emails"):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Example Spam"):
            st.session_state['example'] = (
                "Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize now!"
            )
    with col2:
        if st.button("Example Ham"):
            st.session_state['example'] = (
                "Hi Alex, just confirming our lunch meeting at 12pm tomorrow. Let me know if anything changes."
            )

email_input = st.text_area("Enter Email Text:", height=200, value=st.session_state.get('example', ''))

if st.button("Predict"):
    if email_input.strip() == "":
        st.warning("⚠Please enter or select an email message.")
    else:
        cleaned_input = preprocess_text(email_input)
        transformed_input = vectorizer.transform([cleaned_input])
        prediction = model.predict(transformed_input)[0]
        proba = model.predict_proba(transformed_input)[0]

        st.markdown("---")
        st.subheader("Prediction Result")

        if prediction == "spam":
            st.markdown("## 🟥 **SPAM**")
            st.progress(int(proba[1] * 100))
            st.write(f"**Confidence (Spam):** {proba[1]:.2%}")
        else:
            st.markdown("## 🟩 **HAM**")
            st.progress(int(proba[0] * 100))
            st.write(f"**Confidence (Ham):** {proba[0]:.2%}")

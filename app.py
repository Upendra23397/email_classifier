import streamlit as st
import pickle


# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Load trained model
with open("model.pkl", "rb") as f:
    model= pickle.load(f)
st.title("Email/SMS Spam Classifier")
input_sms=st.text_area("Enter your message:")
#1.preprocess
#2.vectorize
#3.predict
#4.display
if st.button("Predict"):
    email_tfidf = tfidf.transform([input_sms])
    prediction = model.predict(email_tfidf)
    if prediction[0] == 1:
        st.success("This message is spam.")
    else:
        st.success("This message is not spam.")
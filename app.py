import streamlit as st
from main import graph

st.title("🚀 Zocket: URL Summarizer")

url = st.text_input("Enter a URL to summarize:")
if st.button("Summarize") and url:
    with st.spinner("Analyzing..."):
        result = graph.invoke({"url": url})
        st.subheader("🔍 Summary")
        st.write(result["summary"])
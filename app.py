# Important Libraries
import json
import streamlit as st
import pandas as pd 
import torch
import numpy as np  
from sentence_transformers import SentenceTransformer, util

# Load model 
@st.cache_resource
def load_model():
    return SentenceTransformer("multi-qa-mpnet-base-cos-v1")

model = load_model()

# Load Data
@st.cache_data
def load_data():
    # Reading Json File
    with open("C:\\Semantic Search FAQ Bot\\Ecommerce_FAQ_Chatbot_dataset.json", encoding="utf-8") as f:
        raw = json.load(f)
    data = pd.DataFrame(raw["questions"])
    data.reset_index(drop=True, inplace=True) 
    return data

data = load_data()

# Prepare corpus
corpus = data['question'].tolist()
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

# Streamlit UI
st.title("Semantic Search with SBERT")
st.write("Type a question and I’ll find the most similar result to help you")

query = st.text_input("Enter your question:")

if query:
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, corpus_embeddings)[0]

    top_results = torch.topk(scores, k=3)

    st.subheader("Top 3 Matches:")

    indices = top_results.indices.tolist()
    values = top_results.values.tolist()

    for idx, score in zip(indices, values):
        idx_safe = np.int64(idx) 
        score = float(score)
        
        st.write(f"**Question:** {data.iloc[idx_safe]['question']}") 
        st.write(f"**Answer:** {data.iloc[idx_safe]['answer']}")
        
        st.write(f"**Score:** {score:.4f}")
        st.write("---")
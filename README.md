# Semantic-Search-FAQ-Chatbot-with-SBERT
A semantic search application using Sentence-BERT (SBERT) to find the most relevant answers for user queries in an e-commerce FAQ dataset. 

# Semantic Search FAQ Bot

A smart FAQ bot that finds the **most relevant answers** from a dataset even if your question is phrased differently!

## How it Works

1. **User types a question** in the Streamlit app.
2. The question is converted into an **embedding vector** using **SBERT**.
3. The embedding is compared to precomputed embeddings of all questions in the dataset.
4. **Top 3 most similar questions and answers** are displayed along with a similarity score.

![Semantic Search Workflow](semantic_search.gif)

> 💡 Replace `semantic_search.gif` with your actual GIF or image path.

---

## Tech Stack

- **Python**
- **Streamlit** - for the UI
- **Pandas** - for data manipulation
- **PyTorch** - backend for SBERT
- **Sentence-Transformers (SBERT)** - semantic embeddings
- **NumPy** - numerical operations

---

## Usage

1. Clone the repo:
```bash
git clone <your-repo-link>



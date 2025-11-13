# Semantic-Search-FAQ-Chatbot-with-SBERT
This project presents a smart FAQ (Frequently Asked Questions) Bot that utilizes Semantic Search capabilities powered by Sentence-BERT (SBERT) to deliver highly relevant answers to user inquiries, even if the user's question is phrased differently from the questions in the original dataset.

The application transforms an e-commerce FAQ dataset into an intelligent search utility, moving beyond traditional keyword-matching limitations to truly understand the user's intent.

## How it Works

1. **User types a question** in the Streamlit app.
2. The question is converted into an **embedding vector** using **SBERT**.
3. The embedding is compared to precomputed embeddings of all questions in the dataset.
4. **Top 3 most similar questions and answers** are displayed along with a similarity score.

## Technical Architecture: How it Works
The core functionality relies on two main phases driven by the Sentence-BERT model (multi-qa-mpnet-base-cos-v1).

1. Offline Preparation (The Corpus)
Corpus Creation: All questions from the Ecommerce_FAQ_Chatbot_dataset.json are extracted to form the text corpus.

2. Embedding Generation: The SBERT model converts every question in the corpus into a unique high-dimensional vector (Embedding). This vector is a numerical representation of the question's semantic meaning (its "fingerprint").

3. Storage: These embeddings are pre-calculated and stored efficiently (as a PyTorch Tensor) to ensure rapid search speed when the application is live.

## Key Technologies Used

| Technology | Role in the Project |
| :--- | :--- |
| **Sentence-BERT (SBERT)** | The deep learning model responsible for generating high-quality semantic embeddings. |
| **PyTorch & NumPy** | Provides the necessary tensor manipulation capabilities for high-speed vector calculations and robust data type handling. |
| **Pandas** | Used for efficient data loading, structure, and retrieval from the JSON source. |
| **Streamlit** | Enables the rapid creation of an interactive and user-friendly web interface for querying the search engine. |

![Semantic Search Workflow](semantic_search.gif)


---

## Tech Stack

- **Python**
- **Streamlit** - for the UI
- **Pandas** - for data manipulation
- **PyTorch** - backend for SBERT
- **Sentence-Transformers (SBERT)** - semantic embeddings
- **NumPy** - numerical operations



[![Building](https://img.shields.io/badge/Semantic%20Search%20-Online%20and%20Ready-green?style=for-the-badge&logo=pytorch&logoColor=white&cacheSeconds=3600&animate=true)](https://github.com/rawangamal87/Semantic-Search-FAQ-with-SBERT)


![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.9.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Sentence Transformers](https://img.shields.io/badge/SBERT-5.1.2-3178C6?style=for-the-badge&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/NumPy-2.2.6-013243?style=for-the-badge&logo=numpy&logoColor=white)


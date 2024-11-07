# QNA-TEXT-BOT

QNA-TEXT-BOT is a text-based question-answering bot built with Streamlit, designed to answer questions from various text sources. This bot leverages multiple libraries and frameworks to process and retrieve accurate information, providing users with a fast and interactive experience. **Please note:** Running this app requires a high-specification system due to its use of computationally intensive libraries and models.

## Built With

This project integrates the following key libraries:

- **google-generativeai**: This library integrates Google’s generative AI models, providing the capability to generate answers based on sophisticated machine learning algorithms.
  
- **langchain**: LangChain is a framework designed for developing applications powered by language models. It simplifies connecting various components like memory, prompts, and document retrieval, creating a more cohesive and efficient workflow for NLP tasks.
  
- **langchain-community**: An extension of LangChain that includes additional community-driven tools and integrations for enhancing language model interactions and adding custom modules for better model support.
  
- **PyPDF2**: PyPDF2 is a Python library for reading and manipulating PDF files. In this project, it’s used to extract text content from PDFs, allowing the bot to answer questions based on PDF documents.
  
- **faiss-cpu**: FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and clustering. In this project, FAISS helps in retrieving relevant sections of large datasets by organizing and indexing information efficiently.
  
- **streamlit**: Streamlit is a web application framework for creating interactive data apps in Python. Here, it provides the front-end interface for users to interact with the QNA bot.

## System Requirements

Due to the computational needs of these libraries, the app performs best on a high-specification system. For optimal performance:
- **RAM**: 16GB or more
- **CPU**: Multi-core processor (4 cores or higher recommended)
- **Optional**: GPU support if utilizing large models


## Setup and Installation

### Prerequisites
- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [Anaconda](https://www.anaconda.com/products/distribution) (optional, for environment management)

### 1. Create a Python Environment
To isolate the dependencies, it’s recommended to set up a virtual environment using either Conda or Python's built-in virtual environment.

#### Using Conda
```bash
conda create -n qna-text-bot python=3.8
conda activate qna-text-bot
```
### (If not using Conda)
```bash
python -m venv qna-text-bot-env
source qna-text-bot-env/bin/activate  # On Windows, use `qna-text-bot-env\Scripts\activate`
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run app.py
```

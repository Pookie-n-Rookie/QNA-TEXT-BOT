# QNA-TEXT-BOT

QNA-TEXT-BOT is a text-based question-answering bot built with Streamlit for a simple and interactive web interface. This bot can be configured to provide answers based on various models or datasets, helping users to quickly get the information they need.

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

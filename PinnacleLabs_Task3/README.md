# 🎬 Sentiment Analysis Using Machine Learning

## 📌 Overview

This project is a Machine Learning-based Sentiment Analysis System developed using Python and Natural Language Processing (NLP) techniques. The system analyzes movie reviews and predicts whether the sentiment expressed in the review is **Positive** or **Negative**.

The project uses TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization for feature extraction and Logistic Regression for sentiment classification. By training on thousands of labeled movie reviews, the model learns to identify emotional patterns in textual data and accurately classify user-provided reviews.

---

## 🎯 Features

* Positive and Negative Sentiment Classification
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression Model
* Interactive Command-Line Interface (CLI)
* Real-Time Sentiment Prediction
* Model Performance Evaluation

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression
* Natural Language Processing (NLP)

---

## 📂 Dataset

This project utilizes the IMDb Movie Reviews Dataset available on Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Dataset File:

```text
IMDB Dataset.csv
```

### Dataset Information

The dataset contains 50,000 movie reviews labeled as either:

* Positive
* Negative

These labeled reviews are used to train and evaluate the sentiment classification model.

### Note

The original dataset is relatively large and is not included in this repository to keep the repository lightweight and improve download and cloning performance.

Please download the dataset directly from the Kaggle link above and place the dataset file in the project directory before running the program.

---

## 📁 Project Structure

```text
Sentiment-Analysis/
│
├── IMDB Dataset.csv
├── main.py
└── README.md
```

---

## ⚙️ Working Principle

The project follows the following workflow:

1. Load IMDb movie review dataset
2. Split dataset into training and testing sets
3. Convert text into numerical features using TF-IDF
4. Train Logistic Regression model
5. Evaluate model performance
6. Accept custom user review input
7. Predict Positive or Negative sentiment

---

## ▶️ Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

---

## ▶️ Running the Project

Execute the following command:

```bash
python main.py
```

---

## 💡 Sample Inputs

### Positive Review

```text
This movie was absolutely fantastic. The acting, story, and direction were outstanding.
```

Expected Output:

```text
Predicted Sentiment: POSITIVE
```

### Negative Review

```text
This was the worst movie I have ever watched. It was boring and poorly written.
```

Expected Output:

```text
Predicted Sentiment: NEGATIVE
```

---

## 📊 Model Performance

The model is trained using TF-IDF Vectorization and Logistic Regression and achieves high sentiment classification accuracy on the IMDb review dataset.

Example Result:

```text
Accuracy: 88% - 90%+
```

(Actual accuracy may vary depending on preprocessing and train-test split.)

---

## 📚 Learning Outcomes

* Text Preprocessing
* Sentiment Classification
* Natural Language Processing
* Feature Extraction using TF-IDF
* Machine Learning Model Training
* Model Evaluation Techniques

---

## 🚀 Future Enhancements

* Multi-class Sentiment Analysis
* Emotion Detection
* Deep Learning Models (LSTM/BERT)
* Web Application Integration
* Real-Time Review Analysis

---

## 👨‍💻 Author

Anirudh L

Project completed as part of the Pinnacle Labs Internship Program.

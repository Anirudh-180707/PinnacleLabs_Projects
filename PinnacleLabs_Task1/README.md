# 📰 Fake News Detection Using Machine Learning

## 📌 Overview

This project is a Machine Learning-based Fake News Detection System developed using Python and Natural Language Processing (NLP) techniques. The model analyzes news article content and classifies it as either **Real News** or **Fake News** using TF-IDF Vectorization and Logistic Regression.

The system is trained on a publicly available dataset containing real and fake news articles and can predict the authenticity of user-provided news text through a command-line interface.

---

## 🚀 Features

* Fake vs Real News Classification
* Natural Language Processing (NLP)
* TF-IDF Text Vectorization
* Logistic Regression Model
* Model Performance Evaluation
* Interactive Command-Line Prediction System

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression

---

## 📂 Dataset

This project uses the **Fake and Real News Dataset** from Kaggle:

Dataset Link:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Files Used:

* Fake.csv
* True.csv

### Note

The original dataset files are relatively large and may exceed GitHub's recommended file size limits or make the repository unnecessarily heavy. Therefore, the dataset files are not included in this repository.

Please download the dataset directly from the Kaggle link above and place the following files in the project directory before running the program:

```text
Fake.csv
True.csv
```

---

## 📁 Project Structure

```text
Fake-News-Detection/
│
├── Fake.csv
├── True.csv
├── main.py
└── README.md
```

---

## ▶️ How to Run

1. Download the dataset from Kaggle.
2. Place `Fake.csv` and `True.csv` in the project folder.
3. Install the required libraries:

```bash
pip install pandas scikit-learn
```

4. Run the program:

```bash
python main.py
```

---

## 📊 Model Performance

The model is trained using TF-IDF Vectorization and Logistic Regression and achieves high classification accuracy on the test dataset.

Example Accuracy:

```text
Accuracy: 98.64%
```

---

## 🎯 Sample Usage

```text
Enter a news article:

Scientists have developed a new technology to reduce air pollution in major cities.

Prediction: REAL NEWS
```

---

## 📚 Learning Outcomes

* Data Preprocessing
* Text Classification
* Natural Language Processing
* Feature Extraction using TF-IDF
* Machine Learning Model Training
* Model Evaluation and Prediction

---

## 👨‍💻 Author

Anirudh L

Project completed as part of the Pinnacle Labs Internship Program.

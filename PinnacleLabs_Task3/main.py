import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("=" * 40)
print("      SENTIMENT ANALYSIS SYSTEM")
print("=" * 40)

# Load dataset
df = pd.read_csv("IMDB Dataset.csv")

# Features and labels
X = df["review"]
y = df["sentiment"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text into numerical features
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)

print("\nTraining model...")
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# User testing
while True:

    print("\n----------------------------")
    review = input(
        "Enter a movie review (or type 'exit' to quit):\n"
    )

    if review.lower() == "exit":
        break

    review_vector = vectorizer.transform([review])

    result = model.predict(review_vector)

    print(f"\nPredicted Sentiment: {result[0].upper()}")
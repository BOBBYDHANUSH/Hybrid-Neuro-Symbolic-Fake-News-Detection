from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from config import MAX_FEATURES

vectorizer = TfidfVectorizer(
    max_features=MAX_FEATURES
)

model = LogisticRegression()

def train(X_train, y_train):

    X_train_vec = vectorizer.fit_transform(X_train)

    model.fit(
        X_train_vec,
        y_train
    )

    return vectorizer, model


def predict(text):

    vec = vectorizer.transform([text])

    pred = model.predict(vec)[0]

    prob = model.predict_proba(vec).max()

    return pred, prob
import pickle
import pandas as pd


# Load ML model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


# Model version
MODEL_VERSION = "1.0.0"


# Get class labels
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):

    # Convert input dictionary to DataFrame
    df = pd.DataFrame([user_input])

    # Predict class
    predicted_class = model.predict(df)[0]

    # Get probabilities
    probabilities = model.predict_proba(df)[0]

    # Highest probability
    confidence = max(probabilities)

    # Create class-probability mapping
    class_probs = dict(
        zip(
            class_labels,
            map(lambda p: round(float(p), 4), probabilities)
        )
    )

    return {
        "predicted_category": str(predicted_class),
        "confidence": round(float(confidence), 4),
        "class_probabilities": class_probs
    }
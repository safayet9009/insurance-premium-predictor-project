# 💰 Insurance Premium Predictor

An end-to-end **Machine Learning application** that predicts an individual's insurance premium category based on personal, lifestyle, financial, and demographic information.

The project combines a trained **Scikit-learn classification model** with a **FastAPI backend** and an interactive **Streamlit frontend**, with Docker support for containerized deployment.

---

## 🚀 Features

* 🤖 Machine Learning-based insurance premium prediction
* ⚡ FastAPI REST API
* 🎨 Interactive Streamlit frontend
* 🛡️ Input validation using Pydantic
* 📊 Prediction confidence and class probabilities
* 🧮 Automatic BMI calculation
* 👤 Automatic age-group classification
* 🚬 Lifestyle risk calculation
* 🏙️ City-tier classification
* 🐳 Docker support
* 📚 Automatic Swagger API documentation
* 🔍 Health-check endpoint

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Streamlit Frontend │
                    │        :8501         │
                    └──────────┬───────────┘
                               │
                         POST /predict
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │        :8000         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Pydantic Schema    │
                    │      Validation      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Engineering  │
                    │                      │
                    │ BMI                  │
                    │ Age Group            │
                    │ Lifestyle Risk       │
                    │ City Tier            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Scikit-learn Model   │
                    │      model.pkl       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prediction Response  │
                    │                      │
                    │ Category             │
                    │ Confidence           │
                    │ Class Probabilities  │
                    └──────────────────────┘
```

---

## 📁 Project Structure

```text
insurance-premium-predictor/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── config/
│   └── city_tier.py
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
│
└── frontend/
    └── streamlit_app.py
```

---

## 🧠 Model Input

The application accepts the following user information:

| Feature      | Description                  |
| ------------ | ---------------------------- |
| `age`        | User's age                   |
| `weight`     | Weight in kilograms          |
| `height`     | Height in meters             |
| `income_lpa` | Annual income in LPA         |
| `smoker`     | Whether the user is a smoker |
| `city`       | User's city                  |
| `occupation` | User's occupation            |

The application then derives additional features:

* BMI
* Age Group
* Lifestyle Risk
* City Tier

These features are passed to the trained machine learning model.

---

## 📊 Prediction Output

The API returns:

```json
{
  "predicted_category": "High",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.0121,
    "Medium": 0.1447,
    "High": 0.8432
  }
}
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/safayet9009/insurance-premium-predictor.git
cd insurance-premium-predictor
```

### 2. Create a Python environment

This project uses **Python 3.11**.

```bash
python -m venv .venv
```

Activate the environment on Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Backend

Start the API server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

### Health Check

```text
http://127.0.0.1:8000/health
```

---

## 🎨 Run Streamlit Frontend

Open another terminal and activate the environment:

```bash
source .venv/bin/activate
```

Then run:

```bash
streamlit run frontend/streamlit_app.py
```

The frontend will be available at:

```text
http://localhost:8501
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t insurance-premium-api .
```

Run the container:

```bash
docker run -p 8000:8000 insurance-premium-api
```

The FastAPI backend will then be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## 🔌 API Endpoint

### `POST /predict`

Example request:

```json
{
  "age": 30,
  "weight": 65,
  "height": 1.70,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

Example response:

```json
{
  "predicted_category": "Medium",
  "confidence": 0.7812,
  "class_probabilities": {
    "Low": 0.0521,
    "Medium": 0.7812,
    "High": 0.1667
  }
}
```

---

## 🛡️ Input Validation

The FastAPI backend uses **Pydantic** to validate incoming requests.

Examples of validation rules:

* Age must be between 1 and 119
* Weight must be greater than 0
* Height must be between 0 and 2.5 meters
* Income must be greater than 0
* Occupation must belong to the predefined categories
* City names are normalized automatically

---

## 🔍 Derived Features

### BMI

```text
BMI = Weight / Height²
```

### Age Group

```text
Age < 25       → young
25–44          → adult
45–59          → middle_aged
60+            → senior
```

### Lifestyle Risk

The application combines smoking status and BMI to estimate lifestyle risk:

```text
Smoker + BMI > 30 → High
Smoker OR BMI >27 → Medium
Otherwise         → Low
```

### City Tier

Cities are categorized into:

```text
Tier 1
Tier 2
Tier 3
```

---

## 🧰 Technology Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Frontend

* Streamlit
* Requests

### Deployment

* Docker
* Docker Engine

---

## 📌 Project Highlights

This project demonstrates an end-to-end ML deployment workflow:

```text
Machine Learning Model
        ↓
Model Serialization
        ↓
FastAPI REST API
        ↓
Pydantic Validation
        ↓
Feature Engineering
        ↓
Prediction
        ↓
Streamlit UI
        ↓
Docker Containerization
```

It is designed to demonstrate how a machine learning model can be transformed into a practical, production-style application rather than remaining only inside a Jupyter Notebook.

---

## 🔮 Future Improvements

* [ ] Deploy the FastAPI backend to a cloud platform
* [ ] Deploy the Streamlit frontend
* [ ] Add automated CI/CD with GitHub Actions
* [ ] Add model monitoring
* [ ] Add structured logging
* [ ] Add automated API testing
* [ ] Add model versioning
* [ ] Add authentication and API security
* [ ] Add Docker Compose for frontend + backend
* [ ] Add database integration for prediction history

---

## 👨‍💻 Author

**Safayet Hossain**

Computer Science & Engineering Student
Patuakhali Science and Technology University

GitHub: [@safayet9009](https://github.com/safayet9009)

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ star and checking out the other projects on my GitHub profile.

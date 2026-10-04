# 💰 Insurance Premium Predictor

An end-to-end **Machine Learning application** that predicts an individual's insurance premium category based on personal, lifestyle, financial, and demographic information.

The project combines a trained **Scikit-learn classification model** with a **FastAPI backend** and an interactive **Streamlit frontend**, with **Docker and Docker Compose** support for containerized deployment.

The backend and frontend Docker images are also published on **Docker Hub** for easy deployment.

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
* 🐳 Docker containerization
* 🐳 Docker Compose for frontend + backend orchestration
* 📦 Docker Hub images
* 📚 Automatic Swagger API documentation
* 🔍 Health-check endpoint

---

## 🏗️ Architecture

```text
                         Browser
                            │
                            ▼
                ┌──────────────────────┐
                │  Streamlit Frontend  │
                │       :8501          │
                └──────────┬───────────┘
                           │
                           │ POST /predict
                           ▼
                ┌──────────────────────┐
                │   FastAPI Backend    │
                │       :8000          │
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
                │  Feature Engineering │
                │                      │
                │  BMI                 │
                │  Age Group           │
                │  Lifestyle Risk      │
                │  City Tier           │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Scikit-learn Model  │
                │      model.pkl       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Prediction Response │
                │                      │
                │  Category            │
                │  Confidence          │
                │  Class Probabilities │
                └──────────────────────┘
```

### Docker Compose Architecture

```text
                         Host Machine
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
       ┌─────────────────┐         ┌─────────────────┐
       │    Frontend     │         │     Backend     │
       │   Streamlit     │────────▶│     FastAPI     │
       │     :8501       │  HTTP   │      :8000      │
       └─────────────────┘         └────────┬────────┘
                                            │
                                            ▼
                                      ┌─────────────┐
                                      │  model.pkl  │
                                      └─────────────┘
```

The Streamlit frontend communicates with the backend using the Docker Compose service name:

```text
http://backend:8000
```

---

## 📁 Project Structure

```text
insurance-premium-predictor-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
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
    ├── streamlit_app.py
    └── Dockerfile
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

The application derives additional features automatically:

* BMI
* Age Group
* Lifestyle Risk
* City Tier

These features are passed to the trained machine learning model.

---

## 📊 Prediction Output

The API returns the predicted insurance premium category, confidence score, and probability distribution across all classes.

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

# ⚙️ Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/safayet9009/insurance-premium-predictor-project.git

cd insurance-premium-predictor-project
```

---

## 2. Create a Python Environment

This project uses **Python 3.11**.

```bash
python -m venv .venv
```

Activate the environment on Linux/macOS:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Backend Locally

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

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "OK",
  "version": "1.0.0",
  "model_loaded": true
}
```

---

# 🎨 Run Streamlit Frontend Locally

Open another terminal and activate the environment:

```bash
source .venv/bin/activate
```

Run:

```bash
streamlit run frontend/streamlit_app.py
```

The frontend will be available at:

```text
http://localhost:8501
```

> When running the frontend and backend directly on the host machine, the Streamlit application communicates with FastAPI through `127.0.0.1:8000`.

---

# 🐳 Docker

The project supports Docker-based containerization.

## Build Backend Image

```bash
docker build -t insurance-premium-api .
```

Run:

```bash
docker run -p 8000:8000 insurance-premium-api
```

The FastAPI backend will be available at:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker Compose

The recommended way to run the complete application is using Docker Compose.

Docker Compose runs:

* FastAPI backend
* Streamlit frontend
* Internal Docker network between the services

Start the complete application:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

Expected services:

```text
insurance-premium-backend
insurance-premium-frontend
```

### Application URLs

**Streamlit Frontend:**

```text
http://localhost:8501
```

**FastAPI Backend:**

```text
http://localhost:8000
```

**Swagger API Documentation:**

```text
http://localhost:8000/docs
```

**Health Check:**

```text
http://localhost:8000/health
```

### Stop the application

```bash
docker compose down
```

### Rebuild images

```bash
docker compose build
```

Then start again:

```bash
docker compose up -d
```

---

# 📦 Docker Hub

The application images are published on Docker Hub.

**Docker Hub Repository:**

```text
https://hub.docker.com/r/safayet7/insurance-premium-predictor
```

### Backend Image

```bash
docker pull safayet7/insurance-premium-predictor:backend
```

### Frontend Image

```bash
docker pull safayet7/insurance-premium-predictor:frontend
```

### Available Images

```text
safayet7/insurance-premium-predictor:backend
safayet7/insurance-premium-predictor:frontend
```

The backend image contains:

```text
FastAPI
Scikit-learn model
Pydantic validation
Feature engineering
Prediction API
```

The frontend image contains:

```text
Streamlit
Prediction UI
HTTP communication with FastAPI
```

---

# 🔌 API Endpoint

## `POST /predict`

Predict the insurance premium category.

### Example Request

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

### Example Response

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

# 🛡️ Input Validation

The FastAPI backend uses **Pydantic** to validate incoming requests.

Examples of validation rules:

* Age must be between 1 and 119
* Weight must be greater than 0
* Height must be between 0 and 2.5 meters
* Income must be greater than 0
* Occupation must belong to the predefined categories
* City names are normalized automatically

Invalid requests return FastAPI validation errors with HTTP status `422`.

---

# 🔍 Derived Features

## BMI

```text
BMI = Weight / Height²
```

---

## Age Group

```text
Age < 25       → young
25–44          → adult
45–59          → middle_aged
60+            → senior
```

---

## Lifestyle Risk

The application combines smoking status and BMI to estimate lifestyle risk:

```text
Smoker + BMI > 30 → High
Smoker OR BMI >27 → Medium
Otherwise         → Low
```

---

## City Tier

Cities are categorized into:

```text
Tier 1
Tier 2
Tier 3
```

The city tier is automatically determined using the project's city configuration.

---

# 🧰 Technology Stack

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

### Containerization & Deployment

* Docker
* Docker Compose
* Docker Hub

---

# 📌 Project Highlights

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
        ↓
Docker Compose
        ↓
Docker Hub
```

The project demonstrates how a machine learning model can be transformed into a practical, containerized application rather than remaining only inside a Jupyter Notebook.

---

# 🔮 Future Improvements

* [ ] Deploy the FastAPI backend to a cloud platform
* [ ] Deploy the Streamlit frontend
* [ ] Add automated CI/CD with GitHub Actions
* [ ] Add model monitoring
* [ ] Add structured logging
* [ ] Add automated API testing
* [ ] Add model versioning
* [ ] Add authentication and API security
* [ ] Add database integration for prediction history
* [ ] Add automated Docker image publishing through GitHub Actions

---

# 👨‍💻 Author

**Safayet Hossain**

Computer Science & Engineering Student
Patuakhali Science and Technology University

GitHub: [@safayet9009](https://github.com/safayet9009)

---

# ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ star and checking out the other projects on my GitHub profile.

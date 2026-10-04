import streamlit as st
import requests


# ============================================================
# Configuration
# ============================================================

API_URL = "http://backend:8000/predict"
HEALTH_URL = "http://backend:8000/health"


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)


# ============================================================
# Header
# ============================================================

st.title("💰 Insurance Premium Category Predictor")

st.markdown(
    """
    Enter your personal information below to predict
    your insurance premium category using a machine learning model.
    """
)

st.divider()


# ============================================================
# Input Section
# ============================================================

st.subheader("👤 Personal Information")


col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=119,
        value=30,
        step=1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=65.0,
        step=0.1
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70,
        step=0.01
    )


with col2:

    income_lpa = st.number_input(
        "Annual Income (LPA)",
        min_value=0.1,
        max_value=1000.0,
        value=10.0,
        step=0.1
    )

    smoker = st.selectbox(
        "Are you a smoker?",
        options=[False, True],
        format_func=lambda x: "Yes" if x else "No"
    )

    city = st.text_input(
        "City",
        value="Mumbai"
    )


# ============================================================
# Occupation
# ============================================================

st.subheader("💼 Occupation")

occupation = st.selectbox(
    "Select your occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]
)


st.divider()


# ============================================================
# Prediction
# ============================================================

predict_button = st.button(
    "🔮 Predict Premium Category",
    use_container_width=True
)


if predict_button:

    # --------------------------------------------------------
    # Prepare input
    # --------------------------------------------------------

    input_data = {

        "age": age,

        "weight": weight,

        "height": height,

        "income_lpa": income_lpa,

        "smoker": smoker,

        "city": city,

        "occupation": occupation
    }


    # --------------------------------------------------------
    # Validate city
    # --------------------------------------------------------

    if not city.strip():

        st.error("Please enter your city.")

        st.stop()


    # --------------------------------------------------------
    # Send request to FastAPI
    # --------------------------------------------------------

    try:

        with st.spinner("Predicting insurance premium category..."):

            response = requests.post(
                API_URL,
                json=input_data,
                timeout=10
            )


        # ----------------------------------------------------
        # Successful response
        # ----------------------------------------------------

        if response.status_code == 200:

            result = response.json()


            predicted_category = result["predicted_category"]

            confidence = result["confidence"]

            class_probabilities = result["class_probabilities"]


            # ------------------------------------------------
            # Prediction result
            # ------------------------------------------------

            st.success(
                f"Predicted Insurance Premium Category: **{predicted_category}**"
            )


            # ------------------------------------------------
            # Confidence
            # ------------------------------------------------

            st.subheader("📊 Prediction Confidence")

            st.progress(
                confidence
            )

            st.write(
                f"Confidence: **{confidence:.2%}**"
            )


            # ------------------------------------------------
            # Class probabilities
            # ------------------------------------------------

            st.subheader("📈 Class Probabilities")


            for category, probability in class_probabilities.items():

                st.write(
                    f"**{category}**: {probability:.2%}"
                )

                st.progress(
                    probability
                )


            # ------------------------------------------------
            # Input summary
            # ------------------------------------------------

            with st.expander("🔍 View Submitted Information"):

                st.json(input_data)


        # ----------------------------------------------------
        # Validation error
        # ----------------------------------------------------

        elif response.status_code == 422:

            st.error(
                "Invalid input data."
            )

            try:

                error_data = response.json()

                st.json(error_data)

            except Exception:

                st.write(response.text)


        # ----------------------------------------------------
        # Other API errors
        # ----------------------------------------------------

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

            try:

                st.json(response.json())

            except Exception:

                st.write(response.text)


    # --------------------------------------------------------
    # Connection error
    # --------------------------------------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to the FastAPI server."
        )

        st.info(
            "Make sure FastAPI is running on http://127.0.0.1:8000"
        )


    # --------------------------------------------------------
    # Timeout error
    # --------------------------------------------------------

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ Request timed out."
        )


    # --------------------------------------------------------
    # Unexpected error
    # --------------------------------------------------------

    except Exception as e:

        st.error(
            f"Unexpected error: {str(e)}"
        )
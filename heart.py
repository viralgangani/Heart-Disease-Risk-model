import pickle
import streamlit as st
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_background(image_file):
    img = get_base64(image_file)

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("hrt.jpg")
img = get_base64("hrt.jpg")

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background:
            linear-gradient(rgba(0,0,0,0.62),
                            rgba(0,0,0,0.62)),
            url("data:image/png;base64,{img}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Heart Disease Risk Prediction",
    page_icon="🫀",
    layout="wide"
)

st.markdown("""

    <style>
        .st-emotion-cache-4cktc5 h1{
            color: #8B0000;
            background: rgba(255, 255, 255, 0.18);
            padding-left: 3rem;
            margin-top: 3rem;
            
        }
            
        .st-emotion-cache-4cktc5 h3{
            color: #b9f7ff;    
        
        }
                   
        .st-emotion-cache-1anq8dj {
            background-color: rgba(200, 170, 160, 0.4);
            color: rgba(200, 1, 17, 1);
            font-weight: 400;
            line-height: 2.4;
            font-size: 24px;
            border: 2px solid rgba(255, 210, 163, 1);
            }
              
}

    </style>

""", unsafe_allow_html=True)

heart_model = pickle.load(open('heart_risk_modal.sav', 'rb'))

col1, col2 = st.columns(2)
with col1:
    st.title("Heart Disease Risk Prediction")

svg_path = "activity.svg"

with col2:
    st.image("activity.svg", width=150)

st.markdown("---")

card1, card2 = st.columns(2)
with card1:    
    with st.container(border=True):
        st.subheader("📋 Personal Information & Medical Health")
        c1, c2 = st.columns(2)
        with c1:

            Gender = st.selectbox("Gender", ["Male", "Female"], help="Your biological sex (Male or Female).")
            Gender = 1 if Gender == "Male" else 0

            Family_History = st.selectbox("Family History of Heart Disease", ["No", "Yes"],  help="Whether you have a family history of heart disease (Yes or No).")
            Family_History = 1 if Family_History == "Yes" else 0

        with c2:
            Age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=44, help="Your age in years."
            )
                
            Chronic_Stress = st.selectbox("Chronic Stress", ["No", "Yes"], help="Experiencing ongoing stress for a long period of time.")
            Chronic_Stress = 1 if Chronic_Stress == "Yes" else 0

with card2:
    with st.container(border=True):
        st.subheader("🛋️ Lifestyle")
        c1, c2 = st.columns(2)
        with c1:
            Smoking = st.selectbox("Smoking", ["No", "Yes"], help="Regular use of cigarettes or other tobacco products.")
            Smoking = 1 if Smoking == "Yes" else 0

            Obesity = st.selectbox("Obesity", ["No", "Yes"], help="Having over body weight that may affect health.")
            Obesity = 1 if Obesity == "Yes" else 0

        with c2:
            Sedentary_Lifestyle = st.selectbox("Sedentary Lifestyle", ["No", "Yes"], help="Spending most of the day sitting with little physical activity.")
            Sedentary_Lifestyle = 1 if Sedentary_Lifestyle == "Yes" else 0

st.markdown("---")

card3, card4 = st.columns(2)
with card3:
    with st.container(border=True):
        st.subheader("🌡️ Medical Conditions")
        c1, c2 = st.columns(2)
        with c1:
            High_BP = st.selectbox("High Blood Pressure", ["No", "Yes"], help="Having high blood pressure (hypertension).")
            High_BP = 1 if High_BP == "Yes" else 0

            Diabetes = st.selectbox("Diabetes", ["No", "Yes"], help="A condition where the body has difficulty controlling blood sugar levels.")
            Diabetes = 1 if Diabetes == "Yes" else 0

        with c2:
            High_Cholesterol = st.selectbox("High Cholesterol", ["No", "Yes"], help="Having elevated levels of cholesterol in the blood.")
            High_Cholesterol = 1 if High_Cholesterol == "Yes" else 0

with card4:
    with st.container(border=True):
        st.subheader("🫁 Symptoms")

        symptoms = st.multiselect(
            "Select symptoms you are experiencing",
            [
                "Fatigue",
                "Chest Pain",
                "Shortness of Breath",
                "Palpitations",
                "Dizziness",
                "Swelling",
                "Pain in Arms/Jaw/Back",
                "Cold Sweats/Nausea"
            ]
        )

        Fatigue = 1 if "Fatigue" in symptoms else 0
        Chest_Pain = 1 if "Chest Pain" in symptoms else 0
        Shortness_of_Breath = 1 if "Shortness of Breath" in symptoms else 0
        Palpitations = 1 if "Palpitations" in symptoms else 0
        Dizziness = 1 if "Dizziness" in symptoms else 0
        Swelling = 1 if "Swelling" in symptoms else 0
        Pain_Arms_Jaw_Back = 1 if "Pain in Arms/Jaw/Back" in symptoms else 0
        Cold_Sweats_Nausea = 1 if "Cold Sweats/Nausea" in symptoms else 0        

st.markdown("---")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("**Predict Heart Disease Risk**", width=300):
            heart_prediction = heart_model.predict([
                [Chest_Pain, Shortness_of_Breath, Fatigue, Palpitations, Dizziness, 
                Swelling, Pain_Arms_Jaw_Back, Cold_Sweats_Nausea, High_BP, High_Cholesterol, 
                Diabetes, Smoking, Obesity, Sedentary_Lifestyle, Family_History, 
                Chronic_Stress, Gender, Age]])
                
            input_data = [[
            Chest_Pain, Shortness_of_Breath, Fatigue, Palpitations, Dizziness,
            Swelling, Pain_Arms_Jaw_Back, Cold_Sweats_Nausea, High_BP, High_Cholesterol,
            Diabetes, Smoking, Obesity, Sedentary_Lifestyle, Family_History,
            Chronic_Stress, Gender, Age
            ]]

            heart_pred = heart_model.predict(input_data)
            heart_probability = heart_model.predict_proba(input_data)
            risk_probability = heart_probability[0][1] * 100
            with col2:
                if heart_prediction[0] == 1:
                    heart_risk = "There is a Risk of Heart Disease"
                    st.error(f"There is a Risk of Heart Disease" f"Risk Probability: **{risk_probability:.2f}%**")        
                else:
                    heart_risk = "There is No Risk of Heart Disease"
                    st.success(f"There is No Risk of Heart Disease")

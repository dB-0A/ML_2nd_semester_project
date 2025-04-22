# # # # # streamlit_app.py
# # # # import streamlit as st
# # # # import pickle
# # # # import numpy as np
# # # #
# # # # # Load trained model
# # # # # model = pickle.load(open('your_model.pkl', 'rb'))  # Uncomment and use your actual model
# # # #
# # # # st.title("Drug Addiction Risk Prediction")
# # # # st.subheader("Fill in the details to predict drug addiction risk")
# # # #
# # # # # Gender
# # # # gender = st.selectbox("Gender", ["Female", "Male", "Other"])
# # # #
# # # # # Education Level
# # # # education = st.selectbox("Education Level", ["No Formal Education", "High School", "Bachelor's", "Master's", "PhD"])
# # # #
# # # # # Occupation
# # # # occupation = st.selectbox("Occupation", ["Student", "Unemployed", "Teacher", "Business", "Laborer",
# # # #                                          "Engineer", "Clerk", "Artist", "Doctor"])
# # # #
# # # # # Income Level
# # # # income = st.radio("Income Level", ["Low", "Medium", "High"])
# # # #
# # # # # Medical Condition
# # # # medical = st.selectbox("Medical Condition", ["Healthy", "Diabetes", "Heart Disease", "Anxiety",
# # # #                                              "Hypertension", "Depression"])
# # # #
# # # # # Social Behavior
# # # # social_behavior = st.selectbox("Social Behavior", ["No Criminal Record", "Multiple Arrests", "Minor Offense",
# # # #                                                    "Rehab Attended", "Therapy Ongoing"])
# # # #
# # # # # Peer Influence
# # # # peer_influence = st.selectbox("Peer Influence",
# # # #                               ["No Influence", "Some Friends Use", "Many Friends Use", "Peer Pressure"])
# # # #
# # # # # Living Situation
# # # # living = st.selectbox("Living Situation", ["With Family/Relatives", "Hostel/Hall", "Alone"])
# # # #
# # # # # Legal Issues
# # # # legal = st.radio("Legal Issues", ["No", "Yes"])
# # # #
# # # # # Drug Motive
# # # # drug_motive = st.selectbox("Drug Motive", [
# # # #     "Disease",
# # # #     "Should avoid",
# # # #     "Social trend",
# # # #     "Disease, Should avoid",
# # # #     "Disease, Social trend",
# # # #     "Social trend, Should avoid",
# # # #     "Disease, Social trend, Should avoid"
# # # # ])
# # # #
# # # # # Social Time Spent
# # # # social_time = st.selectbox("Social Time Spent", ["Friends", "Family/ Relatives", "Alone", "Job/Work place",
# # # #                                                  "Hostel", "Business", "School"])
# # # #
# # # # # Life Failure
# # # # life_failure = st.radio("Experienced Life Failure?", ["No", "Yes"])
# # # #
# # # # # Mental Health Issues
# # # # mental_health = st.selectbox("Mental Health Issues", ["None / I don't know", "Anxiety/Stress", "Depression/Guilt",
# # # #                                                       "Anger Issues", "Multiple Conditions"])
# # # #
# # # # # Lives With User
# # # # lives_with = st.radio("Lives With User", ["Yes", "No", "Not sure"])
# # # #
# # # # # Smoking Status
# # # # smoking = st.selectbox("Smoking Status", ["No, I don't", "Yes, occasionally", "Yes, every day."])
# # # #
# # # # # Drug Experience
# # # # drug_exp = st.radio("Past Drug Experience?", ["No", "Yes"])
# # # #
# # # # # Friend Influence
# # # # friend_influence = st.radio("Friends Influence?", ["No, they don't", "Yes, often they do"])
# # # #
# # # # # Willingness to Try
# # # # willingness = st.radio("Willingness To Try Drugs", ["no", "maybe", "yes"])
# # # #
# # # # # Self Control
# # # # self_control = st.radio("Self Control", ["Yes, It's possible", "No, It's not possible"])
# # # #
# # # # # Usage Frequency
# # # # usage = st.selectbox("Drug Usage Frequency", ["Never/ Not applicable", "Once/twice a week",
# # # #                                               "Occasionally", "Regularly"])
# # # #
# # # # # Button to predict
# # # # if st.button("Predict"):
# # # #     # Encode inputs (you must match the model's training preprocessing)
# # # #     # For now, let's simulate with dummy input
# # # #     dummy_input = np.zeros(30).reshape(1, -1)  # Replace with actual preprocessing
# # # #     # prediction = model.predict(dummy_input)[0]
# # # #
# # # #     # Simulated prediction
# # # #     prediction = "Could become Drug Addict" if np.random.rand() > 0.5 else "Could Not Become Drug Addict"
# # # #
# # # #     st.markdown(f"### Prediction: **{prediction}**")
# # #
# # #
# # # import streamlit as st
# # # import pandas as pd
# # # import pickle
# # #
# # # # Page settings
# # # st.set_page_config(page_title="Drug Addiction Prediction", layout="centered")
# # # st.title("🧠 Drug Addiction Risk Predictor")
# # #
# # # st.markdown("""
# # # Welcome! Please fill out the form below with the individual's socio-psychological and behavioral profile.
# # # The model will predict if the person **Could Become a Drug Addict** or **Could Not Become a Drug Addict**.
# # # """)
# # #
# # # st.markdown("---")
# # #
# # # with st.form("drug_form"):
# # #     col1, col2 = st.columns(2)
# # #
# # #     with col1:
# # #         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
# # #         education = st.selectbox("Education Level", ["High School", "Bachelor's", "No Formal Education", "Master's", "PhD"])
# # #         occupation = st.selectbox("Occupation", ["Student", "Unemployed", "Teacher", "Business", "Laborer", "Engineer", "Clerk", "Artist", "Doctor"])
# # #         income = st.selectbox("Income Level", ["Low", "Medium", "High"])
# # #         medical_condition = st.selectbox("Medical Condition", ["Healthy", "Diabetes", "Heart Disease", "Anxiety", "Hypertension", "Depression"])
# # #         social_behavior = st.selectbox("Social Behavior", ["No Criminal Record", "Multiple Arrests", "Minor Offense", "Rehab Attended", "Therapy Ongoing"])
# # #         peer_influence = st.selectbox("Peer Influence", ["No Influence", "Some Friends Use", "Many Friends Use", "Peer Pressure"])
# # #         living_situation = st.selectbox("Living Situation", ["With Family/Relatives", "Hostel/Hall", "Alone"])
# # #         legal_issues = st.selectbox("Legal Issues", ["No", "Yes"])
# # #         drug_motive = st.selectbox("Drug Motive", [
# # #             "Disease, Should avoid", "Disease", "Social trend", "Should avoid",
# # #             "Social trend, Should avoid", "Disease, Social trend", "Disease, Social trend, Should avoid"])
# # #
# # #     with col2:
# # #         social_time = st.selectbox("Social Time Spent", ["Friends", "Family/ Relatives", "Alone", "Job/Work place", "Hostel", "Business", "School"])
# # #         life_failure = st.selectbox("Life Failure", ["No", "Yes"])
# # #         mental_health = st.selectbox("Mental Health Issues", ["Anxiety/Stress", "Depression/Guilt", "None / I don't know", "Anger Issues", "Multiple Conditions"])
# # #         lives_with_user = st.selectbox("Lives With User", ["No", "Yes", "Not sure"])
# # #         smoking_status = st.selectbox("Smoking Status", ["Yes, every day.", "Yes, occasionally", "No, I don't"])
# # #         drug_experience = st.selectbox("Drug Experience", ["Yes", "No"])
# # #         friend_influence = st.selectbox("Friend Influence", ["No, they don't", "Yes, often they do"])
# # #         willingness = st.selectbox("Willingness To Try", ["no", "maybe", "yes"])
# # #         self_control = st.selectbox("Self Control", ["No, It's not possible", "Yes, It's possible"])
# # #         usage_frequency = st.selectbox("Usage Frequency", ["Regularly", "Never/ Not applicable", "Occasionally", "Once/twice a week"])
# # #
# # #     submit = st.form_submit_button("🔍 Predict")
# # #
# # # if submit:
# # #     input_dict = {
# # #         "Gender": gender,
# # #         "Education_Level": education,
# # #         "Occupation": occupation,
# # #         "Income_Level": income,
# # #         "Medical_Condition": medical_condition,
# # #         "Social_Behavior": social_behavior,
# # #         "Peer_Influence": peer_influence,
# # #         "Living_Situation": living_situation,
# # #         "Legal_Issues": legal_issues,
# # #         "Drug_Motive": drug_motive,
# # #         "Social_Time_Spent": social_time,
# # #         "Life_Failure": life_failure,
# # #         "Mental_Health_Issues": mental_health,
# # #         "Lives_With_User": lives_with_user,
# # #         "Smoking_Status": smoking_status,
# # #         "Drug_Experience": drug_experience,
# # #         "Friend_Influence": friend_influence,
# # #         "Willingness_To_Try": willingness,
# # #         "Self_Control": self_control,
# # #         "Usage_Frequency": usage_frequency
# # #     }
# # #
# # #     input_df = pd.DataFrame([input_dict])
# # #
# # #     try:
# # #         with open("drug_addiction_model.pkl", "rb") as f:
# # #             model = pickle.load(f)
# # #
# # #         # Assume you have a label encoder or pipeline in model
# # #         prediction = model.predict(input_df)
# # #         result = prediction[0]
# # #
# # #         if result == "Could become Drug Addict":
# # #             st.error("🔴 **Prediction:** The individual *could become a drug addict*.")
# # #         else:
# # #             st.success("🟢 **Prediction:** The individual *could not become a drug addict*.")
# # #
# # #     except Exception as e:
# # #         st.error(f"❌ Prediction failed: {e}")
# # #
# #
# #
# #
# # import streamlit as st
# # import pandas as pd
# # import pickle
# #
# # # Page settings
# # st.set_page_config(page_title="Drug Addiction Prediction", layout="centered")
# # st.title("🧠 Drug Addiction Risk Predictor")
# #
# # st.markdown("""
# # Welcome! Please fill out the form below with the individual's socio-psychological and behavioral profile.
# # The model will predict if the person **Could Become a Drug Addict** or **Could Not Become a Drug Addict**.
# # """)
# #
# # st.markdown("---")
# #
# # with st.form("drug_form"):
# #     col1, col2 = st.columns(2)
# #
# #     with col1:
# #         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
# #         education = st.selectbox("Education Level", ["High School", "Bachelor's", "No Formal Education", "Master's", "PhD"])
# #         occupation = st.selectbox("Occupation", ["Student", "Unemployed", "Teacher", "Business", "Laborer", "Engineer", "Clerk", "Artist", "Doctor"])
# #         income = st.selectbox("Income Level", ["Low", "Medium", "High"])
# #         medical_condition = st.selectbox("Medical Condition", ["Healthy", "Diabetes", "Heart Disease", "Anxiety", "Hypertension", "Depression"])
# #         social_behavior = st.selectbox("Social Behavior", ["No Criminal Record", "Multiple Arrests", "Minor Offense", "Rehab Attended", "Therapy Ongoing"])
# #         peer_influence = st.selectbox("Peer Influence", ["No Influence", "Some Friends Use", "Many Friends Use", "Peer Pressure"])
# #         living_situation = st.selectbox("Living Situation", ["With Family/Relatives", "Hostel/Hall", "Alone"])
# #         legal_issues = st.selectbox("Legal Issues", ["No", "Yes"])
# #         drug_motive = st.selectbox("Drug Motive", [
# #             "Disease, Should avoid", "Disease", "Social trend", "Should avoid",
# #             "Social trend, Should avoid", "Disease, Social trend", "Disease, Social trend, Should avoid"])
# #
# #     with col2:
# #         social_time = st.selectbox("Social Time Spent", ["Friends", "Family/ Relatives", "Alone", "Job/Work place", "Hostel", "Business", "School"])
# #         life_failure = st.selectbox("Life Failure", ["No", "Yes"])
# #         mental_health = st.selectbox("Mental Health Issues", ["Anxiety/Stress", "Depression/Guilt", "None / I don't know", "Anger Issues", "Multiple Conditions"])
# #         lives_with_user = st.selectbox("Lives With User", ["No", "Yes", "Not sure"])
# #         smoking_status = st.selectbox("Smoking Status", ["Yes, every day.", "Yes, occasionally", "No, I don't"])
# #         drug_experience = st.selectbox("Drug Experience", ["Yes", "No"])
# #         friend_influence = st.selectbox("Friend Influence", ["No, they don't", "Yes, often they do"])
# #         willingness = st.selectbox("Willingness To Try", ["no", "maybe", "yes"])
# #         self_control = st.selectbox("Self Control", ["No, It's not possible", "Yes, It's possible"])
# #         usage_frequency = st.selectbox("Usage Frequency", ["Regularly", "Never/ Not applicable", "Occasionally", "Once/twice a week"])
# #
# #     submit = st.form_submit_button("🔍 Predict")
# #
# # if submit:
# #     input_dict = {
# #         "Gender": gender,
# #         "Education_Level": education,
# #         "Occupation": occupation,
# #         "Income_Level": income,
# #         "Medical_Condition": medical_condition,
# #         "Social_Behavior": social_behavior,
# #         "Peer_Influence": peer_influence,
# #         "Living_Situation": living_situation,
# #         "Legal_Issues": legal_issues,
# #         "Drug_Motive": drug_motive,
# #         "Social_Time_Spent": social_time,
# #         "Life_Failure": life_failure,
# #         "Mental_Health_Issues": mental_health,
# #         "Lives_With_User": lives_with_user,
# #         "Smoking_Status": smoking_status,
# #         "Drug_Experience": drug_experience,
# #         "Friend_Influence": friend_influence,
# #         "Willingness_To_Try": willingness,
# #         "Self_Control": self_control,
# #         "Usage_Frequency": usage_frequency
# #     }
# #
# #     input_df = pd.DataFrame([input_dict])
# #
# #     try:
# #         # Load model from the uploaded path
# #         with open("D:\AI Project\model.pkl", "rb") as f:
# #             model = pickle.load(f)
# #
# #         # Predict (assumes your model is a pipeline and handles preprocessing)
# #         prediction = model.predict(input_df)
# #         result = prediction[0]
# #
# #         if result == "Could become Drug Addict":
# #             st.error("🔴 **Prediction:** The individual *could become a drug addict*.")
# #         else:
# #             st.success("🟢 **Prediction:** The individual *could not become a drug addict*.")
# #
# #     except Exception as e:
# #         st.error(f"❌ Prediction failed: {e}")
#
#
# import streamlit as st
# import pandas as pd
# import pickle
#
# # Page settings
# st.set_page_config(page_title="Drug Addiction Prediction", layout="centered")
# st.title("🧠 Drug Addiction Risk Predictor")
#
# st.markdown("""
# Welcome! Please fill out the form below with the individual's socio-psychological and behavioral profile.
# The model will predict if the person **Could Become a Drug Addict** or **Could Not Become a Drug Addict**.
# """)
#
# st.markdown("---")
#
# with st.form("drug_form"):
#     col1, col2 = st.columns(2)
#
#     with col1:
#         age = st.number_input("👤 Age", min_value=1, max_value=120, step=1)
#         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
#         education = st.selectbox("Education Level", ["High School", "Bachelor's", "No Formal Education", "Master's", "PhD"])
#         occupation = st.selectbox("Occupation", ["Student", "Unemployed", "Teacher", "Business", "Laborer", "Engineer", "Clerk", "Artist", "Doctor"])
#         income = st.selectbox("Income Level", ["Low", "Medium", "High"])
#         medical_condition = st.selectbox("Medical Condition", ["Healthy", "Diabetes", "Heart Disease", "Anxiety", "Hypertension", "Depression"])
#         social_behavior = st.selectbox("Social Behavior", ["No Criminal Record", "Multiple Arrests", "Minor Offense", "Rehab Attended", "Therapy Ongoing"])
#         peer_influence = st.selectbox("Peer Influence", ["No Influence", "Some Friends Use", "Many Friends Use", "Peer Pressure"])
#         living_situation = st.selectbox("Living Situation", ["With Family/Relatives", "Hostel/Hall", "Alone"])
#         legal_issues = st.selectbox("Legal Issues", ["No", "Yes"])
#         drug_motive = st.selectbox("Drug Motive", [
#             "Disease, Should avoid", "Disease", "Social trend", "Should avoid",
#             "Social trend, Should avoid", "Disease, Social trend", "Disease, Social trend, Should avoid"])
#
#     with col2:
#         social_time = st.selectbox("Social Time Spent", ["Friends", "Family/ Relatives", "Alone", "Job/Work place", "Hostel", "Business", "School"])
#         life_failure = st.selectbox("Life Failure", ["No", "Yes"])
#         mental_health = st.selectbox("Mental Health Issues", ["Anxiety/Stress", "Depression/Guilt", "None / I don't know", "Anger Issues", "Multiple Conditions"])
#         lives_with_user = st.selectbox("Lives With User", ["No", "Yes", "Not sure"])
#         smoking_status = st.selectbox("Smoking Status", ["Yes, every day.", "Yes, occasionally", "No, I don't"])
#         drug_experience = st.selectbox("Drug Experience", ["Yes", "No"])
#         friend_influence = st.selectbox("Friend Influence", ["No, they don't", "Yes, often they do"])
#         willingness = st.selectbox("Willingness To Try", ["no", "maybe", "yes"])
#         self_control = st.selectbox("Self Control", ["No, It's not possible", "Yes, It's possible"])
#         usage_frequency = st.selectbox("Usage Frequency", ["Regularly", "Never/ Not applicable", "Occasionally", "Once/twice a week"])
#
#     submit = st.form_submit_button("🔍 Predict")
#
# if submit:
#     input_dict = {
#         "Age": age,
#         "Gender": gender,
#         "Education_Level": education,
#         "Occupation": occupation,
#         "Income_Level": income,
#         "Medical_Condition": medical_condition,
#         "Social_Behavior": social_behavior,
#         "Peer_Influence": peer_influence,
#         "Living_Situation": living_situation,
#         "Legal_Issues": legal_issues,
#         "Drug_Motive": drug_motive,
#         "Social_Time_Spent": social_time,
#         "Life_Failure": life_failure,
#         "Mental_Health_Issues": mental_health,
#         "Lives_With_User": lives_with_user,
#         "Smoking_Status": smoking_status,
#         "Drug_Experience": drug_experience,
#         "Friend_Influence": friend_influence,
#         "Willingness_To_Try": willingness,
#         "Self_Control": self_control,
#         "Usage_Frequency": usage_frequency
#     }
#
#     input_df = pd.DataFrame([input_dict])
#
#     try:
#         with open("model.pkl", "rb") as f:
#             model = pickle.load(f)
#
#         # Assume you have a label encoder or pipeline in model
#         prediction = model.predict(input_df)
#         result = prediction[0]
#
#         if result == "Could become Drug Addict":
#             st.error("🔴 **Prediction:** The individual *could become a drug addict*.")
#         else:
#             st.success("🟢 **Prediction:** The individual *could not become a drug addict*.")
#             st.success("🟢 **Prediction:** The individual *could not become a drug addict*.")
#
#     except Exception as e:
#         st.error(f"❌ Prediction failed: {e}")
from doctest import debug

import streamlit as st
import pandas as pd
import pickle

# Set page configuration
st.set_page_config(page_title="Drug Addiction Risk Predictor", layout="wide", page_icon="🧠")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f8;
            padding: 20px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 0.5em 2em;
            border-radius: 10px;
            margin-top: 20px;
        }
        .stSelectbox > div, .stNumberInput > div {
            padding: 10px;
        }
        .big-font {
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
        }
        .title-font {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title-font'>🧠 Drug Addiction Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("Welcome! Please fill out the form below to predict the likelihood of drug addiction based on socio-psychological and behavioral attributes.")
st.markdown("---")

# Form
with st.form("drug_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("👤 Age", min_value=1, max_value=120, step=1)
        gender = st.selectbox("🚻 Gender", ["Female", "Male", "Other"])
        education = st.selectbox("🎓 Education Level", ["High School", "Bachelor's", "No Formal Education", "Master's", "PhD"])
        occupation = st.selectbox("💼 Occupation", ["Student", "Unemployed", "Teacher", "Business", "Laborer", "Engineer", "Clerk", "Artist", "Doctor"])
        income = st.selectbox("💰 Income Level", ["Low", "Medium", "High"])
        medical_condition = st.selectbox("🏥 Medical Condition", ["Healthy", "Diabetes", "Heart Disease", "Anxiety", "Hypertension", "Depression"])
        social_behavior = st.selectbox("🧑‍🤝‍🧑 Social Behavior", ["No Criminal Record", "Multiple Arrests", "Minor Offense", "Rehab Attended", "Therapy Ongoing"])
        peer_influence = st.selectbox("👥 Peer Influence", ["No Influence", "Some Friends Use", "Many Friends Use", "Peer Pressure"])
        living_situation = st.selectbox("🏠 Living Situation", ["With Family/Relatives", "Hostel/Hall", "Alone"])
        legal_issues = st.selectbox("⚖️ Legal Issues", ["No", "Yes"])
        drug_motive = st.selectbox("🎯 Drug Motive", [
            "Disease, Should avoid", "Disease", "Social trend", "Should avoid",
            "Social trend, Should avoid", "Disease, Social trend", "Disease, Social trend, Should avoid"])

    with col2:
        social_time = st.selectbox("⌛ Social Time Spent", ["Friends", "Family/ Relatives", "Alone", "Job/Work place", "Hostel", "Business", "School"])
        life_failure = st.selectbox("💔 Life Failure", ["No", "Yes"])
        mental_health = st.selectbox("🧠 Mental Health Issues", ["Anxiety/Stress", "Depression/Guilt", "None / I don't know", "Anger Issues", "Multiple Conditions"])
        lives_with_user = st.selectbox("🏘️ Lives With Drug User", ["No", "Yes", "Not sure"])
        smoking_status = st.selectbox("🚬 Smoking Status", ["Yes, every day.", "Yes, occasionally", "No, I don't"])
        drug_experience = st.selectbox("💊 Past Drug Experience", ["Yes", "No"])
        friend_influence = st.selectbox("🧑‍🤝‍🧑 Friend Influence", ["No, they don't", "Yes, often they do"])
        willingness = st.selectbox("🤔 Willingness To Try", ["no", "maybe", "yes"])
        self_control = st.selectbox("🧘 Self Control", ["No, It's not possible", "Yes, It's possible"])
        usage_frequency = st.selectbox("📅 Usage Frequency", ["Regularly", "Never/ Not applicable", "Occasionally", "Once/twice a week"])

    submit = st.form_submit_button("🔍 Predict Risk")

# Prediction
if submit:
    input_dict = {
        "Age": age,
        "Gender": gender,
        "Education_Level": education,
        "Occupation": occupation,
        "Income_Level": income,
        "Medical_Condition": medical_condition,
        "Social_Behavior": social_behavior,
        "Peer_Influence": peer_influence,
        "Living_Situation": living_situation,
        "Legal_Issues": legal_issues,
        "Drug_Motive": drug_motive,
        "Social_Time_Spent": social_time,
        "Life_Failure": life_failure,
        "Mental_Health_Issues": mental_health,
        "Lives_With_User": lives_with_user,
        "Smoking_Status": smoking_status,
        "Drug_Experience": drug_experience,
        "Friend_Influence": friend_influence,
        "Willingness_To_Try": willingness,
        "Self_Control": self_control,
        "Usage_Frequency": usage_frequency
    }

    input_df = pd.DataFrame([input_dict])

    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        prediction = model.predict(input_df)
        result = prediction[0]

        st.markdown("---")
        if result == "Could become Drug Addict":
            st.error("🔴 The individual **could become a drug addict.**")
            st.snow()
        else:
            st.success("🟢 The individual **is unlikely to become a drug addict.**")
            st.balloons()

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")



# python -m streamlit run app.py


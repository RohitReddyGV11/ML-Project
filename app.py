import streamlit as st
from src.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write(
    """
    This application predicts **Math Score** based on student demographics 
    and academic performance using a trained Machine Learning model.
    """
)

st.divider()

st.subheader("📥 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender",["male","female"])
    race_ethnicity = st.selectbox("Race / Ethnicity",["group A","group B","group C","group D","group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education",["some high school","high school","some college","associate's degree","bachelor's degree","master's degree"])

with col2:
    lunch = st.selectbox("Lunch",["standard","free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course",["none","completed"])
    reading_score = st.number_input("Reading Score",min_value=0,max_value=100,value=50)
    writing_score = st.number_input("Writing Score",min_value=0,max_value=100,value=50)

st.divider()

if st.button("🔮 Predict Math Score"):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        final_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(final_df)

        st.success(f"📊 **Predicted Math Score:** {round(prediction[0], 2)}")

    except Exception as e:
        st.error("❌ Something went wrong during prediction")
        st.exception(e)
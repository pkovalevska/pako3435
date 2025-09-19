import streamlit as st

st.title("Patricija Kovalevska")

st.markdown("""
## About My Project in the DSHI Course

During the DSHI course, I worked on a project using the **UCI Heart Disease dataset** to predict whether a patient has heart disease. I cleaned and prepared the data, handled missing values, and selected key features like **chest pain type, blood pressure, and cholesterol**. I explored the data with charts and statistics to understand patterns and relationships between variables.

For modeling, I transformed the target into a **binary variable** and trained several classifiers, including:
- Decision Trees  
- Random Forests  
- KNN  
- SVM  
- Gradient Boosting  

**Random Forest** showed the best overall performance, with good accuracy and F1-score, while **KNN** had the highest recall. The project focused on analysis and modeling, and it was **not deployed as a web application**.
""")

# Optional: use HTML for more control (like justification and scaling)
st.markdown("""
<div style='text-align: justify; font-size:16px; line-height:1.6;'>
During the DSHI course, I worked on a project using the <b>UCI Heart Disease dataset</b> to predict whether a patient has heart disease. I cleaned and prepared the data, handled missing values, and selected key features like <b>chest pain type, blood pressure, and cholesterol</b>. I explored the data with charts and statistics to understand patterns and relationships between variables.

For modeling, I transformed the target into a <b>binary variable</b> and trained several classifiers, including Decision Trees, Random Forests, KNN, SVM, and Gradient Boosting. <b>Random Forest</b> showed the best overall performance, with good accuracy and F1-score, while <b>KNN</b> had the highest recall. The project focused on analysis and modeling, and it was <b>not deployed</b> as a web application.
</div>
""", unsafe_allow_html=True)

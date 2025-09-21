import streamlit as st

st.title("Patricija Kovalevska")

st.markdown("""
## About My Project in the DSHI Course

During the DSHI course, I worked on a project using the **UCI Heart Disease dataset** to predict whether a patient has heart disease or not. I cleaned and prepared the data, handled missing values, and selected key features like **chest pain type, blood pressure, and cholesterol**. I explored the data to identify patterns between variables using bivariate analytical questions and data visualization.

For modeling, I transformed the target into a **binary variable** and trained several classifiers, including:
- Decision Trees  
- Random Forests  
- KNN  
- SVM  
- Gradient Boosting  

**Random Forest** showed the best overall performance, with good accuracy and F1-score, while **KNN** had the highest recall. After analysis, it was decided **not deployed the model**.
""")


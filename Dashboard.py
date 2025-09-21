import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
# import numpy as np

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# # Add a slider to the sidebar:
# add_slider = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# Adding wigets to the main dashboard. Keeping previous content of teacher.
import streamlit as st
import pandas as pd
import numpy as np

# Page title
st.title("🎓 Student Research Dashboard")

st.markdown("This is the dashboard page with input widgets, synthetic data, and a chart.")

# --- Input Widgets ---
st.header("📌 Research Information")

# 1. Dropdown: Program of study
program = st.selectbox(
    "Select your program of study:",
    ["Computer Science", "Data Science", "Public Health", "Health Informatics", "Biomedical Engineering"]
)

# 2. Multiple choice: Research topics in healthcare
research_topics = st.multiselect(
    "Select research topics in healthcare:",
    [
        "AI in Medical Imaging",
        "Telemedicine",
        "Wearable Health Devices",
        "Genomics & Precision Medicine",
        "Mental Health Analytics",
        "Healthcare Policy & Management",
        "Chronic Disease Prediction"
    ]
)

# 3. Boolean: Have you decided on a topic?
decided = st.checkbox("✅ Have you decided on your research topic?")

# --- Synthetic Data ---
st.header("📊 Example Data")

# Generate random synthetic data
np.random.seed(42)
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Value": np.random.randint(10, 100, 5)
})

# Show data
st.write("Here is some example data:")
st.dataframe(data)

# --- Chart ---
st.bar_chart(data.set_index("Category"))

# --- Summary ---
st.header("📝 Summary")
st.write(f"**Program Selected:** {program}")
st.write(f"**Research Topics Chosen:** {', '.join(research_topics) if research_topics else 'None'}")
st.write(f"**Decided on Topic?** {'Yes' if decided else 'No'}")


####

# --- 2. Multiple choice: Research topics in healthcare ---
st.header("🔬 Select Research Topics in Healthcare")

topics = [
    "AI in Medical Imaging",
    "Telemedicine",
    "Wearable Health Devices",
    "Genomics & Precision Medicine",
    "Mental Health Analytics",
    "Healthcare Policy & Management",
    "Chronic Disease Prediction"
]

# Show all options with checkboxes
research_topics = []
for topic in topics:
    if st.checkbox(topic, key=topic):
        research_topics.append(topic)

# --- 3. Boolean: Have you decided on a topic? ---

st.header("✅ Have you decided on a topic to write about?")

# Use columns for Yes / No buttons
col1, col2 = st.columns(2)
decided = None
with col1:
    if st.button("Yes"):
        decided = True
with col2:
    if st.button("No"):
        decided = False

# --- 2. Synthetic Data ---
st.header("📊 Example Research Data")

st.write("You can edit this synthetic dataset:")

# Example data with only one metric: Interest_Level
default_data = pd.DataFrame({
    "Category": ["AI", "Telemedicine", "Wearables", "Genomics", "Policy"],
    "Interest_Level": np.random.randint(1, 10, 5)
})

# Make editable in Streamlit
data = st.data_editor(default_data, num_rows="dynamic")

# Show a chart with horizontal labels
st.bar_chart(data.set_index("Category")["Interest_Level"])

# --- 3. Summary ---
st.header("📝 Summary")
if decided is not None:
    st.write(f"**Decided on Topic?** {'Yes' if decided else 'No'}")
else:
    st.write("**Decided on Topic?** Not answered yet")


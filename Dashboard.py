import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# Adding wigets to the main dashboard. Keeping previous content of teacher.
import streamlit as st
import pandas as pd
import numpy as np

# --- Page title ---
st.title("🎓 Student Research Dashboard")
st.markdown("This is the dashboard page with input widgets, synthetic data, and a chart.")

# --- 1. Input Widgets ---
st.header("📌 Research Information")

# Dropdown: Program of study
program = st.selectbox(
    "Select your program of study:",
    ["Computer Science", "Data Science", "Public Health", "Health Informatics", "Biomedical Engineering"]
)

# Multiple choice: Research topics in healthcare
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

research_topics = []
for topic in topics:
    if st.checkbox(topic, key=topic):
        research_topics.append(topic)

# Boolean: Have you decided on a topic?
st.header("✅ Have you decided on a topic to write about?")
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


default_data = pd.DataFrame({
    "Category": [
        "AI in MI",
        "Telemedicine",
        "Wearable HD",
        "Genomics & PM",
        "Mental Health",
        "Healthcare Policy",
        "Disease Prediction"
    ],
    "Interest_Level": np.random.randint(1, 10, 7)
})

# Editable in Streamlit
data = st.data_editor(default_data, num_rows="dynamic")

# Show chart
st.bar_chart(data.set_index("Category")["Interest_Level"])

# --- 3. Summary ---
st.header("📝 Summary")
st.write(f"**Program Selected:** {program}")
st.write(f"**Research Topics Chosen:** {', '.join(research_topics) if research_topics else 'None'}")
st.write(f"**Decided on Topic?** {'Yes' if decided else 'Not answered yet' if decided is None else 'No'}")





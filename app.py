import streamlit as st
import streamlit.components.v1 as components
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(page_title="AccessAble", page_icon="♿", layout="wide")

st.title("♿ AccessAble")
st.subheader("Accessibility Information for Important Locations")

st.write("Choose a location and check its accessibility features.")
st.write("Yes = Available | No = Not available | No info = Not verified")
st.write("Accessibility Score = (Number of Yes features / 6) x 100")

features = [
    "Ramp",
    "Lift",
    "Accessible Washrooms",
    "Tactile Path",
    "Braille Support",
    "Wheelchair Friendly Entrance"
]

locations = {
    "Katpadi Railway Station": {
        "latitude": 12.9614,
        "longitude": 79.1326,
        "type": "Railway Station",
        "features": ["Yes", "Yes", "Yes", "No info", "Yes", "Yes"]
    },
    "Sri Narayani Hospital": {
        "latitude": 12.8700,
        "longitude": 79.0800,
        "type": "Hospital",
        "features": ["Yes", "Yes", "Yes", "Yes", "No info", "Yes"]
    },
    "Vellore New Bus Station": {
        "latitude": 12.9347,
        "longitude": 79.1371,
        "type": "Bus Stand",
        "features": ["Yes", "Yes", "Yes", "No", "No", "Yes"]
    },
    "Health Centre - VIT Vellore": {
        "latitude": 12.9719,
        "longitude": 79.1602,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "TT - VIT Vellore": {
        "latitude": 12.9692,
        "longitude": 79.1559,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "SJT - VIT Vellore": {
        "latitude": 12.9711,
        "longitude": 79.1637,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "MGR Block - VIT Vellore": {
        "latitude": 12.9697,
        "longitude": 79.1578,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "Library - VIT Vellore": {
        "latitude": 12.9692,
        "longitude": 79.1567,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "PRP - VIT Vellore": {
        "latitude": 12.9717,
        "longitude": 79.1633,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    },
    "SMV - VIT Vellore": {
        "latitude": 12.9699,
        "longitude": 79.1565,
        "type": "College",
        "features": ["Yes", "Yes", "Yes", "No info", "No info", "Yes"]
    }
}

# Accessibility status colours
status_colours = {
    "Yes": ("#D9FBE5", "#166534", "#86EFAC"),
    "No": ("#FEE2E2", "#991B1B", "#FCA5A5"),
    "No info": ("#CFE2FF", "#174078", "#8BB9F0")
}

# Dropdown selection
place_options = [
    "VIT",
    "Katpadi Railway Station",
    "Sri Narayani Hospital",
    "Vellore New Bus Station"
]

selected_place = st.selectbox("Select a location", place_options)

if selected_place == "VIT":
    vit_options = [
        "Health Centre - VIT Vellore",
        "TT - VIT Vellore",
        "SJT - VIT Vellore",
        "MGR Block - VIT Vellore",
        "Library - VIT Vellore",
        "PRP - VIT Vellore",
        "SMV - VIT Vellore"
    ]
    chosen_location_name = st.selectbox(
        "Select a VIT building", vit_options
    )
else:
    chosen_location_name = selected_place

# Prepare demonstration ML training data
# Yes = 1, No = 0, No info = 0

training_data = []
training_labels = []

for location_name in locations:
    feature_values = []
    yes_count = 0

    for status in locations[location_name]["features"]:
        if status == "Yes":
            feature_values.append(1)
            yes_count = yes_count + 1
        else:
            feature_values.append(0)

    score = round((yes_count / 6) * 100)

    if score >= 80:
        category = 2
    elif score >= 50:
        category = 1
    else:
        category = 0

    training_data.append(feature_values)
    training_labels.append(category)

# Train the ML model
ml_model = DecisionTreeClassifier(random_state=42)
ml_model.fit(training_data, training_labels)

# Get selected location details
selected_data = locations[chosen_location_name]
selected_features = selected_data["features"]

st.divider()
st.header(chosen_location_name)
st.write("Location type:", selected_data["type"])

# Display Google Maps
latitude = selected_data["latitude"]
longitude = selected_data["longitude"]

map_url = (
    "https://maps.google.com/maps?q="
    + str(latitude) + "," + str(longitude)
    + "&z=16&output=embed"
)

components.iframe(map_url, height=400, scrolling=True)

st.subheader("Accessibility Features")

yes_count = 0
missing_count = 0
ml_input = []

for i in range(len(features)):
    status = selected_features[i]

    if status == "Yes":
        yes_count = yes_count + 1
        ml_input.append(1)
    elif status == "No":
        ml_input.append(0)
    else:
        missing_count = missing_count + 1
        ml_input.append(0)

    background, text_colour, border_colour = status_colours[status]

    st.markdown(
        f"""
        <div style="
            background-color:{background};
            color:{text_colour};
            border:1px solid {border_colour};
            border-radius:10px;
            padding:12px;
            margin:7px 0;
            font-weight:600;">
            {features[i]}: {status}
        </div>
        """,
        unsafe_allow_html=True
    )

score = round((yes_count / 6) * 100)

st.divider()
st.subheader("Accessibility Score")

st.metric("Recorded availability score", str(score) + "/100")
st.progress(score / 100)

st.write("Features marked Yes:", yes_count, "out of 6")
st.write("Features marked No info:", missing_count)

# Machine Learning Analysis
st.divider()
st.subheader("Machine Learning Analysis")

prediction = ml_model.predict([ml_input])[0]

if prediction == 2:
    predicted_category = "High Accessibility"
elif prediction == 1:
    predicted_category = "Moderate Accessibility"
else:
    predicted_category = "Low Accessibility"

st.success("ML Prediction: " + predicted_category)

st.info(
    "The Decision Tree Classifier categorizes the location into "
    "High, Moderate, or Low Accessibility based on its six recorded "
    "accessibility features. No info is counted as 0 for this "
    "demonstration only."
)

st.warning(
    "Accessibility information has not been independently verified. "
    "Please confirm the features with the relevant location before visiting."
)

st.divider()
st.subheader("How Accessibility Works")

st.write("""
- Ramp: Helps wheelchair users move between levels.
- Lift: Provides access between floors.
- Accessible Washrooms: Washrooms designed for accessibility.
- Tactile Path: Helps people with visual impairments navigate.
- Braille Support: Provides information through Braille.
- Wheelchair Friendly Entrance: Provides step-free entry.
""")

st.caption("AccessAble | Accessibility Information Project")

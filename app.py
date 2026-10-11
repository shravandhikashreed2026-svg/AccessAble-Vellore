import json
import re
import streamlit as st
import streamlit.components.v1 as components
from streamlit_mic_recorder import speech_to_text
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(
    page_title="AccessAble",
    page_icon="♿",
    layout="wide"
)

st.title("♿ AccessAble")
st.subheader("Accessibility Information for Important Locations")

st.write("Explore accessibility features or ask AccessAble using your voice.")
st.write("Yes = Available | No = Not available | No info = Not verified")

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

status_colours = {
    "Yes": ("#D9FBE5", "#166534", "#86EFAC"),
    "No": ("#FEE2E2", "#991B1B", "#FCA5A5"),
    "No info": ("#CFE2FF", "#174078", "#8BB9F0")
}

# Machine learning training
training_data = []
training_labels = []

for location in locations.values():
    values = [1 if status == "Yes" else 0
              for status in location["features"]]

    score = round((sum(values) / 6) * 100)

    if score >= 80:
        category = 2
    elif score >= 50:
        category = 1
    else:
        category = 0

    training_data.append(values)
    training_labels.append(category)

ml_model = DecisionTreeClassifier(random_state=42)
ml_model.fit(training_data, training_labels)


def get_score(location):
    return round(
        (location["features"].count("Yes") / 6) * 100
    )


def get_category(location):
    values = [
        1 if status == "Yes" else 0
        for status in location["features"]
    ]

    prediction = ml_model.predict([values])[0]

    if prediction == 2:
        return "High Accessibility"
    elif prediction == 1:
        return "Moderate Accessibility"
    return "Low Accessibility"


def find_location(text):
    query = text.lower()

    # Match longer names first to avoid partial matches.
    aliases = {
        "katpadi railway station": "Katpadi Railway Station",
        "katpadi station": "Katpadi Railway Station",
        "railway station": "Katpadi Railway Station",
        "sri narayani hospital": "Sri Narayani Hospital",
        "narayani hospital": "Sri Narayani Hospital",
        "vellore new bus station": "Vellore New Bus Station",
        "new bus station": "Vellore New Bus Station",
        "health centre": "Health Centre - VIT Vellore",
        "health center": "Health Centre - VIT Vellore",
        "vit health centre": "Health Centre - VIT Vellore",
        "vit health center": "Health Centre - VIT Vellore",
        "tt": "TT - VIT Vellore",
        "sjt": "SJT - VIT Vellore",
        "mgr": "MGR Block - VIT Vellore",
        "mgr block": "MGR Block - VIT Vellore",
        "library": "Library - VIT Vellore",
        "prp": "PRP - VIT Vellore",
        "smv": "SMV - VIT Vellore"
    }

    for alias in sorted(aliases, key=len, reverse=True):
        if re.search(r"\b" + re.escape(alias) + r"\b", query):
            return aliases[alias]

    return None


def make_answer(query, location_name):
    location = locations[location_name]
    recorded_features = location["features"]
    score = get_score(location)
    category = get_category(location)
    query = query.lower()

    feature_aliases = {
        "Ramp": ["ramp", "ramps"],
        "Lift": ["lift", "elevator", "elevators"],
        "Accessible Washrooms": [
            "washroom", "washrooms", "toilet", "toilets",
            "restroom", "restrooms", "bathroom", "bathrooms"
        ],
        "Tactile Path": ["tactile", "tactile path"],
        "Braille Support": ["braille"],
        "Wheelchair Friendly Entrance": [
            "wheelchair", "wheelchair friendly entrance",
            "step free entrance", "step-free entrance"
        ]
    }

    matched_feature = None

    for index, feature in enumerate(features):
        if any(word in query for word in feature_aliases[feature]):
            matched_feature = (index, feature)
            break

    if any(word in query for word in [
        "score", "percentage", "rating", "how accessible"
    ]) and not any(word in query for word in [
        "ramp", "lift", "elevator", "washroom", "toilet",
        "tactile", "braille", "wheelchair"
    ]):
        return (
            f"For {location_name}, the recorded accessibility "
            f"score is {score} out of 100. The machine learning "
            f"category is {category}. This is based on the "
            f"currently recorded features, not an independent "
            f"accessibility assessment."
        )

    if matched_feature:
        index, feature = matched_feature
        status = recorded_features[index]

        explanations = {
            "Yes": "is recorded as available",
            "No": "is recorded as not available",
            "No info": "has not been verified"
        }

        return (
            f"At {location_name}, {feature} "
            f"{explanations[status]}. "
            f"The recorded accessibility score is {score} out of 100. "
            "Please confirm this information before visiting."
        )

    details = []

    for feature, status in zip(features, recorded_features):
        if status == "Yes":
            phrase = "recorded as available"
        elif status == "No":
            phrase = "recorded as not available"
        else:
            phrase = "not verified"

        details.append(f"{feature}: {phrase}")

    return (
        f"Here is the accessibility information for {location_name}. "
        + ". ".join(details)
        + f". The recorded accessibility score is {score} out of 100. "
        + f"The machine learning category is {category}. "
        + "Some information has not been independently verified. "
        + "Please confirm the facilities with the location before visiting."
    )


# Voice assistant
st.divider()
st.header("🎙️ Talk to AccessAble")
st.write(
    "Ask about a location or a particular accessibility feature. "
    "For example, say: Is there a lift at Katpadi Railway Station?"
)

if "last_voice_location" not in st.session_state:
    st.session_state.last_voice_location = "Katpadi Railway Station"

if "voice_answer" not in st.session_state:
    st.session_state.voice_answer = ""

if "voice_question" not in st.session_state:
    st.session_state.voice_question = ""

st.info(
    "Press the microphone button, allow microphone access if asked, "
    "speak in English, and finish your request."
)

recognized_text = speech_to_text(
    language="en",
    start_prompt="🎙️ Start speaking",
    stop_prompt="⏹️ Stop recording",
    just_once=True,
    use_container_width=True,
    key="accessable_voice_input"
)

if recognized_text:
    st.session_state.voice_question = recognized_text

    detected_location = find_location(recognized_text)

    if detected_location:
        st.session_state.last_voice_location = detected_location

    query_lower = recognized_text.lower()

    if any(phrase in query_lower for phrase in [
        "hello", "hello accessable", "who are you",
        "what can you do"
    ]) and not find_location(recognized_text):
        st.session_state.voice_answer = (
            "Hello! I am AccessAble, your accessibility information "
            "assistant. You can ask me about ramps, lifts, washrooms, "
            "tactile paths, Braille support, wheelchair entrances, "
            "or the recorded accessibility score of a listed location."
        )
    else:
        st.session_state.voice_answer = make_answer(
            recognized_text,
            st.session_state.last_voice_location
        )

if st.session_state.voice_question:
    st.markdown("**You asked:**")
    st.write(st.session_state.voice_question)

if st.session_state.voice_answer:
    st.markdown("**AccessAble's answer:**")
    st.write(st.session_state.voice_answer)

    st.caption(
        "The answer is generated from the project's current dataset. "
        "Unverified information should not be treated as confirmed."
    )

    # Speak the answer in English.
    answer_json = json.dumps(
        st.session_state.voice_answer,
        ensure_ascii=True
    )

    components.html(
        f"""
        <div style="font-family:Arial,sans-serif;">
            <button id="playAnswer"
                style="padding:12px 18px;background:#166534;
                color:white;border:0;border-radius:8px;
                cursor:pointer;font-size:16px;">
                🔊 Play Answer in English
            </button>
            <button id="stopAnswer"
                style="padding:12px 18px;background:#991B1B;
                color:white;border:0;border-radius:8px;
                cursor:pointer;font-size:16px;margin-left:8px;">
                ⏹ Stop
            </button>
            <p id="speechStatus" aria-live="polite"></p>
        </div>

        <script>
            const answer = {answer_json};
            const playButton = document.getElementById("playAnswer");
            const stopButton = document.getElementById("stopAnswer");
            const status = document.getElementById("speechStatus");

            playButton.addEventListener("click", function() {{
                if (!("speechSynthesis" in window)) {{
                    status.textContent =
                        "Speech output is not supported by this browser.";
                    return;
                }}

                window.speechSynthesis.cancel();

                const utterance = new SpeechSynthesisUtterance(answer);
                utterance.lang = "en-IN";
                utterance.rate = 0.9;

                utterance.onstart = function() {{
                    status.textContent = "Speaking...";
                }};

                utterance.onend = function() {{
                    status.textContent = "Finished speaking.";
                }};

                utterance.onerror = function(event) {{
                    status.textContent =
                        "Could not play audio: " + event.error;
                }};

                window.speechSynthesis.speak(utterance);
            }});

            stopButton.addEventListener("click", function() {{
                if ("speechSynthesis" in window) {{
                    window.speechSynthesis.cancel();
                    status.textContent = "Audio stopped.";
                }}
            }});
        </script>
        """,
        height=110
    )

# Location explorer
st.divider()
st.header("Explore Locations")

place_options = [
    "VIT",
    "Katpadi Railway Station",
    "Sri Narayani Hospital",
    "Vellore New Bus Station"
]

selected_place = st.selectbox(
    "Select a location",
    place_options,
    key="location_dropdown"
)

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
        "Select a VIT building",
        vit_options,
        key="vit_building_dropdown"
    )
else:
    chosen_location_name = selected_place

selected_data = locations[chosen_location_name]
selected_features = selected_data["features"]

st.divider()
st.subheader(chosen_location_name)
st.write("Location type:", selected_data["type"])

map_url = (
    "https://maps.google.com/maps?q="
    + str(selected_data["latitude"])
    + ","
    + str(selected_data["longitude"])
    + "&z=16&output=embed"
)

components.iframe(map_url, height=400, scrolling=True)

st.subheader("Accessibility Features")

for feature, status in zip(features, selected_features):
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
            {feature}: {status}
        </div>
        """,
        unsafe_allow_html=True
    )

score = get_score(selected_data)

st.divider()
st.subheader("Accessibility Score")
st.metric("Recorded availability score", f"{score}/100")
st.progress(score / 100)

st.write("Features marked Yes:", selected_features.count("Yes"), "out of 6")
st.write("Features marked No info:", selected_features.count("No info"))

st.divider()
st.subheader("Machine Learning Analysis")

predicted_category = get_category(selected_data)
st.success("ML Prediction: " + predicted_category)

st.info(
    "This is an educational ML demonstration trained on the current "
    "small dataset. Categories are derived from the same six features "
    "and are not independent predictions. No info is counted as 0 "
    "for the model demonstration."
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

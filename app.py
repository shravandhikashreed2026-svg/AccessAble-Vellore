
import streamlit as st

st.set_page_config(
    page_title="AccessAble Vellore",
    page_icon="♿",
    layout="wide"
)

# Accessibility features
features = [
    "Ramp",
    "Lift",
    "Accessible Washrooms",
    "Tactile Path",
    "Braille Support",
    "Wheelchair Friendly Entrance"
]

# Location data provided for AccessAble Vellore
locations = [

    {
        "name": "Katpadi Railway Station",
        "type": "Railway Station",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "Yes",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "Sri Narayani Hospital",
        "type": "Hospital",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "Yes",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "Vellore New Bus Station",
        "type": "Bus Stand",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No",
            "Braille Support": "No",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "Health Centre - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "TT - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "SJT - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "MGR Block - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "Library - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "PRP - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    },

    {
        "name": "SMV - VIT Vellore",
        "type": "College",
        "access": {
            "Ramp": "Yes",
            "Lift": "Yes",
            "Accessible Washrooms": "Yes",
            "Tactile Path": "No info",
            "Braille Support": "No info",
            "Wheelchair Friendly Entrance": "Yes"
        }
    }
]

# Website heading
st.title("♿ AccessAble Vellore")

st.subheader(
    "Accessibility Information for Important Locations"
)

st.write(
    "Search for a location, select its type, and check accessibility features."
)

st.info(
    "Yes = Available | No = Not available | "
    "No info = Information is not available"
)

st.divider()

# Search box
search_name = st.text_input(
    "Search by Location Name",
    placeholder="Example: VIT, hospital, library"
)

# Location type selection
selected_type = st.selectbox(
    "Choose Location Type",
    [
        "All Locations",
        "College",
        "Hospital",
        "Railway Station",
        "Bus Stand",
        "Government Building"
    ]
)

# Accessibility feature selection
selected_feature = st.selectbox(
    "Choose Accessibility Feature",
    features
)

# Search button
search_button = st.button(
    "Search Locations",
    type="primary"
)

# Search logic
if search_button:

    count = 0

    st.header("Search Results")

    for location in locations:

        # Check location name
        if search_name.lower() in location["name"].lower():

            # Check location type
            if selected_type == "All Locations":
                type_match = True

            elif location["type"] == selected_type:
                type_match = True

            else:
                type_match = False

            # Display matching locations
            if type_match:

                count = count + 1

                with st.expander(location["name"]):

                    st.write(
                        "Location Type:",
                        location["type"]
                    )

                    # Display selected feature status
                    status = location["access"][selected_feature]

                    st.subheader("Selected Feature Status")

                    if status == "Yes":
                        st.success(
                            selected_feature + ": Yes - Available"
                        )

                    elif status == "No":
                        st.error(
                            selected_feature + ": No - Not available"
                        )

                    else:
                        st.info(
                            selected_feature + ": No info"
                        )

                    # Display every accessibility feature
                    st.subheader("All Accessibility Details")

                    for feature in features:

                        feature_status = location["access"][feature]

                        if feature_status == "Yes":
                            st.success(feature + ": Yes")

                        elif feature_status == "No":
                            st.error(feature + ": No")

                        else:
                            st.info(feature + ": No info")

    # Final result count
    if count == 0:

        st.warning(
            "No matching locations found. Try another search or location type."
        )

    else:

        st.success(
            "Total matching locations: " + str(count)
        )

st.divider()

st.caption(
    "AccessAble Vellore | Accessibility Information Project"
)

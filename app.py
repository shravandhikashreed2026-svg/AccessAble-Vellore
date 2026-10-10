
import streamlit as st

st.set_page_config(
    page_title="AccessAble Vellore",
    page_icon="♿",
    layout="wide"
)

# FRONT PAGE
st.title("♿ AccessAble Vellore")

st.subheader("Accessibility Information for Important Locations")

st.write(
    "Choose a location and check its accessibility features."
)

st.write(
    "Yes = Available | No = Not available | "
    "No info = Treated as not available"
)

st.write(
    "Availability Score = "
    "(Number of features marked Yes / 6) x 100"
)

st.divider()

# ACCESSIBILITY FEATURES
features = [
    "Ramp",
    "Lift",
    "Accessible Washrooms",
    "Tactile Path",
    "Braille Support",
    "Wheelchair Friendly Entrance"
]

# LOCATION DATABASE
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

# HOW ACCESSIBILITY WORKS
st.header("How Accessibility Works")

st.write(
    "Accessibility means making places easier to enter, "
    "move around, and use for people with different access needs."
)

st.write(
    "Ramp: Helps people move between different levels."
)

st.write(
    "Lift: Helps people reach different floors."
)

st.write(
    "Accessible Washrooms: Designed to make washrooms "
    "easier to access and use."
)

st.write(
    "Tactile Path: Textured ground indicators that help "
    "people with visual impairments navigate."
)

st.write(
    "Braille Support: Braille labels or signs that provide "
    "information to people who read Braille."
)

st.write(
    "Wheelchair Friendly Entrance: An entrance designed "
    "to make access easier for wheelchair users."
)

st.divider()

# LOCATION SELECTION
st.header("Choose a Location")

selected_place = st.selectbox(
    "Location",
    [
        "VIT",
        "Katpadi Railway Station",
        "Sri Narayani Hospital",
        "Vellore New Bus Station"
    ]
)

# VIT SUBDIVISIONS
if selected_place == "VIT":

    selected_vit_place = st.selectbox(
        "Choose a place inside VIT Vellore",
        [
            "Health Centre - VIT Vellore",
            "TT - VIT Vellore",
            "SJT - VIT Vellore",
            "MGR Block - VIT Vellore",
            "Library - VIT Vellore",
            "PRP - VIT Vellore",
            "SMV - VIT Vellore"
        ]
    )

    chosen_location_name = selected_vit_place

else:
    chosen_location_name = selected_place

# ACCESSIBILITY FEATURE SELECTION
selected_feature = st.selectbox(
    "Choose an accessibility feature",
    features
)

# CHECK ACCESSIBILITY
if st.button("Check Accessibility", type="primary"):

    for location in locations:

        if location["name"] == chosen_location_name:

            st.divider()

            st.header(location["name"])

            st.write("Location type: " + location["type"])

            # DISPLAY SELECTED FEATURE
            st.subheader("Selected Feature")

            status = location["access"][selected_feature]

            if status == "Yes":

                st.markdown(
                    f"""
                    <div style="
                        background-color: #D9FBE5;
                        color: #166534;
                        padding: 14px;
                        margin: 8px 0;
                        border-radius: 8px;
                        border: 1px solid #86EFAC;
                        font-size: 17px;
                        font-weight: 600;
                    ">
                        {selected_feature}: Yes
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif status == "No":

                st.markdown(
                    f"""
                    <div style="
                        background-color: #FEE2E2;
                        color: #991B1B;
                        padding: 14px;
                        margin: 8px 0;
                        border-radius: 8px;
                        border: 1px solid #FCA5A5;
                        font-size: 17px;
                        font-weight: 600;
                    ">
                        {selected_feature}: No
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        background-color: #CFE2FF;
                        color: #174078;
                        padding: 14px;
                        margin: 8px 0;
                        border-radius: 8px;
                        border: 1px solid #8BB9F0;
                        font-size: 17px;
                        font-weight: 600;
                    ">
                        {selected_feature}: No info
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # DISPLAY ALL ACCESSIBILITY DETAILS
            st.subheader("All Accessibility Details")

            yes_count = 0

            for feature in features:

                feature_status = location["access"][feature]

                if feature_status == "Yes":

                    yes_count = yes_count + 1

                    st.markdown(
                        f"""
                        <div style="
                            background-color: #D9FBE5;
                            color: #166534;
                            padding: 14px;
                            margin: 8px 0;
                            border-radius: 8px;
                            border: 1px solid #86EFAC;
                            font-size: 17px;
                            font-weight: 600;
                        ">
                            {feature}: Yes
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                elif feature_status == "No":

                    st.markdown(
                        f"""
                        <div style="
                            background-color: #FEE2E2;
                            color: #991B1B;
                            padding: 14px;
                            margin: 8px 0;
                            border-radius: 8px;
                            border: 1px solid #FCA5A5;
                            font-size: 17px;
                            font-weight: 600;
                        ">
                            {feature}: No
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        f"""
                        <div style="
                            background-color: #CFE2FF;
                            color: #174078;
                            padding: 14px;
                            margin: 8px 0;
                            border-radius: 8px;
                            border: 1px solid #8BB9F0;
                            font-size: 17px;
                            font-weight: 600;
                        ">
                            {feature}: No info
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # CALCULATE AVAILABILITY SCORE
            availability_score = round(
                (yes_count / 6) * 100
            )

            # DISPLAY AVAILABILITY SCORE
            st.subheader("Availability Score")

            st.metric(
                "Score",
                str(availability_score) + "/100"
            )

            st.write(
                str(yes_count) + " out of 6 features are marked Yes."
            )

            st.progress(availability_score / 100)

            st.caption(
                "This project-defined score is based on the six "
                "features recorded in the database. It is not an "
                "official accessibility certification."
            )

            break

st.divider()

st.caption(
    "AccessAble Vellore | Accessibility Information Project"
)

import streamlit as st
import pandas as pd
import re

# =========================================================
# 1. PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="KNS Smart Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

SCHOOL_NAME = "Khair-un-Nas School Swat"
SCHOOL_ADDRESS = "Gunbad Maira, Mingora, Swat"
PRINCIPAL = "Sir Khalid"
SCHOOL_TIMING = "8:00 AM to 2:00 PM"
SCHOOL_PHONE = "0946-700232"

# =========================================================
# 2. PROFESSIONAL BLUE THEME
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #f3f6fc;
}
[data-testid="stSidebar"] {
    background-color: #102448;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #102448, #2457a7);
    padding: 28px;
    border-radius: 16px;
    color: white;
    margin-bottom: 20px;
}
.hero h1 {
    color: white;
    margin-bottom: 8px;
}
.hero p {
    color: #e4edff;
    font-size: 16px;
}
.info-card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #dce5f4;
    margin-bottom: 12px;
}
div.stButton > button {
    border-radius: 9px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 3. SENIOR TIMETABLE: CLASSES FIVE TO TEN
# =========================================================

SENIOR_TIMES = [
    ("Period 0", "7:50–8:15 AM"),
    ("Period 1", "8:15–8:50 AM"),
    ("Period 2", "8:50–9:25 AM"),
    ("Period 3", "9:25–10:00 AM"),
    ("Period 4", "10:00–10:30 AM"),
    ("Period 5", "10:30–11:00 AM"),
    ("Period 6", "11:00–11:30 AM"),
]

# Each entry is (subject, teacher).
# Entries are kept in the order supplied by the school.

SENIOR = {
    "5th-R": [
        ("English", "Miss Sidra Salman"),
        ("Science", "Sir Shah Sawar"),
        ("Urdu", "Miss Rukhsar"),
        ("Maths", "Sir Shakoor"),
        ("S. Studies", "Sir Yaseen Zaifullah"),
        ("Islamiyat / M.Q", "Sir Abbas"),
    ],

    "5th-J": [
        ("Urdu", "Miss Rukhsar"),
        ("S. Studies", "Miss Sidra Salman"),
        ("Maths", "Sir M Shakoor"),
        ("Science", "Sir Shah Sawar"),
        ("Islamiyat / M.Q", "Sir Abbas"),
        ("English", "Miss Sidra Salman"),
    ],

    "6th-R/J": [
        ("History", "Sir Yaseen Zaifullah"),
        ("Islamiyat / M.Q", "Sir Abbas"),
        ("Science", "Sir Shah Sawar"),
        ("English", "Sir Arif"),
        ("Science", "Sir Shakeeb"),
        ("Urdu", "Sir Siddique"),
    ],

    "7th-Jasmine": [
        ("Islamiyat / M.Q", "Sir Abbas"),
        ("Maths", "Sir Shakeeb"),
        ("History", "Sir Yaseen Zaifullah"),
        ("English", "Miss Sidra Salman"),
        ("Urdu", "Miss Rukhsar"),
        ("Science", "Sir Shah Sawar"),
    ],

    "7th-Rose": [
        ("Maths", "Sir Amjad"),
        ("History", "Sir Yaseen Zaifullah"),
        ("Islamiyat / M.Q", "Miss Sidra Salman"),
        ("English", "Sir Abbas"),
        ("Science", "Sir Shah Sawar"),
        ("Science", "Miss Rukhsar"),
    ],

    "8th-Jasmine": [
        ("Maths", "Sir Amjad"),
        ("Biology", "Sir Siddique"),
        ("Urdu", "Sir Arif"),
        ("Chemistry", "Sir Shakeeb"),
        ("English", "Sir Arif"),
        ("Physics", "Sir M Shakoor"),
    ],

    "8th-Rose": [
        ("Islamiyat / M.Q", "Sir Siddique"),
        ("Biology", "Sir Arif"),
        ("Chemistry", "Sir Shakeeb"),
        ("Maths", "Sir Amjad"),
        ("Physics", "Sir Shakoor"),
        ("Chemistry", "Sir Arif"),
    ],

    "9th-R/J": [
        ("Maths", "Sir Arif"),
        ("Physics", "Sir M Shakoor"),
        ("English", "Sir Shakeeb"),
        ("Pak Studies / AH", "Sir Amjad"),
        ("Islamiyat / M.Q", "Sir Siddique"),
        ("English", "Sir Khalid"),
    ],

    "10th-R/J": [
        ("Urdu", "Sir Majeedullah"),
        ("Chemistry", "Teacher not specified"),
        ("Physics", "Sir M Shakoor"),
        ("Physics", "Sir Asif"),
        ("Islamiyat / M.Q", "Sir Siddique"),
        ("Maths", "Sir Amjad"),
        ("Pak Studies / AH", "Sir Yaseen Zaifullah"),
    ],
}

# =========================================================
# 4. PRIMARY TIMETABLE: PLAY GROUP TO FOURTH
# =========================================================

PRIMARY_TIMES = [
    ("Assembly", "8:10–8:25 AM"),
    ("Period 1", "8:25–9:05 AM"),
    ("Period 2", "9:05–9:45 AM"),
    ("Period 3", "9:45–10:25 AM"),
    ("Period 4", "10:25–11:05 AM"),
    ("Period 5", "11:05–11:30 AM"),
    ("Period 6", "11:30 AM–12:10 PM"),
    ("Period 7", "12:10–12:50 PM"),
]

# offset 0 means the list begins with Assembly.
# offset 1 means the list begins with Period 1.

PRIMARY = {
    "Play Group": {
        "teacher": "Miss Shahida Rahman and Miss Ilham",
        "offset": 0,
        "subjects": [
            "Assembly",
            "English Reading",
            "English Writing",
            "Urdu Reading",
            "Break",
            "Urdu Writing",
            "Maths Reading",
            "Maths Writing",
        ],
    },

    "Nursery-O": {
        "teacher": "Miss Asma",
        "offset": 1,
        "subjects": [
            "English Reading",
            "English Writing",
            "Urdu Reading",
            "Urdu Writing",
            "Maths Reading",
            "Maths Writing",
        ],
    },

    "Nursery-P": {
        "teacher": "Miss Hafsa",
        "offset": 1,
        "subjects": [
            "English Reading",
            "English Writing",
            "Urdu Reading",
            "Urdu Writing",
            "Maths Reading",
            "Maths Writing",
        ],
    },

    "K.G-P": {
        "teacher": "Miss Sumaiya",
        "offset": 1,
        "subjects": [
            "English Reading",
            "English Writing",
            "Urdu/Pashto Reading",
            "Urdu/Pashto Writing",
            "Maths Reading",
            "Maths Writing",
        ],
    },

    "K.G-O": {
        "teacher": "Miss Noreen",
        "offset": 1,
        "subjects": [
            "English Reading",
            "English Writing",
            "Urdu/Pashto Reading",
            "Urdu/Pashto Writing",
            "Maths Reading",
            "Maths Writing",
        ],
    },

    "One-O": {
        "teacher": "Miss Ayesha",
        "offset": 1,
        "subjects": [
            "Maths",
            "Urdu",
            "English",
            "G. Knowledge",
            "Islamiyat",
            "Writing Class",
            "Pashto",
        ],
    },

    "One-P": {
        "teacher": "Miss Hira",
        "offset": 1,
        "subjects": [
            "Urdu",
            "Maths",
            "Islamiyat",
            "G. Knowledge",
            "Pashto",
            "English",
            "Writing Class",
        ],
    },

    "Two-P": {
        "teacher": "Miss Arzoo",
        "offset": 1,
        "subjects": [
            "G. Knowledge",
            "English",
            "Urdu",
            "Pashto",
            "English",
            "Maths",
            "Pashto",
        ],
    },

    "Two-O": {
        "teacher": "Miss Sanam",
        "offset": 1,
        "subjects": [
            "Urdu",
            "Pashto",
            "G. Knowledge",
            "English",
            "Break",
            "Islamiyat",
            "Writing Class",
        ],
    },

    "Three-P": {
        "teacher": "Miss Shabeena",
        "offset": 1,
        "subjects": [
            "Maths",
            "English",
            "Urdu",
            "G. Knowledge",
            "Islamiyat",
            "Writing Class",
        ],
    },

    "Three-O": {
        "teacher": "Miss Madeeha",
        "offset": 1,
        "subjects": [
            "Maths",
            "English",
            "Urdu",
            "G. Knowledge",
            "Islamiyat",
            "Writing Class",
        ],
    },

    "Fourth-O": {
        "teacher": "Miss Sumaira",
        "offset": 1,
        "subjects": [
            "Islamiyat",
            "S. Studies",
            "Science",
            "English",
            "Maths",
            "Urdu",
        ],
    },

    "Fourth-P": {
        "teacher": "Miss Sadaf",
        "offset": 1,
        "subjects": [
            "Islamiyat",
            "S. Studies",
            "Science",
            "Maths",
            "Urdu",
            "English",
        ],
    },
}

# =========================================================
# 5. GENERAL SCHOOL INFORMATION
# =========================================================

TEACHERS = [
    ("Zero Class", "Urdu", "Sir Majeedullah"),
    ("1st Class", "Chemistry", "Sir Saqib"),
    ("2nd Class", "Physics", "Sir Shakur"),
    ("3rd Class", "Biology", "Sir Asif"),
    ("4th Class", "Maths", "Sir Amjad"),
    ("6th Class", "Islamiyat and Mutalia Quran", "Sir Siddiq"),
    ("7th Class", "English", "Sir Arif"),
    ("Last Class", "Pakistan Studies", "Sir Yaseen"),
    ("10th Class", "Artificial Intelligence (AI)", "Sir Sufyan"),
]

# =========================================================
# 6. TIMETABLE DISPLAY FUNCTIONS
# =========================================================

def show_senior_timetable(class_name):
    """Display the timetable for a class from Five to Ten."""

    if class_name not in SENIOR:
        st.error("Timetable not found for this class.")
        return

    rows = []

    for index, (subject, teacher) in enumerate(SENIOR[class_name]):
        if index < len(SENIOR_TIMES):
            period, period_time = SENIOR_TIMES[index]
        else:
            period = f"Period {index}"
            period_time = "Time not specified"

        rows.append({
            "Period": period,
            "Time": period_time,
            "Subject": subject,
            "Teacher": teacher,
        })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "Subjects are shown in the order supplied. "
        "Please verify period alignment against the school's original timetable."
    )


def show_primary_timetable(class_name):
    """Display the timetable for Play Group through Fourth."""

    if class_name not in PRIMARY:
        st.error("Timetable not found for this class.")
        return

    details = PRIMARY[class_name]
    rows = []
    offset = details["offset"]

    for index, subject in enumerate(details["subjects"]):
        time_index = index + offset

        if 0 <= time_index < len(PRIMARY_TIMES):
            period, period_time = PRIMARY_TIMES[time_index]
        else:
            period = f"Period {index + 1}"
            period_time = "Time not specified"

        rows.append({
            "Period": period,
            "Time": period_time,
            "Subject": subject,
            "Class Teacher": details["teacher"],
        })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "Teacher names and subject order are based on the information supplied. "
        "Verify the exact period alignment against the original school timetable."
    )


# =========================================================
# 7. CHATBOT ANSWER FUNCTION
# =========================================================

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s/-]", " ", text)
    return re.sub(r"\s+", " ", text)


def answer_question(question):
    q = normalize(question)

    # Greetings
    if any(word in q.split() for word in ["hi", "hello", "salam", "assalam"]):
        return (
            "Assalam-o-Alaikum! Welcome to Khair-un-Nas School Swat. "
            "How can I help you today?"
        )

    # School information
    if "principal" in q or "head teacher" in q:
        return f"The principal of {SCHOOL_NAME} is {PRINCIPAL}."

    if "address" in q or "location" in q or "where is" in q:
        return f"Our school is located at {SCHOOL_ADDRESS}."

    if "phone" in q or "contact" in q or "number" in q:
        return (
            f"The phone number supplied in the timetable is {SCHOOL_PHONE}. "
            "Please confirm it with the school before relying on it."
        )

    if "timing" in q or "school time" in q or "school open" in q:
        return f"The general school timing is {SCHOOL_TIMING}."

    if "holiday" in q or "vacation" in q:
        return "The previously provided school information says summer holidays are approximately one month. Please confirm current holiday dates with the school."

    if "fee" in q or "fees" in q:
        return (
            "The previously provided fee information is approximately Rs. 2,500–3,000 "
            "for lower classes and Rs. 4,000–4,500 for Classes 7–10. "
            "Please confirm the current fee with the school office."
        )

    if "admission" in q or "admit" in q or "enroll" in q:
        return (
            "For admission, contact the school office to confirm available seats, "
            "required documents, admission dates, and current fees."
        )

    if "facility" in q or "facilities" in q:
        return (
            "Please contact the school office for a current list of facilities "
            "and available services."
        )

    # AI teacher
    if (
        ("ai" in q or "artificial intelligence" in q)
        and ("teacher" in q or "teach" in q or "class" in q or "sir" in q)
    ):
        return "Sir Sufyan teaches Artificial Intelligence (AI) to Class 10."

    # Senior timetable questions
    if "timetable" in q or "time table" in q or "period" in q:
        return (
            "Open the Timetable Browser from the sidebar, select "
            "'Classes Five to Ten' or 'Play Group to Fourth', then choose your class."
        )

    # Teacher / subject search in senior timetable
    for class_name, entries in SENIOR.items():
        normalized_class = normalize(class_name)

        aliases = {
            "5th-r": ["5th-r", "class 5 r", "fifth r"],
            "5th-j": ["5th-j", "class 5 j", "fifth j"],
            "6th-r/j": ["6th-r/j", "class 6", "sixth class"],
            "7th-jasmine": ["7th-jasmine", "class 7 jasmine"],
            "7th-rose": ["7th-rose", "class 7 rose"],
            "8th-jasmine": ["8th-jasmine", "class 8 jasmine"],
            "8th-rose": ["8th-rose", "class 8 rose"],
            "9th-r/j": ["9th-r/j", "class 9", "ninth class"],
            "10th-r/j": ["10th-r/j", "class 10", "tenth class"],
        }

        class_mentioned = (
            normalized_class in q
            or any(alias in q for alias in aliases.get(class_name, []))
        )

        if class_mentioned:
            for subject, teacher in entries:
                if normalize(subject) in q:
                    return (
                        f"In {class_name}, {teacher} is listed for {subject} "
                        "in the supplied timetable."
                    )

            if "teacher" in q or "teach" in q or "who is" in q:
                matches = [
                    f"{subject}: {teacher}"
                    for subject, teacher in entries
                ]
                return (
                    f"Teachers listed for {class_name}:\n\n"
                    + "\n".join(f"- {item}" for item in matches)
                )

    # General teacher search
    for class_name, subject, teacher in TEACHERS:
        if normalize(subject) in q and (
            "teacher" in q or "teach" in q or "who" in q
        ):
            return f"{teacher} is listed for {subject} in {class_name}."

    # Class list
    if "classes" in q or "which class" in q:
        return (
            "The timetable browser contains Play Group, Nursery, K.G., "
            "Classes One to Four, and the supplied sections of Classes Five to Ten."
        )

    if "school" in q or "about" in q:
        return (
            f"{SCHOOL_NAME} is located at {SCHOOL_ADDRESS}. "
            f"The principal is {PRINCIPAL}. General timing: {SCHOOL_TIMING}."
        )

    return (
        "I'm still learning how to answer that question. Try asking about the "
        "principal, school timing, fees, admissions, a teacher, AI in Class 10, "
        "or open the Timetable Browser to see a class timetable."
    )


# =========================================================
# 8. SIDEBAR NAVIGATION
# =========================================================

st.sidebar.markdown("# 🎓 KNS Assistant")
st.sidebar.markdown("### Khair-un-Nas School Swat")
st.sidebar.divider()

page = st.sidebar.radio(
    "Choose a section",
    [
        "Home",
        "Timetable Browser",
        "Ask the Chatbot",
        "About School",
        "Teachers & Subjects",
        "Fee Information",
        "Admission",
        "School Timing",
        "Holidays & Facilities",
    ],
    key="main_navigation",
)

st.sidebar.divider()
st.sidebar.caption("School information assistant • 2026–27")

# =========================================================
# 9. MAIN HEADER
# =========================================================

st.markdown(
    f"""
    <div class="hero">
        <h1>🎓 KNS Smart Assistant</h1>
        <p><b>{SCHOOL_NAME}</b></p>
        <p>{SCHOOL_ADDRESS}</p>
        <p>School information, teachers, and period-wise timetables for 2026–27</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 10. HOME PAGE
# =========================================================

if page == "Home":
    st.subheader("Welcome!")

    st.write(
        "Welcome to the Khair-un-Nas School Swat Smart Assistant. "
        "Choose a section from the sidebar to explore school information "
        "or view your class timetable."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="info-card"><h3>🗓️ Timetables</h3>'
            '<p>Browse the supplied 2026–27 class schedules.</p></div>',
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            '<div class="info-card"><h3>👩‍🏫 Teachers</h3>'
            '<p>Find teachers and their listed subjects.</p></div>',
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            '<div class="info-card"><h3>💬 Ask questions</h3>'
            '<p>Ask about school information and Class 10 AI.</p></div>',
            unsafe_allow_html=True,
        )

    st.info(
        "Tip: Open 'Timetable Browser' in the sidebar, then select "
        "'Classes Five to Ten' to see the senior timetable."
    )

# =========================================================
# 11. TIMETABLE BROWSER
# =========================================================

elif page == "Timetable Browser":
    st.subheader("🗓️ Period-wise Timetable 2026–27")

    level = st.radio(
        "Choose timetable",
        ["Play Group to Fourth", "Classes Five to Ten"],
        horizontal=True,
        key="timetable_level",
    )

    if level == "Classes Five to Ten":
        selected = st.selectbox(
            "Select class",
            list(SENIOR.keys()),
            key="senior_class_select",
        )

        st.subheader(f"{selected} Timetable")
        show_senior_timetable(selected)

    else:
        selected_primary = st.selectbox(
            "Select class",
            list(PRIMARY.keys()),
            key="primary_class_select",
        )

        st.subheader(f"{selected_primary} Timetable")
        show_primary_timetable(selected_primary)

# =========================================================
# 12. CHATBOT PAGE
# =========================================================

elif page == "Ask the Chatbot":
    st.subheader("💬 Ask KNS Smart Assistant")

    st.write(
        "Ask a question below. For the complete timetable, use "
        "'Timetable Browser' in the sidebar."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": (
                    "Assalam-o-Alaikum! Welcome to KNS Smart Assistant. "
                    "What would you like to know?"
                ),
            }
        ]

    if st.button("Clear chat", key="clear_chat"):
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "Chat cleared. How can I help you?",
            }
        ]
        st.rerun()

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask about school, teachers, fees, or AI...")

    if prompt:
        st.session_state.chat_history.append(
            {"role": "user", "content": prompt}
        )

        response = answer_question(prompt)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()

# =========================================================
# 13. ABOUT SCHOOL
# =========================================================

elif page == "About School":
    st.subheader("🏫 About Our School")

    st.markdown(f"**School:** {SCHOOL_NAME}")
    st.markdown(f"**Address:** {SCHOOL_ADDRESS}")
    st.markdown(f"**Principal:** {PRINCIPAL}")
    st.markdown(f"**General timing:** {SCHOOL_TIMING}")
    st.markdown(f"**Phone supplied in timetable:** {SCHOOL_PHONE}")

    st.caption(
        "Please confirm contact details and current school policies "
        "with the school office."
    )

# =========================================================
# 14. TEACHERS AND SUBJECTS
# =========================================================

elif page == "Teachers & Subjects":
    st.subheader("👩‍🏫 Teachers & Subjects")

    teacher_df = pd.DataFrame(
        TEACHERS,
        columns=["Class", "Subject", "Teacher"],
    )

    st.dataframe(
        teacher_df,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Class 10 AI")

    st.success(
        "Sir Sufyan is the Artificial Intelligence (AI) teacher for Class 10."
    )

    st.write(
        "For the teachers listed in the Classes Five to Ten timetable, "
        "open the Timetable Browser and select the relevant class."
    )

# =========================================================
# 15. FEES
# =========================================================

elif page == "Fee Information":
    st.subheader("💰 Fee Information")

    st.write("Previously provided fee ranges:")

    st.markdown("""
    - Lower classes: approximately Rs. 2,500–3,000
    - Classes 7–10: approximately Rs. 4,000–4,500
    """)

    st.info(
        "These are previously supplied figures, not verified current fees. "
        "Contact the school office for the latest fee schedule."
    )

# =========================================================
# 16. ADMISSIONS
# =========================================================

elif page == "Admission":
    st.subheader("📝 Admission Information")

    st.write(
        "For admission to Khair-un-Nas School Swat, contact the school "
        "office to confirm available seats, the admission process, "
        "required documents, and current fees."
    )

    st.markdown(f"**Location:** {SCHOOL_ADDRESS}")
    st.markdown(f"**Phone supplied in timetable:** {SCHOOL_PHONE}")

# =========================================================
# 17. SCHOOL TIMING
# =========================================================

elif page == "School Timing":
    st.subheader("⏰ School Timing")

    st.markdown(f"**General school timing:** {SCHOOL_TIMING}")

    st.write(
        "The timetable supplied for Classes Five to Ten starts at 7:50 AM. "
        "The primary timetable lists assembly from 8:10 AM. "
        "Please confirm the applicable arrival time for each class with the school."
    )

# =========================================================
# 18. HOLIDAYS AND FACILITIES
# =========================================================

elif page == "Holidays & Facilities":
    st.subheader("🏖️ School Holidays")

    st.markdown(
        """
        Holiday dates may change according to the school calendar.
        Please contact the school administration to confirm the
        official summer holiday dates and reopening date.
        """
    )

    st.divider()

    st.subheader("🏫 Our School Facilities")

    facilities = [
        (
            "📚 Library",
            "A place where students can read books and develop "
            "their knowledge and reading skills."
        ),
        (
            "🏃 Playground",
            "A space for students to participate in physical "
            "activities, games, and outdoor recreation."
        ),
        (
            "🔬 Laboratory",
            "A learning space for practical work and scientific "
            "experiments under appropriate supervision."
        ),
        (
            "🩺 Medical Facility",
            "Medical assistance for students when they feel unwell "
            "or need attention during school hours."
        ),
    ]

    col1, col2 = st.columns(2)

    for index, (facility_name, description) in enumerate(facilities):
        with (col1 if index % 2 == 0 else col2):
            st.markdown(
                f"""
                <div class="info-card">
                    <h3>{facility_name}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.info(
        "For details about facility availability and school policies, "
        "please contact the school administration."
    )

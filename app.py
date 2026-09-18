import streamlit as st

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="KNS Smart Assistant",
    page_icon="🏫",
    layout="centered"
)

# -----------------------------
# SCHOOL INFORMATION
# -----------------------------
school_name = "Khair un Nas School Swat"
location = "Gunbad Maira, Mingora, Swat"
principal = "Sir Khalid"
timing = "8:00 AM – 2:00 PM"
phone = "+92 346 9443390"

# -----------------------------
# HEADER
# -----------------------------
st.title("🏫 KNS Smart Assistant")
st.caption("Khair un Nas School Swat")
st.divider()

# -----------------------------
# WELCOME
# -----------------------------
st.markdown("""
### 👋 Assalamu Alaikum!

Welcome to **KNS Smart Assistant**.

I am the digital assistant of **Khair un Nas School Swat**.

I can help you find information about our school,
teachers, classes, admissions, facilities, timings,
and student information.
""")

st.divider()

# -----------------------------
# QUICK INFORMATION
# -----------------------------
st.subheader("📌 Quick Information")

col1, col2 = st.columns(2)

with col1:
    about = st.button(
        "🏫 About School",
        use_container_width=True
    )

    teachers = st.button(
        "👨‍🏫 Teachers & Subjects",
        use_container_width=True
    )

    classes = st.button(
        "📚 Classes",
        use_container_width=True
    )

    fees = st.button(
        "💰 Fee Information",
        use_container_width=True
    )

with col2:
    admission = st.button(
        "📝 Admission",
        use_container_width=True
    )

    timing_button = st.button(
        "🕐 School Timing",
        use_container_width=True
    )

    holidays = st.button(
        "🏖️ Holidays",
        use_container_width=True
    )

    facilities = st.button(
        "🏢 Facilities",
        use_container_width=True
    )

    about_me = st.button(
        "👩‍💻 About Me",
        use_container_width=True
    )

# -----------------------------
# ABOUT SCHOOL
# -----------------------------
if about:
    st.markdown("## 🏫 About Khair un Nas School Swat")

    st.markdown("""
**Khair un Nas School Swat** is an educational institution
located in **Gunbad Maira, Mingora, Swat**.

Our school is committed to providing students with:

- 📚 Quality education
- 🧭 Discipline
- 🌱 Character development
- 🤝 A supportive learning environment
- 💡 Confidence and academic growth

We aim to help students develop strong academic knowledge,
good manners, confidence, and the skills they need to become
responsible and successful members of society.

Our dedicated teachers guide students in different subjects
and encourage them to learn, ask questions, and achieve their goals.
""")

    st.divider()

    st.markdown("### 🏫 School Information")

    info1, info2 = st.columns(2)

    with info1:
        st.markdown("**👨‍💼 Principal**")
        st.write(principal)

        st.markdown("**📍 Location**")
        st.write(location)

    with info2:
        st.markdown("**📚 Classes**")
        st.write("8 Classes")

        st.markdown("**🕐 School Timing**")
        st.write(timing)

    st.success(
        "🌟 Our goal is to provide students with education, "
        "discipline, confidence, and skills for a successful future."
    )

# -----------------------------
# TEACHERS
# -----------------------------
if teachers:
    st.markdown("## 👨‍🏫 Teachers & Subjects")

    teacher_data = [
        ("Zero Class", "Urdu", "Sir Majeedullah"),
        ("1st Class", "Chemistry", "Sir Saqib"),
        ("2nd Class", "Physics", "Sir Shakur"),
        ("3rd Class", "Biology", "Sir Asif"),
        ("4th Class", "Mathematics", "Sir Amjad"),
        ("6th Class", "Islamiyat & Mutalia Quran", "Sir Siddiq"),
        ("7th Class", "English", "Sir Arif"),
        ("Last Class", "Pak Study", "Sir Yaseen")
    ]

    for class_name, subject, teacher in teacher_data:
        st.markdown(
            f"""
### 🎓 {class_name}

**Subject:** {subject}

**Teacher:** {teacher}
"""
        )

        st.divider()

# -----------------------------
# CLASSES
# -----------------------------
if classes:
    st.markdown("## 📚 Classes")

    st.success(
        "Khair un Nas School Swat currently has **8 classes**."
    )

    st.markdown("""
### 📖 Classes & Subjects

1. Zero Class — Urdu
2. 1st Class — Chemistry
3. 2nd Class — Physics
4. 3rd Class — Biology
5. 4th Class — Mathematics
6. 6th Class — Islamiyat & Mutalia Quran
7. 7th Class — English
8. Last Class — Pak Study
""")

# -----------------------------
# FEES
# -----------------------------
if fees:
    st.markdown("## 💰 Fee Information")

    st.info(
        "For the most accurate and current fee information, "
        "please contact the school administration."
    )

    st.markdown(f"""
**📞 School Contact:** {phone}

The administration can provide information about:

- 💰 Monthly fees
- 📝 Admission fees
- 📚 Other educational charges
- 📋 Required documents
""")

# -----------------------------
# ADMISSION
# -----------------------------
if admission:
    st.markdown("## 📝 Admission Process")

    st.markdown("""
Welcome to **Khair un Nas School Swat!**

Our admission process is simple and student-friendly.

### 1️⃣ Visit the School

Parents or guardians should visit the school
along with the student.

### 2️⃣ Get Admission Information

Collect information about available classes,
fees, and requirements from the school administration.

### 3️⃣ Submit Required Documents

Provide the necessary student documents
as requested by the school.

### 4️⃣ Admission Confirmation

After verification and approval by the school
administration, the student's admission will be confirmed.

### 5️⃣ Start Classes

The student can begin attending classes
according to the school schedule.
""")

    st.success(
        "📍 Visit: Gunbad Maira, Mingora, Swat"
    )

# -----------------------------
# SCHOOL TIMING
# -----------------------------
if timing_button:
    st.markdown("## 🕐 School Timing")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🌅 School Starts",
            "8:00 AM"
        )

    with col2:
        st.metric(
            "🌇 School Ends",
            "2:00 PM"
        )

    st.info(
        "Students should arrive at school on time "
        "according to the school schedule."
    )

# -----------------------------
# HOLIDAYS
# -----------------------------
if holidays:
    st.markdown("## 🏖️ School Holidays")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ☀️ Summer Holidays")
        st.write("Approximately one month.")

    with col2:
        st.markdown("### ❄️ Winter Holidays")
        st.write("Approximately one month.")

# -----------------------------
# FACILITIES
# -----------------------------
if facilities:
    st.markdown("## 🏢 School Facilities")

    st.markdown("""
### 📚 Library

A learning space where students can access
books and educational resources.

### 🔬 Laboratory

A facility that supports practical and
science-related learning.

### ⚽ Playground

A space where students can participate
in physical activities and sports.

### 🚌 Transport

School transport facilities are available
for students.

### 📱 Zama App

The school's **Zama App** provides access
to services such as:

- 📖 Child diary
- 📊 Test results
""")

# -----------------------------
# ABOUT ME
# -----------------------------
if about_me:
    st.markdown("## 👩‍💻 About Me")

    st.markdown("""
### 🌟 Student Profile

**👩 Name:** Madiha Sha

**👨 Father's Name:** Barkat Ali

**🎓 Class:** 10th

**🏫 School:** Khair un Nas School Swat

### 📚 Hobbies

- 📖 Reading books
- ✍️ Writing stories
- 🏸 Playing with rackets
""")

    st.success(
        "🌟 Madiha is a student who loves learning, "
        "reading books, writing stories, and playing with rackets."
    )

# -----------------------------
# CHATBOT
# -----------------------------
st.divider()

st.subheader("🤖 Ask KNS Assistant")

question = st.chat_input(
    "Ask something about the school or Madiha..."
)

if question:

    st.chat_message("user").write(question)

    q = question.lower().strip()

    # -----------------------------
    # MADIHA INFORMATION
    # -----------------------------

    if (
        "madiha" in q
        and (
            "who" in q
            or "about" in q
            or "tell me" in q
        )
    ):
        answer = (
            "👩‍💻 **Madiha Sha** is a Class 10 student "
            "of **Khair un Nas School Swat**."
        )

    elif "madiha" in q and "father" in q:
        answer = (
            "👨 Madiha Sha's father's name is "
            "**Barkat Ali**."
        )

    elif "madiha" in q and "class" in q:
        answer = (
            "🎓 Madiha Sha is a student of "
            "**Class 10**."
        )

    elif "madiha" in q and "school" in q:
        answer = (
            "🏫 Madiha Sha is a student of "
            "**Khair un Nas School Swat**."
        )

    elif "madiha" in q and (
        "hobby" in q
        or "hobbies" in q
    ):
        answer = (
            "📚 Madiha Sha's hobbies are "
            "**reading books, writing stories, "
            "and playing with rackets**."
        )

    # -----------------------------
    # TEACHERS
    # -----------------------------

    elif "biology" in q and (
        "teacher" in q
        or "teach" in q
    ):
        answer = (
            "🧬 Biology is taught by "
            "**Sir Asif**."
        )

    elif "chemistry" in q and (
        "teacher" in q
        or "teach" in q
    ):
        answer = (
            "🧪 Chemistry is taught by "
            "**Sir Saqib**."
        )

    elif "physics" in q and (
        "teacher" in q
        or "teach" in q
    ):
        answer = (
            "⚛️ Physics is taught by "
            "**Sir Shakur**."
        )

    elif (
        ("math" in q or "mathematics" in q)
        and (
            "teacher" in q
            or "teach" in q
        )
    ):
        answer = (
            "➗ Mathematics is taught by "
            "**Sir Amjad**."
        )

    elif "english" in q and (
        "teacher" in q
        or "teach" in q
    ):
        answer = (
            "🇬🇧 English is taught by "
            "**Sir Arif**."
        )

    elif (
        "islamiyat" in q
        or "mutalia quran" in q
    ):
        answer = (
            "📖 Islamiyat and Mutalia Quran "
            "are taught by **Sir Siddiq**."
        )

    elif (
        "pak study" in q
        or "pakistan study" in q
    ):
        answer = (
            "🇵🇰 Pak Study is taught by "
            "**Sir Yaseen**."
        )

    elif "urdu" in q and (
        "teacher" in q
        or "teach" in q
    ):
        answer = (
            "📚 Urdu is taught by "
            "**Sir Majeedullah**."
        )

    # -----------------------------
    # SCHOOL INFORMATION
    # -----------------------------

    elif "principal" in q:
        answer = (
            "👨‍💼 The principal of "
            "Khair un Nas School Swat is "
            "**Sir Khalid**."
        )

    elif (
        "where" in q
        and (
            "school" in q
            or "location" in q
        )
    ):
        answer = (
            "📍 Our school is located in "
            "**Gunbad Maira, Mingora, Swat**."
        )

    elif (
        "location" in q
        or "located" in q
    ):
        answer = (
            "📍 Khair un Nas School Swat is located "
            "in **Gunbad Maira, Mingora, Swat**."
        )

    elif (
        "timing" in q
        or "time" in q
        or "start" in q
        or "end" in q
    ):
        answer = (
            "🕐 School starts at **8:00 AM** "
            "and ends at **2:00 PM**."
        )

    elif (
        "how many" in q
        and "class" in q
    ):
        answer = (
            "📚 Khair un Nas School Swat has "
            "**8 classes**."
        )

    elif (
        "class" in q
        and "number" in q
    ):
        answer = (
            "📚 Khair un Nas School Swat has "
            "**8 classes**."
        )

    elif (
        "holiday" in q
        or "holidays" in q
    ):
        answer = (
            "🏖️ We have both summer and winter "
            "holidays, each approximately one month."
        )

    elif "admission" in q:
        answer = (
            "📝 For admission, parents or guardians "
            "should visit the school with the student "
            "and contact the administration for "
            "requirements and fees."
        )

    elif (
        "facility" in q
        or "facilities" in q
    ):
        answer = (
            "🏢 Our facilities include a "
            "**library, laboratory, playground, "
            "transport and Zama App**."
        )

    elif (
        "zama" in q
        or "diary" in q
        or "result" in q
    ):
        answer = (
            "📱 The **Zama App** provides services "
            "such as the child's diary and test results."
        )

    elif (
        "contact" in q
        or "phone" in q
        or "number" in q
    ):
        answer = (
            "📞 You can contact "
            "Khair un Nas School Swat at "
            "**+92 346 9443390**."
        )

    # -----------------------------
    # FALLBACK
    # -----------------------------

    else:
        answer = (
            "🤖 I'm sorry, I don't have verified "
            "information about that yet.\n\n"
            "You can ask me about **teachers, classes, "
            "timing, admission, holidays, facilities, "
            "location, contact information, Zama App, "
            "or Madiha Sha**."
        )

    st.chat_message("assistant").markdown(answer)

# -----------------------------
# CREATED BY
# -----------------------------
st.divider()

st.markdown("## 👩‍💻 Created By")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("sudais.jpg", width=150)

with col2:
    st.markdown("""
### 🌟 Madiha Sha

**Class:** 10th  
**School:** Khair un Nas School Swat

📚 Reading Books  
✍️ Writing Stories  
🏸 Playing with Rackets
""")

st.caption("🏫 KNS Smart Assistant • Khair un Nas School Swat")

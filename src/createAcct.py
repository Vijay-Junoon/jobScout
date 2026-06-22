import streamlit as st
from tools.databaseHandler import put
import time


st.set_page_config(
    page_title="JobScout - Create Account",
    page_icon="🚀",
    layout="centered"
)


def createAccount(name, email, pwd, jobrole, exp, loc, sal):

    # Validation
    if not name or not email or not pwd or not jobrole or not loc:
        st.error("⚠️ Please fill all required fields.")
        return

    if "@" not in email:
        st.error("⚠️ Please enter a valid email address.")
        return


    with st.spinner("Creating your JobScout account..."):

        result = put(
            name,
            email,
            pwd,
            jobrole,
            exp,
            loc,
            float(sal)
        )

        time.sleep(1)


    if result:

        st.session_state.account_created = True
        st.session_state.user_email = email

        st.success(
            "🎉 Account created successfully!"
        )

        st.info(
            "📩 You will start receiving personalized job alerts every day at 9 AM."
        )

        time.sleep(2)
        st.rerun()

    else:
        st.error(
            "❌ Account creation failed. Email may already exist."
        )



# -------------------------
# UI
# -------------------------

if st.session_state.get("account_created"):

    st.balloons()

    st.success("Welcome to JobScout 🚀")

    st.write(
        """
        Your account has been created successfully.

        Daily job alerts will be sent to:
        """
    )

    st.code(
        st.session_state.user_email
    )


else:

    st.title("🚀 Create your JobScout Account")

    st.caption(
        "Find relevant jobs automatically. Receive personalized job alerts every morning."
    )


    st.divider()


    with st.container():

        st.subheader("👤 Personal Information")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )


        email = st.text_input(
            "Email Address",
            placeholder="example@gmail.com"
        )


        pwd = st.text_input(
            "Password",
            type="password",
            placeholder="Create a strong password"
        )


    st.divider()


    with st.container():

        st.subheader("💼 Job Preferences")


        jobRole = st.text_input(
            "Desired Job Role",
            placeholder="Example: Python Developer"
        )


        exp = st.slider(
            "Years of Experience",
            min_value=0,
            max_value=35,
            value=0
        )


        loc = st.text_input(
            "Preferred Location",
            placeholder="Example: Hyderabad"
        )


        salary = st.slider(
            "Expected Salary (₹)",
            min_value=0,
            max_value=1000000,
            step=50000
        )


    st.divider()


    create = st.button(
        "🚀 Create Account",
        use_container_width=True
    )


    if create:

        createAccount(
            name,
            email,
            pwd,
            jobRole,
            exp,
            loc,
            salary
        )
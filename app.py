import streamlit as st
from utils.db import init_db, get_users, add_user

# Initialize the database
init_db()

# App title
st.set_page_config(page_title="Mini EBS R12", layout="wide")
st.title("Mini EBS R12 - Oracle E-Business Suite Simulation")

# Sidebar navigation
menu = ["Home", "Users", "Add User"]
choice = st.sidebar.selectbox("Menu", menu)

# Home Page
if choice == "Home":
    st.markdown(
        """
        # Welcome to Mini EBS R12
        This is a **Streamlit** simulation of Oracle E-Business Suite R12.
        Use the sidebar to navigate between pages.
        """
    )

# Users Page
elif choice == "Users":
    st.subheader("Registered Users")
    users = get_users()
    if users:
        for user in users:
            st.write(f"👤 **Name:** {user[1]} | 📧 **Email:** {user[2]}")
    else:
        st.info("No users found.")

# Add User Page
elif choice == "Add User":
    st.subheader("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Save"):
        if name and email:
            add_user(name, email)
            st.success(f"User {name} added successfully!")
        else:
            st.warning("Please enter both name and email.")

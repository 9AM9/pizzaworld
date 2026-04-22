# Modules
import streamlit as st

# Setting pages
homepage = st.Page(
    page = 'pages\home.py',
    title = "Home",
    icon = "🏡",
    default = True
    )

chatbot_page = st.Page(
    page = 'pages\chatbot.py',
    title = "PizzAI",
    icon = "💬"
    )

login_page = st.Page(
    page = 'pages\log in.py',
    title = "Login",
    icon = "🔐"
    )

signup_page = st.Page(
    page = 'pages\sign up.py',
    title = "Sign up",
    icon = "📝"
    )

menu_page = st.Page(
    page = "pages\menu.py",
    title = "Menu",
    icon = "📜"
)

# Navbar
pages = st.navigation(
    [
        homepage,
        signup_page,
        login_page,
        menu_page,
        chatbot_page
    ],
    position='top'
)

# Running all pages
pages.run()

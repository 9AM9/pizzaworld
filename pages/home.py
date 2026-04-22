# Modules
import streamlit as st

# Title
st.title('Welcome to PizzaWorld 🍕', text_alignment='center')

# Slogan
st.subheader('Delicious italian _cibo._', text_alignment='center')

# Hero image
st.image('images/hero.jpg')
st.divider()

## Help & Chatbot Buttons
# Creating Columns
help_col, bot_col = st.columns(2, border=True)

# Adding text and buttons to each column
with help_col:
    st.header("Hungry? 🍽")
    st.text("Take a look at our menu  with various types of italian food, pizzas, pasta, drinks, and any of what you can imagine!")
    if st.button("Explore Menu", width='stretch'):
        st.switch_page("pages/menu.py")

with bot_col:
    st.header("Need help? 🤖")
    st.text("Nutrition facts? Work info? Anything you want to know? Ask our AI assistant and get your answers as fast and smart as possible!")
    if st.button("PizzAI", width='stretch'):
        st.switch_page("pages/chatbot.py")

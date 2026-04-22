import streamlit as st

# Initializing session vars
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone_number' not in st.session_state:
    st.session_state['phone_number'] = None

# Title
st.title("Create your new account.", text_alignment='center')

# Creating Form
account_form = st.form(key='account form', border=True, enter_to_submit=False)

# Editing Form
with account_form:
    # Top columns title
    st.text("Personal Information:")

    # Top Columns (Name & Email)
    fcol1, fcol2 = st.columns(2)
    with fcol1:
        name = st.text_input("Full Name")
        email = st.text_input("E-mail", placeholder="example@gmail.com")
    
    with fcol2:
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type='password')

    # Bottom Columns title
    st.text("Delivery Details:")

    # Bottom Columns (Address)
    fcol3, fcol4 = st.columns([0.8, 0.2])
    with fcol3:
        address = st.text_input("Street Address")
    
    with fcol4:
        apt = st.text_input("Apartment no.")

    # Form Submit Btn
    submit = st.form_submit_button("Create Account", width='stretch')

        # 8. Form validation and account creation
    if submit:
        if name and email and password and address:
            st.session_state['name'] = name
            st.session_state['phone'] = phone
            st.session_state['email'] = email
            st.session_state['address'] = f"{address}, Apt {apt}"
            
            st.success(f"Account created successfully for {name}! Please sign in.")
            
            # 9. Redirecting to sign-in page
            st.switch_page("pages/log in.py")
        else:
            st.error("Please fill in all required fields (Name, Email, Password, Address).")

st.divider()

# Already has an account? Btn
st.text("Already have an account?")

if st.button("Log in instead", width='stretch'):
    st.switch_page("pages/log in.py")


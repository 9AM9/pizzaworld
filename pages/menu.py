# Modules
import streamlit as st
import pandas as pd

# Intializing session vars
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone' not in st.session_state:
    st.session_state['phone'] = None

# Tabs
pizza_tab, pasta_tab, drinks_tab = st.tabs(['Pizzas', 'Pasta', 'Soft drinks'])

# Final order list
order = []

# Data
pizzas = {
    'pepperoni': {'Small': 10, 'Medium': 25, 'Large': 40},
    'margerita': {'Small': 10, 'Medium': 25, 'Large': 40},
    'chicken': {'Small': 15, 'Medium': 30, 'Large': 45}
}

menu_pasta = {
    'Alfredo': 180,
    'Bolognese': 200,
    'Pesto': 190
}

menu_drinks = {
    'Cola': 30,
    'Sprite': 30,
    'Orange Juice': 45,
    'Water': 15
}

# Logged in Check
if not st.session_state['logged_in']:
    st.warning("Create an account first to view the menu.")
    st.stop()

# The Pizza tab
with pizza_tab:
    pcol1, pcol2, pcol3 = st.columns(3)

    # The Pepperoni Column
    with pcol1:
        # Image
        st.image('images/pepperoni.png')
        # Name
        st.subheader('Pepperoni Pizza', text_alignment='center', anchor=False)
        # Size choices
        pepp_size = st.segmented_control('Size', pizzas['pepperoni'], key='pepp pills', default='Medium') 
        # Price Display
        st.subheader(f"Price: :red[{pizzas['pepperoni'][pepp_size]}] EGP", anchor=False)
        # Quantity
        pepp_qty = st.number_input('Quantity', step=1, min_value=0, max_value=50, key='pepp quant')

        if pepp_qty > 0:
            order.append({'Item': f"Pepperoni Pizza {pepp_size}", 'Quantity': pepp_qty, 'Price': pizzas['pepperoni'][pepp_size] * pepp_qty})


    # The Margerita Column
    with pcol2:
        # Image
        st.image('images/margerita.png')
        # Name
        st.subheader('Margerita Pizza', text_alignment='center', anchor=False)
        # Size Choices
        marg_size = st.segmented_control('Size', pizzas['margerita'], key='marg pills', default='Medium')
        # Price Display 
        st.subheader(f"Price: :red[{pizzas['margerita'][marg_size]}] EGP", anchor=False)
        # Quantity
        marg_qty = st.number_input('Quantity', step=1, min_value=0, max_value=50, key='marg quant')
        if marg_qty > 0:
            order.append({'Item': f"Margerita Pizza {marg_size}", 'Quantity': marg_qty, 'Price': pizzas['margerita'][marg_size] * marg_qty})

    # The Chicken Column
    with pcol3:
        # Image
        st.image('images/chicken.png')
        # Name
        st.subheader('Chicken Pizza', text_alignment='center', anchor=False)
        # Size Choices
        chicken_size = st.segmented_control('Size', pizzas['chicken'], key='chick pills', default='Medium') 
        # Price Display
        st.subheader(f"Price: :red[{pizzas['chicken'][chicken_size]}] EGP", anchor=False)
        # Quantity
        chicken_qty = st.number_input('Quantity', step=1, min_value=0, max_value=50, key='chick quant')

        if chicken_qty > 0:
            order.append({'Item': f"Chicken Pizza {chicken_size}", 'Quantity': chicken_qty, 'Price': pizzas['chicken'][chicken_size] * chicken_qty})
# The Pasta Tab
with pasta_tab:
    st.header('Italian Pasta🍝')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Fettuccine Alfredo")
        st.write(f'Price: :red[{menu_pasta["Alfredo"]}] EGP')
        alfredo_qty = st.number_input('Choose quantity:', key='alfredo', min_value=0, max_value=20, step=1)
        if alfredo_qty > 0: order.append({"Item": "Fettuccine Alfredo", "Quantity": alfredo_qty, "Price": alfredo_qty * menu_pasta["Alfredo"]})
        
    with col2:
        st.image("https://images.unsplash.com/photo-1626844131082-256783844137?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Spaghetti")
        st.write(f'Price: :red[{menu_pasta["Bolognese"]}] EGP')
        bolognese_qty = st.number_input('Choose quantity:', key='bolognese', min_value=0, max_value=20, step=1)
        if bolognese_qty > 0: order.append({"Item": "Spaghetti Bolognese", "Quantity": bolognese_qty, "Price": bolognese_qty * menu_pasta["Bolognese"]})
        
    with col3:
        st.image("https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Pesto Penne")
        st.write(f'Price: :red[{menu_pasta["Pesto"]}] EGP')
        pesto_qty = st.number_input('Choose quantity:', key='pesto', min_value=0, max_value=20, step=1)
        if pesto_qty > 0: order.append({"Item": "Pesto Penne", "Quantity": pesto_qty, "Price": pesto_qty * menu_pasta["Pesto"]})
# Soft Drinks Tab
with drinks_tab:
    st.header('Soft Drinks🥤')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Cola")
        st.write(f'Price: :red[{menu_drinks["Cola"]}] EGP')
        cola_qty = st.number_input('Quantity:', key='cola', min_value=0, max_value=20, step=1)
        if cola_qty > 0: order.append({"Item": "Cola", "Quantity": cola_qty, "Price": cola_qty * menu_drinks["Cola"]})
        
    with col2:
        st.image("https://images.unsplash.com/photo-1680404005217-a441afdefe83?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Sprite")
        st.write(f'Price: :red[{menu_drinks["Sprite"]}] EGP')
        sprite_qty = st.number_input('Quantity:', key='sprite', min_value=0, max_value=20, step=1)
        if sprite_qty > 0: order.append({"Item": "Sprite", "Quantity": sprite_qty, "Price": sprite_qty * menu_drinks["Sprite"]})
        
    with col3:
        st.image("https://images.unsplash.com/photo-1613478223719-2ab802602423?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Orange Juice")
        st.write(f'Price: :red[{menu_drinks["Orange Juice"]}] EGP')
        orj_qty = st.number_input('Quantity:', key='orj', min_value=0, max_value=20, step=1)
        if orj_qty > 0: order.append({"Item": "Orange Juice", "Quantity": orj_qty, "Price": orj_qty * menu_drinks["Orange Juice"]})
        
    with col4:
        st.image("https://images.unsplash.com/photo-1550505095-81378a674395?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Water")
        st.write(f'Price: :red[{menu_drinks["Water"]}] EGP')
        water_qty = st.number_input('Quantity:', key='water', min_value=0, max_value=20, step=1)
        if water_qty > 0: order.append({"Item": "Water", "Quantity": water_qty, "Price": water_qty * menu_drinks["Water"]})

st.divider()

# Order Summary
st.subheader('Order Summary:')

if len(order) > 0:
 
    # Calculating total price from `Order` list
    total = sum(i['Price'] for i in order)

    df = pd.DataFrame(order)
    st.dataframe(df, hide_index=True)

    st.header(f"Total Order Price: :red[{total}] EGP")

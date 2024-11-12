import streamlit as st

# Inject custom CSS to hide or modify the class '_container_1upux_1'
st.markdown("""
    <style>
        /* Hide the specific class by setting display to none */
        ._container_1upux_1 {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Your Streamlit content here
st.title("Streamlit App with Custom CSS")
st.write("This is a sample app.")

# You can add other components as needed
st.button("Click me")

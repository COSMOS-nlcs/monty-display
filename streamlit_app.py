import streamlit as st

# Custom CSS to hide the fullscreen button
st.markdown(
    """
    <style>
        .css-1aumxhk { 
            display: none;  /* Hides the fullscreen button */
        }
    </style>
    """, unsafe_allow_html=True
)

# Your Streamlit app content
st.title('Streamlit App Without Fullscreen Option')
st.write("This app doesn't show the fullscreen button.")

import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="PostureAI", page_icon="🧍‍♂️", layout="centered")

# Title and header image
st.title("🧍‍♂️ PostureAI")
st.image("example_home.png", use_container_width=True)  # <-- FIXED LINE

# Instructions
st.markdown("""
Check your posture in seconds.  
Just upload a **side-angle** photo.  
**No login. No data stored. 100% private.**
""")

# Image upload
uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Photo", use_container_width=True)

    # Sample Result
    st.markdown("### ✅ Posture Assessment Result")
    st.markdown("**Posture Score:** 6/10")
    st.markdown("🧠 Forward Head Posture Detected")
    st.markdown("""
    **Issues:**
    - Head tilted ~12° forward  
    - Added pressure on neck & spine

    **Suggestions:**
    - Chin Tucks  
    - Wall Angels  
    - Shoulder Blade Squeezes
    """)

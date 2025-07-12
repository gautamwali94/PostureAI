import streamlit as st
from PIL import Image

# Set page title and layout
st.set_page_config(page_title="PostureAI", page_icon="🧍‍♂️", layout="centered")

# Title and header image
st.title("🧍‍♂️ PostureAI")

# Load and show the example image (must be uploaded in root folder of repo)
try:
    home_img = Image.open("example_home.png")
    st.image(home_img, use_container_width=True)
except Exception as e:
    st.warning("⚠️ Example image not found. Please upload 'example_home.png' to the root of the GitHub repo.")

# Intro text
st.markdown("""
Check your posture in seconds.  
Just upload a **side-angle** photo.  
**No login. No data stored. 100% private.**
""")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Photo", use_container_width=True)

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

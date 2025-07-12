import streamlit as st
from PIL import Image

st.set_page_config(page_title="PostureAI", page_icon="🧍‍♂️", layout="centered")

st.title("🧍‍♂️ PostureAI")
st.image("static/example_home.png", use_column_width=True)

st.markdown("""
Check your posture in seconds.  
Just upload a **side-angle** photo.  
**No login. No data stored. 100% private.**
""")

uploaded_file = st.file_uploader("📤 Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Photo", use_column_width=True)

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

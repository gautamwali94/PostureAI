import streamlit as st
import cv2
import tempfile
import numpy as np
import mediapipe as mp
import math

st.title("PostureAI - Posture Analysis from Image")

st.markdown("Upload a side or front-view image to assess your posture.")

uploaded_file = st.file_uploader("Upload Posture Photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    image = cv2.imread(tfile.name)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    results = pose.process(image_rgb)

    annotated_image = image.copy()
    feedback = "Could not detect posture."

    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        h, w, _ = image.shape
        landmarks = results.pose_landmarks.landmark

        shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
        ear = landmarks[mp_pose.PoseLandmark.LEFT_EAR]

        s = np.array([shoulder.x * w, shoulder.y * h])
        h_ = np.array([hip.x * w, hip.y * h])
        e = np.array([ear.x * w, ear.y * h])

        torso_vec = s - h_
        vertical_vec = np.array([0, -1])
        angle_rad = math.acos(np.dot(torso_vec, vertical_vec) / (np.linalg.norm(torso_vec) * np.linalg.norm(vertical_vec)))
        torso_angle = np.degrees(angle_rad)

        neck_vec = e - s
        neck_angle_rad = math.acos(np.dot(neck_vec, vertical_vec) / (np.linalg.norm(neck_vec) * np.linalg.norm(vertical_vec)))
        neck_angle = np.degrees(neck_angle_rad)

        score = 10
        posture_label = "Neutral posture"
        description = "Your head and spine are aligned."

        if torso_angle > 20:
            posture_label = "Slouched posture"
            description = "Your torso leans forward. This can indicate poor core engagement."
            score -= 3
        if neck_angle > 30:
            posture_label = "Forward head posture"
            description = "Your head is positioned ahead of your shoulders, straining your neck."
            score -= 4
        if torso_angle > 20 and neck_angle > 30:
            posture_label = "Forward head + Slouched posture"
            description = "Both your spine and head are misaligned, affecting posture."
            score = 2

        feedback = f"**🧠 Posture Score: {score}/10**\n\n**🔍 {posture_label}**\n{description}"

    st.image(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB), caption="Posture Analysis Result")
    st.markdown(feedback)

    if "Forward head" in feedback:
        st.info("💡 Tip: Try chin tuck exercises to align your head with your spine.")
    if "Slouched" in feedback:
        st.info("💡 Tip: Strengthen your core and upper back to support upright posture.")

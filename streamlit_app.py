import streamlit as st
from app.captioner import generate_caption
from app.self_corrector import refine_caption
from app.scorer import choose_best

st.title("🖼️ Smart Image Captioner")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)

    c1 = generate_caption("temp.jpg")
    c2 = refine_caption("temp.jpg")

    best = choose_best(c1, c2)

    st.subheader("Generated Captions")
    st.write("Caption 1:", c1)
    st.write("Caption 2:", c2)

    st.success(f"Best Caption: {best}")
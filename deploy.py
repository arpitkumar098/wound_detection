import streamlit as st
from fastai.learner import load_learner
from PIL import Image
import os
import pathlib

# Fix for Windows path compatibility with FastAI
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the model (since it's in the same directory as this script)
MODEL_PATH = 'wound classifier.pkl'

# Check if the model file exists
if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found at: {MODEL_PATH}")
    st.stop()

# Load model
learn_inf = load_learner(MODEL_PATH)

# Mappings for display
display_name_map = {
    "abrasion wound": "Abrasion",
    "bruises wound": "Bruise/Contusion",
    "burn wound": "Burn wound",
    "cut wound": "Cut/Incised wound",
    "laceration wound": "Laceration",
    "Stab_wound": "Stab wound",
}

dscrp_map1 = {
    "abrasion wound": "Rough surfaces, fingernail scratches, bite marks",
    "bruises wound": "Hand (slap mark, grab mark), belts, bats, blunt objects",
    "burn wound": "Thermal, chemical, or electrical heat source",
    "cut wound": "Sharp object (knife, scalpel, glass)",
    "laceration wound": "Rough-edged objects (pipe wrench, bricks)",
    "Stab_wound": "Sharp pointed objects (knife, screwdriver, ice pick)",
}

dscrp_map2 = {
    "abrasion wound": "Scrapes away top skin layers, usually shallow, slight bleeding.",
    "bruises wound": "Discolored skin due to internal bleeding, no broken skin.",
    "burn wound": "Varied damage depth depending on severity.",
    "cut wound": "Clean, straight-edged wound, minimal tissue bridging.",
    "laceration wound": "Torn skin from blunt trauma, crushed edges, possible exposure of deeper tissue.",
    "Stab_wound": "Deep puncture wound, narrow entry, potential internal bleeding.",
}

# Streamlit UI
st.title("🩹 Wound Classification App")
st.markdown("Upload or select an image to identify the wound type using an AI model.")

# Sample image selection
sample_folder = 'sample_images'
sample_images = []
if os.path.exists(sample_folder):
    sample_images = [f for f in os.listdir(sample_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]

selected_file = st.selectbox("📁 Select a sample image", [""] + sample_images)

# Upload your own image
uploaded_file = st.file_uploader("📤 Or upload your own image", type=["jpg", "jpeg", "png"])

# Load image function
def load_image(image_file):
    return Image.open(image_file)

# Determine which image to use
image_file = None
if uploaded_file:
    image_file = uploaded_file
elif selected_file:
    selected_path = os.path.join(sample_folder, selected_file)
    if os.path.exists(selected_path):
        image_file = selected_path

# Run prediction
if image_file:
    image = load_image(image_file)
    st.image(image, caption="🖼️ Selected Image", use_column_width=True)

    with st.spinner("Classifying..."):
        pred_class, class_idx, probs = learn_inf.predict(image)
        pred_prob = float(max(probs)) * 100
        readable_class = display_name_map.get(pred_class, pred_class)

    st.subheader("✅ Prediction")
    st.success(f"**{readable_class}** — **{pred_prob:.2f}%** confidence")

    st.subheader("🛠️ Possible Weapon")
    st.info(dscrp_map1.get(pred_class, "Unknown"))

    st.subheader("🧬 Wound Characteristics")
    st.write(dscrp_map2.get(pred_class, "No description available."))

    st.caption("⚠️ Characteristics may vary depending on severity and cause.")
else:
    st.warning("Please select or upload an image to get a prediction.")

# 🩸 Wound Detection and Classification for Domestic Violence Cases

## 📌 Objective

This project aims to support **victim screening in domestic violence cases** by classifying wounds based on type and characteristics using computer vision and deep learning. The ultimate goal is to assist healthcare professionals and investigators in identifying abuse-related injuries faster and more accurately—even without specialized expertise.

---

## 🗂 Dataset

- Primary sources: 
  - Kaggle datasets: `wound_dataset` and `wound_cls_4_13`
  - Additional data from **DuckDuckGo Image Search API**
- Dataset cleaned and filtered to remove unrelated/noisy images (bandages, posters, in-surgery photos, etc.)
- Final classes (6 wound types based on weapon characteristics):
  - **Abrasion**
  - **Burn**
  - **Contusion (Bruise)**
  - **Cut/Incised**
  - **Laceration**
  - **Stab wound**
- Split ratio: **Train 80% / Validation 10% / Test 10%**

---

## 🧠 Model Architecture

- Base models used:
  - **ResNet34 (baseline)**
  - **ResNet50 (final model)**
- Image input size: 224x224
- Transfer Learning used with fine-tuning
- Regularization: Dropout and BatchNorm

---

## 🧪 Techniques Used

### ⚙️ Preprocessing:
- Removal of mirrored, poor quality, and noisy images
- Manual labeling by wound type

### 🧪 Data Handling:
- **Upsampling** using `imgaug` to balance classes
- Advanced **data augmentation** using `fastai`:
  - Random crops, flips, lighting, and rotation
  - Custom aspect ratio cropping (e.g., 9:16, 4:3)
- Class weighting using **Effective Number of Samples (ENS)**

### 🧮 Training:
- Optimizers tested: `Adam`, `SGD`, `RAdam`
- Learning Rate Finder used for optimal tuning
- Custom loss functions:
  - Cross-entropy
  - Weighted cross-entropy
  - Focal loss

---

## 📈 Results

| Metric          | Baseline (ResNet34) | Final (ResNet50) |
|------------------|---------------------|------------------|
| Accuracy         | 79%                 | **82%**          |
| F1-score         | 73%                 | **79%**          |
| Macro Precision  | 74%                 | 81%              |

✅ The final model improved baseline F1-score by **6%** and accuracy by **3%**.

---

## 🧪 Error Analysis & Sensitivity

- **Skin tone analysis**: The model performs comparably across different skin tones (light/dark), though training data was skewed toward fair-skinned individuals.
- **Cropping/Aspect Ratio Sensitivity**:
  - Model predictions vary significantly with wound position, zoom level, and image proportions.
  - Extensive cropping and resizing strategies were added to reduce this issue.

---

## 💻 Deployment

- **Streamlit** used for creating a lightweight web app
- Allows uploading an image to get real-time wound classification

---

## 🔮 Future Scope

- Expand dataset: Include wound severity, wound age, depth, and additional skin tones
- Detect **multiple wounds** in the same image
- Extend model to **predict likely weapon type** from wound characteristics
- Integrate into **mobile devices** or **field diagnostic tools**

---

## 🧑‍💻 Author

**Arpit Kumar**  
Final Year B.Tech, Electronics & Computer Science  
KIIT University  
📧 [ad8409112303@gmail.com](mailto:ad8409112303@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/arpit-kumar-435a11252/) | [GitHub](https://github.com/arpitkumar098)

---

## 📚 References & Acknowledgements

- Fateen, Ibrahim. *Wound Classification Notebook* – Kaggle  
- Jakupov, A. *Computer Vision Data Augmentation*  
- Shrivastava, I. *Loss Weighting for Class Imbalance*  
- Streamlit & FastAI Docs  
- AI Builders Project Mentors & Contributors

---

> 🛑 **Disclaimer**: This model is developed for educational and research purposes and is **not intended for clinical use** without proper validation and certification.


# 🧠 CS2 Computer Vision — YOLOv10 Player Detection

This project demonstrates a **YOLOv10-based object detection model** trained to recognize **CT** and **T** players in _Counter-Strike 2_ gameplay footage.  
It was created for computer vision experimentation and showcases detection results on in-game screenshots.

---

## 📸 Overview

The model is capable of detecting:

- 🟦 **CT (Counter-Terrorists)**
- 🟥 **T (Terrorists)**

Training and testing were done using custom dataset samples collected from _CS2_ gameplay footage.

---

## 🚀 Features

- Fine-tuned **YOLOv10** model trained on custom CS2 dataset
- Detects player teams (CT / T) in screenshots or videos
- Inference examples provided for quick visual comparison
- Lightweight and fast — runs in real time on GPU

---

## 🧩 Model Information

| Property            | Description                   |
| ------------------- | ----------------------------- |
| **Model**           | YOLOv10                       |
| **Framework**       | Ultralytics                   |
| **Classes**         | 2 (`CT`, `T`)                 |
| **Training Source** | Custom CS2 dataset            |
| **Output Type**     | Bounding boxes + class labels |

---

## 🧪 Example Results

Below are some sample detections generated using `yolo predict` command on the trained model.

| Original                           | Detection                        |
| ---------------------------------- | -------------------------------- |
| ![Original 1](docs/original/1.jpg) | ![Detected 1](docs/output/1.jpg) |
| ![Original 2](docs/original/2.jpg) | ![Detected 2](docs/output/2.jpg) |
| ![Original 3](docs/original/3.jpg) | ![Detected 3](docs/output/3.jpg) |
| ![Original 4](docs/original/4.jpg) | ![Detected 4](docs/output/4.jpg) |
| ![Original 5](docs/original/5.jpg) | ![Detected 5](docs/output/5.jpg) |

---

## ⚙️ Usage

### 1️⃣ Clone repository

```bash
git clone https://github.com/yellowDeerrr/CS2-Computer-Vision-YOLO.git
cd CS2-Computer-Vision-YOLO
```

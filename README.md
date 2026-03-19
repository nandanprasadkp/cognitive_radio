#  AI-Based Cognitive Radio System

##  Overview

This project implements a **Cognitive Radio system** using **MATLAB Simulink and Deep Learning (CNN)** to intelligently detect free and occupied spectrum channels.

The system simulates a multi-channel wireless environment and applies AI to perform **automatic spectrum sensing and channel selection**.

---

## System Flow

Simulink → Signal Generation → Dataset Export → CNN Training → Prediction → Free Channel Selection

---

## Key Features

* Multi-channel RF signal simulation (5 channels)
* Random channel activity using Bernoulli switching
* Realistic environment with AWGN noise
* CNN-based spectrum sensing
* Automatic detection of free and occupied channels

---

## Workflow

1. Run Simulink model to generate RF signal
2. Export dataset in MATLAB
3. Train CNN model using Python
4. Predict spectrum occupancy
5. Identify free channels

---

##  Requirements

Install dependencies:

pip install -r requirements.txt

### Libraries Used

* tensorflow==2.15.0
* numpy==1.24.3
* pandas==2.1.0
* scipy==1.11.2

---

## ▶️ How to Run

### Step 1: Generate Dataset (MATLAB)

Run the Simulink model and export dataset.

---

### Step 2: Train Model

```
python train.py
```

---

### Step 3: Predict Spectrum

```
python predict.py
```

---

## 📸 Simulink Model

This shows the multi-channel signal generation setup.

![Simulink](5-results/signalgenerationsetup.png)

---

## 📡 Generated Signal

This represents the combined RF signal across channels.

![Signal](5-results/generatedsignal.jpeg)

---

## 🤖 Output

CNN detects occupied and free spectrum windows.

![Output](5-results/output.jpeg)

---

## 📊 Output Summary

* Total Windows: 8104
* Busy Channels: 8095
* Free Channels: 9
* Availability: 0.11%

---

## 🤖 Pretrained Model

Due to GitHub file size limits, the trained model is hosted externally.

📥 [Download Model](https://drive.google.com/your-link-here)

---

## 🎯 Objective

To enable **efficient spectrum utilization** by automatically detecting free channels and avoiding interference using AI.

---

## 🚀 Future Work

* Reinforcement Learning for dynamic channel selection
* Real-time implementation using SDR
* Extension to 5G/6G networks

---

## 👨‍💻 Authors

* Nandan
* Shreyas



# Simulink Setup

![Setup](results/signalgenerationsetup.png)

---

# Generated Signal

![Signal](results/generatedsignal.jpeg)

---

#Output

![Output](results/output.jpeg)
---
#Authors
* Nandan(ECE NIE MYSORE)
* Shreyas(AI NIT SURATKAL)

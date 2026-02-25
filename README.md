# EcoDetect-YOLO: A Synergistic Framework for Real-time Sanitary Condition Monitoring

This repository contains the official implementation of the paper: 
**"A Synergistic Framework for Real-time Sanitary Condition Monitoring in Semi-outdoor Garbage Rooms using Edge-deployed Deep Learning and GAN-based Augmentation"**.

Submitted to *PeerJ Computer Science*.

## Abstract
Effective waste classification and sanitary monitoring are critical for achieving carbon neutrality and sustainable urban governance. However, deploying automated visual perception systems in semi-outdoor garbage rooms faces significant hurdles, primarily due to drastic illumination fluctuations, visual occlusion by environmental noise (e.g., fallen leaves, water stains), and the computational constraints of edge devices. Existing high-precision models often require prohibitive hardware costs, while lightweight detectors frequently suffer from poor robustness in non-ideal imaging conditions. To address these challenges, this paper proposes a lightweight, robust detection framework tailored for the RK3399 edge computing platform.
First, we construct the GADIG (Garbage Detection dataset of Intelligent Garbage), a large-scale dataset capturing diverse sanitary conditions. To mitigate the long-tail distribution problem of rare waste categories, we employ Generative Adversarial Networks (GANs) to synthesize high-fidelity training samples under extreme lighting scenarios, thereby enhancing the model's generalization capability. Second, we introduce a Structural Similarity Index Measure (SSIM)-based dynamic filtering mechanism. This module acts as a pre-screening stage to filter out over 80% of redundant background frames, significantly reducing the computational load and energy consumption on the edge device. Finally, an optimized single-stage detector is deployed to identify waste accumulation and infrastructure status.
Experimental results on the GADIG dataset demonstrate that the proposed framework achieves a Precision of 79.05%and a Recall of 75.17%even under challenging unstructured environments where traditional baselines fail. Most importantly, the system maintains an inference speed of 78.1FPS on the RK3399 platform, achieving a superior trade-off between detection robustness and real-time performance. This study provides a cost-effective and scalable solution for intelligent waste management in smart cities.


## System Requirements
- Python 3.8+
- PyTorch 1.8+
- Hardware: NVIDIA GPU (for training), RK3399 (for edge inference)

## Installation
```bash
git clone https://github.com/YourUsername/EcoDetect-YOLO.git
cd EcoDetect-YOLO
pip install -r requirements.txt

## Dataset (GADIG)
The **GADIG Dataset** (Garbage Detection dataset of Intelligent Garbage) constructed in this study consists of over 20,000 images covering diverse sanitary conditions and extreme lighting scenarios.

It is open-access and hosted on Zenodo:
- **Download Link:** https://zenodo.org/record/18759483
- **DOI:** 10.5281/zenodo.18759483

Training
To reproduce the results of the EcoDetect-YOLO model (Ours):
Bash
python train.py --img 640 --batch 16 --epochs 100 --data data/ecodetect_data.yaml --cfg models/ecodetect_yolo.yaml --weights yolov5s.pt --name ecodetect_run
Evaluation
To evaluate the model performance:
Bash
python val.py --weights best.pt --data data/ecodetect_data.yaml --img 640
FPS Estimation on RK3399
To estimate the system-level equivalent FPS described in the paper:
Bash
python calc_fps.py
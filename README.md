# EcoDetect-YOLO: A Synergistic Framework for Real-time Sanitary Condition Monitoring

This repository contains the official implementation of the paper: 
**"A Synergistic Framework for Real-time Sanitary Condition Monitoring in Semi-outdoor Garbage Rooms using Edge-deployed Deep Learning and GAN-based Augmentation"**.

Submitted to *PeerJ Computer Science*.

## Abstract
Real-time waste classification in semi-outdoor environments is pivotal for sustainable urban governance but remains constrained by drastic illumination fluctuations, environmental noise (e.g., occlusion by leaves), and the limited computational resources of edge devices. Conventional high-precision models are computationally prohibitive for edge deployment, while lightweight detectors often compromise robustness under non-ideal imaging conditions. To bridge this gap, this paper proposes EcoDetect-YOLO, a robust, hardware-aware detection framework tailored for the RK3399 edge platform. We first introduce the GADIG (Garbage Detection dataset of Intelligent Garbage) dataset, aimed at complex sanitary conditions. To address the long-tail distribution of rare categories, a GAN-based augmentation strategy is employed to synthesize high-fidelity samples under extreme lighting, thereby enhancing model generalization. Furthermore, a Structural Similarity Index Measure (SSIM)-based dynamic filtering mechanism is integrated as a pre-screening stage. This mechanism effectively filters out over 80% of redundant background frames, minimizing computational load without sacrificing detection capability. Experimental results demonstrate that the proposed framework achieves a Precision of 79.05% and a Recall of 75.17%, significantly outperforming traditional baselines in unstructured environments. Notably, the system attains a system-level equivalent inference speed of 78.1 FPS on the RK3399 platform, establishing a superior trade-off between robustness and real-time performance. This work provides a scalable, cost-effective solution for intelligent waste management in smart cities.


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

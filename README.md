# EcoDetect-YOLO: Sanitary Condition Monitoring in Garbage Rooms

## Description
This repository contains the official implementation of **EdgeWaste-YOLO**, a synergistic framework designed for real-time sanitary condition monitoring in semi-outdoor garbage rooms. It integrates a Structural Similarity Index Measure (SSIM) preprocessing module with a lightweight YOLOv5 architecture to achieve high-precision and low-power inference on edge devices (RK3399).

## Dataset Information
The **GADIG Dataset** (Garbage Detection dataset of Intelligent Garbage) constructed in this study contains over 5,000 images covering various weather conditions, extreme lighting, and complex backgrounds.
- **Dataset DOI:** 10.5281/zenodo.18759483
- **Download Link:**[https://zenodo.org/record/18759483](https://zenodo.org/record/18759483)

## Code Information
The codebase is built upon PyTorch and optimized for edge deployment. It includes the SSIM gating mechanism script, the customized Inception-CSP backbone, and the multi-constraint composite loss function.

## Requirements
- Python 3.8+
- PyTorch 1.8+
- OpenCV, NumPy, SciPy
To install the dependencies, run:
  bash
pip install -r requirements.txt
  

## Usage Instructions
1. Training
To train the EcoDetect-YOLO model on the GADIG dataset:
Bash
python train.py --img 640 --batch 16 --epochs 100 --data data/ecodetect_data.yaml --cfg models/ecodetect_yolo.yaml --weights yolov5s.pt --name ecodetect_run
2. Evaluation
To validate the model performance:
Bash
python val.py --weights runs/train/ecodetect_run/weights/best.pt --data data/ecodetect_data.yaml --img 640

## Methodology
The framework operates in three cascaded stages:
Preprocessing: Grayscale conversion and Gaussian blur to mitigate noise.
SSIM-based Gating: Filters out >80% of static background frames dynamically.
EcoDetect-YOLO Inference: Activated only when structural anomalies are detected, significantly reducing computational overhead. GAN-augmented samples are used during offline training to combat the long-tail distribution of rare waste categories.

## Citations
If you find this code or the GADIG dataset useful in your research, please cite our paper (Citation details will be updated upon publication).

## License & Contribution Guidelines
This project is licensed under the MIT License. Contributions and pull requests are welcome.

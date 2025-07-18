<div id="readme-top" align="center">

[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![Stargazers][stars-shield]][stars-url]
[![AGLP License][license-shield]][license-url]
[![python][python]][python-url]

</div>

<div>
<h1 align="center">STRIKE: A Framework for Smoothing High-Impact Martial Arts Motion</h1>

  <p align="center">
    This repository contains the STRIKE framework, designed to enhance motion analysis in martial arts using the Unscented Kalman Filter to improve pose estimation from lightweight YOLO-based detectors.
    <br />
    <a href="https://github.com/alexispfp/strike/issues">Report Bug</a>
  </p>
</div>

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#key-features">Key Features</a>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#results-summary">Results Summary</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

This project introduces the **STRIKE (Smoothed Tracking & Recognition of In-fight Kinetic Engagement)** framework, which leverages the Unscented Kalman Filter (UKF) to improve the accuracy and temporal smoothness of joint tracking in Muay Thai videos. In high-impact sports like Muay Thai, characterized by rapid and complex movements, stable pose estimation is critical for reliable analysis and feedback.

Lightweight pose estimators, while suitable for edge devices, often produce jittery or incomplete detections under occlusion and rapid motion. To address this, STRIKE applies a UKF instance per joint to filter the raw keypoint observations generated from YOLO-based detectors, yielding more stable and accurate pose sequences.

This repository contains a single notebook, `strike.ipynb`, which encapsulates the full experimental pipeline — from pose extraction to filtering and evaluation.

Key components of the STRIKE pipeline:

  1. **Pose Extraction:** Uses a YOLO-based model to extract keypoints from video frames.

  2. **Temporal Filtering:** Applies a UKF to each joint’s 2D trajectory using a 5D state model: $[x, y, v, \theta, \omega]^T$.

  3. **Performance Evaluation:** Analyzes improvements in mean joint error (MPJPE) and detection reliability (F1-Score), including both benchmark testing on the Penn Action dataset and real-world footage.

### Built With

The STRIKE framework is built using modern computer vision and machine learning technologies.

[![python][python2]][python-url]
[![YOLO][yolo]][yolo-url]
[![OpenCV][opencv]][opencv-url]
[![pytorch][pytorch]][pytorch-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Key Features

- **Modular Pipeline:**  
  - **Pose Extraction:** YOLO-based keypoint detection on video frames.
  - **Temporal Filtering:** Per-joint UKF smoothing, leveraging a 5D state model (`[x, y, v, θ, ω]`).
  - **Evaluation:** Automated benchmarking (MPJPE and F1-Score), with qualitative visualization.

- **Benchmark-Backed:**  
  - Processes 2,326 Penn Action sequences, with improvements in MPJPE on 1,135 and F1-Score in 747 sequences.
  - Real-world test: 9,160-frame Muay Thai video processed in 4m 30.3s (RTX 3060, Ryzen 5 2600, 32GB RAM).

- **Reproducible Results:**  
  - All experiments, evaluation scripts, and result visualizations integrated in `strike.ipynb`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

**Prerequisites:**
- Python 3.12+
- Recommended: Virtual environment (conda or venv)
- Notebook dependencies listed in `environment.yml` (or see notebook cell 1).

**Setup:**
```sh
  git clone https://github.com/alexispfp/strike.git
  cd strike
  conda create --name strike python=3.12 # Or use venv
  conda activate strike
```

**Usage:**
1. Open `strike.ipynb` in Jupyter.
2. Run cells sequentially:
   - Load (or generate) keypoints.
   - Configure UKF parameters.
   - Run filtering/evaluation.
   - Inspect tables and visualizations.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Results Summary

| Metric               | Value                |
|----------------------|---------------------|
| Sequences Processed  | 2,326               |
| Mean Raw YOLO MPJPE  | 76.06 pixels        |
| Mean Filtered MPJPE  | 75.37 pixels        |
| Accuracy Improvement | 0.91%               |
| Mean Raw F1-Score    | 0.4280              |
| Mean UKF F1-Score    | 0.4221              |

**Top MPJPE Improvement:** Up to 92% reduction in select outlier sequences.  
**Real-World Speed:** 9,160 Muay Thai frames filtered in under 5 minutes on consumer hardware.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

While STRIKE already demonstrates practical gains on both benchmark and real-world Muay Thai data, future work includes:

 - [ ] ⚙️ Live inference testing on real-time edge devices

 - [ ] 🤖 Integration into referee-assist or coaching systems

 - [ ] 🚀 Adaptation of advanced or learning-based motion models for ballistic strikes

 - [ ] 🦿 Extension to 3D pose estimation pipelines

 - [ ] 📦 Modular support for other detectors (e.g., OpenPose, MoveNet)

See the [open issues](https://github.com/alexispfp/strike/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the AGPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

[![Gmail][mail-shield]][mail-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Github][git]][git-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/alexispfp/strike.svg?style=for-the-badge
[forks-url]: https://github.com/alexispfp/strike/network/members
[stars-shield]: https://img.shields.io/github/stars/alexispfp/strike.svg?style=for-the-badge&color=yellow
[stars-url]: https://github.com/alexispfp/strike/stargazers
[issues-shield]: https://img.shields.io/github/issues/alexispfp/strike.svg?style=for-the-badge
[issues-url]: https://github.com/alexispfp/strike/issues
[license-shield]: https://img.shields.io/github/license/alexispfp/strike.svg?style=for-the-badge
[license-url]: https://github.com/alexispfp/strike/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alexis-p-p-72b733189/
[mail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[mail-url]: mailto:alicepfp@labnet.nce.ufrj.br
[python]: https://img.shields.io/badge/python-gray?style=for-the-badge&logo=python&logoColor=white&labelColor=blue
[python-url]: https://www.python.org
[python2]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[pytorch]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[pytorch-url]: https://pytorch.org
[yolo]: https://img.shields.io/badge/YOLO_Pose-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white
[yolo-url]: https://docs.ultralytics.com/pt/tasks/pose/
[git]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[git-url]: https://github.com/alexispfp
[opencv]: https://img.shields.io/badge/OpenCV-purple?style=for-the-badge&logo=opencv&logoColor=white
[opencv-url]: https://opencv.org

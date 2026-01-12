# ML Project Template (Starter)

This repository is a reusable template for small machine-learning projects, designed to emphasize **engineering discipline over model complexity**.

The goal is to provide a clean, repeatable structure for experimenting with classification problems while maintaining production-quality practices such as deterministic data generation, proper evaluation, and regression testing.

---

## Project Overview

The project simulates a **system health classification problem** using synthetic data.

Each data sample represents a **single snapshot in time** of a system’s condition, described by derived measurements (e.g., magnitude, distortion, imbalance, noise).  
Each snapshot is labeled as one of three states:

- **0 — Normal**
- **1 — Degraded**
- **2 — Anomalous**

The dataset is intentionally noisy and overlapping to reflect real operational ambiguity rather than idealized toy data.

---

## What This Project Demonstrates

This project focuses on **ML workflow correctness**, not algorithm novelty.

Key elements include:

- Deterministic synthetic data generation
- Explicit train / validation / test splits
- Baseline multi-class classification
- Metrics beyond accuracy (macro-F1)
- Machine-readable evaluation artifacts
- Regression testing to enforce minimum model performance
- Clean Git history with incremental changes

---

## Repository Structure
ml-project-template/
├── src/
│   ├── data.py        # Synthetic data generation and splitting
│   ├── train.py       # Baseline model training and evaluation
│   └── hello.py       # Environment sanity check
├── tests/
│   └── test_training.py  # Regression test enforcing performance threshold
├── data/
│   ├── raw/
│   └── processed/
├── reports/
│   └── metrics.json
├── requirements.txt
├── README.md
└── .gitignore

## Running the Project

### 1. Generate the dataset
```bash
python src/data.py


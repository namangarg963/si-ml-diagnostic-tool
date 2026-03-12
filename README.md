
# Machine Learning–Driven Signal Integrity (SI) Diagnostic Tool for High‑Speed PCIe Links

A practical, end‑to‑end **ML + SI** tool that predicts **receiver eye width (ps)** from layout and simulation features and emits **actionable recommendations** (e.g., *add return‑via stitching*, *increase trace spacing*). Includes a before/after case study and a sensitivity sweep.

<p align="center">
  <img src="assets/banner.png" alt="SI ML Diagnostic Tool" width="800"/>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/ready-run%20locally-brightgreen"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue"/></a>
</p>

## ✨ Features
- **Prediction**: Decision‑tree regression to estimate eye width from 4 features.
- **Pass/Fail**: Rule‑based spec check at **35 ps**.
- **Prescriptions**: If `return_via_dist_um > 500` ⇒ add return‑via stitching; if `trace_spacing_mils < 8` ⇒ increase spacing.
- **Case Study**: Before/After optimization demo.
- **Sensitivity Plot**: Eye width vs return‑via distance sweep.
- **Model Persistence**: Saves trained model to `models/`.

> ⚠️ Dataset here is **synthetic** for demonstration. Do **not** upload internal/company data.

## 🧰 Tech Stack
Python • pandas • NumPy • scikit‑learn • matplotlib

## 🗂️ Repository Structure
```
si-ml-diagnostic-tool/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   └── sample_si_dataset.csv
├── models/
│   └── README.md
├── src/
│   ├── train_model.py
│   ├── recommendation_engine.py
│   ├── sensitivity_plot.py
│   └── utils.py
├── docs/
│   ├── theory_background.md
│   ├── system_architecture.md
│   └── example_report.md
├── examples/
│   └── prediction_example.py
└── assets/
    └── banner.png
```

## 🚀 Quick Start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install -r requirements.txt
python src/train_model.py --data data/sample_si_dataset.csv --model models/si_model_v1.pkl
python examples/prediction_example.py --model models/si_model_v1.pkl   --trace_spacing_mils 6 --return_via_dist_um 850 --sim_crosstalk_mv 45 --temp_c 25
python src/sensitivity_plot.py --model models/si_model_v1.pkl --out assets/via_sensitivity.png
```

## 📈 Sensitivity
The `sensitivity_plot.py` sweeps `return_via_dist_um` from 100–1000 µm and plots predicted eye width with a 35 ps spec line.

## 🗺️ Roadmap
- Add RandomForest/XGBoost baselines & model selection
- Add SHAP attributions
- Add basic uncertainty intervals

MIT © Naman Garg

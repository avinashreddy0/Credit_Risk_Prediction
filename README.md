# Fraud Detection App

<p align="center">
  <img src="Gemini_Generated_Image_i45sm2i45sm2i45s.png" alt="Fraud Detection App — secure transactions, protect identity" width="720">
</p>

> **Welcome to the Fraud Detection App** — secure your transactions and protect your identity. This project combines **machine learning**, **interactive dashboards**, and a **Streamlit** web app to spot suspicious financial activity.

---

## Table of contents

- [Overview](#overview)
- [What this project does](#what-this-project-does)
- [Architecture (ML pipeline)](#architecture-ml-pipeline)
- [App walkthrough](#app-walkthrough)
- [Power BI dashboard](#power-bi-dashboard)
- [Tech stack](#tech-stack)
- [How to run](#how-to-run)
- [Project structure](#project-structure)
- [About the developer](#about-the-developer)

---

## Overview

This repository is an end-to-end **fraud detection** project: messy transaction data is cleaned and engineered, models are trained with **Scikit-learn** pipelines, and results are explored in **Power BI** and delivered through a **Streamlit** app where users enter transaction details and get a **live fraud probability** with clear approve / alert style feedback.

---

## What this project does

| Area | Description |
|------|-------------|
| **Data** | ETL, EDA, and feature engineering on transaction-style records (amount, location, device, merchant, etc.). |
| **ML** | Models such as **Logistic Regression**, **Random Forest**, and **Gradient Boosting** inside pipelines; evaluation with accuracy, precision, recall, F1, ROC-AUC, and confusion matrices. |
| **App** | **Streamlit** tabs: hero image, project description, **user input** form, **visualizations**, and **about developer**. |
| **BI** | **Power BI** dashboards for KPIs, fraud rate, geography, and trends. |

---

## Architecture (ML pipeline)

Conceptually the system follows this flow (from raw signals → decision):

1. **Ingest** — transaction streams, user behavior, and account context.  
2. **Feature engineering** — signals like transaction patterns, location consistency, and time-of-day behavior.  
3. **Train** — supervised learning on labeled **fraud vs legitimate** data; optional anomaly-style thinking for rare patterns.  
4. **Deploy** — saved model (`fraud_model.pkl`) serves **real-time inference**.  
5. **Decide** — model outputs a **fraud score / probability**; the app surfaces it so analysts or rules can **approve**, **review**, or **block** high-risk cases.

---

## App walkthrough

The Streamlit app is organized into tabs:

| Tab | Purpose |
|-----|---------|
| **PHOTO** | Project hero / branding image (same style as the banner at the top of this README). |
| **ABOUT PROJECT** | Describes the ML approach, pipelines, metrics, and tools used. |
| **USER INPUT** | Fields such as **amount**, **age**, **device**, **location**, **payment method**, **merchant**, and **category** — then **Predict** runs the loaded model. |
| **VISUALIZATION** | Charts like **amount per location (sum)** and **fraud vs non-fraud** counts from the engineered dataset. |
| **ABOUT DEVELOPER** | Bio, skills, and links (GitHub / LinkedIn). |

**Tip:** After prediction, the app shows **probability**, a **progress bar**, and messages like **Fraud Detected** or **Safe Transaction**, with themed images for fraud vs safe outcomes.

---

## Power BI dashboard

The Power BI report gives a **monitoring-style** view: total amounts, fraud counts, fraud rate, fraud by location, trends over time, and transaction-level detail.

<p align="center">
  <img src="power%20bi/Screenshot%202026-03-22%20174803.png" alt="Power BI fraud dashboard — KPIs and charts" width="720">
</p>

<p align="center">
  <img src="power%20bi/Screenshot%202026-03-22%20174841.png" alt="Power BI — fraud analytics views" width="720">
</p>

<p align="center">
  <img src="power%20bi/Screenshot%202026-03-22%20174929.png" alt="Power BI — transaction and fraud metrics" width="720">
</p>

These screenshots help readers **see** how totals, fraud rate, geography, and time trends are presented alongside the ML app.

---

## Tech stack

- **Python** · **Pandas** · **NumPy**  
- **Scikit-learn** (pipelines, Logistic Regression, Random Forest, Gradient Boosting)  
- **Streamlit** (web UI)  
- **Joblib** (model persistence)  
- **Matplotlib** · **Seaborn**  
- **MySQL** · **ETL**  
- **Power BI**

---

## How to run

1. **Clone** this repository and open the project folder.  
2. **Install** Python dependencies (example):

   ```bash
   pip install pandas scikit-learn streamlit joblib matplotlib seaborn
   ```

3. Ensure **`fraud_model.pkl`** is present at the project root (or adjust the path in `App/app.py`).  
4. Ensure **`feature_engineering.csv`** exists where the app expects it for the **VISUALIZATION** tab (update the path in `App/app.py` if your layout differs).  
5. **Launch** the app:

   ```bash
   streamlit run App/app.py
   ```

> **Note:** Some image and CSV paths in `App/app.py` may point to machine-specific locations. For portability, change those to **paths relative to the project folder** (same idea as the images in this README).

---

## Project structure

| Path | Role |
|------|------|
| `App/app.py` | Streamlit fraud detection application |
| `fraud_model.pkl` | Trained model artifact |
| `Feature Engineering/` | Notebooks and engineered datasets |
| `data/` | Raw and cleaned data |
| `EDA/` | Exploratory analysis |
| `ETL/` | Extract, transform, load notebooks |
| `ML Code/` | Model training notebooks |
| `power bi/` | Power BI dashboard screenshots |
| `SQL/` | Example SQL queries |

---

## About the developer

**Induri Avinash Reddy** — B.Tech Computer Science student at **Chalapathi Institute of Engineering and Technology**, focused on **Data Science** and **Machine Learning**, with experience in Python, MySQL, Power BI, and end-to-end data projects.

- **GitHub:** [github.com/avinashreddy0](https://github.com/avinashreddy0)  
- **LinkedIn:** [Avinash Reddy Induri](https://www.linkedin.com/in/avinash-reddy-induri-4662b832a/)  

**Contact:**  
- Email: induriavinashreddy05@gmail.com  
- Phone: 9346739650  

---

<p align="center">
  <sub>Built with curiosity for safer transactions and clearer data stories.</sub>
</p>

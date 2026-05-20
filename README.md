# AGR-04: Micro-Climate Volatility

## Project Title
Python-Based Statistical Analysis of Micro-Climate Volatility in Smart Greenhouse Systems Using IoT Sensor Data

## Project Overview
This project develops an automated Python-based engineering data pipeline for analyzing greenhouse micro-climate volatility using IoT sensor data.

The system performs automated:

- Data ingestion
- Data cleaning
- Statistical analysis
- Correlation analysis
- Visualization generation

The objective is to evaluate environmental behavior under greenhouse heat-stress conditions.

---

## Dataset Information

Dataset:
Smart Farming Sensor Data for Yield Prediction

Source:
https://www.kaggle.com/datasets/atharvasoundankar/smart-farming-sensor-data-for-yield-prediction

Original Records:
500

Unique Filter Logic:
Temperature > 30°C

Final Records:
53

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

---

## Repository Structure

```plaintext
main.py
requirements.txt
README.md

data/
│
├── dataset_original.csv
└── dataset_cleaned.csv

outputs/
│
├── correlation_heatmap.png
├── humidity_boxplot.png
├── temperature_distribution.png
└── temperature_vs_humidity.png
```

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Run Program

```bash
python main.py
```

---

## Generated Outputs

The program automatically generates:

- Cleaned dataset
- Statistical outputs
- Correlation analysis
- Histogram
- Boxplot
- Scatter plot
- Heatmap

---

## Author

Oliver C. Rodelas

Computer Programming 1

Technological University of the Philippines

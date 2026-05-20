# AGR-04: Micro-Climate Volatility

## Project Title
Python-Based Statistical Analysis of Micro-Climate Volatility in Smart Greenhouse Systems Using IoT Sensor Data

## Description
This project analyzes greenhouse environmental conditions using IoT sensor data and Python-based statistical analytics.

The system performs:

- Dataset ingestion
- Data cleaning
- Unique filtering (Temperature > 30°C)
- Statistical analysis
- Correlation analysis
- Visualization generation

The project evaluates greenhouse micro-climate volatility using environmental variables including temperature, humidity, and soil moisture.

## Dataset
Source:
https://www.kaggle.com/datasets/atharvasoundankar/smart-farming-sensor-data-for-yield-prediction

Unique Filter Logic:
Temperature > 30°C

## Libraries Used
- pandas
- numpy
- matplotlib
- seaborn
- plotly

## Project Structure

```plaintext
main.py
requirements.txt
README.md
data/
outputs/
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## Output
Generated files include:

- cleaned_dataset.csv
- correlation_heatmap.png
- humidity_boxplot.png
- temperature_distribution.png
- temperature_vs_humidity.png

## Author

Oliver C. Rodelas
Computer Programming 1
Technological University of the Philippines

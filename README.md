# Topic Modeling Task

This repository contains the code and data for a project that processes **raw JSON data** into **CSV format** and then applies **topic modeling** techniques to extract coherent themes.

## Overview

- **Raw Data**  
  The initial dataset is provided in JSON format.

- **Data Processing**  
  The JSON data is converted into CSV format using the [`data_processing.py`](data_processing.py) script.

- **Modeling**  
  The [`modeling.ipynb`](modeling.ipynb) Jupyter Notebook loads the processed CSV data and applies topic modeling to identify key themes within the dataset. Running the notebook will display visualizations and key insights derived from the analysis.

## How to Run

### 1. Process the Data
Run the following command to execute the data processing script, which reads the raw JSON data and converts it into CSV format:

```bash
python data_processing.py
```

### 2. Run the Modeling Notebook
Open the `modeling.ipynb` file in Jupyter Notebook and run all the cells to see the topic modeling results.

```bash
pip install -r requirements.txt
```

## Repository Structure

- [`data_processing.py`](data_processing.py) – Script to convert raw JSON data into CSV format.
- [`modeling.ipynb`](modeling.ipynb) – Jupyter Notebook for performing topic modeling analysis.
- `requirements.txt` – List of Python dependencies.
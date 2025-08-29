# LYSO Signal Classification and Visualization

This project demonstrates the classification and visualization of LYSO detector signals using machine learning. The workflow includes reading data from a ROOT file, training a Random Forest classifier, evaluating its performance, and visualizing the results.

### Overview

The main components of the project are:

- **main.py**: The main script that orchestrates data loading, model training, prediction, evaluation, and visualization.
- **utils.py**: Contains utility functions for reading ROOT files and plotting 2D scatter plots of the data.

---

### main.py

1. **Data Loading**: Reads signal data from a ROOT file (`LYSO15x4NTUmentor.root`) using the `read_root` function from `utils.py`.
2. **Feature Preparation**: Separates the features (signal columns) and the target variable (`ID`).
3. **Train/Test Split**: Splits the data into training and testing sets.
4. **Model Training**: Trains a `RandomForestClassifier` on the training data.
5. **Prediction & Evaluation**: Predicts the IDs for the test set and computes the accuracy.
6. **Visualization**:
	- Plots the original data (`original_data.png`).
	- Plots the predicted data (`predicted_data.png`).
	- Identifies and plots misclassified points (`misclassified_data.png`).
7. **Output**: Prints the accuracy and details of misclassified points.

---

### utils.py

- **read_root(fname)**: Reads a ROOT file using `uproot`, extracts the relevant signal columns and the `ID`, and returns a pandas DataFrame.
- **plot2d(df, x, y, size, output_fname)**: Plots a 2D scatter plot of two selected signal columns, coloring points by their `ID`. The plot is saved to the `output/` directory with the specified filename.

---

### Requirements

- Python 3
- pandas
- numpy
- matplotlib
- uproot
- scikit-learn

Install dependencies with:

```bash
pip install pandas numpy matplotlib uproot scikit-learn
```

---

### Usage

Run the main script:

```bash
python main.py
```

This will generate the following plots in the `output/` directory:

- `original_data.png`: Original labeled data
- `predicted_data.png`: Data colored by predicted labels
- `misclassified_data.png`: Points where the model misclassified the ID

---

### Data

The data is expected in the `data/` directory as a ROOT file with a tree named `LYSO` and columns: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, and `ID`.

---

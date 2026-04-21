# 🧑‍💻 Iris Data Visualization

## Problem Statement

The goal of this project is to visualize patterns in the classic **Iris Dataset** using various chart types. By exploring the data visually, we aim to uncover relationships between different flower features and identify patterns across the three Iris species.

---

## Dataset Details

- **Dataset:** Iris Dataset (`iris_dataset.csv`)
- **Features:** Sepal Length, Sepal Width, Petal Length, Petal Width
- **Target:** Species (Setosa, Versicolor, Virginica)
- **Total Records:** 150 samples (50 per species)

---

## Approach

The project is built using Python and generates interactive HTML visualizations. The main script (`main.py`) processes the dataset and produces the following outputs:

- **Bar Chart** – Compares average feature values across species
- **Histogram** – Shows the distribution of individual features
- **Scatter Plot** – Reveals relationships between pairs of features
- **Feature Comparison** – Side-by-side comparison of all features across species

Each chart is saved as a separate HTML file (`chart1.html`, `chart2.html`, `chart3.html`, `chart4.html`) and a combined insights dashboard (`insights.html`) is generated for a holistic view.

---

## Project Structure

```
iris-visualization/
├── main.py               # Main script to generate all visualizations
├── index.py              # Entry point / helper
├── iris_dataset.csv      # Dataset
├── chart1.html           # Bar chart
├── chart2.html           # Histogram
├── chart3.html           # Scatter plot
├── chart4.html           # Feature comparison
├── charts.png            # Static chart snapshot
├── compare.html          # Feature comparison page
├── index.html            # Landing page
├── main.html             # Main dashboard
├── insights.html         # Full insights dashboard
└── README.md             # Project documentation
```

---

## Results

The visualizations clearly reveal:

- **Setosa** is distinctly separable from the other two species based on petal dimensions.
- **Versicolor and Virginica** show some overlap in sepal measurements but are well-separated by petal length and width.
- **Petal Length and Petal Width** are the most discriminative features for species classification.
- The histograms confirm that petal features follow near-normal distributions within each species.

All charts are rendered as interactive HTML files and the full dashboard can be viewed by opening `insights.html` in any browser.

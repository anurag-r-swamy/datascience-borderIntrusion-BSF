# Border Intrusion Behavior Analysis Using K-Means Clustering

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/sklearn-1.0+-orange.svg" alt="Scikit-learn Version">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-Academic-yellow.svg" alt="License">
</p>

## 📋 Project Overview

A comprehensive **defence-oriented machine learning project** that implements K-Means clustering from scratch and using industry-standard libraries to analyze and classify border intrusion behaviors. This project is designed for academic submission, defence-style viva presentation, and live web demonstration.

### 🎯 Key Features

- **Dual Implementation**: K-Means algorithm built from scratch (NumPy/Pandas only) AND using sklearn/scipy
- **Three Distance Metrics**: Euclidean, Manhattan, and Chebyshev distance calculations
- **Multiple Evaluation Metrics**: Silhouette Score, Davies-Bouldin Index, Inertia, Calinski-Harabasz Index
- **Interactive Web Application**: Flask-based UI with real-time prediction capabilities
- **Comprehensive Visualization**: PCA plots, cluster distributions, elbow curves, and radar charts
- **Presentation Mode**: Dedicated presentation page for academic defence

---

## 📁 Project Structure

```
K Border Crossing/
│
├── 📓 Jupyter Notebooks
│   ├── kmeans_from_scratch.ipynb    # Complete K-Means implementation without ML libraries
│   └── kmeans_with_libraries.ipynb  # Professional sklearn/scipy implementation
│
├── 🐍 Flask Application
│   ├── app.py                       # Main Flask application with API endpoints
│   │
│   ├── templates/                   # Jinja2 HTML templates
│   │   ├── base.html               # Base template with navigation
│   │   ├── home.html               # Home page with prediction form
│   │   ├── from_scratch.html       # From-scratch model display
│   │   ├── library_model.html      # Library model display
│   │   ├── comparison.html         # Side-by-side comparison
│   │   ├── presentation.html       # Academic presentation slides
│   │   ├── 404.html                # Custom 404 error page
│   │   └── 500.html                # Custom 500 error page
│   │
│   └── static/                      # Static assets
│       ├── css/style.css           # Custom styling
│       └── js/main.js              # JavaScript functionality
│
├── 📊 Data
│   └── border_intrusion.csv        # Dataset (10,000 records, 6 features)
│
├── 📄 Generated Files (after running notebooks)
│   ├── model_results_scratch.json   # Results from scratch implementation
│   └── model_results_library.json   # Results from library implementation
│
└── 📖 README.md                     # This file
```

---

## 🔬 Dataset Description

| Feature | Description | Range | Defence Significance |
|---------|-------------|-------|---------------------|
| `entry_angle` | Direction of approach | 0-360° | Origin direction identification |
| `speed` | Movement velocity | 0-5 units | Vehicle vs foot traffic detection |
| `speed_variance` | Velocity consistency | 0-2 | Surveillance awareness indicator |
| `stop_duration` | Stationary time | 0-300 units | Reconnaissance activity detection |
| `time_of_intrusion` | Hour of activity | 0-23 | Operational window analysis |
| `path_deviation` | Route directness | 1-2 | Evasive tactics identification |

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install required packages
pip install flask numpy pandas matplotlib scikit-learn scipy seaborn
```

### Running the Application

1. **Run the Jupyter Notebooks** (generate model results):
   ```bash
   # Open and run kmeans_from_scratch.ipynb
   # Open and run kmeans_with_libraries.ipynb
   ```

2. **Start the Flask Web Application**:
   ```bash
   cd "K Border Crossing"
   python app.py
   ```

3. **Open in Browser**:
   ```
   http://localhost:5000
   ```

---

## 📊 Implementation Details

### Part 1: K-Means from Scratch

**Libraries Used**: NumPy, Pandas, Matplotlib (NO sklearn/scipy)

- Manual Z-score normalization
- Custom distance functions (Euclidean, Manhattan, Chebyshev)
- K-Means++ initialization from scratch
- Custom Silhouette Score calculation
- Custom Davies-Bouldin Index calculation
- PCA implementation from scratch for visualization

### Part 2: K-Means with Libraries

**Libraries Used**: sklearn, scipy, seaborn

- StandardScaler for preprocessing
- sklearn PCA for dimensionality reduction
- scipy.spatial.distance for distance calculations
- sklearn.metrics for evaluation
- Custom wrapper for non-Euclidean distance metrics

### Part 3: Model Comparison

| Metric | From Scratch | Library | Notes |
|--------|-------------|---------|-------|
| Silhouette Score | ✅ | ✅ | Higher is better |
| Davies-Bouldin Index | ✅ | ✅ | Lower is better |
| Inertia (WCSS) | ✅ | ✅ | Lower is better |
| Calinski-Harabasz Index | ✅ | ✅ | Higher is better |

---

## 🌐 Web Application Features

### Navigation Tabs

1. **Home**: Live prediction with input form
2. **From Scratch**: Algorithm details and metrics
3. **Library Model**: sklearn implementation results
4. **Comparison**: Side-by-side analysis
5. **Presentation**: Academic defence slides

### API Endpoint

```http
POST /predict
Content-Type: application/json

{
    "entry_angle": 145,
    "speed": 2.5,
    "speed_variance": 0.8,
    "stop_duration": 45,
    "time_of_intrusion": 3,
    "path_deviation": 1.4,
    "distance_metric": "euclidean"
}
```

---

## 📈 Identified Clusters

| Cluster | Name | Characteristics | Threat Level |
|---------|------|-----------------|--------------|
| 0 | Reconnaissance Pattern | Low speed, high stop duration | HIGH |
| 1 | Direct Passage Attempt | High speed, minimal deviation | MEDIUM |
| 2 | Evasive Maneuver | Variable speed, high deviation | HIGH |
| 3 | Opportunistic Intrusion | Night-time, moderate patterns | MEDIUM |

---

## 🎓 Academic Presentation

The project includes a dedicated **Presentation** page with:

- Problem Statement
- Defence Use Case Explanation
- Feature Engineering Details
- Distance Metric Justification
- System Architecture
- Dataset Explanation (Synthetic Data Justification)
- Clustering Results & Graphs
- Model Comparison Analysis
- Conclusion & Future Work

---

## 📝 Viva Preparation

### Likely Questions & Answers

1. **Why K-Means clustering?**
   - Unsupervised learning suitable for unlabeled intrusion data
   - Computationally efficient for large datasets
   - Interpretable cluster assignments

2. **Why three distance metrics?**
   - Different metrics reveal different pattern aspects
   - Euclidean: general similarity
   - Manhattan: robust to outliers
   - Chebyshev: extreme value detection

3. **Why synthetic data?**
   - Real border data is classified
   - Enables academic reproducibility
   - Controlled validation

4. **What is K-Means++ initialization?**
   - Smart centroid initialization
   - Reduces sensitivity to initial positions
   - Converges faster with better results

---

## 🔧 Configuration

### Flask Configuration (app.py)

```python
app.run(debug=True, port=5000, host='0.0.0.0')
```

### Cluster Count

The optimal K=4 was determined using:
- Elbow Method (WCSS curve)
- Silhouette Analysis
- Domain knowledge

---

## 📚 References

1. Lloyd, S. P. (1982). Least squares quantization in PCM
2. Arthur, D., & Vassilvitskii, S. (2007). K-means++: The advantages of careful seeding
3. Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis
4. Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure

---

## 👤 Author

**Academic Project** - Border Intrusion Behavior Analysis

---

## 📄 License

This project is for academic and educational purposes only.

---

<p align="center">
  <strong>🛡️ Secure Borders Through Intelligent Analysis 🛡️</strong>
</p>

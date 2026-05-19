"""
Border Intrusion Behavior Analysis - Flask Web Application
===========================================================
K-Means clustering comparing From-Scratch vs Library (sklearn) implementations.
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import json
import os

app = Flask(__name__)
app.secret_key = 'border_intrusion_analysis_2026'

# ============================================================================
# LOAD MODELS
# ============================================================================

def load_models():
    """Load both scratch and library model results."""
    models = {'scratch': None, 'library': None}
    for name in ['scratch', 'library']:
        path = os.path.join(os.path.dirname(__file__), f'model_results_{name}.json')
        if os.path.exists(path):
            with open(path, 'r') as f:
                models[name] = json.load(f)
    return models

# ============================================================================
# DISTANCE FUNCTIONS
# ============================================================================

def euclidean(p1, p2): return np.sqrt(np.sum((np.array(p1) - np.array(p2)) ** 2))
def manhattan(p1, p2): return np.sum(np.abs(np.array(p1) - np.array(p2)))
def chebyshev(p1, p2): return np.max(np.abs(np.array(p1) - np.array(p2)))

DIST_FUNCS = {'euclidean': euclidean, 'manhattan': manhattan, 'chebyshev': chebyshev}

# ============================================================================
# PREDICTION
# ============================================================================

def predict_cluster(features, centroids, dist_func):
    """Predict cluster for given features."""
    distances = [dist_func(features, c) for c in centroids]
    cluster = int(np.argmin(distances))
    return cluster, float(distances[cluster])

# ============================================================================
# CLUSTER INFO
# ============================================================================

CLUSTERS = {
    0: {'name': 'Accidental Crossing', 'threat': 'LOW', 'desc': 'Unintentional border crossing', 'action': 'Issue warning and redirect', 'color': '#2ECC71'},
    1: {'name': 'Smuggling Activity', 'threat': 'HIGH', 'desc': 'Suspected smuggling operation', 'action': 'Immediate interception and search', 'color': '#E74C3C'},
    2: {'name': 'Reconnaissance', 'threat': 'MEDIUM', 'desc': 'Surveillance and scouting behavior', 'action': 'Deploy covert monitoring', 'color': '#F39C12'},
    3: {'name': 'Hostile Intrusion', 'threat': 'CRITICAL', 'desc': 'Hostile intent detected', 'action': 'Full tactical response', 'color': '#9B59B6'}
}

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def home():
    models = load_models()
    return render_template('home.html', scratch_data=models['scratch'], library_data=models['library'])

@app.route('/from-scratch')
def from_scratch():
    models = load_models()
    return render_template('from_scratch.html', model_data=models['scratch'])

@app.route('/library-model')
def library_model():
    models = load_models()
    return render_template('library_model.html', model_data=models['library'])

@app.route('/comparison')
def comparison():
    models = load_models()
    return render_template('comparison.html', scratch_data=models['scratch'], library_data=models['library'])

@app.route('/presentation')
def presentation():
    models = load_models()
    return render_template('presentation.html', scratch_data=models['scratch'], library_data=models['library'])

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            float(data.get('entry_angle', 0)),
            float(data.get('speed', 0)),
            float(data.get('speed_variance', 0)),
            float(data.get('stop_duration', 0)),
            float(data.get('time_of_intrusion', 0)),
            float(data.get('path_deviation', 1))
        ]
        
        models = load_models()
        if not models['scratch'] or not models['library']:
            return jsonify({'success': False, 'error': 'Models not found. Run generate_models.py first.'})
        
        # Normalize using library model
        model_data = models['library']
        means = np.array(model_data['scaler_mean'])
        stds = np.array(model_data['scaler_scale'])
        normalized = (np.array(features) - means) / stds
        
        # Predict using sklearn library method with Euclidean metric
        centroids = model_data['euclidean']['centroids']
        cluster, distance = predict_cluster(normalized.tolist(), centroids, DIST_FUNCS['euclidean'])
        info = CLUSTERS.get(cluster, CLUSTERS[0])
        
        result = {
            'cluster': cluster,
            'distance': round(distance, 4),
            'cluster_name': info['name'],
            'threat': info['threat'],
            'color': info['color'],
            'accuracy': model_data['euclidean']['accuracy']
        }
        
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("=" * 50)
    print("BORDER INTRUSION BEHAVIOR ANALYSIS")
    print("=" * 50)
    print("\nAccess at: http://127.0.0.1:5001")
    print("\nRoutes: /, /from-scratch, /library-model, /comparison, /presentation")
    print("=" * 50)
    app.run(debug=True, port=5001)

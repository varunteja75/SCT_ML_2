"""
Configuration settings for the clustering project
"""
import os

# Data settings
DEFAULT_N_CUSTOMERS = 1000
RANDOM_STATE = 42

# Clustering settings
MAX_CLUSTERS = 10
MAX_ITERATIONS = 100
CONVERGENCE_THRESHOLD = 1e-4

# File paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')
REPORTS_DIR = os.path.join(OUTPUT_DIR, 'reports')

# Visualization settings
FIGURE_SIZE = (12, 8)
DPI = 300
COLOR_PALETTE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create directories if they don't exist
for directory in [DATA_DIR, OUTPUT_DIR, PLOTS_DIR, REPORTS_DIR]:
    os.makedirs(directory, exist_ok=True)
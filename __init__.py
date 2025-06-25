"""
Customer Clustering Package
"""
__version__ = "1.0.0"
__author__ = "Your Name"

from .kmeans_clustering import CustomerSegmentationAnalyzer
from .data_generator import generate_customer_data
from .visualization import plot_clusters

__all__ = ['CustomerSegmentationAnalyzer', 'generate_customer_data', 'plot_clusters']
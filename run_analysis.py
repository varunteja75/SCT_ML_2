"""
Complete analysis pipeline script
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from kmeans_clustering import CustomerSegmentationAnalyzer
from visualization import ClusterVisualizer
import logging

def run_complete_analysis():
    """Run the complete clustering analysis pipeline"""
    logging.basicConfig(level=logging.INFO)
    
    # Initialize components
    analyzer = CustomerSegmentationAnalyzer()
    visualizer = ClusterVisualizer(save_plots=True)
    
    # Generate data
    print("Step 1: Generating sample data...")
    data = analyzer.generate_sample_data(n_customers=1000)
    
    # Prepare features
    print("Step 2: Preparing features...")
    features = analyzer.prepare_features()
    
    # Find optimal clusters
    print("Step 3: Finding optimal number of clusters...")
    optimal_k, wcss, silhouette = analyzer.find_optimal_clusters()
    
    # Perform clustering
    print(f"Step 4: Performing clustering with k={optimal_k}...")
    model = analyzer.perform_clustering(n_clusters=optimal_k)
    
    # Analyze results
    print("Step 5: Analyzing clusters...")
    summary, interpretations = analyzer.analyze_clusters()
    
    # Create visualizations
    print("Step 6: Creating visualizations...")
    analyzer.visualize_clusters()
    
    print("Analysis completed successfully!")
    return analyzer, visualizer

if __name__ == "__main__":
    analyzer, visualizer = run_complete_analysis()
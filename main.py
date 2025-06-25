"""
Main entry point for customer clustering analysis
"""
import sys
import os
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from kmeans_clustering import CustomerSegmentationAnalyzer
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Run the complete clustering analysis"""
    try:
        logger.info("Starting Customer Segmentation Analysis...")
        
        # Initialize analyzer
        analyzer = CustomerSegmentationAnalyzer()
        
        # Run analysis pipeline
        data = analyzer.generate_sample_data(n_customers=1000)
        features = analyzer.prepare_features()
        optimal_k, _, _ = analyzer.find_optimal_clusters()
        model = analyzer.perform_clustering(n_clusters=optimal_k)
        summary, interpretations = analyzer.analyze_clusters()
        analyzer.visualize_clusters()
        
        # Save results
        os.makedirs('output/reports', exist_ok=True)
        data.to_csv('output/reports/customer_segments.csv', index=False)
        
        logger.info("Analysis completed successfully!")
        return analyzer
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise

if __name__ == "__main__":
    analyzer = main()

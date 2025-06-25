import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

class CustomerSegmentationAnalyzer:
    def __init__(self):
        self.data = None
        self.features = None
        self.model = None
        self.labels = None

    def generate_sample_data(self, n_customers=1000):
        # Generate synthetic customer data for clustering
        np.random.seed(42)
        age = np.random.randint(18, 70, size=n_customers)
        income = np.random.normal(50000, 15000, size=n_customers)
        spending_score = np.random.randint(1, 100, size=n_customers)
        self.data = pd.DataFrame({
            'Age': age,
            'Annual Income': income,
            'Spending Score': spending_score
        })
        return self.data

    def prepare_features(self):
        # Prepare features for clustering
        if self.data is None:
            raise ValueError("Data not generated yet.")
        self.features = self.data[['Age', 'Annual Income', 'Spending Score']]
        return self.features

    def find_optimal_clusters(self, max_k=10):
        # Use elbow method and silhouette score to find optimal number of clusters
        wcss = []
        silhouette = []
        for k in range(2, max_k+1):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.features)
            wcss.append(kmeans.inertia_)
            score = silhouette_score(self.features, kmeans.labels_)
            silhouette.append(score)
        optimal_k = silhouette.index(max(silhouette)) + 2
        return optimal_k, wcss, silhouette

    def perform_clustering(self, n_clusters):
        # Perform KMeans clustering
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.labels = self.model.fit_predict(self.features)
        self.data['Cluster'] = self.labels
        return self.model

    def analyze_clusters(self):
        # Analyze clusters and provide summary and interpretations
        summary = self.data.groupby('Cluster').mean()
        interpretations = {}
        for cluster in summary.index:
            interpretations[cluster] = f"Cluster {cluster}: Avg Age={summary.loc[cluster, 'Age']:.1f}, " \
                                       f"Avg Income=${summary.loc[cluster, 'Annual Income']:.0f}, " \
                                       f"Avg Spending Score={summary.loc[cluster, 'Spending Score']:.1f}"
        return summary, interpretations

    def visualize_clusters(self):
        # Visualize clusters using scatter plot
        plt.figure(figsize=(8,6))
        plt.scatter(self.data['Annual Income'], self.data['Spending Score'], c=self.labels, cmap='viridis')
        plt.xlabel('Annual Income')
        plt.ylabel('Spending Score')
        plt.title('Customer Segments')
        plt.colorbar(label='Cluster')
        plt.show()

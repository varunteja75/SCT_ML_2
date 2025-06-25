import matplotlib.pyplot as plt

class ClusterVisualizer:
    def __init__(self, save_plots=False, save_path='plots/'):
        self.save_plots = save_plots
        self.save_path = save_path

    def plot_clusters(self, data, labels):
        plt.figure(figsize=(8,6))
        scatter = plt.scatter(data['Annual Income'], data['Spending Score'], c=labels, cmap='viridis')
        plt.xlabel('Annual Income')
        plt.ylabel('Spending Score')
        plt.title('Customer Segments')
        plt.colorbar(scatter, label='Cluster')
        if self.save_plots:
            plt.savefig(f"{self.save_path}customer_segments.png")
        plt.show()

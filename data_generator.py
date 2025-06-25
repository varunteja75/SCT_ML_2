import numpy as np
import pandas as pd

def generate_customer_data(n_customers=1000):
    """Generate synthetic customer data for clustering."""
    np.random.seed(42)
    age = np.random.randint(18, 70, size=n_customers)
    income = np.random.normal(50000, 15000, size=n_customers)
    spending_score = np.random.randint(1, 100, size=n_customers)
    data = pd.DataFrame({
        'Age': age,
        'Annual Income': income,
        'Spending Score': spending_score
    })
    return data

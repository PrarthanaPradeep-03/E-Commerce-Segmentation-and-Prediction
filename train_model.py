# train_model.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib
import os

# ===============================
# Load data
# ===============================
# Use raw string (r"") for Windows paths
df = pd.read_csv(r"C:\Users\prart\OneDrive\Desktop\ecommerce segmentation\data.csv", encoding='ISO-8859-1')

# ===============================
# RFM Calculation
# ===============================
# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Reference date for Recency calculation
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Aggregate per customer
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,   # Recency
    'InvoiceNo': 'nunique',                                   # Frequency
    'UnitPrice': lambda x: (x * df.loc[x.index, 'Quantity']).sum()  # Monetary
})

# Rename columns
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'UnitPrice': 'Monetary'
}, inplace=True)

# ===============================
# Features for clustering
# ===============================
X = rfm[['Recency', 'Frequency', 'Monetary']]

# ===============================
# Scale features
# ===============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===============================
# Train KMeans
# ===============================
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# Assign cluster labels
rfm['Cluster'] = kmeans.labels_

# ===============================
# Save models
# ===============================
os.makedirs("models", exist_ok=True)
joblib.dump(kmeans, "models/kmeans_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# ===============================
# Save RFM with clusters
# ===============================
rfm.to_csv("customer_rfm_with_clusters.csv", index=True)

print("✅ RFM table with clusters saved")
print("✅ KMeans model and scaler saved in 'models/' folder")

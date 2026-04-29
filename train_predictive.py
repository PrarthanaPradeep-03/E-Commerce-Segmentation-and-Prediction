import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import os

# -----------------------------
# Paths
# -----------------------------
df = pd.read_csv(r"C:\Users\prart\OneDrive\Desktop\ecommerce segmentation\data.csv", encoding='ISO-8859-1')
models = r"C:\Users\prart\OneDrive\Desktop\ecommerce segmentation\models"


# Make sure model folder exists
os.makedirs(models, exist_ok=True)

# -----------------------------
# Load raw transaction data
# -----------------------------
df = pd.read_csv(r"C:\Users\prart\OneDrive\Desktop\ecommerce segmentation\data.csv", encoding='ISO-8859-1')

print("Columns in dataset:", df.columns.tolist())

# -----------------------------
# Compute RFM features
# -----------------------------
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
today = df['InvoiceDate'].max() + pd.Timedelta(days=1)

# Total purchase amount per row
df['TotalPrice'] = df['UnitPrice'] * df['Quantity']

# Aggregate to customer-level RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (today - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                           # Frequency
    'TotalPrice': 'sum'                               # Monetary
}).rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}).reset_index()

print("RFM table preview:")
print(rfm.head())

# -----------------------------
# Scale features
# -----------------------------
X = rfm[['Recency', 'Frequency', 'Monetary']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# Train KMeans
# -----------------------------
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)
clusters = kmeans.predict(X_scaled)

# Add cluster labels to RFM table
rfm['Cluster'] = clusters

# -----------------------------
# Train Random Forest to predict cluster
# -----------------------------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_scaled, clusters)

# -----------------------------
# Save models and scaler
# -----------------------------
joblib.dump(scaler, os.path.join(models, 'scaler.pkl'))
joblib.dump(kmeans, os.path.join(models, 'kmeans_model.pkl'))
joblib.dump(rf_model, os.path.join(models, 'rf_segment_predictor.pkl'))

print(f"✅ Models and scaler saved successfully in '{models}'")

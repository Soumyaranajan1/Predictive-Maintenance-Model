import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv(r'C:\Users\USER\Desktop\Predictive Maintenance Model\predictive_maintenance.csv')

# Step 1: Clean column names
df.columns = df.columns.str.strip()

# Step 2: Encode 'Type' if present
if 'Type' in df.columns:
    df['Type'] = df['Type'].map({'L': 0, 'M': 1, 'H': 2})

# Step 3: Define feature columns (exact names from CSV)
feature_cols = [
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]'
]

# Step 4: Include 'Type' if available
if 'Type' in df.columns:
    feature_cols.insert(0, 'Type')

# Step 5: Filter only existing columns to avoid KeyError
available_cols = [col for col in feature_cols if col in df.columns]
if len(available_cols) != len(feature_cols):
    missing = set(feature_cols) - set(available_cols)
    raise ValueError(f"Missing expected feature columns: {missing}")

print("Using feature columns:", available_cols)

X = df[available_cols]
y = df['Target']

# Step 6: Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 7: Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Step 9: Save model using pickle
with open('a.dat', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'a.dat'")

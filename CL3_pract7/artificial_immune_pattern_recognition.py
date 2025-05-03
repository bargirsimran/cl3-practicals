import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -----------------------------
# Step 1: Generate Sensor-Based Dummy Data
# -----------------------------
def generate_sensor_data(samples=100):
    # Simulate sensor readings:
    # Vibration: 0 to 10 (arbitrary units)
    # Strain: 0 to 0.05 (e.g., decimal percentage)
    # Displacement: 0 to 0.1 (e.g., in meters)
    vibration = np.random.uniform(0, 10, samples)
    strain = np.random.uniform(0, 0.05, samples)
    displacement = np.random.uniform(0, 0.1, samples)
    
    X = np.vstack((vibration, strain, displacement)).T

    # Assign damage labels based on simple thresholds:
    # 0: No Damage, 1: Minor Damage, 2: Moderate Damage, 3: Severe Damage
    labels = []
    for v, s, d in zip(vibration, strain, displacement):
        if v < 2 and s < 0.01 and d < 0.02:
            labels.append(0)  # No Damage
        elif v < 4 and s < 0.02 and d < 0.04:
            labels.append(1)  # Minor Damage
        elif v < 7 and s < 0.035 and d < 0.07:
            labels.append(2)  # Moderate Damage
        else:
            labels.append(3)  # Severe Damage
    return X, np.array(labels)

# -----------------------------
# Step 2: Define the AIRS Classifier
# -----------------------------
class AIRS:
    def __init__(self, num_detectors=10, hypermutation_rate=0.1):
        self.num_detectors = num_detectors
        self.hypermutation_rate = hypermutation_rate

    def train(self, X, y):
        # Select a few samples as detectors and store their feature vector and the corresponding label
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = [(X[i], y[i]) for i in indices]

    def predict(self, X):
        predictions = []
        for sample in X:
            # Compute the Euclidean distances between the sample and each detector
            distances = [np.linalg.norm(detector[0] - sample) for detector in self.detectors]
            nearest_idx = np.argmin(distances)
            # Use the label from the closest detector as the predicted class
            predictions.append(self.detectors[nearest_idx][1])
        return np.array(predictions)

# -----------------------------
# Step 3: Generate Data and Split (Using Stratified Split)
# -----------------------------
data, labels = generate_sensor_data(100)

# Stratified split so that each class is more likely to appear in training & test sets
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42, stratify=labels
)

# -----------------------------
# Step 4: Train the AIRS and Predict
# -----------------------------
airs = AIRS(num_detectors=15, hypermutation_rate=0.1)
airs.train(X_train, y_train)
predictions = airs.predict(X_test)

# -----------------------------
# Step 5: Evaluate and Display Damage Levels
# -----------------------------
accuracy = accuracy_score(y_test, predictions)
print(f"Overall Accuracy: {accuracy:.4f}\n")

# Map numeric labels to descriptive names
label_map = {0: "No Damage", 1: "Minor Damage", 2: "Moderate Damage", 3: "Severe Damage"}

print("Predicted vs Actual Damage Levels:")
for pred, actual in zip(predictions, y_test):
    print(f"Predicted: {label_map[pred]} \tActual: {label_map[actual]}")

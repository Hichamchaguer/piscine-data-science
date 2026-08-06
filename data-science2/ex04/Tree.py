import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# ======================
# Load arguments
# ======================
train_file = sys.argv[1]
test_file = sys.argv[2]
model_type = sys.argv[3]  # "tree" or "forest"

# ======================
# Load data
# ======================
train = pd.read_csv(train_file)
test = pd.read_csv(test_file)

# ======================
# Prepare data
# ======================
X = train.drop(columns=["knight"])   # change if needed
y = train["knight"]
if "knight" in test.columns:
    test = test.drop(columns=["knight"])  # change if needed

# Split for evaluation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================
# Choose model
# ======================
if model_type == "tree":
    model = DecisionTreeClassifier(max_depth=7, random_state=42)
elif model_type == "forest":
    model = RandomForestClassifier(n_estimators=100, random_state=42)
else:
    print("Choose 'tree' or 'forest'")
    sys.exit()

# ======================
# Train
# ======================
model.fit(X_train, y_train)

# ======================
# Evaluate
# ======================
y_pred = model.predict(X_val)
f1 = f1_score(y_val, y_pred, pos_label="Jedi")

print("F1-score:", f1)

# ======================
# Predict on test
# ======================
test_pred = model.predict(test)

# Save predictions
with open("Tree.txt", "w") as f:
    for p in test_pred:
        f.write(p + "\n")

# ======================
# Plot tree (only for Decision Tree)
# ======================
if model_type == "tree":
    plt.figure(figsize=(12, 8))
    plot_tree(model, feature_names=X.columns, class_names=model.classes_, filled=True)
    plt.show()
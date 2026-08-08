import sys
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, f1_score

# ======================
# Load data
# ======================
train = pd.read_csv(sys.argv[1])
test = pd.read_csv(sys.argv[2])

# ======================
# Prepare data
# ======================
X = train.drop(columns=["knight"])
y = train["knight"]
if "knight" in test.columns:
    X_test = test.drop(columns=["knight"])
else:
    X_test = test

# ✅ Scale features (FIXED)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)

# ======================
# Models
# ======================
forest = RandomForestClassifier(
    n_estimators=250,
    max_depth=10,
    random_state=42
)

logreg = LogisticRegression (
    max_iter=10000,
    solver="saga",
    penalty="l2",
    C=0.1,
    random_state=42,
    class_weight="balanced"
)

knn = KNeighborsClassifier(n_neighbors=5)

# ======================
# Voting Classifier
# ======================
model = VotingClassifier(
    estimators=[
        ("forest", forest),
        ("lr", logreg),
        ("knn", knn)
    ],
    voting="hard"
)

# ======================
# F1-score using cross-validation on SCALED data
# ======================
f1 = cross_val_score(
    model,
    X_scaled,  # ✅ Use scaled data
    y,
    cv=5,
    scoring=make_scorer(f1_score, pos_label="Jedi")
)

print(f"F1-score: {f1.mean():.4f}")

# ======================
# Train on full scaled data
# ======================
vote = model.fit(X_scaled, y)
forest.fit(X_scaled, y)
logreg.fit(X_scaled, y)
knn.fit(X_scaled, y)

# ======================
# Predict on scaled test
# ======================
pred = model.predict(X_test_scaled)

# Individual model predictions
pred_forest = forest.predict(X_test_scaled)
pred_lr = logreg.predict(X_test_scaled)
pred_knn = knn.predict(X_test_scaled)
pred_vote = model.predict(X_test_scaled)

for i in range(10):
    print(f"Sample {i}:")
    print("  Forest :", pred_forest[i])
    print("  LogReg :", pred_lr[i])
    print("  KNN    :", pred_knn[i])
    print("  FINAL  :", pred_vote[i])
    print()

# Save predictions
with open("Voting.txt", "w") as f:
    for p in pred:
        f.write(p + "\n")

print("✅ Predictions saved to Voting.txt")
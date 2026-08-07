import sys
import pandas as pd
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
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

X_test = test  # no target

# ======================
# Models
# ======================
tree = DecisionTreeClassifier(max_depth=8, random_state=42)
forest = RandomForestClassifier(n_estimators=250, random_state=42)
logreg = LogisticRegression(max_iter=1000)
knn = KNeighborsClassifier(n_neighbors=7)

# ======================
# Voting Classifier
# ======================
model = VotingClassifier(
    estimators=[
        ("tree", tree),
        ("forest", forest),
        ("lr", logreg),
        ("knn", knn)
    ],
    voting="hard"
)

# ======================
# F1-score using cross-validation
# ======================
f1 = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring=make_scorer(f1_score, pos_label="Jedi")
)

print("F1-score (CV):", f1.mean())

# ======================
# Train on full data
# ======================
model.fit(X, y)

# ======================
# Predict on test
# ======================
pred = model.predict(X_test)

# Save predictions
with open("Voting.txt", "w") as f:
    for p in pred:
        f.write(p + "\n")

print("Predictions saved ✔")
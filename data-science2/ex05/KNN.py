import sys
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score


if __name__ == "__main__":

    # =========================
    # 1. LOAD DATA
    # =========================
    train = pd.read_csv(sys.argv[1])
    test = pd.read_csv(sys.argv[2])

    # =========================
    # 2. PREPARE DATA
    # =========================
    X = train.drop(columns=["knight"])
    y = train["knight"]

    # =========================
    # 3. SCALE FEATURES
    # =========================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # =========================
    # 4. FIND BEST K
    # =========================
    k_values = range(1, 31)
    scores = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)

        # Cross-validation (F1 score)
        score = cross_val_score(
            knn,
            X_scaled,
            y,
            cv=5,
            scoring='f1_weighted'
        ).mean()

        accuracy = cross_val_score(
            knn,
            X_scaled,
            y,
            cv=5,
            scoring='accuracy'
        ).mean()

        scores.append(accuracy)

    # =========================
    # 5. PLOT RESULTS
    # =========================
    plt.plot(k_values, scores)
    plt.xlabel("k value")
    plt.ylabel("F1-score")
    plt.title("K vs F1-score")
    plt.show()

    # =========================
    # 6. SELECT BEST K
    # =========================
    best_k = k_values[scores.index(max(scores))]
    print("Best k:", best_k)

    # =========================
    # 7. TRAIN FINAL MODEL
    # =========================
    knn = KNeighborsClassifier(n_neighbors=best_k)
    knn.fit(X_scaled, y)

    # =========================
    # 8. PREPARE TEST DATA
    # =========================
    if "knight" in test.columns:
        X_test = test.drop(columns=["knight"])
    else:
        X_test = test

    X_test = scaler.transform(X_test)

    # =========================
    # 9. PREDICT
    # =========================
    predictions = knn.predict(X_test)

    # =========================
    # 10. SAVE RESULTS
    # =========================
    with open("KNN.txt", "w") as f:
        for p in predictions:
            f.write(p + "\n")

    print("Predictions saved to KNN.txt")


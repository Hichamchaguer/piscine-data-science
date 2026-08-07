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
    # with open("KNN.txt", "w") as f:
    #     for p in predictions:
    #         f.write(p + "\n")

    # print("Predictions saved to KNN.txt")








#     import pandas as pd
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score, f1_score
# import matplotlib.pyplot as plt
# import sys

# def main():
#     # 1. Check arguments
#     if len(sys.argv) != 3:
#         print("Usage: python knn.py Train_knight.csv Test_knight.csv")
#         sys.exit(1)
    
#     train_file = sys.argv[1]
#     test_file = sys.argv[2]
    
#     # 2. Load data
#     train_df = pd.read_csv(train_file)
#     test_df = pd.read_csv(test_file)
    
#     # 3. Separate features and target from training data
#     X_train = train_df.drop(columns=['knight'])
#     y_train = train_df['knight']
#     X_test = test_df  # No 'knight' column in test file
    
#     print(f"Training data: {X_train.shape[0]} rows, {X_train.shape[1]} features")
#     print(f"Test data: {X_test.shape[0]} rows, {X_test.shape[1]} features")
    
#     # 4. Scale data
#     scaler = StandardScaler()
#     X_train_scaled = scaler.fit_transform(X_train)
#     X_test_scaled = scaler.transform(X_test)
    
#     # 5. Train KNN with different k values
#     k_values = range(1, 31)
#     f1_scores = []
#     accuracies = []
    
#     for k in k_values:
#         knn = KNeighborsClassifier(n_neighbors=k)
#         knn.fit(X_train_scaled, y_train)
        
#         # 6. Use Validation_knight.csv for validation (if you have it)
#         # OR use cross-validation (recommended)
#         from sklearn.model_selection import cross_val_score
#         cv_scores = cross_val_score(knn, X_train_scaled, y_train, cv=5)
#         accuracies.append(cv_scores.mean())
        
#         # Or if you have Validation_knight.csv:
#         # y_val = validation_df['knight']
#         # X_val = validation_df.drop(columns=['knight'])
#         # X_val_scaled = scaler.transform(X_val)
#         # y_pred = knn.predict(X_val_scaled)
#         # f1_scores.append(f1_score(y_val, y_pred, pos_label='Jedi'))
    
#     # 7. Find best k
#     best_k = k_values[np.argmax(accuracies)]
#     print(f"Best k: {best_k} with accuracy: {max(accuracies):.4f}")
    
#     # 8. Train final model with best k
#     knn_best = KNeighborsClassifier(n_neighbors=best_k)
#     knn_best.fit(X_train_scaled, y_train)
    
#     # 9. Make predictions on test data
#     predictions = knn_best.predict(X_test_scaled)
    
#     # 10. Save predictions
#     with open('KNN.txt', 'w') as f:
#         for pred in predictions:
#             f.write(f"{pred}\n")
    
#     print(f"✅ Predictions saved to KNN.txt")
#     print(f"📊 Best k value: {best_k}")

# if __name__ == "__main__":
#     main()
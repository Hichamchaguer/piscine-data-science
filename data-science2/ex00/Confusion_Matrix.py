import sys
import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(cm, tp, fn, fp, tn):

    fig, ax = plt.subplots(figsize=(6, 6))

    im = ax.imshow(cm, cmap="viridis")

    # Labels
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    ax.set_xticklabels(["Jedi", "Sith"])
    ax.set_yticklabels(["Jedi", "Sith"])

    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    ax.set_title("Confusion Matrix")

    # Write values inside cells
    for i in range(2):
        for j in range(2):
            ax.text(
                j, i,
                str(cm[i, j]),
                ha="center",
                va="center",
                color="white",
                fontsize=18
            )

    plt.colorbar(im)
    plt.tight_layout()
    plt.show()


def main():
    if len(sys.argv) != 3:
        print("Error: Invalid arguments")
        sys.exit(1)

    prediction_file = sys.argv[1]
    truth_file = sys.argv[2]

    try:
        with open(prediction_file, 'r') as f:
            pred_labels = [line.strip() for line in f if line.strip()]
        with open(truth_file, 'r') as f:
            truth_labels = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if len(pred_labels) != len(truth_labels):
        print("Error: The files do not contain the same number of labels")
        sys.exit(1)

    valid_classes = {"Jedi", "Sith"}
    for label in pred_labels + truth_labels:
        if label not in valid_classes:
            print(f"Error: Invalid label '{label}' found in input files")
            sys.exit(1)

    # TP (True Positive) for Jedi: Actual Jedi, Predicted Jedi
    # FN (False Negative) for Jedi: Actual Jedi, Predicted Sith
    # FP (False Positive) for Jedi: Actual Sith, Predicted Jedi
    # TN (True Negative) for Jedi: Actual Sith, Predicted Sith
    tp = sum(1 for t, p in zip(truth_labels, pred_labels) if t == "Jedi" and p == "Jedi")
    fn = sum(1 for t, p in zip(truth_labels, pred_labels) if t == "Jedi" and p == "Sith")
    fp = sum(1 for t, p in zip(truth_labels, pred_labels) if t == "Sith" and p == "Jedi")
    tn = sum(1 for t, p in zip(truth_labels, pred_labels) if t == "Sith" and p == "Sith")

    # Jedi metrics
    precision_jedi = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall_jedi = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1_jedi = 2 * (precision_jedi * recall_jedi) / (precision_jedi + recall_jedi) if (precision_jedi + recall_jedi) > 0 else 0.0
    total_jedi = tp + fn

    # Sith metrics (Sith as positive class)
    # TP_sith = tn
    # FP_sith = fn
    # FN_sith = fp
    # TN_sith = tp
    precision_sith = tn / (tn + fn) if (tn + fn) > 0 else 0.0
    recall_sith = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    f1_sith = 2 * (precision_sith * recall_sith) / (precision_sith + recall_sith) if (precision_sith + recall_sith) > 0 else 0.0
    total_sith = tn + fp

    # Global metrics
    total_samples = len(truth_labels)
    accuracy = (tp + tn) / total_samples if total_samples > 0 else 0.0

    # Print classification report
    print(f"{'':<14}precision recall f1-score total\n")
    print(f"{'Jedi':<17}{precision_jedi:>4.2f}{recall_jedi:>8.2f}{f1_jedi:>8.2f}    {total_jedi}")
    print(f"{'Sith':<17}{precision_sith:>4.2f}{recall_sith:>8.2f}{f1_sith:>8.2f}    {total_sith}\n")
    print(f"{'accuracy':<17}{'':>4}{'':>8}{accuracy:>8.2f}    {total_samples}\n\n")

    # Print Confusion Matrix
    max_len = max(len(str(tp)), len(str(fn)), len(str(fp)), len(str(tn)))
    print("Confusion Matrix:\n")
    arr = np.array([[tp, fn], [fp, tn]])
    print(arr)
    plot_confusion_matrix(arr, tp, fn, fp, tn)




if __name__ == "__main__":
    main()
def calculate_metrics(tp, tn, fp, fn):
    """
    Calculate Accuracy, Precision, Recall, and F1 Score.

    Parameters:
    tp (int): True Positives
    tn (int): True Negatives
    fp (int): False Positives
    fn (int): False Negatives

    Returns:
    dict: Dictionary containing the calculated metrics
    """
    # Accuracy: (TP + TN) / (TP + TN + FP + FN)
    accuracy = (tp + tn) / (tp + tn + fp +
                            fn) if (tp + tn + fp + fn) != 0 else 0

    # Precision: TP / (TP + FP)
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0

    # Recall: TP / (TP + FN)
    recall = tp / (tp + fn) if (tp + fn) != 0 else 0

    # F1 Score: 2 * (Precision * Recall) / (Precision + Recall)
    f1_score = (
        2 * (precision * recall) / (precision + recall)
        if (precision + recall) != 0
        else 0
    )

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1_score,
    }


# Example usage
if __name__ == "__main__":
    # Sample values for demonstration
    tp = int(input("Enter True Positives (TP): "))
    tn = int(input("Enter True Negatives (TN): "))
    fp = int(input("Enter False Positives (FP): "))
    fn = int(input("Enter False Negatives (FN): "))

    metrics = calculate_metrics(tp, tn, fp, fn)

    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

def generate_rationale(
    ml_pred,
    bert_pred,
    ml_prob,
    bert_prob
):

    rationale = []

    if ml_pred == 1:
        rationale.append(
            "Machine Learning predicts REAL."
        )
    else:
        rationale.append(
            "Machine Learning predicts FAKE."
        )

    if bert_pred == 1:
        rationale.append(
            "BERT predicts REAL."
        )
    else:
        rationale.append(
            "BERT predicts FAKE."
        )

    rationale.append(
        f"ML Confidence : {ml_prob:.2f}"
    )

    rationale.append(
        f"BERT Confidence : {bert_prob:.2f}"
    )

    return rationale
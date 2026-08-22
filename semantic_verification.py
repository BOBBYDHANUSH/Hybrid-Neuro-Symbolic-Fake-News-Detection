def semantic_verification(text):

    reasons = []

    if "alien" in text.lower():
        reasons.append(
            "Extraordinary claim detected."
        )

    if "unicorn" in text.lower():
        reasons.append(
            "Unverified entity detected."
        )

    if len(reasons) == 0:
        reasons.append(
            "No semantic inconsistency detected."
        )

    return reasons
import math

def class_weighted_loss(logits, labels, weights):
    n = len(labels)
    total_loss = 0.0

    for row, y in zip(logits, labels):
        m = max(row)
        log_sum_exp = m + math.log(
            sum(math.exp(z - m) for z in row)
        )
        total_loss += weights[y] * (log_sum_exp - row[y])

    return round(total_loss / n, 6)

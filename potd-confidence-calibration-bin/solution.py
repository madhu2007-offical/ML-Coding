
def confidence_calibration_bin(probs, labels, K):
    counts = [0] * K
    sums = [0.0] * K
    positives = [0] * K

    for p, label in zip(probs, labels):
        b = min(K - 1, int(p * K))
        counts[b] += 1
        sums[b] += p
        positives[b] += label

    result = []
    for i in range(K):
        if counts[i] == 0:
            result.append((0, 0.0, 0.0))
        else:
            result.append((
                counts[i],
                sums[i] / counts[i],
                positives[i] / counts[i]
            ))

    return result

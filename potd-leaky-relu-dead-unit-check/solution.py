def leaky_relu_dead_unit_check(x, alpha): return ([round(float(v if v > 0 else alpha * v), 6) for v in x], [1.0 if v > 0 else float(alpha) for v in x])

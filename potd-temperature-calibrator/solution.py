def temperature_calibrator(z, tau): import numpy as np; x = np.asarray(z, dtype=float) / tau; e = np.exp(x - np.max(x)); return e / e.sum()

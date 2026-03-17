import numpy as np


def add_gaussian_noise(signal, noise_level=0.02):

    noise = np.random.normal(0, noise_level, len(signal))

    return (np.array(signal) + noise).tolist()
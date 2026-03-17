import wfdb
import numpy as np


def load_record(record="100", path="mitdb"):

    record = wfdb.rdrecord(f"{path}/{record}")
    signal = record.p_signal[:, 0]

    return signal


def normalize_signal(signal):

    signal = np.array(signal)

    return (signal - signal.mean()) / (signal.std() + 1e-8)
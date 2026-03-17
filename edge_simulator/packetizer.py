from constants import WINDOW_SIZE


def create_packets(signal):

    packets = []

    for i in range(0, len(signal), WINDOW_SIZE):

        packet = signal[i:i + WINDOW_SIZE]

        if len(packet) == WINDOW_SIZE:
            packets.append(packet.tolist())

    return packets
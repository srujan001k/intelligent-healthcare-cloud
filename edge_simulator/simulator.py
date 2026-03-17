import time
import json

from edge_simulator.dataset_loader import load_record, normalize_signal
from edge_simulator.packetizer import create_packets
from edge_simulator.noise import add_gaussian_noise
from edge_simulator.crypto_utils import load_private_key, sign_packet

from schema import ECGPacket
from constants import SAMPLING_RATE, API_URL

import requests


PRIVATE_KEY_PATH = "edge_simulator/keys/private.pem"


def send_packet(packet):

    try:
        response = requests.post(API_URL, json=packet)
        print("Sent:", response.status_code)
    except Exception as e:
        print("Error:", e)


def run():

    signal = normalize_signal(load_record())
    packets = create_packets(signal)

    private_key = load_private_key(PRIVATE_KEY_PATH)

    print("Starting ECG stream...")

    for p in packets:

        noisy = add_gaussian_noise(p)

        payload = json.dumps(noisy).encode()
        signature = sign_packet(private_key, payload)

        packet = ECGPacket(
            raw_signal=noisy,
            signature=signature
        )

        send_packet(packet.model_dump())

        time.sleep(len(p) / SAMPLING_RATE)


if __name__ == "__main__":
    run()
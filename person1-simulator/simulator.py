import numpy as np
import time
from datetime import datetime


# ----------------------------
# PATIENT CLASS
# ----------------------------
class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id

        # Each patient gets slightly different baseline
        self.hr_baseline = np.random.randint(60, 90)
        self.spo2_baseline = np.random.randint(95, 100)
        self.sys_baseline = np.random.randint(110, 130)
        self.dia_baseline = np.random.randint(70, 85)

        self.reading_count = 0
        self.anomaly_active = False
        self.anomaly_duration = 0

    def generate_vitals(self):
        self.reading_count += 1

        # Inject anomaly every 50 readings
        if self.reading_count % 50 == 0:
            self.anomaly_active = True
            self.anomaly_duration = np.random.randint(3, 6)

        if self.anomaly_active:
            self.anomaly_duration -= 1
            if self.anomaly_duration <= 0:
                self.anomaly_active = False

            return {
                "heart_rate": 140,
                "spo2": 85,
                "blood_pressure_systolic": 160,
                "blood_pressure_diastolic": 100
            }

        return {
            "heart_rate": int(np.random.normal(self.hr_baseline, 3)),
            "spo2": int(np.random.normal(self.spo2_baseline, 1)),
            "blood_pressure_systolic": int(np.random.normal(self.sys_baseline, 4)),
            "blood_pressure_diastolic": int(np.random.normal(self.dia_baseline, 3))
        }


# ----------------------------
# JSON BUILDER
# ----------------------------
def build_json(patient_id, vitals):
    return {
        "patient_id": patient_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "vitals": vitals,
        "encrypted": False
    }


# ----------------------------
# MAIN LOOP
# ----------------------------
if __name__ == "__main__":
    patients = [Patient(f"P00{i}") for i in range(1, 6)]

    while True:
        for patient in patients:
            vitals = patient.generate_vitals()
            data = build_json(patient.patient_id, vitals)

            print(data)

        print("----- cycle complete -----\n")
        time.sleep(5)
import unittest
import tinytuya
import time

#Visu mājā esošo viedierīču saraksts.
#Šajā kodā, "device1_id", "device1_key", "device1_ip", "device2_id", "device2_key", "device2_ip", "device3_id", "device3_key", and "device3_ip" jāaizstāj ar reāliem identifikatoriem, atslēgām un jūsu ierīču IP adresēm.

smart_devices = [
    {"id": "device1_id", "key": "device1_key", "ip": "device1_ip"},
    {"id": "device2_id", "key": "device2_key", "ip": "device2_ip"},
    {"id": "device3_id", "key": "device3_key", "ip": "device3_ip"},
]

def turn_on_device(device):
    """Ierīces ieslēgšanas funkcija"""
    d = tinytuya.OutletDevice(device["id"], device["ip"], device["key"])
    d.set_status(True)
    print(f"{device['id']} enabled.")
    return True

def main():
    """Galvenā funkcija, kas ieslēdz visas ierīces startēšanas laikā"""
    for device in smart_devices:
        turn_on_device(device)
        time.sleep(1)  # Pauze starp komandām

class TestTurnOnDevice(unittest.TestCase):
    def test_turn_on_device(self):
        device = {"id": "test_id", "key": "test_key", "ip": "test_ip"}
        self.assertTrue(turn_on_device(device))

if __name__ == "__main__":
    unittest.main()
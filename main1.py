import unittest
import tinytuya
import time
from cryptography.fernet import Fernet

class SmartDevice:
    def __init__(self, id, key, ip):
        self.id = id
        self.key = key
        self.ip = ip

    def encrypt_key(self):
        """Atslēgas šifrēšanas funkcija"""
        cipher_suite = Fernet(Fernet.generate_key())
        cipher_text = cipher_suite.encrypt(self.key.encode())
        return cipher_text

    def turn_on(self):
        """Ierīces ieslēgšanas funkcija"""
        encrypted_key = self.encrypt_key()
        d = tinytuya.OutletDevice(self.id, self.ip, encrypted_key)
        d.set_status(True)
        print(f"{self.id} enabled.")
        return True

class TestTurnOnDevice(unittest.TestCase):
    def test_turn_on_device(self):
        device = SmartDevice("test_id", "test_key", "test_ip")
        self.assertTrue(device.turn_on())

if __name__ == "__main__":
    unittest.main()

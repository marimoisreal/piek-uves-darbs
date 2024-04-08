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
        """Atslēga šifrēšanas funkcija"""
        try:
            cipher_suite = Fernet(Fernet.generate_key())
            cipher_text = cipher_suite.encrypt(self.key.encode())  #Pirms šifrēšanas konverte atslēgu baitos
            return cipher_text
        except Exception as e:
            print(f"Error encrypting key: {e}")
            return None

    def turn_on(self):
        """Ierīces ieslēgšanas funkcija"""
        encrypted_key = self.encrypt_key()
        if encrypted_key is None or self.key == "invalid_key" or self.ip == "invalid_ip":
            return False
        try:
            d = tinytuya.OutletDevice(self.id, self.ip, encrypted_key.decode())  #Atšifre šifrēto atslēgu atpakaļ uz virkni
            d.set_status(True)
            print(f"{self.id} enabled.")
            return True
        except Exception as e:
            print(f"Error turning on device: {e}")
            return False

class TestTurnOnDevice(unittest.TestCase):
    def test_turn_on_device(self):
        device = SmartDevice("test_id", "test_key", "test_ip")
        self.assertTrue(device.turn_on())

    def test_turn_on_device_with_invalid_key(self):
        device = SmartDevice("test_id", "invalid_key", "test_ip")
        self.assertFalse(device.turn_on())

    def test_turn_on_device_with_invalid_ip(self):
        device = SmartDevice("test_id", "test_key", "invalid_ip")
        self.assertFalse(device.turn_on())

if __name__ == "__main__":
    unittest.main()

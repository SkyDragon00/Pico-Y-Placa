from django.test import TestCase
from .services import PicoPlacaPredictor

class PicoPlacaTests(TestCase):
    def test_invalid_plate(self):
        with self.assertRaises(ValueError):
            PicoPlacaPredictor('BADFORMAT', '2025-05-12', '08:00')

    def test_basic_allowed(self):
        # Assuming stub always returns True for now
        p = PicoPlacaPredictor('ABC-1234', '2025-05-12', '08:00')
        self.assertTrue(p.can_drive())

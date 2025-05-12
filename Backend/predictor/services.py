# predictor/services.py

import datetime
import re

class PicoPlacaPredictor:
    """
    Given a full plate string (e.g. 'PBX-1234'), date string, and time string,
    determines if the vehicle may be on the road.
    """

    PLATE_PATTERN = re.compile(r'^[A-Z]{3}-\d{4}$')

    def __init__(self, plate: str, date_str: str, time_str: str, fmt_date='%Y-%m-%d', fmt_time='%H:%M'):
        if not self.PLATE_PATTERN.match(plate):
            raise ValueError(f"Invalid plate format: {plate}")
        self.plate = plate
        self.date = datetime.datetime.strptime(date_str, fmt_date).date()
        self.time = datetime.datetime.strptime(time_str, fmt_time).time()

    def can_drive(self) -> bool:
        """
        Apply Pico y Placa rules (e.g., based on last digit, weekday, and time windows).
        Returns True if allowed, False if restricted.
        """
        # TODO: implement actual rule logic
        return True

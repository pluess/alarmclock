from logutil import get_logger

_min_ldr = 15000
_max_ldr = 58400
_min_display = 5
_max_display = 200

class Brightness:
    """
    Calculates the brightness of the matrix based
    on the current brightness, measures with an LDR
    on GPIO26.
    """

    def __init__(self, ldr) -> None:
        """_summary_

        Args:
            ldr (ModuleType): The ldr.py module or a mock for testing.
        """
        self.ldr = ldr
        self.logger = get_logger(__name__)
        self.min_ldr = _min_ldr
        self.max_ldr = _max_ldr
        self.min_display = _min_display
        self.max_dispaly = _max_display

    def getCurrentBrightness(self) -> int:
        """
        Returns the current brightness value based
        on the LDR mesurament.
        """
        reading = self.ldr.read_sensor()
        ldr = reading
        if reading < self.min_ldr:
            return self.min_display
        if reading > self.max_ldr:
            return self.max_dispaly

        return (int) (((reading - self.min_ldr)/(self.max_ldr-self.min_ldr))*(self.max_dispaly-self.min_display) + self.min_display)


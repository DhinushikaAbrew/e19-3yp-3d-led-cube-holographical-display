
# Core Library modules
import time
from typing import Union

# Third party modules
import RPi.GPIO as GPIO

# GPIO Mode: BOARD - Use Raspberry Pi Board pin numbers
#            BCM   - Use Broadcom GPIO pin numbers

GPIO.setwarnings(False)



class Towers:
    """
    Represents the control module for the LED towers in the 3D LED cube holographical display.

    Args:
        mode (str): The GPIO mode to use. Default is "BCM".
        data_1 (int): The GPIO pin number for data_1. Default is 16.
        data_2 (int): The GPIO pin number for data_2. Default is 12.
        data_3 (int): The GPIO pin number for data_3. Default is 1.
        data_4 (int): The GPIO pin number for data_4. Default is 7.
        clock (int): The GPIO pin number for the clock. Default is 21.
        ics (int): The GPIO pin number for the ics. Default is 2.
    """

    def __init__(
        self,
        mode: str = "BCM",
        data_1: int = 16,
        data_2: int = 12,
        data_3: int = 1,
        data_4: int = 7,
        clock: int = 21,
        latch: int=20,
        ics: int = 2,
    ):
        """
        Initializes the Towers object.

        Raises:
            Exception: If the pins are not unique.
        """
        self._DATA_1 = data_1
        self._DATA_2 = data_2
        self._DATA_3 = data_3
        self._DATA_4 = data_4
        self._CLOCK = clock
        self._LATCH = clock
        self._ICS = ics
        self._mode = mode

        if len({self._DATA_1, self._DATA_2, self._DATA_3, self._DATA_4, self._CLOCK, self._LATCH}) != 6:
            raise Exception("Pins must be unique")

        if self._mode == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self._DATA_1, GPIO.OUT)
        GPIO.setup(self._DATA_2, GPIO.OUT)
        GPIO.setup(self._DATA_3, GPIO.OUT)
        GPIO.setup(self._DATA_4, GPIO.OUT)
        GPIO.setup(self._CLOCK, GPIO.OUT)
        GPIO.setup(self._LATCH, GPIO.OUT)

        GPIO.output(self._DATA_1, GPIO.LOW)
        GPIO.output(self._DATA_2, GPIO.LOW)
        GPIO.output(self._DATA_3, GPIO.LOW)
        GPIO.output(self._DATA_4, GPIO.LOW)
        GPIO.output(self._CLOCK, GPIO.LOW)
        GPIO.output(self._LATCH, GPIO.LOW)
        

    def send_data(self, pattern: list) -> None:
        """
        Sends the data pattern to the LED towers.

        Args:
            pattern (list): The data pattern to send.

        Raises:
            IndexError: If the pattern length is less than 64.
        """
        if len(pattern) < 64:
            raise IndexError("Pattern length must be 64")

        for i in range(16):
            GPIO.output(self._DATA_1, pattern[i])
            GPIO.output(self._DATA_2, pattern[i + 16])
            GPIO.output(self._DATA_3, pattern[i + 32])
            GPIO.output(self._DATA_4, pattern[i + 48])
            GPIO.output(self._CLOCK, GPIO.HIGH)
            #time.sleep(0.0000001)
            GPIO.output(self._CLOCK, GPIO.LOW)
        GPIO.output(self._LATCH, GPIO.HIGH)
        #time.sleep(0.0000001)
        GPIO.output(self._LATCH, GPIO.LOW)


class Layers:
    """
    Represents the control module for the layers in the 3D LED cube holographical display.

    Args:
        mode (str): The GPIO mode to use. Default is "BCM".
        data (int): The GPIO pin number for the data. Default is 13.
        clock (int): The GPIO pin number for the clock. Default is 6.
        latch (int): The GPIO pin number for the latch. Default is 5.
        ics (int): The GPIO pin number for the ics. Default is 2.
    """

    def __init__(
        self,
        mode: str = "BCM",
        data: int = 13,
        clock: int = 6,
        latch: int = 5,
        ics: int = 2,
    ):
        """
        Initializes the Layers object.

        Raises:
            Exception: If the pins are not unique.
        """
        self._DATA = data
        self._CLOCK = clock
        self._LATCH = latch
        self._ICS = ics
        self._mode = mode

        if len({self._DATA, self._CLOCK, self._LATCH}) != 3:
            raise Exception("Pins must be unique")

        if self._mode == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self._DATA, GPIO.OUT)
        GPIO.setup(self._CLOCK, GPIO.OUT)
        GPIO.setup(self._LATCH, GPIO.OUT)

        GPIO.output(self._DATA, GPIO.LOW)
        GPIO.output(self._CLOCK, GPIO.LOW)
        GPIO.output(self._LATCH, GPIO.LOW)

    def set_layer(self, iteration: int) -> None:
        """
        Sets the layer for the LED cube.

        Args:
            iteration (int): The iteration number.

        Raises:
            ValueError: If the iteration is less than 0.
        """
        if iteration < 0:
            raise ValueError("Iteration must be non-negative")

        if iteration == 0:
            GPIO.output(self._DATA, GPIO.LOW)
            GPIO.output(self._CLOCK, GPIO.HIGH)
            #time.sleep(0.0000001)
            GPIO.output(self._CLOCK, GPIO.LOW)
        else:
            GPIO.output(self._DATA, GPIO.HIGH)
            GPIO.output(self._CLOCK, GPIO.HIGH)
            #time.sleep(0.0000001)
            GPIO.output(self._CLOCK, GPIO.LOW)

        GPIO.output(self._LATCH, GPIO.HIGH)
        #time.sleep(0.0000001)
        GPIO.output(self._LATCH, GPIO.LOW)


class MasterLatch:
    """
    Represents the control module for the master latch in the 3D LED cube holographical display.

    Args:
        mode (str): The GPIO mode to use. Default is "BCM".
        latch (int): The GPIO pin number for the latch. Default is 5.
    """

    def __init__(
        self,
        mode: str = "BCM",
        latch: int = 5,
    ):
        """
        Initializes the MasterLatch object.

        Raises:
            Exception: If the pins are not unique.
        """
        self._LATCH = latch
        self._mode = mode

        if self._mode == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self._LATCH, GPIO.OUT)
        GPIO.output(self._DATA, GPIO.LOW)

    def master_latch(self) -> None:
        """
        Performs the master latch operation.
        """
        GPIO.output(self._LATCH, GPIO.HIGH)
        #time.sleep(0.0000001)
        GPIO.output(self._LATCH, GPIO.LOW)

def send_data(self, pattern: list) -> None:
    """
    Sends the data pattern to the LED towers.

    Args:
        pattern (list): The data pattern to send.

    Raises:
        IndexError: If the pattern length is less than 64.

    >>> module = Module()
    >>> module.send_data([0] * 64)  # No exception should be raised

    >>> module.send_data([0] * 63)  # IndexError should be raised
    Traceback (most recent call last):
        ...
    IndexError: Pattern length must be 64

    >>> module.send_data([1] * 64)  # No exception should be raised

    >>> module.send_data([1] * 65)  # No exception should be raised
    """
    if len(pattern) < 64:
        raise IndexError("Pattern length must be 64")

    for i in range(16):
        GPIO.output(self._DATA_1, pattern[i])
        GPIO.output(self._DATA_2, pattern[i + 16])
        GPIO.output(self._DATA_3, pattern[i + 32])
        GPIO.output(self._DATA_4, pattern[i + 48])
        GPIO.output(self._CLOCK, GPIO.HIGH)
        time.sleep(0.0000001)
        GPIO.output(self._CLOCK, GPIO.LOW)
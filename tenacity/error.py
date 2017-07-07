class RetryError(Exception):
    """Encapsulates the last attempt instance right before giving up."""

    def __init__(self, last_attempt):
        self.last_attempt = last_attempt

    def reraise(self):
        if self.last_attempt.failed:
            raise self.last_attempt.result()
        raise self

    def __str__(self):
        return "RetryError[{0}]".format(self.last_attempt)
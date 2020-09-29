"""
We do have a simple class for adding or removing cucumbers.
"""

class CucumberBasket():

    def __init__(self, initial_count=0, max_count=10):
        if initial_count < 0:
            raise ValueError("Initial count must not be negative")
        if max_count < 0:
            raise ValueError("Maximum count couldn't be negative")
        self._count = initial_count
        self._max_count = max_count

    @property
    def count(self):
        return self._count

    @property
    def full(self):
        return self._max_count

    @property
    def add_cucumber(self, count=1):
        new_count = self.count + count
        if new_count > self._max_count:
            raise ValueError("Error: New count is greater than the maximum count value")
        self.count = new_count

    @property
    def remove_cucumber(self, count=1):
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("Error: They cannot be less than 0 cucumbers")
        self.count = new_count
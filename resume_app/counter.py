class Counter:
    def __init__(self, count=0, max=5):
        self.count = count
        self.max = max

    def increment(self):
        self.count += 1
        return self.count % self.max

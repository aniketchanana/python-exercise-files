class Counter:
    def __init__(self,low,high):
        if low>high:
            low,high = high,low
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high :
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for i in Counter(1,10):
    print(i)

        
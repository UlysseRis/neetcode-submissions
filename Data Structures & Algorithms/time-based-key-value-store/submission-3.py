class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = (value, timestamp)

        if key not in self.data:
            self.data[key] = []

        self.data[key].append(t)
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.data:
            return ""
        values = self.data[key]

        if len(values) == 0:
            return ""

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if values[right][1] > timestamp:
            return ""
        return values[right][0]
            
        

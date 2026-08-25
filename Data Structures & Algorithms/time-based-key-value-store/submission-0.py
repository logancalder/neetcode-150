class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        if not arr:
            return ""
        
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            if arr[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        if l > 0:
            return arr[l - 1][1]
        return ""

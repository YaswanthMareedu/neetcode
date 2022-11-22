class TimeMap:

    def __init__(self):
        self.time = {}
        self.max = -999999
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key,value) in self.time:
            self.time[(key,timestamp)].append(value)
        else:
            self.time[(key,timestamp)]=[value]
        if timestamp>self.max:
            self.max = timestamp
        #print(self.time)

    def get(self, key: str, timestamp: int) -> str:
        #print(key,timestamp)
        if timestamp>self.max:
            timestamp = self.max
        for i in range(0,timestamp+1):
            if (key,timestamp-i) in self.time:
                return self.time[key,timestamp-i][-1]
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
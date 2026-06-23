class TimeMap:

    def __init__(self):
        self.store = {}
        # store maps from key -> list of (timestamp, value) tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        if len(self.store[key]) != 0 and self.store[key][-1][0] == timestamp:
            self.store[key][-1] = (timestamp, value)
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timestamped_store = self.store[key]
        if timestamped_store[0][0] > timestamp:
            return ""
        for i in range(len(timestamped_store)):
            if timestamped_store[i][0] <= timestamp:
                if i + 1 == len(timestamped_store):
                    return timestamped_store[i][1]
                else:
                    if timestamped_store[i+1][0] > timestamp:
                        return timestamped_store[i][1]
        return ""
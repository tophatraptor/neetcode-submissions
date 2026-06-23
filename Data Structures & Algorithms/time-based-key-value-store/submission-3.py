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
        lower = 0
        upper = len(self.store[key]) - 1
        offset = (upper - lower) // 2
        cursor = lower + upper
        if self.store[key][lower][0] > timestamp:
                return ""
        if self.store[key][upper][0] < timestamp:
            return self.store[key][upper][1]
        
        while lower <= upper:
            if self.store[key][cursor][0] == timestamp:
                return self.store[key][cursor][1]
            
            if self.store[key][cursor][0] < timestamp:
                if cursor + 1 >= len(self.store[key]) or self.store[key][cursor + 1][0] > timestamp:
                    return self.store[key][cursor][1]
                lower = cursor + 1
                cursor = (upper - lower) // 2 + lower
            else:
                upper = cursor - 1
                cursor = (upper - lower) // 2 + lower
        return ""

# Version 3
# class TimeMap:

#     def __init__(self):
#         self.store = {}
#         # store maps from key -> list of (timestamp, value) tuples

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store:
#             self.store[key] = []
#         if len(self.store[key]) != 0 and self.store[key][-1][0] == timestamp:
#             self.store[key][-1] = (timestamp, value)
#         else:
#             self.store[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.store:
#             return ""
#         lower = 0
#         upper = len(self.store[key]) - 1
#         offset = (upper - lower) // 2
#         cursor = lower + upper
#         if self.store[key][lower][0] > timestamp:
#                 return ""
#         if self.store[key][upper][0] < timestamp:
#             return self.store[key][upper][1]
        
#         while lower <= upper:
            
#             if self.store[key][cursor][0] == timestamp:
#                 return self.store[key][cursor][1]
            
#             if self.store[key][cursor][0] < timestamp:
#                 lower = cursor + 1
#                 cursor = (upper - lower) // 2 + lower
#             else:
#                 upper = cursor - 1
#                 cursor = (upper - lower) // 2 + lower
#         return ""


# Version 2
# class TimeMap:

#     def __init__(self):
#         self.store = {}
#         # store maps from key -> list of (timestamp, value) tuples

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store:
#             self.store[key] = []
#         if len(self.store[key]) != 0 and self.store[key][-1][0] == timestamp:
#             self.store[key][-1] = (timestamp, value)
#         else:
#             self.store[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         lower = 0
#         upper = len(self.store[key]) - 1
#         offset = (upper - lower) // 2
#         cursor = lower + upper
#         if self.store[key][lower][0] > timestamp:
#                 return ""
#         if self.store[key][upper][0] < timestamp:
#             return self.store[key][upper][1]
        
#         while lower <= upper and self.store[key][cursor][0] != timestamp:
            
#             if self.store[key][cursor][0] == timestamp:
#                 return self.store[key][cursor][1]
            
#             if self.store[key][cursor][0] < timestamp:
#                 lower = cursor + 1
#                 cursor = (upper - lower) // 2 + lower
#             else:
#                 upper = cursor - 1
#                 cursor = (upper - lower) // 2 + lower
#         return ""



# Version 1
# class TimeMap:

#     def __init__(self):
#         self.store = {}
#         # store maps from key -> list of (timestamp, value) tuples

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store:
#             self.store[key] = []
#         if len(self.store[key]) != 0 and self.store[key][-1][0] == timestamp:
#             self.store[key][-1] = (timestamp, value)
#         else:
#             self.store[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.store:
#             return ""
#         timestamped_store = self.store[key]
#         if timestamped_store[0][0] > timestamp:
#             return ""
#         for i in range(len(timestamped_store)):
#             if timestamped_store[i][0] <= timestamp:
#                 if i + 1 == len(timestamped_store):
#                     return timestamped_store[i][1]
#                 else:
#                     if timestamped_store[i+1][0] > timestamp:
#                         return timestamped_store[i][1]
#         return ""
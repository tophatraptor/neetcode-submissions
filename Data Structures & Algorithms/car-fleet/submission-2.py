class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = [(pos, spd) for pos, spd in zip(position, speed)]
        merged.sort(key = lambda x: x[0])
        # Now sorted in ascending order
        fleets = []
        for pos, spd in merged:
            if len(fleets) == 0:
                fleets.append((pos, spd))
                continue
            cur_arrival = (target - pos) / spd
            while len(fleets) > 0:
                # If C1 is faster than C2, then pop C1 before appending C2
                prev_pos, prev_spd = fleets[-1]
                prev_arrival = (target - prev_pos) / prev_spd
                if prev_arrival <= cur_arrival:
                    fleets.pop()
                else:
                    break
            fleets.append((pos, spd))
        return len(fleets)
"""
So, the way this works is that a car is limited by the car in front of it.

For any two cars, C1 and C2, if C1 would reach or pass C2's position by the end
of the trip, then C1 and C2 will merge. So what we need to do then is:
- Start adding cars to the stack
- Each time we come across the car, we calculate whether or not our top of stack
(C1) will pass C2 by the end. If it is, then we can merge them. If they won't, then
we can append a new car to the end of the stack.

By default, this is a n**2 problem, since we would ahve to 

If we sort it, this becomes a O(nlogn) for sort + O(n) for actually merging
in each of the items; so we'll do that.

I see; there's a gap in my implementation. My implementation only addresses the most recent car on the stack.

However, it's possible that we have the late arrival of a car that collapses many candidates together.

Therefore, we continually pop from the stack until we've formed our "fleet", headed by the current car.
"""
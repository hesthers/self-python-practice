class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = altitude = 0 
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
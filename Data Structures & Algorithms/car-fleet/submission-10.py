class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the car positions first
        # Create time array that contains the time that each car will reach the target
        # without consider the fleet conditions
        fleet = 0 
        car_data = sorted(zip(position,speed), key=lambda x : x[0])
        time_car = [ (target-pos)/speed for pos,speed in car_data]
        print(time_car)
        for i in range(len(time_car)-2, -1,-1):
            print(time_car[i], time_car[i+1])
            if time_car[i] < time_car[i+1]:
                time_car[i] = time_car[i+1]
        print(time_car)
        fleet = len(set(time_car))
        return fleet
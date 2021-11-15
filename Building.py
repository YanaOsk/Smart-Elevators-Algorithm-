

class Building:
    def __init__(self,minFloor , maxFloor , elevators):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = elevators

    def __str__(self):
        return f"_minFloor:{self.minFloor} _maxFloor:{self.maxFloor} _elevators:{self.elevators}"

    def __repr__(self):
        return f"_minFloor:{self.minFloor} _maxFloor:{self.maxFloor} _elevators:{self.elevators}"
class Elevator:
    def __init__(self,id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime):

        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime



    def __str__(self):
        return f"_id:{self.id} _speed:{self.speed} _minFloor:{self.minFloor} _maxFloor:{self.maxFloor} _closeTime:{self.closeTime} _openTime:{self.openTime} _startTime:{self.startTime} _stopTime:{self.stopTime}"

    def __repr__(self):
        return f"_id:{self.id} _speed:{self.speed} _minFloor:{self.minFloor} _maxFloor:{self.maxFloor} _closeTime:{self.closeTime} _openTime:{self.openTime} _startTime:{self.startTime} _stopTime:{self.stopTime}"



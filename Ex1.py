import sys
import json
import csv
from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator


def json_to_obj_elev(build_json):
    try:
        with open(build_json, "r+") as f:
            elv = []
            arr = []
            elevator_dict = json.load(f)
            elev_for_obj = elevator_dict["_elevators"]
            for k in elev_for_obj:
                e1 = Elevator(k["_id"], k["_speed"], k["_minFloor"], k["_maxFloor"], k["_closeTime"], k["_openTime"],
                              k["_startTime"], k["_stopTime"])
                elv.append(e1)
            return elv
    except IOError as e:
        print(e)


def json_to_obj(build_json):
    try:
        with open(build_json, "r+") as f:
            building_dictionary = json.load(f)
            return Building(building_dictionary["_minFloor"], building_dictionary["_maxFloor"],
                            json_to_obj_elev(build_json))

    except IOError as e:
        print(e)


def csv_to_list_of_obj(calls_csv):
    calls = []
    with open(sys.argv[2]) as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        for row in csv_reader:
            c = CallForElevator(elv=str(row[0]), time=float(row[1]), src=int(row[2]), dest=int(row[3]),
                                elv_pos=int(row[4]), alloc=int(row[5]))
            calls.append(c)
    return calls



def insert_zero(calls):
    for call in calls:
        call.alloc = 0

def make_out_file(calls, file_name):
    new_list = []
    for call in calls:
        new_list.append(call.__dict__.values())
    with open(file_name, "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(new_list)

#########ZUR LOOK AT HERE ########################################################
def calcTimeForOneCall(elv, call):
    """Function that calculates how much time it takes to one call"""
    time1 = abs((call.elv_pos - call.src) * elv.speed) + elv.closeTime + elv.openTime + abs(
        (call.dest - call.src) * elv.speed) + elv.closeTime + elv.openTime
    return time1


def checkIfEmpty(arr):
    """Function that checks if the elevators array is empty or not(if it have calls inside)"""
    isEmpty = False
    for i in arr:
        if not any(arr):
            isEmpty = True
    return isEmpty


def calcTimeForCallsInArr(arr):
    """Function that calculates how much time it will take to elevator to do all calls"""
    allTime = 0
    for i in arr:
        for j in arr[i]:
            if checkIfEmpty(arr[j]) == False:
                allTime += calcTimeForOneCall(arr[i], arr[j])
    return allTime


def allocateCall(arr, call):
    """A function that inserts an elevator call considering the times"""
    minTime = 0
    elevid = 0
    for i in arr:
        for j in arr:
            if checkIfEmpty(arr[j]) == True:
                call.alloc = arr[j]
            else:
                timeForOne = calcTimeForOneCall(arr[i], arr[j])
            allTime = calcTimeForCallsInArr(arr[j])
            x = timeForOne + allTime
            if minTime > x:
                minTime = x
                elevid = arr[i]
                call.alloc = elevid




    if __name__ == '__main__':
        print(sys.argv)
        print(sys.argv[1])
        b1 = json_to_obj(sys.argv[1])
        print("Our Building: ")
        print(b1)
        print("---------------")
        print("Our Elevators")
        e1 = json_to_obj_elev(sys.argv[1])
        print(e1)
        print("------------")
        print("Our Calls")
        c1 = csv_to_list_of_obj(sys.argv[2])
        print(c1)
        print("----------------")
        make_out_file(c1, sys.argv[3])


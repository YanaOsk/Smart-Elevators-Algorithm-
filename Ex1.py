import sys
import json
from Building import Building
import csv
from CallForElevator import CallForElevator
from Elevator import Elevator


def json_to_obj_elev(build_json):
    try:
        with open(build_json, "r+") as f:
            elv = []
            elevator_dict = json.load(f)
            elev_for_obj = elevator_dict["_elevators"]

            lastpos = 0
            counter = 0
            for k in elev_for_obj:
                e1 = Elevator(k["_id"], k["_speed"], k["_minFloor"], k["_maxFloor"], k["_closeTime"], k["_openTime"],
                              k["_startTime"], k["_stopTime"], [], lastpos)
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


def allocate_id_to_call(calls, building):
    all_calls_time = []
    for i in building.elevators:
        all_calls_time.append(0)
    for call in calls:
        min_time = sys.maxsize
        id_elv = 0

        for elvator in building.elevators:
            calltime = calcTimeForOneCall(elvator, call)
            if (calltime + all_calls_time[building.elevators.index(elvator)]) < min_time:
                min_time = calcTimeForOneCall(elvator, call) + all_calls_time[building.elevators.index(elvator)]
                id_elv = building.elevators.index(elvator)
        all_calls_time[id_elv] += calcTimeForOneCall(building.elevators[id_elv], call)
        building.elevators[id_elv].arr.append(call)
        call.alloc = building.elevators[id_elv].id


def make_out_file(calls, file_name):
    new_list = []
    for call in calls:
        new_list.append(call.__dict__.values())
    with open(file_name, "w", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(new_list)


def calcTimeForOneCall(elv, call):
    """Function that calculates how much time it takes to one call"""
    stoptime = elv.closeTime + elv.startTime + elv.stopTime + elv.openTime
    if isEmpty(elv.arr) == True:
        time1 = abs((0 - call.src) ** elv.speed) + stoptime + abs((call.dest - call.src) * elv.speed) + stoptime
    else:
        time1 = abs((elv.arr[len(elv.arr) - 1].dest - call.src) * elv.speed) + stoptime + abs(
            (call.dest - call.src) * elv.speed) + stoptime
    return time1


def isEmpty(arr):
    """Function that checks if the elevators array is empty or not(if it have calls inside)"""
    isEmpty = False
    if len(arr) == 0:
        isEmpty = True
    return isEmpty


building = json_to_obj(sys.argv[1])
calls = csv_to_list_of_obj(sys.argv[2])
allocate_id_to_call(calls, building)
make_out_file(calls, sys.argv[3])

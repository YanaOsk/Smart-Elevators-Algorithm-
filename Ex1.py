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
            # print(type(elv))
            elevator_dict = json.load(f)
            elev_for_obj = elevator_dict["_elevators"]
            # print(e1)
            counter = 0
            for k in elev_for_obj:
                e1 = Elevator(k["_id"], k["_speed"], k["_minFloor"], k["_maxFloor"], k["_closeTime"], k["_openTime"],
                              k["_startTime"], k["_stopTime"])

                # print(e2)
                # print(type(e2))
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
            c = CallForElevator(elv=str(row[0]), time=float(row[1]), src=int(row[2]), dest=int(row[3]), elv_pos=int(row[4]), alloc=int(row[5]))
            calls.append(c) 

    # print(temp )
    return calls


def insertDataCall_and_CalcTime(elv, calls):
    id_elev = 0
    time_arr = []
    avg = 0
    min_avg = 0
    temp_dict = {}
    for k, v in temp_dict.items():
        temp_dict[k] = elv[k]
        temp_dict[v] = calls[v]
    print(temp_dict)
    # for i,j in temp_dict.items():
    #     floor = temp_dict[j]
    #


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


if __name__ == '__main__':
    # print(sys.argv)
    # print(sys.argv[1])
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
    # insertDataCall_and_CalcTime(e1,c1)
    insert_zero(c1)
    make_out_file(c1, sys.argv[3])

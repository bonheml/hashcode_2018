from itertools import dropwhile

from io_utils import read_file, write_file


def clear_missed_rides(rides, max_time, ctime):
    time_left = max_time - ctime
    if rides and rides[0].score > time_left:
        rides = list(dropwhile(lambda x: x.score > time_left, rides))
    return rides


def run_example(input_file, output_file):
    print("Reading file: {}\n".format(input_file))
    max_time, bonus, cars, rides, cars_nb = read_file(input_file)
    for ctime in range(max_time):
        cars_idle = 0
        for car in cars:
            car.drive(rides)
            if car.current_ride is None:
                cars_idle += 1
        rides = clear_missed_rides(rides, max_time, ctime)
        if not rides and cars_idle == cars_nb:
            break
    write_file(cars, output_file)

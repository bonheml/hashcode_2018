from Car import Car
from Ride import Ride


def read_file(input_file):
    rides = []
    with open(input_file) as f:
        lines = f.readlines()
        _, _, cars_nb, _, bonus, time = list(map(int, lines.pop(0).split()))
        for i, line in enumerate(lines):
            args = list(map(int, line.split()))
            rides.append(Ride(i, *args))
        rides = sorted(rides, key=lambda x: x.score, reverse=True)
        cars = [Car(time, bonus) for _ in range(cars_nb)]
    return time, bonus, cars, rides, cars_nb


def write_file(c, output_file):
    with open(output_file, 'w') as f:
        for car in c:
            f.write(car.__str__() + '\n')

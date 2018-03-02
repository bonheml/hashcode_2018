from algo_utils import get_manhattan


class Car:
    def __init__(self, max_time, bonus):
        self.position = (0, 0)
        self.passed_rides = []
        self.current_ride = None
        self.max_time = max_time
        self.ctime = 0
        self.goal = (0, 0)
        self.ride_time = 0
        self.bonus = bonus

    def choose_best_ride(self, rides):
        scores = []
        ride = None
        for r in rides:
            dist = get_manhattan(self.position, r.start)
            if r.score + dist <= (self.max_time - self.ctime):
                ride_start = abs(self.ctime + dist - r.earliest_start)
                score = r.score - ride_start
                if ride_start == 0:
                    score += self.bonus
                scores.append((score, r))
        if scores:
            ride = max(scores, key=lambda x: x[0])[1]
            rides.remove(ride)
        return ride

    def get_new_ride(self, rides):
        self.current_ride = self.choose_best_ride(rides)
        if self.current_ride is None:
            return
        if self.position != self.current_ride.start:
            self.goal = self.current_ride.start
            self.ride_time = get_manhattan(self.position,
                                           self.current_ride.start)
        else:
            self.goal = self.current_ride.goal
            self.ride_time = get_manhattan(self.position,
                                           self.current_ride.goal)

    def update_position(self, rides):
        self.position = self.goal
        if self.current_ride.goal == self.goal:
            self.passed_rides.append(self.current_ride)
            self.get_new_ride(rides)
        elif self.ctime >= self.current_ride.earliest_start:
            self.goal = self.current_ride.goal
            self.ride_time = self.current_ride.score

    def drive(self, rides):
        if self.current_ride is None:
            self.get_new_ride(rides)
        elif self.ride_time <= 0:
            self.update_position(rides)
        self.ride_time -= 1
        self.ctime += 1

    def __str__(self):
        res = "{}".format(len(self.passed_rides))
        for p in self.passed_rides:
            res += " {}".format(p.id)
        return res

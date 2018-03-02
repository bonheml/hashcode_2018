from algo_utils import get_manhattan


class Ride:
    def __init__(self, ride_id, start_x, start_y, goal_x, goal_y,
                 earliest_start, latest_finish):
        self.id = ride_id
        self.start = (start_x, start_y)
        self.goal = (goal_x, goal_y)
        self.score = get_manhattan(self.start, self.goal)
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

    def __str__(self):
        return ("Ride n°{} from {} to {} with score {}"
                .format(self.id, self.start, self.goal, self.score))

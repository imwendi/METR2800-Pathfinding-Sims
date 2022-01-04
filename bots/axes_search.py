"""
Path-finding algorithm by searching for grid-axis

"""
import numpy as np
from .basic_algo import BasicBot
import itertools

class AxesSearch(BasicBot):
    def navigate(self, num_points=10):
        theta_x, dx, dy = self.find_axes(num_points)

        if theta_x is None:
            return

        # side_length, _ = self.get_map().get_dims()
        # side_length /= 2.0

        self.turn(theta_x)
        self.equalize_distance()
        self.turn(90)
        self.equalize_distance()

    def find_axes(self, num_points):
        """
        Returns angular position of the map's x-axis and the cartesian
        coordinates of the robot's current position with respects to the map.

        Args:
            num_points: Number of angular points to sample in a rotation

        Returns:
            theta_x: Angle from x-coord
            dx: Distance to wall in direction of x-coord
            dy: Distance to wall in direction of  y-coord

        """
        # Sample distances around the robot
        d_theta = 2*np.pi/num_points
        distances = np.zeros(num_points)

        for i in range(num_points):
            distances[i] = self.sense()
            self.turn(d_theta, degrees=False)

        # Compute segment lengths and find segments the same length as the side
        # lengths of the map
        segments = distances[:num_points//2] + distances[num_points//2:]
        l,_ = self.get_map().get_dims()
        angles = np.linspace(0, np.pi, num_points//2)
        lengths = [(angles[i], distances[:num_points//2][i])
                   for i, length in enumerate(segments)
                   if np.abs(length - l) < 0.5]

        # All combinations of found lengths
        length_combos = list(itertools.combinations(lengths, r=2))

        # Compute theta_x, dx, dy (-1 indicates error)
        theta_x, dx, dy = None, None, None

        for (theta1, l1), (theta2, l2) in length_combos:
            if np.abs((np.abs(theta1 - theta2) - np.pi/2)) < np.deg2rad(10):
                if theta1 < theta2:
                    theta_x = theta1
                    dx = l1
                    dy = l2
                else:
                    theta_x = theta2
                    dx = l2
                    dy = l1

        return theta_x, dx, dy







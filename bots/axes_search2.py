"""
Path-finding algorithm by searching for grid-axis

"""
import numpy as np
from .basic_algo import BasicBot
from sim import find_nearest
import itertools


class AxesSearch2(BasicBot):
    def navigate(self, num_points=10, plot_ax=False):
        """


        Args:
            num_points: Number of points to sample
            plot_ax: Whether or not the plot the direction of axes found with
                    dotted lines

        Returns:

        """
        theta_x, x_dist, y_dist = self.find_axes(num_points)

        if theta_x is None:
            return

        side_length, _ = self.get_map().get_dims()
        side_length /= 2.0

        dx, dy = x_dist - side_length, y_dist - side_length
        self.turn(theta_x, degrees=False)
        self.move(dx)
        self.turn(90)
        self.move(dy)


    def find_axes(self, num_points):
        """
        Returns angular position of the map's x-axis and the cartesian
        coordinates of the robot's current position with respects to the map.

        Args:
            num_points: Number of angular points to sample in a rotation

        Returns:
            theta_x: Angle from x-coord
            x_dist: Distance to wall in direction of x-coord
            y_dist: Distance to wall in direction of  y-coord

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

        # Find the indices of the 5 measured segments whose lengths are closest
        # to the side length of the map
        direction_indices = find_nearest(segments, l, 5)
        # Create tuples of directions (angle, segment length) corresponding to
        # the found segments
        directions = [(angles[i], distances[:num_points//2][i])
                   for i in direction_indices]

        # All combinations of two directions
        length_combos = list(itertools.combinations(directions, r=2))
        angle_differences = [np.abs(theta1 - theta2) for
                             (theta1, l1), (theta2, l2) in length_combos]
        # Chose the pair of directions whose angular difference is closest to
        # a right angle
        combo_index = find_nearest(angle_differences, 90, 1)
        (theta1, l1), (theta2, l2) = length_combos[combo_index]

        # Assign output values
        if theta1 < theta2:
            theta_x = theta1
            x_dist = l1
            y_dist = l2
        else:
            theta_x = theta2
            x_dist = l2
            y_dist = l1

        return theta_x, x_dist, y_dist

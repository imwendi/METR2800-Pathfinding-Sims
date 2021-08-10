import numpy as np
from .utils import angle_is_between


class Bot():
    def __init__(self, map, x=0, y=0, theta=0, min_rad=25, random=True):
        """
        Spawns a new bot in given x, y, theta (position and orientation),
        unless random is True in which case a randomized position and
        orientation are used.

        Args:
            map: Map to add bot to
            x, y: Coords of spawn point (cm)
            theta: Angle bot faces (degrees)
            min_rad: Minimum distance away from center to spawn

        """
        self.map = map

        # Set initial position of bot
        if random:
            self.x, self.y = 0, 0
            width, height = map.get_dims()
            # Ensure bot spawns outside of center rings
            while np.linalg.norm([self.x, self.y]) < min_rad:
                self.x = np.random.uniform(-width/2, width/2)
                self.y = np.random.uniform(-height/2, height/2)

            self.theta = np.random.uniform(0, 2*np.pi)
        else:
            self.x = x
            self.y = y
            self.theta = np.deg2rad(theta)

        # Arrays to store traversed points
        self.x_path = [self.x]
        self.y_path = [self.y]

        # Add bot to map
        map.add_bot(new_bot=self)

    def sense(self):
        """
        Simulates distance sensing proximity to a wall in a given direction.
        By default the direction is that of the robots orientation.

        Args:
            sensor_theta: Orientation of sensor relative to robot body
            degrees: If sensing_angle is in degrees

        Returns:
            Distance to wall in cm (Tuple is returned in 'both' mode)
            Otherwise returns -1 on error

        """
        # Compute angles to corners of 1st-4th quadrants
        l,_ = self.get_map().get_dims()
        l /= 2
        x0, y0 = self.get_pos()
        angles = [np.arctan2(y-y0, x-x0) for (x, y) in
                  [(l, l), (-l, l), (-l, -l), (l, -l)]]

        # Determine the wall the bot is facing (left, top, right, bottom)
        theta = self.get_theta()
        m = np.tan(theta)
        wall = None

        # Place theta in the same range as np.arctan2's output
        wall_coords = [(l, None), (None, l), (-l, None), (None, -l)]
        for i in range(-1, 3):
            #if angles[i] <= theta <= angles[i+1]:
            if angle_is_between(theta, angles[i], angles[i+1]):
                wall = wall_coords[i+1]

        if wall is None:
            print(f'None for theta = {np.degrees(theta)}')
            print(f'Angles: {[np.degrees(i) for i in angles]}')

        # Determine the intercept (x1, y1) on the wall
        if wall[0] is not None:
            x1 = wall[0]
            y1 = m*(x1 - x0) + y0
        else:
            y1 = wall[1]
            x1 = (y1 - y0)/m + x0

        return np.linalg.norm(np.array([x1, y1]) - np.array([x0, y0]))

    def move(self, distance):
        """
        Moves the bot a specified distance in the direction specified by its
        current theta.

        Args:
            distance: Distance to move

        """
        next_x = self.x + distance*np.cos(self.theta)
        next_y = self.y + distance*np.sin(self.theta)
        self.update_pos(next_x, next_y)

    def turn(self, theta, degrees=True):
        """
        Turns bot a specified number of degrees. (Positive is CCW)

        Args:
            theta: Degree to turn
            degrees: Whether or not theta is in degrees

        Returns:

        """
        turn_angle = theta
        if degrees:
            turn_angle = np.deg2rad(turn_angle)

        self.set_theta((self.theta + turn_angle) % (2*np.pi), degrees=False)


    def get_map(self):
        """
        Returns: Current map of the robot

        """
        return self.map

    def get_pos(self):
        """
        Returns: x, y coords of bot

        """

        return self.x, self.y

    def update_pos(self, x, y):
        """
        Updates position of the bot.

        Args:
            x, y: Coordinates of new position

        """
        self.x = x
        self.y = y
        self.x_path.append(x)
        self.y_path.append(y)

    def get_theta(self):
        """
        Returns: Orientation theta of the bot

        """
        return self.theta

    def set_theta(self, theta, degrees=True):
        """
        Setter for theta parameter

        Args:
            theta: Angle to set
            degrees: Whether or not angle is in degrees

        """
        if degrees:
            self.theta = np.deg2rad(theta)
        else:
            self.theta = theta

    def get_path(self):
        """
        Returns path traversed by bot as arrays

        Returns:
            Arrays containing traversed x and y positions respectively

        """

        return np.array(self.x_path), np.array(self.y_path)



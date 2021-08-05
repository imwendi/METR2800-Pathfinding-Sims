import numpy as np


class Bot():
    def __init__(self, map, x, y, theta, random=True):
        """
        Spawns a new bot in given x, y, theta (position and orientation),
        unless random is True in which case a randomized position and
        orientation are used.

        Args:
            map: Map to add bot to
            x, y: Coords of spawn point (cm)
            theta: Angle bot faces (degrees)

        """
        self.map = map

        # Set initial position of bot
        if random:
            width, height = map.get_dims()

            self.x = np.random.uniform(-width/2, width/2)
            self.y = np.random.uniform(-height/2, height/2)
            self.theta = np.random.uniform(0, 2*np.pi)
        else:
            self.x = x
            self.y = y
            self.theta = theta

        # Arrays to store traversed points
        self.x_path = []
        self.y_path = []

        # Add bot to map
        map.add_bot(new_bot=self)

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

        self.set_theta(self.theta + turn_angle, degrees=False)

    def sense(self, sensor_theta=0, degrees=True):
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
        if degrees:
            sensor_theta = np.deg2rad(sensor_theta)

        l, _ = self.get_map().get_dims()
        l /= 2.0
        x0, y0 = self.get_pos()
        m = np.arctan(self.get_theta() + sensor_theta)
        intercepts = np.zeros((4, 2))  # x,y values as columns

        print(np.rad2deg(self.theta))

        for i, x in enumerate((-l, l)):
            if np.isclose(self.theta, np.pi/2)\
                    or np.isclose(self.theta, 3*np.pi/2):
                y = self.y
            else:
                y = m*(l-x0) + y0

            intercepts[i, :] = [x, y]

        for i, y in enumerate((-l, l)):
            if np.isclose(self.theta, 0) or np.isclose(self.theta, np.pi):
                x = self.x
            else:
                x = (y-y0)/m + x0

            intercepts[i+2, :] = [x, y]

        for (x, y) in intercepts[:, ...]:
            print(x, y)
            if self.is_facing((x, y)):
                return np.sqrt((x-self.x)**2 + (y-self.y)**2)

        return -1

    def is_facing(self, point):
        """
        Returns whether or not a point is in the bot's current line of sight

        Args:
            point: Tuple of (x, y) coords

        Returns:
            True if the point is in the bot's line of sight, else false

        """
        x, y = point

        if np.isclose(self.x, x)\
            and (np.isclose(self.theta, np.pi/2)
                 or np.isclose(self.theta, 3*np.pi/2)):
            return True

        elif np.isclose(self.y, y) \
                and (np.isclose(self.theta, 0)
                     or np.isclose(self.theta, np.pi)):
            return True

        else:
            m = (y - self.y)/(x - self.x)

            return np.isclose(m, np.arctan(self.get_theta()))

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



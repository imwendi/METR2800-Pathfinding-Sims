import numpy as np

class Bot():
    def __init__(self, x, y, theta):
        """
        Spawns a new bot

        Args:
            x, y: Coords of spawn point (cm)
            theta: Angle bot faces (degrees)

        """
        # Set initial position of bot
        self.x = x
        self.y = y
        self.theta = theta

        # Arrays to store traversed points
        self.x_path = []
        self.y_path = []

        # Map the bot is on
        self.map = None

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

        self.set_angle(self.theta + turn_angle, degrees=False)

    def set_angle(self, theta, degrees=True):
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


    def sense(self, mode='both'):
        """
        Simulates distance sensing proximity to a wall in the direction of
        the robot's orientation.

        Args:
            mode:
            'both' - Computes distance to forwards and backwards walls
            'forward' - Computes distance to forwards wall only

        Returns:
            Distance to wall in cm (Tuple is returned in 'both' mode)

        """

    def is_facing(self, point):
        """
        Returns whether or not a point is in the bot's current line of sight

        Args:
            point: Tuple of (x, y) coords

        Returns:
            True if the point is in the bot's line of sight, else false

        """
        x, y = point
        theta = np.atan((y-self.y)/(x-self.x))

        return np.abs(theta-self.theta) < 0.1

    def set_map(self, current_map):
        """
        Sets the map the bot is on

        Args:
            current_map: Map to set

        """
        self.map = current_map

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

    def get_path(self):
        """
        Returns path traversed by bot as arrays

        Returns:
            Arrays containing traversed x and y positions respectively

        """

        return np.array(self.x_path), np.array(self.y_path)



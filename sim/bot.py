import numpy as np

class Bot():
    def __init__(self, x, y, angle):
        """
        Spawns a new bot

        Args:
            x, y: Coords of spawn point (cm)
            angle: Angle bot faces (degrees)

        """
        # Arrays to store traversed points
        self.x_path = []
        self.y_path = []

        # Set initial position of bot
        self.angle = angle
        self.update_pos(x, y)

    def move(self, distance):
        """
        Moves the bot a specified distance in the direction specified by its
        current angle.

        Args:
            distance: Distance to move

        """

        next_x = self.x + distance*np.cos(np.deg2rad(self.angle))
        next_y = self.y + distance*np.sin(np.deg2rad(self.angle))
        self.update_pos(next_x, next_y)

    def turn(self, degrees):
        """
        Turns bot a specified number of degrees. (Positive is CCW)

        Args:
            degrees: Degree to turn

        Returns:

        """

        self.set_angle(self.angle + degrees)

    def set_angle(self, angle):
        """
        Setter for angle parameter

        Args:
            angle: Angle to set

        """
        self.angle = angle

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





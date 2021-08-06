import numpy as np
from sim import Bot, pol2cart


class BasicBot(Bot):
    def equalize_distance(self):
        """
        Equalizes front and back distances of the robot

        """

        # Measure forwards and backwards distance
        d_for = self.sense()
        self.turn(180)
        d_back = self.sense()

        # Navigate to middle of forwards and backwards distances
        d_center = (d_for + d_back) / 2

        if d_back > d_for:
            self.move(d_center - d_for)

        elif d_for > d_back:
            self.turn(180)
            self.move(d_center - d_back)

    def navigate(self):
        """
        Navigates bot to the center of its map

        """

        self.equalize_distance()
        self.turn(90)
        self.equalize_distance()

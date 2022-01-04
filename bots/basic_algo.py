"""
Basic path-finding by equalizing front and back distances
(in-progress)

"""

import numpy as np
from sim import Bot, pol2cart


class BasicBot(Bot):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        # Max possible coordinate value, equal to half of width of map
        self.l_max = map.get_dims()[0]/2.0

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
            self.turn(180)
        else:
            self.turn(180)
            self.move(d_center - d_back)

    def navigate(self):
        """
        Navigates bot to the center of its map

        """

        d_prev = np.abs(self.l_max - self.sense())

        noise = 1 + (-1)**(np.random.randint(0, 1)) * np.random.random()
        self.turn(90)
        self.equalize_distance()
        count = 1
        while(count <= 3):
            count += 1
            d_new = np.abs(self.l_max - self.sense())

            if np.sqrt(d_prev**2 + d_new**2) < 15:
                break
            else:
                d_prev = d_new
                self.turn(90)
                self.equalize_distance()

    def navigate2(self, threshold):
        """
        Navigates bot to the center of its map

        """

        d_prev = np.abs(self.l_max - self.sense())

        self.turn(90)
        self.equalize_distance()
        count = 1
        while(count <= 3):
            count += 1
            d_new = np.abs(self.l_max - self.sense())

            if d_prev < threshold and d_new < threshold:
                break
            else:
                d_prev = d_new
                self.turn(90)
                self.equalize_distance()

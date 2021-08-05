import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .bot import Bot

class Map():
    """
    Represents the test environment
    """
    def __init__(self, width=100, height=100):
        """
        Initializes a new map

        Args:
            width: Width of map
            height: Height of map
        """
        self.width = width
        self.height = height
        self.bots = []

        # Configure figure
        self.fig, self.ax = plt.subplots()
        bound_scale = 1.3
        self.ax.set_xlim(-width/2*bound_scale, width/2*bound_scale)
        self.ax.set_ylim(-height/2*bound_scale, height/2*bound_scale)
        self.ax.set_aspect('equal')

        # Area boundary
        boundary = patches.Rectangle((-width/2, -height/2),
                                     width,
                                     height,
                                     color=(240/255,)*3)

        # Target circles
        outer = patches.Circle((0, 0),
                               radius=25,
                               color=[i/255 for i in (255, 205, 210)])
        middle = patches.Circle((0, 0),
                               radius=20,
                               color=[i / 255 for i in (255, 224, 178)])
        inner = patches.Circle((0, 0),
                                radius=15,
                                color=[i / 255 for i in (220, 237, 200)])

        # Added shapes
        for patch in [boundary, outer, middle, inner]:
            self.ax.add_patch(patch)

    def add_bot(self, new_bot):
        """
        Adds a new bot to the map

        Args:
            new_bot: Bot to add
        """

        self.bots.append(new_bot)

    def get_paths(self):
        """
        Returns: array of all paths taken by all bots in the Map.
        Shape should be (examples, x-coords, y-coords)

        """

    def get_bots(self):
        """
        Returns: list of all bots in the map

        """

        return self.bots

    def plot_path(self, bot):
        """
        Plots the path of a bot onto self.fig

        Args:
            bot: bot whose path is to be plotted

        """
        x_path, y_path = bot.get_path()
        self.ax.plot(x_path, y_path)


    def plot_all_paths(self):
        """
        Same as plot_path but for all bots in the map

        """

    def get_fig(self):
        """
        Returns the fig and ax of the map with plotted paths.

        Returns:
            fig, ax of map plot.

        """

        return self.fig, self.ax

    def get_dims(self):
        """
        Returns: Width and height of map

        """
        return self.width, self.height
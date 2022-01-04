import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .bot import Bot

class Map():
    """
    Represents the test environment
    """
    def __init__(self, width=100, height=100, fig=None, ax=None):
        """
        Initializes a new map

        Args:
            width: Width of map
            height: Height of map
            fig, ax: Option to provide fig and axe to plot on, else new ones
                     are created.
        """
        self.width = width
        self.height = height
        self.bots = []

        # Configure figure
        if fig is None or ax is None:
            self.fig, self.ax = plt.subplots()
        else:
            self.fig = fig
            self.ax = ax


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
        # x, y = new_bot.get_pos()
        # self.ax.plot(x,
        #              y,
        #              #marker=(3, 0, np.rad2deg(new_bot.get_theta())-90),
        #              marker='s',
        #              markersize=8,
        #              color=[i/255 for i in (179, 157, 219)],
        #              zorder=888)

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
        self.ax.plot(x_path,
                     y_path,
                     linewidth=0.88)

    def plot_all_paths(self):
        """
        Same as plot_path but for all bots in the map

        """

    def plot_pos(self, bot, markersize=5):
        """
        Plots the end position of a bot onto self.fig

        Args:
            bot: bot whose position is to be plotted
            markersize: Pyplot plot option

        """
        x, y = bot.get_pos()
        self.ax.plot(x, y, marker='.', markersize=markersize, zorder=888)

    def plot_all_pos(self):
        """
        Same as plot_pos but for all bots in the map

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

    def evaluate(self):
        """
        Computes the percentage of bots that are in the center of the map

        """
        successful_bot_no = 0

        for bot in self.bots:
            x, y = bot.get_pos()
            if np.sqrt(x**2 + y**2) < 15:
                successful_bot_no += 1

        return successful_bot_no/len(self.bots)

    def displacement(self, bot):
        """
        Computes the displacement from the center of a bot

        Args:
            bot: Bot to compute displacement for

        Returns:
            Displacement

        """
        x, y = bot.get_pos()

        return np.sqrt(x**2 + y**2)

    def mean_displacement(self):
        """
        Computes the average displacement from the center of bots that are in
        the map

        """
        total_disp = 0

        for bot in self.bots:
            total_disp += self.displacement(bot)

        return total_disp/len(self.bots)

    def travel_distance(self, bot):
        """
        Computes travel distance of a bot

        Args:
            bot: Bot to compute travel distance for

        Returns:
            Travel distance
        """
        x_path, y_path = bot.get_path()
        delta_x = x_path[1:] - x_path[:-1]
        delta_y = y_path[1:] - y_path[:-1]

        return np.sum(np.sqrt(delta_x**2 + delta_y**2))

    def mean_travel_distance(self):
        """
        Computes the mean travel distance of each bot that is in the inner
        circle of the map

        Returns:
            Mean travel distance

        """
        # successful_bots = []
        # for bot in self.bots:
        #     x, y = bot.get_pos()
        #     if np.sqrt(x**2+y**2) < 15:
        #         successful_bots.append(bot)

        return sum([self.travel_distance(bot) for bot in self.bots])\
               /len(self.bots)








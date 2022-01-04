import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sim import Map, Bot
from bots import BasicBot
import tqdm

mpl.rcParams['figure.dpi'] = 300
plt.rc('font', size=14)

fig, axes = plt.subplots(1, 3, figsize=(10, 5))

for i, ax in enumerate(axes):
    map = Map(fig=fig, ax=ax)

    for j in tqdm.tqdm(range(1000)):
        bot = BasicBot(map)
        for k in range(i+1):
            bot.equalize_distance()
            bot.turn(90)
        map.plot_pos(bot, markersize=2)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([-52, 52])
    ax.set_ylim([-52, 52])
    acc = map.evaluate()
    acc = np.round(acc*100, 3)
    mean_disp = np.round(map.mean_displacement(), 3)

    ax.set_title(f'Iterations: {i+1}')

    print(f'acc:{map.evaluate()}, disp:{map.mean_displacement()},'
          f'dist:{map.mean_travel_distance()}')

fig.show()
fig.savefig('distributions.png', dpi=300)


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from sim import Map, setup_tex
from bots import AxesSearch2
import tqdm

mpl.rcParams['figure.dpi'] = 300

points = np.arange(12, 604, 16)
acc = np.zeros(shape=points.shape)

fig1, ax1 = plt.subplots(figsize=(10, 8))

for i, num in enumerate(points):
    map = Map(fig=fig1, ax=ax1)

    for j in tqdm.tqdm(range(1000)):
        bot = AxesSearch2(map)
        bot.navigate(num_points=num)

    acc[i] = map.evaluate()

setup_tex()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(points, acc*100)
ax.set_title('Axes Search Algorithm Accuracy')
ax.set_xlabel('Number of Sampled Points')
ax.set_ylabel('% Accuracy')

data = np.stack([points, acc])
np.save('data304', data)

plt.show()
fig.savefig('algo2acc.png', dpi=300)



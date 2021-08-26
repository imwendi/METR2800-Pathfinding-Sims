#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib as mpl
from sim import Map, Bot

mpl.rcParams['figure.dpi'] = 300

fig, ax = plt.subplots(figsize=(5, 5))
map = Map(fig=fig, ax=ax)
bot = Bot(map, x=-30, y=-35, random=False)
x, y = bot.get_pos()
ax.plot(x, y, 'k.', markersize=15, zorder=888)

x_vals = [(-15, -50), (50, -50), (50, -45), (-30, -30)]
y_vals = [(-50, -15), (-35, -35), (45, -50), (50, -50)]

for i in range(len(x_vals)):
    ax.plot(x_vals[i], y_vals[i], '-.')

ax.text(-17, -45, '1', fontsize=15, fontfamily='serif')
ax.text(45, -33, '2', fontsize=15, fontfamily='serif')
ax.text(30, 32, '3', fontsize=15, fontfamily='serif')
ax.text(-36, 32, '4', fontsize=15, fontfamily='serif')

ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-52, 52])
ax.set_ylim([-52, 52])

fig.show()
fig.savefig('algo2demo.png', dpi=150)

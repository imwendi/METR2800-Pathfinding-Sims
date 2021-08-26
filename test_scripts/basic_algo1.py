from sim import Map, Bot
from bots import BasicBot
import tqdm

map = Map()

for i in tqdm.tqdm(range(1000)):
    bot = BasicBot(map, min_rad=25)
    bot.navigate2(threshold=15)
    # map.plot_path(bot)
    map.plot_pos(bot)

print(f'acc:{map.evaluate()}, disp:{map.mean_displacement()},'
        f'dist:{map.mean_travel_distance()}')

print(map.evaluate())
fig, ax = map.get_fig()
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-52, 52])
ax.set_ylim([-52, 52])
fig.show()
fig.savefig('test.png', dpi=150)

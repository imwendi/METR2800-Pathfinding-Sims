import tqdm
from sim import Map
from bots import AxesSearch2

map = Map()

# for i in tqdm.tqdm(range(1)):
#     bot = AxesSearch2(map, x=-20, y=20, theta=0, random=False)
#     bot.navigate(num_points=100)
#     map.plot_pos(bot)
#     map.plot_path(bot)

for i in tqdm.tqdm(range(10)):
    bot = AxesSearch2(map)
    map.plot_pos(bot)
    bot.navigate(num_points=500)
    map.plot_pos(bot)
    map.plot_path(bot)

print(f'acc:{map.evaluate()}, disp:{map.mean_displacement()},'
        f'dist:{map.mean_travel_distance()}')

print(map.evaluate())
fig, ax = map.get_fig()
fig.show()

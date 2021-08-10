from sim import Map
from bots import AxesSearch

map = Map()

for i in range(10000):
    bot = AxesSearch(map)

    for j in range(2 ):
        bot.navigate(num_points=50)
    #map.plot_path(bot)
    map.plot_pos(bot)

print(map.evaluate())
fig, ax = map.get_fig()
fig.show()

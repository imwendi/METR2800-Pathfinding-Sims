from sim import Map, Bot
from bots import BasicBot

map = Map()

for i in range(1000):
    bot = BasicBot(map)

    for j in range(2 ):
        bot.navigate()
    map.plot_pos(bot)

fig, ax = map.get_fig()
fig.show()

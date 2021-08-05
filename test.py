import numpy as np
from sim import Bot, Map

map = Map()

bot = Bot(map, 20, 20, 0, random=False)
map.add_bot(bot)

bot.turn(120)
bot.move(30)
bot.turn(100)
bot.move(20)
bot.turn(30)
bot.move(10)
bot.turn(50)
bot.move(30)

map.plot_path(bot)
fig, ax = map.get_fig()
fig.show()
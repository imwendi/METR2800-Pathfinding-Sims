from sim import Map, Bot
import numpy as np

map = Map()

# bot = Bot(map, 0, 0, 320, random=False)
# bot.sense()


bot = Bot(map, 0, 0, 0, random=False)
for i in range(37):
    print(f'{np.degrees(bot.get_theta())}: ', bot.sense())
    bot.turn(10)


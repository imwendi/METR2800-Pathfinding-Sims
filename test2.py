from sim import Bot, Map

map = Map()
map.spawn_bot(20, 20, 0, random=False)
bot, = map.get_bots()
print(bot.sense())
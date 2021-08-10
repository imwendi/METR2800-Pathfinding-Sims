from sim import Bot, Map
import matplotlib.pyplot as plt

test_area = Map()
bot = Bot(test_area, 20, 20, 0, random=False)
test_area.add_bot(bot)

bot.turn(120)
bot.move(30)
bot.turn(100)
bot.move(20)
bot.turn(30)
bot.move(10)
bot.turn(50)
bot.move(30)

test_area.plot_path(bot)
fig, ax = test_area.get_fig()
ax.set_xticks([-50, 50])
ax.set_yticks([-50, 50])
ax.set_xlim([-52, 52])
ax.set_ylim([-52, 52])
fig.savefig('test.png', dpi=150)
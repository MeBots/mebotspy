import gmbots
import os

GROUP_ID = 49940116

# "bot" name can be whatever is most convenient for your program
bot = gmbots.Bot("test", os.environ["BOT_TOKEN"])
print(bot.instance(GROUP_ID).id)

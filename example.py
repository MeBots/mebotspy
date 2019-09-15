import gmbots
import os

GROUP_ID = 49940116

# "bot" name can be whatever is most convenient for your program
bot = gmbots.Bot("test", os.environ["BOT_TOKEN"])

# Given a group's ID, get the ID of the bot instance in that group
print(bot.instance(GROUP_ID).id)

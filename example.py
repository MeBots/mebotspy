import gmbots
import os

# "bot" name can be whatever is most convenient for your program
bot = gmbots.Bot("test", os.environ["BOT_TOKEN"])
print(bot.get_instance(group_id=49940116))

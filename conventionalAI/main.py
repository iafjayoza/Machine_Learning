import json
from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

# print('Bot> Hi!')
#
# while True:
#     msg = input('You> ').lower()
#     if msg in ('exit','quit','bye'):
#         break
#     reply = bot.reply("localuser",msg)
#     print('Bot>', reply)

def getReply(msg):
    if msg in ('exit', 'quit', 'bye'):
        return 'ok bye'
    return bot.reply("localuser",msg)

# print(getReply("Please search a flight from bangalore to delhi on 12th july"));
# print(getReply("from bangalore to chennai, please suggest some flights on 12th july"));
# print(getReply("Show me some flights from mumbai to trivandrum on 12th july"));
# print(getReply("I want to search flights from chennai to delhi on 12th july"));
# print(getReply("search for a flight from bangalore to chennai on 45"));
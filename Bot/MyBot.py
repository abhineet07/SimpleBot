import discord
from SearchGoogle import *
from SearchHistory import *

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.searchObj = Google()
        self.historyObj = History()

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        print(type(message.content), message.content)
        if message.author.id == self.user.id:
            return

        if message.content.startswith('hi'):
            await message.channel.send('hey')

        if message.content.startswith('!google'):
            query = str(message.content).split(" ")[1:]
            query = ' '.join(token for token in query)
            # print(type(query), query)
            results = self.searchObj.search(query)

            # maintaining history in text file
            with open("history.txt", "a") as history:
                history.write(query + "\n")

            await message.channel.send(results)

        if message.content.startswith('!recent'):
            query = str(message.content).split(" ")[1:]
            query = ' '.join(token for token in query)
            results = self.historyObj.getRecentTen(query)
            await message.channel.send(results)


client = MyClient()
client.run('NjQ3MTI4NTkxMDE2MDAxNTM3.XdbOhg.KnAnIU0D1T41JBHwPjtLsVm-gvM')
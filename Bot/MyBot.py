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
		
		# replying 'hey' to 'hi'
        if message.content.startswith('hi'):
            await message.channel.send('hey')

		# replying google searches
        if message.content.startswith('!google'):
			# splitting the text after '!google'
            query = str(message.content).split(" ")[1:]
            query = ' '.join(token for token in query)
            # print(type(query), query)
            results = self.searchObj.search(query)

            # maintaining history in text file
            with open("history.txt", "a") as history:
                history.write(query + "\n")

            await message.channel.send(results)
		
		# replying the recent searches
        if message.content.startswith('!recent'):
            query = str(message.content).split(" ")[1:]
            query = ' '.join(token for token in query)
            results = self.historyObj.getRecentTen(query)
            await message.channel.send(results)


client = MyClient()
# Insert the chatbot app's token in the run method
client.run('<Token>')
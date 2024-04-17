import discord
import os
from dotenv import load_dotenv
from send_text import send_message
from extra import is_exp_product

load_dotenv()

bot_token = os.getenv('discordBotToken')
channel_id = int(os.getenv('refundChannelId'))

gatewayAddress = "5166332118@vtext.com"
lower_bound = 250

#interests
intents = discord.Intents.default() 
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):

    if message.author == client.user or message.channel.id != channel_id:
        return
    
    # Delete Message if not David and Zeela
    if message.author.name != "davfong" and message.author.name != "zeela.":
        try:
            await message.delete()
        except discord.Forbidden:
            print("Do not have permission to delete messages in this channel.")
        except discord.HTTPException:
            print("Failed to delete message.")

        return
    
    
    product_price, product = is_exp_product(message.content, lower_bound)
    
    if product_price != -1:

        text_message = f"Product Price: {product_price}\n\n" + product
        send_message(gatewayAddress, text_message)

client.run(bot_token)

from discord.ext import commands
import discord
import asyncio
import io
import aiohttp


client = commands.Bot(command_prefix='#')

@client.command()
async def nft(ctx):
    while 3>2:


        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):

            approved_msg1 = (msg.content)
            x = approved_msg1.translate({ord(i): None for i in '!'})
            if x.isdecimal():
                y = int(x)
                return msg.content.startswith('!') and len(msg.content) == 6 and y < 20001

        msg = await client.wait_for("message", check=check)

        if msg:

            approved_msg = (msg.content)
            token = approved_msg.replace("!", "")
            print("token:", token)
            token_png = (str(token) + ".png")

            nft_image2 = ("https://storage.googleapis.com/6fec357fd03a49559b39557a2552f775/icons/" + str(token) + ".png")
            print("nft_image2: ", nft_image2)

            async with aiohttp.ClientSession() as session:
                async with session.get(nft_image2) as resp:
                    if resp.status != 200:
                        return await ctx.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    print("data: ", data)
                    await ctx.send(file=discord.File(data,token_png))
                    
client.run("")

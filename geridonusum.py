import discord


intents= discord.Intents.default()
intents.message_content = True


# Discord bot token
TOKEN = "buraya tokeni yaz."


bot = discord.Client(intents=intents)

ayristima_sureleri={
    "plastik":"450 yıl",
    "kağıt":"2-4 hafta",
    "metal":"200 yıl",
    "cam":"1 milyon yıl",
    "organik":"2-6 ay",
    "elektronik":"1-3 yıl",
    "tek kullanımlık ürünler":"10-20 yıl",
    "lastik":"50-80 yıl",
    "piller":"100 yıl",
    "tek kullanımlık şişeler":"450 yıl",
    "tek kullanımlık poşetler":"10-20 yıl",
    "tek kullanımlık tabaklar":"10-20 yıl",
}




@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptık!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    esya= message.content.lower()#kullanıcı küük harflerle yazarsa
    if esya in ayristima_sureleri:
        sure = ayristima_sureleri[esya]
        await message.channel.send(f"{esya.capitalize()} atıklarının doğada ayrışma süresi: {sure}.")
    else:
        await message.channel.send("Bu atık türü hakkında bilgi bulunmamaktadır. Lütfen başka bir atık türü girin.")


   

bot.run(TOKEN)

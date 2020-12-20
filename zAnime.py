import discord
from discord.ext import commands
import random
import time
import os

client = commands.Bot(command_prefix = 'a!')
client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity= discord.Activity(
        type= discord.ActivityType.playing, name= 
        "zAnime! here the prefix is a!, check a!help to see my useless commands" 
    ))
    print("Bot is ready.")

@client.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = 'a!help', description = 'use a!help (command name) for more info on them')
    embed.add_field(name='non-admin commands', value='a!zoro\na!hisoka\na!kakashi\na!senku\na!speed_check', inline=False)
    embed.add_field(name="user-info-commands", value='a!whois', inline=False)
    embed.add_field(name='admin commads', value='a!ban\na!kick\na!unban\na!clear\na!mute\na!unmute\na!create', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/777070524588359741/789491406233141308/IMG_20201218_194627.png')
    await ctx.send(embed=embed)
@help.command()
async def zoro(ctx):
    embed = discord.Embed(title = 'ZORO', description = "\nuse a!zoro for Roronoa Zoro GIFs")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/788829955621650472/789071533515341824/one-piece-zoro-1190171-1280x0.jpeg")
    await ctx.send(embed=embed)
@help.command()
async def hisoka(ctx):
    embed = discord.Embed(title = 'HISOKA', description = "\nuse a!hisoka for Hisoka Morow's GIFs")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/788829955621650472/789071579623325716/hisoka-1200x900.jpg")
    await ctx.send(embed=embed)
@help.command()
async def ban(ctx):
    embed = discord.Embed(title = 'BAN', description = 'use a!ban @<user_name> <reason> to ban user')
    await ctx.send(embed=embed)
@help.command()
async def unban(ctx):
    embed = discord.Embed(title = 'UNBAN', description = 'use a!unban <user tag> to unban user')
    await ctx.send(embed=embed)
@help.command()
async def kick(ctx):
    embed = discord.Embed(title = 'KICK', description = 'use a!kick @<user name> <reason> to kick user')
    await ctx.send(embed=embed)
@help.command()
async def speed_check(ctx):
    embed = discord.Embed(title = 'speed_check', description = "use a!speed_check to check for host's latency")
    await ctx.send(embed=embed)
@help.command()
async def kakashi(ctx):
    embed = discord.Embed(title='KAKASHI',description = "use a!kakashi for Kakashi's Gifs")
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/777070525436002354/789091864947064862/-yqpL-1S_400x400.png')
    await ctx.send(embed=embed)
@help.command()
async def whois(ctx):
    embed = discord.Embed(title = 'WHOIS', description = 'use a!whois <username> to check their INFOs')
    await ctx.send(embed=embed)
@help.command()
async def clear(ctx):
    embed = discord.Embed(title='CLEAR', description = 'use a!clear <the amount you want to clear>')
    await ctx.send(embed=embed)
@help.command()
async def mute(ctx):
    embed = discord.Embed(title='MUTE', description = 'use a!mute <user name> to mute the user')
    await ctx.send(embed=embed)
@help.command()
async def unmute(ctx):
    embed = discord.Embed(titile='UNMUTE', description = 'use a!unmute <username> to unmute user')
    await ctx.send(embed=embed)
@help.command()
async def senku(ctx):
    embed = discord.Embed(title='SENKU', description='use a!senku for GIFs of Ishigami Senku')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/777070524588359741/789413837715275776/9k.png')
    await ctx.send(embed=embed)
@help.command()
async def create(ctx):
    embed = discord.Embed(title='CREATE', description='use a!create <the word> and should come 10 times')
    await ctx.send(embed=embed)
#@client.event
#async def on_ready():
#    await client.change_presence(status = discord.Status.online, activity= discord.Activity(
#        type= discord.ActivityType.playing, name= 
#        "zAnime! here the prefix is a!, check a!help to see my useless commands" 
#    ))
#    print("Bot is ready.")
@client.command()
async def whois(ctx,member : discord.Member):
    embed = discord.Embed(title = member.name, description = f'@{member.name}')
    embed.add_field(name = "ID", value = member.id)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text=f"requested by @{ctx.author.name}")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(789163084735316079)
    baby_mod = ctx.guild.get_role(787705710615461938)
    baby_baby_mod = ctx.guild.get_role(789477457484840981)
    bot = ctx.guild.get_role(777070475435704330)

    if (muted_role in member.roles):
        await ctx.send(f'{ctx.author.mention} member already muted')
    elif (baby_mod in member.roles):
        await ctx.send(f'{ctx.author.mention} you can not mute a mod')
    elif (baby_baby_mod in member.roles):
        await ctx.send(f'{ctx.author.mention} you can not mute a mod')
    elif (bot in member.roles):
        await ctx.send(f'remove `bot` role from {member.mention} to mute the account')
    else:
        await member.add_roles(muted_role)

        await ctx.send(f'{member.mention} was muted by {ctx.author.mention}')

@client.command()
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(789163084735316079)

    if (muted_role not in member.roles):
        await ctx.send(f'{ctx.author.mention} user is already unmuted')
    else:
        await member.remove_roles(muted_role)

        await ctx.send(f'{member.mention} was unmuted by {ctx.author.mention}')

@client.command(aliases = ['S'])
async def senku(ctx):
    await ctx.send('Here Ishigami Senku -_-')
    senku_gif = ['https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-pabloc-gif-19477723','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477888','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477891','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477891','https://tenor.com/view/franco-ddlj-franco-luizdoro-dr-stone-senku-gif-19064538','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477479','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477884','https://tenor.com/view/starstrails-shatito-shatito-producciones-pae-nachobkn-gif-19477478','https://tenor.com/view/dr-stone-senku-angry-gif-14601021','https://tenor.com/view/senku-ishigami-chrome-magma-cringy-dr-stone-gif-15698675','https://tenor.com/view/dr-stone-chibi-senku-ishigami-anime-boy-shooting-star-gif-15800596','https://tenor.com/view/franco-franco-ddlj-luizdoro-senku-ishigami-senku-gif-19022652','https://tenor.com/view/senku-dr-stone-senku-ishigami-luizdoro-gif-19022306','https://tenor.com/view/senku-dr-stone-senku-ishigami-franco-franco-ddlj-gif-19022681','https://tenor.com/view/senku-dr-stone-senku-ishigami-luizdoro-gif-19022313','https://tenor.com/view/dr-stone-senku-anime-hot-stare-gif-19437590','https://tenor.com/view/dr-stone-rainbow-barf-hold-magma-chrome-gif-15698655','https://tenor.com/view/dr-stone-senku-anime-smirk-smile-gif-19437591','https://tenor.com/view/senku-dr-stone-electricity-power-shock-lightning-gif-15566774','https://tenor.com/view/anime-dr-stone-senku-science-math-gif-14797363','https://tenor.com/view/senku-dr-stone-anime-smile-gif-16993458']
    await ctx.send('Enjoy!!!')
    await ctx.send(random.choice(senku_gif))
@client.command(aliases = ['H'])
async def hisoka(ctx):
    await ctx.send('Here Hisoka Morow -_-')
    hisoka_gif = ['https://tenor.com/view/hisoka-hxh-hunter-x-hunter-anime-hair-down-gif-17560875','https://tenor.com/view/hisoka-ok-gif-13721467','https://tenor.com/view/hisoka-hunter-x-hunter-hxh-anime-aura-gif-17602951','https://tenor.com/view/hxh-hisoka-hunter-x-hunter-anime-joker-gif-16816643','https://tenor.com/view/hisoka-hunter-x-hunter-stare-gif-8680716','https://tenor.com/view/hisoka-hunter-x-hunter-gif-13721470','https://tenor.com/view/kurocass-gif-9350671','https://tenor.com/view/hisoka-gif-14143763','https://tenor.com/view/hisoka-happy-hisoka-vs-gon-hxh-hunter-x-hunter-gif-16556305','https://tenor.com/view/hisoka-gon-hunterxhunter-gif-6164327','https://tenor.com/view/hisoka-hisoka-morow-hisoka-hxh-hxh-hunter-x-hunter-gif-16052660','https://tenor.com/view/loveyou-love-you-hisoka-heart-gif-5511432','https://tenor.com/view/hisoka-hunter-smug-hxh-gif-4749197','https://tenor.com/view/hisoka-hxh-hunterxhunter-gif-5292003','https://tenor.com/view/hisoka-gif-12748963','https://tenor.com/view/hisoka-hisoka-nen-hisoka-fight-hisoka-greed-island-greed-island-gif-16556405','https://tenor.com/view/hisoka-hunterx-hunter-anime-turn-around-nude-gif-17740689','https://tenor.com/view/anime-hisoka-hunterxhunter-hxh-good-gif-13170154','https://tenor.com/view/hisoka-card-hisoka-hxh-hunter-x-hunter-gif-16052944','https://tenor.com/view/hisoka-hunter-x-hunter-gif-13721472','https://tenor.com/view/hisoka-hunter-x-hunter-gif-13721471','https://tenor.com/view/naked-hisoka-morow-anime-gif-18781477','https://tenor.com/view/im-pretty-shy-quiet-party-gif-5511433','https://tenor.com/view/hisoka-pose-smile-gif-12762415','https://tenor.com/view/straight-face-hunter-x-hunter-gif-13851978','https://tenor.com/view/hisoka-hisoka-morrow-gif-19188120','https://tenor.com/view/hisoka-hunter-x-hunter-stare-gif-8680716','https://tenor.com/view/hisoka-gif-18482106','https://tenor.com/view/hisoka-gif-18482106','https://tenor.com/view/hisoka-hisoka-vs-gon-hisoka-renatoxd-hisoka-hxh-hunter-x-hunter-gif-16052647','https://tenor.com/view/hisoka-hunter-x-hunter-hxh-anime-power-gif-17610829','https://tenor.com/view/hisoka-gif-18677673','https://tenor.com/view/hisoka-hunter-x-hunter-hxh-anime-power-gif-17602949','https://tenor.com/view/morrow-hisoka-hunter-x-hunter-hxh-anime-gif-15981482','https://tenor.com/view/hisoka-hxh-anime-hunterxhunter-gif-5291995','https://tenor.com/view/hunter-x-hunter-hisoka-anime-sourcile-evil-gif-17167208','https://tenor.com/view/hisoka-hxh-hunter-x-hunter-smile-smirk-gif-17610823','https://tenor.com/view/hisoka-hunter-x-hunter-gif-15773404','https://tenor.com/view/that-is-my-target-hunter-x-hunter-hisoka-hisoka1999-gif-15313850','https://tenor.com/view/hisoka-hunter-x-hunter-gif-13721469','https://tenor.com/view/hisoka-dancing-hxh-hunterxhunter-anime-gif-5755399'] 
    await ctx.send('Enjoy!!!')
    await ctx.send(random.choice(hisoka_gif))

@client.command(aliases = ['K'])
async def kakashi(ctx):
    await ctx.send('Here Kakashi -_-')
    kakashi_gif = ['https://tenor.com/view/kakashi-gif-5228544','https://tenor.com/view/thumbsup-approve-kakashi-naruto-gif-8212733','https://tenor.com/view/naruto-hi-hello-kakashi-wave-gif-4890052','https://tenor.com/view/kakashi-naruto-gif-4978618','https://tenor.com/view/kakashi-hatake-lol-gif-13599150','https://tenor.com/view/kakashi-hatake-naruto-smile-mask-anime-gif-17707743','https://tenor.com/view/idk-kakashi-naruto-kids-gif-14039609','https://tenor.com/view/naruto-gif-7918603','https://tenor.com/view/kakashi-kakashi-hatake-chidori-lightening-lightening-blade-gif-5373413','https://tenor.com/view/kakashi-hatake-gif-11594732', 'https://tenor.com/view/kakashi-hatake-face-palm-naruto-gif-11602503','https://tenor.com/view/naruto-thumbs-up-approve-approval-yup-gif-7943827','https://tenor.com/view/kakakshi-kakashi-hatake-kakashia-shokage-spinning-in-chair-shikamaru-gif-5373420','https://tenor.com/view/kakashi-naruto-smile-kawaii-anime-gif-4887912','https://tenor.com/view/kakashi-hatake-jutsu-gif-13599266','https://tenor.com/view/kakashi-kakashieating-kakashihatake-naruto-narutoshippuden-gif-5373406','https://tenor.com/view/kakashi-hatake-kid-naruto-gif-5075026','https://tenor.com/view/kakashi-naruto-gif-7249547','https://tenor.com/view/naruto-kakashi-scary-gif-14510702','https://tenor.com/view/kakashi-mangekyou-obito-mangekyou-kakashi-obito-gif-14848309','https://tenor.com/view/kakashi-hatake-gif-11594768','https://tenor.com/view/naruto-kakashi-sneak-observe-look-gif-4887793','https://tenor.com/view/surya-surya-kp-kakashi-sharingan-surya-kakashi-gif-18225507','https://tenor.com/view/kakashi-hatake-funnny-moment-gif-14559744','https://tenor.com/view/naruto-kakashi-shrug-gif-12980424','https://tenor.com/view/kakashi-hatake-deep-sigh-gif-15336876','https://tenor.com/view/hatake-kakashi-kakashi-hatake-naruto-padre-ehijo-gif-18598504',]
    await ctx.send('Enjoy!!!')
    await ctx.send(random.choice(kakashi_gif))




@client.command(aliases = ['Z'])
async def zoro(ctx):
    await ctx.send('Here Roronoa Zoro -_-')
    zoro_gif = ['https://tenor.com/view/zoro-one-piece-sword-epic-gif-17912030','https://tenor.com/view/one-piece-anime-zoro-laughing-lol-gif-16674515','https://tenor.com/view/zoro-ultimate-gif-18029429','https://tenor.com/view/zoro-fakesmile-gif-18464823','https://tenor.com/view/roronoa-zoro-one-piece-gif-12702248','https://tenor.com/view/lick-sword-zoro-one-piece-kill-gif-4773569','https://tenor.com/view/zoro-one-piece-snore-snoring-bubble-gif-5392221','https://tenor.com/view/luffy-one-piece-anime-dead-evil-gif-5378937','https://tenor.com/view/zoro-roronoa-zoro-laugh-one-piece-zoro-one-piece-gif-11990845','https://tenor.com/view/zoro-haki-one-piece-gif-14591756','https://tenor.com/view/sanji-one-piece-gif-16224246','https://tenor.com/view/one-piece-roronoa-zoro-onsen-hotspring-chill-gif-8968823','https://tenor.com/view/zoro-sleep-sleepy-one-piece-anime-gif-15159533','https://tenor.com/view/zoro-rononora-zoro-one-piece-practice-gif-14578557','https://tenor.com/view/zoro-sword-trick-one-piece-anime-gif-17235716','https://tenor.com/view/zoro-rononora-zoro-one-piece-practice-weightlifting-gif-14578573','https://tenor.com/view/one-piece-zoro-anime-sword-gif-16324555','https://tenor.com/view/zoro-one-piece-straw-hat-one-piece-gif-5376790','https://tenor.com/view/zoro-dragon-twister-one-piece-gif-14591763','https://tenor.com/view/zoro-sword-one-piece-gif-15934323','https://tenor.com/view/zoro-one-piece-straw-hat-one-piece-gif-5376790','','https://tenor.com/view/zoro-sword-one-piece-gif-15934323','https://tenor.com/view/one-piece-zoro-anime-sword-gif-16324555','https://tenor.com/view/luffy-zoro-one-piece-one-piece-gif-5376810','https://tenor.com/view/zoro-one-piece-straw-hat-one-piece-gif-5376793','https://tenor.com/view/one-piece-anime-drinking-force-luffy-gif-16581128','https://tenor.com/view/one-piece-wano-ep934-zoro-three-sword-style-gif-17911583','https://tenor.com/view/zoro-drink-zoro-drink-gif-18448771','https://tenor.com/view/luffy-zoro-friends-friend-one-piece-gif-17241566','https://tenor.com/view/zoro-battle-attack-gif-13850289','https://tenor.com/view/one-piece-sleepy-yawn-zoro-gif-9627780','https://tenor.com/view/anime-one-piece-roronoa-zoro-rage-angry-gif-12305224','https://tenor.com/view/tashigi-zoro-roronoa-zoro-zotash-blush-gif-16270260','https://tenor.com/view/zoro-gif-18444309','https://tenor.com/view/zoro-one-piece-gif-9932573','https://tenor.com/view/zoro-one-piece-gif-8451924','https://tenor.com/view/one-piece-gif-4871398','https://tenor.com/view/zoro-one-piece-wink-smile-anime-gif-17606766']
    await ctx.send('Enjoy!!!')
    await ctx.send(random.choice(zoro_gif))


@client.command()
async def speed_check(ctx):
    await ctx.send(f'The speed is {round(client.latency * 1000)} miliseconds!!')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    if amount == amount:
        await ctx.send(f'cleared {amount} msg/msgs')
        time.sleep(3)
        await ctx.channel.purge(limit=1)

@client.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason):
    await member.kick(reason=reason)  
    await ctx.send(f"kicked {member.mention} by {ctx.author.name} because: {reason}")



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason):
    await member.ban(reason=reason)     
    await ctx.send(f"banned {member.mention} by {ctx.author.name} because: {reason}")



@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user


        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")

@client.command()
@commands.has_permissions(kick_members=True)
async def first_bot(ctx):
    time.sleep(3)
    await ctx.send('||how did you know about it???||')
    time.sleep(3)
    await ctx.send('||i do not have the function to check if anyone said anything or not\nbut let me tell you this\nInspirational bot was the first bot my creator made\nthe bot that gave me birth\ndig for more secrets you have proven your self worth by using this command.||')
    time.sleep(5)
    await ctx.channel.purge(limit=3)
    return

@client.command()
@commands.has_permissions(manage_messages=True)
async def create(ctx,*,amount: str):
    if time.sleep(0):
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)
        await ctx.send(amount)


client.run(os.environ['token'])
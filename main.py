 # -*- coding: utf-8 -*-
import discord
from discord.ext import commands, tasks
import json




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open('users.json', 'r') as f:
	users = json.load(f)
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = ['!', '?', '-', '$', '/', ','], intents=intents)
bot.remove_command('help')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
async def add_experience(users, user):
	if not f'{user.id}' in users:
		users[f'{user.id}'] = {}
		users[f'{user.id}']['experience'] = 0
		users[f'{user.id}']['level'] = 0
	users[f'{user.id}']['experience'] += 4
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
async def level_up(users, user, message):
	experience = users[f'{user.id}']["experience"]
	lvl_start = users[f'{user.id}']["level"]
	lvl_end = int(experience ** (1 / 3.25))
	if lvl_start < lvl_end:
		embed = discord.Embed(title = f'Lvl {int(experience ** (1/3.25))} ({experience}/{int((lvl_end+1)**(1*3.25))} exp | {int((float(experience ** (1/3.25))-int(experience ** (1/3.25))) * 100)}%)', description = f"{getloading(16, ((float(experience ** (1/3.25))-int(experience ** (1/3.25))) * 100), ctx.message.author)}\n**{'Land' if int(experience ** (1/3.25)) < 5 else 'Wooden' if int(experience ** (1/3.25)) < 10 else 'Coal' if int(experience ** (1/3.25)) < 15 else 'Stone' if int(experience ** (1/3.25)) < 20 else 'Bronze' if int(experience ** (1/3.25)) < 25 else 'Iron' if int(experience ** (1/3.25)) < 30 else 'Gold' if int(experience ** (1/3.25)) < 35 else 'Diamond' if int(experience ** (1 /3.25)) < 40 else 'Emerald' if int(experience ** (1/3.25)) < 45 else 'Sapphire' if int(experience ** (1/3.25)) < 50 else 'Amethyst'} league!**", color = discord.Color.green())
		embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
		await bot.get_channel(925125678855229450).send(content=f'{user.mention} leveled up!', embed = embed)
		users[f'{user.id}']["level"] = lvl_end
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def getloading(total, progres, user):
	progress = int(total*progres//100)
	S0 = "<:loading0start:927249513679302686>"
	S1 = "<:loading10start:927261897588367390>"
	S2 = "<:loading1start:927250592471089203>"
	M0 = "<:loading0mid:927250659059826718>"
	M1 = "<:loading10mid:927252512027844619>"
	M2 = "<:loading1mid:927250682371801118>"
	E0 = "<:loading0end:927250763938418749>"
	E1 = "<:loading10end:927261897466720276>"
	E2 = "<:loading1end:927250775665705010>"
	N0 = "<:0_:927255264808275988>"
	N1 = "<:1_:927255264728600586>"
	N2 = "<:2_:927255264908955679>"
	N3 = "<:3_:927255264468537385>"
	N4 = "<:4_:927255264766328923>"
	N5 = "<:5_:927255265240318042>"
	N6 = "<:6_:927255265038987265>"
	N7 = "<:7_:927255265206763592>"
	N8 = "<:8_:927255265286430740>"
	N9 = "<:9_:927255265018019931>"
	result=""
	experience = users[f'{user.id}']["experience"]
	lvl_start = users[str(user.id)]['level']
	lvl_end = int(experience ** (1/3.25))
	exp_nextlevel = int((lvl_end+1)**(1*3.25))
	exp_thislevel = int((lvl_end)**(1*3.25))
	if progres != 100:
		a=""
		for i in str(lvl_end):
			if i == "0": a+=N0
			if i == "1": a+=N1
			if i == "2": a+=N2
			if i == "3": a+=N3
			if i == "4": a+=N4
			if i == "5": a+=N5
			if i == "6": a+=N6
			if i == "7": a+=N7
			if i == "8": a+=N8
			if i == "9": a+=N9
		result+=f"{a} "
		if progress < 1: result+=S0
		elif progress < 2: result+=S1
		else: result+=S2
		progress -= 1
		for i in range(total-3):
			if progress < 1: result+=M0
			elif progress < 2: result+=M1
			else: result+=M2
			progress -= 1
		if progress < 1: result+=E0
		elif progress < 2: result+=E1
		else: result+=E2
		a=""
		for i in str(lvl_end + 1):
			if i == "0": a+=N0
			if i == "1": a+=N1
			if i == "2": a+=N2
			if i == "3": a+=N3
			if i == "4": a+=N4
			if i == "5": a+=N5
			if i == "6": a+=N6
			if i == "7": a+=N7
			if i == "8": a+=N8
			if i == "9": a+=N9
		result+=f" {a}\n"
	if progres == 100:
		a=""
		for i in str(lvl_end-1):
			if i == "0": a+=N0
			if i == "1": a+=N1
			if i == "2": a+=N2
			if i == "3": a+=N3
			if i == "4": a+=N4
			if i == "5": a+=N5
			if i == "6": a+=N6
			if i == "7": a+=N7
			if i == "8": a+=N8
			if i == "9": a+=N9
		result+=f"{a} "
		if progress < 1: result+=S0
		elif progress < 2: result+=S1
		else: result+=S2
		progress -= 1
		for i in range(total-3):
			if progress < 1: result+=M0
			elif progress < 2: result+=M1
			else: result+=M2
			progress -= 1
		if progress < 1: result+=E0
		elif progress < 2: result+=E1
		else: result+=E2
		a=""
		for i in str(lvl_end):
			if i == "0": a+=N0
			if i == "1": a+=N1
			if i == "2": a+=N2
			if i == "3": a+=N3
			if i == "4": a+=N4
			if i == "5": a+=N5
			if i == "6": a+=N6
			if i == "7": a+=N7
			if i == "8": a+=N8
			if i == "9": a+=N9
		result+=f" {a}\n"
	return result

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
	if message.author.bot == False:
		global users
		with open('users.json', 'r') as f:
			users = json.load(f)
		await add_experience(users, message.author)
		await level_up(users, message.author, message)
		with open('users.json', 'w') as f:
			json.dump(users, f, indent=4, sort_keys=True)
		await bot.process_commands(message)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.command(aliases=["уровень", "level", "lvl", "ранг", "ранк", "лвл"])
async def rank(ctx):
	experience = users[str(ctx.author.id)]['experience']
	lvl_end = int(experience ** (1 / 3.25))

	embed = discord.Embed(title = f'Lvl {int(experience ** (1/3.25))} ({experience}/{int((lvl_end+1)**(1*3.25))} exp | {int((float(experience ** (1/3.25))-int(experience ** (1/3.25))) * 100)}%)', description = f"{getloading(16, ((float(experience ** (1/3.25))-int(experience ** (1/3.25))) * 100), ctx.message.author)}\n**{'Land' if int(experience ** (1/3.25)) < 5 else 'Wooden' if int(experience ** (1/3.25)) < 10 else 'Coal' if int(experience ** (1/3.25)) < 15 else 'Stone' if int(experience ** (1/3.25)) < 20 else 'Bronze' if int(experience ** (1/3.25)) < 25 else 'Iron' if int(experience ** (1/3.25)) < 30 else 'Gold' if int(experience ** (1/3.25)) < 35 else 'Diamond' if int(experience ** (1 /3.25)) < 40 else 'Emerald' if int(experience ** (1/3.25)) < 45 else 'Sapphire' if int(experience ** (1/3.25)) < 50 else 'Amethyst'} league!**", color = discord.Color.green())
	embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.command(aliases=["leader", "лидеры", "leaders", "leaderboard", "leadersboard", "топ", "лидербоард", "top", "лидер"])
async def ranks(ctx):
	total=[]
	result=''
	for user in users:
		experience = users[user]['experience']
		total.append([experience, int(user)])
	total = sorted(total,reverse=True, key=lambda x:x[0])




	try: result+=f':tada: <:1_:927255264728600586> - **{await bot.fetch_user(int(total[0][1]))}** {" " * 15}lvl: **{int(total[0][0]**(1/3.25))}** {" " * 15}exp: **{total[0][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:2_:927255264908955679> - **{await bot.fetch_user(int(total[1][1]))}** {" " * 15}lvl: **{int(total[1][0]**(1/3.25))}** {" " * 15}exp: **{total[1][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:3_:927255264468537385> - **{await bot.fetch_user(int(total[2][1]))}** {" " * 15}lvl: **{int(total[2][0]**(1/3.25))}** {" " * 15}exp: **{total[2][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:4_:927255264766328923> - **{await bot.fetch_user(int(total[3][1]))}** {" " * 15}lvl: **{int(total[3][0]**(1/3.25))}** {" " * 15}exp: **{total[3][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:5_:927255265240318042> - **{await bot.fetch_user(int(total[4][1]))}** {" " * 15}lvl: **{int(total[4][0]**(1/3.25))}** {" " * 15}exp: **{total[4][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:6_:927255265038987265> - **{await bot.fetch_user(int(total[5][1]))}** {" " * 15}lvl: **{int(total[5][0]**(1/3.25))}** {" " * 15}exp: **{total[5][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:7_:927255265206763592> - **{await bot.fetch_user(int(total[6][1]))}** {" " * 15}lvl: **{int(total[6][0]**(1/3.25))}** {" " * 15}exp: **{total[6][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:8_:927255265286430740> - **{await bot.fetch_user(int(total[7][1]))}** {" " * 15}lvl: **{int(total[7][0]**(1/3.25))}** {" " * 15}exp: **{total[7][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:9_:927255265018019931> - **{await bot.fetch_user(int(total[8][1]))}** {" " * 15}lvl: **{int(total[8][0]**(1/3.25))}** {" " * 15}exp: **{total[8][0]}** :tada: \n'
	except Exception as e: pass
	try: result+=f':tada: <:1_:927255264728600586><:0_:927255264808275988> - **{await bot.fetch_user(int(total[9][1]))}** {" " * 15}lvl: **{int(total[9][0]**(1/3.25))}** {" " * 15}exp: **{total[9][0]}** :tada: \n'
	except Exception as e: pass



	embed = discord.Embed(title = f'Список лидеров по уровням.', description = f"{result}", color = discord.Color.green())
	embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot.run('')

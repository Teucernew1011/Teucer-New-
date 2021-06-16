import discord
import os
import asyncio
import datetime
from discord.ext import commands, tasks
from emotes import *
from miscdata import *
from chardata import *
from charinfo import *
from weapinfo import *

client = commands.Bot(command_prefix='$')
client.remove_command("help")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="with Mora"))
	print("Alright, now we gotta make a pinkie promise!".format(client))
	await reminder.start()

#---------------------------------------
# Daily Reminder
#---------------------------------------
@tasks.loop(seconds=60)
async def reminder():
	
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  channel = client.get_channel(851446891089494066)

  if (minute == 0):
    reset_times = [9, 3, 20]
    role_mentions = ["<@&823837101391872001>", "<@&823837115782660106>", "<@&823837117812572180> and <@&828528959716065280>"]

    regions = ["`AMERICA`", "`EUROPE`", "`ASIA` & `TW, HK, MO`"]
    if (hour in reset_times):
        index = reset_times.index(hour)
        reminder_embed = discord.Embed(description=f"{regions[index]} server times have reset. Remember to do your **Daily Check-In**!\n— [HoYoLAB Daily Check-In](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us)", color=color)
        await channel.send(content=role_mentions[index], embed=reminder_embed)

#---------------------------------------
# Help Command
#---------------------------------------
@client.command()
async def help(ctx):
	
	embed = discord.Embed(description=f"Teucer will listen to you if you play with me using the prefix, `$`.\nReact with {exit} to close this menu.", color=color)
	embed.add_field(name="Commands List", value="• `$character <characterName>`: Shows detailed information about the specified character.\n— *aliases: $char*\n• `$farm <material>`: Shows all available farming routes for the specified material.\n— *aliases: $map, $route*\n• `$transformer`: Shows which materials are available for transmutation into your desired outcome.\n— *aliases: $parametric, $transmute, $transmutation*",inline=False)
	embed.set_author(name="Help Menu [Under Development]")
	embed.set_footer(text="Character Information retrieved from HoneyHunterWorld. All rights reserved by miHoYo.")
	embed.set_thumbnail(url='https://i.imgur.com/UZi0yUa.png')
	
	message = await ctx.send(embed=embed)
	
	await message.add_reaction(exit)
	
	def check(reaction, user):
		return user == ctx.author and str(reaction.emoji) in [exit] and reaction.message == message
	
	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
			
			if str(reaction.emoji) == exit:
				await message.delete()
		
		except asyncio.TimeoutError:
			await message.clear_reactions()
			break
			
#---------------------------------------
# Parametric Transformer
#---------------------------------------
@client.command(aliases=['parametric', 'transmute', 'transmutation'])
async def transformer(ctx):

	parametric_page_index = 0
	parametric_page_total = 2
	
	transformer = [parametric[0], parametric[1], parametric[2], parametric[3], parametric[4], parametric[5], parametric[6], parametric[7], parametric[8], parametric[9], parametric[10], parametric[11]]

	def transformer_toggle():
		transformer_embed = discord.Embed(color=color)
		transformer_embed.set_author(name="Parametric Transformer", icon_url="https://static.wikia.nocookie.net/gensin-impact/images/f/f1/Item_Parametric_Transformer.png/revision/latest/scale-to-width-down/256?cb=20210312183450")
		transformer_embed.add_field(name=f"{transformer[parametric_page_index]}", value=f"{transformer[parametric_page_index+6]}", inline=True)
		transformer_embed.add_field(name=f"{transformer[parametric_page_index+3]}", value=f"{transformer[parametric_page_index+9]}", inline=True)
		transformer_embed.set_footer(text=f"Page {parametric_page_index+1}/{parametric_page_total+1}")
		return transformer_embed
	message = await ctx.send(embed=transformer_toggle())

	await message.add_reaction(left)
	await message.add_reaction(right)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
			
			if str(reaction.emoji) == right and parametric_page_index != parametric_page_total:
				parametric_page_index += 1
			elif str(reaction.emoji) == left and parametric_page_index > 0:
				parametric_page_index -= 1
		
			await message.edit(embed=transformer_toggle())
			await message.remove_reaction(reaction, user)
		
		except asyncio.TimeoutError:
			await message.clear_reactions()
			break

#---------------------------------------
# Farming Maps
#---------------------------------------
@client.command(aliases=['map', 'route'])
async def farm(ctx, *, material):

	material = material.lower()

	index = 1
	farm_page_index = 0

	if material == "wood":
		farm_page_total = 0
		def embed_toggle():
			embed = discord.Embed(color=color)
			embed.set_image(url="https://media.discordapp.net/attachments/821365246043095050/839499189209923594/yp9oe5yxxbw61.png")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "bamboo" or material == "bamboo segment":
		farm_page_total = 1
		data = ["https://i.imgur.com/XhtKBSw.png", "https://i.imgur.com/hoRFd29.png"]
		def embed_toggle():
			embed = discord.Embed(description="Segments of bamboo that are light and far stronger than their humble appearance might suggest. It lets off a light fragrance. Can be used to create furnishings.", color=color)
			embed.set_author(name="Bamboo Segment", icon_url="https://cdn.discordapp.com/emojis/849917931500208128.png?v=1")
			embed.set_image(url=f"{data[farm_page_index]}")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "wolfhook":
		farm_page_total = 0
		def embed_toggle():
			embed = discord.Embed(description="A berry with thorns that often gets attached to a wolf's pelt. When you look at it, you can almost hear the echoing cries of the wolves in the woods.", color=color)
			embed.set_author(name="Wolfhook", icon_url="https://cdn.discordapp.com/emojis/846999357815390208.png?v=1")
			embed.set_image(url="https://i.imgur.com/4zAJnNI.png")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "valberry" or material == "valberries":
		farm_page_total = 2
		data = ["https://i.imgur.com/DEuZhSg.png", "https://i.imgur.com/Uknsij4.png", "https://i.imgur.com/wEJS68k.png"]
		def embed_toggle():
			embed = discord.Embed(description="A plump and translucent berry that has a fragrant smell and a sweet refreshing taste. In the past, the watchers of the storms found solace in the sweetness of the fruit and the hope for the city's security.", color=color)
			embed.set_author(name="Valberry", icon_url="https://cdn.discordapp.com/emojis/846999354874003487.png?v=1")
			embed.set_image(url=f"{data[farm_page_index]}")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "cecilia":
		farm_page_total = 0
		def embed_toggle():
			embed = discord.Embed(description="A beautiful flower with a name that suits its appearance. It only grows where harsh winds blow, and is just as intangible as the true heart of an unbound soul.", color=color)
			embed.set_author(name="Cecilia", icon_url="https://cdn.discordapp.com/emojis/846999355897806868.png?v=1")
			embed.set_image(url="https://i.imgur.com/Svw5x1n.png")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "philanemo mushroom" or material == "philanemo":
		farm_page_total = 2
		data = ["https://i.imgur.com/AZgzHQV.png", "https://i.imgur.com/NrFh0W7.png", "https://i.imgur.com/ev7NuFq.png"]
		def embed_toggle():
			embed = discord.Embed(description="A fungus that grows in the warm caress of the wind. It is as everlasting as the wind, nourishing life.", color=color)
			embed.set_author(name="Philanemo Mushroom", icon_url="https://cdn.discordapp.com/emojis/846999356078555147.png?v=1")
			embed.set_image(url=f"{data[farm_page_index]}")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "windwheel aster" or material == "windwheel" or material == "aster":
		farm_page_total = 6
		data = ["https://i.imgur.com/492wmN6.png", "https://i.imgur.com/g1rySfs.png", "https://i.imgur.com/WW4hdkE.png", "https://i.imgur.com/PtQrZ0v.png", "https://i.imgur.com/dQstBPQ.png", "https://i.imgur.com/45TWCWs.png", "https://i.imgur.com/j1dRfop.png"]
		def embed_toggle():
			embed = discord.Embed(description="A plant that adores the wind. To the proud children of the wind, or the citizens of Mondstadt, the Windwheel Asters are the \"visible winds\".", color=color)
			embed.set_author(name="Windwheel Aster", icon_url="https://cdn.discordapp.com/emojis/846999355994144849.png?v=1")
			embed.set_image(url=f"{data[farm_page_index]}")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	elif material == "calla lily" or material == "calla" or material == "callalily":
		farm_page_total = 7
		data = ["https://i.imgur.com/QGJXyva.png", "https://i.imgur.com/fI8UpGR.png", "https://i.imgur.com/GHoAnD3.png", "https://i.imgur.com/SE33T0t.png", "https://i.imgur.com/g7FfTaf.png", "https://i.imgur.com/wgQrD0Q.png", "https://i.imgur.com/Pc3gCZd.png", "https://i.imgur.com/ij3AmFV.png"]
		def embed_toggle():
			embed = discord.Embed(description="A flower that grows near water sources. When cooked, the petals have a chunky texture, yet are sweet and a little bitter.", color=color)
			embed.set_author(name="Calla Lily", icon_url="https://cdn.discordapp.com/emojis/849918031835430942.png?v=1")
			embed.set_image(url=f"{data[farm_page_index]}")
			embed.set_footer(text=f"Page {farm_page_index+1}/{farm_page_total+1}")
			return embed
		message = await ctx.send(embed=embed_toggle())

	else:
		index = 0
		embed = discord.Embed(description="This material is either invalid or has not been added yet.", color=color)
		await ctx.send(embed=embed)

	if index != 0: await message.add_reaction(left)
	if index != 0: await message.add_reaction(right)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
			
			if str(reaction.emoji) == right and farm_page_index != farm_page_total:
				farm_page_index += 1
			elif str(reaction.emoji) == left and farm_page_index > 0:
				farm_page_index -= 1
			
			await message.edit(embed=embed_toggle())
			await message.remove_reaction(reaction, user)

		except asyncio.TimeoutError:
			await message.clear_reactions()
			break

#---------------------------------------
# Character Info
#---------------------------------------
@client.command(aliases=['char'])
async def character(ctx, *, char_name):

	char_name = char_name.lower()

	index = profile_page_total = cons_page_total = 1
	profile_page_index = autoattack_page_index = skill_page_index = burst_page_index = cons_page_index = 0

	if char_name == "sucrose" or char_name == "succ":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Sucrose", four[0], anemo[0], catalyst_icon]
		char_desc = "An alchemist filled with curiosity about all things. She researches bio-alchemy."
		char_img = ["https://i.imgur.com/FNSP60J.png", "https://i.imgur.com/Xg3tQL8.png", "https://i.imgur.com/9ZDyVDP.png", "https://i.imgur.com/kFzt7JK.png", "https://i.imgur.com/gyXYDik.png"]

		profile_data = ["Harmless Sweetie", "Knights of Favonius", "November 26", "Ampulla", "Valeria Rodriguez", "Xiaogan (小敢)", "Akane Fujita (藤田茜)", "Kim Ha-yeong (김하영)"]
		stats_data = ["775 → 9244", "14 → 170", "59 → 703", "• Anemo DMG%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], anemo_hypo, aster, nectar[0], nectar[1], nectar[2], freedom[0], freedom[1], freedom[2], boreas[2]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=sucrose_autoattack[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				sucrose_autoattack_data(embed)
			if autoattack_page_index == 2:
				sucrose_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{sucrose_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=sucrose_skill[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				sucrose_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{sucrose_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=sucrose_burst[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				sucrose_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{sucrose_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])

			cons_field  = [sucrose_cons[0], sucrose_cons[6], sucrose_cons[2], sucrose_cons[8], sucrose_cons[4], sucrose_cons[10], sucrose_cons[1], sucrose_cons[7], sucrose_cons[3], sucrose_cons[9], sucrose_cons[5], sucrose_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{sucrose_cons[12]}`", value=f"{sucrose_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{sucrose_cons[14]}`", value=f"{sucrose_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{sucrose_cons[16]}`", value=f"{sucrose_cons[17]}", inline=False)
			return embed

	elif char_name == "sayu" or char_name == "ball":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Sayu", four[0], anemo[0], claymore_icon]
		char_desc = "A pint-sized ninja attached to the Shiyuumatsu-Ban, who always seems sleep-deprived."
		char_img = ["https://i.imgur.com/MWmXGpI.png", "https://i.imgur.com/Ngkvp6R.png"]

		profile_data = ["_ _", "_ _", "October 19", "_ _", "_ _", "_ _", "_ _", "_ _"]
		stats_data = ["994 → 11854", "20 → 244", "62 → 745", "• EM: 0.0 → 96.0", "5.0%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], kenki, local2, nectar[0], nectar[1], nectar[2], talent2[0], talent2[1], talent2[2], azhdaha[2]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=sayu_autoattack[1], color=anemo[1])
		#		embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				sayu_autoattack_data(embed)
			if autoattack_page_index == 2:
				sayu_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{sayu_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=sayu_skill[1], color=anemo[1])
		#		embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				sayu_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{sayu_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=sayu_burst[1], color=anemo[1])
		#		embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				sayu_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{sayu_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])
			
			cons_field = [sayu_cons[0], sayu_cons[6], sayu_cons[2], sayu_cons[8], sayu_cons[4], sayu_cons[10], sayu_cons[1], sayu_cons[7], sayu_cons[3], sayu_cons[9], sayu_cons[5], sayu_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{sayu_cons[12]}`", value=f"{sayu_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{sayu_cons[14]}`", value=f"{sayu_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{sayu_cons[16]}`", value=f"{sayu_cons[17]}", inline=False)
			return embed

	elif char_name == "jean" or char_name == "tights":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Jean Gunnhildr", five[0], anemo[0], sword_icon]
		char_desc = "The righteous and rigorous Dandelion Knight, and Acting Grand Master of the Knights of Favonius of Mondstadt."
		char_img = ["https://i.imgur.com/QZhI15q.png", "https://i.imgur.com/E8aycv2.png", "https://i.imgur.com/2i4PCoN.png", "https://i.imgur.com/plSbRVj.png", "https://i.imgur.com/u20s9Dv.png"]

		profile_data = ["Dandelion Knight", "Knights of Favonius", "March 14", "Leo Minor", "Stephanie Southerland", "Su Lin (林簌)", "Chiwa Saitō (斎藤千和)", "Ahn Young-mi (안영미)"]
		stats_data = ["1144 → 14695", "19 → 239", "60 → 769", "• Healing%: 0.0% → 22.2%", "5.0%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], anemo_hypo, dandelion, mask[0], mask[1], mask[2], resistance[0], resistance[1], resistance[2], dvalin[0]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=jean_autoattack[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				jean_autoattack_data(embed)
			if autoattack_page_index == 2:
				jean_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{jean_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=jean_skill[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				jean_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{jean_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=jean_burst[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				jean_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{jean_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])

			cons_field  = [jean_cons[0], jean_cons[6], jean_cons[2], jean_cons[8], jean_cons[4], jean_cons[10], jean_cons[1], jean_cons[7], jean_cons[3], jean_cons[9], jean_cons[5], jean_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{jean_cons[12]}`", value=f"{jean_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{jean_cons[14]}`", value=f"{jean_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{jean_cons[16]}`", value=f"{jean_cons[17]}", inline=False)
			return embed

	elif char_name == "venti" or char_name == "barbatos" or char_name == "barsibatos" or char_name == "bartobas" or char_name == "bard" or char_name == "kazeda":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Venti", five[0], anemo[0], bow_icon]
		char_desc = "One of the many bards of Mondstadt, who freely wanders the city's streets and alleys."
		char_img = ["https://i.imgur.com/ghljZAy.png", "https://i.imgur.com/9b5mMpV.png", "https://i.imgur.com/oom7A7K.png", "https://i.imgur.com/N1mebGY.png", "https://i.imgur.com/WpmLB6D.png"]

		profile_data = ["Windborne Bard", "Mondstadt", "June 16", "Carmen Dei", "Erika Harlacher", "Miaojiang (喵酱)", "Ayumu Murase (村瀬歩)", "Jung Yoo-jung (정유정)"]
		stats_data = ["820 → 10531", "20 → 263", "52 → 669", "• ER%: 0.0% → 32.0%", "5.0%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], anemo_hypo, cecilia, slime[0], slime[1], slime[2], ballad[0], ballad[1], ballad[2], boreas[0]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			

			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=venti_autoattack[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")
			if autoattack_page_index == 1:
				venti_autoattack_data(embed)
			if autoattack_page_index == 2:
				venti_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{venti_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=venti_skill[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				venti_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{venti_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=venti_burst[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				venti_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{venti_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])

			cons_field  = [venti_cons[0], venti_cons[6], venti_cons[2], venti_cons[8], venti_cons[4], venti_cons[10], venti_cons[1], venti_cons[7], venti_cons[3], venti_cons[9], venti_cons[5], venti_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{venti_cons[12]}`", value=f"{venti_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{venti_cons[14]}`", value=f"{venti_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{venti_cons[16]}`", value=f"{venti_cons[17]}", inline=False)
			return embed

	elif char_name == "xiao" or char_name == "alatus" or char_name == "midget" or char_name == "edge":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Xiao", five[0], anemo[0], polearm_icon]
		char_desc = "A yaksha adeptus who defends Liyue. Also heralded as the \"Conqueror of Demons\" and \"Vigilant Yaksha.\""
		char_img = ["https://i.imgur.com/F52rL1N.png", "https://i.imgur.com/hUDj92f.png", "https://i.imgur.com/ElOAXAM.png", "https://i.imgur.com/nfJQFun.png", "https://i.imgur.com/2OhIFuf.png"]

		profile_data = ["Vigilant Yaksha", "Liyue Adeptus", "April 17", "Alatus Nemeseos", "Laila Berzins", "kinsen", "Yoshitsugu Matsuoka (松岡禎丞)", "Sim Kyu-hyuk (심규혁)"]
		stats_data = ["991 → 12736", "27 → 349", "62 → 799", "_ _", "5.0% → 24.2%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], geovishap, qingxin, slime[0], slime[1], slime[2], prosperity[0], prosperity[1], prosperity[2], childe[2]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=xiao_autoattack[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				xiao_autoattack_data(embed)
			if autoattack_page_index == 2:
				xiao_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{xiao_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=xiao_skill[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				xiao_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{xiao_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=xiao_burst[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				xiao_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{xiao_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])

			cons_field  = [xiao_cons[0], xiao_cons[6], xiao_cons[2], xiao_cons[8], xiao_cons[4], xiao_cons[10], xiao_cons[1], xiao_cons[7], xiao_cons[3], xiao_cons[9], xiao_cons[5], xiao_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{xiao_cons[12]}`", value=f"{xiao_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{xiao_cons[14]}`", value=f"{xiao_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{xiao_cons[16]}`", value=f"{xiao_cons[17]}", inline=False)
			return embed

	elif char_name == "kazuha" or char_name == "kazu" or char_name == "kazoo" or char_name == "zuzu" or char_name == "aether dlc":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Kaedahara Kazuha", five[0], anemo[0], sword_icon]
		char_desc = "A wandering samurai from Inazuma who is currently with Liyue's Crux Fleet. A gentle and carefree soul whose heart hides a great many burdens from the past."
		char_img = ["https://i.imgur.com/wuRVE3g.png", "https://i.imgur.com/WuJNtdk.png", "https://i.imgur.com/2i4PCoN.png"]

		profile_data = ["Scarlet Leaves Pursue Wild Leaves", "Crux Fleet", "October 29", "Acer Palmatum", "Mark Whitten", "Bānmǎ (斑马)", "Nobunaga Shimazaki (島﨑信長)", "Shin-Woo Kim (김신우)"]
		stats_data = ["1039 → 13348", "23 → 297", "63 → 807", "• EM: 0.0 → 115.2", "5.0%", "50.0%"]
		ascension_data = [anemo[2], anemo[3], anemo[4], anemo[5], kenki, ganoderma, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], diligence[0], diligence[1], diligence[2], azhdaha[2]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=anemo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=anemo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=kazuha_autoattack[1], color=anemo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				kazuha_autoattack_data(embed)

			if autoattack_page_index == 2:
				kazuha_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{kazuha_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=anemo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=kazuha_skill[1], color=anemo[1])
		#		embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				kazuha_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{kazuha_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=anemo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=kazuha_burst[1], color=anemo[1])
		#		embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				kazuha_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{kazuha_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=anemo[1])

			cons_field  = [kazuha_cons[0], kazuha_cons[6], kazuha_cons[2], kazuha_cons[8], kazuha_cons[4], kazuha_cons[10], kazuha_cons[1], kazuha_cons[7], kazuha_cons[3], kazuha_cons[9], kazuha_cons[5], kazuha_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{kazuha_cons[12]}`", value=f"{kazuha_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{kazuha_cons[14]}`", value=f"{kazuha_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{kazuha_cons[16]}`", value=f"{kazuha_cons[17]}", inline=False)
			return embed

	elif char_name == "noelle" or char_name == "maid":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Noelle", four[0], geo[0], claymore_icon]
		char_desc = "A maid in the service of the Knights of Favonius that dreams of joining their ranks someday."
		char_img = ["https://i.imgur.com/uEilPHa.png", "https://i.imgur.com/5lBwgvY.png", "https://i.imgur.com/85Wxdnm.png", "https://i.imgur.com/Qom6TYO.png", "https://i.imgur.com/77z1I6G.png"]

		profile_data = ["Chivalric Blossom", "Knights of Favonius", "March 21", "Parma Cordis", "Laura Faye Smith", "Yanning (宴宁)", "Kanon Takao (高尾奏音)", "Lee Bo-hee (이보희)"]
		stats_data = ["1012 → 12071", "16 → 191", "67 → 799", "• DEF%: 0.0% → 30.0%", "5.0%", "50.0%"]
		ascension_data = [geo[2], geo[3], geo[4], geo[5], geo_hypo, valberry, mask[0], mask[1], mask[2], resistance[0], resistance[1], resistance[2], dvalin[1]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=geo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=geo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=noelle_autoattack[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				noelle_autoattack_data(embed)
			if autoattack_page_index == 2:
				noelle_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{noelle_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=geo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=noelle_skill[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				noelle_skill_data(embed)
		
			embed.set_author(name=f"{char_talent[1]}{noelle_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=geo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=noelle_burst[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				noelle_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{noelle_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=geo[1])
			
			cons_field = [noelle_cons[0], noelle_cons[6], noelle_cons[2], noelle_cons[8], noelle_cons[4], noelle_cons[10], noelle_cons[1], noelle_cons[7], noelle_cons[3], noelle_cons[9], noelle_cons[5], noelle_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{noelle_cons[12]}`", value=f"{noelle_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{noelle_cons[14]}`", value=f"{noelle_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{noelle_cons[16]}`", value=f"{noelle_cons[17]}", inline=False)
			return embed

	elif char_name == "ningguang" or char_name == "ning":

		autoattack_page_total = 1
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Ningguang", four[0], geo[0], catalyst_icon]
		char_desc = "The Tianquan of Liyue Qixing. Her wealth is unsurpassed in all of Teyvat."
		char_img = ["https://i.imgur.com/5my6Vcy.png", "https://i.imgur.com/pE0n8d5.png", "https://i.imgur.com/tVi9lMR.png", "https://i.imgur.com/kN5TePE.png", "https://i.imgur.com/vSWVN0f.png"]

		profile_data = ["Eclipsing Star", "Liyue Qixing", "August 26", "Opus Aequilibrium", "Erin Ebers", "Mingya Du (杜冥鸦)", "Sayaka Ohara (大原さやか)", "Gwak Gyu-mi (곽규미)"]
		stats_data = ["821 → 9787", "18 → 212", "48 → 573", "• Geo DMG%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [geo[2], geo[3], geo[4], geo[5], geo_hypo, glazelily, fatui_insignia[0], fatui_insignia[1], fatui_insignia[2], prosperity[0], prosperity[1], prosperity[2], boreas[2]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=geo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=geo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=ningguang_autoattack[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				ningguang_autoattack_data(embed)

			embed.set_author(name=f"{char_talent[0]}{ningguang_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=geo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=ningguang_skill[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				ningguang_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{ningguang_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=geo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=ningguang_burst[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				ningguang_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{ningguang_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=geo[1])
			
			cons_field = [ningguang_cons[0], ningguang_cons[6], ningguang_cons[2], ningguang_cons[8], ningguang_cons[4], ningguang_cons[10], ningguang_cons[1], ningguang_cons[7], ningguang_cons[3], ningguang_cons[9], ningguang_cons[5], ningguang_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{ningguang_cons[12]}`", value=f"{ningguang_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{ningguang_cons[14]}`", value=f"{ningguang_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{ningguang_cons[16]}`", value=f"{ningguang_cons[17]}", inline=False)
			return embed

	elif char_name == "zhongli" or char_name == "morax" or char_name == "rex lapis" or char_name == "daddy" or char_name == "zheith" or char_name == "broke":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Zhongli", five[0], geo[0], polearm_icon]
		char_desc = "A mysterious expert contracted by the Wangsheng Funeral Parlor. Extremely knowledgeable in all things."
		char_img = ["https://i.imgur.com/Mnu2qRl.png", "https://i.imgur.com/YvxrxGe.png", "https://i.imgur.com/J6n2tlT.png", "https://i.imgur.com/YIkuadV.png", "https://i.imgur.com/Jqdw3gs.png"]

		profile_data = ["Vago Mundo", "Liyue Harbor", "December 31", "Lapis Dei", "Keith Silverstein", "Bo Peng (彭博)", "Tomoaki Maeno (前野智昭)", "Pyo Yeong-jae (표영재)"]
		stats_data = ["1144 → 14695", "20 → 251", "57 → 738", "• Geo DMG%: 0.0% → 28.8%", "5.0%", "50.0%"]
		ascension_data = [geo[2], geo[3], geo[4], geo[5], geo_hypo, corlapis, slime[0], slime[1], slime[2], gold[0], gold[1], gold[2], childe[0]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=geo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=geo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=zhongli_autoattack[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				zhongli_autoattack_data(embed)
			if autoattack_page_index == 2:
				zhongli_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{zhongli_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=geo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=zhongli_skill[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				zhongli_skill_data(embed)
			if skill_page_index == 2:
				zhongli_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{zhongli_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=geo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=zhongli_burst[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				zhongli_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{zhongli_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=geo[1])
			
			cons_field = [zhongli_cons[0], zhongli_cons[6], zhongli_cons[2], zhongli_cons[8], zhongli_cons[4], zhongli_cons[10], zhongli_cons[1], zhongli_cons[7], zhongli_cons[3], zhongli_cons[9], zhongli_cons[5], zhongli_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{zhongli_cons[12]}`", value=f"{zhongli_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{zhongli_cons[14]}`", value=f"{zhongli_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{zhongli_cons[16]}`", value=f"{zhongli_cons[17]}", inline=False)
			return embed

	elif char_name == "albedo" or char_name == "kreideprinz"  or char_name == "alchemist" or char_name == "chalk" or char_name == "bedo" or char_name == "khoi" or char_name == "khoi dao":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Albedo", five[0], geo[0], sword_icon]
		char_desc = "A genius known as the Kreideprinz, he is the Chief Alchemist and Captain of the Investigation Team of the Knights of Favonius."
		char_img = ["https://i.imgur.com/mjjYYUG.png", "https://i.imgur.com/m7p4rab.png", "https://i.imgur.com/nqiCvPx.png", "https://i.imgur.com/L005e9m.png", "https://i.imgur.com/Ko7EWkh.png"]

		profile_data = ["Kreideprinz", "Knights of Favonius", "September 13", "Princeps Cretaceus", "Khoi Dao", "Mace", "Kenji Nojima (野島健児)", "Kim Myung-jun (김명준)"]
		stats_data = ["1030 → 13226", "20 → 251", "68 → 876", "• Geo DMG%: 0.0% → 28.8%", "5.0%", "50.0%"]
		ascension_data = [geo[2], geo[3], geo[4], geo[5], geo_hypo, cecilia, scroll[0], scroll[1], scroll[2], ballad[0], ballad[1], ballad[2], childe[0]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=geo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=geo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=albedo_autoattack[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				albedo_autoattack_data(embed)
			if autoattack_page_index == 2:
				albedo_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{albedo_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=geo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=albedo_skill[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				albedo_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{albedo_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=geo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=albedo_burst[1], color=geo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				albedo_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{albedo_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=geo[1])
			
			cons_field = [albedo_cons[0], albedo_cons[6], albedo_cons[2], albedo_cons[8], albedo_cons[4], albedo_cons[10], albedo_cons[1], albedo_cons[7], albedo_cons[3], albedo_cons[9], albedo_cons[5], albedo_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{albedo_cons[12]}`", value=f"{albedo_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{albedo_cons[14]}`", value=f"{albedo_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{albedo_cons[16]}`", value=f"{albedo_cons[17]}", inline=False)
			return embed

	elif char_name == "lisa" or char_name == "librarian" or char_name == "ara ara":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Lisa Minci", four[0], electro[0], catalyst_icon]
		char_desc = "The languid but knowledgeable Librarian of the Knights of Favonius, deemed by Sumeru Academia to be their most distinguished graduate in the past two centuries."
		char_img = ["https://i.imgur.com/OX1MSZe.png", "https://i.imgur.com/MO9avBL.png", "https://i.imgur.com/v0fVWmv.png", "https://i.imgur.com/W9jUwub.png", "https://i.imgur.com/srHliVi.png"]

		profile_data = ["Witch of Purple Rose", "Knights of Favonius", "June 09", "Tempus Fugit", "Mara Junot", "Ke Zhong (钟可)", "Rie Tanaka (田中理恵)", "Park Go-woon (박고운)"]
		stats_data = ["802 → 9570", "19 → 232", "48 → 573", "• EM: 0.0 → 96.0", "5.0%", "50.0%"]
		ascension_data = [electro[2], electro[3], electro[4], electro[5], electro_hypo, valberry, slime[0], slime[1], slime[2], ballad[0], ballad[1], ballad[2], dvalin[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=electro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=electro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=lisa_autoattack[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				lisa_autoattack_data(embed)
			if autoattack_page_index == 2:
				lisa_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{lisa_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=electro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=lisa_skill[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				lisa_skill_data(embed)
			if skill_page_index == 2:
				lisa_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{lisa_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=electro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=lisa_burst[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				lisa_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{lisa_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=electro[1])
      
			cons_field = [lisa_cons[0], lisa_cons[6], lisa_cons[2], lisa_cons[8], lisa_cons[4], lisa_cons[10], lisa_cons[1], lisa_cons[7], lisa_cons[3], lisa_cons[9], lisa_cons[5], lisa_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{lisa_cons[12]}`", value=f"{lisa_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{lisa_cons[14]}`", value=f"{lisa_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{lisa_cons[16]}`", value=f"{lisa_cons[17]}", inline=False)
			return embed

	elif char_name == "fischl" or char_name == "oz" or char_name == "amy":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Fischl von Luftschloss Narfidort", four[0], electro[0], bow_icon]
		char_desc = "A mysterious girl who calls herself \"Prinzessin der Verurteilung\" and travels with a night raven named Oz."
		char_img = ["https://i.imgur.com/aKaWqMH.png", "https://i.imgur.com/j4zemFn.png", "https://i.imgur.com/E37g4Mp.png", "https://i.imgur.com/pRLK808.png", "https://i.imgur.com/mxoQf0W.png"]

		profile_data = ["Prinzessin der Verurteilung", "Adventurers\' Guild", "May 27", "Corvus", "Brittany Cox", "Mace", "Maaya Uchida (内田真礼)", "Park Go-woon (박고운)"]
		stats_data = ["770 → 9189", "20 → 244", "50 → 594", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [electro[2], electro[3], electro[4], electro[5], electro_hypo, lampgrass, arrowhead[0], arrowhead[1], arrowhead[2], ballad[0], ballad[1], ballad[2], boreas[2]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=electro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=electro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=fischl_autoattack[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				fischl_autoattack_data(embed)
			if autoattack_page_index == 2:
				fischl_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{fischl_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=electro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=fischl_skill[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				fischl_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{fischl_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=electro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=fischl_burst[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				fischl_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{fischl_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=electro[1])
      
			cons_field = [fischl_cons[0], fischl_cons[6], fischl_cons[2], fischl_cons[8], fischl_cons[4], fischl_cons[10], fischl_cons[1], fischl_cons[7], fischl_cons[3], fischl_cons[9], fischl_cons[5], fischl_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{fischl_cons[12]}`", value=f"{fischl_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{fischl_cons[14]}`", value=f"{fischl_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{fischl_cons[16]}`", value=f"{fischl_cons[17]}", inline=False)
			return embed

	elif char_name == "razor" or char_name == "wolf" or char_name == "woof":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 2

		char_data = ["Razor", four[0], electro[0], claymore_icon]
		char_desc = "A boy who lives among the wolves in Wolvendom of Mondstadt, away from human civilization. As agile as lightning."
		char_img = ["https://i.imgur.com/EGOkTzp.png", "https://i.imgur.com/QStR63l.png", "https://i.imgur.com/ysLZT2o.png", "https://i.imgur.com/F4gc7an.png", "https://i.imgur.com/Uk6utZ0.png"]

		profile_data = ["Wolf Boy", "Wolvendom", "September 09", "Lupus Minor", "Todd Haberkorn", "Shuai Zhou (周帅)", "Kōki Uchiyama (内山昂輝)", "Kim Seo-yeong (김서영)"]
		stats_data = ["1003 → 11962", "20 → 234", "63 → 751", "• Phys DMG%: 0.0% → 30.0%", "5.0%", "50.0%"]
		ascension_data = [electro[2], electro[3], electro[4], electro[5], electro_hypo, wolfhook, mask[0], mask[1], mask[2], resistance[0], resistance[1], resistance[2], dvalin[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=electro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=electro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=razor_autoattack[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				razor_autoattack_data(embed)
			if autoattack_page_index == 2:
				razor_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{razor_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=electro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=razor_skill[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				razor_skill_data(embed)
			if skill_page_index == 2:
				razor_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{razor_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=electro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=razor_burst[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				razor_burst_data(embed)
			if burst_page_index == 2:
				razor_burst_data2(embed)

			embed.set_author(name=f"{char_talent[2]}{razor_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=electro[1])
      
			cons_field = [razor_cons[0], razor_cons[6], razor_cons[2], razor_cons[8], razor_cons[4], razor_cons[10], razor_cons[1], razor_cons[7], razor_cons[3], razor_cons[9], razor_cons[5], razor_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{razor_cons[12]}`", value=f"{razor_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{razor_cons[14]}`", value=f"{razor_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{razor_cons[16]}`", value=f"{razor_cons[17]}", inline=False)
			return embed

	elif char_name == "beidou":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Beidou", four[0], electro[0], claymore_icon]
		char_desc = "Captain of her crew, The Crux. She's quite an unbound and forthright woman."
		char_img = ["https://i.imgur.com/t9tf3D1.png", "https://i.imgur.com/QcUOshy.png", "https://i.imgur.com/ErGO7m4.png", "https://i.imgur.com/nUE0ee8.png", "https://i.imgur.com/RCxfuYy.png"]

		profile_data = ["Uncrowned Lord of the Ocean", "The Crux", "February 14", "Victor Mare", "Allegra Clark", "Yajing Tang (唐雅菁)", "Ami Koshimizu (小清水亜美)", "Jeong Yoo-mi (정유미)"]
		stats_data = ["1094 → 13050", "19 → 225", "54 → 648", "• Electro DMG%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [electro[2], electro[3], electro[4], electro[5], electro_hypo, nocjade, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], gold[0], gold[1], gold[2], dvalin[2]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=electro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=electro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=beidou_autoattack[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				beidou_autoattack_data(embed)
			if autoattack_page_index == 2:
				beidou_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{beidou_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=electro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=beidou_skill[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				beidou_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{beidou_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=electro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=beidou_burst[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				beidou_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{beidou_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=electro[1])
      
			cons_field = [beidou_cons[0], beidou_cons[6], beidou_cons[2], beidou_cons[8], beidou_cons[4], beidou_cons[10], beidou_cons[1], beidou_cons[7], beidou_cons[3], beidou_cons[9], beidou_cons[5], beidou_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{beidou_cons[12]}`", value=f"{beidou_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{beidou_cons[14]}`", value=f"{beidou_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{beidou_cons[16]}`", value=f"{beidou_cons[17]}", inline=False)
			return embed

	elif char_name == "keqing" or char_name == "keking" or char_name == "keq":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Keqing", five[0], electro[0], sword_icon]
		char_desc = "The Yuheng of the Liyue Qixing. Keqing has much to say about Rex Lapis' unilateral approach to policymaking in Liyue — but in truth, gods admire skeptics such as her quite a lot."
		char_img = ["https://i.imgur.com/iQCW8Bl.png", "https://i.imgur.com/A40Re2U.png", "https://i.imgur.com/heFPl2b.png", "https://i.imgur.com/Km7tTLG.png", "https://i.imgur.com/Aoy6B9D.png"]

		profile_data = ["Driving Thunder", "Liyue Qixing", "November 20", "Trulla Cementarii", "Kayli Mills", "Ying Xie (谢莹)", "Eri Kitamura (喜多村英梨)", "Lee Bo-hee (이보희)"]
		stats_data = ["1020 → 13103", "25 → 323", "62 → 799", "_ _", "5.0%", "50.0% → 88.4%"]
		ascension_data = [electro[2], electro[3], electro[4], electro[5], electro_hypo, corlapis, nectar[0], nectar[1], nectar[2], prosperity[0], prosperity[1], prosperity[2], boreas[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=electro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=electro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=keqing_autoattack[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				keqing_autoattack_data(embed)
			if autoattack_page_index == 2:
				keqing_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{keqing_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=electro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=keqing_skill[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				keqing_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{keqing_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=electro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=keqing_burst[1], color=electro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				keqing_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{keqing_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=electro[1])
      
			cons_field = [keqing_cons[0], keqing_cons[6], keqing_cons[2], keqing_cons[8], keqing_cons[4], keqing_cons[10], keqing_cons[1], keqing_cons[7], keqing_cons[3], keqing_cons[9], keqing_cons[5], keqing_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{keqing_cons[12]}`", value=f"{keqing_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{keqing_cons[14]}`", value=f"{keqing_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{keqing_cons[16]}`", value=f"{keqing_cons[17]}", inline=False)
			return embed

	elif char_name == "barbara" or char_name == "barb" or char_name == "ikuyo":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Barbara Pegg", four[0], hydro[0], catalyst_icon]
		char_desc = "Every citizen of Mondstadt adores Barbara. However, she learned the word \"idol\" from a magazine."
		char_img = ["https://i.imgur.com/dLaedfT.png", "https://i.imgur.com/QmS3pTk.png", "https://i.imgur.com/1gR9o6Y.png", "https://i.imgur.com/9W5hiLp.png", "https://i.imgur.com/QqZHBIs.png"]

		profile_data = ["Shining Idol", "Church of Favonius", "July 05", "Crater", "Laura Stahl", "Yuanyuan Song (宋媛媛)", "Akari Kitō (鬼頭明里)", "Yun Ah-yeong (윤아영)"]
		stats_data = ["821 → 9787", "13 → 159", "56 → 669", "• HP%: 0.0% → 24.0%", "5.0%", "50.0"]
		ascension_data = [hydro[2], hydro[3], hydro[4], hydro[5], oceanid, philanemo, scroll[0], scroll[1], scroll[2], freedom[0], freedom[1], freedom[2], boreas[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=hydro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=hydro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=barbara_autoattack[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				barbara_autoattack_data(embed)
			if autoattack_page_index == 2:
				barbara_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{barbara_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=hydro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=barbara_skill[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				barbara_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{barbara_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=hydro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=barbara_burst[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				barbara_burst_data(embed)
			
			embed.set_author(name=f"{char_talent[2]}{barbara_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=hydro[1])
      
			cons_field = [barbara_cons[0], barbara_cons[6], barbara_cons[2], barbara_cons[8], barbara_cons[4], barbara_cons[10], barbara_cons[1], barbara_cons[7], barbara_cons[3], barbara_cons[9], barbara_cons[5], barbara_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{barbara_cons[12]}`", value=f"{barbara_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{barbara_cons[14]}`", value=f"{barbara_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{barbara_cons[16]}`", value=f"{barbara_cons[17]}", inline=False)
			return embed

	elif char_name == "xingqiu" or char_name == "xq":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Xingqiu", four[0], hydro[0], sword_icon]
		char_desc = "A young man carrying a longsword who is frequently seen at book booths. He has a heart of gold and yearns for justice and fairness for all."
		char_img = ["https://i.imgur.com/Gcs1VaT.png", "https://i.imgur.com/MREIv3y.png", "https://i.imgur.com/UbSmoLs.png", "https://i.imgur.com/Z3tc7b0.png", "https://i.imgur.com/1DscEoP.png"]

		profile_data = ["Juvenile Galant", "Feiyun Commerce Guild", "October 09", "Fabulae Textile", "Cristina Vee Valenzuela", "Yajing Tang (唐雅菁)", "Junko Minagawa (皆川純子)", "Gwak Gyu-mi (곽규미)"]
		stats_data = ["857 → 10222", "17 → 202", "64 → 758", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0"]
		ascension_data = [hydro[2], hydro[3], hydro[4], hydro[5], oceanid, silkflower, mask[0], mask[1], mask[2], gold[0], gold[1], gold[2], boreas[0]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=hydro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=hydro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=xingqiu_autoattack[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				xingqiu_autoattack_data(embed)
			if autoattack_page_index == 2:
				xingqiu_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{xingqiu_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=hydro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=xingqiu_skill[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				xingqiu_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{xingqiu_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=hydro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=xingqiu_burst[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				xingqiu_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{xingqiu_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=hydro[1])
      
			cons_field = [xingqiu_cons[0], xingqiu_cons[6], xingqiu_cons[2], xingqiu_cons[8], xingqiu_cons[4], xingqiu_cons[10], xingqiu_cons[1], xingqiu_cons[7], xingqiu_cons[3], xingqiu_cons[9], xingqiu_cons[5], xingqiu_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{xingqiu_cons[12]}`", value=f"{xingqiu_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xingqiu_cons[14]}`", value=f"{xingqiu_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xingqiu_cons[16]}`", value=f"{xingqiu_cons[17]}", inline=False)
			return embed

	elif char_name == "mona":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Mona Megistus", five[0], hydro[0], catalyst_icon]
		char_desc = "A mysterious young astrologer who proclaims herself to be \"Astrologist Mona Megistus,\" and who possesses abilities to match the title. Erudite, but prideful."
		char_img = ["https://i.imgur.com/capIKOw.png", "https://i.imgur.com/njbntrZ.png", "https://i.imgur.com/1gR9o6Y.png", "https://i.imgur.com/Cq6rhzB.png", "https://i.imgur.com/YNiOt4F.png"]

		profile_data = ["Astral Reflection", "Hexenzirkel", "August 31", "Astrolabos", "Felecia Angelle", "Tingting Chen (陈婷婷)", "Konomi Kohara (小原好美)", "Woo Jeong-sin (우정신)"]
		stats_data = ["810 → 10409", "22 → 287", "51 → 653", "• ER%: 0.0% → 32.0%", "5.0%", "50.0"]
		ascension_data = [hydro[2], hydro[3], hydro[4], hydro[5], oceanid, philanemo, nectar[0], nectar[1], nectar[2], resistance[0], resistance[1], resistance[2], boreas[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=hydro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=hydro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=mona_autoattack[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				mona_autoattack_data(embed)
			if autoattack_page_index == 2:
				mona_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{mona_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=hydro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=mona_skill[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				mona_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{mona_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=hydro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=mona_burst[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				mona_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{mona_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=hydro[1])
      
			cons_field = [mona_cons[0], mona_cons[6], mona_cons[2], mona_cons[8], mona_cons[4], mona_cons[10], mona_cons[1], mona_cons[7], mona_cons[3], mona_cons[9], mona_cons[5], mona_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 0:
				embed.add_field(name=f"<:_:853893900280397854> {mona_cons[18]}", value=f"{mona_cons[19]}", inline=False)
			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{mona_cons[12]}`", value=f"{mona_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{mona_cons[14]}`", value=f"{mona_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{mona_cons[16]}`", value=f"{mona_cons[17]}", inline=False)
			return embed

	elif char_name == "tartaglia" or char_name == "childe" or char_name == "ajax" or char_name == "whale" or char_name == "chiffin" or char_name == "griffin" or char_name == "griffin burns":

		autoattack_page_total = 3
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Tartaglia", five[0], hydro[0], bow_icon]
		char_desc = "No. 11 of The Harbingers, also known as \"Childe.\" His name is highly feared on the battlefield."
		char_img = ["https://i.imgur.com/qpQBYmd.png", "https://i.imgur.com/rPECHHs.png", "https://i.imgur.com/6nDZTyj.png", "https://i.imgur.com/PNJxTha.png", "https://i.imgur.com/rGuFWBZ.png"]

		profile_data = ["Childe", "Fatui", "July 20", "Monoceros Caeli", "Griffin Burns", "Yudong (鱼冻)", "Ryōhei Kimura (木村良平)", "Nam Doh-hyeong (남도형)"]
		stats_data = ["1020 → 13103", "23 → 301", "63 → 815", "• Hydro DMG%: 0.0% → 28.8%", "5.0%", "50.0"]
		ascension_data = [hydro[2], hydro[3], hydro[4], hydro[5], oceanid, starconch, fatui_insignia[0], fatui_insignia[1], fatui_insignia[2], freedom[0], freedom[1], freedom[2], childe[1]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=hydro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=hydro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=tartaglia_autoattack[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")
				
			if autoattack_page_index == 1:
				tartaglia_autoattack_data(embed)
			if autoattack_page_index == 2:
				tartaglia_autoattack_data2(embed)
			if autoattack_page_index == 3:
				tartaglia_autoattack_data3(embed)

			embed.set_author(name=f"{char_talent[0]}{tartaglia_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=hydro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=tartaglia_skill[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				tartaglia_skill_data(embed)
			if skill_page_index == 2:
				tartaglia_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{tartaglia_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=hydro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=tartaglia_burst[1], color=hydro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				tartaglia_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{tartaglia_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=hydro[1])
      
			cons_field = [tartaglia_cons[0], tartaglia_cons[6], tartaglia_cons[2], tartaglia_cons[8], tartaglia_cons[4], tartaglia_cons[10], tartaglia_cons[1], tartaglia_cons[7], tartaglia_cons[3], tartaglia_cons[9], tartaglia_cons[5], tartaglia_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{tartaglia_cons[12]}`", value=f"{tartaglia_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{tartaglia_cons[14]}`", value=f"{tartaglia_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{tartaglia_cons[16]}`", value=f"{tartaglia_cons[17]}", inline=False)
			return embed

	elif char_name == "amber":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Amber", four[0], pyro[0], bow_icon]
		char_desc = "Always energetic and full of life, Amber's the best - albeit only - Outrider of the Knights of Favonius."
		char_img = ["https://i.imgur.com/q1qRaVY.png", "https://i.imgur.com/EOQdjp4.png", "https://i.imgur.com/v6QIvsX.png", "https://i.imgur.com/DmEIcvt.png", "https://i.imgur.com/TZLlZ7C.png"]

		profile_data = ["Gliding Champion", "Knights of Favonius", "August 10", "Lepus", "Kelly Baskin", "Shujin Cai (蔡书瑾)", "Manaka Iwami (石見舞菜香)", "Kim Yeon-woo (김연우)"]
		stats_data = ["793 → 9461", "19 → 223", "50 → 601", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, lampgrass, arrowhead[0], arrowhead[1], arrowhead[2], freedom[0], freedom[1], freedom[2], dvalin[2]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=amber_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				amber_autoattack_data(embed)
			if autoattack_page_index == 2:
				amber_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{amber_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=amber_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				amber_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{amber_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=amber_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				amber_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{amber_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [amber_cons[0], amber_cons[6], amber_cons[2], amber_cons[8], amber_cons[4], amber_cons[10], amber_cons[1], amber_cons[7], amber_cons[3], amber_cons[9], amber_cons[5], amber_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{amber_cons[12]}`", value=f"{amber_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{amber_cons[14]}`", value=f"{amber_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{amber_cons[16]}`", value=f"{amber_cons[17]}", inline=False)
			return embed

	elif char_name == "bennett" or char_name == "benny":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Bennett", four[0], pyro[0], sword_icon]
		char_desc = "A righteous and good-natured adventurer from Mondstadt who's unfortunately extremely unlucky."
		char_img = ["https://i.imgur.com/aenmZTm.png", "https://i.imgur.com/SDztWgj.png", "https://i.imgur.com/w57uNgu.png", "https://i.imgur.com/mK0mbet.png", "https://i.imgur.com/0tuR99J.png"]

		profile_data = ["Trial by Fire", "Adventurers\' Guild", "February 29", "Rota Calamitas", "Cristina Vee Valenzuela", "Xueting Mu (穆雪婷)", "Ryōta Ōsaka (逢坂良太)", "Song Ha-rim (송하림)"]
		stats_data = ["1039 → 12397", "16 → 191", "65 → 771", "• ER%: 0.0% → 26.7%", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, aster, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], resistance[0], resistance[1], resistance[2], dvalin[0]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=bennett_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				bennett_autoattack_data(embed)
			if autoattack_page_index == 2:
				bennett_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{bennett_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=bennett_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				bennett_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{bennett_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=bennett_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				bennett_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{bennett_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [bennett_cons[0], bennett_cons[6], bennett_cons[2], bennett_cons[8], bennett_cons[4], bennett_cons[10], bennett_cons[1], bennett_cons[7], bennett_cons[3], bennett_cons[9], bennett_cons[5], bennett_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{bennett_cons[12]}`", value=f"{bennett_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{bennett_cons[14]}`", value=f"{bennett_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{bennett_cons[16]}`", value=f"{bennett_cons[17]}", inline=False)
			return embed

	elif char_name == "xiangling" or char_name == "xl" or char_name == "chef" or char_name == "guoba":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 2

		char_data = ["Xiangling", four[0], pyro[0], polearm_icon]
		char_desc = "A renowned chef from Liyue. She's extremely passionate about cooking and excels at making her signature hot and spicy dishes."
		char_img = ["https://i.imgur.com/sPinxfS.png", "https://i.imgur.com/DSif2nx.png", "https://i.imgur.com/TG98HZz.png", "https://i.imgur.com/VKqrTP5.png", "https://i.imgur.com/OEVs7rU.png"]

		profile_data = ["Exquisite Delicacy", "Wanmin Restaurant", "November 02", "Trulla", "Jackie Lastra", "Xiao N (小N)", "Ari Ozawa (小澤亜李)", "Yun A-yeong (윤아영)"]
		stats_data = ["912 → 10875", "19 → 225", "56 → 669", "• EM: 0.0 → 96.0", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, jueyunchili, slime[0], slime[1], slime[2], diligence[0], diligence[1], diligence[2], dvalin[1]]

		def char_profile():		
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=xiangling_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				xiangling_autoattack_data(embed)
			if autoattack_page_index == 2:
				xiangling_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{xiangling_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=xiangling_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				xiangling_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{xiangling_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=xiangling_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				xiangling_burst_data(embed)
			if burst_page_index == 2:
				xiangling_burst_data2(embed)

			embed.set_author(name=f"{char_talent[2]}{xiangling_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [xiangling_cons[0], xiangling_cons[6], xiangling_cons[2], xiangling_cons[8], xiangling_cons[4], xiangling_cons[10], xiangling_cons[1], xiangling_cons[7], xiangling_cons[3], xiangling_cons[9], xiangling_cons[5], xiangling_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{xiangling_cons[12]}`", value=f"{xiangling_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xiangling_cons[14]}`", value=f"{xiangling_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xiangling_cons[16]}`", value=f"{xiangling_cons[17]}", inline=False)
			return embed

	elif char_name == "xinyan":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Xinyan", four[0], pyro[0], claymore_icon]
		char_desc = "Liyue's sole rock 'n' roll musician. She rebels against ossified prejudices using her music and passionate singing."
		char_img = ["https://i.imgur.com/hABS68y.png", "https://i.imgur.com/xzJ5Ruj.png", "https://i.imgur.com/tUq3rNU.png", "https://i.imgur.com/fQoqGQq.png", "https://i.imgur.com/2iv1ofw.png"]

		profile_data = ["Blazing Riff", "Liyue Harbor", "October 16", "Fila Ignium", "Laura Stahl", "Yaxin Wang (王雅欣)", "Chiaki Takahashi (たかはし智秋)", "Kim Chae-ha (김채하)"]
		stats_data = ["939 → 11201", "21 → 249", "67 → 799", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, violetgrass, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], gold[0], gold[1], gold[2], childe[0]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=xinyan_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				xinyan_autoattack_data(embed)
			if autoattack_page_index == 2:
				xinyan_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{xinyan_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=xinyan_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				xinyan_skill_data(embed)
			if skill_page_index == 2:
				xinyan_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{xinyan_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=xinyan_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				xinyan_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{xinyan_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [xinyan_cons[0], xinyan_cons[6], xinyan_cons[2], xinyan_cons[8], xinyan_cons[4], xinyan_cons[10], xinyan_cons[1], xinyan_cons[7], xinyan_cons[3], xinyan_cons[9], xinyan_cons[5], xinyan_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{xinyan_cons[12]}`", value=f"{xinyan_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xinyan_cons[14]}`", value=f"{xinyan_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{xinyan_cons[16]}`", value=f"{xinyan_cons[17]}", inline=False)
			return embed

	elif char_name == "yanfei" or char_name == "feiyan" or char_name == "law":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Yanfei", four[0], pyro[0], catalyst_icon]
		char_desc = "A well-known legal adviser active in Liyue Harbor. A brilliant young lady in whose veins runs the blood of an illuminated beast."
		char_img = ["https://i.imgur.com/Hqe6kC8.png", "https://i.imgur.com/YZm4uHa.png", "https://i.imgur.com/l30tCiH.png", "https://i.imgur.com/wG3sS61.png", "https://i.imgur.com/GDvifeM.png"]

		profile_data = ["Wise Innocence", "Liyue Harbor", "July 28", "Bestia Iustitia", "Lizzie Freeman", "Ziwu Su (苏子芜)", "Yumiri Hanamori (花守 ゆみり)", "Cho Kyung-yi (조경이)"]
		stats_data = ["784 → 9352", "20 → 240", "49 → 587", "• Pyro DMG%: 0.0% → 24.0%", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], geovishap, nocjade, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], gold[0], gold[1], gold[2], azhdaha[1]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=yanfei_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")				
			if autoattack_page_index == 1:
				yanfei_autoattack_data(embed)
			if autoattack_page_index == 2:
				yanfei_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{yanfei_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=yanfei_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				yanfei_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{yanfei_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=yanfei_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				yanfei_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{yanfei_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [yanfei_cons[0], yanfei_cons[6], yanfei_cons[2], yanfei_cons[8], yanfei_cons[4], yanfei_cons[10], yanfei_cons[1], yanfei_cons[7], yanfei_cons[3], yanfei_cons[9], yanfei_cons[5], yanfei_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{yanfei_cons[12]}`", value=f"{yanfei_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{yanfei_cons[14]}`", value=f"{yanfei_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{yanfei_cons[16]}`", value=f"{yanfei_cons[17]}", inline=False)
			return embed

	elif char_name == "diluc":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Diluc Ragnvindr", five[0], pyro[0], claymore_icon]
		char_desc = "The tycoon of a winery empire in Mondstadt, unmatched in every possible way."
		char_img = ["https://i.imgur.com/g0I1YpW.png", "https://i.imgur.com/eWQUhOV.png", "https://i.imgur.com/tUq3rNU.png", "https://i.imgur.com/zT6GTDk.png", "https://i.imgur.com/fXSIATt.png"]

		profile_data = ["The Dark Side of Dawn", "Dawn Winery", "April 30", "Noctua", "Sean Chiplock", "Yang Ma (马洋)", "Kensho Ono (小野賢章)", "Choi Seung-hoon (최승훈)"]
		stats_data = ["1011 → 12981", "26 → 335", "61 → 784", "_ _", "5.0% → 24.2%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, lampgrass, fatui_insignia[0], fatui_insignia[1], fatui_insignia[2], resistance[0], resistance[1], resistance[2], dvalin[0]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=diluc_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				diluc_autoattack_data(embed)
			if autoattack_page_index == 2:
				diluc_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{diluc_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=diluc_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				diluc_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{diluc_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=diluc_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				diluc_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{diluc_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [diluc_cons[0], diluc_cons[6], diluc_cons[2], diluc_cons[8], diluc_cons[4], diluc_cons[10], diluc_cons[1], diluc_cons[7], diluc_cons[3], diluc_cons[9], diluc_cons[5], diluc_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{diluc_cons[12]}`", value=f"{diluc_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{diluc_cons[14]}`", value=f"{diluc_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{diluc_cons[16]}`", value=f"{diluc_cons[17]}", inline=False)
			return embed

	elif char_name == "klee" or char_name == "bomb":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Klee", five[0], pyro[0], catalyst_icon]
		char_desc = "An explosives expert and a regular at the Knights of Favonius' confinement room. Also known as Fleeing Sunlight."
		char_img = ["https://i.imgur.com/OhyHeJC.png", "https://i.imgur.com/Ohy84J2.png", "https://i.imgur.com/l30tCiH.png", "https://i.imgur.com/6cgWPvR.png", "https://i.imgur.com/ern3XCE.png"]

		profile_data = ["Fleeing Sunlight", "Knights of Favonius", "July 27", "Trifolium", "Poonam Basu", "Hualing (花玲)", "Misaki Kuno (久野美咲)", "Bang Yeon-ji (방연지)"]
		stats_data = ["801 → 10287", "24 → 311", "48 → 615", "• Pyro DMG%: 0.0% → 28.8%", "5.0%", "50.0"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_regis, philanemo, scroll[0], scroll[1], scroll[2], freedom[0], freedom[1], freedom[2], boreas[1]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=klee_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				klee_autoattack_data(embed)
			if autoattack_page_index == 2:
				klee_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{klee_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=klee_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				klee_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{klee_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=klee_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				klee_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{klee_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [klee_cons[0], klee_cons[6], klee_cons[2], klee_cons[8], klee_cons[4], klee_cons[10], klee_cons[1], klee_cons[7], klee_cons[3], klee_cons[9], klee_cons[5], klee_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{klee_cons[12]}`", value=f"{klee_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{klee_cons[14]}`", value=f"{klee_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{klee_cons[16]}`", value=f"{klee_cons[17]}", inline=False)
			return embed

	elif char_name == "hu tao" or char_name == "hutao" or char_name == "hu":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Hu Tao", five[0], pyro[0], polearm_icon]
		char_desc = "The 77th Director of the Wangsheng Funeral Parlor. She took over the business at a rather young age."
		char_img = ["https://i.imgur.com/tyZC2N8.png", "https://i.imgur.com/A1CEa0j.png", "https://i.imgur.com/TG98HZz.png", "https://i.imgur.com/yXOQkCq.png", "https://i.imgur.com/AX6edp5.png"]

		profile_data = ["Fragrance in Thaw", "Wangsheng Funeral Parlor", "July 15", "Papilio Charontis", "Brianna Knickerbocker", "Dian Tao (陶典)", "Rie Takahashi (高橋李依)", "Kim Ha-ru (김하루)"]
		stats_data = ["1211 → 15552", "8 → 106", "68 → 876", "_ _", "5.0%", "50.0% → 88.4%"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], geovishap, silkflower, nectar[0], nectar[1], nectar[2], diligence[0], diligence[1], diligence[2], childe[1]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=hutao_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				hutao_autoattack_data(embed)
			if autoattack_page_index == 2:
				hutao_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{hutao_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=hutao_skill[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				hutao_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{hutao_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=hutao_burst[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				hutao_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{hutao_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [hutao_cons[0], hutao_cons[6], hutao_cons[2], hutao_cons[8], hutao_cons[4], hutao_cons[10], hutao_cons[1], hutao_cons[7], hutao_cons[3], hutao_cons[9], hutao_cons[5], hutao_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{hutao_cons[12]}`", value=f"{hutao_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{hutao_cons[14]}`", value=f"{hutao_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{hutao_cons[16]}`", value=f"{hutao_cons[17]}", inline=False)
			return embed

	elif char_name == "yoimiya":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Yoimiya", five[0], pyro[0], bow_icon]
		char_desc = "Owner of Naganohara Fireworks. Known as \"Queen of the Summer Festival,\" she excels in her craft of creating fireworks that symbolize people\'s hopes and dreams."
		char_img = ["https://i.imgur.com/pvJcXZU.png", "https://i.imgur.com/UmLkMYn.png", "https://i.imgur.com/v6QIvsX.png"]

		profile_data = ["_ _", "_ _", "June 21", "_ _", "_ _", "_ _", "_ _", "_ _"]
		stats_data = ["791 → 10164", "25 → 323", "48 → 615", "_ _", "5.0% → 24.2%", "50.0%"]
		ascension_data = [pyro[2], pyro[3], pyro[4], pyro[5], pyro_hypo, local3, scroll[0], scroll[1], scroll[2], talent3[0], talent3[1], talent3[2], azhdaha[2]]

		def char_profile():			
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=pyro[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=pyro[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=yoimiya_autoattack[1], color=pyro[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				yoimiya_autoattack_data(embed)
			if autoattack_page_index == 2:
				yoimiya_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{yoimiya_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=pyro[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=yoimiya_skill[1], color=pyro[1])
		#		embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				yoimiya_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{yoimiya_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=pyro[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=yoimiya_burst[1], color=pyro[1])
		#		embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				yoimiya_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{yoimiya_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed						

		def char_cons():
			embed = discord.Embed(color=pyro[1])
      
			cons_field = [yoimiya_cons[0], yoimiya_cons[6], yoimiya_cons[2], yoimiya_cons[8], yoimiya_cons[4], yoimiya_cons[10], yoimiya_cons[1], yoimiya_cons[7], yoimiya_cons[3], yoimiya_cons[9], yoimiya_cons[5], yoimiya_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{yoimiya_cons[12]}`", value=f"{yoimiya_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{yoimiya_cons[14]}`", value=f"{yoimiya_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{yoimiya_cons[16]}`", value=f"{yoimiya_cons[17]}", inline=False)
			return embed

	elif char_name == "kaeya" or char_name == "kayak":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Kaeya Alberich", four[0], cryo[0], sword_icon]
		char_desc = "An accomplished swordsman and a strategic thinker in the Knights of Favonius, rumored to hail from beyond Mondstadt."
		char_img = ["https://i.imgur.com/yM8bDBt.png", "https://i.imgur.com/sNB6OXX.png", "https://i.imgur.com/U12YXD1.png", "https://i.imgur.com/toA2IGG.png", "https://i.imgur.com/WxQCxjV.png"]

		profile_data = ["Frostwind Swordsman", "Knights of Favonius", "November 30", "Pavo Ocellus", "Josey Montana McCoy", "Ye Sun (孙晔)", "Kohsuke Toriumi (鳥海浩輔)", "Jeong Joo-won (정주원)"]
		stats_data = ["976 → 11636", "19 → 223", "66 → 792", "• ER%: 0.0% → 26.7%", "5.0%", "50.0%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, callalily, hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2], ballad[0], ballad[1], ballad[2], boreas[2]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=kaeya_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")		
			if autoattack_page_index == 1:
				kaeya_autoattack_data(embed)
			if autoattack_page_index == 2:
				kaeya_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{kaeya_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=kaeya_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				kaeya_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{kaeya_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=kaeya_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				kaeya_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{kaeya_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [kaeya_cons[0], kaeya_cons[6], kaeya_cons[2], kaeya_cons[8], kaeya_cons[4], kaeya_cons[10], kaeya_cons[1], kaeya_cons[7], kaeya_cons[3], kaeya_cons[9], kaeya_cons[5], kaeya_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{kaeya_cons[12]}`", value=f"{kaeya_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{kaeya_cons[14]}`", value=f"{kaeya_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{kaeya_cons[16]}`", value=f"{kaeya_cons[17]}", inline=False)
			return embed

	elif char_name == "diona":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Diona", four[0], cryo[0], bow_icon]
		char_desc = "A young lady who has inherited trace amounts of non-human blood. She is the incredible popular bartender of the Cat's Tail tavern."
		char_img = ["https://i.imgur.com/0XXZvIK.png", "https://i.imgur.com/dpgYSxX.png", "https://i.imgur.com/5wvoSzD.png", "https://i.imgur.com/C7Tu9uH.png", "https://i.imgur.com/ULv3WWB.png"]

		profile_data = ["Kätzlein Cocktail", "Cat\'s Tail Tavern", "January 18", "Feles", "Dina Sherman", "Nuoya (诺亚)", "Shiori Izawa (井澤詩織)", "Woo Jeong-sin (우정신)"]
		stats_data = ["802 → 9570", "18 → 212", "50 → 601", "• Cryo DMG%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, callalily, arrowhead[0], arrowhead[1], arrowhead[2], freedom[0], freedom[1], freedom[2], childe[1]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=diona_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")
			if autoattack_page_index == 1:
				diona_autoattack_data(embed)
			if autoattack_page_index == 2:
				diona_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{diona_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=diona_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				diona_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{diona_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=diona_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				diona_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{diona_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [diona_cons[0], diona_cons[6], diona_cons[2], diona_cons[8], diona_cons[4], diona_cons[10], diona_cons[1], diona_cons[7], diona_cons[3], diona_cons[9], diona_cons[5], diona_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{diona_cons[12]}`", value=f"{diona_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{diona_cons[14]}`", value=f"{diona_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{diona_cons[16]}`", value=f"{diona_cons[17]}", inline=False)
			return embed

	elif char_name == "rosaria":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Rosaria", four[0], cryo[0], polearm_icon]
		char_desc = "A sister of the church, though you wouldn't know it if it weren't for her attire. Known for her sharp, cold words and manner, she often works alone."
		char_img = ["https://i.imgur.com/pZFgjLg.png", "https://i.imgur.com/93SZhAm.png", "https://i.imgur.com/bKESx3I.png", "https://i.imgur.com/goqv3eM.png", "https://i.imgur.com/pR0LugA.png"]

		profile_data = ["Thorny Benevolence", "Church of Favonius", "January 24", "Spinea Corona", "Elizabeth Maxwell", "Anqi Zhang (张安琪)", "Ai Kakuma (加隈亜衣)", "Kim Bo-na (김보나)"]
		stats_data = ["1030 → 12289", "20 → 240", "60 → 710", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, valberry, fatui_insignia[0], fatui_insignia[1], fatui_insignia[2], ballad[0], ballad[1], ballad[2], childe[2]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=rosaria_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")
			if autoattack_page_index == 1:
				rosaria_autoattack_data(embed)
			if autoattack_page_index == 2:
				rosaria_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{rosaria_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=rosaria_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				rosaria_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{rosaria_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=rosaria_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				rosaria_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{rosaria_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [rosaria_cons[0], rosaria_cons[6], rosaria_cons[2], rosaria_cons[8], rosaria_cons[4], rosaria_cons[10], rosaria_cons[1], rosaria_cons[7], rosaria_cons[3], rosaria_cons[9], rosaria_cons[5], rosaria_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{rosaria_cons[12]}`", value=f"{rosaria_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{rosaria_cons[14]}`", value=f"{rosaria_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{rosaria_cons[16]}`", value=f"{rosaria_cons[17]}", inline=False)
			return embed

	elif char_name == "chongyun" or char_name == "chong" or char_name == "chongus":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Chongyun", four[0], cryo[0], claymore_icon]
		char_desc = "A young exorcist from a family of exorcists. He does everything he can to suppress his abundance of yang energy."
		char_img = ["https://i.imgur.com/7N1RCfq.png", "https://i.imgur.com/L9XLmVN.png", "https://i.imgur.com/nHv2qPV.png", "https://i.imgur.com/ro4me7D.png", "https://i.imgur.com/oPijKDh.png"]

		profile_data = ["Frozen Ardor", "Liyue Harbor", "September 07", "Nubis Caesor", "Beau Bridgland", "kinsen", "Soma Saito (斉藤壮馬)", "Yang Jeong-hwa (양정화)"]
		stats_data = ["921 → 10894", "19 → 223", "54 → 648", "• ATK%: 0.0% → 24.0%", "5.0%", "50.0%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, corlapis, mask[0], mask[1], mask[2], diligence[0], diligence[1], diligence[2], dvalin[2]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=chongyun_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")		
			if autoattack_page_index == 1:
				chongyun_autoattack_data(embed)
			if autoattack_page_index == 2:
				chongyun_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{chongyun_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=chongyun_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				chongyun_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{chongyun_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=chongyun_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				chongyun_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{chongyun_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [chongyun_cons[0], chongyun_cons[6], chongyun_cons[2], chongyun_cons[8], chongyun_cons[4], chongyun_cons[10], chongyun_cons[1], chongyun_cons[7], chongyun_cons[3], chongyun_cons[9], chongyun_cons[5], chongyun_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{four[1]} `{chongyun_cons[12]}`", value=f"{chongyun_cons[13]}", inline=False)
				embed.add_field(name=f"{four[1]} `{chongyun_cons[14]}`", value=f"{chongyun_cons[15]}", inline=False)
				embed.add_field(name=f"{four[1]} `{chongyun_cons[16]}`", value=f"{chongyun_cons[17]}", inline=False)
			return embed

	elif char_name == "qiqi" or char_name == "zombie":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Qiqi", five[0], cryo[0], sword_icon]
		char_desc = "An apprentice and herb-picker at Bubu Pharmacy. An undead with a bone-white complexion, she seldom has much in the way of words or emotion."
		char_img = ["https://i.imgur.com/b2CGkYF.png", "https://i.imgur.com/yWLbcUV.png", "https://i.imgur.com/U12YXD1.png", "https://i.imgur.com/BiGdG0b.png", "https://i.imgur.com/ZFwNgUC.png"]

		profile_data = ["Icy Resurrection", "Bubu Pharmacy", "March 03", "Pristina Nola", "Christie Cate", "Yanning (宴宁)", "Yukari Tamura (田村ゆかり)", "Lee Seul (이슬)"]
		stats_data = ["963 → 12368", "22 → 287", "72 → 922", "• Healing%: 0.0% → 22.2%", "5.0%", "50.0%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, violetgrass, scroll[0], scroll[1], scroll[2], prosperity[0], prosperity[1], prosperity[2], boreas[0]]

		def char_profile():	
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=qiqi_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				qiqi_autoattack_data(embed)
			if autoattack_page_index == 2:
				qiqi_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{qiqi_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=qiqi_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				qiqi_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{qiqi_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=qiqi_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				qiqi_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{qiqi_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [qiqi_cons[0], qiqi_cons[6], qiqi_cons[2], qiqi_cons[8], qiqi_cons[4], qiqi_cons[10], qiqi_cons[1], qiqi_cons[7], qiqi_cons[3], qiqi_cons[9], qiqi_cons[5], qiqi_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{qiqi_cons[12]}`", value=f"{qiqi_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{qiqi_cons[14]}`", value=f"{qiqi_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{qiqi_cons[16]}`", value=f"{qiqi_cons[17]}", inline=False)
			return embed

	elif char_name == "ganyu" or char_name == "cocogoat":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Ganyu", five[0], cryo[0], bow_icon]
		char_desc = "The secretary at Yuehai Pavilion. The blood of the qilin, an illuminated beast, flows within her veins."
		char_img = ["https://i.imgur.com/uQQRiNS.png", "https://i.imgur.com/P2jPrX9.png", "https://i.imgur.com/uvWgamo.png", "https://i.imgur.com/ZvhjFnQ.png", "https://i.imgur.com/GFlB97G.png"]

		profile_data = ["Plenilune Gaze", "Yuehai Pavilion", "December 02", "Sinae Unicornis", "Jennifer Losi", "Su Lin (林簌)", "Reina Ueda (上田麗奈)", "Kim Sun-hye (김선혜)"]
		stats_data = ["763 → 9797", "26 → 335", "49 → 630", "_ _", "5.0%", "50.0% → 88.4%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_regis, qingxin, nectar[0], nectar[1], nectar[2], diligence[0], diligence[1], diligence[2], childe[2]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=ganyu_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				ganyu_autoattack_data(embed)
			if autoattack_page_index == 2:
				ganyu_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{ganyu_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=ganyu_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				ganyu_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{ganyu_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=ganyu_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				ganyu_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{ganyu_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed	

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [ganyu_cons[0], ganyu_cons[6], ganyu_cons[2], ganyu_cons[8], ganyu_cons[4], ganyu_cons[10], ganyu_cons[1], ganyu_cons[7], ganyu_cons[3], ganyu_cons[9], ganyu_cons[5], ganyu_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{ganyu_cons[12]}`", value=f"{ganyu_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{ganyu_cons[14]}`", value=f"{ganyu_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{ganyu_cons[16]}`", value=f"{ganyu_cons[17]}", inline=False)
			return embed

	elif char_name == "eula" or char_name == "awooga":

		autoattack_page_total = 2
		skill_page_total = 2
		burst_page_total = 1

		char_data = ["Eula Lawrence", five[0], cryo[0], claymore_icon]
		char_desc = "The Spindrift Knight, a scion of the old aristocracy, and the Captain of the Knights of Favonius Reconnaissance Company. The reason for which a descendant of the ancient nobles might join the Knights remains a great mystery in Mondstadt to this very day."
		char_img = ["https://i.imgur.com/Duy8Aek.png", "https://i.imgur.com/jtZNE93.png", "https://i.imgur.com/nHv2qPV.png", "https://i.imgur.com/sV7sz8A.png", "https://i.imgur.com/F6duHFC.png"]

		profile_data = ["Dance of the Shimmering Wave", "Knights of Favonius", "October 25", "Aphros Delos", "Suzie Yeung", "Ziyin (子音)", "Rina Sato (佐藤利奈)", "Kim Hyeon-ji (김현지)"]
		stats_data = ["1030 → 13226", "27 → 342", "58 → 751", "_ _", "5.0%", "50.0% → 88.4%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], cryo_hypo, dandelion, mask[0], mask[1], mask[2], resistance[0], resistance[1], resistance[2], azhdaha[0]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=eula_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")			
			if autoattack_page_index == 1:
				eula_autoattack_data(embed)
			if autoattack_page_index == 2:
				eula_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{eula_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=eula_skill[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				eula_skill_data(embed)
			if skill_page_index == 2:
				eula_skill_data2(embed)

			embed.set_author(name=f"{char_talent[1]}{eula_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=eula_burst[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				eula_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{eula_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed			

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [eula_cons[0], eula_cons[6], eula_cons[2], eula_cons[8], eula_cons[4], eula_cons[10], eula_cons[1], eula_cons[7], eula_cons[3], eula_cons[9], eula_cons[5], eula_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{eula_cons[12]}`", value=f"{eula_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{eula_cons[14]}`", value=f"{eula_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{eula_cons[16]}`", value=f"{eula_cons[17]}", inline=False)
			return embed

	elif char_name == "ayaka":

		autoattack_page_total = 2
		skill_page_total = 1
		burst_page_total = 1

		char_data = ["Kamisato Ayaka", five[0], cryo[0], sword_icon]
		char_desc = "Daughter of the Yashiro Commision\'s Kamisato Clan. Dignified and elegant, as well as wise and strong."
		char_img = ["https://i.imgur.com/i7rePhr.png", "https://i.imgur.com/oupYFB9.png", "https://i.imgur.com/U12YXD1.png"]

		profile_data = ["_ _", "_ _", "September 28", "_ _", "_ _", "_ _", "_ _", "_ _"]
		stats_data = ["1001 → 12858", "27 → 342", "61 → 784", "_ _", "5.0%", "50.0% → 88.4%"]
		ascension_data = [cryo[2], cryo[3], cryo[4], cryo[5], boss1, local1, common1[0], common1[1], common1[2], talent1[0], talent1[1], talent1[2], azhdaha[1]]

		def char_profile():
			embed = discord.Embed(description=f"**{char_data[0]}**\n{char_data[1]} | {char_data[2]} | ​{char_data[3]}\n{char_desc}", color=cryo[1])

			profile_value = [info_field1(profile_data), ascension_field1(ascension_data), info_field2(profile_data), ascension_field2(ascension_data), info_field3(stats_data), ascension_field3(ascension_data), info_field4(stats_data), ascension_field4(ascension_data)]
			
			info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total)

			if profile_page_index == 0:
				embed.set_thumbnail(url=f"{char_img[0]}")
			return embed

		def char_autoattack():			
			embed = discord.Embed(color=cryo[1])

			if autoattack_page_index == 0:
				embed = discord.Embed(description=ayaka_autoattack[1], color=cryo[1])
				embed.set_thumbnail(url=f"{char_img[2]}")		
			if autoattack_page_index == 1:
				ayaka_autoattack_data(embed)
			if autoattack_page_index == 2:
				ayaka_autoattack_data2(embed)

			embed.set_author(name=f"{char_talent[0]}{ayaka_autoattack[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {autoattack_page_index+1}/{autoattack_page_total+1}")
			return embed

		def char_skill():
			embed = discord.Embed(color=cryo[1])

			if skill_page_index == 0:
				embed = discord.Embed(description=ayaka_skill[1], color=cryo[1])
		#		embed.set_thumbnail(url=f"{char_img[3]}")
			if skill_page_index == 1:
				ayaka_skill_data(embed)

			embed.set_author(name=f"{char_talent[1]}{ayaka_skill[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {skill_page_index+1}/{skill_page_total+1}")
			return embed

		def char_burst():
			embed = discord.Embed(color=cryo[1])

			if burst_page_index == 0:
				embed = discord.Embed(description=ayaka_burst[1], color=cryo[1])
		#		embed.set_thumbnail(url=f"{char_img[4]}")
			if burst_page_index == 1:
				ayaka_burst_data(embed)

			embed.set_author(name=f"{char_talent[2]}{ayaka_burst[0]}", icon_url=f"{char_img[1]}")
			embed.set_footer(text=f"Page {burst_page_index+1}/{burst_page_total+1}")
			return embed	

		def char_cons():
			embed = discord.Embed(color=cryo[1])
      
			cons_field = [ayaka_cons[0], ayaka_cons[6], ayaka_cons[2], ayaka_cons[8], ayaka_cons[4], ayaka_cons[10], ayaka_cons[1], ayaka_cons[7], ayaka_cons[3], ayaka_cons[9], ayaka_cons[5], ayaka_cons[11]]
			cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img)

			if cons_page_index == 0:
				embed.add_field(name=f"<:_:853893900280397854> {ayaka_cons[18]}", value=f"{ayaka_cons[19]}", inline=False)
			if cons_page_index == 1:
				embed.add_field(name=f"{five[1]} `{ayaka_cons[12]}`", value=f"{ayaka_cons[13]}", inline=False)
				embed.add_field(name=f"{five[1]} `{ayaka_cons[14]}`", value=f"{ayaka_cons[15]}", inline=False)
				embed.add_field(name=f"{five[1]} `{ayaka_cons[16]}`", value=f"{ayaka_cons[17]}", inline=False)
			return embed

	else:
		index = 0
		embed = discord.Embed(description="This character is invalid.", color=color)
		await ctx.send(embed=embed)

	if index != 0: message = await ctx.send(embed=char_profile())

	if index != 0: await message.add_reaction(left)
	if index != 0: await message.add_reaction(right)
	if index != 0: await message.add_reaction(auto)
	if index != 0: await message.add_reaction(skill)
	if index != 0: await message.add_reaction(burst)
	if index != 0: await message.add_reaction(cons)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right, auto, skill, exit, burst, cons] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=120, check=check)
			
			if str(reaction.emoji) == right and profile_page_index != profile_page_total and index == 1:
				profile_page_index += 1
				await message.edit(embed=char_profile())
			
			elif str(reaction.emoji) == left and profile_page_index > 0 and index == 1:
				profile_page_index -= 1
				await message.edit(embed=char_profile())
			
			elif str(reaction.emoji) == right and autoattack_page_index != autoattack_page_total and index == 2:
				autoattack_page_index += 1
				await message.edit(embed=char_autoattack())
			elif str(reaction.emoji) == left and autoattack_page_index > 0 and index == 2:
				autoattack_page_index -= 1
				await message.edit(embed=char_autoattack())

			elif str(reaction.emoji) == right and skill_page_index != skill_page_total and index == 3:
				skill_page_index += 1
				await message.edit(embed=char_skill())
			elif str(reaction.emoji) == left and skill_page_index > 0 and index == 3:
				skill_page_index -= 1
				await message.edit(embed=char_skill())

			elif str(reaction.emoji) == right and burst_page_index != burst_page_total and index == 4:
				burst_page_index += 1
				await message.edit(embed=char_burst())
			elif str(reaction.emoji) == left and burst_page_index > 0 and index == 4:
				burst_page_index -= 1
				await message.edit(embed=char_burst())

			elif str(reaction.emoji) == right and cons_page_index != cons_page_total and index == 5:
				cons_page_index += 1
				await message.edit(embed=char_cons())
			elif str(reaction.emoji) == left and cons_page_index > 0 and index == 5:
				cons_page_index -= 1
				await message.edit(embed=char_cons())

			elif str(reaction.emoji) == exit:
				index = 1
				await message.clear_reactions()
				await message.edit(embed=char_profile())
				await message.add_reaction(left)
				await message.add_reaction(right)
				await message.add_reaction(auto)
				await message.add_reaction(skill)
				await message.add_reaction(burst)
				await message.add_reaction(cons)

			elif str(reaction.emoji) == auto:
				index = 2
				await message.clear_reactions()
				await message.edit(embed=char_autoattack())
				await message.add_reaction(left)
				await message.add_reaction(right)
				await message.add_reaction(exit)

			elif str(reaction.emoji) == skill:
				index = 3
				await message.clear_reactions()
				await message.edit(embed=char_skill())
				await message.add_reaction(left)
				await message.add_reaction(right)
				await message.add_reaction(exit)

			elif str(reaction.emoji) == burst:
				index = 4
				await message.clear_reactions()
				await message.edit(embed=char_burst())
				await message.add_reaction(left)
				await message.add_reaction(right)
				await message.add_reaction(exit)

			elif str(reaction.emoji) == cons:
				index = 5
				await message.clear_reactions()
				await message.edit(embed=char_cons())
				await message.add_reaction(left)
				await message.add_reaction(right)
				await message.add_reaction(exit)

			await message.remove_reaction(reaction, user)

		except asyncio.TimeoutError:
			await message.clear_reactions()
			break

#---------------------------------------
# Weapon Info: Sword
#---------------------------------------
@client.command(aliases=['s'])
async def sword(ctx, *, weap_name):

	weap_name = weap_name.lower()
	
	weap_page_index = 0
	weap_page_total = 1

	if weap_name == "freedom-sworn" or weap_name == "freedom sworn" or weap_name == "freedom" or weap_name == "sworn":
		weap_data = ["Freedom-Sworn", five[0], sword_icon, freedom_sworn, "Revolutionary Chorale", "https://i.imgur.com/MPzGBlC.png"]
		weap_desc = "A straight sword, azure as antediluvian song, and as keen as the oaths of freedom taken in the Land of Wind."
		weap_stats = ["46 → 608", "EM: 43 → 198"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "primordial jade cutter" or weap_name == "jade cutter" or weap_name == "jade sword" or weap_name == "jade":
		weap_data = ["Primordial Jade Cutter", five[0], sword_icon, jade_cutter, "Protector's Virtue", "https://i.imgur.com/amTwWOu.png"]
		weap_desc = "A ceremonial sword masterfully carved from pure jade. There almost seems to be an audible sigh in the wind as it is swung."
		weap_stats = ["44 → 542", "CRIT Rate: 9.6% → 44.1%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "summit shaper" or weap_name == "summit":
		weap_data = ["Summit Shaper", five[0], sword_icon, summit_shaper, "Golden Majesty", "https://i.imgur.com/1Bo7dvX.png"]
		weap_desc = "A symbol of a legendary pact, this sharp blade once cut off the peak of a mountain."
		weap_stats = ["46 → 608", "ATK%: 10.8% → 49.6%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "skyward blade" or weap_name == "skyward sword" or weap_name == "skyward":
		weap_data = ["Skyward Blade", five[0], sword_icon, skyward_blade, "Sky-Piercing Fang", "https://i.imgur.com/ZEEZSHs.png"]
		weap_desc = "The sword of a knight that symbolizes the restored honor of Dvalin. The blessings of the Anemo Archon rest on the fuller of the blade, imbuing the sword with the powers of the sky and the wind."
		weap_stats = ["46 → 608", "ER%: 12.0% → 55.1%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "aquila favonia" or weap_name == "aquila" or weap_name == "favonia":
		weap_data = ["Aquila Favonia", five[0], sword_icon, aquila_favonia, "Falcon's Defiance", "https://i.imgur.com/PDoqGcX.png"]
		weap_desc = "The soul of the Knights of Favonius. Millennia later, it still calls on the winds of swift justice to vanquish all evil—just like the last heroine who wielded it."
		weap_stats = ["48 → 674", "Phys DMG%: 9.0% → 41.3%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "mistsplitter's reflection" or weap_name == "mistsplitter" or weap_name == "reflection" or weap_name == "mist":
		weap_data = ["Mistsplitter's Reflection", five[0], sword_icon, mistsplitter, "Mistsplitter's Sheath", "https://i.imgur.com/z8AO8Vz.png"]
		weap_desc = "A sword that blazes with a fierce violet light. The name \"Reflection\" comes from its once having been broken."
		weap_stats = ["48 → 674", "Crit DMG%: 9.6% → 44.1%"]
		weap_ascension = [ascension1[0], ascension1[1], ascension1[2], ascension1[3], common2[0], common2[1], common2[2], common1[0], common1[1], common1[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "blackcliff longsword" or weap_name == "blackcliff sword" or weap_name == "blackcliff":
		weap_data = ["Blackcliff Longsword", four[0], sword_icon, blackcliff_sword, "Press the Advantage", "https://i.imgur.com/q7dntTu.png"]
		weap_desc = "A sword made of blackstone. It has a dark crimson glow on its black blade."
		weap_stats = ["44 → 565", "Crit DMG%: 8.0% → 36.8%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "favonius sword" or weap_name == "favonius" or weap_name == "fav":
		weap_data = ["Favonius Sword", four[0], sword_icon, fav_sword, "Windfall", "https://i.imgur.com/xybihf7.png"]
		weap_desc = "A standard-issue longsword of the Knights of Favonius. When you're armed with this agile and sharp weapon, channeling the power of the elements has never been so easy!"
		weap_stats = ["41 → 454", "ER%: 13.3% → 61.3%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "iron sting" or weap_name == "iron" or weap_name == "sting":
		weap_data = ["Iron Sting", four[0], sword_icon, iron_sting, "Infusion Stinger", "https://i.imgur.com/ztY31CT.png"]
		weap_desc = "An exotic long-bladed rapier that somehow found its way into Liyue via foreign traders. It is light, agile, and sharp."
		weap_stats = ["42 → 510", "EM: 36 → 165"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], nectar[0], nectar[1], nectar[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {sword_proto} `x01`, {crystal_chunk} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "lion's roar" or weap_name == "lions roar" or weap_name == "lion" or weap_name == "roar":
		weap_data = ["Lion's Roar", four[0], sword_icon, lions_roar, "Bane of Fire and Thunder", "https://i.imgur.com/iqFEgmh.png"]
		weap_desc = "A sharp blade with extravagant carvings that somehow does not compromise on durability and sharpness. It roars like a lion as it cuts through the air."
		weap_stats = ["42 → 510", "ATK%: 9.0% → 41.3%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "prototype rancour" or weap_name == "rancour":
		weap_data = ["Prototype Rancour", four[0], sword_icon, rancour, "Smashed Stone", "https://i.imgur.com/dQ3vWjR.png"]
		weap_desc = "An ancient longsword discovered in the Blackcliff Forge that cuts through rocks like a hot knife through butter."
		weap_stats = ["44 → 565", "Phys DMG%: 7.5% → 34.5%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {sword_proto} `x01`, {crystal_chunk} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "royal longsword" or weap_name == "royal sword" or weap_name == "royal":
		weap_data = ["Royal Longsword", four[0], sword_icon, royal_sword, "Focus", "https://i.imgur.com/u4jme3f.png"]
		weap_desc = "An old longsword that belonged to the erstwhile rulers of Mondstadt. Exquisitely crafted, the carvings and embellishments testify to the stature of its owner."
		weap_stats = ["42 → 510", "ATK%: 9.0% → 41.3%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "sacrificial sword" or weap_name == "sacrificial" or weap_name == "sac sword" or weap_name == "sac":
		weap_data = ["Sacrificial Sword", four[0], sword_icon, sac_sword, "Composed", "https://i.imgur.com/N2btcUA.png"]
		weap_desc = "A ceremonial sword that has become petrified over time. The trinkets on it are still visible. It grants the wielder the power to withstand the winds of time."
		weap_stats = ["41 → 454", "ER%: 13.3% → 61.3%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "the alley flash" or weap_name == "alley flash" or weap_name == "alley" or weap_name == "flash":
		weap_data = ["The Alley Flash", four[0], sword_icon, alley_flash, "Itinerant Hero", "https://i.imgur.com/w01lMEW.png"]
		weap_desc = "A straight sword as black as the night. It once belonged to a thief who roamed the benighted streets."
		weap_stats = ["41 → 454", "ER%: 13.3% → 61.3%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "the black sword" or weap_name == "black sword" or weap_name == "black" or weap_name == "bs":
		weap_data = ["The Black Sword", four[0], sword_icon, black_sword, "Justice", "https://i.imgur.com/RKNrsfM.png"]
		weap_desc = "A pitch-black longsword that thirsts for violence and conflict. It is said that this weapon can cause its user to become drunk on the red wine of slaughter."
		weap_stats = ["42 → 510", "CRIT Rate%: 6.0% → 27.6%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "the flute" or weap_name == "flute":
		weap_data = ["The Flute", four[0], sword_icon, flute, "Chord", "https://i.imgur.com/WTXnxws.png"]
		weap_desc = "Beneath its rusty exterior is a lavishly decorated thin blade. It swings as swiftly as the wind."
		weap_stats = ["42 → 510", "ATK%: 9.0% → 41.3%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "sword of descension" or weap_name == "descension" or weap_name == "ps5" or weap_name == "ps4" or weap_name == "ps":
		weap_data = ["Sword of Descension", four[0], sword_icon, descension, "Descension", "https://i.imgur.com/QBuCqBr.png"]
		weap_desc = "A sword of unique craftsmanship. It does not appear to belong to this world."
		weap_stats = ["39 → 440", "ATK%: 7.7% → 35.2%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "festering desire" or weap_name == "festering" or weap_name == "fester" or weap_name == "desire" or weap_name == "durin":
		weap_data = ["Festering Desire", four[0], sword_icon, festering_desire, "Undying Admiration", "https://i.imgur.com/IfQNc5R.png"]
		weap_desc = "A creepy straight sword that almost seems to yearn for life. It drips with a shriveling venom that could even corrupt a mighty dragon."
		weap_stats = ["42 → 510", "ER%: 10.0% → 45.9%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], horn[0], horn[1], horn[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Special Refinement Material", value=f"<:_:854309073804853288>: {event_ref[0]} `x05`", inline=False)
				return embed

	elif weap_name == "amenoma kageuta blade" or weap_name == "amenoma kageuta" or weap_name == "amenoma" or weap_name == "ameno" or weap_name == "kageuta":
		weap_data = ["Amenoma Kageuta Blade", four[0], sword_icon, amenoma_kageuta, "Iwakura Succession", "https://i.imgur.com/t3zAUAE.png"]
		weap_desc = "A blade that was said to have been made to order by a famed samurai who could even cut a tengu warrior, famed for their skill in using their incredible speed, down from the air."
		weap_stats = ["41 → 454", "ATK%: 12.0% → 55.1%"]
		weap_ascension = [ascension1[0], ascension1[1], ascension1[2], ascension1[3], common2[0], common2[1], common2[2], common1[0], common1[1], common1[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {sword_proto} `x01`, {amethyst_lump} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "traveler's handy sword" or weap_name == "travelers handy sword" or weap_name == "traveler handy sword" or weap_name == "handy sword" or weap_name == "handy":
		weap_data = ["Traveler's Handy Sword", three, sword_icon, trav_handy_sword, "Journey", "https://i.imgur.com/TfILFdY.png"]
		weap_desc = "A handy steel sword which contains scissors, a magnifying glass, tinder, and other useful items in its sheath."
		weap_stats = ["40 → 448", "DEF%: 6.4% → 27.5%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "skyrider sword" or weap_name == "skyrider":
		weap_data = ["Skyrider Sword", three, sword_icon, skyrider_sword, "Determination", "https://i.imgur.com/kVK10u4.png"]
		weap_desc = "A reliable steel sword. The legendary Skyrider once tried to ride it as a flying sword..."
		weap_stats = ["38 → 354", "ER%: 11.3% → 51.7%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "harbinger of dawn" or weap_name == "harbinger" or weap_name == "hod":
		weap_data = ["Harbinger of Dawn", three, sword_icon, harbinger_dawn, "Vigorous", "https://i.imgur.com/XTAM0Y2.png"]
		weap_desc = "A sword that once shone like the sun. The wielder of this sword will be blessed with a \"feel-good\" buff. The reflective material on the blade has long worn off."
		weap_stats = ["39 → 401", "CRIT DMG%: 10.2% → 46.9%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "fillet blade" or weap_name == "fillet":
		weap_data = ["Fillet Blade", three, sword_icon, fillet_blade, "Gash", "https://i.imgur.com/6LcOG6l.png"]
		weap_desc = "A sharp filleting knife. The blade is long, thin, and incredibly sharp."
		weap_stats = ["39 → 401", "ATK%: 7.7% → 35.2%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "dark iron sword" or weap_name == "dark iron":
		weap_data = ["Dark Iron Sword", three, sword_icon, dark_iron_sword, "Overloaded", "https://i.imgur.com/PMySIJX.png"]
		weap_desc = "A perfectly ordinary iron sword, just slightly darker than most."
		weap_stats = ["39 → 401", "EM: 31.0 → 141.0"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "cool steel":
		weap_data = ["Cool Steel", three, sword_icon, cool_steel, "Bane of Water and Ice", "https://i.imgur.com/X7tJ5l9.png"]
		weap_desc = "A reliable steel-forged weapon that serves as a testament to the great adventures of its old master."
		weap_stats = ["39 → 401", "ATK%: 7.7% → 35.2%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "silver sword" or weap_name == "silver":
		weap_data = ["Silver Sword", two, sword_icon, no_data, " ", "https://i.imgur.com/ii1tRGX.png"]
		weap_desc = "A sword for chasing away demons. Everyone knows it's made of a silver alloy, not pure silver."
		weap_stats = ["33 → 243", " "]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension2(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "dull blade" or weap_name == "dull":
		weap_data = ["Dull Blade", one, sword_icon, no_data, " ", "https://i.imgur.com/HoMaBQg.png"]
		weap_desc = "Youthful dreams and the thrill of adventure. If this isn't enough, then make it up with valiance."
		weap_stats = ["23 → 185", " "]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension1(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	message = await ctx.send(embed=weap_profile())

	await message.add_reaction(left)
	await message.add_reaction(right)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=120, check=check)
			
			if str(reaction.emoji) == right and weap_page_index != weap_page_total:
				weap_page_index += 1
				await message.edit(embed=weap_profile())
			
			elif str(reaction.emoji) == left and weap_page_index > 0:
				weap_page_index -= 1
				await message.edit(embed=weap_profile())

			await message.remove_reaction(reaction, user)

		except asyncio.TimeoutError:
			await message.clear_reactions()
			break

#---------------------------------------
# Weapon Info: Claymore
#---------------------------------------
@client.command(aliases=['greatsword', 'gs'])
async def claymore(ctx, *, weap_name):

	weap_name = weap_name.lower()
	
	weap_page_index = 0
	weap_page_total = 1

	if weap_name == "song of broken pines" or weap_name == "broken pines" or weap_name == "pines"  or weap_name == "pine" or weap_name == "sbp":
		weap_data = ["Song of Broken Pines", five[0], claymore_icon, broken_pines, "Rebel's Banner Hymn", "https://i.imgur.com/XRwrekK.png"]
		weap_desc = "A greatsword as light as the sigh of grass in the breeze, yet as merciless to the corrupt as a typhoon."
		weap_stats = ["49 → 741", "Phys DMG%: 4.5% → 20.7%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "the unforged" or weap_name == "unforged" or weap_name == "unforge":
		weap_data = ["The Unforged", five[0], claymore_icon, unforged, "Golden Majesty", "https://i.imgur.com/VdmVDta.png"]
		weap_desc = "Capable of driving away evil spirits and wicked people alike, this edgeless claymore seems to possess divine might."
		weap_stats = ["46 → 608", "ATK%: 10.8% → 49.6%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "wolf's gravestone" or weap_name == "wolf" or weap_name == "gravestone" or weap_name == "wgs" or weap_name == "wolf gstone" or weap_name == "gstone" or weap_name == "dogstick" or weap_name == "dog stick":
		weap_data = ["Wolf's Gravestone", five[0], claymore_icon, wgs, "Wolfish Tracker", "https://i.imgur.com/1g4mqjv.png"]
		weap_desc = "A longsword used by the Wolf Knight. Originally just a heavy sheet of iron given to the knight by a blacksmith from the city, it became endowed with legendary power owing to his friendship with the wolves."
		weap_stats = ["46 → 608", "ATK%: 10.8% → 49.6%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "skyward pride" or weap_name == "skyward" or weap_name == "pride":
		weap_data = ["Skyward Pride", five[0], claymore_icon, skyward_pride, "Sky-ripping Dragon Spine", "https://i.imgur.com/qE9PcwS.png"]
		weap_desc = "A claymore that symbolizes the pride of Dvalin soaring through the skies. When swung, it emits a deep hum as the full force of Dvalin's command of the sky and the wind is unleashed."
		weap_stats = ["48 → 674", "ER%: 8.0% → 36.8%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "snow-tombed starsilver" or weap_name == "snow tombed starsilver" or weap_name == "snow tomb starsilver" or weap_name == "snow tombed" or weap_name == "snow tomb" or weap_name == "snow" or weap_name == "tomb" or weap_name == "starsilver" or weap_name == "dragonspine" or weap_name == "dspine":
		weap_data = ["Snow-Tombed Starsilver", four[0], claymore_icon, snow_tomb, "Frost Burial", "https://i.imgur.com/rEV4p1M.png"]
		weap_desc = "An ancient greatsword that was stored between frescoes. Forged from Starsilver, it has the power to cleave through ice and snow."
		weap_stats = ["44 → 565", "Phys DMG%: 7.5% → 34.5%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {claymore_proto} `x01`, {starsilver} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "sacrificial greatsword" or weap_name == "sacrificial gsword" or weap_name == "sac gsword" or weap_name == "sacrificial" or weap_name == "sac":
		weap_data = ["Sacrificial Greatsword", four[0], claymore_icon, sac_gsword, "Composed", "https://i.imgur.com/srAbFvS.png"]
		weap_desc = "A ceremonial greatsword that has become petrified over time. The trinkets on it are still visible. It grants the wielder the power to withstand the winds of time."
		weap_stats = ["44 → 565", "ER%: 6.7% → 30.6%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "whiteblind" or weap_name == "wb":
		weap_data = ["Whiteblind", four[0], claymore_icon, whiteblind, "Infusion Blade", "https://i.imgur.com/4YNKVW1.png"]
		weap_desc = "An exotic sword with one section of the blade left blunt. It made its way into Liyue via the hands of foreign traders. Incredibly powerful in the hands of someone who knows how to use it."
		weap_stats = ["42 → 510", "DEF%: 11.3% → 51.7%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {claymore_proto} `x01`, {crystal_chunk} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "the bell" or weap_name == "bell":
		weap_data = ["The Bell", four[0], claymore_icon, bell, "Rebellious Guardian", "https://i.imgur.com/n2Y6P7a.png"]
		weap_desc = "A heavy greatsword. A clock is embedded within it, though its internal mechanisms have long been damaged."
		weap_stats = ["42 → 510", "HP%: 9.0% → 41.3%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], nectar[0], nectar[1], nectar[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "serpent spine" or weap_name == "serpent" or weap_name == "spine" or weap_name == "ss":
		weap_data = ["Serpent Spine", four[0], claymore_icon, serpent_spine, "Wavesplitter", "https://i.imgur.com/FRJUie6.png"]
		weap_desc = "A rare weapon whose origin is the ancient ocean. One can hear the sound of the ageless waves as one swings it."
		weap_stats = ["42 → 510", "CRIT Rate%: 6.0% → 27.6%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], nectar[0], nectar[1], nectar[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "royal greatsword" or weap_name == "royal gsword" or weap_name == "royal":
		weap_data = ["Royal Greatsword", four[0], claymore_icon, royal_gsword, "Focus", "https://i.imgur.com/rAmy6Og.png"]
		weap_desc = "An old greatsword that belonged to the erstwhile rulers of Mondstadt. It is made from the finest-quality materials and has stood the test of time. A weapon for use by royals only."
		weap_stats = ["44 → 565", "ATK%: 6.0% → 27.6%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "rainslasher":
		weap_data = ["Rainslasher", four[0], claymore_icon, rainslasher, "Bane of Storm and Tide", "https://i.imgur.com/MdIgWlp.png"]
		weap_desc = "A fluorescent greatsword with no sharp edge that crushes enemies with brute force and raw power."
		weap_stats = ["42 → 510", "EM: 36.0 → 165"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "prototype archaic" or weap_name == "prototype aminus" or weap_name == "prototype animus" or weap_name == "archaic" or weap_name == "aminus" or weap_name == "animus":
		weap_data = ["Prototype Archaic", four[0], claymore_icon, archaic, "Crush", "https://i.imgur.com/YShmQCR.png"]
		weap_desc = "An ancient greatsword discovered in the Blackcliff Forge. It swings with such an immense force that one feels it could cut straight through reality itself."
		weap_stats = ["44 → 565", "ATK%: 6.0% → 27.6%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {claymore_proto} `x01`, {crystal_chunk} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "lithic blade" or weap_name == "lithic" or weap_name == "racist":
		weap_data = ["Lithic Blade", four[0], claymore_icon, lithic_blade, "Lithic Axiom - Unity", "https://i.imgur.com/qKVAZce.png"]
		weap_desc = "A greatsword carved and chiseled from the very bedrock of Liyue."
		weap_stats = ["42 → 510", "ATK%: 9.0% → 41.3%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "favonius greatsword" or weap_name == "fav greatsword" or weap_name == "fav gsword" or weap_name == "favonius" or weap_name == "fav":
		weap_data = ["Favonius Greatsword", four[0], claymore_icon, fav_gsword, "Windfall", "https://i.imgur.com/3mm7lyU.png"]
		weap_desc = "A heavy ceremonial sword of the Knights of Favonius. It channels elemental power easily and is highly destructive."
		weap_stats = ["41 → 454", "ER%: 13.3% → 61.3%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "blackcliff slasher" or weap_name == "blackcliff":
		weap_data = ["Blackcliff Slasher", four[0], claymore_icon, blackcliff_slasher, "Press the Advantage", "https://i.imgur.com/Z8PbU2i.png"]
		weap_desc = "An extremely sturdy greatsword from the Blackcliff Forge. It has a dark crimson color from the blade to the pommel."
		weap_stats = ["42 → 510", "CRIT DMG%: 12.0% → 55.1%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "katsuragi's slasher" or weap_name == "katsuragis slasher" or weap_name == "katsuragi's" or weap_name == "katsuragi":
		weap_data = ["Katsuragi's Slasher", four[0], claymore_icon, katsuragi_slasher, "Samurai Conduct", "https://i.imgur.com/ZmAKjbT.png"]
		weap_desc = "A blade that was once made in Tatarasuna. Heavy and tough."
		weap_stats = ["42 → 510", "ER%: 10.0% → 45.9%"]
		weap_ascension = [ascension2[0], ascension2[1], ascension2[2], ascension2[3], common3[0], common3[1], common3[2], common1[0], common1[1], common1[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				embed.add_field(name="Forging Recipe", value=f"<:_:854304817568808960>: {claymore_proto} `x01`, {amethyst_lump} `x50`, {white_chunk} `x50`, <:_:847015060374814761> `x500`", inline=False)
				return embed

	elif weap_name == "white iron greatsword" or weap_name == "white iron gsword" or weap_name == "white iron":
		weap_data = ["White Iron Greatsword", three, claymore_icon, white_iron_gsword, "Cull the Weak", "https://i.imgur.com/amGBl9a.png"]
		weap_desc = "A claymore made from white iron. Lightweight without compromising on power. Effective even when wielded by one of average strength, it is extremely deadly in the hands of a physically stronger wielder."
		weap_stats = ["39 → 401", "DEF%: 9.6% → 43.9%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "skyrider greatsword" or weap_name == "skyrider gsword" or weap_name == "skyrider":
		weap_data = ["Skyrider Greatsword", three, claymore_icon, skyrider_gsword, "Courage", "https://i.imgur.com/Xxug2ZH.png"]
		weap_desc = "A reliable steel sword. The legendary Skyrider once tried to ride it as a flying sword... for the second time."
		weap_stats = ["39 → 401", "Phys DMG%: 9.6% → 43.9%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "ferrous shadow" or weap_name == "ferrous" or weap_name == "shadow":
		weap_data = ["Ferrous Shadow", three, claymore_icon, ferrous_shadow, "Unbending", "https://i.imgur.com/OcKgLYP.png"]
		weap_desc = "A replica of the famed sword of Arundolyn, the Lion of Light. Feel the power of a legendary hero as you hold this sword in your hand! Imagine yourself as the great warrior himself! Note: Daydreaming not recommended in live combat."
		weap_stats = ["39 → 401", "HP%: 7.7% → 35.2%"]
		weap_ascension = [tile[0], tile[1], tile[2], tile[3], horn[0], horn[1], horn[2], nectar[0], nectar[1], nectar[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "debate club" or weap_name == "debate" or weap_name == "club" or weap_name == "bonk":
		weap_data = ["Debate Club", three, claymore_icon, debate_club, "Blunt Conclusion", "https://i.imgur.com/bZMrok0.png"]
		weap_desc = "A handy club made of fine steel. The most persuasive line of reasoning in any debater's arsenal."
		weap_stats = ["39 → 401", "ATK%: 7.7% → 35.2%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "bloodtainted greatsword" or weap_name == "bloodtainted gsword" or weap_name == "bloodtainted":
		weap_data = ["Bloodtainted Greatsword", three, claymore_icon, bloodtainted_gsword, "Bane of Fire and Thunder", "https://i.imgur.com/fKZiyaA.png"]
		weap_desc = "A steel sword that is said to have been coated with dragon blood, rendering it invulnerable to damage. This effect is not extended to its wielder, however."
		weap_stats = ["38 → 354", "EM: 41 → 187"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "old merc's pal" or weap_name == "old mercs pal" or weap_name == "old merc's" or weap_name == "old mercs" or weap_name == "merc's pal" or weap_name == "mercs pal" or weap_name == "merc's" or weap_name == "mercs":
		weap_data = ["Old Merc's Pal", two, claymore_icon, no_data, " ", "https://i.imgur.com/zONomfd.png"]
		weap_desc = "A battle-tested greatsword that has seen better days and worse."
		weap_stats = ["33 → 243", " "]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension2(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	elif weap_name == "waster greatsword" or weap_name == "waster gsword" or weap_name == "waster":
		weap_data = ["Waster Greatsword", one, claymore_icon, no_data, " ", "https://i.imgur.com/RuncZE9.png"]
		weap_desc = "A sturdy sheet of iron that may be powerful enough to break apart mountains, if wielded with enough willpower."
		weap_stats = ["23 → 185", " "]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension1(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	message = await ctx.send(embed=weap_profile())

	await message.add_reaction(left)
	await message.add_reaction(right)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=120, check=check)
			
			if str(reaction.emoji) == right and weap_page_index != weap_page_total:
				weap_page_index += 1
				await message.edit(embed=weap_profile())
			
			elif str(reaction.emoji) == left and weap_page_index > 0:
				weap_page_index -= 1
				await message.edit(embed=weap_profile())

			await message.remove_reaction(reaction, user)

		except asyncio.TimeoutError:
			await message.clear_reactions()
			break

#---------------------------------------
# Weapon Info: Polearm
#---------------------------------------
@client.command(aliases=['spear', 'p'])
async def polearm(ctx, *, weap_name):

	weap_name = weap_name.lower()
	
	weap_page_index = 0
	weap_page_total = 1

	if weap_name == "staff of homa" or weap_name == "homa":
		weap_data = ["Staff of Homa", five[0], polearm_icon, staff_homa, "Reckless Cinnabar", "https://i.imgur.com/qHPNHym.png"]
		weap_desc = "A \"firewood staff\" that was once used in ancient and long-lost rituals."
		weap_stats = ["46 → 608", "CRIT DMG%: 14.4% → 66.2%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], leyline[0], leyline[1], leyline[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "primordial jade winged-spear" or weap_name == "primordial jade winged-spear" or weap_name == "primordial jade spear" or weap_name == "jade winged-spear" or weap_name == "jade winged spear" or weap_name == "primordial jade spear" or weap_name == "primordial jade" or weap_name == "jade spear" or weap_name == "pjws":
		weap_data = ["Primordial Jade Winged-Spear", five[0], polearm_icon, jade_spear, "Eagle Spear of Justice", "https://i.imgur.com/LgwhXIm.png"]
		weap_desc = "A jade polearm made by the archons, capable of slaying ancient beasts."
		weap_stats = ["48 → 674", "CRIT Rate%: 4.8% → 22.1%"]
		weap_ascension = [pillar[0], pillar[1], pillar[2], pillar[3], sac_knife[0], sac_knife[1], sac_knife[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "vortex vanquisher" or weap_name == "vortex" or weap_name == "vanquisher" or weap_name == "vv":
		weap_data = ["Vortex Vanquisher", five[0], polearm_icon, vortex_vanquisher, "Golden Majesty", "https://i.imgur.com/b4FZGyg.png"]
		weap_desc = "This sharp polearm can seemingly pierce through anything. When swung, one can almost see the rift it tears in the air."
		weap_stats = ["46 → 608", "ATK%: 10.8% → 49.6%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], hoarder_insignia[0], hoarder_insignia[1], hoarder_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "skyward spine" or weap_name == "skyward" or weap_name == "spine":
		weap_data = ["Skyward Spine", five[0], polearm_icon, skyward_spine, "Blackwing", "https://i.imgur.com/O5c4c7F.png"]
		weap_desc = "A polearm that symbolizes Dvalin's fire resolve. The upright shaft of this weapon points towards the heavens, clad in the might of sky and wind."
		weap_stats = ["48 → 674", "ER%: 8.0% → 36.8%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], scroll[0], scroll[1], scroll[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "dragonspine spear" or weap_name == "dspine spear" or weap_name == "dragonspine" or weap_name == "dspine":
		weap_data = ["Dragonspine Spear", four[0], polearm_icon, dragonspine_spear, "Frost Burial", "https://i.imgur.com/gQyRVI8.png"]
		weap_desc = "A Spear created from the fang of a dragon. It is oddly warm to the touch."
		weap_stats = ["41 → 454", "Phys DMG%: 15.0% → 69.0%"]
		weap_ascension = [tooth[0], tooth[1], tooth[2], tooth[3], mist_grass[0], mist_grass[1], mist_grass[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "royal spear" or weap_name == "royal":
		weap_data = ["Royal Spear", four[0], polearm_icon, royal_spear, "Focus", "https://i.imgur.com/JYKmS81.png"]
		weap_desc = "This polearm was once cherished by a member of the old nobility that governed Mondstadt long ago. Although it has never seen the light of day, it is still incomparably sharp."
		weap_stats = ["44 → 565", "ATK%: 6.0% → 27.6%"]
		weap_ascension = [elixir[0], elixir[1], elixir[2], elixir[3], mist_grass[0], mist_grass[1], mist_grass[2], fatui_insignia[0], fatui_insignia[1], fatui_insignia[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "favonius lance" or weap_name == "favonius" or weap_name == "fav lance" or weap_name == "fav":
		weap_data = ["Favonius Lance", four[0], polearm_icon, fav_lance, "Windfall", "https://i.imgur.com/EY3ETiZ.png"]
		weap_desc = "A polearm made in the style of the Knights of Favonius. Its shaft is straight, and its tip flows lightly like the wind."
		weap_stats = ["44 → 565", "ATK%: 6.7% → 30.6%"]
		weap_ascension = [chain[0], chain[1], chain[2], chain[3], ruin[0], ruin[1], ruin[2], slime[0], slime[1], slime[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "prototype starglitter" or weap_name == "prototype grudge" or weap_name == "starglitter" or weap_name == "grudge":
		weap_data = ["Prototype Starglitter", four[0], polearm_icon, starglitter, "Magic Affinity", "https://i.imgur.com/IZsoi8l.png"]
		weap_desc = "A grudge discovered in the Blackcliff Forge. The glimmers along the sharp edge are like stars in the night."
		weap_stats = ["42 → 510", "ER%: 10.0% → 45.9%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], mask[0], mask[1], mask[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	if weap_name == "lithic spear" or weap_name == "lithic" or weap_name == "racist":
		weap_data = ["Lithic Spear", four[0], polearm_icon, lithic_spear, "Lithic Axiom - Unity", "https://i.imgur.com/YnkSMZX.png"]
		weap_desc = "A spear forged from the rocks of the Guyun Stone Forest. Its hardness knows no equal."
		weap_stats = ["44 → 565", "ATK%: 6.0% → 27.6%"]
		weap_ascension = [aerosiderite[0], aerosiderite[1], aerosiderite[2], aerosiderite[3], bone_shard[0], bone_shard[1], bone_shard[2], arrowhead[0], arrowhead[1], arrowhead[2]]

		def weap_profile():
			embed = discord.Embed(description=f"**{weap_data[0]}**\n{weap_data[1]} | {weap_data[2]}\n{weap_desc}", color=null)
			embed.set_thumbnail(url=f"{weap_data[5]}")

			if weap_page_index == 0:
				weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total)
				return embed
			if weap_page_index == 1:
				weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total)
				return embed

	message = await ctx.send(embed=weap_profile())

	await message.add_reaction(left)
	await message.add_reaction(right)

	def check(reaction, user):
		return user == ctx.author and str(
			reaction.emoji) in [left, right] and reaction.message == message

	while True:
		try:
			reaction, user = await client.wait_for("reaction_add", timeout=120, check=check)
			
			if str(reaction.emoji) == right and weap_page_index != weap_page_total:
				weap_page_index += 1
				await message.edit(embed=weap_profile())
			
			elif str(reaction.emoji) == left and weap_page_index > 0:
				weap_page_index -= 1
				await message.edit(embed=weap_profile())

			await message.remove_reaction(reaction, user)

		except asyncio.TimeoutError:
			await message.clear_reactions()
			break
			
client.run(os.getenv('DISCORD_TOKEN'))
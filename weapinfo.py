def weap_info(embed, weap_data, weap_stats, weap_page_index, weap_page_total):
	embed.add_field(name="Stat Progression", value=f"Base ATK: {weap_stats[0]}\n{weap_stats[1]}\n\n**{weap_data[4]}**\n{weap_data[3]}", inline=False)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	embed.set_thumbnail(url=f"{weap_data[5]}")
	return embed

def weap_ascension5(embed, weap_ascension, weap_page_index, weap_page_total):
	embed.add_field(name="Weapon Ascension Materials", value=f"<:_:851297316379295744>: {weap_ascension[0]} `x05`, {weap_ascension[4]} `x05`, {weap_ascension[7]} `x03`, <:_:847015060374814761> `x10,000`\n<:_:851297316338008064>: {weap_ascension[1]} `x05`, {weap_ascension[4]} `x18`, {weap_ascension[7]} `x12`, <:_:847015060374814761> `x20,000`\n<:_:851297316308254740>: {weap_ascension[1]} `x09`, {weap_ascension[5]} `x09`, {weap_ascension[8]} `x09`, <:_:847015060374814761> `x30,000`", inline=True)
	embed.add_field(name="_ _", value=f"<:_:851297316333289512>: {weap_ascension[2]} `x05`, {weap_ascension[5]} `x18`, {weap_ascension[8]} `x14`, <:_:847015060374814761> `x45,000`\n<:_:851299506510233620>: {weap_ascension[2]} `x09`, {weap_ascension[6]} `x14`, {weap_ascension[9]} `x09`, <:_:847015060374814761> `x55,000`\n<:_:851299506435260457>: {weap_ascension[3]} `x06`, {weap_ascension[6]} `x27`, {weap_ascension[9]} `x18`, <:_:847015060374814761> `x65,000`", inline=True)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	return embed

def weap_ascension4(embed, weap_ascension, weap_page_index, weap_page_total):
	embed.add_field(name="Weapon Ascension Materials", value=f"<:_:851297316379295744>: {weap_ascension[0]} `x03`, {weap_ascension[4]} `x03`, {weap_ascension[7]} `x02`, <:_:847015060374814761> `x5,000`\n<:_:851297316338008064>: {weap_ascension[1]} `x03`, {weap_ascension[4]} `x12`, {weap_ascension[7]} `x08`, <:_:847015060374814761> `x15,000`\n<:_:851297316308254740>: {weap_ascension[1]} `x06`, {weap_ascension[5]} `x06`, {weap_ascension[8]} `x06`, <:_:847015060374814761> `x20,000`", inline=True)
	embed.add_field(name="_ _", value=f"<:_:851297316333289512>: {weap_ascension[2]} `x03`, {weap_ascension[5]} `x12`, {weap_ascension[8]} `x09`, <:_:847015060374814761> `x30,000`\n<:_:851299506510233620>: {weap_ascension[2]} `x06`, {weap_ascension[6]} `x09`, {weap_ascension[9]} `x06`, <:_:847015060374814761> `x35,000`\n<:_:851299506435260457>: {weap_ascension[3]} `x04`, {weap_ascension[6]} `x18`, {weap_ascension[9]} `x12`, <:_:847015060374814761> `x45,000`", inline=True)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	return embed

def weap_ascension3(embed, weap_ascension, weap_page_index, weap_page_total):
	embed.add_field(name="Weapon Ascension Materials", value=f"<:_:851297316379295744>: {weap_ascension[0]} `x02`, {weap_ascension[4]} `x02`, {weap_ascension[7]} `x01`, <:_:847015060374814761> `x5,000`\n<:_:851297316338008064>: {weap_ascension[1]} `x02`, {weap_ascension[4]} `x08`, {weap_ascension[7]} `x05`, <:_:847015060374814761> `x10,000`\n<:_:851297316308254740>: {weap_ascension[1]} `x04`, {weap_ascension[5]} `x04`, {weap_ascension[8]} `x04`, <:_:847015060374814761> `x15,000`", inline=True)
	embed.add_field(name="_ _", value=f"<:_:851297316333289512>: {weap_ascension[2]} `x02`, {weap_ascension[5]} `x08`, {weap_ascension[8]} `x06`, <:_:847015060374814761> `x20,000`\n<:_:851299506510233620>: {weap_ascension[2]} `x04`, {weap_ascension[6]} `x06`, {weap_ascension[9]} `x04`, <:_:847015060374814761> `x25,000`\n<:_:851299506435260457>: {weap_ascension[3]} `x03`, {weap_ascension[6]} `x12`, {weap_ascension[9]} `x08`, <:_:847015060374814761> `x30,000`", inline=True)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	return embed

def weap_ascension2(embed, weap_ascension, weap_page_index, weap_page_total):
	embed.add_field(name="Weapon Ascension Materials", value=f"<:_:851297316379295744>: {weap_ascension[0]} `x01`, {weap_ascension[4]} `x01`, {weap_ascension[7]} `x01`, <:_:847015060374814761> `x5,000`\n<:_:851297316338008064>: {weap_ascension[1]} `x01`, {weap_ascension[4]} `x05`, {weap_ascension[7]} `x04`, <:_:847015060374814761> `x5,000`", inline=True)
	embed.add_field(name="_ _", value=f"<:_:851297316308254740>: {weap_ascension[1]} `x03`, {weap_ascension[5]} `x03`, {weap_ascension[8]} `x03`, <:_:847015060374814761> `x10,000`\n<:_:851297316333289512>: {weap_ascension[2]} `x01`, {weap_ascension[5]} `x05`, {weap_ascension[8]} `x04`, <:_:847015060374814761> `x15,000`", inline=True)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	return embed

def weap_ascension1(embed, weap_ascension, weap_page_index, weap_page_total):
	embed.add_field(name="Weapon Ascension Materials", value=f"<:_:851297316379295744>: {weap_ascension[0]} `x01`, {weap_ascension[4]} `x01`, {weap_ascension[7]} `x01`, <:_:847015060374814761> `x00`\n<:_:851297316338008064>: {weap_ascension[1]} `x01`, {weap_ascension[4]} `x04`, {weap_ascension[7]} `x02`, <:_:847015060374814761> `x5,000`", inline=True)
	embed.add_field(name="_ _", value=f"<:_:851297316308254740>: {weap_ascension[1]} `x02`, {weap_ascension[5]} `x02`, {weap_ascension[8]} `x02`, <:_:847015060374814761> `x5,000`\n<:_:851297316333289512>: {weap_ascension[2]} `x01`, {weap_ascension[5]} `x04`, {weap_ascension[8]} `x03`, <:_:847015060374814761> `x10,000`", inline=True)
	embed.set_footer(text=f"Page {weap_page_index+1}/{weap_page_total+1}")
	return embed

no_data = " "

# Swords

freedom_sworn = "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases DMG by `10%`/`12.5%`/`15%`/`17.5%`/`20%`. When the character wielding this weapon triggers Elemental Reactions, they gain a Sigil of Rebellion. This effect can be triggered once every 0.5s and can be triggered even if said character is not on the field.\nWhen you possess 2 Sigils of Rebellion, all of them will be consumed and all nearby party members will obtain \"Millennial Movement: Song of Resistance\" for 12s. \"Millennial Movement: Song of Resistance\" increases Normal, Charged and Plunging Attack DMG by `16%`/`20%`/`24%`/`28%`/`32%` and increases ATK by `20%`/`25%`/`30%`/`35%`/`40%`.\nOnce this effect is triggered, you will not gain Sigils of Rebellion for 20s. Of the many effects of the \"Millennial Movement,\" buffs of the same type will not stack."

jade_cutter = "HP increased by `20%`/`25%`/`30%`/`35%`/`40%`. Additionally, provides an ATK Bonus based on `1.2%`/`1.5%`/`1.8%`/`2.1%`/`2.4%` of the wielder's Max HP."

summit_shaper = "Increases Shield Strength by `20%`/`25%`/`30%`/`35%`/`40%`. Scoring hits on opponents increases ATK by `4%`/`5%`/`6%`/`7%`/`8%` for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%."

skyward_blade = "Crit Rate increased by `4%`/`5%`/`6%`/`7%`/`8%`. Gains Skypiercing Might upon using Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to `20%`/`25%`/`30%`/`35%`/`40%` of ATK. Skypiercing Might lasts for 12s."

aquila_favonia = "ATK is increased by `20%`/`25%`/`30%`/`35%`/`40%`. Triggers on taking DMG: the soul of the Falcon of the West awakens, holding the banner of the resistance aloft, regenerating HP equal to `100%`/`115%`/`130%`/`145%`/`160%` of ATK and dealing `200%`/`230%`/`260%`/`290%`/`320%` of ATK as DMG to surrounding opponents. This effect can only occur once every 15s."

mistsplitter = "Gain a `12%`/`15%`/`18%`/`21%`/`24%` Elemental DMG Bonus for every element and receive the might of Mistsplitter's Seal.\nAt stack levels 1/2/3, Mistsplitter's Seal provides a\n`8%`/`10%`/`12%`/`14%`/`16%`\n`16%`/`20%`/`24%`/`28%`/`32%`\n`28%`/`35%`/`42%`/`49%`/`56%`\nElemental DMG Bonus for the character's Elemental Type. The character will obtain 1 stack of Mistsplitter's Seal in each of the following scenarios: Normal Attack deals Elemental DMG (stack lasts 5s), casting Elemental Burst (stacks lasts 10s); Energy is less than 100% (stack disappears when Energy is full). Each stack's duration is calculated independently."

festering_desire = "Increases Elemental Skill DMG by `16%`/`20%`/`24%`/`28%`/`32%` and Elemental Skill CRIT Rate by `6%`/`7.5%`/`9%`/`10.5%`/`12%`."

descension = "Hitting enemies with Normal or Charged Attacks grants a 50% chance to deal 200% ATK as DMG in a small AoE. This effect can only occur once every 10s. Additionally, if the Traveler equips the Sword of Descension, their ATK is increased by 66."

flute = "Normal or Charged Attacks grant a Harmonic on hits. Gaining 5 Harmonics triggers the power of music and deals `100%`/`125%`/`150%`/`175%`/`200%` ATK DMG to surrounding enemies. Harmonics last up to 30s, and a maximum of 1 can be gained every 0.5s."

black_sword = "Increases DMG dealt by Normal and Charged Attacks by `20%`/`25%`/`30%`/`35%`/`40%`.\nAdditionally, regenerates `60%`/`70%`/`80%`/`90%`/`100%` of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s."

alley_flash = "Increases DMG dealt by the character equipping this weapon by `12%`/`15%`/`18%`/`21%`/`24%`. Taking DMG disables this effect for 5s."

sac_sword = "After dealing damage to an opponent with an Elemental Skill, the skill has a `40%`/`50%`/`60%`/`70%`/`80%` chance to end its own CD. Can only occur once every `30`/`26`/`22`/`19`/`16` seconds."

royal_sword = "Upon dealing damage to an opponent, increases CRIT Rate by `8%`/`10%`/`12%`/`14%`/`16%`. Max 5 stacks. A CRIT hit removes all existing stacks."

rancour = "On hit, Normal or Charged Attacks increase ATK and DEF by `4%`/`5%`/`6%`/`7%`/`8%` for 6s. Max 4 stacks. Can only occur once every 0.3s."

lions_roar = "Increases DMG against enemies affected by Pyro or Electro by `20%`/`24%`/`28%`/`32%`/`36%`."

iron_sting = "Dealing Elemental DMG increases all DMG by `6%`/`7.5%`/`9%`/`10.5%`/`12%` for 6s. Max 2 stacks. Can only occur once every 1s."

fav_sword = "CRIT hits have a `60%`/`70%`/`80%`/`90%`/`100%` chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every `12`/`10.5`/`9`/`7.5`/`6` seconds."

blackcliff_sword = "After defeating an opponent, ATK is increased by `12%`/`15%`/`18%`/`21%`/`24%` for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others."

amenoma_kageuta = "After casting an Elemental Skill, gain 1 Succession Seed. This effect can be triggered once every 5s. The Succession Seed lasts for 30s. Up to 3 Succession Seeds may exist simultaneously. After using an Elemental Burst, all Succession Seeds are consumed and after 2s, the character regenerates `6`/`7.5`/`9`/`10.5`/`12` Energy for each seed consumed."

trav_handy_sword = "Each Elemental Orb or Particle collected restores `1%`/`1.25%`/`1.5%`/`1.75%`/`2%` HP."

skyrider_sword = "Using an Elemental Burst grants a `12%`/`15%`/`18%`/`21%`/`24%` increase in ATK and Movement SPD for 15s."

harbinger_dawn = "When HP is above 90%, increases CRIT Rate by `14%`/`17.5%`/`21%`/`24.5%`/`28%`."

fillet_blade = "On hit, has a 50% chance to deal `240%`/`280%`/`320%`/`360%`/`400%` ATK DMG to a single opponent. Can only occur once every `15`/`14`/`13`/`12`/`11` seconds."

dark_iron_sword = "Upon causing an Overloaded, Superconduct, Electro-Charged, or an Electro-infused Swirl reaction, ATK is increased by `20%`/`25%`/`30%`/`35%`/`40%` for 12s."

cool_steel = "Increases DMG against opponents affected by Hydro or Cryo by `12%`/`15%`/`18%`/`21%`/`24%`."

# Claymores

broken_pines = "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases ATK by `16%`/`20%`/`24%`/`28%`/`32%`, and when Normal or Charged Attacks hit opponents, the character gains a Sigil of Whispers. This effect can be triggered once every 0.3s.\nWhen you possess four Sigils of Whispers, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Banner-Hymn\" effect for 12s. \"Millennial Movement: Banner-Hymn\" increases Normal ATK SPD by `12%`/`15%`/`18%`/`21%`/`24%` and increases ATK by `20%`/`25%`/`30%`/`35%`/`40%`.\nOnce this effect is triggered, you will not gain Sigils of Whispers for 20s. Of the many effects of the \"Millennial Movement\", buffs of the same type will not stack."

unforged = "Increases Shield Strength by `20%`/`25%`/`30%`/`35%`/`40%`. Scoring hits on opponents increases ATK by `4%`/`5%`/`6%`/`7%`/`8%` for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%."

wgs = "Increases ATK by `20%`/`25%`/`30%`/`35%`/`40%`. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by `40%`/`50%`/`60%`/`70%`/`80%` for 12s. Can only occur once every 30s."

skyward_pride = "Increases all DMG by `8%`/`10%`/`12%`/`14%`/`16%`. After using an Elemental Burst, Normal or Charged Attack, on hit, creates a vacuum blade that does `80%`/`100%`/`120%`/`140%`/`160%` of ATK as DMG to opponents along its path. Lasts for 20s or 8 vacuum blades."

snow_tomb = "Hitting an opponent with Normal and Charged Attacks has a `60%`/`70%`/`80%`/`90%`/`100%` chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to `80%`/`95%`/`110%`/`125%`/`140%` of ATK. Opponents affected by Cryo are instead dealt DMG equal to `200%`/`240%`/`280%`/`320%`/`360%` of ATK. Can only occur once every 10s."

sac_gsword = "After damaging an opponent with an Elemental Skill, the skill has a `40%`/`50%`/`60%`/`70%`/`80%` chance to end its own CD. Can only occur once every `30`/`26`/`22`/`19`/`16` seconds."

whiteblind = "On hit, Normal or Charged Attacks increase ATK and DEF by `6%`/`7.5%`/`9%`/`10.5%`/`12%` for 6s. Max 4 stacks. This effect can only occur once every 0.5s."

bell = "Taking DMG generates a shield which absorbs DMG up to `20%`/`23%`/`26%`/`29%`/`32%` of Max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains `12%`/`15%`/`18%`/`21%`/`24%` increased DMG."

serpent_spine = "Every 4s a character is on the field, they will deal `6%`/`7%`/`8%`/`9%`/`10%` more DMG and take `3%`/`2.7%`/`2.4%`/`2.2%`/`2%` more DMG. This effect has a maximum of 5 stacks and will not be reset if the character leaves the field, but will be reduced by 1 stack when the character takes DMG."

royal_gsword = "Upon damaging an opponent, increases CRIT Rate by `8%`/`10%`/`12%`/`14%`/`16%`. Max 5 stacks. A CRIT Hit removes all stacks."

rainslasher = "Increases DMG against opponents affected by Hydro or Electro by `20%`/`24%`/`28%`/`32%`/`36%`."

archaic = "On hit, Normal or Charged Attacks have a 50% chance to deal an additional `240%`/`300%`/`360%`/`420%`/`480%` ATK DMG to opponents within a small AoE. Can only occur once every 15s."

lithic_blade = "For every character in the party who hails from Liyue, the character who equips this weapon gains a `7%`/`8%`/`9%`/`10%`/`11%` ATK increase and a `3%`/`4%`/`5%`/`6%`/`7%` CRIT Rate increase. This effect stacks up to 4 times."

fav_gsword = "CRIT Hits have a `60%`/`70%`/`80%`/`90%`/`100%` chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every `12`/`10.5`/`9`/`7.5`/`6` seconds."

blackcliff_slasher = "After defeating an opponent, ATK is increased by `12%`/`15%`/`18%`/`21%`/`24%` for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others."

katsuragi_slasher = "Increases Elemental Skill DMG by `6%`/`7.5%`/`9%`/`10.5%`/`12%`. After an Elemental Skill hits an opponent, lose 3 Energy but regenerate `3`/`3.5`/`4`/`4.5`/`5` Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field."

white_iron_gsword = "Defeating an opponent restores `8%`/`10%`/`12%`/`14%`/`16%` HP."

skyrider_gsword = "On hit, Normal or Charged Attacks increase ATK by `6%`/`7%`/`8%`/`9%`/`10%` for 6s. Max 4 stacks. Can occur once every 0.5s."

ferrous_shadow = "When HP falls below `70%`/`75%`/`80%`/`85%`/`90%`, increases Charged Attack DMG by `30%`/`35%`/`40%`/`45%`/`50%` and Charged Attacks become harder to interrupt."

debate_club = "After using an Elemental Skill, on hit, Normal and Charged Attacks deal additional DMG equal to `60%`/`75%`/`90%`/`105%`/`120%` of ATK in a small AoE. Effect lasts 15s. DMG can only occur once every 3s."

bloodtainted_gsword = "Increases DMG dealt against opponents affected by Pyro or Electro by 12%/15%/18%/21%/24%."

# Polearms

staff_homa = "HP increased by `20%`/`25%`/`30%`/`35%`/`40%`. Additionally, provides an ATK Bonus based on `0.8%`/`1%`/`1.2%`/`1.4%`/`1.6%` of the wielder's Max HP. When the wielder's HP is less than 50%, this ATK Bonus is increased by an additional `1%`/`1.2%`/`1.4%`/`1.6%`/`1.8%` of Max HP."

skyward_spine = "Increases CRIT Rate by `8%`/`10%`/`12%`/`14%`/`16%` and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals `40%`/`55%`/`70%`/`85%`/`100%` of ATK as DMG in a small AoE. This effect can occur no more than once every 2s."

jade_spear = "On hit, increases ATK by `3.2%`/`3.9%`/`4.6%`/`5.3%`/`6%` for 6s. Max 7 stacks. This effect can only occur once every 0.3s. While in possession of the maximum possible stacks, DMG dealt is increased by `12%`/`15%`/`18%`/`21%`/`24%`."

vortex_vanquisher = "Increases Shield Strength by `20%`/`25%`/`30%`/`35%`/`40%`. Scoring hits on opponents increases ATK by `4%`/`5%`/`6%`/`7%`/`8%` for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%."

dragonspine_spear = "Hitting an opponent with Normal and Charged Attacks has a `60%`/`70%`/`80%`/`90%`/`100%` chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to `80%`/`95%`/`110%`/`125%`/`140%` of ATK. Opponents affected by Cryo are instead dealt DMG equal to `200%`/`240%`/`280%`/`320%`/`360%` of ATK. Can only occur once every 10s."

royal_spear = "Upon damaging an opponent, increases CRIT Rate by `8%`/`10%`/`12%`/`14%`/`16%`. Max 5 stacks. A CRIT Hit removes all stacks.	"

fav_lance = "CRIT Hits have a `60%`/`70%`/`80%`/`90%`/`100%` chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every `12`/`10.5`/`9`/`7.5`/`6` seconds."

starglitter = "After using an Elemental Skill, increases Normal and Charged Attack DMG by `8%`/`10%`/`12%`/`14%`/`16%` for 12s. Max 2 stacks."

lithic_spear = "For every character in the party who hails from Liyue, the character who equips this weapon gains a `7%`/`8%`/`9%`/`10%`/`11%` ATK increase and a `3%`/`4%`/`5%`/`6%`/`7%` CRIT Rate increase. This effect stacks up to 4 times."

dragons_bane = "Increases DMG against opponents affected by Hydro or Pyro by `20%`/`24%`/`28%`/`32%`/`36%`."

deathmatch = "If there are at least 2 opponents nearby, ATK is increased by `16%`/`20%`/`24%`/`28%`/`32%` and DEF is increased by `16%`/`20%`/`24%`/`28%`/`32%`. If there are fewer than 2 opponents nearby, ATK is increased by `24%`/`30%`/`36%`/`42%`/`48%`."

crescent_pike = "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal additional DMG equal to `20%`/`25%`/`30%`/`35%`/`40%` of ATK for 5s."

blackcliff_pole = "After defeating an enemy, ATK is increased by `12%`/`15%`/`18%`/`21%`/`24%` for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others."

kitain_spear = "Increases Elemental Skill DMG by `6%`/`7.5%`/`9%`/`10.5%`/`12%`. After Elemental Skill hits an opponent, lose 3 Energy but regenerate `3`/`3.5`/`4`/`4.5`/`5` Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field."

white_tassel = "Increases Normal Attack DMG by `24%`/`30%`/`36%`/`42%`/`48%`."

halberd = "Normal Attacks deal an additional `160%`/`200%`/`240%`/`280%`/`320%` ATK as DMG. Can only occur once every 10s."

black_tassel = "Increases DMG against slimes by `40%`/`50%`/`60%`/`70%`/`80%`."

# Bows

elegy = "A part of the \"Millennial Movement\" that wanders amidst the winds. Increases Elemental Mastery by 60. When the Elemental Skills or Elemental Bursts of the character wielding this weapon hit opponents, that character gains a Sigil of Remembrance. This effect can be triggered once every 0.2s and can be triggered even if said character is not on the field.\nWhen you possess 4 Sigils of Remembrance, all of them will be consumed and all nearby party members will obtain the \"Millennial Movement: Farewell Song\" effect for 12s. \"Millennial Movement: Farewell Song\" increases Elemental Mastery by 100 and increases ATK by 20%.\nOnce this effect is triggered, you will not gain Sigils of Remembrance for 20s. Of the many effects of the \"Millennial Movement,\" buffs of the same type will not stack."

amos_bow = "Increases Normal and Charged Attack DMG by 12%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 8% every 0.1s the arrow is in the air for up to 5 times."

skyward_harp = "Increases CRIT DMG by 20%. Hits have a 60% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 4s."

mitternachts_waltz = "Normal Attack hits on opponents increase Elemental Skill DMG by 20% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 20% for 5s."

windblume_ode = "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 16% for 6s."

viri_hunt = "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 40% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 14s."

sac_bow = "After damaging an opponent with an Elemental Skill, the skill has a 40% chance to end its own CD. Can only occur once every 30s."

rust = "Increases Normal Attack DMG by 40% but decreases Charged Attack DMG by 10%."

royal_bow = "Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks. A CRIT Hit removes all stacks."

crescent = "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 36% for 10s."

fav_bow = "CRIT Hits have a 60% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 12s."

compound_bow = "Normal Attack and Charged Attack hits increase ATK by 4% and Normal ATK SPD by 1.2% for 6s. Max 4 stacks. Can only occur once every 0.3s."

blackcliff_warbow = "After defeating an enemy, ATK is increased by 12% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others."

alley_hunter = "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 2% every second up to a max of 20%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 4% per second until it reaches 0%."

stringless = "Increases Elemental Skill and Elemental Burst DMG by 24%."

thundering_pulse = "Increases ATK by `20%`/`25%`/`30%`/`35%`/`40%` and grants the might of the Thunder Seal. At stack levels 1/2/3, the Thunder Seal increases Normal Attack DMG by\n`12%`/`15%`/`18%`/`21%`/`24%`\n`24%`/`30%`/`36%`/`42%`/`48%`\n`40%`/`50%`/`60%`/`70%`/`80%`.\nThe character will obtain 1 stack of Thunder Seal in each of the following scenarios: Normal Attack deals DMG (stack lasts 5s), casting Elemental Skill (stacks lasts 10s); Energy is less than 100% (stack disappears when Energy is full). Each stack's duration is calculated independently."

slingshot = "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by `36%`/`42%`/`48%`/`54%`/`60%`. Otherwise, decreases DMG by 10%."

sharpshooter_oath = "Increases DMG against weak spots by `24%`/`30%`/`36%`/`42%`/`48%`."

recurve_bow = "Defeating an opponent restores `8%`/`10%`/`12%`/`14%`/`16%` HP."

raven_bow = "Increases DMG against opponents affected by Hydro or Pyro by `12%`/`15%`/`18%`/`21%`/`24%`."

messenger = "Charged Attack hits on weak points deal an additional `100%`/`125%`/`150%`/`175%`/`200%` ATK DMG as CRIT DMG. Can only occur once every 10s."

# Catalysts

memory_dust = "Increases Shield Strength by 20%. Scoring hits on opponents increases ATK by 4% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%."

skyward_atlas = "Increases Elemental DMG Bonus by 12%. Normal Attack hits have a 50% chance to earn the favor of the clouds, which actively seek out nearby opponents to attack for 15s, dealing 160% ATK DMG. Can only occur once every 30s."

lost_prayer = "Increases Movement SPD by 10%. When in battle, gain an 8% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat."

dodoco_tales = "Normal Attack hits on opponents increase Charged Attack DMG by 16% for 6s. Charged Attack hits on opponents increase ATK by 8% for 6s."

frostbearer = "Hitting an opponent with Normal and Charged Attacks has a 60% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 80% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 200% of ATK. Can only occur once every 10s."

eye_perception = "Normal and Charged Attacks have a 50% chance to fire a Bolt of Perception, dealing 240% ATK as DMG. This bolt can bounce between opponents a maximum of 4 times. This effect can occur once every 12s."

wine_song = "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 14% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 20% for 5s."

widsith = "When the character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 60%. Aria: Increases all Elemental DMG by 48%. Interlude: Elemental Mastery is increased by 240."

solar_pearl = "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 20% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 20% for 6s."

sac_frag = "After damaging an opponent with an Elemental Skill, the skill has a 40% chance to end its own CD. Can only occur once every 30s."

royal_grim = "Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks. A CRIT Hit removes all stacks."

amber = "Using an Elemental Burst regenerates 4 Energy every 2s for 6s. All party members will regenerate 4% HP every 2s for this duration."

mappa_mare = "Triggering an Elemental reaction grants a 8% Elemental DMG Bonus for 10s. Max 2 stacks."

fav_codex = "CRIT Hits have a 60% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 12s."

blackcliff_agate = "After defeating an enemy, ATK is increased by 12% for 30s. This effect has a maximum of 3 stacks, and the duration of each stack is independent of the others."

white_dragon_ring = "After the character equipped with this weapon triggers an Electro elemental reaction, nearby party members of an Elemental Type involved in the elemental reaction receive a 10% Elemental DMG Bonus for their element, lasting 6s. Elemental Bonuses gained in this way cannot be stacked."

twin_nephrite = "Defeating an opponent increases Movement SPD and ATK by `12%`/`14%`/`16%`/`18%`/`20%` for 15s."

thrilling_tales = "When switching characters, the new character taking the field has their ATK increased by `24%`/`30%`/`36%`/`42%`/`48%` for 10s. This effect can only occur once every 20s."

otherworldly_story = "Picking up an Elemental Energy Orb/Particle recovers `1%`/`1.25%`/`1.5%`/`1.75%`/`2%` HP."

magic_guide = "Increases DMG against opponents affected by Hydro or Electro by `12%`/`15%`/`18%`/`21%`/`24%`."

emerald_orb = "Upon causing a Vaporize, Electro-Charged, Frozen, or a Hydro-infused Swirl reaction, increases ATK by `20%`/`25%`/`30%`/`35%`/`40%` for 12s."
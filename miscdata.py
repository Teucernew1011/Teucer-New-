def ascension_field1(ascension_data):
  ascension_field1 = f"<:_:851297316379295744>: {ascension_data[0]} `x01`, {ascension_data[4]} `x00`, {ascension_data[5]} `x03`,\n {ascension_data[6]} `x03`, <:_:847015060374814761> `x20,000`\n<:_:851297316338008064>: {ascension_data[1]} `x03`, {ascension_data[4]} `x02`, {ascension_data[5]} `x10`,\n {ascension_data[6]} `x15`, <:_:847015060374814761> `x40,000`\n<:_:851297316308254740>: {ascension_data[1]} `x06`, {ascension_data[4]} `x04`, {ascension_data[5]} `x20`,\n {ascension_data[7]} `x12`, <:_:847015060374814761> `x60,000`"
  return ascension_field1

def ascension_field2(ascension_data):
  ascension_field2 = f"<:_:851297316333289512>: {ascension_data[2]} `x03`, {ascension_data[4]} `x08`, {ascension_data[5]} `x30`,\n {ascension_data[7]} `x18`, <:_:847015060374814761> `x80,000`\n<:_:851299506510233620>: {ascension_data[2]} `x06`, {ascension_data[4]} `x12`, {ascension_data[5]} `x45`,\n {ascension_data[8]} `x12`, <:_:847015060374814761> `x100,000`\n<:_:851299506435260457>:  {ascension_data[3]} `x06`, {ascension_data[4]} `x20`, {ascension_data[5]} `x60`,\n {ascension_data[8]} `x24`, <:_:847015060374814761> `x120,000`"
  return ascension_field2

def ascension_field3(ascension_data):
  ascension_field3 = f"<:_:851297316338008064>: {ascension_data[9]} `x03`, {ascension_data[6]} `x06`, <:_:847015060374814761> `x12,500`\n<:_:851297316308254740>: {ascension_data[10]} `x02`, {ascension_data[7]} `x03`, <:_:847015060374814761> `x17,500`\n<:_:851297316333289512>: {ascension_data[10]} `x04`, {ascension_data[7]} `x04`, <:_:847015060374814761> `x25,000`\n<:_:851299506510233620>: {ascension_data[10]} `x06`, {ascension_data[7]} `x06`, <:_:847015060374814761> `x30,000`\n<:_:851299506435260457>: {ascension_data[10]} `x09`, {ascension_data[7]} `x09`, <:_:847015060374814761> `x37,500`"
  return ascension_field3

def ascension_field4(ascension_data):
  ascension_field4 = f"<:_:851299506113085461>: {ascension_data[11]} `x04`, {ascension_data[8]} `x04`, {ascension_data[12]} `x01`,\n <:_:847015060374814761> `x120,000`\n<:_:851299506447450142>: {ascension_data[11]} `x06`, {ascension_data[8]} `x06`, {ascension_data[12]} `x01`,\n <:_:847015060374814761> `x260,000`\n<:_:851299506477858846>: {ascension_data[11]} `x12`, {ascension_data[8]} `x09`, {ascension_data[12]} `x02`,\n <:_:847015060374814761> `x450,000`\n<:_:851299506338922505>: {ascension_data[11]} `x16`, {ascension_data[8]} `x12`, {ascension_data[12]} `x02`,\n <:_:847015060374814761> `x700,000`, <:_:850168084744372245> `x01`"
  return ascension_field4

def info_field1(profile_data):
	info_field1 = f"• Title: {profile_data[0]}\n• Affiliation: {profile_data[1]}\n• Birthday: {profile_data[2]}\n• Constellation: {profile_data[3]}"
	return info_field1

def info_field2(profile_data):
	info_field2 = f"• EN VA: {profile_data[4]}\n• CN VA: {profile_data[5]}\n• JP VA: {profile_data[6]}\n• KR VA: {profile_data[7]}"
	return info_field2
	
def info_field3(stats_data):
	info_field3 = f"• Base HP: {stats_data[0]}\n• Base ATK: {stats_data[1]}\n• Base DEF: {stats_data[2]}"
	return info_field3

def info_field4(stats_data):
	info_field4 = f"{stats_data[3]}\n• CRIT Rate: {stats_data[4]}\n• CRIT DMG: {stats_data[5]}"
	return info_field4

def info_template(embed, profile_name, profile_value, profile_page_index, profile_page_total):
  embed.add_field(name=f"{profile_name[profile_page_index]}", value=f"{profile_value[profile_page_index]}", inline=True)
  embed.add_field(name="_ _", value=f"{profile_value[profile_page_index+2]}", inline=True)
  embed.add_field(name="_ _", value="_ _", inline=False)
  embed.add_field(name=f"{profile_name[profile_page_index+2]}", value=f"{profile_value[profile_page_index+4]}", inline=True)
  embed.add_field(name="_ _", value=f"{profile_value[profile_page_index+6]}", inline=True)
  embed.set_footer(text=f"Page {profile_page_index+1}/{profile_page_total+1}")

def cons_template(embed, cons_emote, cons_author, cons_field, cons_page_index, cons_page_total, char_img):
	embed.set_author(name=f"{cons_author[cons_page_index]}", icon_url=f"{char_img[1]}")
	embed.add_field(name=f"{cons_emote[cons_page_index]} {cons_field[cons_page_index]}", value=f"{cons_field[cons_page_index+6]}", inline=False)
	embed.add_field(name=f"{cons_emote[cons_page_index+2]} {cons_field[cons_page_index+2]}", value=f"{cons_field[cons_page_index+8]}", inline=False)
	embed.add_field(name=f"{cons_emote[cons_page_index+4]} {cons_field[cons_page_index+4]}", value=f"{cons_field[cons_page_index+10]}", inline=False)
	embed.set_footer(text=f"Page {cons_page_index+1}/{cons_page_total+1}")
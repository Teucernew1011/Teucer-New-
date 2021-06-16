import discord
from emotes import *

embed = discord.Embed(color=color)

def level_template(embed, level):
  embed.add_field(name=f"{level[0]}", value=f"<:_:851297316379295744>` {level[1]} `\n<:_:851297316338008064>` {level[2]} `\n<:_:851297316308254740>` {level[3]} `\n<:_:851297316333289512>` {level[4]} `\n<:_:851299506510233620>` {level[5]} `", inline=True)
  embed.add_field(name=f"_ _", value=f"<:_:851299506435260457>` {level[6]} `\n<:_:851299506113085461>` {level[7]} `\n<:_:851299506447450142>` {level[8]} `\n<:_:851299506477858846>` {level[9]} `\n<:_:851299506338922505>` {level[10]} `", inline=True)
  embed.add_field(name=f"_ _", value=f"<:_:851299506246254593>` {level[11]} `\n<:_:851299506292785152>` {level[12]} `\n<:_:851299506242322472>` {level[13]} `\n<:_:851299506233540618>` {level[14]} `\n<:_:851299506163023882>` {level[15]} `", inline=True)

# Anemo

def sucrose_autoattack_data(embed):
	sucrose_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "33.46%", "35.97%", "38.48%", "41.83%", "44.34%", "46.85%", "50.2%", "53.54%", "56.89%", "60.24%", "63.58%", "66.93%", "71.11%", "75.29%", "79.48%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "30.62%", "32.91%", "35.21%", "38.27%", "40.57%", "42.86%", "45.92%", "48.99%", "52.05%", "55.11%", "58.17%", "61.23%", "65.06%", "68.89%", "72.71%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "38.45%", "41.33%", "44.22%", "48.06%", "50.94%", "53.83%", "57.67%", "61.52%", "65.36%", "69.21%", "73.05%", "76.9%", "81.7%", "86.51%", "91.31%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "47.92%", "51.51%", "55.11%", "59.9%", "63.49%", "67.08%", "71.88%", "76.67%", "81.46%", "86.25%", "91.04%", "95.84%", "101.82%", "107.81%", "113.8%"]
	level_template(embed, level)
	return sucrose_autoattack_data

def sucrose_autoattack_data2(embed):
	sucrose_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "120.16%", "129.17%", "138.18%", "150.2%", "159.21%", "168.22%", "180.24%", "192.26%", "204.27%", "216.29%", "228.3%", "240.32%", "255.34%", "270.36%", "285.38%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.60%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.20%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return sucrose_autoattack_data2

def sucrose_skill_data(embed):
	sucrose_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "211.2%", "227.04%", "242.88%", "264%", "279.84%", "295.68%", "316.8%", "337.92%", "359.04%", "380.16%", "401.28%", "422.4%", "448.8%", "475.2%", "501.6%"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	return sucrose_skill_data

def sucrose_burst_data(embed):
	sucrose_burst_data = discord.Embed(color=color)
	level = ["DoT", "148%", "159.1%", "170.2%", "185%", "196.1%", "207.2%", "222%", "236.8%", "251.6%", "266.4%", "281.2%", "296%", "314.5%", "333%", "351.5%"]
	level_template(embed, level)
	level = ["Additional Elemental DMG", "44%", "47.3%", "50.6%", "55%", "58.3%", "61.6%", "66%", "70.4%", "74.8%", "79.2%", "83.6%", "88%", "93.5%", "99%", "104.5%"]
	level_template(embed, level)
	level = ["Duration", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return sucrose_burst_data

def sayu_autoattack_data(embed):
	sayu_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "72.24%", "78.12%", "84%", "92.4%", "98.28%", "105%", "114.24%", "123.48%", "132.72%", "142.8%", "154.35%", "167.93%", "181.52%", "195.1%", "209.92%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "71.38%", "77.19%", "83%", "91.3%", "97.11%", "103.75%", "112.88%", "122.01%", "131.14%", "141.1%", "152.51%", "165.93%", "179.35%", "192.78%", "207.42%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "43.43% + 43.43%", "46.97% + 46.97%", "50.5% + 50.5%", "55.55% + 55.55%", "59.09% + 59.09%", "63.13% + 63.13%", "68.68% + 68.68%", "74.23% + 74.23%", "79.79% + 79.79%", "85.85% + 85.85%", "92.79% + 92.79%", "100.96% + 100.96%", "109.13% + 109.13%", "117.29% + 117.29%", "126.2% + 126.2%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "98.13%", "106.11%", "114.1%", "125.51%", "133.5%", "142.63%", "155.18%", "167.73%", "180.28%", "193.97%", "209.66%", "228.11%", "246.56%", "265.01%", "285.14%"]
	level_template(embed, level)
	return sayu_autoattack_data

def sayu_autoattack_data2(embed):
	sayu_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "62.55%", "67.64%", "72.73%", "80%", "85.09%", "90.91%", "98.91%", "106.91%", "114.91%", "123.64%", "133.64%", "145.4%", "157.16%", "168.92%", "181.75%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "113.09%", "122.3%", "131.5%", "144.65%", "153.86%", "164.38%", "178.84%", "193.31%", "207.77%", "223.55%", "241.63%", "262.89%", "284.16%", "305.42%", "328.62%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "157.85%", "168.26%", "178.66%", "189.07%", "199.48%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "315.63% / 394.24%", "336.44% / 420.23%", "357.25% / 446.23%", "378.06% / 472.22%", "398.87% / 498.21%"]
	level_template(embed, level)
	return sayu_autoattack_data2

def sayu_skill_data(embed):
	sayu_skill_data = discord.Embed(color=color)
	level = ["Fufu Windwheel DMG", "36%", "38.7%", "41.4%", "45%", "47.7%", "50.4%", "54%", "57.6%", "61.2%", "64.8%", "68.4%", "72%", "76.5%", "81%", "85.5%"]
	level_template(embed, level)
	level = ["Fufu Whirlwind Kick DMG", "158.4%", "170.28%", "182.16%", "198%", "209.88%", "221.76%", "237.6%", "253.44%", "269.28%", "285.12%", "300.96%", "316.8%", "336.6%", "356.4%", "376.2%"]
	level_template(embed, level)
	level = ["Fufu Whirlwind Kick DMG (Hold)", "217.6%", "233.92%", "250.24%", "272%", "288.32%", "304.64%", "326.4%", "348.16%", "369.92%", "391.68%", "413.44%", "435.2%", "462.4%", "489.6%", "516.8%"]
	level_template(embed, level)
	level = ["Fufu Windwheel Elemental DMG", "16.8%", "18.06%", "19.32%", "21%", "22.26%", "23.52%", "25.2%", "26.88%", "28.56%", "30.24%", "31.92%", "33.6%", "35.7%", "37.8%", "39.9%"]
	level_template(embed, level)
	level = ["Fufu Whirlwind Kick Elemental DMG", "76.16%", "81.87%", "87.58%", "95.2%", "100.91%", "106.62%", "114.24%", "121.86%", "129.47%", "137.09%", "144.7%", "152.32%", "161.84%", "171.36%", "180.88%"]
	level_template(embed, level)
	return sayu_skill_data

def sayu_skill_data2(embed):
	sayu_skill_data2 = discord.Embed(color=color)
	level = ["Max Duration (Hold)", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s", "6 to 11s"]
	level_template(embed, level)
	return sayu_skill_data2

def sayu_burst_data(embed):
	sayu_burst_data = discord.Embed(color=color)
	level = ["Burst Activation DMG", "116.8%", "125.56%", "134.32%", "146%", "154.76%", "163.52%", "175.2%", "186.88%", "198.56%", "210.24%", "221.92%", "233.6%", "248.2%", "262.8%", "277.4%"]
	level_template(embed, level)
	level = ["Burst Activation Healing", "92.16% ATK + 577", "99.07% ATK + 635", "105.98% ATK + 698", "115.2% ATK + 765", "122.11% ATK + 837", "129.02% ATK + 914", "138.24% ATK + 996", "147.46% ATK + 1083", "156.67% ATK + 1174", "165.89% ATK + 1270", "175.1% ATK + 1371", "184.32% ATK + 1477", "195.84% ATK + 1588", "207.36% ATK + 1703", "218.88% ATK + 1824"]
	level_template(embed, level)
	level = ["Muji-Muji Daruma DMG", "52%", "55.9%", "59.8%", "65%", "68.9%", "72.8%", "78%", "83.2%", "88.4%", "93.6%", "98.8%", "104%", "110.5%", "117%", "123.5%"]
	level_template(embed, level)
	level = ["Muji-Muji Daruma Healing", "79.87% ATK + 500", "85.86% ATK + 550", "91.85% ATK + 605", "99.84% ATK + 663", "105.83% ATK + 726", "111.82% ATK + 792", "119.81% ATK + 863", "127.8% ATK + 938", "135.78% ATK + 1017", "143.77% ATK + 1101", "151.76% ATK + 1188", "159.74% ATK + 1280", "169.73% ATK + 1376", "179.71% ATK + 1476", "189.7% ATK + 1580"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return sayu_burst_data

def jean_autoattack_data(embed):
	jean_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "48.33%", "52.27%", "56.2%", "61.82%", "65.75%", "70.25%", "76.43%", "82.61%", "88.8%", "95.54%", "103.27%", "112.36%", "121.44%", "130.53%", "140.44%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "45.58%", "49.29%", "53%", "58.3%", "62.01%", "66.25%", "72.08%", "77.91%", "83.74%", "90.1%", "97.39%", "105.96%", "114.53%", "123.1%", "132.45%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "60.29%", "65.19%", "70.1%", "77.11%", "82.02%", "87.63%", "95.34%", "103.05%", "110.76%", "119.17%", "128.81%", "140.14%", "151.48%", "162.81%", "175.18%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "65.88%", "71.24%", "76.6%", "84.26%", "89.62%", "95.75%", "104.18%", "112.6%", "121.03%", "130.22%", "140.75%", "153.14%", "165.52%", "177.91%", "191.42%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "79.21%", "85.65%", "92.1%", "101.31%", "107.76%", "115.13%", "125.26%", "135.39%", "145.52%", "156.57%", "169.23%", "184.13%", "199.02%", "213.91%", "230.16%"]
	level_template(embed, level)
	return jean_autoattack_data

def jean_autoattack_data2(embed):
	jean_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "162.02%", "175.21%", "188.4%", "207.24%", "220.43%", "235.5%", "256.22%", "276.95%", "297.67%", "320.28%", "346.19%", "376.65%", "407.11%", "437.58%", "470.81%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return jean_autoattack_data2

def jean_skill_data(embed):
	jean_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "292%", "313.9%", "335.8%", "365%", "386.9%", "408.8%", "438%", "467.2%", "496.4%", "525.6%", "554.8%", "584%", "620.5%", "657%", "693.5%"]
	level_template(embed, level)
	level = ["Stamina Consumption", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s", "20/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	return jean_skill_data

def jean_burst_data(embed):
	jean_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "424.8%", "456.66%", "488.52%", "531%", "562.86%", "594.72%", "637.2%", "679.68%", "722.16%", "764.64%", "807.12%", "849.6%", "902.7%", "955.8%", "1008.9%"]
	level_template(embed, level)
	level = ["Field Entering/Exiting DMG", "78.4%", "84.28%", "90.16%", "98%", "103.88%", "109.76%", "117.6%", "125.44%", "133.28%", "141.12%", "148.96%", "156.8%", "166.6%", "176.4%", "186.2%"]
	level_template(embed, level)
	level = ["Field Activation Healing", "251.2% ATK + 1540", "270.04% ATK + 1694", "288.88% ATK + 1861", "314% ATK + 2041", "332.84% ATK + 2234", "351.68% ATK + 2439", "376.8% ATK + 2657", "401.92% ATK + 2888", "427.04% ATK + 3132", "452.16% ATK + 3389", "477.28% ATK + 3659", "502.4% ATK + 3941", "533.8% ATK + 4236", "565.2% ATK + 4544", "596.6% ATK + 4865"]
	level_template(embed, level)
	level = ["Continuous Regen", "25.12% ATK + 154", "27% ATK + 169", "28.89% ATK + 186", "31.4% ATK + 204", "33.28% ATK + 223", "35.17% ATK + 244", "37.68% ATK + 266", "40.19% ATK + 289", "42.7% ATK + 313", "45.22% ATK + 339", "47.73% ATK + 366", "50.24% ATK + 394", "53.38% ATK + 424", "56.52% ATK + 454", "59.66% ATK + 487"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return jean_burst_data

def venti_autoattack_data(embed):
	venti_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "20.38% + 20.38%", "22.04% + 22.04%", "23.7% + 23.7%", "26.07% + 26.07%", "27.73% + 27.73%", "29.63% + 29.63%", "32.23% + 32.23%", "34.84% + 34.84%", "37.45% + 37.45%", "40.29% + 40.29%", "43.55% + 43.55%", "47.38% + 47.38%", "51.21% + 51.21%", "55.05% + 55.05%", "59.23% + 59.23%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "44.38%", "47.99%", "51.6%", "56.76%", "60.37%", "64.5%", "70.18%", "75.85%", "81.53%", "87.72%", "94.82%", "103.16%", "111.5%", "119.85%", "128.95%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "52.37%", "56.64%", "60.9%", "66.99%", "71.25%", "76.13%", "82.82%", "89.52%", "96.22%", "103.53%", "111.9%", "121.75%", "131.6%", "141.45%", "152.19%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "26.06% + 26.06%", "28.18% + 28.18%", "30.3% + 30.3%", "33.33% + 33.33%", "35.45% + 35.45%", "37.87% + 37.87%", "41.21% + 41.21%", "44.54% + 44.54%", "47.87% + 47.87%", "51.51% + 51.51%", "55.68% + 55.68%", "60.58% + 60.58%", "65.48% + 65.48%", "70.37% + 70.37%", "75.72% + 75.72%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "50.65%", "54.78%", "58.9%", "64.79%", "68.91%", "73.63%", "80.1%", "86.58%", "93.06%", "100.13%", "108.23%", "117.75%", "127.28%", "136.8%", "147.19%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "70.95%", "76.73%", "82.5%", "90.75%", "96.53%", "103.13%", "112.2%", "121.28%", "130.35%", "140.25%", "151.59%", "164.93%", "178.27%", "191.61%", "206.17%"]
	level_template(embed, level)
	return venti_autoattack_data

def venti_autoattack_data2(embed):
	venti_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "93.71%", "101.96%", "110.21%", "118.45%", "127.45%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "236.1%", "252.96%", "269.82%", "286.69%", "303.55%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return venti_autoattack_data2

def venti_skill_data(embed):
	venti_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "276%", "296.7%", "317.4%", "345%", "365.7%", "386.4%", "414%", "441.6%", "469.2%", "496.8%", "524.4%", "552%", "586.5%", "621%", "655.5%"]
	level_template(embed, level)
	level = ["Press CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["Hold DMG", "380%", "408.5%", "437%", "475%", "503.5%", "532%", "570%", "608%", "646%", "684%", "722%", "760%", "807.5%", "855%", "902.5%"]
	level_template(embed, level)
	level = ["CD (Hold)", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	return venti_skill_data

def venti_burst_data(embed):
	venti_burst_data = discord.Embed(color=color)
	level = ["DoT", "37.6%", "40.42%", "43.24%", "47%", "49.82%", "52.64%", "56.4%", "60.16%", "63.92%", "67.68%", "71.44%", "75.2%", "79.9%", "84.6%", "89.3%"]
	level_template(embed, level)
	level = ["Field Entering/Exiting DMG", "78.4%", "84.28%", "90.16%", "98%", "103.88%", "109.76%", "117.6%", "125.44%", "133.28%", "141.12%", "148.96%", "156.8%", "166.6%", "176.4%", "186.2%"]
	level_template(embed, level)
	level = ["Additional Elemental DMG", "18.8%", "20.21%", "21.62%", "23.5%", "24.91%", "26.32%", "28.2%", "30.08%", "31.96%", "33.84%", "35.72%", "37.6%", "39.95%", "42.3%", "44.65%"]
	level_template(embed, level)
	level = ["Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return venti_burst_data

def xiao_autoattack_data(embed):
	xiao_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "27.54% + 27.54%", "29.42% + 29.42%", "31.3% + 31.3%", "33.8% + 33.8%", "35.68% + 35.68%", "37.87% + 37.87%", "40.69% + 40.69%", "43.51% + 43.51%", "46.32% + 46.32%", "49.14% + 49.14%", "51.96% + 51.96%", "54.78% + 54.78%", "57.59% + 57.59%", "60.41% + 60.41%", "63.23% + 63.23%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "56.94%", "60.82%", "64.7%", "69.88%", "73.76%", "78.29%", "84.11%", "89.93%", "95.76%", "101.58%", "107.4%", "113.23%", "119.05%", "124.87%", "130.69%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "68.55%", "73.23%", "77.9%", "84.13%", "88.81%", "94.26%", "101.27%", "108.28%", "115.29%", "122.3%", "129.31%", "136.33%", "143.34%", "150.35%", "157.36%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "37.66% + 37.66%", "40.23% + 40.23%", "42.8% + 42.8%", "46.22% + 46.22%", "48.79% + 48.79%", "51.79% + 51.79%", "55.64% + 55.64%", "59.49% + 59.49%", "63.34% + 63.34%", "67.2% + 67.2%", "71.05% + 71.05%", "74.9% + 74.9%", "78.75% + 78.75%", "82.6% + 82.6%", "86.46% + 86.46%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "71.54%", "76.42%", "81.3%", "87.8%", "92.68%", "98.37%", "105.69%", "113.01%", "120.32%", "127.64%", "134.96%", "142.28%", "149.59%", "156.91%", "164.23%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "95.83%", "102.37%", "108.9%", "117.61%", "124.15%", "131.77%", "141.57%", "151.37%", "161.17%", "170.97%", "180.77%", "190.58%", "200.38%", "210.18%", "219.98%"]
	level_template(embed, level)
	return xiao_autoattack_data

def xiao_autoattack_data2(embed):
	xiao_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "121.09%", "129.34%", "137.6%", "148.61%", "156.86%", "166.5%", "178.88%", "191.26%", "203.65%", "216.03%", "228.42%", "240.8%", "253.18%", "265.57%", "277.95%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "81.83%", "88.49%", "95.16%", "104.67%", "111.33%", "118.94%", "129.41%", "139.88%", "150.35%", "161.76%", "173.18%", "184.6%", "196.02%", "207.44%", "218.86%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "163.63% / 204.39%", "176.95% / 221.02%", "190.27% / 237.66%", "209.3% / 261.42%", "222.62% / 278.06%", "237.84% / 297.07%", "258.77% / 323.21%", "279.7% / 349.36%", "300.63% / 375.5%", "323.46% / 404.02%", "346.29% / 432.54%", "369.12% / 461.06%", "391.96% / 489.57%", "414.79% / 518.09%", "437.62% / 546.61%"]
	level_template(embed, level)
	return xiao_autoattack_data2

def xiao_skill_data(embed):
	xiao_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "252.8%", "271.76%", "290.72%", "316%", "334.96%", "353.92%", "379.2%", "404.48%", "429.76%", "455.04%", "480.32%", "505.6%", "537.2%", "568.8%", "600.4%"]
	level_template(embed, level)
	level = ["CD", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return xiao_skill_data

def xiao_burst_data(embed):
	xiao_burst_data = discord.Embed(color=color)
	level = ["DMG Bonus", "58.45%", "61.95%", "65.45%", "70%", "73.5%", "77%", "81.55%", "86.1%", "90.65%", "95.2%", "99.75%", "104.3%", "108.85%", "113.4%", "117.95%"]
	level_template(embed, level)
	level = ["Life Drain", "3%/s", "3%/s", "3%/s", "2.5%/s", "2.5%/s", "2.5%/s", "2%/s", "2%/s", "2%/s", "2%/s", "2%/s", "2%/s", "2%/s", "2%/s", "2%/s"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s"]
	level_template(embed, level)
	level = ["Energy Cost", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70", "70"]
	level_template(embed, level)
	return xiao_burst_data

def kazuha_autoattack_data(embed):
	kazuha_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "44.98%", "48.64%", "52.3%", "57.53%", "61.19%", "65.38%", "71.13%", "76.88%", "82.63%", "88.91%", "96.1%", "104.56%", "113.02%", "121.47%", "130.7%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "45.24%", "48.92%", "52.6%", "57.86%", "61.54%", "65.75%", "71.54%", "77.32%", "83.11%", "89.42%", "96.65%", "105.16%", "113.66%", "122.17%", "131.45%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "25.8% + 30.96%", "27.9% + 33.48%", "30% + 36%", "33% + 39.6%", "35.1% + 42.12%", "37.5% + 45%", "40.8% + 48.96%", "44.1% + 52.92%", "47.4% + 56.88%", "51% + 61.2%", "55.13% + 66.15%", "59.98% + 71.97%", "64.83% + 77.79%", "69.68% + 83.61%", "74.97% + 89.96%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "60.72%", "65.66%", "70.6%", "77.66%", "82.6%", "88.25%", "96.02%", "103.78%", "111.55%", "120.02%", "129.73%", "141.14%", "152.56%", "163.98%", "176.43%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "25.37%×3", "27.44%×3", "29.5%×3", "32.45%×3", "34.52%×3", "36.88%×3", "40.12%×3", "43.37%×3", "46.61%×3", "50.15%×3", "54.21%×3", "58.98%×3", "63.75%×3", "68.52%×3", "73.72%×3"]
	level_template(embed, level)
	return kazuha_autoattack_data

def kazuha_autoattack_data2(embed):
	kazuha_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "43% + 74.65%", "46.5% + 80.72%", "50% + 86.8%", "55% + 95.48%", "58.5% + 101.56%", "62.5% + 108.5%", "68% + 118.05%", "73.5% + 127.6%", "79% + 137.14%", "85% + 147.56%", "91.88% + 159.5%", "99.96% + 173.53%", "108.05% + 187.57%", "116.13% + 201.6%", "124.95% + 216.91%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "81.83%", "88.49%", "95.16%", "104.67%", "111.33%", "118.94%", "129.41%", "139.88%", "150.35%", "161.76%", "173.18%", "184.6%", "196.02%", "207.44%", "218.86%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "163.63% / 204.39%", "176.95% / 221.02%", "190.27% / 237.66%", "209.3% / 261.42%", "222.62% / 278.06%", "237.84% / 297.07%", "258.77% / 323.21%", "279.7% / 349.36%", "300.63% / 375.5%", "323.46% / 404.02%", "346.29% / 432.54%", "369.12% / 461.06%", "391.96% / 489.57%", "414.79% / 518.09%", "437.62% / 546.61%"]
	level_template(embed, level)
	return kazuha_autoattack_data2

def kazuha_skill_data(embed):
	kazuha_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "192%", "206.4%", "220.8%", "240%", "254.4%", "268.8%", "288%", "307.2%", "326.4%", "345.6%", "364.8%", "384%", "408%", "432%", "456%"]
	level_template(embed, level)
	level = ["Press CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["Hold DMG", "260.8%", "280.36%", "299.92%", "326%", "345.56%", "365.12%", "391.2%", "417.28%", "443.36%", "469.44%", "495.52%", "521.6%", "554.2%", "586.8%", "619.4%"]
	level_template(embed, level)
	level = ["CD (Hold)", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s"]
	level_template(embed, level)
	return kazuha_skill_data

def kazuha_burst_data(embed):
	kazuha_burst_data = discord.Embed(color=color)
	level = ["Slashing DMG", "262.4%", "282.08%", "301.76%", "328%", "347.68%", "367.36%", "393.6%", "419.84%", "446.08%", "472.32%", "498.56%", "524.8%", "557.6%", "590.4%", "623.2%"]
	level_template(embed, level)
	level = ["DoT", "120%", "129%", "138%", "150%", "159%", "168%", "180%", "192%", "204%", "216%", "228%", "240%", "255%", "270%", "285%"]
	level_template(embed, level)
	level = ["Additional Elemental DMG", "36%", "38.7%", "41.4%", "45%", "47.7%", "50.4%", "54%", "57.6%", "61.2%", "64.8%", "68.4%", "72%", "76.5%", "81%", "85.5%"]
	level_template(embed, level)
	level = ["Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return kazuha_burst_data

# Geo

def noelle_autoattack_data(embed):
	noelle_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "79.12%", "85.56%", "92%", "101.2%", "107.64%", "115%", "125.12%", "135.24%", "145.36%", "156.4%", "167.44%", "178.48%", "189.52%", "200.56%", "211.6%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "73.36%", "79.33%", "85.3%", "93.83%", "99.8%", "106.63%", "116.01%", "125.39%", "134.77%", "145.01%", "155.25%", "165.48%", "175.72%", "185.95%", "196.19%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "86.26%", "93.28%", "100.3%", "110.33%", "117.35%", "125.38%", "136.41%", "147.44%", "158.47%", "170.51%", "182.55%", "194.58%", "206.62%", "218.65%", "230.69%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "113.43%", "122.67%", "131.9%", "145.09%", "154.32%", "164.88%", "179.38%", "193.89%", "208.4%", "224.23%", "240.06%", "255.89%", "271.71%", "287.54%", "303.37%"]
	level_template(embed, level)
	return noelle_autoattack_data

def noelle_autoattack_data2(embed):
	noelle_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "50.74%", "54.87%", "59%", "64.9%", "69.03%", "73.75%", "80.24%", "86.73%", "93.22%", "100.3%", "107.38%", "114.46%", "121.54%", "128.62%", "135.7%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "90.47%", "97.84%", "105.2%", "115.72%", "123.08%", "131.5%", "143.07%", "154.64%", "166.22%", "178.84%", "191.46%", "204.09%", "216.71%", "229.34%", "241.96%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "157.85%", "168.26%", "178.66%", "189.07%", "199.48%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "315.63% / 394.24%", "336.44% / 420.23%", "357.25% / 446.23%", "378.06% / 472.22%", "398.87% / 498.21%"]
	level_template(embed, level)
	return noelle_autoattack_data2

def noelle_skill_data(embed):
	noelle_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "120% DEF", "129% DEF", "138% DEF", "150% DEF", "159% DEF", "168% DEF", "180% DEF", "192% DEF", "204% DEF", "216% DEF", "228% DEF", "240% DEF", "255% DEF", "270% DEF", "285% DEF"]
	level_template(embed, level)
	level = ["Shield DMG Absorption", "160% DEF + 770", "172% DEF + 847", "184% DEF + 930", "200% DEF + 1020", "212% DEF + 1116", "224% DEF + 1219", "240% DEF + 1328", "256% DEF + 1443", "272% DEF + 1565", "288% DEF + 1694", "304% DEF + 1828", "320% DEF + 1970", "340% DEF + 2117", "360% DEF + 2271", "380% DEF + 2431"]
	level_template(embed, level)
	level = ["Healing", "21.28% DEF + 103", "22.88% DEF + 113", "24.47% DEF + 124", "26.6% DEF + 136", "28.2% DEF + 149", "29.79% DEF + 163", "31.92% DEF + 177", "34.05% DEF + 193", "36.18% DEF + 209", "38.3% DEF + 226", "40.43% DEF + 244", "42.56% DEF + 263", "45.22% DEF + 282", "47.88% DEF + 303", "50.54% DEF + 324"]
	level_template(embed, level)
	level = ["Healing Chance", "50%", "51%", "52%", "53%", "54%", "55%", "56%", "57%", "58%", "59%", "59%", "60%", "60%", "60%", "60%"]
	level_template(embed, level)
	level = ["Duration", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["CD", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s", "24s"]
	level_template(embed, level)
	return noelle_skill_data

def noelle_burst_data(embed):
	noelle_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "67.2%", "72.24%", "77.28%", "84%", "89.04%", "94.08%", "100.8%", "107.52%", "114.24%", "120.96%", "127.68%", "134.4%", "142.8%", "151.2%", "159.6%"]
	level_template(embed, level)
	level = ["ATK DMG Bonus", "92.8%", "99.76%", "106.72%", "116%", "122.96%", "129.92%", "139.2%", "148.48%", "157.76%", "167.04%", "176.32%", "185.6%", "197.2%", "208.8%", "220.4%"]
	level_template(embed, level)
	level = ["DEF Conversion Bonus", "40% DEF", "43% DEF", "46% DEF", "50% DEF", "53% DEF", "56% DEF", "60% DEF", "64% DEF", "68% DEF", "72% DEF", "76% DEF", "80% DEF", "85% DEF", "90% DEF", "95% DEF"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return noelle_burst_data

def ningguang_autoattack_data(embed):
	ningguang_autoattack_data = discord.Embed(color=color)
	level = ["Normal Attack DMG", "28%", "30.1%", "32.2%", "35%", "37.1%", "39.2%", "42%", "44.8%", "47.6%", "50.4%", "53.31%", "57.12%", "60.93%", "64.74%", "68.54%"]
	level_template(embed, level)
	level = ["Charged Attack DMG", "174.08%", "187.14%", "200.19%", "217.6%", "230.66%", "243.71%", "261.12%", "278.53%", "295.94%", "313.34%", "331.45%", "355.12%", "378.8%", "402.47%", "426.15%"]
	level_template(embed, level)
	level = ["DMG per Star Jade", "49.6%", "53.32%", "57.04%", "62%", "65.72%", "69.44%", "74.4%", "79.36%", "84.32%", "89.28%", "94.44%", "101.18%", "107.93%", "114.68%", "121.42%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return ningguang_autoattack_data

def ningguang_skill_data(embed):
	ningguang_skill_data = discord.Embed(color=color)
	level = ["Inherited HP", "50.1%", "53.1%", "56.1%", "60%", "63%", "66%", "69.9%", "73.8%", "77.7%", "81.6%", "85.5%", "89.4%", "93.3%", "97.2%", "101.1%"]
	level_template(embed, level)
	level = ["Skill DMG", "230.4%", "247.68%", "264.96%", "288%", "305.28%", "322.56%", "345.6%", "368.64%", "391.68%", "414.72%", "437.76%", "460.8%", "489.6%", "518.4%", "547.2%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	return ningguang_skill_data

def ningguang_burst_data(embed):
	ningguang_burst_data = discord.Embed(color=color)
	level = ["DMG Per Gem", "86.96%", "93.48%", "100%", "108.7%", "115.22%", "121.74%", "130.44%", "139.14%", "147.83%", "156.53%", "165.22%", "173.92%", "184.79%", "195.66%", "206.53%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return ningguang_burst_data

def zhongli_autoattack_data(embed):
	zhongli_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "30.77%", "33.27%", "35.78%", "39.36%", "41.86%", "44.72%", "48.66%", "52.59%", "56.53%", "60.82%", "65.74%", "71.53%", "77.31%", "83.1%", "89.41%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "31.15%", "33.69%", "36.22%", "39.85%", "42.38%", "45.28%", "49.26%", "53.25%", "57.23%", "61.58%", "66.56%", "72.42%", "78.27%", "84.13%", "90.52%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "38.58%", "41.72%", "44.86%", "49.34%", "52.48%", "56.07%", "61%", "65.94%", "70.87%", "76.26%", "82.42%", "89.68%", "96.93%", "104.18%", "112.1%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "42.94%", "46.43%", "49.93%", "54.92%", "58.42%", "62.41%", "67.9%", "73.4%", "78.89%", "84.88%", "91.74%", "99.82%", "107.89%", "115.97%", "124.77%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "10.75%×4", "11.63%×4", "12.5%×4", "13.75%×4", "14.63%×4", "15.63%×4", "17%×4", "18.38%×4", "19.75%×4", "21.25%×4", "22.97%×4", "24.99%×4", "27.01%×4", "29.03%×4", "31.24%×4"]
	level_template(embed, level)
	level = ["6-Hit DMG", "54.5%", "58.93%", "63.37%", "69.7%", "74.14%", "79.21%", "86.18%", "93.15%", "100.12%", "107.73%", "116.44%", "126.69%", "136.93%", "147.18%", "158.36%"]
	level_template(embed, level)
	return zhongli_autoattack_data

def zhongli_autoattack_data2(embed):
	zhongli_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "111.03%", "120.06%", "129.1%", "142.01%", "151.05%", "161.38%", "175.58%", "189.78%", "203.98%", "219.47%", "237.22%", "258.1%", "278.97%", "299.85%", "322.62%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return zhongli_autoattack_data2

def zhongli_skill_data(embed):
	zhongli_skill_data = discord.Embed(color=color)
	level = ["Stone Stele/Resonance DMG", "16% / 32%", "17.2% / 34.4%", "18.4% / 36.8%", "20% / 40%", "21.2% / 42.4%", "22.4% / 44.8%", "24% / 48%", "25.6% / 51.2%", "27.2% / 54.4%", "28.8% / 57.6%", "30.4% / 60.8%", "32% / 64%", "34% / 68%", "36% / 72%", "38% / 76%"]
	level_template(embed, level)
	level = ["Press CD", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s"]
	level_template(embed, level)
	level = ["Hold DMG", "80%", "86%", "92%", "100%", "106%", "112%", "120%", "128%", "136%", "144%", "152%", "160%", "170%", "180%", "190%"]
	level_template(embed, level)
	level = ["Shield Base Absorption", "1232", "1356", "1489", "1633", "1787", "1951", "2126", "2311", "2506", "2712", "2927", "3153", "3389", "3636", "3893"]
	level_template(embed, level)
	return zhongli_skill_data

def zhongli_skill_data2(embed):
	zhongli_skill_data2 = discord.Embed(color=color)
	level = ["Additional Shield Absorption", "12.8% Max HP", "13.76% Max HP", "14.72% Max HP", "16% Max HP", "16.96% Max HP", "17.92% Max HP", "19.2% Max HP", "20.48% Max HP", "21.76% Max HP", "23.04% Max HP", "24.32% Max HP", "25.6% Max HP", "27.2% Max HP", "28.8% Max HP", "30.4% Max HP"]
	level_template(embed, level)
	level = ["Shield Duration", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["CD (Hold)", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	return zhongli_skill_data2

def zhongli_burst_data(embed):
	zhongli_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "401.08%", "444.44%", "487.8%", "542%", "590.78%", "639.56%", "704.6%", "769.64%", "834.68%", "899.72%", "964.76%", "1029.8%", "1084%", "1138.2%", "1192.4%"]
	level_template(embed, level)
	level = ["Petrification Duration", "3.1s", "3.2s", "3.3s", "3.4s", "3.5s", "3.6s", "3.7s", "3.8s", "3.9s", "4s", "4s", "4s", "4s", "4s", "4s"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return zhongli_burst_data

def albedo_autoattack_data(embed):
	albedo_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "36.74%", "39.73%", "42.72%", "46.99%", "49.98%", "53.4%", "58.1%", "62.8%", "67.5%", "72.62%", "78.5%", "85.41%", "92.31%", "99.22%", "106.76%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "36.74%", "39.73%", "42.72%", "46.99%", "49.98%", "53.4%", "58.1%", "62.8%", "67.5%", "72.62%", "78.5%", "85.41%", "92.31%", "99.22%", "106.76%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "47.45%", "51.32%", "55.18%", "60.7%", "64.56%", "68.98%", "75.04%", "81.11%", "87.18%", "93.81%", "101.39%", "110.32%", "119.24%", "128.16%", "137.89%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "49.75%", "53.8%", "57.85%", "63.64%", "67.68%", "72.31%", "78.68%", "85.04%", "91.4%", "98.35%", "106.3%", "115.65%", "125.01%", "134.36%", "144.57%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "62.07%", "67.13%", "72.18%", "79.4%", "84.45%", "90.22%", "98.16%", "106.1%", "114.04%", "122.7%", "132.63%", "144.3%", "155.97%", "167.64%", "180.38%"]
	level_template(embed, level)
	return albedo_autoattack_data

def albedo_autoattack_data2(embed):
	albedo_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "47.3% + 60.2%", "51.15% + 65.1%", "55% + 70%", "60.5% + 77%", "64.35% + 81.9%", "68.75% + 87.5%", "74.8% + 95.2%", "80.85% + 102.9%", "86.9% + 110.6%", "93.5% + 119%", "101.06% + 128.62%", "109.96% + 139.94%", "118.85% + 151.26%", "127.74% + 162.58%", "137.45% + 174.93%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return albedo_autoattack_data2

def albedo_skill_data(embed):
	albedo_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "130.4%", "140.18%", "149.96%", "163%", "172.78%", "182.56%", "195.6%", "208.64%", "221.68%", "234.72%", "247.76%", "260.8%", "277.1%", "293.4%", "309.7%"]
	level_template(embed, level)
	level = ["Transient Blossom DMG", "133.6% DEF", "143.62% DEF", "153.64% DEF", "167% DEF", "177.02% DEF", "187.04% DEF", "200.4% DEF", "213.76% DEF", "227.12% DEF", "240.48% DEF", "253.84% DEF", "267.2% DEF", "283.9% DEF", "300.6% DEF", "317.3% DEF"]
	level_template(embed, level)
	level = ["Duration", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s"]
	level_template(embed, level)
	level = ["CD", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s"]
	level_template(embed, level)
	return albedo_skill_data

def albedo_burst_data(embed):
	albedo_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "367.2%", "394.74%", "422.28%", "459%", "486.54%", "514.08%", "550.8%", "587.52%", "624.24%", "660.96%", "697.68%", "734.4%", "780.3%", "826.2%", "872.1%"]
	level_template(embed, level)
	level = ["Fatal Blossom DMG", "72% each", "77.4% each", "82.8% each", "90% each", "95.4% each", "100.8% each", "108% each", "115.2% each", "122.4% each", "129.6% each", "136.8% each", "144% each", "153% each", "162% each", "171% each"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return albedo_burst_data

# Electro

def lisa_autoattack_data(embed):
	lisa_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "39.6%", "42.57%", "45.54%", "49.5%", "52.47%", "55.44%", "59.4%", "63.36%", "67.32%", "71.28%", "75.4%", "80.78%", "86.17%", "91.56%", "96.94%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "35.92%", "38.61%", "41.31%", "44.9%", "47.59%", "50.29%", "53.88%", "57.47%", "61.06%", "64.66%", "68.39%", "73.28%", "78.16%", "83.05%", "87.93%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "42.8%", "46.01%", "49.22%", "53.5%", "56.71%", "59.92%", "64.2%", "68.48%", "72.76%", "77.04%", "81.49%", "87.31%", "93.13%", "98.95%", "104.77%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "54.96%", "59.08%", "63.2%", "68.7%", "72.82%", "76.94%", "82.44%", "87.94%", "93.43%", "98.93%", "104.64%", "112.12%", "119.59%", "127.07%", "134.54%"]
	level_template(embed, level)
	return lisa_autoattack_data

def lisa_autoattack_data2(embed):
	lisa_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "177.12%", "190.4%", "203.69%", "221.4%", "234.68%", "247.97%", "265.68%", "283.39%", "301.1%", "318.82%", "337.24%", "361.32%", "385.41%", "409.5%", "433.59%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return lisa_autoattack_data2

def lisa_skill_data(embed):
	lisa_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "80%", "86%", "92%", "100%", "106%", "112%", "120%", "128%", "136%", "144%", "152%", "160%", "170%", "180%", "190%"]
	level_template(embed, level)
	level = ["Press CD", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s"]
	level_template(embed, level)
	level = ["Non-Conductive Hold DMG", "320%", "344%", "368%", "400%", "424%", "448%", "480%", "512%", "544%", "576%", "608%", "640%", "680%", "720%", "760%"]
	level_template(embed, level)
	return lisa_skill_data

def lisa_skill_data2(embed):
	lisa_skill_data2 = discord.Embed(color=color)
	level = ["Stack 1 Conductive Hold DMG", "368%", "395.6%", "423.2%", "460%", "487.6%", "515.2%", "552%", "588.8%", "625.6%", "662.4%", "699.2%", "736%", "782%", "828%", "874%"]
	level_template(embed, level)
	level = ["Stack 2 Conductive Hold DMG", "424%", "455.8%", "487.6%", "530%", "561.8%", "593.6%", "636%", "678.4%", "720.8%", "763.2%", "805.6%", "848%", "901%", "954%", "1007%"]
	level_template(embed, level)
	level = ["Stack 3 Conductive Hold DMG", "487.2%", "523.74%", "560.28%", "609%", "645.54%", "682.08%", "730.8%", "779.52%", "828.24%", "876.96%", "925.68%", "974.4%", "1035.3%", "1096.2%", "1157.1%"]
	level_template(embed, level)
	level = ["CD (Hold)", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s"]
	level_template(embed, level)
	return lisa_skill_data2

def lisa_burst_data(embed):
	lisa_burst_data = discord.Embed(color=color)
	level = ["Discharge DMG", "36.56%", "39.3%", "42.04%", "45.7%", "48.44%", "51.18%", "54.84%", "58.5%", "62.15%", "65.81%", "69.46%", "73.12%", "77.69%", "82.26%", "86.83%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return lisa_burst_data

def fischl_autoattack_data(embed):
	fischl_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "44.12%", "47.71%", "51.3%", "56.43%", "60.02%", "64.13%", "69.77%", "75.41%", "81.05%", "87.21%", "93.37%", "99.52%", "105.68%", "111.83%", "117.99%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "46.78%", "50.59%", "54.4%", "59.84%", "63.65%", "68%", "73.98%", "79.97%", "85.95%", "92.48%", "99.01%", "105.54%", "112.06%", "118.59%", "125.12%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "58.14%", "62.87%", "67.6%", "74.36%", "79.09%", "84.5%", "91.94%", "99.37%", "106.81%", "114.92%", "123.03%", "131.14%", "139.26%", "147.37%", "155.48%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "57.71%", "62.4%", "67.1%", "73.81%", "78.51%", "83.88%", "91.26%", "98.64%", "106.02%", "114.07%", "122.12%", "130.17%", "138.23%", "146.28%", "154.33%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "72.07%", "77.93%", "83.8%", "92.18%", "98.05%", "104.75%", "113.97%", "123.19%", "132.4%", "142.46%", "152.52%", "162.57%", "172.63%", "182.68%", "192.74%"]
	level_template(embed, level)
	return fischl_autoattack_data

def fischl_autoattack_data2(embed):
	fischl_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "92.82%", "98.94%", "105.06%", "111.18%", "117.3%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "235.6%", "248%", "263.5%", "279%", "294.5%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return fischl_autoattack_data2

def fischl_skill_data(embed):
	fischl_skill_data = discord.Embed(color=color)
	level = ["Oz's ATK DMG", "88.8%", "95.46%", "102.12%", "111%", "117.66%", "124.32%", "133.2%", "142.08%", "150.96%", "159.84%", "168.72%", "177.6%", "188.7%", "199.8%", "210.9%"]
	level_template(embed, level)
	level = ["Summoning DMG", "115.44%", "124.1%", "132.76%", "144.3%", "152.96%", "161.62%", "173.16%", "184.7%", "196.25%", "207.79%", "219.34%", "230.88%", "245.31%", "259.74%", "274.17%"]
	level_template(embed, level)
	level = ["Oz's Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s", "25s"]
	level_template(embed, level)
	return fischl_skill_data

def fischl_burst_data(embed):
	fischl_burst_data = discord.Embed(color=color)
	level = ["Falling Thunder DMG", "208%", "223.6%", "239.2%", "260%", "275.6%", "291.2%", "312%", "332.8%", "353.6%", "374.4%", "395.2%", "416%", "442%", "468%", "494%"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return fischl_burst_data

def razor_autoattack_data(embed):
	razor_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "95.92%", "102.46%", "109%", "117.72%", "124.26%", "131.89%", "141.7%", "151.51%", "161.32%", "171.13%", "180.94%", "190.75%", "200.56%", "210.37%", "220.18%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "82.63%", "88.27%", "93.9%", "101.41%", "107.05%", "113.62%", "122.07%", "130.52%", "138.97%", "147.42%", "155.87%", "164.33%", "172.78%", "181.23%", "189.68%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "103.31%", "110.36%", "117.4%", "126.79%", "133.84%", "142.05%", "152.62%", "163.19%", "173.75%", "184.32%", "194.88%", "205.45%", "216.02%", "226.58%", "237.15%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "136.05%", "145.32%", "154.6%", "166.97%", "176.24%", "187.07%", "200.98%", "214.89%", "228.81%", "242.72%", "256.64%", "270.55%", "284.46%", "298.38%", "312.29%"]
	level_template(embed, level)
	return razor_autoattack_data

def razor_autoattack_data2(embed):
	razor_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "62.54%", "67.63%", "72.72%", "79.99%", "85.08%", "90.9%", "98.9%", "106.9%", "114.9%", "123.62%", "132.35%", "141.08%", "149.8%", "158.53%", "167.26%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "113.09%", "122.3%", "131.5%", "144.65%", "153.86%", "164.38%", "178.84%", "193.31%", "207.77%", "223.55%", "239.33%", "255.11%", "270.89%", "286.67%", "302.45%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "82.05%", "88.72%", "95.4%", "104.94%", "111.62%", "119.25%", "129.75%", "140.24%", "150.74%", "162.19%", "173.63%", "185.08%", "196.53%", "207.98%", "219.43%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "164.06% / 204.92%", "177.41% / 221.6%", "190.77% / 238.28%", "209.84% / 262.1%", "223.2% / 278.78%", "238.46% / 297.85%", "259.44% / 324.06%", "280.43% / 350.27%", "301.41% / 376.48%", "324.3% / 405.07%", "347.19% / 433.66%", "370.09% / 462.26%", "392.98% / 490.85%", "415.87% / 519.44%", "438.76% / 548.04%"]
	level_template(embed, level)
	return razor_autoattack_data2

def razor_skill_data(embed):
	razor_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "199.2%", "214.14%", "229.08%", "249%", "263.94%", "278.88%", "298.8%", "318.72%", "338.64%", "358.56%", "378.48%", "398.4%", "423.3%", "448.2%", "473.1%"]
	level_template(embed, level)
	level = ["Hold DMG", "295.2%", "317.34%", "339.48%", "369%", "391.14%", "413.28%", "442.8%", "472.32%", "501.84%", "531.36%", "560.88%", "590.4%", "627.3%", "664.2%", "701.1%"]
	level_template(embed, level)
	level = ["Energy Recharge Bonus", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil", "20%/sigil"]
	level_template(embed, level)
	level = ["Energy Regenerated", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil", "5/sigil"]
	level_template(embed, level)
	return razor_skill_data

def razor_skill_data2(embed):
	razor_skill_data2 = discord.Embed(color=color)
	level = ["Electro Sigil Duration", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s"]
	level_template(embed, level)
	level = ["Press CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["CD (Hold)", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return razor_skill_data2

def razor_burst_data(embed):
	razor_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "160%", "172%", "184%", "200%", "212%", "224%", "240%", "256%", "272%", "288%", "304%", "320%", "340%", "360%", "380%"]
	level_template(embed, level)
	level = ["Soul Companion DMG", "24%", "25.8%", "27.6%", "30%", "31.8%", "33.6%", "36%", "38.4%", "40.8%", "43.2%", "45.6%", "48%", "51%", "54%", "57%"]
	level_template(embed, level)
	level = ["ATK SPD Bonus", "26%", "28%", "30%", "32%", "34%", "36%", "37%", "38%", "39%", "40%", "40%", "40%", "40%", "40%", "40%"]
	level_template(embed, level)
	level = ["Electro RES Bonus", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%", "80%"]
	level_template(embed, level)
	return razor_burst_data

def razor_burst_data2(embed):
	razor_burst_data2 = discord.Embed(color=color)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return razor_burst_data2

def beidou_autoattack_data(embed):
	beidou_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "71.12%", "76.91%", "82.7%", "90.97%", "96.76%", "103.38%", "112.47%", "121.57%", "130.67%", "140.59%", "151.96%", "165.33%", "178.71%", "192.08%", "206.67%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "70.86%", "76.63%", "82.4%", "90.64%", "96.41%", "103%", "112.06%", "121.13%", "130.19%", "140.08%", "151.41%", "164.73%", "178.06%", "191.38%", "205.92%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "88.32%", "95.51%", "102.7%", "112.97%", "120.16%", "128.38%", "139.67%", "150.97%", "162.27%", "174.59%", "188.71%", "205.32%", "221.92%", "238.53%", "256.65%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "86.52%", "93.56%", "100.6%", "110.66%", "117.7%", "125.75%", "136.82%", "147.88%", "158.95%", "171.02%", "184.85%", "201.12%", "217.39%", "233.65%", "251.4%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "112.14%", "121.27%", "130.4%", "143.44%", "152.57%", "163%", "177.34%", "191.69%", "206.03%", "221.68%", "239.61%", "260.7%", "281.78%", "302.87%", "325.87%"]
	level_template(embed, level)
	return beidou_autoattack_data

def beidou_autoattack_data2(embed):
	beidou_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "56.24%", "60.82%", "65.4%", "71.94%", "76.52%", "81.75%", "88.94%", "96.14%", "103.33%", "111.18%", "120.17%", "130.75%", "141.32%", "151.9%", "163.43%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "101.82%", "110.11%", "118.4%", "130.24%", "138.53%", "148%", "161.02%", "174.05%", "187.07%", "201.28%", "217.56%", "236.71%", "255.85%", "275%", "295.88%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "157.85%", "168.26%", "178.66%", "189.07%", "199.48%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "315.63% / 394.24%", "336.44% / 420.23%", "357.25% / 446.23%", "378.06% / 472.22%", "398.87% / 498.21%"]
	level_template(embed, level)
	return beidou_autoattack_data2

def beidou_skill_data(embed):
	beidou_skill_data = discord.Embed(color=color)
	level = ["Shield DMG Absorption", "14.4% Max HP + 1386", "15.48% Max HP + 1525", "16.56% Max HP + 1675", "18% Max HP + 1837", "19.08% Max HP + 2010", "20.16% Max HP + 2195", "21.6% Max HP + 2392", "23.04% Max HP + 2600", "24.48% Max HP + 2819", "25.92% Max HP + 3050", "27.36% Max HP + 3293", "28.8% Max HP + 3547", "30.6% Max HP + 3813", "32.4% Max HP + 4090", "34.2% Max HP + 4379"]
	level_template(embed, level)
	level = ["Base DMG", "121.6%", "130.72%", "139.84%", "152%", "161.12%", "170.24%", "182.4%", "194.56%", "206.72%", "218.88%", "231.04%", "243.2%", "258.4%", "273.6%", "288.8%"]
	level_template(embed, level)
	level = ["DMG Bonus on Hit Taken", "160%", "172%", "184%", "200%", "212%", "224%", "240%", "256%", "272%", "288%", "304%", "320%", "340%", "360%", "380%"]
	level_template(embed, level)
	level = ["CD", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s"]
	level_template(embed, level)
	return beidou_skill_data

def beidou_burst_data(embed):
	beidou_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "121.6%", "130.72%", "139.84%", "152%", "161.12%", "170.24%", "182.4%", "194.56%", "206.72%", "218.88%", "231.04%", "243.2%", "258.4%", "273.6%", "288.8%"]
	level_template(embed, level)
	level = ["Lightning DMG", "96%", "103.2%", "110.4%", "120%", "127.2%", "134.4%", "144%", "153.6%", "163.2%", "172.8%", "182.4%", "192%", "204%", "216%", "228%"]
	level_template(embed, level)
	level = ["DMG Reduction", "20%", "21%", "22%", "24%", "25%", "26%", "28%", "30%", "32%", "34%", "35%", "36%", "37%", "38%", "39%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return beidou_burst_data

def keqing_autoattack_data(embed):
	keqing_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "41.02%", "44.36%", "47.7%", "52.47%", "55.81%", "59.62%", "64.87%", "70.12%", "75.37%", "81.09%", "86.81%", "92.54%", "98.26%", "103.99%", "109.71%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "41.02%", "44.36%", "47.7%", "52.47%", "55.81%", "59.62%", "64.87%", "70.12%", "75.37%", "81.09%", "86.81%", "92.54%", "98.26%", "103.99%", "109.71%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "54.44%", "58.87%", "63.3%", "69.63%", "74.06%", "79.13%", "86.09%", "93.05%", "100.01%", "107.61%", "115.21%", "122.8%", "130.4%", "137.99%", "145.59%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "31.48% + 34.4%", "34.04% + 37.2%", "36.6% + 40%", "40.26% + 44%", "42.82% + 46.8%", "45.75% + 50%", "49.78% + 54.4%", "53.8% + 58.8%", "57.83% + 63.2%", "62.22% + 68%", "66.61% + 72.8%", "71% + 77.6%", "75.4% + 82.4%", "79.79% + 87.2%", "84.18% + 92%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "66.99%", "72.45%", "77.9%", "85.69%", "91.14%", "97.38%", "105.94%", "114.51%", "123.08%", "132.43%", "141.78%", "151.13%", "160.47%", "169.82%", "179.17%"]
	level_template(embed, level)
	return keqing_autoattack_data

def keqing_autoattack_data2(embed):
	keqing_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "76.8% + 86%", "83.05% + 93%", "89.3% + 100%", "98.23% + 110%", "104.48% + 117%", "111.63% + 125%", "121.45% + 136%", "131.27% + 147%", "141.09% + 158%", "151.81% + 170%", "162.53% + 182%", "173.24% + 194%", "183.96% + 206%", "194.67% + 218%", "205.39% + 230%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return keqing_autoattack_data2

def keqing_skill_data(embed):
	keqing_skill_data = discord.Embed(color=color)
	level = ["Lightning Stiletto DMG", "50.4%", "54.18%", "57.96%", "63%", "66.78%", "70.56%", "75.6%", "80.64%", "85.68%", "90.72%", "95.76%", "100.8%", "107.1%", "113.4%", "119.7%"]
	level_template(embed, level)
	level = ["Slashing DMG", "168%", "180.6%", "193.2%", "210%", "222.6%", "235.2%", "252%", "268.8%", "285.6%", "302.4%", "319.2%", "336%", "357%", "378%", "399%"]
	level_template(embed, level)
	level = ["Thunderclap Slash DMG", "84%×2", "90.3%×2", "96.6%×2", "105%×2", "111.3%×2", "117.6%×2", "126%×2", "134.4%×2", "142.8%×2", "151.2%×2", "159.6%×2", "168%×2", "178.5%×2", "189%×2", "199.5%×2"]
	level_template(embed, level)
	level = ["CD", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s", "7.5s"]
	level_template(embed, level)
	return keqing_skill_data

def keqing_burst_data(embed):
	keqing_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "88%", "94.6%", "101.2%", "110%", "116.6%", "123.2%", "132%", "140.8%", "149.6%", "158.4%", "167.2%", "176%", "187%", "198%", "209%"]
	level_template(embed, level)
	level = ["Consecutive Slash DMG", "24%*8", "25.8%*8", "27.6%*8", "30%*8", "31.8%*8", "33.6%*8", "36%*8", "38.4%*8", "40.8%*8", "43.2%*8", "45.6%*8", "48%*8", "51%*8", "54%*8", "57%*8"]
	level_template(embed, level)
	level = ["Last Attack DMG", "188.8%", "202.96%", "217.12%", "236%", "250.16%", "264.32%", "283.2%", "302.08%", "320.96%", "339.84%", "358.72%", "377.6%", "401.2%", "424.8%", "448.4%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return keqing_burst_data

# Hydro

def barbara_autoattack_data(embed):
	barbara_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "37.84%", "40.68%", "43.52%", "47.3%", "50.14%", "52.98%", "56.76%", "60.54%", "64.33%", "68.11%", "72.05%", "77.19%", "82.34%", "87.49%", "92.63%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "35.52%", "38.18%", "40.85%", "44.4%", "47.06%", "49.73%", "53.28%", "56.83%", "60.38%", "63.94%", "67.63%", "72.46%", "77.29%", "82.12%", "86.95%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "41.04%", "44.12%", "47.2%", "51.3%", "54.38%", "57.46%", "61.56%", "65.66%", "69.77%", "73.87%", "78.14%", "83.72%", "89.3%", "94.88%", "100.47%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "55.2%", "59.34%", "63.48%", "69%", "73.14%", "77.28%", "82.8%", "88.32%", "93.84%", "99.36%", "105.1%", "112.61%", "120.12%", "127.62%", "135.13%"]
	level_template(embed, level)
	return barbara_autoattack_data

def barbara_autoattack_data2(embed):
	barbara_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "166.24%", "178.71%", "191.18%", "207.8%", "220.27%", "232.74%", "249.36%", "265.98%", "282.61%", "299.23%", "316.52%", "339.13%", "361.74%", "384.35%", "406.96%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return barbara_autoattack_data2

def barbara_skill_data(embed):
	barbara_skill_data = discord.Embed(color=color)
	level = ["HP Regen Per Hit", "0.75% Max HP + 72", "0.81% Max HP + 79", "0.86% Max HP + 87", "0.94% Max HP + 96", "0.99% Max HP + 105", "1.05% Max HP + 114", "1.13% Max HP + 125", "1.2% Max HP + 135", "1.27% Max HP + 147", "1.35% Max HP + 159", "1.43% Max HP + 172", "1.5% Max HP + 185", "1.59% Max HP + 199", "1.69% Max HP + 213", "1.78% Max HP + 228"]
	level_template(embed, level)
	level = ["Continuous Regen", "4% Max HP + 385", "4.3% Max HP + 424", "4.6% Max HP + 465", "5% Max HP + 510", "5.3% Max HP + 559", "5.6% Max HP + 610", "6% Max HP + 664", "6.4% Max HP + 722", "6.8% Max HP + 783", "7.2% Max HP + 847", "7.6% Max HP + 915", "8% Max HP + 986", "8.5% Max HP + 1059", "9% Max HP + 1136", "9.5% Max HP + 1217"]
	level_template(embed, level)
	level = ["Droplet DMG", "58.4%", "62.78%", "67.16%", "73%", "77.38%", "81.76%", "87.6%", "93.44%", "99.28%", "105.12%", "110.96%", "116.8%", "124.1%", "131.4%", "138.7%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s", "32s"]
	level_template(embed, level)
	return barbara_skill_data

def barbara_burst_data(embed):
	barbara_burst_data = discord.Embed(color=color)
	level = ["Healing", "17.6% Max HP + 1694", "18.92% Max HP + 1864", "20.24% Max HP + 2047", "22% Max HP + 2245", "23.32% Max HP + 2457", "24.64% Max HP + 2683", "26.4% Max HP + 2923", "28.16% Max HP + 3177", "29.92% Max HP + 3445", "31.68% Max HP + 3728", "33.44% Max HP + 4024", "35.2% Max HP + 4335", "37.4% Max HP + 4660", "39.6% Max HP + 4999", "41.8% Max HP + 5352"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return barbara_burst_data

def xingqiu_autoattack_data(embed):
	xingqiu_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "46.61%", "50.41%", "54.2%", "59.62%", "63.41%", "67.75%", "73.71%", "79.67%", "85.64%", "92.14%", "99.59%", "108.36%", "117.12%", "125.88%", "135.45%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "47.64%", "51.52%", "55.4%", "60.94%", "64.82%", "69.25%", "75.34%", "81.44%", "87.53%", "94.18%", "101.8%", "110.76%", "119.71%", "128.67%", "138.44%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "28.55% + 28.55%", "30.88% + 30.88%", "33.2% + 33.2%", "36.52% + 36.52%", "38.84% + 38.84%", "41.5% + 41.5%", "45.15% + 45.15%", "48.8% + 48.8%", "52.46% + 52.46%", "56.44% + 56.44%", "61.01% + 61.01%", "66.37% + 66.37%", "71.74% + 71.74%", "77.11% + 77.11%", "82.97% + 82.97%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "55.99%", "60.54%", "65.1%", "71.61%", "76.17%", "81.38%", "88.54%", "95.7%", "102.86%", "110.67%", "119.62%", "130.15%", "140.67%", "151.2%", "162.68%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "35.86% + 35.86%", "38.78% + 38.78%", "41.7% + 41.7%", "45.87% + 45.87%", "48.79% + 48.79%", "52.13% + 52.13%", "56.71% + 56.71%", "61.3% + 61.3%", "65.89% + 65.89%", "70.89% + 70.89%", "76.62% + 76.62%", "83.37% + 83.37%", "90.11% + 90.11%", "96.85% + 96.85%", "104.21% + 104.21%"]
	level_template(embed, level)
	return xingqiu_autoattack_data

def xingqiu_autoattack_data2(embed):
	xingqiu_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "47.3% + 56.16%", "51.15% + 60.73%", "55% + 65.3%", "60.5% + 71.83%", "64.35% + 76.4%", "68.75% + 81.63%", "74.8% + 88.81%", "80.85% + 95.99%", "86.9% + 103.17%", "93.5% + 111.01%", "101.06% + 119.99%", "109.96% + 130.55%", "118.85% + 141.11%", "127.74% + 151.67%", "137.45% + 163.18%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return xingqiu_autoattack_data2

def xingqiu_skill_data(embed):
	xingqiu_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "168% + 191.2%", "180.6% + 205.54%", "193.2% + 219.88%", "210% + 239%", "222.6% + 253.34%", "235.2% + 267.68%", "252% + 286.8%", "268.8% + 305.92%", "285.6% + 325.04%", "302.4% + 344.16%", "319.2% + 363.28%", "336% + 382.4%", "357% + 406.3%", "378% + 430.2%", "399% + 454.1%"]
	level_template(embed, level)
	level = ["Damage Reduction Ratio", "20%", "21%", "22%", "23%", "24%", "25%", "26%", "27%", "28%", "29%", "29%", "29%", "29%", "29%", "29%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s", "21s"]
	level_template(embed, level)
	return xingqiu_skill_data

def xingqiu_burst_data(embed):
	xingqiu_burst_data = discord.Embed(color=color)
	level = ["Sword Rain DMG", "54.27%", "58.34%", "62.41%", "67.84%", "71.91%", "75.98%", "81.41%", "86.84%", "92.26%", "97.69%", "103.12%", "108.54%", "115.33%", "122.11%", "128.9%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return xingqiu_burst_data

def mona_autoattack_data(embed):
	mona_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "37.6%", "40.42%", "43.24%", "47%", "49.82%", "52.64%", "56.4%", "60.16%", "63.92%", "67.68%", "71.44%", "75.2%", "79.9%", "84.6%", "89.3%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "36%", "38.7%", "41.4%", "45%", "47.7%", "50.4%", "54%", "57.6%", "61.2%", "64.8%", "68.4%", "72%", "76.5%", "81%", "85.5%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "44.8%", "48.16%", "51.52%", "56%", "59.36%", "62.72%", "67.2%", "71.68%", "76.16%", "80.64%", "85.12%", "89.6%", "95.2%", "100.8%", "106.4%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "56.16%", "60.37%", "64.58%", "70.2%", "74.41%", "78.62%", "84.24%", "89.86%", "95.47%", "101.09%", "106.7%", "112.32%", "119.34%", "126.36%", "133.38%"]
	level_template(embed, level)
	return mona_autoattack_data

def mona_autoattack_data2(embed):
	mona_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "149.72%", "160.95%", "172.18%", "187.15%", "198.38%", "209.61%", "224.58%", "239.55%", "254.52%", "269.5%", "285.07%", "305.43%", "325.79%", "346.15%", "366.51%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return mona_autoattack_data2

def mona_skill_data(embed):
	mona_skill_data = discord.Embed(color=color)
	level = ["DoT", "32%", "34.4%", "36.8%", "40%", "42.4%", "44.8%", "48%", "51.2%", "54.4%", "57.6%", "60.8%", "64%", "68%", "72%", "76%"]
	level_template(embed, level)
	level = ["Explosion DMG", "132.8%", "142.76%", "152.72%", "166%", "175.96%", "185.92%", "199.2%", "212.48%", "225.76%", "239.04%", "252.32%", "265.6%", "282.2%", "298.8%", "315.4%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	return mona_skill_data

def mona_burst_data(embed):
	mona_burst_data = discord.Embed(color=color)
	level = ["Illusory Bubble Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["Illusory Bubble Explosion", "442.4%", "475.58%", "508.76%", "553%", "586.18%", "619.36%", "663.6%", "707.84%", "752.08%", "796.32%", "840.56%", "884.8%", "940.1%", "995.4%", "1050.7%"]
	level_template(embed, level)
	level = ["DMG Bonus", "42%", "44%", "46%", "48%", "50%", "52%", "54%", "56%", "58%", "60%", "60%", "60%", "60%", "60%", "60%"]
	level_template(embed, level)
	level = ["Omen Duration", "4s", "4s", "4s", "4.5s", "4.5s", "4.5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return mona_burst_data

def tartaglia_autoattack_data(embed):
	tartaglia_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "41.28%", "44.64%", "48%", "52.8%", "56.16%", "60%", "65.28%", "70.56%", "75.84%", "81.6%", "87.36%", "93.12%", "98.88%", "104.64%", "110.4%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "46.27%", "50.03%", "53.8%", "59.18%", "62.95%", "67.25%", "73.17%", "79.09%", "85%", "91.46%", "97.92%", "104.37%", "110.83%", "117.28%", "123.74%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "55.38%", "59.89%", "64.4%", "70.84%", "75.35%", "80.5%", "87.58%", "94.67%", "101.75%", "109.48%", "117.21%", "124.94%", "132.66%", "140.39%", "148.12%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "57.02%", "61.66%", "66.3%", "72.93%", "77.57%", "82.88%", "90.17%", "97.46%", "104.75%", "112.71%", "120.67%", "128.62%", "136.58%", "144.53%", "152.49%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "60.89%", "65.84%", "70.8%", "77.88%", "82.84%", "88.5%", "96.29%", "104.08%", "111.86%", "120.36%", "128.86%", "137.35%", "145.85%", "154.34%", "162.84%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "72.76%", "78.68%", "84.6%", "93.06%", "98.98%", "105.75%", "115.06%", "124.36%", "133.67%", "143.82%", "153.97%", "164.12%", "174.28%", "184.43%", "194.58%"]
	level_template(embed, level)
	return tartaglia_autoattack_data

def tartaglia_autoattack_data2(embed):
	tartaglia_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "92.82%", "98.94%", "105.06%", "111.18%", "117.3%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "235.6%", "248%", "263.5%", "279%", "294.5%"]
	level_template(embed, level)
	level = ["Riptide Flash DMG", "12.4%×3", "13.33%×3", "14.26%×3", "15.5%×3", "16.43%×3", "17.36%×3", "18.6%×3", "19.84%×3", "21.08%×3", "22.32%×3", "23.56%×3", "24.8%×3", "26.35%×3", "27.9%×3", "29.45%×3"]
	level_template(embed, level)
	level = ["Riptide Burst DMG", "62%", "66.65%", "71.3%", "77.5%", "82.15%", "86.8%", "93%", "99.2%", "105.4%", "111.6%", "117.8%", "124%", "131.75%", "139.5%", "147.25%"]
	level_template(embed, level)
	level = ["Riptide Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return tartaglia_autoattack_data2

def tartaglia_autoattack_data3(embed):
	tartaglia_autoattack_data3 = discord.Embed(color=color)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return tartaglia_autoattack_data3

def tartaglia_skill_data(embed):
	tartaglia_skill_data = discord.Embed(color=color)
	level = ["Stance Change DMG", "72%", "77.4%", "82.8%", "90%", "95.4%", "100.8%", "108%", "115.2%", "122.4%", "129.6%", "136.8%", "144%", "153%", "162%", "171%"]
	level_template(embed, level)
	level = ["1-Hit DMG", "38.87%", "42.04%", "45.2%", "49.72%", "52.88%", "56.5%", "61.47%", "66.44%", "71.42%", "76.84%", "82.26%", "87.69%", "93.11%", "98.54%", "103.96%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "41.62%", "45.01%", "48.4%", "53.24%", "56.63%", "60.5%", "65.82%", "71.15%", "76.47%", "82.28%", "88.09%", "93.9%", "99.7%", "105.51%", "111.32%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "56.33%", "60.92%", "65.5%", "72.05%", "76.64%", "81.88%", "89.08%", "96.29%", "103.49%", "111.35%", "119.21%", "127.07%", "134.93%", "142.79%", "150.65%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "59.94%", "64.82%", "69.7%", "76.67%", "81.55%", "87.13%", "94.79%", "102.46%", "110.13%", "118.49%", "126.85%", "135.22%", "143.58%", "151.95%", "160.31%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "55.3%", "59.8%", "64.3%", "70.73%", "75.23%", "80.38%", "87.45%", "94.52%", "101.59%", "109.31%", "117.03%", "124.74%", "132.46%", "140.17%", "147.89%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "35.43% + 37.67%", "38.32% + 40.73%", "41.2% + 43.8%", "45.32% + 48.18%", "48.2% + 51.25%", "51.5% + 54.75%", "56.03% + 59.57%", "60.56% + 64.39%", "65.1% + 69.2%", "70.04% + 74.46%", "74.98% + 79.72%", "79.93% + 84.97%", "84.87% + 90.23%", "89.82% + 95.48%", "94.76% + 100.74%"]
	level_template(embed, level)
	return tartaglia_skill_data

def tartaglia_skill_data2(embed):
	tartaglia_skill_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "60.2% + 71.98%", "65.1% + 77.84%", "70% + 83.7%", "77% + 92.07%", "81.9% + 97.93%", "87.5% + 104.62%", "95.2% + 113.83%", "102.9% + 123.04%", "110.6% + 132.25%", "119% + 142.29%", "127.4% + 152.33%", "135.8% + 162.38%", "144.2% + 172.42%", "152.6% + 182.47%", "161% + 192.51%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Riptide Slash", "60.2%", "65.1%", "70%", "77%", "81.9%", "87.5%", "95.2%", "102.9%", "110.6%", "119%", "127.4%", "135.8%", "144.2%", "152.6%", "161%"]
	level_template(embed, level)
	level = ["Max Duration", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s"]
	level_template(embed, level)
	level = ["Preemptive CD", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s", "6-36s"]
	level_template(embed, level)
	level = ["Max CD", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s", "45s"]
	level_template(embed, level)
	return tartaglia_skill_data2

def tartaglia_burst_data(embed):
	tartaglia_burst_data = discord.Embed(color=color)
	level = ["Burst DMG: Melee", "464%", "498.8%", "533.6%", "580%", "614.8%", "649.6%", "696%", "742.4%", "788.8%", "835.2%", "881.6%", "928%", "986%", "1044%", "1102%"]
	level_template(embed, level)
	level = ["Burst DMG: Ranged", "378.4%", "406.78%", "435.16%", "473%", "501.38%", "529.76%", "567.6%", "605.44%", "643.28%", "681.12%", "718.96%", "756.8%", "804.1%", "851.4%", "898.7%"]
	level_template(embed, level)
	level = ["Riptide Blast DMG", "120%", "129%", "138%", "150%", "159%", "168%", "180%", "192%", "204%", "216%", "228%", "240%", "255%", "270%", "285%"]
	level_template(embed, level)
	level = ["Energy Return (Ranged)", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return tartaglia_burst_data

# Pyro

def amber_autoattack_data(embed):
	amber_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "36.12%", "39.06%", "42%", "46.2%", "49.14%", "52.5%", "57.12%", "61.74%", "66.36%", "71.4%", "76.44%", "81.48%", "86.52%", "91.56%", "96.6%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "36.12%", "39.06%", "42%", "46.2%", "49.14%", "52.5%", "57.12%", "61.74%", "66.36%", "71.4%", "76.44%", "81.48%", "86.52%", "91.56%", "96.6%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "46.44%", "50.22%", "54%", "59.4%", "63.18%", "67.5%", "73.44%", "79.38%", "85.32%", "91.8%", "98.28%", "104.76%", "111.24%", "117.72%", "124.2%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "47.3%", "51.15%", "55%", "60.5%", "64.35%", "68.75%", "74.8%", "80.85%", "86.9%", "93.5%", "100.1%", "106.7%", "113.3%", "119.9%", "126.5%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "59.34%", "64.17%", "69%", "75.9%", "80.73%", "86.25%", "93.84%", "101.43%", "109.02%", "117.3%", "125.58%", "133.86%", "142.14%", "150.42%", "158.7%"]
	level_template(embed, level)
	return amber_autoattack_data

def amber_autoattack_data2(embed):
	amber_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "92.82%", "98.94%", "105.06%", "111.18%", "117.3%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "235.6%", "248%", "263.5%", "279%", "294.5%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return amber_autoattack_data2

def amber_skill_data(embed):
	amber_skill_data = discord.Embed(color=color)
	level = ["Inherited HP", "41.36%", "44.46%", "47.56%", "51.7%", "54.8%", "57.9%", "62.04%", "66.18%", "70.31%", "74.45%", "78.58%", "82.72%", "87.89%", "93.06%", "98.23%"]
	level_template(embed, level)
	level = ["Explosion DMG", "123.2%", "132.44%", "141.68%", "154%", "163.24%", "172.48%", "184.8%", "197.12%", "209.44%", "221.76%", "234.08%", "246.4%", "261.8%", "277.2%", "292.6%"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	return amber_skill_data

def amber_burst_data(embed):
	amber_burst_data = discord.Embed(color=color)
	level = ["Fiery Rain DMG Per Wave", "28.08%", "30.19%", "32.29%", "35.1%", "37.21%", "39.31%", "42.12%", "44.93%", "47.74%", "50.54%", "53.35%", "56.16%", "59.67%", "63.18%", "66.69%"]
	level_template(embed, level)
	level = ["Total Fiery Rain DMG", "505.44%", "543.35%", "581.26%", "631.8%", "669.71%", "707.62%", "758.16%", "808.7%", "859.25%", "909.79%", "960.34%", "1010.88%", "1074.06%", "1137.24%", "1200.42%"]
	level_template(embed, level)
	level = ["Duration", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return amber_burst_data

def bennett_autoattack_data(embed):
	bennett_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "44.55%", "48.17%", "51.8%", "56.98%", "60.61%", "64.75%", "70.45%", "76.15%", "81.84%", "88.06%", "94.28%", "100.49%", "106.71%", "112.92%", "119.14%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "42.74%", "46.22%", "49.7%", "54.67%", "58.15%", "62.13%", "67.59%", "73.06%", "78.53%", "84.49%", "90.45%", "96.42%", "102.38%", "108.35%", "114.31%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "54.61%", "59.06%", "63.5%", "69.85%", "74.3%", "79.38%", "86.36%", "93.35%", "100.33%", "107.95%", "115.57%", "123.19%", "130.81%", "138.43%", "146.05%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "59.68%", "64.54%", "69.4%", "76.34%", "81.2%", "86.75%", "94.38%", "102.02%", "109.65%", "117.98%", "126.31%", "134.64%", "142.96%", "151.29%", "159.62%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "71.9%", "77.75%", "83.6%", "91.96%", "97.81%", "104.5%", "113.7%", "122.89%", "132.09%", "142.12%", "152.15%", "162.18%", "172.22%", "182.25%", "192.28%"]
	level_template(embed, level)
	return bennett_autoattack_data

def bennett_autoattack_data2(embed):
	bennett_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "55.9% + 60.72%", "60.45% + 65.66%", "65% + 70.6%", "71.5% + 77.66%", "76.05% + 82.6%", "81.25% + 88.25%", "88.4% + 96.02%", "95.55% + 103.78%", "102.7% + 111.55%", "110.5% + 120.02%", "118.3% + 128.49%", "126.1% + 136.96%", "133.9% + 145.44%", "141.7% + 153.91%", "149.5% + 162.38%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return bennett_autoattack_data2

def bennett_skill_data(embed):
	bennett_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "137.6%", "147.92%", "158.24%", "172%", "182.32%", "192.64%", "206.4%", "220.16%", "233.92%", "247.68%", "261.44%", "275.2%", "292.4%", "309.6%", "326.8%"]
	level_template(embed, level)
	level = ["Charge Lv 1 DMG", "84% + 92%", "90.3% + 98.9%", "96.6% + 105.8%", "105% + 115%", "111.3% + 121.9%", "117.6% + 128.8%", "126% + 138%", "134.4% + 147.2%", "142.8% + 156.4%", "151.2% + 165.6%", "159.6% + 174.8%", "168% + 184%", "178.5% + 195.5%", "189% + 207%", "199.5% + 218.5%"]
	level_template(embed, level)
	level = ["Charge Lv 2 DMG", "88% + 96%", "94.6% + 103.2%", "101.2% + 110.4%", "110% + 120%", "116.6% + 127.2%", "123.2% + 134.4%", "132% + 144%", "140.8% + 153.6%", "149.6% + 163.2%", "158.4% + 172.8%", "167.2% + 182.4%", "176% + 192%", "187% + 204%", "198% + 216%", "209% + 228%"]
	level_template(embed, level)
	level = ["Explosion DMG", "132%", "141.9%", "151.8%", "165%", "174.9%", "184.8%", "198%", "211.2%", "224.4%", "237.6%", "250.8%", "264%", "280.5%", "297%", "313.5%"]
	level_template(embed, level)
	level = ["CD", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s", "5 / 7.5 / 10s"]
	level_template(embed, level)
	return bennett_skill_data

def bennett_burst_data(embed):
	bennett_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "232.8%", "250.26%", "267.72%", "291%", "308.46%", "325.92%", "349.2%", "372.48%", "395.76%", "419.04%", "442.32%", "465.6%", "494.7%", "523.8%", "552.9%"]
	level_template(embed, level)
	level = ["Regen Per Sec", "6% Max HP + 577", "6.45% Max HP + 635", "6.9% Max HP + 698", "7.5% Max HP + 765", "7.95% Max HP + 837", "8.4% Max HP + 914", "9% Max HP + 996", "9.6% Max HP + 1083", "10.2% Max HP + 1174", "10.8% Max HP + 1270", "11.4% Max HP + 1371", "12% Max HP + 1477", "12.75% Max HP + 1588", "13.5% Max HP + 1703", "14.25% Max HP + 1824"]
	level_template(embed, level)
	level = ["ATK Bonus Ratio", "56%", "60.2%", "64.4%", "70%", "74.2%", "78.4%", "84%", "89.6%", "95.2%", "100.8%", "106.4%", "112%", "119%", "126%", "133%"]
	level_template(embed, level)
	level = ["Duration", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return bennett_burst_data

def xiangling_autoattack_data(embed):
	xiangling_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "42.05%", "45.48%", "48.9%", "53.79%", "57.21%", "61.13%", "66.5%", "71.88%", "77.26%", "83.13%", "89.85%", "97.76%", "105.67%", "113.58%", "122.2%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "42.14%", "45.57%", "49%", "53.9%", "57.33%", "61.25%", "66.64%", "72.03%", "77.42%", "83.3%", "90.04%", "97.96%", "105.88%", "113.81%", "122.45%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "26.06% + 26.06%", "28.18% + 28.18%", "30.3% + 30.3%", "33.33% + 33.33%", "35.45% + 35.45%", "37.87% + 37.87%", "41.21% + 41.21%", "44.54% + 44.54%", "47.87% + 47.87%", "51.51% + 51.51%", "55.68% + 55.68%", "60.58% + 60.58%", "65.48% + 65.48%", "70.37% + 70.37%", "75.72% + 75.72%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "14.1%*4", "15.25%*4", "16.4%*4", "18.04%*4", "19.19%*4", "20.5%*4", "22.3%*4", "24.11%*4", "25.91%*4", "27.88%*4", "30.14%*4", "32.79%*4", "35.44%*4", "38.09%*4", "40.98%*4"]
	level_template(embed, level)
	level = ["5-Hit DMG", "71.04%", "76.82%", "82.6%", "90.86%", "96.64%", "103.25%", "112.34%", "121.42%", "130.51%", "140.42%", "151.78%", "165.13%", "178.49%", "191.85%", "206.42%"]
	level_template(embed, level)
	return xiangling_autoattack_data

def xiangling_autoattack_data2(embed):
	xiangling_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "121.69%", "131.6%", "141.5%", "155.65%", "165.56%", "176.88%", "192.44%", "208.01%", "223.57%", "240.55%", "260.01%", "282.89%", "305.77%", "328.65%", "353.61%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return xiangling_autoattack_data2

def xiangling_skill_data(embed):
	xiangling_skill_data = discord.Embed(color=color)
	level = ["Flame DMG", "111.28%", "119.63%", "127.97%", "139.1%", "147.45%", "155.79%", "166.92%", "178.05%", "189.18%", "200.3%", "211.43%", "222.56%", "236.47%", "250.38%", "264.29%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	return xiangling_skill_data

def xiangling_burst_data(embed):
	xiangling_burst_data = discord.Embed(color=color)
	level = ["1-Hit Swing DMG", "72%", "77.4%", "82.8%", "90%", "95.4%", "100.8%", "108%", "115.2%", "122.4%", "129.6%", "136.8%", "144%", "153%", "162%", "171%"]
	level_template(embed, level)
	level = ["2-Hit Swing DMG", "88%", "94.6%", "101.2%", "110%", "116.6%", "123.2%", "132%", "140.8%", "149.6%", "158.4%", "167.2%", "176%", "187%", "198%", "209%"]
	level_template(embed, level)
	level = ["3-Hit Swing DMG", "109.6%", "117.82%", "126.04%", "137%", "145.22%", "153.44%", "164.4%", "175.36%", "186.32%", "197.28%", "208.24%", "219.2%", "232.9%", "246.6%", "260.3%"]
	level_template(embed, level)
	level = ["Pyronado DMG", "112%", "120.4%", "128.8%", "140%", "148.4%", "156.8%", "168%", "179.2%", "190.4%", "201.6%", "212.8%", "224%", "238%", "252%", "266%"]
	level_template(embed, level)
	level = ["Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return xiangling_burst_data

def xiangling_burst_data2(embed):
	xiangling_burst_data2 = discord.Embed(color=color)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return xiangling_burst_data2

def xinyan_autoattack_data(embed):
	xinyan_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "76.54%", "82.77%", "89%", "97.9%", "104.13%", "111.25%", "121.04%", "130.83%", "140.62%", "151.3%", "161.98%", "172.66%", "183.34%", "194.02%", "204.7%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "73.96%", "79.98%", "86%", "94.6%", "100.62%", "107.5%", "116.96%", "126.42%", "135.88%", "146.2%", "156.52%", "166.84%", "177.16%", "187.48%", "197.8%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "95.46%", "103.23%", "111%", "122.1%", "129.87%", "138.75%", "150.96%", "163.17%", "175.38%", "188.7%", "202.02%", "215.34%", "228.66%", "241.98%", "255.3%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "115.84%", "125.27%", "134.7%", "148.17%", "157.6%", "168.38%", "183.19%", "198.01%", "212.83%", "228.99%", "245.15%", "261.32%", "277.48%", "293.65%", "309.81%"]
	level_template(embed, level)
	return xinyan_autoattack_data

def xinyan_autoattack_data2(embed):
	xinyan_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "62.55%", "67.64%", "72.73%", "80%", "85.09%", "90.91%", "98.91%", "106.91%", "114.91%", "123.64%", "132.36%", "141.09%", "149.82%", "158.55%", "167.27%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "113.09%", "122.3%", "131.5%", "144.65%", "153.86%", "164.38%", "178.84%", "193.31%", "207.77%", "223.55%", "239.33%", "255.11%", "270.89%", "286.67%", "302.45%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "157.85%", "168.26%", "178.66%", "189.07%", "199.48%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "315.63% / 394.24%", "336.44% / 420.23%", "357.25% / 446.23%", "378.06% / 472.22%", "398.87% / 498.21%"]
	level_template(embed, level)
	return xinyan_autoattack_data2

def xinyan_skill_data(embed):
	xinyan_skill_data = discord.Embed(color=color)
	level = ["Swing DMG", "169.6%", "182.32%", "195.04%", "212%", "224.72%", "237.44%", "254.4%", "271.36%", "288.32%", "305.28%", "322.24%", "339.2%", "360.4%", "381.6%", "402.8%"]
	level_template(embed, level)
	level = ["Shield Lv 1 DMG Absorption", "104.04% DEF + 501", "111.84% DEF + 551", "119.65% DEF + 605", "130.05% DEF + 663", "137.85% DEF + 726", "145.66% DEF + 793", "156.06% DEF + 864", "166.46% DEF + 939", "176.87% DEF + 1018", "187.27% DEF + 1101", "197.68% DEF + 1189", "208.08% DEF + 1281", "221.09% DEF + 1377", "234.09% DEF + 1477", "247.1% DEF + 1581"]
	level_template(embed, level)
	level = ["Shield Lv 2 DMG Absorption", "122.4% DEF + 589", "131.58% DEF + 648", "140.76% DEF + 712", "153% DEF + 780", "162.18% DEF + 854", "171.36% DEF + 932", "183.6% DEF + 1016", "195.84% DEF + 1104", "208.08% DEF + 1197", "220.32% DEF + 1296", "232.56% DEF + 1399", "244.8% DEF + 1507", "260.1% DEF + 1620", "275.4% DEF + 1737", "290.7% DEF + 1860"]
	level_template(embed, level)
	level = ["Shield Lv 3 DMG Absorption", "144% DEF + 693", "154.8% DEF + 762", "165.6% DEF + 837", "180% DEF + 918", "190.8% DEF + 1005", "201.6% DEF + 1097", "216% DEF + 1195", "230.4% DEF + 1299", "244.8% DEF + 1409", "259.2% DEF + 1524", "273.6% DEF + 1646", "288% DEF + 1773", "306% DEF + 1905", "324% DEF + 2044", "342% DEF + 2188"]
	level_template(embed, level)
	return xinyan_skill_data

def xinyan_skill_data2(embed):
	xinyan_skill_data2 = discord.Embed(color=color)
	level = ["DoT", "33.6%", "36.12%", "38.64%", "42%", "44.52%", "47.04%", "50.4%", "53.76%", "57.12%", "60.48%", "63.84%", "67.2%", "71.4%", "75.6%", "79.8%"]
	level_template(embed, level)
	level = ["Shield Duration", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["CD", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s"]
	level_template(embed, level)
	return xinyan_skill_data2

def xinyan_burst_data(embed):
	xinyan_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "340.8%", "366.36%", "391.92%", "426%", "451.56%", "477.12%", "511.2%", "545.28%", "579.36%", "613.44%", "647.52%", "681.6%", "724.2%", "766.8%", "809.4%"]
	level_template(embed, level)
	level = ["Pyro DoT", "40%", "43%", "46%", "50%", "53%", "56%", "60%", "64%", "68%", "72%", "76%", "80%", "85%", "90%", "95%"]
	level_template(embed, level)
	level = ["Duration", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s", "2s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return xinyan_burst_data

def yanfei_autoattack_data(embed):
	yanfei_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "58.34%", "62.72%", "67.09%", "72.93%", "77.3%", "81.68%", "87.51%", "93.35%", "99.18%", "105.01%", "110.85%", "116.68%", "123.98%", "131.27%", "138.56%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "52.13%", "56.04%", "59.94%", "65.16%", "69.07%", "72.98%", "78.19%", "83.4%", "88.61%", "93.83%", "99.04%", "104.25%", "110.77%", "117.28%", "123.8%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "76.01%", "81.71%", "87.41%", "95.02%", "100.72%", "106.42%", "114.02%", "121.62%", "129.22%", "136.82%", "144.42%", "152.03%", "161.53%", "171.03%", "180.53%"]
	level_template(embed, level)
	level = ["Charged Attack", "98.23% / 115.56% / 132.9% / 150.23% / 167.57%", "104.11% / 122.48% / 140.86% / 159.23% / 177.6%", "109.99% / 129.4% / 148.81% / 168.23% / 187.64%", "117.64% / 138.4% / 159.16% / 179.92% / 200.68%", "123.52% / 145.32% / 167.12% / 188.92% / 210.71%", "129.4% / 152.24% / 175.08% / 197.91% / 220.75%", "137.05% / 161.24% / 185.42% / 209.61% / 233.79%", "144.7% / 170.23% / 195.77% / 221.3% / 246.84%", "152.34% / 179.23% / 206.11% / 233% / 259.88%", "159.99% / 188.22% / 216.46% / 244.69% / 272.92%", "167.64% / 197.22% / 226.8% / 256.39% / 285.97%", "175.28% / 206.22% / 237.15% / 268.08% / 299.01%", "182.93% / 215.21% / 247.49% / 279.78% / 312.06%", "190.58% / 224.21% / 257.84% / 291.47% / 325.1%", "198.22% / 233.2% / 268.18% / 303.17% / 338.15%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	return yanfei_autoattack_data

def yanfei_autoattack_data2(embed):
	yanfei_autoattack_data2 = discord.Embed(color=color)
	level = ["Scarlet Seal Stamina Consumption Decrease", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal", "15% Per Seal"]
	level_template(embed, level)
	level = ["Scarlet Seal Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return yanfei_autoattack_data2

def yanfei_skill_data(embed):
	yanfei_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "169.6%", "182.32%", "195.04%", "212%", "224.72%", "237.44%", "254.4%", "271.36%", "288.32%", "305.28%", "322.24%", "339.2%", "360.4%", "381.6%", "402.8%"]
	level_template(embed, level)
	level = ["CD", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s"]
	level_template(embed, level)
	return yanfei_skill_data

def yanfei_burst_data(embed):
	yanfei_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "182.4%", "196.08%", "209.76%", "228%", "241.68%", "255.36%", "273.6%", "291.84%", "310.08%", "328.32%", "346.56%", "364.8%", "387.6%", "410.4%", "433.2%"]
	level_template(embed, level)
	level = ["Scarlet Seal Grant Interval", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s", "1s"]
	level_template(embed, level)
	level = ["Charged Attack DMG Bonus", "33.4%", "35.4%", "37.4%", "40%", "42%", "44%", "46.6%", "49.2%", "51.8%", "54.4%", "57%", "59.6%", "62.2%", "64.8%", "67.4%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return yanfei_burst_data

def diluc_autoattack_data(embed):
	diluc_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "89.7%", "97%", "104.3%", "114.73%", "122.03%", "130.38%", "141.85%", "153.32%", "164.79%", "177.31%", "191.65%", "208.52%", "225.38%", "242.25%", "260.65%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "87.63%", "94.77%", "101.9%", "112.09%", "119.22%", "127.38%", "138.58%", "149.79%", "161%", "173.23%", "187.24%", "203.72%", "220.2%", "236.67%", "254.65%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "98.81%", "106.86%", "114.9%", "126.39%", "134.43%", "143.63%", "156.26%", "168.9%", "181.54%", "195.33%", "211.13%", "229.71%", "248.29%", "266.87%", "287.14%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "133.99%", "144.89%", "155.8%", "171.38%", "182.29%", "194.75%", "211.89%", "229.03%", "246.16%", "264.86%", "286.28%", "311.48%", "336.67%", "361.86%", "389.34%"]
	level_template(embed, level)
	return diluc_autoattack_data

def diluc_autoattack_data2(embed):
	diluc_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "68.8%", "74.4%", "80%", "88%", "93.6%", "100%", "108.8%", "117.6%", "126.4%", "136%", "147%", "159.94%", "172.87%", "185.81%", "199.92%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "124.7%", "134.85%", "145%", "159.5%", "169.65%", "181.25%", "197.2%", "213.15%", "229.1%", "246.5%", "266.44%", "289.88%", "313.33%", "336.78%", "362.36%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "89.51%", "96.79%", "104.08%", "114.48%", "121.77%", "130.1%", "141.54%", "152.99%", "164.44%", "176.93%", "189.42%", "201.91%", "214.4%", "226.89%", "239.37%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "178.97% / 223.55%", "193.54% / 241.74%", "208.11% / 259.94%", "228.92% / 285.93%", "243.49% / 304.13%", "260.13% / 324.92%", "283.03% / 353.52%", "305.92% / 382.11%", "328.81% / 410.7%", "353.78% / 441.89%", "378.76% / 473.09%", "403.73% / 504.28%", "428.7% / 535.47%", "453.68% / 566.66%", "478.65% / 597.86%"]
	level_template(embed, level)
	return diluc_autoattack_data2

def diluc_skill_data(embed):
	diluc_skill_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "94.4%", "101.48%", "108.56%", "118%", "125.08%", "132.16%", "141.6%", "151.04%", "160.48%", "169.92%", "179.36%", "188.8%", "200.6%", "212.4%", "224.2%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "97.6%", "104.92%", "112.24%", "122%", "129.32%", "136.64%", "146.4%", "156.16%", "165.92%", "175.68%", "185.44%", "195.2%", "207.4%", "219.6%", "231.8%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "128.8%", "138.46%", "148.12%", "161%", "170.66%", "180.32%", "193.2%", "206.08%", "218.96%", "231.84%", "244.72%", "257.6%", "273.7%", "289.8%", "305.9%"]
	level_template(embed, level)
	level = ["CD", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return diluc_skill_data

def diluc_burst_data(embed):
	diluc_burst_data = discord.Embed(color=color)
	level = ["Slashing DMG", "204%", "219.3%", "234.6%", "255%", "270.3%", "285.6%", "306%", "326.4%", "346.8%", "367.2%", "387.6%", "408%", "433.5%", "459%", "484.5%"]
	level_template(embed, level)
	level = ["DoT", "60%", "64.5%", "69%", "75%", "79.5%", "84%", "90%", "96%", "102%", "108%", "114%", "120%", "127.5%", "135%", "142.5%"]
	level_template(embed, level)
	level = ["Explosion DMG", "204%", "219.3%", "234.6%", "255%", "270.3%", "285.6%", "306%", "326.4%", "346.8%", "367.2%", "387.6%", "408%", "433.5%", "459%", "484.5%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Infusion Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return diluc_burst_data

def klee_autoattack_data(embed):
	klee_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "72.16%", "77.57%", "82.98%", "90.2%", "95.61%", "101.02%", "108.24%", "115.46%", "122.67%", "129.89%", "137.39%", "147.21%", "157.02%", "166.83%", "176.65%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "62.4%", "67.08%", "71.76%", "78%", "82.68%", "87.36%", "93.6%", "99.84%", "106.08%", "112.32%", "118.81%", "127.3%", "135.78%", "144.27%", "152.76%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "89.92%", "96.66%", "103.41%", "112.4%", "119.14%", "125.89%", "134.88%", "143.87%", "152.86%", "161.86%", "171.21%", "183.44%", "195.67%", "207.9%", "220.12%"]
	level_template(embed, level)
	level = ["Charged Attack DMG", "157.36%", "169.16%", "180.96%", "196.7%", "208.5%", "220.3%", "236.04%", "251.78%", "267.51%", "283.25%", "299.61%", "321.01%", "342.42%", "363.82%", "385.22%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50", "50"]
	level_template(embed, level)
	return klee_autoattack_data

def klee_autoattack_data2(embed):
	klee_autoattack_data2 = discord.Embed(color=color)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return klee_autoattack_data2

def klee_skill_data(embed):
	klee_skill_data = discord.Embed(color=color)
	level = ["Jumpy Dumpty DMG", "95.2%", "102.34%", "109.48%", "119%", "126.14%", "133.28%", "142.8%", "152.32%", "161.84%", "171.36%", "180.88%", "190.4%", "202.3%", "214.2%", "226.1%"]
	level_template(embed, level)
	level = ["Mine DMG", "32.8%", "35.26%", "37.72%", "41%", "43.46%", "45.92%", "49.2%", "52.48%", "55.76%", "59.04%", "62.32%", "65.6%", "69.7%", "73.8%", "77.9%"]
	level_template(embed, level)
	level = ["Mine Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	return klee_skill_data

def klee_burst_data(embed):
	klee_burst_data = discord.Embed(color=color)
	level = ["Sparks 'n' Splash DMG", "42.64%", "45.84%", "49.04%", "53.3%", "56.5%", "59.7%", "63.96%", "68.22%", "72.49%", "76.75%", "81.02%", "85.28%", "90.61%", "95.94%", "101.27%"]
	level_template(embed, level)
	level = ["Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return klee_burst_data

def hutao_autoattack_data(embed):
	hutao_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "46.89%", "50.08%", "53.28%", "57.54%", "60.74%", "64.47%", "69.26%", "74.06%", "78.85%", "83.65%", "88.44%", "93.24%", "98.04%", "102.83%", "107.63%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "48.25%", "51.54%", "54.83%", "59.22%", "62.51%", "66.35%", "71.28%", "76.22%", "81.15%", "86.09%", "91.02%", "95.96%", "100.89%", "105.83%", "110.76%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "61.05%", "65.21%", "69.38%", "74.93%", "79.09%", "83.94%", "90.19%", "96.43%", "102.68%", "108.92%", "115.16%", "121.41%", "127.65%", "133.89%", "140.14%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "65.64%", "70.12%", "74.59%", "80.56%", "85.03%", "90.26%", "96.97%", "103.68%", "110.4%", "117.11%", "123.82%", "130.54%", "137.25%", "143.96%", "150.68%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "33.27% + 35.2%", "35.54% + 37.6%", "37.81% + 40%", "40.84% + 43.2%", "43.1% + 45.6%", "45.75% + 48.4%", "49.15% + 52%", "52.56% + 55.6%", "55.96% + 59.2%", "59.36% + 62.8%", "62.77% + 66.4%", "66.17% + 70%", "69.57% + 73.6%", "72.98% + 77.2%", "76.38% + 80.8%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "85.96%", "91.82%", "97.68%", "105.49%", "111.36%", "118.19%", "126.98%", "135.78%", "144.57%", "153.36%", "162.15%", "170.94%", "179.73%", "188.52%", "197.31%"]
	level_template(embed, level)
	return hutao_autoattack_data

def hutao_autoattack_data2(embed):
	hutao_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack", "135.96%", "145.23%", "154.5%", "166.86%", "176.13%", "186.95%", "200.85%", "214.76%", "228.66%", "242.57%", "256.47%", "270.38%", "284.28%", "298.19%", "312.09%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "65.42%", "69.88%", "74.34%", "80.29%", "84.75%", "89.95%", "96.64%", "103.33%", "110.02%", "116.71%", "123.4%", "130.1%", "136.79%", "143.48%", "150.17%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "130.81% / 163.39%", "139.73% / 174.53%", "148.65% / 185.67%", "160.54% / 200.52%", "169.46% / 211.66%", "179.86% / 224.66%", "193.24% / 241.37%", "206.62% / 258.08%", "220% / 274.79%", "233.38% / 291.5%", "246.76% / 308.21%", "260.13% / 324.92%", "273.51% / 341.63%", "286.89% / 358.34%", "300.27% / 375.05%"]
	level_template(embed, level)
	return hutao_autoattack_data2

def hutao_skill_data(embed):
	hutao_skill_data = discord.Embed(color=color)
	level = ["Activation Cost", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP", "30% Current HP"]
	level_template(embed, level)
	level = ["ATK Increase", "3.84% Max HP", "4.07% Max HP", "4.3% Max HP", "4.6% Max HP", "4.83% Max HP", "5.06% Max HP", "5.36% Max HP", "5.66% Max HP", "5.96% Max HP", "6.26% Max HP", "6.56% Max HP", "6.85% Max HP", "7.15% Max HP", "7.45% Max HP", "7.75% Max HP"]
	level_template(embed, level)
	level = ["Blood Blossom DMG", "64%", "68.8%", "73.6%", "80%", "84.8%", "89.6%", "96%", "102.4%", "108.8%", "115.2%", "121.6%", "128%", "136%", "144%", "152%"]
	level_template(embed, level)
	level = ["Blood Blossom Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["Duration", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s", "9s"]
	level_template(embed, level)
	level = ["CD", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s", "16s"]
	level_template(embed, level)
	return hutao_skill_data

def hutao_burst_data(embed):
	hutao_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "303.27%", "321.43%", "339.59%", "363.2%", "381.36%", "399.52%", "423.13%", "446.74%", "470.34%", "493.95%", "517.56%", "541.17%", "564.78%", "588.38%", "611.99%"]
	level_template(embed, level)
	level = ["Low HP Burst DMG", "379.09%", "401.79%", "424.49%", "454%", "476.7%", "499.4%", "528.91%", "558.42%", "587.93%", "617.44%", "646.95%", "676.46%", "705.97%", "735.48%", "764.99%"]
	level_template(embed, level)
	level = ["HP Regeneration", "6.26% Max HP", "6.64% Max HP", "7.01% Max HP", "7.5% Max HP", "7.88% Max HP", "8.25% Max HP", "8.74% Max HP", "9.23% Max HP", "9.71% Max HP", "10.2% Max HP", "10.69% Max HP", "11.18% Max HP", "11.66% Max HP", "12.15% Max HP", "12.64% Max HP"]
	level_template(embed, level)
	level = ["Low HP Regeneration", "8.35% Max HP", "8.85% Max HP", "9.35% Max HP", "10% Max HP", "10.5% Max HP", "11% Max HP", "11.65% Max HP", "12.3% Max HP", "12.95% Max HP", "13.6% Max HP", "14.25% Max HP", "14.9% Max HP", "15.55% Max HP", "16.2% Max HP", "16.85% Max HP"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return hutao_burst_data

def yoimiya_autoattack_data(embed):
	yoimiya_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "35.64%×2", "38.07%×2", "40.5%×2", "43.74%×2", "46.17%×2", "49.01%×2", "52.65%×2", "56.29%×2", "59.94%×2", "63.59%×2", "67.23%×2", "70.88%×2", "74.52%×2", "78.17%×2", "81.81%×2"]
	level_template(embed, level)
	level = ["2-Hit DMG", "68.38%", "73.04%", "77.7%", "83.92%", "88.58%", "94.02%", "101.01%", "108%", "115%", "121.99%", "128.98%", "135.98%", "142.97%", "149.96%", "156.95%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "88.89%", "94.95%", "101.01%", "109.09%", "115.15%", "122.22%", "131.31%", "140.4%", "149.49%", "158.59%", "167.68%", "176.77%", "185.86%", "194.95%", "204.04%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "46.42%×2", "49.59%×2", "52.75%×2", "56.97%×2", "60.14%×2", "63.83%×2", "68.58%×2", "73.32%×2", "78.07%×2", "82.82%×2", "87.57%×2", "92.31%×2", "97.06%×2", "101.81%×2", "106.56%×2"]
	level_template(embed, level)
	level = ["5-Hit DMG", "105.86%", "113.08%", "120.3%", "129.92%", "137.14%", "145.56%", "156.39%", "167.22%", "178.04%", "188.87%", "199.7%", "210.53%", "221.35%", "232.18%", "243.01%"]
	level_template(embed, level)
	return yoimiya_autoattack_data

def yoimiya_autoattack_data2(embed):
	yoimiya_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "92.82%", "98.94%", "105.06%", "111.18%", "117.3%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "235.6%", "248%", "263.5%", "279%", "294.5%"]
	level_template(embed, level)
	level = ["Kindling Arrow DMG", "16.4%", "17.63%", "18.86%", "20.5%", "21.73%", "22.96%", "24.6%", "26.24%", "27.88%", "29.52%", "31.16%", "32.8%", "34.85%", "36.9%", "38.95%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return yoimiya_autoattack_data2

def yoimiya_skill_data(embed):
	yoimiya_skill_data = discord.Embed(color=color)
	level = ["Blazing Arrow DMG", "137.91%", "140.18%", "142.45%", "145.4%", "147.67%", "149.94%", "152.89%", "155.84%", "158.79%", "161.74%", "164.7%", "167.65%", "170.6%", "173.55%", "176.5%"]
	level_template(embed, level)
	level = ["Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	return yoimiya_skill_data

def yoimiya_burst_data(embed):
	yoimiya_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "127.2%", "136.74%", "146.28%", "159%", "168.54%", "178.08%", "190.8%", "203.52%", "216.24%", "228.96%", "241.68%", "254.4%", "270.3%", "286.2%", "302.1%"]
	level_template(embed, level)
	level = ["Aurous Blaze Explosion DMG", "122%", "131.15%", "140.3%", "152.5%", "161.65%", "170.8%", "183%", "195.2%", "207.4%", "219.6%", "231.8%", "244%", "259.25%", "274.5%", "289.75%"]
	level_template(embed, level)
	level = ["Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return yoimiya_burst_data

# Cryo

def kaeya_autoattack_data(embed):
	kaeya_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "53.75%", "58.13%", "62.5%", "68.75%", "73.13%", "78.13%", "85%", "91.88%", "98.75%", "106.25%", "114.84%", "124.95%", "135.06%", "145.16%", "156.19%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "51.69%", "55.89%", "60.1%", "66.11%", "70.32%", "75.13%", "81.74%", "88.35%", "94.96%", "102.17%", "110.43%", "120.15%", "129.87%", "139.59%", "150.19%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "65.27%", "70.59%", "75.9%", "83.49%", "88.8%", "94.88%", "103.22%", "111.57%", "119.92%", "129.03%", "139.47%", "151.74%", "164.01%", "176.29%", "189.67%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "70.86%", "76.63%", "82.4%", "90.64%", "96.41%", "103%", "112.06%", "121.13%", "130.19%", "140.08%", "151.41%", "164.73%", "178.06%", "191.38%", "205.92%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "88.24%", "95.42%", "102.6%", "112.86%", "120.04%", "128.25%", "139.54%", "150.82%", "162.11%", "174.42%", "188.53%", "205.12%", "221.71%", "238.3%", "256.4%"]
	level_template(embed, level)
	return kaeya_autoattack_data

def kaeya_autoattack_data2(embed):
	kaeya_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "55.04% + 73.1%", "59.52% + 79.05%", "64% + 85%", "70.4% + 93.5%", "74.88% + 99.45%", "80% + 106.25%", "87.04% + 115.6%", "94.08% + 124.95%", "101.12% + 134.3%", "108.8% + 144.5%", "117.6% + 156.19%", "127.95% + 169.93%", "138.3% + 183.68%", "148.65% + 197.42%", "159.94% + 212.42%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return kaeya_autoattack_data2

def kaeya_skill_data(embed):
	kaeya_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "191.2%", "205.54%", "219.88%", "239%", "253.34%", "267.68%", "286.8%", "305.92%", "325.04%", "344.16%", "363.28%", "382.4%", "406.3%", "430.2%", "454.1%"]
	level_template(embed, level)
	level = ["CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	return kaeya_skill_data

def kaeya_burst_data(embed):
	kaeya_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "77.6%", "83.42%", "89.24%", "97%", "102.82%", "108.64%", "116.4%", "124.16%", "131.92%", "139.68%", "147.44%", "155.2%", "164.9%", "174.6%", "184.3%"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return kaeya_burst_data

def diona_autoattack_data(embed):
	diona_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "36.12%", "39.06%", "42%", "46.2%", "49.14%", "52.5%", "57.12%", "61.74%", "66.36%", "71.4%", "77.18%", "83.97%", "90.76%", "97.55%", "104.96%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "33.54%", "36.27%", "39%", "42.9%", "45.63%", "48.75%", "53.04%", "57.33%", "61.62%", "66.3%", "71.66%", "77.97%", "84.28%", "90.58%", "97.46%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "45.58%", "49.29%", "53%", "58.3%", "62.01%", "66.25%", "72.08%", "77.91%", "83.74%", "90.1%", "97.39%", "105.96%", "114.53%", "123.1%", "132.45%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "43%", "46.5%", "50%", "55%", "58.5%", "62.5%", "68%", "73.5%", "79%", "85%", "91.88%", "99.96%", "108.05%", "116.13%", "124.95%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "53.75%", "58.13%", "62.5%", "68.75%", "73.13%", "78.13%", "85%", "91.88%", "98.75%", "106.25%", "114.84%", "124.95%", "135.06%", "145.16%", "156.19%"]
	level_template(embed, level)
	return diona_autoattack_data

def diona_autoattack_data2(embed):
	diona_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "93.71%", "101.96%", "110.21%", "118.45%", "127.45%"]
	level_template(embed, level)
	level = ["Fully-Charged Aimed Shot", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "236.1%", "252.96%", "269.82%", "286.69%", "303.55%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return diona_autoattack_data2

def diona_skill_data(embed):
	diona_skill_data = discord.Embed(color=color)
	level = ["Icy Paw DMG", "41.92% per Paw", "45.06% per Paw", "48.21% per Paw", "52.4% per Paw", "55.54% per Paw", "58.69% per Paw", "62.88% per Paw", "67.07% per Paw", "71.26% per Paw", "75.46% per Paw", "79.65% per Paw", "83.84% per Paw", "89.08% per Paw", "94.32% per Paw", "99.56% per Paw"]
	level_template(embed, level)
	level = ["Shield Base DMG Absorption", "7.2% Max HP + 693", "7.74% Max HP + 762", "8.28% Max HP + 837", "9% Max HP + 918", "9.54% Max HP + 1005", "10.08% Max HP + 1097", "10.8% Max HP + 1195", "11.52% Max HP + 1299", "12.24% Max HP + 1409", "12.96% Max HP + 1524", "13.68% Max HP + 1646", "14.4% Max HP + 1773", "15.3% Max HP + 1905", "16.2% Max HP + 2044", "17.1% Max HP + 2188"]
	level_template(embed, level)
	level = ["Duration", "1.8s per Paw", "1.9s per Paw", "2s per Paw", "2.1s per Paw", "2.2s per Paw", "2.3s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw", "2.4s per Paw"]
	level_template(embed, level)
	level = ["Press CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["CD (Hold)", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	return diona_skill_data

def diona_burst_data(embed):
	diona_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "80%", "86%", "92%", "100%", "106%", "112%", "120%", "128%", "136%", "144%", "152%", "160%", "170%", "180%", "190%"]
	level_template(embed, level)
	level = ["Continuous Field DMG", "52.64%", "56.59%", "60.54%", "65.8%", "69.75%", "73.7%", "78.96%", "84.22%", "89.49%", "94.75%", "100.02%", "105.28%", "111.86%", "118.44%", "125.02%"]
	level_template(embed, level)
	level = ["HP Regen Over Time", "5.34% Max HP + 513", "5.74% Max HP + 565", "6.14% Max HP + 620", "6.67% Max HP + 680", "7.07% Max HP + 744", "7.47% Max HP + 813", "8% Max HP + 885", "8.54% Max HP + 962", "9.07% Max HP + 1044", "9.6% Max HP + 1129", "10.14% Max HP + 1219", "10.67% Max HP + 1313", "11.34% Max HP + 1411", "12.01% Max HP + 1514", "12.67% Max HP + 1621"]
	level_template(embed, level)
	level = ["Duration", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return diona_burst_data

def rosaria_autoattack_data(embed):
	rosaria_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "52.46%", "56.73%", "61%", "67.1%", "71.37%", "76.25%", "82.96%", "89.67%", "96.38%", "103.7%", "111.02%", "118.34%", "125.66%", "132.98%", "140.3%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "51.6%", "55.8%", "60%", "66%", "70.2%", "75%", "81.6%", "88.2%", "94.8%", "102%", "109.2%", "116.4%", "123.6%", "130.8%", "138%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "31.82%×2", "34.41%×2", "37%×2", "40.7%×2", "43.29%×2", "46.25%×2", "50.32%×2", "54.39%×2", "58.46%×2", "62.9%×2", "67.34%×2", "71.78%×2", "76.22%×2", "80.66%×2", "85.1%×2"]
	level_template(embed, level)
	level = ["4-Hit DMG", "69.66%", "75.33%", "81%", "89.1%", "94.77%", "101.25%", "110.16%", "119.07%", "127.98%", "137.7%", "147.42%", "157.14%", "166.86%", "176.58%", "186.3%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "41.62% + 43%", "45.01% + 46.5%", "48.4% + 50%", "53.24% + 55%", "56.63% + 58.5%", "60.5% + 62.5%", "65.82% + 68%", "71.15% + 73.5%", "76.47% + 79%", "82.28% + 85%", "88.09% + 91%", "93.9% + 97%", "99.7% + 103%", "105.51% + 109%", "111.32% + 115%"]
	level_template(embed, level)
	return rosaria_autoattack_data

def rosaria_autoattack_data2(embed):
	rosaria_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "136.74%", "147.87%", "159%", "174.9%", "186.03%", "198.75%", "216.24%", "233.73%", "251.22%", "270.3%", "289.38%", "308.46%", "327.54%", "346.62%", "365.7%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25", "25"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return rosaria_autoattack_data2

def rosaria_skill_data(embed):
	rosaria_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "58.4% + 136%", "62.78% + 146.2%", "67.16% + 156.4%", "73% + 170%", "77.38% + 180.2%", "81.76% + 190.4%", "87.6% + 204%", "93.44% + 217.6%", "99.28% + 231.2%", "105.12% + 244.8%", "110.96% + 258.4%", "116.8% + 272%", "124.1% + 289%", "131.4% + 306%", "138.7% + 323%"]
	level_template(embed, level)
	level = ["CD", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	return rosaria_skill_data

def rosaria_burst_data(embed):
	rosaria_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "104% + 152%", "111.8% + 163.4%", "119.6% + 174.8%", "130% + 190%", "137.8% + 201.4%", "145.6% + 212.8%", "156% + 228%", "166.4% + 243.2%", "176.8% + 258.4%", "187.2% + 273.6%", "197.6% + 288.8%", "208% + 304%", "221% + 323%", "234% + 342%", "247% + 361%"]
	level_template(embed, level)
	level = ["Ice Lance DoT", "132%", "141.9%", "151.8%", "165%", "174.9%", "184.8%", "198%", "211.2%", "224.4%", "237.6%", "250.8%", "264%", "280.5%", "297%", "313.5%"]
	level_template(embed, level)
	level = ["Duration", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s", "8s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return rosaria_burst_data

def chongyun_autoattack_data(embed):
	chongyun_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "70%", "75.7%", "81.4%", "89.54%", "95.24%", "101.75%", "110.7%", "119.66%", "128.61%", "138.38%", "148.15%", "157.92%", "167.68%", "177.45%", "187.22%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "63.12%", "68.26%", "73.4%", "80.74%", "85.88%", "91.75%", "99.82%", "107.9%", "115.97%", "124.78%", "133.59%", "142.4%", "151.2%", "160.01%", "168.82%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "80.32%", "86.86%", "93.4%", "102.74%", "109.28%", "116.75%", "127.02%", "137.3%", "147.57%", "158.78%", "169.99%", "181.2%", "192.4%", "203.61%", "214.82%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "101.22%", "109.46%", "117.7%", "129.47%", "137.71%", "147.13%", "160.07%", "173.02%", "185.97%", "200.09%", "214.21%", "228.34%", "242.46%", "256.59%", "270.71%"]
	level_template(embed, level)
	return chongyun_autoattack_data

def chongyun_autoattack_data2(embed):
	chongyun_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "56.29%", "60.87%", "65.45%", "71.99%", "76.57%", "81.81%", "89.01%", "96.21%", "103.41%", "111.26%", "119.12%", "126.97%", "134.82%", "142.68%", "150.53%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "101.78%", "110.07%", "118.35%", "130.19%", "138.47%", "147.94%", "160.96%", "173.97%", "186.99%", "201.2%", "215.4%", "229.6%", "243.8%", "258%", "272.21%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "157.85%", "168.26%", "178.66%", "189.07%", "199.48%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "315.63% / 394.24%", "336.44% / 420.23%", "357.25% / 446.23%", "378.06% / 472.22%", "398.87% / 498.21%"]
	level_template(embed, level)
	return chongyun_autoattack_data2

def chongyun_skill_data(embed):
	chongyun_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "172.04%", "184.94%", "197.85%", "215.05%", "227.95%", "240.86%", "258.06%", "275.26%", "292.47%", "309.67%", "326.88%", "344.08%", "365.59%", "387.09%", "408.6%"]
	level_template(embed, level)
	level = ["Infusion Duration", "2s", "2.1s", "2.2s", "2.3s", "2.4s", "2.5s", "2.6s", "2.7s", "2.8s", "2.9s", "3s", "3s", "3s", "3s", "3s"]
	level_template(embed, level)
	level = ["Field Duration", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	return chongyun_skill_data

def chongyun_burst_data(embed):
	chongyun_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "142.4%", "153.08%", "163.76%", "178%", "188.68%", "199.36%", "213.6%", "227.84%", "242.08%", "256.32%", "270.56%", "284.8%", "302.6%", "320.4%", "338.2%"]
	level_template(embed, level)
	level = ["CD", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s", "12s"]
	level_template(embed, level)
	level = ["Energy Cost", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40", "40"]
	level_template(embed, level)
	return chongyun_burst_data

def qiqi_autoattack_data(embed):
	qiqi_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "37.75%", "40.83%", "43.9%", "48.29%", "51.36%", "54.88%", "59.7%", "64.53%", "69.36%", "74.63%", "79.9%", "85.17%", "90.43%", "95.7%", "100.97%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "38.87%", "42.04%", "45.2%", "49.72%", "52.88%", "56.5%", "61.47%", "66.44%", "71.42%", "76.84%", "82.26%", "87.69%", "93.11%", "98.54%", "103.96%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "24.17% + 24.17%", "26.13% + 26.13%", "28.1% + 28.1%", "30.91% + 30.91%", "32.88% + 32.88%", "35.13% + 35.13%", "38.22% + 38.22%", "41.31% + 41.31%", "44.4% + 44.4%", "47.77% + 47.77%", "51.14% + 51.14%", "54.51% + 54.51%", "57.89% + 57.89%", "61.26% + 61.26%", "64.63% + 64.63%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "24.68% + 24.68%", "26.69% + 26.69%", "28.7% + 28.7%", "31.57% + 31.57%", "33.58% + 33.58%", "35.88% + 35.88%", "39.03% + 39.03%", "42.19% + 42.19%", "45.35% + 45.35%", "48.79% + 48.79%", "52.23% + 52.23%", "55.68% + 55.68%", "59.12% + 59.12%", "62.57% + 62.57%", "66.01% + 66.01%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "63.04%", "68.17%", "73.3%", "80.63%", "85.76%", "91.63%", "99.69%", "107.75%", "115.81%", "124.61%", "133.41%", "142.2%", "151%", "159.79%", "168.59%"]
	level_template(embed, level)
	return qiqi_autoattack_data

def qiqi_autoattack_data2(embed):
	qiqi_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "64.33% + 64.33%", "69.56% + 69.56%", "74.8% + 74.8%", "82.28% + 82.28%", "87.52% + 87.52%", "93.5% + 93.5%", "101.73% + 101.73%", "109.96% + 109.96%", "118.18% + 118.18%", "127.16% + 127.16%", "136.14% + 136.14%", "145.11% + 145.11%", "154.09% + 154.09%", "163.06% + 163.06%", "172.04% + 172.04%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return qiqi_autoattack_data2

def qiqi_skill_data(embed):
	qiqi_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "96%", "103.2%", "110.4%", "120%", "127.2%", "134.4%", "144%", "153.6%", "163.2%", "172.8%", "182.4%", "192%", "204%", "216%", "228%"]
	level_template(embed, level)
	level = ["Regen on Hit", "10.56% ATK + 67", "11.35% ATK + 74", "12.14% ATK + 81", "13.2% ATK + 89", "13.99% ATK + 98", "14.78% ATK + 107", "15.84% ATK + 116", "16.9% ATK + 126", "17.95% ATK + 137", "19.01% ATK + 148", "20.06% ATK + 160", "21.12% ATK + 172", "22.44% ATK + 185", "23.76% ATK + 199", "25.08% ATK + 213"]
	level_template(embed, level)
	level = ["Continuous Regen", "69.6% ATK + 451", "74.82% ATK + 496", "80.04% ATK + 544", "87% ATK + 597", "92.22% ATK + 653", "97.44% ATK + 713", "104.4% ATK + 777", "111.36% ATK + 845", "118.32% ATK + 916", "125.28% ATK + 991", "132.24% ATK + 1070", "139.2% ATK + 1153", "147.9% ATK + 1239", "156.6% ATK + 1329", "165.3% ATK + 1423"]
	level_template(embed, level)
	level = ["Herald of Frost DMG", "36%", "38.7%", "41.4%", "45%", "47.7%", "50.4%", "54%", "57.6%", "61.2%", "64.8%", "68.4%", "72%", "76.5%", "81%", "85.5%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s", "30s"]
	level_template(embed, level)
	return qiqi_skill_data

def qiqi_burst_data(embed):
	qiqi_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "284.8%", "306.16%", "327.52%", "356%", "377.36%", "398.72%", "427.2%", "455.68%", "484.16%", "512.64%", "541.12%", "569.6%", "605.2%", "640.8%", "676.4%"]
	level_template(embed, level)
	level = ["Healing", "90% ATK + 577", "96.75% ATK + 635", "103.5% ATK + 698", "112.5% ATK + 765", "119.25% ATK + 837", "126% ATK + 914", "135% ATK + 996", "144% ATK + 1083", "153% ATK + 1174", "162% ATK + 1270", "171% ATK + 1371", "180% ATK + 1477", "191.25% ATK + 1588", "202.5% ATK + 1703", "213.75% ATK + 1824"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return qiqi_burst_data

def ganyu_autoattack_data(embed):
	ganyu_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "31.73%", "34.32%", "36.9%", "40.59%", "43.17%", "46.13%", "50.18%", "54.24%", "58.3%", "62.73%", "67.8%", "73.77%", "79.74%", "85.7%", "92.21%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "35.6%", "38.5%", "41.4%", "45.54%", "48.44%", "51.75%", "56.3%", "60.86%", "65.41%", "70.38%", "76.07%", "82.77%", "89.46%", "96.16%", "103.46%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "45.49%", "49.2%", "52.9%", "58.19%", "61.89%", "66.13%", "71.94%", "77.76%", "83.58%", "89.93%", "97.2%", "105.76%", "114.31%", "122.87%", "132.2%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "45.49%", "49.2%", "52.9%", "58.19%", "61.89%", "66.13%", "71.94%", "77.76%", "83.58%", "89.93%", "97.2%", "105.76%", "114.31%", "122.87%", "132.2%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "48.25%", "52.17%", "56.1%", "61.71%", "65.64%", "70.13%", "76.3%", "82.47%", "88.64%", "95.37%", "103.08%", "112.16%", "121.23%", "130.3%", "140.19%"]
	level_template(embed, level)
	level = ["6-Hit DMG", "57.62%", "62.31%", "67%", "73.7%", "78.39%", "83.75%", "91.12%", "98.49%", "105.86%", "113.9%", "123.11%", "133.95%", "144.78%", "155.61%", "167.43%"]
	level_template(embed, level)
	return ganyu_autoattack_data

def ganyu_autoattack_data2(embed):
	ganyu_autoattack_data2 = discord.Embed(color=color)
	level = ["Aimed Shot", "43.86%", "47.43%", "51%", "56.1%", "59.67%", "63.75%", "69.36%", "74.97%", "80.58%", "86.7%", "92.82%", "98.94%", "105.06%", "111.18%", "117.3%"]
	level_template(embed, level)
	level = ["Aimed Shot Charge Lv 1", "124%", "133.3%", "142.6%", "155%", "164.3%", "173.6%", "186%", "198.4%", "210.8%", "223.2%", "235.6%", "248%", "263.5%", "279%", "294.5%"]
	level_template(embed, level)
	level = ["Frostflake Arrow DMG", "128%", "137.6%", "147.2%", "160%", "169.6%", "179.2%", "192%", "204.8%", "217.6%", "230.4%", "243.2%", "256%", "272%", "288%", "304%"]
	level_template(embed, level)
	level = ["Frostflake Arrow Bloom DMG", "217.6%", "233.92%", "250.24%", "272%", "288.32%", "304.64%", "326.4%", "348.16%", "369.92%", "391.68%", "413.44%", "435.2%", "462.4%", "489.6%", "516.8%"]
	level_template(embed, level)
	level = ["Plunge DMG", "56.83%", "61.45%", "66.08%", "72.69%", "77.31%", "82.6%", "89.87%", "97.14%", "104.41%", "112.34%", "120.27%", "128.2%", "136.12%", "144.05%", "151.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "113.63% / 141.93%", "122.88% / 153.49%", "132.13% / 165.04%", "145.35% / 181.54%", "154.59% / 193.1%", "165.17% / 206.3%", "179.7% / 224.45%", "194.23% / 242.61%", "208.77% / 260.76%", "224.62% / 280.57%", "240.48% / 300.37%", "256.34% / 320.18%", "272.19% / 339.98%", "288.05% / 359.79%", "303.9% / 379.59%"]
	level_template(embed, level)
	return ganyu_autoattack_data2

def ganyu_skill_data(embed):
	ganyu_skill_data = discord.Embed(color=color)
	level = ["Inherited HP", "120%", "129%", "138%", "150%", "159%", "168%", "180%", "192%", "204%", "216%", "228%", "240%", "255%", "270%", "285%"]
	level_template(embed, level)
	level = ["Skill DMG", "132%", "141.9%", "151.8%", "165%", "174.9%", "184.8%", "198%", "211.2%", "224.4%", "237.6%", "250.8%", "264%", "280.5%", "297%", "313.5%"]
	level_template(embed, level)
	level = ["Duration", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s", "6s"]
	level_template(embed, level)
	level = ["CD", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return ganyu_skill_data

def ganyu_burst_data(embed):
	ganyu_burst_data = discord.Embed(color=color)
	level = ["Ice Shard DMG", "70.27%", "75.54%", "80.81%", "87.84%", "93.11%", "98.38%", "105.41%", "112.44%", "119.46%", "126.49%", "133.52%", "140.54%", "149.33%", "158.11%", "166.9%"]
	level_template(embed, level)
	level = ["Duration", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["CD", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s", "15s"]
	level_template(embed, level)
	level = ["Energy Cost", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60", "60"]
	level_template(embed, level)
	return ganyu_burst_data

def eula_autoattack_data(embed):
	eula_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "89.73%", "97.04%", "104.34%", "114.77%", "122.08%", "130.43%", "141.9%", "153.38%", "164.86%", "177.38%", "191.72%", "208.6%", "225.47%", "242.34%", "260.75%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "93.55%", "101.17%", "108.78%", "119.66%", "127.27%", "135.98%", "147.94%", "159.91%", "171.87%", "184.93%", "199.88%", "217.47%", "235.06%", "252.65%", "271.84%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "56.8% + 56.8%", "61.42% + 61.42%", "66.05% + 66.05%", "72.65% + 72.65%", "77.27% + 77.27%", "82.56% + 82.56%", "89.82% + 89.82%", "97.09% + 97.09%", "104.35% + 104.35%", "112.28% + 112.28%", "121.36% + 121.36%", "132.04% + 132.04%", "142.72% + 142.72%", "153.4% + 153.4%", "165.05% + 165.05%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "112.64%", "121.81%", "130.98%", "144.08%", "153.25%", "163.73%", "178.13%", "192.54%", "206.95%", "222.67%", "240.68%", "261.86%", "283.03%", "304.21%", "327.32%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "71.83% + 71.83%", "77.68% + 77.68%", "83.53% + 83.53%", "91.88% + 91.88%", "97.73% + 97.73%", "104.41% + 104.41%", "113.6% + 113.6%", "122.79% + 122.79%", "131.97% + 131.97%", "142% + 142%", "153.48% + 153.48%", "166.99% + 166.99%", "180.49% + 180.49%", "194% + 194%", "208.74% + 208.74%"]
	level_template(embed, level)
	return eula_autoattack_data

def eula_autoattack_data2(embed):
	eula_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack Spinning DMG", "68.8%", "74.4%", "80%", "88%", "93.6%", "100%", "108.8%", "117.6%", "126.4%", "136%", "147%", "159.94%", "172.87%", "185.81%", "199.92%"]
	level_template(embed, level)
	level = ["Charged Attack Final DMG", "124.4%", "134.52%", "144.65%", "159.12%", "169.24%", "180.81%", "196.72%", "212.64%", "228.55%", "245.91%", "265.79%", "289.18%", "312.57%", "335.96%", "361.48%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s", "40/s"]
	level_template(embed, level)
	level = ["Max Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["Plunge DMG", "74.59%", "80.66%", "86.73%", "95.4%", "101.47%", "108.41%", "117.95%", "127.49%", "137.03%", "147.44%", "159.37%", "173.39%", "187.41%", "201.44%", "216.74%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "149.14% / 186.29%", "161.28% / 201.45%", "173.42% / 216.62%", "190.77% / 238.28%", "202.91% / 253.44%", "216.78% / 270.77%", "235.86% / 294.6%", "254.93% / 318.42%", "274.01% / 342.25%", "294.82% / 368.25%", "318.67% / 398.03%", "346.71% / 433.06%", "374.75% / 468.08%", "402.79% / 503.11%", "433.38% / 541.32%"]
	level_template(embed, level)
	return eula_autoattack_data2

def eula_skill_data(embed):
	eula_skill_data = discord.Embed(color=color)
	level = ["Press DMG", "146.4%", "157.38%", "168.36%", "183%", "193.98%", "204.96%", "219.6%", "234.24%", "248.88%", "263.52%", "278.16%", "292.8%", "311.1%", "329.4%", "347.7%"]
	level_template(embed, level)
	level = ["Hold DMG", "245.6%", "264.02%", "282.44%", "307%", "325.42%", "343.84%", "368.4%", "392.96%", "417.52%", "442.08%", "466.64%", "491.2%", "521.9%", "552.6%", "583.3%"]
	level_template(embed, level)
	level = ["Icewhirl Brand DMG", "96%", "103.2%", "110.4%", "120%", "127.2%", "134.4%", "144%", "153.6%", "163.2%", "172.8%", "182.4%", "192%", "204%", "216%", "228%"]
	level_template(embed, level)
	level = ["DEF Bonus", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack", "30% Per Stack"]
	level_template(embed, level)
	level = ["Grimheart Duration", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s", "18s"]
	level_template(embed, level)
	return eula_skill_data

def eula_skill_data2(embed):
	eula_skill_data2 = discord.Embed(color=color)
	level = ["Physical RES Decrease", "16%", "17%", "18%", "19%", "20%", "21%", "22%", "23%", "24%", "25%", "25%", "25%", "25%", "25%", "25%"]
	level_template(embed, level)
	level = ["Cryo RES Decrease", "16%", "17%", "18%", "19%", "20%", "21%", "22%", "23%", "24%", "25%", "25%", "25%", "25%", "25%", "25%"]
	level_template(embed, level)
	level = ["RES Decrease Duration", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s", "7s"]
	level_template(embed, level)
	level = ["Press CD", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s", "4s"]
	level_template(embed, level)
	level = ["CD (Hold)", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s", "10s"]
	level_template(embed, level)
	return eula_skill_data2

def eula_burst_data(embed):
	eula_burst_data = discord.Embed(color=color)
	level = ["Burst DMG", "245.6%", "264.02%", "282.44%", "307%", "325.42%", "343.84%", "368.4%", "392.96%", "417.52%", "442.08%", "466.64%", "491.2%", "521.9%", "552.6%", "583.3%"]
	level_template(embed, level)
	level = ["Lightfall Sword Base DMG", "367.05%", "396.92%", "426.8%", "469.48%", "499.36%", "533.5%", "580.45%", "627.4%", "674.34%", "725.56%", "784.25%", "853.26%", "922.27%", "991.29%", "1066.57%"]
	level_template(embed, level)
	level = ["DMG Per Stack", "74.99%", "81.1%", "87.2%", "95.92%", "102.02%", "109%", "118.59%", "128.18%", "137.78%", "148.24%", "160.23%", "174.33%", "188.43%", "202.53%", "217.91%"]
	level_template(embed, level)
	level = ["Maximum Stacks", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30", "30"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return eula_burst_data

def ayaka_autoattack_data(embed):
	ayaka_autoattack_data = discord.Embed(color=color)
	level = ["1-Hit DMG", "48.68%", "52.65%", "56.61%", "62.27%", "66.23%", "70.76%", "76.99%", "83.22%", "89.44%", "96.24%", "103.03%", "109.82%", "116.62%", "123.41%", "130.2%"]
	level_template(embed, level)
	level = ["2-Hit DMG", "50.5%", "54.61%", "58.72%", "64.59%", "68.7%", "73.4%", "79.86%", "86.32%", "92.78%", "99.82%", "106.87%", "113.91%", "120.96%", "128.01%", "135.05%"]
	level_template(embed, level)
	level = ["3-Hit DMG", "63.39%", "68.54%", "73.7%", "81.07%", "86.23%", "92.13%", "100.24%", "108.34%", "116.45%", "125.3%", "134.14%", "142.99%", "151.83%", "160.67%", "169.52%"]
	level_template(embed, level)
	level = ["4-Hit DMG", "22.53% + 22.53% + 22.53%", "24.37% + 24.37% + 24.37%", "26.2% + 26.2% + 26.2%", "28.82% + 28.82% + 28.82%", "30.65% + 30.65% + 30.65%", "32.75% + 32.75% + 32.75%", "35.63% + 35.63% + 35.63%", "38.51% + 38.51% + 38.51%", "41.4% + 41.4% + 41.4%", "44.54% + 44.54% + 44.54%", "47.68% + 47.68% + 47.68%", "50.83% + 50.83% + 50.83%", "53.97% + 53.97% + 53.97%", "57.12% + 57.12% + 57.12%", "60.26% + 60.26% + 60.26%"]
	level_template(embed, level)
	level = ["5-Hit DMG", "85.05%", "91.98%", "98.9%", "108.79%", "115.71%", "123.63%", "134.5%", "145.38%", "156.26%", "168.13%", "180%", "191.87%", "203.73%", "215.6%", "227.47%"]
	level_template(embed, level)
	return ayaka_autoattack_data

def ayaka_autoattack_data2(embed):
	ayaka_autoattack_data2 = discord.Embed(color=color)
	level = ["Charged Attack DMG", "55.13%", "59.61%", "64.1%", "70.51%", "75%", "80.13%", "87.18%", "94.23%", "101.28%", "108.97%", "116.66%", "124.35%", "132.05%", "139.74%", "147.43%"]
	level_template(embed, level)
	level = ["Charged Attack Stamina Cost", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20", "20"]
	level_template(embed, level)
	level = ["Plunge DMG", "63.93%", "69.14%", "74.34%", "81.77%", "86.98%", "92.93%", "101.1%", "109.28%", "117.46%", "126.38%", "135.3%", "144.22%", "153.14%", "162.06%", "170.98%"]
	level_template(embed, level)
	level = ["Low/High Plunge DMG", "127.84% / 159.68%", "138.24% / 172.67%", "148.65% / 185.67%", "163.51% / 204.24%", "173.92% / 217.23%", "185.81% / 232.09%", "202.16% / 252.51%", "218.51% / 272.93%", "234.86% / 293.36%", "252.7% / 315.64%", "270.54% / 337.92%", "288.38% / 360.2%", "306.22% / 382.48%", "324.05% / 404.76%", "341.89% / 427.04%"]
	level_template(embed, level)
	return ayaka_autoattack_data2

def ayaka_skill_data(embed):
	ayaka_skill_data = discord.Embed(color=color)
	level = ["Skill DMG", "239.2%", "257.14%", "275.08%", "299%", "316.94%", "334.88%", "358.8%", "382.72%", "406.64%", "430.56%", "454.48%", "478.4%", "508.3%", "538.2%", "568.1%"]
	level_template(embed, level)
	level = ["CD", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10"]
	level_template(embed, level)
	return ayaka_skill_data

def ayaka_burst_data(embed):
	ayaka_burst_data = discord.Embed(color=color)
	level = ["Slashing DMG", "112.3%", "120.72%", "129.15%", "140.38%", "148.8%", "157.22%", "168.45%", "179.68%", "190.91%", "202.14%", "213.37%", "224.6%", "238.64%", "252.68%", "266.71%"]
	level_template(embed, level)
	level = ["Bladestorm DMG", "168.45%", "181.08%", "193.72%", "210.56%", "223.2%", "235.83%", "252.68%", "269.52%", "286.36%", "303.21%", "320.05%", "336.9%", "357.96%", "379.01%", "400.07%"]
	level_template(embed, level)
	level = ["Duration", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s", "5s"]
	level_template(embed, level)
	level = ["CD", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s", "20s"]
	level_template(embed, level)
	level = ["Energy Cost", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80", "80"]
	level_template(embed, level)
	return ayaka_burst_data

# This code was designed by '500 Internal Server Error'
# http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959851-my-first-script-for-minecraft-pi-api-a-rainbow


# Imports
from mcpi.minecraft import Minecraft
from mcpi import block
from math import *

# Variables
colors = [14,1,4,5,3,11,10]
mc = Minecraft.create()
height = 60

# Create the rainbow
mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0,128):
	for colorindex in range(0, len(colors)):
		y = sin((x/128.0) * pi) * height + colorindex
		mc.setBlock(x-64, int(y), 0, block.WOOL.id, colors[len(colors) - 1 - colorindex])

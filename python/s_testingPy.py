# # -*- coding: utf-8 -*-
# from PIL import Image,ImageDraw,ImageFont

# originl_avatar = "sprite.png"
# save_avatar = "new_avatar.png"
# windows_font = "Arial.ttf"
# color = (255,0,0)

# def draw_text(text,fill_color,windows_font):
# 	print("do some")
# 	try:
# 		im = Image.open(originl_avatar)
# 		x,y = im.size
# 		print(im.size,im.format,im.mode)
# 		im.show()

# 		draw = ImageDraw.Draw(im)
# 		font = ImageFont.truetype(windows_font,35)
# 		draw.text((x - 20,7),text,fill_color,font)
# 		im.save(save_avatar)
# 		im.show()
# 	except :
# 		print("Unable to load Image")


# number = str("wave")
# draw_text(number,color,windows_font)

# -*- coding: utf-8 -*-
import random,string

class LengthError(ValueError):
	"""docstring for LengthError"""
	def __init__(self, arg):
		super(LengthError, self).__init__()
		self.arg = arg
def pad_zero_to_left(inputNumString,totalLength):
	lengthOfInput  = len(inputNumString)
	if lengthOfInput > totalLength:
		raise LengthError("error")
	else:
		return '0' * (totalLength - lengthOfInput) + inputNumString

poolOfChars = string.ascii_letters + string.digits
random_codes = lambda x,y:''.join([random.choice(x) for i in range(y)])

def invitation_code_generator(quantity,lengthOfRandom,LengthOfKey):
	placeHoldChar = "L"
	for index in range(quantity):
		tempString = ""
		try:
			yield random_codes(poolOfChars, lengthOfRandom) + placeHoldChar + pad_zero_to_left(str(index), LengthOfKey)
		except LengthError:
			print "Index exceeds the length of master key."

for invitationCode in invitation_code_generator(200,16,4):
	print( invitationCode)
	
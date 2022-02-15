# dog_x = 0
# cat_x = 0
# def dog_move():
# 	global dog_x
# 	dog_x = dog_x + 10
#
# def cat_move():
# 	global cat_x
# 	cat_x = cat_x + 1
# x = 0
class Animals():
	def __init__(self):
		print("Animals 类被初始化")
		self.x = 0

	def move(self):
		# global x
		self.x = self.x + 10
		# x = x + 10
		# return x



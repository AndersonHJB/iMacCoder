from project01 import Animals

cat = Animals()  # 实例化
dog = Animals()
user_input = input()
if user_input == "move":
	# print("dog:{x}, cat:{y}".format(x=dog.x, y=cat.x))
	print("dog:{x}, cat:{y}".format(x=0, y=0))
	cat_x = cat.move()
	dog_x = dog.move()
	print("dog:{x}, cat:{y}".format(x=dog_x, y=cat_x))

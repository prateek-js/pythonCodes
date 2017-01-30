import turtle

def draw_square(shape_name):
	for i in range(1,5):
		shape_name.forward(100)
		shape_name.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(2)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)
	


	# angie = turtle.Turtle()
	# angie.shape("arrow")
	# angie.color("blue")
	# angie.circle(100)
	

	# bengie = turtle.Turtle()
	# bengie.shape("classic")
	# bengie.color("#a0c8f0")
	# bengie.forward(100)
	# bengie.left(120)
	# bengie.forward(100)
	# bengie.left(120)
	# bengie.forward(100)

	window.exitonclick()

draw_art()

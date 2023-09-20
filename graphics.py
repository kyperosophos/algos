import turtle

def draw_board_line(size, angle):
	size *= 20*2**0.5/4
	turtle.left(angle)
	turtle.up()
	turtle.forward(size)
	turtle.left(90)
	turtle.fd(size*3)
	turtle.down()
	turtle.left(180)
	turtle.forward(size*6)

def draw_board(size):
	for i in range(4):
		draw_board_line(size, i*90)
		turtle.up()
		turtle.home()
                                               
def draw_symbol(
	size,
	symbol,
	pos,
):
	t = 20*2**0.5
	x, y = pos
	x *= t * size/2
	y *= t * size/2
	turtle.up()
	turtle.left(90)
	turtle.fd(y)
	turtle.right(90)
	turtle.fd(x)
	turtle.down()
	if symbol == "X":
		turtle.up()
		turtle.fd(-t/2)
		turtle.down()
		turtle.left(45)
		turtle.fd(20*size)
		turtle.left(135)
		turtle.up()
		turtle.forward(20/2**0.5*size)
		turtle.down()
		turtle.left(135)
		turtle.fd(20*size)
	else:
		turtle.circle(10/2**0.5*size)

def reset():
	turtle.up()
	turtle.home()
	turtle.down()

def main():
	size = 4
	draw_board(size)
	reset()
	draw_symbol(size, "X", (-1, 1))
	reset()
	draw_symbol(size, "0", (0,0))
	reset()

if __name__=="__main__":
	main()
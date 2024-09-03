import turtle

equivalent = {"Tourne droite": "right", "Tourne gauche": "left", "Avance": "forward", "Recule": "backward"}

def draw(filename):
	t = turtle.Turtle()
	t.speed(0)
	splitted = ""
	screen = turtle.Screen()
	screen.setup(1000, 800)
	with open(filename, "r") as file:
		t.penup()
		t.goto(-screen.window_width() / 2 + 300, 0)
		t.pendown()
		for line in file:
			line = line.strip()
			if line == "":
				t.penup()
				t.goto(t.xcor() + 300, t.ycor())
				t.pendown()
				continue
			if line[0] == "C":
				continue
			splitted = line.split(" ")
			if splitted[0] or (splitted[0] + " " + splitted[1]) in equivalent:
				if "Avance" in line or "Recule" in line:
					command = splitted[0]
					distance = int(splitted[1])
				else:
					command = splitted[0] + " " + splitted[1]
					distance = int(splitted[3])
				eval("t." + equivalent[command] + "(" + str(distance) + ")")
	turtle.done()

draw("turtle")

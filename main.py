import turtle
import pandas

#-------------DEFINE-SCREEN-----------------#
screen = turtle.Screen()
screen.title("Türkiye Cumhuriyeti Devlet Vilayetleri Oyunu")
screen.bgcolor("lightblue")
screen.setup(width=1400, height=600)
image = "tr_map.gif"
screen.addshape(image)
turtle.shape(image)
#-------------------------------------------#

data = pandas.read_csv("tr_illeri.csv")
all_cities = data.il.to_list()
guessed_cities = []

while len(guessed_cities) != len(all_cities):
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/{len(all_cities)}", prompt="Bir vilayet daha tahmin et! \n Çıkmak için 'Çıkış' yaz. ").capitalize()

    if answer_city == "Çıkış":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("missing_cities.csv")
        break
    if answer_city in all_cities:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("blue")
        city_data = data[data.il == answer_city]
        t.goto(city_data.x.item(), city_data.y.item())
        t.write(answer_city, align="left", font=("Arial", 7, "bold"))
        guessed_cities.append(answer_city)
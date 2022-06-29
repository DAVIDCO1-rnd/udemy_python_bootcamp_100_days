# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(400)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettyTables

table = prettyTables.Table()
table.add_column("Pokemon name", ['data1', 'data2', 'data3'])
table.add_column("Type", ['type1', 'type2', 'type3'])


print(table.table_align)

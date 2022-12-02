import tkinter
import turtle
from tkinter import *
from turtle import RawTurtle
# Introducing the Font module
import tkinter.font as tkfont

import datafile


# Initialization Interface


def gameui():

    # Create a window
    root = Tk()
    root.title("Money Saving Trip")
    root.geometry('800x500+350+150')

    # Create the caption Lable
    # Specifies the font name, size, and style
    # ft = tkfont.Font(family='Fixdsys', size=20, weight=tkfont.BOLD)
    # Applying Fonts
    # Label(root, text='Game Map', font=ft).pack()

    # Left interactive area f1
    f1 = tkinter.Frame(root, width=350, bg='#F5DEB3')
    f1.pack(side=tkinter.LEFT, fill=tkinter.Y, pady=2)

    # The button part of detection result in the left interaction area (floyd algorithm) f3
    f3 = tkinter.Frame(f1, width=350, height=60, bg='#87CEEB')
    f3.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=3)

    # The test result display section in the left interactive area
    f31 = tkinter.LabelFrame(f1, text='Result of Floyd-Warshall algorithm', width=350, height=60, bg='#AFEEEE')
    f31.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=3)
    f4 = tkinter.Label(f31, text='', bg='#FAFAD2', height=5)
    f4.pack(fill=tkinter.X)

    # The button position is a custom place
    tkinter.Button(f3, width=18, height=2, text='check the answer', bg='#90EE90', command=lambda: check_func(f4, tu)).place(x=100, y=6)

    # Here we need to add the text result (Freud's algorithm) to the f4 region
    # The user clicks on the interaction area f5
    f5 = tkinter.LabelFrame(f1, text='user show time', width=350, height=450, bg='#FAFAD2')
    f5.pack(side=tkinter.TOP, fill=tkinter.Y, padx=1, pady=1)

    # Starting point Description
    label1 = tkinter.Label(f5, text='start from the city : A ,'+'\n' +
                                    'find out the lowest cost which could get the destination.', bg='#FAFAD2')
    label1.pack(fill=tkinter.X)
    label2 = tkinter.Label(f5, text='chose your next destination : ', bg='#FAFAD2')
    label2.pack(side=tkinter.LEFT, fill=tkinter.X, padx=1)

    # This area is used to select the next city to reach, and each selection updates the list of cities that can be reached next
    f6 = tkinter.LabelFrame(f1, width=350, height=100, bg='#DEB887')
    f6.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=3)

    # The retraction button, three chances
    f61 = tkinter.LabelFrame(f1, width=350, height=53, bg='#F5DEB3', text='click the button of start')

    f61.pack(side=tkinter.TOP, fill=tkinter.X, padx=3, pady=3)
    revoke_btn = tkinter.Button(f61, width=8, height=1, text='revoke', bg='#8FBC8F')
    revoke_btn.place(x=277, y=-1)
    # revoke_btn.config(text="333")
    # btn_data = revoke_btn.configure().get("text")
    # print(btn_data) # print('text', 'text', 'Text', '', 'revoke')
    # print(btn_data[4])  # Get the text content, where the parameter is 4 Not sure if it's correct, but it works
    revoke_btn.place_forget()  #Hide the button


    # route record
    labelr = tkinter.LabelFrame(f1, text='your route : ', bg='#FAFAD2', width=60, height=120)
    labelr.pack(side=tkinter.TOP, fill=tkinter.X, padx=1)

    label3 = tkinter.Label(labelr, text='', bg='#FAFAD2', height=90)
    label3.pack(fill=tkinter.X)
    # total cost
    costlabel = tkinter.Label(labelr, width=10, height=1, text='cost : ', bg='#FFE4C4')
    costlabel.place(x=268, y=-12)
    # start button
    tkinter.Button(f61, width=8, height=1, text='start', bg='#8FBC8F', command=lambda: start_fun(tu, f6, f61, label3, costlabel)).place(x=1, y=-1)
    # Interactive area on the right
    f2 = tkinter.Frame(root, width=450, bg='#B0C4DE')
    f2.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    # The top half is map f7
    f7 = tkinter.LabelFrame(f2, width=435, height=350, bg='#C0C0C0', text='Map')
    f7.place(x=3, y=3)
    # Place the canvas
    #Creating a Canvas
    canvas = Canvas(f7, width=431, height=350, bg="#C0C0C0")
    # Set the canvas placement layout
    canvas.pack()
    # turtle.TurtleScreen(canvas).bgcolor("#C0C0C0")
    tu = RawTurtle(canvas)
    # tu.color("#C0C0C0")
    tu.getscreen().bgcolor("#C0C0C0")
    tu.pensize(2)
    tu.hideturtle()


    # The bottom half is the level button f8
    f8 = tkinter.LabelFrame(f2, width=438, height=110, bg='#FFEBCD', text='Level')
    f8.place(x=3, y=383)
    # Level Button group
    # The command link function is preceded by lambda if it takes an argument and removed with parentheses if it takes no argument
    tkinter.Button(f8, width=6, height=1, text='level 1', bg='#FFD700', command=lambda: loadmap(tu, 1)).place(x=14, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 2', bg='#FFD700', command=lambda: loadmap(tu, 2)).place(x=72, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 3', bg='#FFD700', command=lambda: loadmap(tu, 3)).place(x=130, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 4', bg='#FFD700', command=lambda: loadmap(tu, 4)).place(x=189, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 5', bg='#FFD700', command=lambda: loadmap(tu, 5)).place(x=248, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 6', bg='#FFD700', command=lambda: loadmap(tu, 6)).place(x=307, y=6)
    tkinter.Button(f8, width=6, height=1, text='level 7', bg='#FFD700', command=lambda: loadmap(tu, 7)).place(x=365, y=6)

    root.mainloop()
    print("hello888")


# Clear all widgets
def clear_all(frame):
    for item in frame.winfo_children():
        item.destroy()
      #button.config(state= "disabled")


# The start button provides the first reachable city and resets the back button to 3 times
def start_fun(tu, f6, f61, label3, costlabel):
    datafile.route = ""
    datafile.player_cost = 0
    # Determine if there is a map
    if datafile.map_exist == 1:
        datafile.revoke_num = 3
        f61.config(text="destination "+datafile.destination)
        # Determine the current map and take out the data
        next_city(f6, "A", tu, label3, costlabel)


def next_city(f6, startcity, tu, label3, costlabel):
    # Clear all buttons
    clear_all(f6)
    # If you're not there yet
    if startcity != datafile.destination:
        # Calculate how many neighboring cities there are
        btnlist = []
        # fromx, fromy, tox, toy, cost = 0

        for i in range(len(datafile.current_map)):
            if datafile.current_map[i][0] == startcity:
                nextcity = datafile.current_map[i][3]
                fromx = datafile.current_map[i][1]
                fromy = datafile.current_map[i][2]

                # If the current starting city has no neighboring cities
                #if len(nextcity) == 0:
                    #tkinter.Label(f6, text='sorry! there is no way!.', bg='#FAFAD2')
                #else:
                # Generate the city selection button
                btn_num = len(nextcity)
                count = 0
                for j in range(btn_num):
                    # Get button data
                    btncity = nextcity[j][0]
                    print(btncity)
                    # button number

                    # Assign a value to a button, and assign a position to the button
                    # btnlist.append(tkinter.Button(f6, width=8, height=1, text=btncity+' city', bg='#8FBC8F',
                    #                               command=lambda: markroute(f6, startcity, tu, fromx, fromy,
                    #                                                         nextcity[j][0], "yellow")))
                    if btncity not in datafile.route:
                        btnlist.append(tkinter.Button(f6, width=8, height=1, text=btncity, bg='#8FBC8F'))
                        print(datafile.next_city_position[count][0], datafile.next_city_position[count][1])
                        btnlist[count].place(x=datafile.next_city_position[count][0], y=datafile.next_city_position[count][1])
                        btnlist[count].bind("<Button-1>", lambda event: markroute(event, f6, label3, costlabel, startcity,
                                                                              tu, fromx, fromy, "yellow"))
                        count = count+1
                if len(btnlist) == 0:
                    f6.config(text="sorry!There is no way!")
    else:
        f6.config(text="you have arrive the destination!!! ")



# Loading map functions
# To draw a map, it is necessary to provide the parameter center coordinates (x,y), city name name, adjacent city name nextname, and the cost of reaching the adjacent city

def loadmap(tu,level):
    tu.speed(0)
    #speed(9)
    r = 20
    '''
    maplist = [
        ['A', -180, 0, [['B', -100, 80, 2], ['C', -110, -60, 7]]],
        ['B', -100, 80, [['D', 120, 80, 1]]],
        ['C', -110, -60, [['E', 80, -50, 2]]],
        ['D', 120, 80, [['F', 0, 10, 3]]],
        ['E', 80, -50, [['G', 150, 0, 8]]],
        ['F', 0, 10, [['E', 80, -50, 2]]],
        ['G', 150, 0]
    ]
    '''
    if level == 1:
        maplist=datafile.level_1
        datafile.current_map = datafile.level_1
        datafile.current_matrix = datafile.matrix_1
        datafile.destination = "E"  # Setting the Destination
    elif level == 2:
        maplist=datafile.level_2
        datafile.current_map = datafile.level_2
        datafile.current_matrix = datafile.matrix_2
        datafile.destination = "F"  # Setting the Destination
    elif level == 3:
        maplist=datafile.level_3
        datafile.current_map = datafile.level_3
        datafile.current_matrix = datafile.matrix_3
        datafile.destination = "G"  #Setting the Destination
    elif level == 4:
        maplist=datafile.level_4
        datafile.current_map = datafile.level_4
        datafile.current_matrix = datafile.matrix_4
        datafile.destination = "G"  # Setting the Destination
    elif level == 5:
        maplist=datafile.level_5
        datafile.current_map = datafile.level_5
        datafile.current_matrix = datafile.matrix_5
        datafile.destination = "I"  # Setting the Destination
    elif level == 6:
        maplist=datafile.level_6
        datafile.current_map = datafile.level_6
        datafile.current_matrix = datafile.matrix_6
        datafile.destination = "I"  # Setting the Destination
    elif level == 7:
        maplist=datafile.level_7
        datafile.current_map = datafile.level_7
        datafile.current_matrix = datafile.matrix_7
        datafile.destination = "L"  # Setting the Destination

    # If the map has already loaded, you can reload the map
    if datafile.map_loaded == 1:
        # Mark the map as unloaded first to prevent other buttons from interrupting the loading
        datafile.map_loaded = 0
        #  Clear the canvas
        tu.clear()
        # Go through the data list, draw a circle of the local city, write the name, when the length is 4, there are adjacent cities, draw the line to the adjacent city, mark the cost
        citynum = len(maplist)
        # print(citynum)
        for i in range(citynum):
            tu.up()   
            tu.goto(maplist[i][1], maplist[i][2]-r)  
            tu.down()   # Put down the pen
            tu.circle(20)  # A circle
            # Write the city name
            tu.up()  # Lift the pen
            tu.goto(maplist[i][1], maplist[i][2]+3)  # Back to the center of the circle
            if datafile.destination == maplist[i][0]:
                tu.pencolor("green")
                tu.write(maplist[i][0], font=("黑体", 11, 'bold'))
            else:
                tu.pencolor("black")
                tu.write(maplist[i][0], font=("黑体", 11, 'bold'))
            tu.down()  
            # If there are neighboring cities
            if len(maplist[i]) == 4:
                # Every neighboring city has to be wired
                nextcitynum = len(maplist[i][3])
                # print(nextcitynum)
                for j in range(nextcitynum):
                    # Cut information about adjacent cities
                    info = maplist[i][3][j]
                    #infolist = info[0].split(",")
                    # tu.pencolor("black")
                    markroute2(tu, maplist[i][1], maplist[i][2], maplist[i][3][j][1], maplist[i][3][j][2],
                               maplist[i][3][j][3], "black")
                 
                    '''
                    tu.up()  # 抬起笔
                    tu.goto(maplist[i][1], maplist[i][2])  # 回到出发城市圆心
                    tu.down()  # 放下笔
                    tu.goto(maplist[i][3][j][1], maplist[i][3][j][2])  # 去到相邻城市圆心
                    tu.up()  # 抬起笔
                    tu.goto((maplist[i][1]+maplist[i][3][j][1])/2,
                            (maplist[i][2]+maplist[i][3][j][2])/2+5)  # 到路线中心写下费用
                    tu.write(maplist[i][3][j][3], font=("黑体", 10, 'bold'))
                    '''
        datafile.map_loaded = 1
        datafile.map_exist = 1


# City highway code,fromx,fromy, tox is the center of the departure city,toy is the center of the arrival city, cost is the bus fare
def markroute(event, f6, label3, costlabel, startcity, tu, fromx, fromy,color):
    btncity = event.widget['text']
    dlist = [1, 2, 3]
    tox = dlist[0]
    toy = dlist[1]
    cost = dlist[2]
    nextlist = []
    # Get to the city marked on the button
    for i in range(len(datafile.current_map)):
        if datafile.current_map[i][0] == startcity:
            nextlist = datafile.current_map[i][3]
            for j in range(len(nextlist)):
                if nextlist[j][0] == btncity:
                    tox = nextlist[j][1]
                    toy = nextlist[j][2]
                    cost = nextlist[j][3]
                    datafile.player_cost += cost
                    # print(tox, toy, cost)

    linckcircle(tu, fromx, fromy, tox, toy, cost, color)   
    datafile.route +=startcity+"----->"+btncity+"   "
    label3['text'] = datafile.route
    costlabel['text'] = datafile.player_cost
    next_city(f6, btncity, tu, label3, costlabel)


def markroute2(tu, fromx, fromy, tox, toy, cost, color):
    linckcircle(tu, fromx, fromy, tox, toy, cost, color)


def linckcircle(tu, fromx, fromy, tox, toy, cost, color):
    tu.pencolor(color)
    tu.up()  
    tu.goto(fromx, fromy) 
    tu.down()  
    tu.goto(tox, toy)  
    tu.up() 
    tu.goto((fromx + tox) / 2,
            (fromy + toy) / 2 + 8) 
    tu.pencolor("red")
    tu.write(cost, font=("黑体", 15, 'bold'))
    tu.pencolor("black")


# check button click function
def check_func(f4, tu):
    if len(datafile.current_matrix) != 0:
        floyd(datafile.current_matrix, f4, tu)

    else:
        print("no map")


# Floyd algorithm
def floyd(map_matrix, f4, tu):
    vertex_num = len(map_matrix)
    matrix = [[0 for i in range(vertex_num)] for j in range(vertex_num)]
    for i in range(vertex_num):
        for j in range(vertex_num):
            matrix[i][j] = map_matrix[i][j]

    # Initializes the matrix of vertices through which the shortest path from vertex A to vertex B passes
    route_matrix = [[0 for i in range(vertex_num)] for j in range(vertex_num)]

    for i in range(vertex_num):
        for j in range(vertex_num):
            if matrix[i][j] > 0:         # -1 means not directly reachable,0 means self to self
                route_matrix[i][j] = j+1    # j+1 is the name of the reachable vertex
            else:
                route_matrix[i][j] = 0
    for k in range(vertex_num): #k is the intermediate node
        for i in range(vertex_num):
            for j in range(vertex_num):
                #
                if matrix[i][k] > 0 and matrix[k][j] > 0 and (matrix[i][k] + matrix[k][j] < matrix[i][j] or matrix[i][j] == -1):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    route_matrix[i][j] = k+1
        '''
        print("第%d次循环：" % (k+1))
        print("距离矩阵：")
        for row in matrix:
            print(row)
        print("途径矩阵:")
        for row in route_matrix:
            print(row)
        '''
    for row in route_matrix:
        print(row)
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
    start_index = name.index('A') 
    destination_index = name.index(datafile.destination)
    floyd_route(route_matrix, 'A', datafile.destination, f4, matrix[start_index][destination_index], tu)


# Output the route according to the path matrix
def floyd_route(route_matrix, start, destination, f4, cost, tu):
    # city name
    name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
    route = []
    start_index = name.index(start)     
    target = destination   
    destination_index = name.index(destination)     
    transit = ""    

    # Find the transition point between origin and destination until the latest transition point and the latest destination are directly accessible and update the route
    while start != target:
        while True:
            tran_position = route_matrix[start_index][destination_index]-1   # Numerical marks for transition points

            # If the transition point and destination are reachable directly, they are added to the roadmap
            if name[tran_position] == target:
                # route.append([name[start_index], target])
                route.insert(0, [name[start_index], target])

                # Update the destination
                target = name[start_index]
                destination_index = start_index
                break
            else:
                # Find the transition point to the transition point of the destination
                #The new starting point is the transition point
                start_index = tran_position

        start_index = name.index(start)

    f4['text'] = ""
    print_route = ""
    for i in range(len(route)):
        print_route += route[i][0]+"---->"+route[i][1]+"  "
        floyd_link(route[i][0], route[i][1], tu)
        f4['text'] = print_route
    f4['text'] = print_route + "cost：" + str(cost)

    print(route)


def floyd_link(startcity, destination, tu):

    for i in range(len(datafile.current_map)):
        if datafile.current_map[i][0] == startcity:
            fromx = datafile.current_map[i][1]
            fromy = datafile.current_map[i][2]
        if datafile.current_map[i][0] == destination:
            tox = datafile.current_map[i][1]
            toy = datafile.current_map[i][2]

    tu.pencolor("red")
    tu.up() 
    tu.goto(fromx, fromy)  
    tu.down() 
    tu.goto(tox, toy) 
    tu.up() 
    tu.goto((fromx + tox) / 2,
            (fromy + toy) / 2 + 8) 
    tu.pencolor("red")
    tu.pencolor("black")


if __name__ == '__main__':

    gameui()


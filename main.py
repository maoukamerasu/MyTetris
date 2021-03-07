import tkinter
import random
root = tkinter.Tk()
root.resizable(False,False)
root.bind("")
root.title("テトリス")
key=""
keyoff=False
def press_key(e):
    global key,keyoff
    key=e.keysym
    keyoff= False
def release_key(e):
    global keyoff
    keyoff = True
root.bind("<KeyPress>",press_key)
root.bind("<KeyRelease>",release_key)

canvas=tkinter.Canvas(width=450,height=600,bg="black")
canvas.pack()
block=[]
block_0 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0],
    [1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0],
    [1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0]
]
block_1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0],
    [0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0],
    [1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0]
]
block_2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0],
    [1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0]
]
block_3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0],
    [1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0]
]
block_4 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
    [0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0]
]
block_5 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
    [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
]
block_6 = [
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0]
]
key = ""
block_x = 4
block_y = -4
block_size=30
block_type=0
time=0
bottom=0
next_block=0
show_next=[]
score=0
gameover=False
colour=["maroon4","brown2","goldenrod","darkgreen","cyan4","gray","pink"]
blinking=False
blinking_time=0

def Collision_Detection(block_x,block_y,block_type):
    global block
    if block_type==4:
        block_type=0
    for x in range(4):
        for y in range(4):
            if block[y][x+block_type*4] == 1:
                if block_x+x>=0 and block_x+x<10 and block_y+y<20:
                    if field[block_y+y+4][block_x+x]>0:
                        return True
                else:
                    return True
    return False
def gameover():
    global field
    for y in range(4):
        for x in range(10):
            if field[y][x]==1:
                return True
    return False
def blinking_block():
    global field, score,blinking_time,blinking,blinking_delete
    y_1st = 23
    if blinking_time <= 0:
        while y_1st >= 4:
            blinking_delete = True
            for x in range(10):
                if field[y_1st][x] == 0:
                    blinking_delete = False
            if blinking_delete == True:
                for x in range(10):
                    blinking_field[y_1st][x]=1
                blinking = True
            y_1st -= 1
        if blinking == True:
            blinking_time = 10

def blinking_reset():
    for x in range(10):
        for y in range(24):
            blinking_field[y][x]=0

def delete_block():
    global field, score,blinking
    y_1st=23
    while y_1st>=4:
        delete = True
        for x in range(10):
            if field[y_1st][x]==0:
                delete=False
        if delete==True:
            y_2nd=y_1st
            while y_2nd>=4:
                for x in range(10):
                    field[y_2nd][x]=field[y_2nd-1][x]
                y_2nd=y_2nd-1
            y_1st=y_1st+1
            score+=50
            if score>9999:
                score=9999
            canvas.delete("SCORE")
            canvas.create_text(400, 80, text=score, fill="white", font=("NewRamon", 25), tag="SCORE")
        y_1st-=1
def create_block(block_index):
    if block_index ==0:
        block=block_0
    elif block_index ==1:
        block = block_1
    elif block_index ==2:
        block = block_2
    elif block_index ==3:
        block = block_3
    elif block_index ==4:
        block = block_4
    elif block_index ==5:
        block = block_5
    elif block_index ==6:
        block = block_6
    return block
def block_change():
    global block, block_type,block_0,block_1,block_2,block_3,block_4,block_5,block_6,next_block,block_colour,colour_value,next_colour_value
    block_index = next_block
    block=[]
    block=create_block(block_index)
    block_type=0
    next_block=random.randint(0,6)
    colour_value=next_colour_value
    next_colour_value=next_block

def field_block():
    global block_x, block_y,field,block_type,block
    for x in range(4):
        for y in range(4):
            if block[y][x+block_type*4] > 0:
               field[block_y+y+4][block_x+x] = colour_value+1
    block_y = -4
    block_x = 4
    block_change()
canvas.create_rectangle(0,0,301,600,outline="white")
canvas.create_rectangle(319,99,441,221,outline="white")
canvas.create_text(345,50,text="Score",fill="white",font=("NewRamon",18))
canvas.create_text(400, 80, text=score, fill="white", font=("NewRamon", 25), tag="SCORE")
def next():
    show_next=create_block(next_block)
    for x in range(4):
        for y in range(4):
            if show_next[y][x] == 1:
                  canvas.create_rectangle(320+x*block_size,100+y*block_size,320+x*block_size+block_size,100+y*block_size+block_size,fill=colour[next_colour_value],tag="BLOCK")
def draw_field():
    canvas.delete("FIELD")
    global field,block_x,block_y,block_size
    for x in range(10):
        for y in range (4,24):
            if blinking == False:
                if field[y][x] > 0:
                    canvas.create_rectangle(x*block_size,(y-4)*block_size,x*block_size+block_size,(y-4)*block_size+block_size,fill=colour[field[y][x]-1], tag="FIELD")
            elif blinking == True:
                if field[y][x] > 0:
                    if blinking_field[y][x] != 1:
                        canvas.create_rectangle(x * block_size, (y - 4) * block_size, x * block_size + block_size,
                                        (y - 4) * block_size + block_size, fill=colour[field[y][x] - 1], tag="FIELD")
                    elif blinking_field[y][x] == 1 and blinking_time%3==0:
                        canvas.create_rectangle(x * block_size, (y - 4) * block_size, x * block_size + block_size,
                                                (y - 4) * block_size + block_size, fill=colour[field[y][x] - 1],
                                                tag="FIELD")
def reset(event):
    global score, next_colour_value, block_y,gameover
    for x in range(10):
        for y in range(24):
            field[y][x]=0
    score = 0
    canvas.delete("SCORE")
    canvas.create_text(400, 80, text=score, fill="white", font=("NewRamon", 25), tag="SCORE")
    next_colour_value = next_block
    block_change()
    draw_field()
    block_y = -4
    canvas.delete("GameOver")
field=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]
blinking_field=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]
def move_block():
    global key,keyoff,block_x,block_y,block_type,bottom
    if bottom > 1:
        if key == "Left":
            if Collision_Detection(block_x-1,block_y,block_type) == False:
                 block_x = block_x - 1
                 bottom=0
        if key == "Right":
            if Collision_Detection(block_x+1,block_y,block_type) == False:
                 block_x = block_x + 1
                 bottom = 0
    if key == "Down":
        if Collision_Detection(block_x,block_y+1,block_type) == False:
            block_y = block_y + 1
            bottom = 0
    if bottom > 2:
        if key == "Up":
            if Collision_Detection(block_x, block_y,block_type+1) == False:
                  block_type = block_type + 1
                  if block_type==4:
                       block_type=0
            bottom = 0
    if keyoff == True:
        key=""
        keyoff=False
def bool(bool):
    return not bool
def draw_block():
    global pause
    canvas.delete("pause_text")
    canvas.delete("BLOCK")
    global block_y,block_size,block
    for x in range(block_type*4, block_type*4+4):
        for y in range(4):
            if block[y][x] > 0:
                canvas.create_rectangle((block_x + (x-block_type*4))*30, (block_y + y)*30, block_size + (block_x +
                                        (x-block_type*4))*30, block_size + (block_y+ y)*30, fill=colour[colour_value],tag="BLOCK")
    if pause == True:
        canvas.create_text(150, 250, text="PAUSE", fill="white", font=("New Roman", 30), tag="pause_text")
    elif pause == False:
        canvas.delete(pause)
def main():
    global block_y,time,keyoff,bottom,block,pause,key,blinking,blinking_time
    resetButton = tkinter.Button(root, text='reset',width=6,height=3)
    resetButton.place(x=360, y=500)
    resetButton.bind("<Button-1>",reset)
    bottom = bottom + 1
    if key == "p" and bottom >2:
        pause =not pause
        key = ""
    draw_block()
    next()
    if gameover()==False and pause!=True:
        if blinking_time > 0:
            blinking_time = blinking_time - 1
            draw_field()
            if blinking_time <= 0:
                blinking = False
                delete_block()
                draw_field()
                blinking_reset()
        else:
            move_block()
            time = time + 1
            if time==8:
                if Collision_Detection(block_x,block_y+1,block_type) == False:
                    block_y = block_y + 1
                else:
                    field_block()
                    blinking_block()
                    draw_field()
                    gameover()
                time = 0
    elif gameover()==True:
          canvas.create_text(150, 250, text="Game Over", fill="white", font=("New Roman", 30),tag="GameOver")
    root.after(60, main)
next_block=random.randint(0, 6)
pause=False
global block_colour
next_colour_value = next_block
block_change()
main()
root.mainloop()
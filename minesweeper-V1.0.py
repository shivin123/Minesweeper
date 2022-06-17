#!/usr/bin/env python
# coding: utf-8

# In[ ]:


debug_mode=0
import random
gip=1
#board creation

hight_upper=10 #hard coded limts on hight
hight_lower=5
if debug_mode==1:
    print("Upper Hight limit:", hight_upper)
    print("Lower Hight limit:", hight_lower)
while True:
    h=input("Enter the hight of the board: ")
    if h.isdigit():
        h=int(h)
    else:
        print("Invlaid input, Not a number")
        continue
    if isinstance(h, float):
        print("Input invlaid, Not an integer")
        continue
    if hight_lower<=h and h<=hight_upper:
        break
    else:
        print("Invlaid input, Not in range")
    
width_upper=10 #hard coded limts on width
width_lower=5

if debug_mode==1:
    print("Upper Width limit:", width_upper)
    print("Lower Width limit:", width_lower)

while True:
    w=input("Enter the hight of the board: ")
    if w.isdigit():
        w=int(w)
    else:
        print("Invlaid input, Not a number")
        continue
    if isinstance(w, float):
        print("Input invlaid, Not an integer")
        continue
    if width_lower<=w and w<=width_upper:
        break
    else:
        print("Invlaid input, Not in range")
        
print("Your selected hight and width are",h,w,"respectivly.")

area=h*w
mul=int(area/5) #mine upper limit
mll=int(area/10) #mine lower limit


print("Upper Mine limit:", mul)
print("Lower Mine limit:", mll)

while True:
    mn=input("Enter the number of mine on the board: ")
    if mn.isdigit():
        mn=int(mn)
    else:
        print("Invlaid input, Not a number")
        continue
    if isinstance(mn, float):
        print("Input invlaid, Not an integer")
        continue
    if mll<=mn and mn<=mul:
        break
    else:
        print("Invlaid input, Not in range")
        
if debug_mode==1:
    print("Number of mines:",mn)
     
#the first two levels are for storeing the location of each tile
#in the base arry 
#pos 0:Number of adjcent mines
#pos 1:has mine 
#pos 2:is revelveled
#pos 3:is flaged
board=[[[0,False,False,False] for j in range(h)] for i in range(w)]
if debug_mode==1:
    print(board)


def print_board_P(board):
    top="|     |"
    for i in range(w):
        if i<9:
            top+=(" C"+str(i+1)+"  | ")
        else:
            top+=("C"+str(i+1)+"  | ")
    print(top)
    e1=0
    for i in range(h):
        if i<9:
            line="|  R"+str(e1+1)+" |"
        else:
            line="| R"+str(e1+1)+" |"
        e1+=1
        for e in range(w):
            if board[e][i][2]==False:
                if board[e][i][3]==True:
                    line+=" F   | "
                    continue
                else:
                    line+=" T   | "
                    continue
            else:
                if board[e][i][0]==0:
                    line+="     | "
                    continue
                else:
                    line+=" "+str(board[e][i][0])+"   | "
                    continue
        print(line)
    

print_board_P(board)

all_loc=[]
for i in range(h):
    for e in range(w):
        all_loc.append([i,e])
        

        
if debug_mode==1:
    print(all_loc)
    
mine_loc=random.choices(all_loc, k=mn)

if debug_mode==1:
    print("Mine Locations:")
    print(mine_loc)
    
for i in mine_loc:
    board[i[0]][i[1]][1]=True
    
    try:
        if i[0]-1>=0 and i[1]-1>=0:
            board[i[0]-1][i[1]-1][0]+=1
    except:
        pass
    try:
        if i[0]-1>=0:
            board[i[0]-1][i[1]][0]+=1
    except:
        pass
    try:
        if i[0]-1>=0 and i[1]<w-1:
            board[i[0]-1][i[1]+1][0]+=1
    except:
        pass
    try:
        if i[1]-1>=0:
            board[i[0]][i[1]-1][0]+=1
    except:
        pass
    try:
        if i[1]<w-1:
            board[i[0]][i[1]+1][0]+=1
    except:
        pass
    try:
        if i[1]-1>=0 and i[0]<h-1:
            board[i[0]+1][i[1]-1][0]+=1
    except:
        pass
    try:
        if i[0]<h-1:
            board[i[0]+1][i[1]][0]+=1
    except:
        pass
    try:
        if i[0]<h-1 and i[1]<w-1:
            board[i[0]+1][i[1]+1][0]+=1
    except:
        pass
    
    
def print_board_C(board):
    top="|     |"
    for i in range(w):
        if i<9:
            top+=(" C"+str(i+1)+"  | ")
        else:
            top+=("C"+str(i+1)+"  | ")
    print(top)
    e1=0
    for i in range(h):
        if i<9:
            line="|  R"+str(e1+1)+" |"
        else:
            line="| R"+str(e1+1)+" |"
        e1+=1
        for e in range(w):
            if board[e][i][1]==True:
                line+=" M   | "
                continue
            else:
                if board[e][i][0]==0:
                    line+="     | "
                    continue
                else:
                    line+=" "+str(board[e][i][0])+"   | "
                    continue
        print(line)
    
if debug_mode==1:
    print_board_C(board)
    
def play_move(cord):
    x=int(cord[0])-1
    y=int(cord[1])-1
    if board[x][y][1]==True:
        print("Game over, you hit a mine.")
        gip=0
        return None
    
    board[x][y][2]=True
    
    loa=[]
    
    loa.append([x,y])
    
    ars=[[x,y]]
    
    
    find_n(loa, ars)
    
            
    
def find_n(loa, ars):
    
    ploa=[]
    
    for i in loa:
        x=i[0]
        y=i[1]
        
        qloa=[]
        
        ars.append([x,y])
        
        if x>0:
            if board[x-1][y][2]==False:
                qloa.append([x-1,y]) #numpad pos 4
                
            if y<w-1:
                if board[x-1][y+1][2]==False:
                    qloa.append([x-1,y+1])   #numpad pos 1
        if y>0:
            if board[x][y-1][2]==False:
                qloa.append([x,y-1]) #numpad pos 8
            if x<h-1:
                if board[x+1][y-1][2]==False:
                    qloa.append([x+1,y-1])   #numpad pos 9
        if x>0 and y>0:
            if board[x-1][y-1][2]==False:
                qloa.append([x-1,y-1]) #numpad pos 7

        if x<h-1:
            if board[x+1][y][2]==False:
                qloa.append([x+1,y]) #numpad pos 2
        if x<h-1 and y<w-1:
            if board[x+1][y+1][2]==False:
                qloa.append([x+1,y+1])   #numpad pos 3
        if y<w-1:
            if board[x][y+1][2]==False:
                qloa.append([x,y+1]) #numpad pos 6
        
        
        
        for i in qloa:
            try:

                if board[i[0]][i[1]][0]==0 and board[i[0]][i[1]][2]==False:
                    ploa.append(i)
                if board[i[0]][i[1]][1]==False:
                    board[i[0]][i[1]][2]=True
            except:
                pass
    floa=[]
    for i in ploa:
        if i not in ars:
            floa.append(i)
    if len(floa)==0:
        return None
    find_n(floa, ars)
    
def move():
    if gip==0:
        return None
    y=input("Enter row number:")
    x=input("Enter columb number:")

    move=[x,y]
    play_move(move)

    print_board_P(board)    
    
CT=area-mn
while gip==1:
    
    if gip==0:
        break
    
    CT_T=0
    for i in board:
        for e in i:
            if e[1]==False and e[2]==True:
                CT_T+=1
    if gip==0:
        break
    
    move()
    
    if CT==CT_T:
        gip==0
        break
            
print("")
print("Game Over:")
print("")
print_board_C(board)    
    


# In[ ]:





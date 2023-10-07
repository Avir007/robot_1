s=input('Enter you string of char')
ans=[0,0,"S"]
x_limit=5
y_limit=4
def breach_condition(x_coord,y_coord):
    if(x_coord<0 or x_coord>x_limit or y_coord<0 or y_coord>y_limit):
        # breach stay at your position
        return False
    else:
        return True

dict={"E":[0,1],"W":[0,-1],"N":[-1,0],"S":[1,0]}
def move(dir,x_coord,y_coord):
    a=[0,0]
    # dict[dir]
    # print("dictionary of dir :",a)
    a[0]=dict[dir][0]+x_coord
    a[1]=dict[dir][1]+y_coord
    print("coordinate array :",a)
    return a

def game(s,x_coord,y_coord,dir,index):
    if(index==len(s)):
        ans[0]=x_coord
        ans[1]=y_coord
        ans[2]=dir
        return
    if(s[index]=="M"):
        new_dir_arr=move(dir,x_coord,y_coord)
        if(breach_condition(new_dir_arr[0],new_dir_arr[1])):
            game(s,new_dir_arr[0],new_dir_arr[1],dir,index+1)
        else:
            game(s,x_coord,y_coord,dir,index+1)
    else:
        game(s,x_coord,y_coord,s[index],index+1)

game(s,0,0,"S",0)
print("ANS IS :",ans)

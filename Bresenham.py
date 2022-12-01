def distance(x,y,d):
    if x!=end_x and y!=end_y:
        if d<0:
            x=x+1
            print(f"( {x} , {y} )")
            d=d+2*dy
            distance(x,y,d)
        else:
            x=x+1
            y=y+1
            print(f"( {x} , {y} )")
            d=d+2*(dy-dx)
            distance(x,y,d)
    else:
        return 0

start_x=int(input("Enter start x : "))
end_x=int(input("Enter end x : "))
start_y=int(input("Enter start y : "))
end_y=int(input("Enter end y : "))
steps=1
dx=end_x-start_x
dy=end_y-start_y
d=2*dy-dx
distance(int(start_x),int(start_y),d)
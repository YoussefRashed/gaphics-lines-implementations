def mid(x,y,q):
    if x!=end_x and y!=end_y:
        if q<0:
            x=x+1
            print(f"( {x} , {y} )")
            q=q+dy
            mid(x,y,q)
        else:
            x=x+1
            y=y+1
            print(f"( {x} , {y} )")
            q=q+dy-dx
            mid(x,y,q)
    else:
        return 0
start_x=20
end_x= 30
start_y=10
end_y=18
dx=end_x-start_x
dy=end_y-start_y
q_intit=dy-(dx/2)
print(q_intit)
mid(start_x,start_y,q_intit)
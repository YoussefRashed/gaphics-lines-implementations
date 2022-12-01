start_x=int(input("Enter start x : "))
end_x=int(input("Enter end x : "))
starty=int(input("Enter start y : "))
endy=int(input("Enter end y : "))
steps=1
slope=(endy-starty)/(end_x-start_x)
if(slope<=1):
    while starty !=endy and start_x!=end_x: 
        start_x=start_x+1
        starty=starty+slope
        print(f"step {steps}(",start_x," , ",starty.__round__(),")")
        steps=steps+1
else:
    while starty !=endy and start_x!=end_x: 
        start_x=start_x+(1/slope)
        starty=starty+1
        print(f"step {steps}(",start_x," , ",starty.__round__(),")")
        steps=steps+1
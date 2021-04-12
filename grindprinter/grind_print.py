# Print a Grid
line1=""
line2=""
line3=""
for i in range( 20 ):
    if i == 0 or i % 10 ==0 or i==19:
        line1=line1+"+"
        line2=line2+"|"
        line3=line3+" "
    elif i % 2 == 0:
        line1=line1+"-"
        line2=line2+" "
        line3=line3+" "
    line1=line1+" "
    line2=line2+" "
    line3=line3+" "
for j in range( 21 ):
    if j ==0 or j == 10 or j ==20:
        print(line1)
    elif j % 2 == 0:#every even number prints line 2
        print(line2)
    else:#every odd number prints line 3
        print(line3)

input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
if a == 0 :
    a = str(a)
    output_data = open("output.txt","w")
    output_data.write(a)
else:  
    for x1 in range(-101,101):
            if a * (x1 ** 3) + b * (x1 ** 2) + c * x1 + d == 0:
                p = x1 + 1
                break
            else:
                x1 = " "
    for x2 in range(p,101):
        if  a * (x2 ** 3) + b * (x2 ** 2) + c * x2 + d == 0:
            o = x2 + 1
            break
        else:
            x2 = " "
    for x3 in range(o,101):
        if a * (x3 ** 3) + b * (x3 ** 2) + c * x3 + d == 0:
            i = x3 + 1
            break
        else:
            x3 = " "        
v = str(x1) + " " + str(x2) + " " + str(x3)
output_data = open("output.txt","w")
output_data.write(v)
output_data.close()
input_data.close()


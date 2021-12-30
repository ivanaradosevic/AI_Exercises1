file_object=open("example.txt", "w")
with open('izrazi.txt', 'r') as f:
    lines=f.readlines()
    for l in lines:
        linija= l.rstrip('\n')
        prvi_broj= int(l[0])
        drugi_broj=int(l[1])
        print(f"{linija}={eval(1)}")
        file_object.write(linija + "=" + str(eval(1)) + "\n")
file_object.close()




#5. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste


li_a = ["Ivana", 13, "Yoko", 3, "Sting", 35]
br=[]
st=[]

for i in li_a:
    if type(i)==int:
        br.append(i)
    elif type(i)==str:
        st.append(i)
print(br)
print(st)

# bilo mi je teško riješiti bez kolege 
 



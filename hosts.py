

f = open("hosts.cfg", "w")
f.write("###MESONES 1-4###\n")
meson=1
for i in range (41,61,5):
    f.write("#MESON "+str(meson)+"\n")
    f.write("define host {\n")
    f.write("use windows-server\n")
    f.write("host_name meson"+str(meson)+"\n")
    f.write("alias meson"+str(meson)+"\n")
    f.write("address 192.168.23."+str(i)+"\n")
    f.write("icon_image win40.png\n")
    f.write("}\n")
    meson+=1
n=5
f.write("###EQUIPOS 41-60###\n")
for i in range (41,61):
    f.write("#EQUIPO "+str(i)+" - "+"MESON "+str(n//5)+"\n")
    f.write("define host {\n")
    f.write("use windows-server\n")
    f.write("host_name equipo"+str(i)+"\n")
    f.write("alias equipo"+str(i)+"\n")
    f.write("address 192.168.23."+str(i)+"\n")
    f.write("icon_image win40.png\n")
    f.write("parents meson"+str(n//5)+"\n")
    f.write("}\n")
    n+=1

f.write('###HIJOS###\n')
vm=0
equipo=41
for i in range (150,210):
    if vm==3:
        vm=0
        equipo+=1
    if vm==0:
        f.write("#EQUIPO "+str(equipo)+"-"+"SERVIDOR\n")
    else:
        f.write("#EQUIPO "+str(equipo)+"-"+"CLIENTE " +str(vm)+"\n")
    f.write("define host {\n")
    f.write("use generic-switch\n")
    f.write("host_name equipo"+str(equipo)+"-vm"+str(vm)+"\n")
    f.write("alias equipo"+str(equipo)+"\n")
    f.write("address 192.168.23."+str(i)+"\n")
    f.write("parents equipo"+str(equipo)+"\n")
    f.write("icon_image debian.png\n")
    f.write("}\n")
    vm+=1
    

f.close()
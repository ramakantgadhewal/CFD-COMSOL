import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


height = np.loadtxt("videoheight_v0.txt")
lenheight = np.size(height)
t = np.linspace(0,np.size(height)-1,np.size(height))
# print(lenheight)
# print(np.size(t))

# plt.plot(t,height)
# plt.show()

# comsolheightdata = np.loadtxt("comsolheight.txt")
with open("comsolheight3_roughmesh.txt","r") as f:
# with open("comsolheight.txt","r") as f:
    comsolheightdata = f.readlines()
ind_of_t = 0
ind_of_h = 1

def getline(line):
    templist = []
    temp = line.split(" ")
    for j in range(len(temp)):
        if temp[j]!="":
            templist.append(temp[j])
    return templist



comsoltime = np.empty([len(comsolheightdata)-5])
comsolheight = np.empty([len(comsolheightdata)-5])
for i in range(len(comsolheightdata)-5):
    print(i)
    # templist = []
    # print(comsolheightdata[i])
    line= getline(comsolheightdata[i+5])
    print(line)
    comsoltime[i] = line[ind_of_t]
    comsolheight[i] = line[ind_of_h]
    
    # comsolheight[i] = comsolheightdata[2,i+5].split(" ")[2]

fntsz = 14
# print(f"{comsoltime},{comsolheight}")
plt.plot(t[:-34]/50,height[34:]/164*6.5e-2-5.2e-2)
# plt.plot(t[:-34]/60,height[34:]/288*6e-2)
plt.plot(comsoltime,comsolheight)
plt.grid()
plt.xlabel("Time [s]",size=fntsz)
plt.ylabel("Height [m]",size=fntsz)

plt.rc("legend",fontsize=fntsz)
plt.legend(["Experimental","Comsol"])#,size=16)
plt.savefig("waterheight_comp_v2.png")
plt.show()



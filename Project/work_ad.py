import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature import LAND, COASTLINE


ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Example data (replace with your data)
longitude = [0, 45, 90, 135, -135, -179]
latitude = [0, 30, 60, 80, 90, 0]



class GeoPoint:
    def __init__(self,longitude,latitude):
        self.longitude = longitude
        self.latitude = latitude

class Box:
    def __init__(self,tl,vtl,tr,vtr,bl,vbl,br,vbr):
        self.tldata = [tl,vtl]
        self.trdata = [tr,vtr]
        self.bldata = [bl,vbl]
        self.brdata = [br,vbr]
        
        
        
class Plot_Marching_squares:
    def __init__(self,box,q,color):
        self.color = color
        if (box.tldata[1] <= q):
            self.booltl = 0
        elif (box.tldata[1] > q):
            self.booltl = 1
        
        if (box.trdata[1] <= q):
            self.booltr = 0
        elif (box.trdata[1] > q):
            self.booltr = 1
            
        if (box.bldata[1] <= q):
            self.boolbl = 0
        elif (box.bldata[1] > q):
            self.boolbl = 1
        
        if (box.brdata[1] <= q):
            self.boolbr = 0
        elif (box.brdata[1] > q):
            self.boolbr = 1    
            
        case = str(self.booltl) + str(self.booltr) + str(self.boolbl) + str(self.boolbr)
        
        topmidlong = (box.tldata[0].longitude + box.trdata[0].longitude)/2
        topmidlat = (box.tldata[0].latitude + box.trdata[0].latitude)/2
        
        leftmidlong = (box.tldata[0].longitude + box.bldata[0].longitude)/2
        leftmidlat = (box.tldata[0].latitude + box.bldata[0].latitude)/2
        
        rightmidlong = (box.trdata[0].longitude + box.brdata[0].longitude)/2
        rightmidlat = (box.trdata[0].latitude + box.brdata[0].latitude)/2
        
        bottommidlong = (box.bldata[0].longitude + box.brdata[0].longitude)/2
        bottommidlat = (box.bldata[0].latitude + box.brdata[0].latitude)/2
        
        if case == "0000": 
            pass
        elif case == "0001": 
            plot_line_segment(rightmidlong, rightmidlat, bottommidlong, bottommidlat, color)
        elif case == "0010":
            plot_line_segment(leftmidlong, leftmidlat, bottommidlong, bottommidlat, color)
        elif case == "0011":
            plot_line_segment(leftmidlong, leftmidlat, rightmidlong, rightmidlat, color)
        elif case == "0100":
            plot_line_segment(topmidlong, topmidlat, rightmidlong, rightmidlat, color)
        elif case == "0101":
            plot_line_segment(topmidlong, topmidlat, bottommidlong ,bottommidlat, color)
        elif case == "0110":
            # plot_line_segment(topmidlong, topmidlat, leftmidlong, leftmidlat)
            # plot_line_segment(bottommidlong, bottommidlat, rightmidlong, rightmidlat)
            plot_line_segment(topmidlong, topmidlat, rightmidlong, rightmidlat, color)
            plot_line_segment(bottommidlong, bottommidlat, leftmidlong, leftmidlat, color)
        elif case == "0111":
            plot_line_segment(topmidlong, topmidlat, leftmidlong, leftmidlat, color)
        elif case == "1000":
            plot_line_segment(topmidlong, topmidlat, leftmidlong, leftmidlat, color)
        elif case == "1001":
            # plot_line_segment(topmidlong, topmidlat, rightmidlong, rightmidlat)
            # plot_line_segment(bottommidlong, bottommidlat, leftmidlong, leftmidlat)
            plot_line_segment(topmidlong, topmidlat, leftmidlong, leftmidlat, color)
            plot_line_segment(bottommidlong, bottommidlat, rightmidlong, rightmidlat, color)
        elif case == "1010":
            plot_line_segment(topmidlong, topmidlat, bottommidlong ,bottommidlat, color)
        elif case == "1011":
            plot_line_segment(topmidlong, topmidlat, rightmidlong, rightmidlat, color)
        elif case == "1100":
            plot_line_segment(leftmidlong, leftmidlat, rightmidlong, rightmidlat, color)
        elif case == "1101":
            plot_line_segment(leftmidlong, leftmidlat, bottommidlong, bottommidlat, color)
        elif case == "1110":
            plot_line_segment(rightmidlong, rightmidlat, bottommidlong, bottommidlat, color)
        elif case == "1111":
            pass    
  

def plot_line_segment(x1, y1, x2, y2,clr):
    plt.plot([x1, x2], [y1, y2],
         color=clr, 
         transform=ccrs.PlateCarree(),
         )

        

fh = open("11_Jun_2015.txt")

min = -1

for line in fh:
    x = len(line.split())
    if x < min or min == -1:
        min = x

fh.close()
fh = open("11_Jun_2015.txt")



data = {}
long = []
lati = []

i = 0
for line in fh:
    y = line.split()
    
    
    if i == 0:
        # long = y[:min]]
        it1 = 0
        while (it1 < min):
            if y[it1][-1] == "E":
                long.append(float(y[it1][:-1]))
            elif y[it1][-1] == "W":
                long.append(360-float(y[it1][:-1]))
            it1 = it1 + 1
                
            
        
    else:    
        
        lat = y[0]
        
        if lat[-1] == "N":
            lat = float(lat[:-1])
            lati.append(lat)
            
        elif lat[-1] == "S":
            lat = -float(lat[:-1])
            lati.append(lat)
            
        
        j=1
        
        data[lat] = {}
        
        while (j<min):
            data[lat][long[j-1]] = float(y[j])
            j=j+1
            
        # print(len(y))    
        data[lat][long[min-1]] = -999 #float(y[min])    
        
        #lati.append(lat)    
        
    
    i=i+1   

print(long)
fh.close()


# for elem in data:
#     print(elem)
#     print()



cl = ["blue","green","red"]


val = [0.03, 0.15 ,0.3]

it_f = 0

while (it_f<len(val)):
    it2 = 8
    while(it2<len(lati)):
        it3 = 8
        while (it3<min):
            # print("Hi")
            ptl = GeoPoint(long[it3-8],lati[it2-8])
            ptr = GeoPoint(long[it3], lati[it2-8])
            pbl = GeoPoint(long[it3-8], lati[it2])
            pbr = GeoPoint(long[it3], lati[it2])
        
            vtl = data[lati[it2-8]][long[it3-8]]
            vtr = data[lati[it2-8]][long[it3]]
            vbl = data[lati[it2]][long[it3-8]]
            vbr = data[lati[it2]][long[it3]]
        
            obj=Box(ptl,vtl,ptr,vtr,pbl,vbl,pbr,vbr)
            plotter = Plot_Marching_squares(obj,val[it_f],cl[it_f])
        
            it3 = it3 + 8
        it2 = it2 + 8
    print(it_f)    
    it_f = it_f + 1    
    
    

plt.legend()
# Plot your data
ax.scatter(longitude, latitude, label='Data Points', color='red', marker='o')

# Customize appearance, add labels, titles, legends, etc.

# Display the map
plt.show()
    
        
        
# Written by Jashwanth Kadaru
# Roll number: IMT2021095
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# ocean data from the .txt file as a grid. (replace with your own data)
# ocean_data = np.random.rand(180, 360)  
ocean_data_file_path = './21_Jun_2015.txt'
plot_name = 'Color Map ' + '21_Jun_2015'

file = open(ocean_data_file_path, 'r')
rows = 0
cols = 0


for line in file:
    rows+=1
    if(cols==0 and rows==2):
        words = line.split()
        for word in words:
            cols+=1

print(rows, cols)

file.close()


file = open(ocean_data_file_path, 'r')
latitudes_list = []
longitudes_list = []

i=0
for line in file:
    if(i==0):
        for word in line.split():
            longitudes_list.append(word)
    else:
        j=0
        for word in line.split():
            if(j==0):
                latitudes_list.append(word)
                j+=1
    i+=1
    
file.close()



print('longitudes_list:',longitudes_list)
print('latitudes_list:',latitudes_list)

file = open(ocean_data_file_path, 'r')
ocean_data = []

i=0
for line in file:
    if(i==0):
        pass
    else:
        j=0
        line_data = []
        for word in line.split():
            if(j==0):
                j+=1
            else:
                if(word[-1] not in ['1', '2', '3','4','5', '6', '7','8','9', '0']):
                    line_data.append(-2)
                elif(word[0]=='-'):
                    line_data.append(-2)
                else:
                    line_data.append(float(word))
                j+=1
        ocean_data.append(line_data)
    i+=1
    
file.close()
print(ocean_data.__len__())
print(ocean_data[650])

max_len = 0
for line_data in ocean_data:
    line = list(line_data)
    if(max_len < line.__len__()):
        max_len = line.__len__()

index = 0
for line_data in ocean_data:
    line = list(line_data)
    if(line.__len__() < max_len):
        add = max_len - line.__len__()
        while(add):
            line.append(-2)
            add-=1
        ocean_data[index] = line
    index+=1

print(ocean_data.__len__())
print(ocean_data[0].__len__())
# print(ocean_data[650])

count = 0
for line_data in ocean_data:
    line = list(line_data)
    if(max_len > line.__len__()):
        count+=1

print('count', count)

min_datum = 1000000
max_datum = -100000
for line_data in ocean_data:
    for datum in line_data:
        if(min_datum>datum):
            min_datum = datum
        elif(max_datum<datum):
            max_datum = datum

print('min, max:', min_datum, max_datum)

new_ocean_data = []
for line_data in ocean_data:
    line = list(line_data)
    new_ocean_data.append(line)

new_ocean_data.reverse()

i=0
for line in new_ocean_data: 
    j=0
    for word in line:
        if(new_ocean_data[i][j]==-2):
            pass
        else:
            new_ocean_data[i][j] = (new_ocean_data[i][j]-min_datum)/(max_datum-min_datum)
        j+=1
    i+=1    

ocean_data_np = np.array(new_ocean_data)

# Define your custom colormap
colors = [
    (0.0, 'blue'),  # For null data (e.g., -2)
    (0.07, 'skyblue'),  # For null data (e.g., -2)
    (0.14, 'white'),       # For values less than 0
    (0.21, 'yellow'),       # 
    (0.28, 'orange'),      # For values in the range (0, 30)
    (0.35, 'red'),         # For values greater than or equal to 30
    (1, 'red'),        # For values greater than or equal to 30
]

custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_colormap', colors)

# Set colormap (you can choose a different colormap)
# viridis, cividis, jet, ocean, inferno, plasma
cmap = plt.get_cmap('viridis')

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)})


# Define the extent of your data
# lon_min, lon_max, lat_min, lat_max = -90, 180, -90, 90

# Define the resolution (0.25 degrees) for both latitude and longitude
resolution = 0.25

# Calculate latitude and longitude grids based on the resolution
latitudes = np.linspace(90 - 0.5 * resolution, -90 + 0.5 * resolution, ocean_data_np.shape[0])
longitudes = np.linspace(-180 + 0.5 * resolution, 180 - 0.5 * resolution, ocean_data_np.shape[1])

# Define the extent of your data
lon_min, lon_max, lat_min, lat_max = -180, 180, -90, 90

# Plot ocean data (Logarithmic color mapping)
# im = ax.imshow(new_ocean_data, extent=(lon_min, lon_max, lat_min, lat_max), cmap=cmap, norm=mcolors.LogNorm(0.05, 0.1), transform=ccrs.PlateCarree(central_longitude=180))

# Plot ocean data (Discrete color mapping)
# bounds = [0, 0.01, 0.02, 0.03, 0.04, 0.05, .07, .08]
# num_c = len(bounds)
# cmap = mpl.colormaps['viridis']._resample(num_c)
# norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
# im = ax.imshow(ocean_data, extent=(lon_min, lon_max, lat_min, lat_max), cmap=cmap, norm=norm, transform=ccrs.PlateCarree())


# Plot the data using pcolormesh with specified latitudes and longitudes
im = ax.pcolormesh(longitudes, latitudes, ocean_data_np, cmap=cmap, vmin=0.0755, vmax=0.0855)

# Overlay world map
ax.add_feature(cfeature.COASTLINE, linewidth=2, edgecolor='black', zorder=2)
ax.add_feature(cfeature.BORDERS, linewidth=1, edgecolor='black', zorder=1)
ax.add_feature(cfeature.LAND, facecolor='white', zorder=1)

# Customize the color mapping as needed
cbar = plt.colorbar(im, ax=ax, orientation='vertical', fraction=0.025, pad=0.05)
cbar.set_label('Attribute Value (scaled to 0 - 1 range)')

# Set plot title
ax.set_title( plot_name )

# Show the plot
plt.show()


from PIL import Image
import os
import numpy as np
import pandas as pd

# specify the folder that contains the TIF images
image_folder = "path/to/folder"
image_files = [f for f in os.listdir(image_folder) if f.endswith('.tif')]

# specify the x,y pixel coordinates of the pixel that you want to extract
x_coord = 10
y_coord = 20

data = []
for file in image_files:
    # Open the TIF file
    img = Image.open(os.path.join(image_folder, file))
    # Get the pixel value
    pixel = img.getpixel((x_coord, y_coord))
    # Extract date from file name without the .tif extension
    date = os.path.splitext(file)[0]
    # Append the data to a list
    data.append([date, pixel])

# Create the dataframe
df = pd.DataFrame(data, columns=['date', 'pixel_value'])

# Save the dataframe to a CSV file
df.to_csv('image_timeseries.csv', index=False)

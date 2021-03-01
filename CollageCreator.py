# Task - Create a collage using the frames of Video

# IMPORT PACKAGES INCLUDING os,skimage,numpy,PIL and matplotlib
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image

# Create function CollageCreate with address of Folder as the parameter
def CollageCreate(AddressofFolder):
  dir=AddressofFolder
  l1=[]
  for files in os.listdir(dir):
    # For each image in the folder
    source = os.path.join(dir,files)

    image = io.imread(source)
    # Create Histogram for each Colour and Total Intensity
    plt.hist(image.ravel(), bins = 256, color = 'orange', )
    plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    plt.xlabel('Intensity Value')
    plt.ylabel('Count')
    plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.show()
    # For each image calculate colour intensity of each colour, i.e , Red , Green and Blue
    p1=sum(image[:,:,0].ravel())
    p2=sum(image[:,:,1].ravel())
    p3=sum(image[:,:,2].ravel())
    # Calculate total score using Totalscore = (RedIntensity+GreenIntensity+BlueIntensity)/3
    Totalscore=(p1+p2+p3)/3
    l1.append(Totalscore)
  # In a dictionary we store the values of each photo with respect to intensity
  # of each colour that helps us determine the position of each image in the Collage
  dicts = {}
  img_list = os.listdir(dir)
  dicts=dict(zip(img_list,l1))

  l2=[]
  sort_orders=sorted(dicts.items(),key=lambda x:x[1],reverse=True)
  for i in sort_orders:
    print(i[0],i[1])
    l2.append(i[0])

  # Create Template or Blank image to create a collage on
  result = Image.new("RGB", (800, 800))
  # Place each image in the collage with respect to the sorted intensity of Images
  for index, file in enumerate(l2):
    sorted_img_path = os.path.join(dir,file)
    img=Image.open(sorted_img_path)
    img.thumbnail((400, 400), Image.ANTIALIAS)
    x = index // 2 * 200
    y = index % 2 * 400
    w, h = img.size
    # Display position and size of each image and its position
    print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
    result.paste(img, (x, y, x + w, y + h))
  # Save the result in the directory
  result.save(os.path.expanduser('collageResult.jpg'))

# Import the directory
path=os.getcwd()
dir=os.path.join(path,'pics')
# Create collage using the function CollageCreate(AddressFolder)
CollageCreate(dir)

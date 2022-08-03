import struct
import os
import sys
import math
import random
import string
from PIL import Image #pip install pillow
BLOCKSIZE=16 #bytes

def random_string():
  return ''.join(random.choice(string.ascii_letters) for i in range(20))

def main(filename, width=0, offset=0):
  if not os.path.exists(filename) and not os.path.isfile(filename):
    print("File not found.",file=sys.stderr)
    exit()
  filesize=os.path.getsize(filename)
  print("Filesize: %d" % filesize)
  if width==0 or width=="0":
    width=(filesize /BLOCKSIZE) **.5
    if math.floor(width)!=width:
      width=math.ceil(width)
  else:
    width = int(width)
  height = math.ceil((filesize/BLOCKSIZE) / width)
  print("Image Size: %d x %d" % (width, height))

  #Step1) Analyze the data and find frequent blocks
  data={}
  with open(filename,"rb") as f:
    bytes = f.read(16)
    while bytes:
      num=bytes.hex()
      if not num in data:
        data[num]=1
      else:
        data[num]+=1
      bytes = f.read(16)
  sorted_data = sorted(data.items(), key=lambda kv: -kv[1])
  #Step2) Assign colors to frequent blocks
  try:
    colors={}
    colors[sorted_data[0][0]]=(255,255,255)   #white
    colors[sorted_data[1][0]]=(0,0,0)         #black
    colors[sorted_data[2][0]]=(128,0,0)       #dark red
    colors[sorted_data[3][0]]=(0,128,0)       #dark blue
    colors[sorted_data[4][0]]=(0,0,128)       #dark green
    colors[sorted_data[5][0]]=(0,128,128)     #deep aqua
    colors[sorted_data[6][0]]=(128,0,128)     #dark magenta
    colors[sorted_data[7][0]]=(128,128,0)     #swampgreen
    colors[sorted_data[8][0]]=(255,0,0)       #red
    colors[sorted_data[9][0]]=(0,255,0)       #blue
    colors[sorted_data[10][0]]=(0,0,255)      #green
  except:
    #in case the block patterns has less than 11 patterns
    pass
  
  #Step3) Create the image
  i=0
  x=0
  y=0
  img = Image.new( 'RGB', (width,height), "white")
  pixels = img.load()
  with open(filename,"rb") as f:
    bytes = f.read(16)
    while bytes:

      if bytes.hex() in colors.keys():
        pixels[x,y]=colors[bytes.hex()]
      else:
        pixels[x,y]=(128,128,128)
      i=i+1
      x=(i + int(offset)) % width
      y=math.floor(i/width)
      bytes = f.read(16)

  img=img.resize((width, height//8), Image.Resampling.NEAREST)
  # img=img.resize((width, height//8), Image.NEAREST)  <- for old pillow library

  filename=random_string() + ".png"
  img.save(filename)
  img.show()
  print(filename)

if __name__ == '__main__':
  if len(sys.argv) > 3:
    main(sys.argv[1], sys.argv[2], sys.argv[3])
  elif len(sys.argv) > 2:
    main(sys.argv[1], sys.argv[2])
  elif len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    print("usage: aes_ecb.py <filename> [width] [offset n blocks]")

  
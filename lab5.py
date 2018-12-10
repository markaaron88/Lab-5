#Mark Mariscal
#11/6/2018
#Lab5
def get_pic():
 return makePicture(pickAFile())
#Problem1
sourceWidth = getWidth( source )
  sourceHeight = getHeight( source )
  targetWidth = getWidth( target )
  targetHeight = getHeight( target )
  
  for x in range( 0, sourceWidth ):
    for y in range( 0, sourceHeight ):
      pixel = getPixel( source, x, y )
      color = getColor( pixel )
      
      if x + targetX < targetWidth - 1 and y + targetY < targetHeight - 1:      
        setColor( getPixel( target, x + targetX, y + targetY ), color )
        
  return target


  
def makecollage():
  target = makeEmptyPicture( 950, 1300, white)
  picture1 = get_pic()
  picture2 = get_pic()
  picture3 = get_pic()
  picture4 = get_pic()
  picture5 = get_pic()
  picture6 = get_pic()
  picture7 = get_pic()
  picture8 = get_pic()
  
  target=pyCopy(roseCoveredGlasses(picture1),target, 400, 350)
  
  target=pyCopy(BnW(picture2),target, 150, 150)
  
  target=pyCopy(makeNegative(picture3),target, 350, 850)
  
  target=pyCopy(noBlue(picture4),target, 650, 450)
  
  target=pyCopy(topbottom(picture5),target, 150, 450)
  
  target=pyCopy(copyMirror(picture6),target, 255, 650)
  
  target=pyCopy(rotatePic(picture7),target, 700, 200)
  
  target=pyCopy(picture8,target, 500, 800)
    
  show(target)
    
def roseCoveredGlasses(picture):
 pixels = getPixels(picture)
 for p in pixels:
  b = getBlue(p)
  g = getGreen(p)
  g *= .82
  b *= .863
  setGreen(p, g)
  setBlue(p, b)
 return picture  

def BnW(picture):
 pixels = getPixels(picture)
 for p in pixels:
  b = getBlue(p)
  g = getGreen(p)
  r = getRed(p)
  avg = (b + g + r)/3  
  setRed(p, avg)
  setGreen(p, avg)
  setBlue(p, avg)
 return picture
   
def makeNegative(picture):
  pixels = getPixels(picture)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    setRed(p, 255 - r)
    setGreen(p, 255 - g)
    setBlue(p, 255 - b)
  return picture   

def noBlue(picture):
  pixels = getPixels(picture)
  for p in pixels:
    setBlue(p, 0)
  return picture     

def topbottom(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width):
    for y in range(0, height/2):
      color=getColor(getPixel(picture, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,x, height-1-y),color)
  return canvas         

def copyMirror(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(width,height)
  for x in range(0, width/2):
    for y in range(0,height):
      color=getColor(getPixel(picture, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,width-x-1,y),color)
  return canvas  

def rotatePic(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(height, width)
  for x in range(0, width):
    for y in range(0, height):
      setColor(getPixel(canvas, y, getHeight(canvas)-x-1), getColor(getPixel(picture, x, y)))
  return canvas 
    
    
    
 
#Warmup
def makelarger():
  pic = get_pic()
  changedPic = makeEmptyPicture(getWidth(pic) * 2, getHeight(pic) * 2)
  xPad = getWidth(pic) / 2
  yPad = getHeight(pic) / 2
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      readPix = getPixel(pic, x, y)
      readColor = getColor(readPix)
      writePix = getPixel(changedPic, x + xPad, y + yPad)
      setColor(writePix, readColor)
  show(changedPic)
  return changedPic      
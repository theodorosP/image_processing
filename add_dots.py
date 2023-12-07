import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

#this function adds dot in a picture
#image name is the name of the picture in the working directory
def add _dots(image_name):
	img = mpimg.imread(image_name ) 
	fig = plt.figure()
	ax = fig.add_subplot( 1,1,1) 
	sc = ax.imshow( img ) 
	xx = 100
	yy = 100
	circ = Circle((xx,yy),10, color = "black")
	ax.add_patch(circ)
	plt.savefig("dot_" + image_name)
	plt.show() 
	

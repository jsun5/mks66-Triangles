import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
	length = math.sqrt( vector[0]**2 + vector[1]**2 + vector[2]**2)
    vector = [vector[0]/length,vector[1]/length,vector[2]/length)

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross_product(a, b):
	return [a[1]*b[2] - b[1]*a[2],
			a[2]*b[0] - b[2]*a[0],
			a[0]*b[1] - b[0]*a[1]]
			
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    leg1 = [polygons[i+1][0] - polygons[i][0],
			polygons[i+1][1] - polygons[i][1],
			polygons[i+1][2] - polygons[i][2]]
	leg2 = [polygons[i+2][0] - polygons[i][0],
			polygons[i+2][1] - polygons[i][1],
			polygons[i+2][2] - polygons[i][2]]
	return cross_product(leg1,leg2)

import numpy as np
from sklearn import linear_model

a = np.zeros(3) #array mit 3 nullen
print(a.shape)

b = np.array([1,5,6]) #array
print(b[0])

c_list = [3,5,7,9] #liste
c_array = np.array(c_list) #array bekommt liste uebergeben
print(c_array[2])

e_list = [[1,2,3], [4,5,6]] #zwei dimensionale liste
e_array = np.array(e_list) #zweidimensionales array
print(e_array[1][0])

print(e_array < 3) #testet welche indize kleiner als 3 sind
print(e_array[e_array<3]) # gibt genau die indize aus bei denen die bedingung zutrifft

#scikitlearn ausprobiert bissl
reg = linear_model.LinearRegression()
reg.fit([[0,0], [1,1], [2,2]], [0,1,2])
LinearRegression()
reg.coef_
array([0.5, 0.5])
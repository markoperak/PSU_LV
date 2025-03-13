import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("C:\\Users\\student\\Desktop\\lv2\\mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
mpg = data[:,0]
hp = data[:, 3]
wt = data[:, 5]

filter = data[:, 1] == 6
mpg6 = data[filter, 0]

plt.scatter(mpg, hp, s=wt*30)
plt.title("Ovisnost potrosnje o konjskim snagama")
plt.xlabel("Potrosnja")
plt.ylabel("Konjske snage")
plt.grid(True)
plt.show()

print("Min, max i avg za sve aute: ")
print(np.min(mpg))
print(np.max(mpg))
print(np.mean(mpg))

print("Min, max i avg za one od 6cyl: ")
print(np.min(mpg6))
print(np.max(mpg6))
print(np.mean(mpg6))
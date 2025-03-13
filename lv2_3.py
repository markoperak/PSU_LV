import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("C:\\Users\\student\\Desktop\\lv2\\tiger.png")

svjetlija = img + 0.50
rotirana = np.rot90(img, k=-1)
zrcaljeno = np.fliplr(img)
smanjeno = img[::10, ::10]

plt.figure()
plt.imshow(svjetlija, cmap="gray")
plt.show()

plt.figure()
plt.imshow(rotirana, cmap="gray")
plt.show()

plt.figure()
plt.imshow(zrcaljeno, cmap="gray")
plt.show()

plt.figure()
plt.imshow(smanjeno, cmap="gray")
plt.show()
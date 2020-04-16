import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

L = 256
n_iterations = 100

initial_probability = .5
neighbour_template = np.ones((3,3),dtype=np.int)
neighbour_template[1,1]=0

life_map = np.random.choice(a=[False, True], size=(L, L), p=[1-initial_probability,initial_probability])

for iplot in range(n_iterations):
    print(iplot)
    plt.clf()
    plt.imshow(life_map)
    plt.savefig(f"pics/{iplot:06}.png",dpi=250)
    neighbour_map = scipy.signal.convolve2d(life_map, neighbour_template, mode='same',boundary='wrap')
    life_map = neighbour_map==3 | (neighbour_map==2 & life_map) 

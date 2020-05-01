import numpy as np
import subprocess
import matplotlib.pyplot # required for PIL images, apparently?
import PIL


def count_neighbours_roll(bool_map): # about 6x faster than scipy convolve2d
    life_map = bool_map.astype(np.int)
    neighbours = np.roll(life_map,1,axis=0)
    neighbours += np.roll(life_map,-1,axis=0)
    neighbours += np.roll(life_map,1,axis=1)
    neighbours += np.roll(life_map,-1,axis=1)
    neighbours += np.roll(life_map,(-1,-1),axis=(0,1))
    neighbours += np.roll(life_map,(1,-1),axis=(0,1))
    neighbours += np.roll(life_map,(-1,1),axis=(0,1))
    neighbours += np.roll(life_map,(1,1),axis=(0,1))
    return neighbours

def game_of_life():
    L = 1024
    n_iterations = 100

    initial_probability = .3

    life_map = np.random.random((L,L))<=initial_probability

    for iplot in range(n_iterations):
        print(iplot)
        PIL.Image.fromarray(life_map).save(f"pics/{iplot:06}.png")
        neighbour_map = count_neighbours_roll(life_map)
        life_map = neighbour_map==3 | (neighbour_map==2 & life_map) 

def animate_pics():
    subprocess.call('ffmpeg -y -r 20 -i pics/%06d.png -c:v mpeg4 -q:v 1 game_of_life.mp4', shell=True)    

if __name__=="__main__":
    game_of_life()
    animate_pics()

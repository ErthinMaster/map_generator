
from platform import platform
import random, numpy as np
import string
from datetime import datetime as dt



def generate_platform_string(platform, size):
    abc = list(string.ascii_uppercase)	
    platform_string = " ,"
    platform_string += ",".join([abc[i] for i in range(0, size[1])])
    platform_string += "\n"
    for i in range(0, size[0]):
        platform_string += f"{abc[i]},"
        platform_string += ",".join([f"{platform[i,j]}" for j in range(0, size[1])])    
        platform_string += "\n"
    
    return platform_string

def save_platform(name, platform_string):
    with open(f"{name}.csv", "w") as f: f.write(platform_string)

def generate_platform(name, size, nb_pos, index_offset, current_pos=[], current_prob=90, dec_prob=10):
    if not current_pos:
        current_pos = [(random.randint(0,size[0]-1), random.randint(0,size[1]-1)) for i in range(0, nb_pos)]

    platform = np.zeros(size, dtype=np.uint16)
    _rec_generate_platform(platform, current_pos, index_offset, current_prob, dec_prob)
    platform_string = generate_platform_string(platform, size)
    save_platform(name, platform_string)

def _rec_generate_platform(platform, current_pos, index_offset, current_prob, dec_prob):
    if not current_pos: return
    for pos in current_pos: platform[pos[0], pos[1]] = current_prob
    new_pos = []
    for pos in current_pos: check_pos_around(platform, pos, new_pos, index_offset)
    _rec_generate_platform(platform, new_pos, index_offset, current_prob-dec_prob if current_prob-dec_prob > 0 else current_prob , dec_prob)

def check_pos_around(platform, pos, new_pos, index_offset):
    shape = platform.shape
    for index in index_offset:
        
        x = pos[1]+index[1]
        y = pos[0]+index[0]
        if x < 0 or x >= shape[1]: continue
        if y < 0 or y >= shape[0]: continue
        if platform[y,x] != 0: continue
        new_pos.append((y,x))

if __name__ == '__main__':
    index_offset_1 = [
        (-1,-1), (-1, 0), (-1, 1),
        (0,-1),  (0,1),
        (1,-1),  (1,0),   (1,1)
    ]
    index_offset_2 = [
                    (-1,0),    
        (0,-1),                 (0,1),
                    (1,0)
    ]
    index_offset_3 = [
        (-2,-1),    
        (-1,-1),   (-1,-0),    
                                (0,1),
                    (1,0),      (1,1),
                                (2,1),      (2,2)
    ]
    index_offset_4 = [
        (-1,-1),   (-1, 1),
        (0,-1),    (0,1),
        (1,-1),    (1,1)
    ]

    index_offset_5 = [
                    (-1,-1),   (-1, 1),      (-1, 2),
            
        (1,-2),      (1,-1),    (1,1)
    ]

    index_offset_6 = [
                    (-2,0),
        (-1,-1),    (-1,0),
        (0,-1),                 (0,1),
                    (1,0),      (1,1),      (1,2)
    ]

    t = dt.now()            
    day = f'{t.strftime("%Y_%m_%d")}_{t.strftime("%H%M%S")}'
    size = (9,9)
    # generate_platform(f"Lapin_{day}",   size, 1, index_offset_1, current_pos=[(4,4)], current_prob=90, dec_prob=15)
    # generate_platform(f"Bouc_{day}",    size, 1, index_offset_2, current_pos=[(4,4)], current_prob=64, dec_prob=16)
    # generate_platform(f"Renard_{day}",  size, 1, index_offset_3, current_pos=[(4,4)], current_prob=82, dec_prob=8)
    # generate_platform(f"Sanglier_{day}",size, 1, index_offset_4, current_pos=[(4,4)], current_prob=76, dec_prob=12)
    generate_platform(f"Cerf_{day}",    size, 1, index_offset_5, current_pos=[(4,4)], current_prob=90, dec_prob=20)
    # generate_platform(f"Ours_{day}",    size, 1, index_offset_6, current_pos=[(4,4)], current_prob=100,dec_prob=25)

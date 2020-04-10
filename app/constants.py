'''Midi velocity to dynamics notation dictionary'''
dynamicsDict = dict([
    (8, 'pppp'), (20, 'ppp'), (31, 'pp'), (42, 'p'), (53, 'mp'), (64, 'mf'), (80, 'f'), (96, 'ff'), (112, 'fff'), (127, 'ffff')
])
#

dynamics_lst = [8, 20, 31, 42, 53, 64, 80, 96, 112, 127]
#


'''Midi key number to piano key number dictionary'''
midikeyDict = dict([
    (108, 88), (107, 87), (106, 86), (105, 85), (104, 84), (103, 83), (102, 82), (101, 81), (100, 80), (99, 79), (98, 78), (97, 77), (96, 76), (95, 75),
    (94, 74), (93, 73), (92, 72), (91, 71), (90, 70), (89, 69), (88, 68), (87, 67), (86, 66), (85, 65), (84, 64), (83, 63), (82, 62), (81, 61), (80, 60),
    (79, 59), (78, 58), (77, 57), (76, 56), (75, 55), (74, 54), (73, 53), (72, 52), (71, 51), (70, 50), (69, 49), (68, 48), (67, 47), (66, 46), (65, 45),
    (64, 44), (63, 43), (62, 42), (61, 41), (60, 40), (59, 39), (58, 38), (57, 37), (56, 36), (55, 35), (54, 34), (53, 33), (52, 32), (51, 31), (50, 30),
    (49, 29), (48, 28), (47, 27), (46, 26), (45, 25), (44, 24), (43, 23), (42, 22), (41, 21), (40, 20), (39, 19), (38, 18), (37, 17), (36, 16), (35, 15),
    (34, 14), (33, 13), (32, 12), (31, 11), (30, 10), (29, 9), (28, 8), (27, 7), (26, 6), (25, 5), (24, 4), (23, 3), (22, 2), (21, 1)
])
#

def midi_vel_to_dynamics(velocity, format, offset):
    '''
    Convert the midi velocity to standard English notation, either short or long.
    params:
        velocity:   int     between 1 and 127
        format:     str     'short' or 'long'
        offset:     float   shifts the dynamics up or down -- multiplied by the velocity-dynamics thresholds
    '''
    if format == 'short':
        dynamic_str = 0
    else:
        dynamic_str = 1

    # velocity-dynamics thresholds
    if velocity
        8, 'pppp'), (20, 'ppp'), (31, 'pp'), (42, 'p'), (53, 'mp'), (64, 'mf'), (80, 'f'), (96, 'ff'), (112, 'fff'), (
    127, 'ffff')
    ])


    dynamics_description =  {ppp':  'extremely soft',
                            'pp':   'very soft',
                            'p':    'soft',
                            'mp':   'moderately soft',
                            'mf':   'moderately loud',
                            'f':    'loud',
                            'ff':   'very loud',
                            'fff':  'extremely loud'}


def dynamics_color(dynamic_term, palette):
    '''
    Color codes the dynamics in a few different ways
    parameters:
        palette:    str 'light' or 'dark'
    '''
    default_color_scheme =
    if palette:
        try:
            palette = palette
        except:
            palette = default_color_scheme
            print('palette not found, using default')
    else:
        palette = default_color_scheme
    # if dynamics == 'pp':
    #     c.itemconfig(find_rect_id, fill='#71C7E7')
    # elif dynamics == 'p':
    #     c.itemconfig(find_rect_id, fill='#009FDA')
    # elif dynamics == 'mf':
    #     c.itemconfig(find_rect_id, fill='#A54499')
    # elif dynamics == 'f':
    #     c.itemconfig(find_rect_id, fill='#FD663F')
    # elif dynamics == 'ff':
    #     c.itemconfig(find_rect_id, fill='#FD2D26')
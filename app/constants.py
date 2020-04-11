'''Midi velocity to dynamics notation dictionary'''
dynamicsDict = dict([
    (8, 'pppp'), (20, 'ppp'), (31, 'pp'), (42, 'p'), (53, 'mp'), (64, 'mf'), (80, 'f'), (96, 'ff'), (112, 'fff'), (127, 'ffff')
])
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

def closest_dynamics(velocity):
    import numpy as np
    # Calculating closest dynamics variable from velocity integer
    lst = [8, 20, 31, 42, 53, 64, 80, 96, 112, 127]
    lst = np.asarray(lst)
    idx = (np.abs(lst - velocity)).argmin()
    return lst[idx]


def midi_dynamics(velocity):
    '''
    Convert the midi velocity to standard English notation, either short or long.
    params      velocity:   int     between 1 and 127
    returns     [dynamics_name, dynamics_description]
    '''
    dynamics_name = dict([(8, 'pppp'),
                     (20, 'ppp'),
                     (31, 'pp'),
                     (42, 'p'),
                     (53, 'mp'),
                     (64, 'mf'),
                     (80, 'f'),
                     (96, 'ff'),
                     (112, 'fff'),
                     (127, 'ffff')])

    dynamics_desc = {'ppp':  'extremely soft',
                         'pp':   'very soft',
                         'p':    'soft',
                        'mp':   'moderately soft',
                        'mf':   'moderately loud',
                        'f':    'loud',
                        'ff':   'very loud',
                        'fff':  'extremely loud'}

    closest_x = closest_dynamics(velocity)
    dname = dynamics_name[closest_x]
    # ddesc = dynamics_desc[dname]
    # return [str(dname), str(ddesc)]
    return dname

def dynamics_color(velocity):
    '''
    Color codes the dynamics
    parameters:
        velocity:    int    midi velocity
    '''
    if 0   <= velocity < 8:    color = '#0E0050'
    if 8   <= velocity < 11:  color = '#0E0066'
    if 11  <= velocity < 17:   color = '#14056B'
    if 17  <= velocity < 20:   color = '#1B0B70'
    if 20  <= velocity < 22:   color = '#221175'
    if 22  <= velocity < 28:   color = '#29167B'
    if 28  <= velocity < 31:   color = '#2F1C80'
    if 31  <= velocity < 33:   color = '#362285'
    if 33  <= velocity < 39:   color = '#3D278A'
    if 39  <= velocity < 42:   color = '#442D90'
    if 42  <= velocity < 44:   color = '#4A3395'
    if 44  <= velocity < 50:   color = '#51389A'
    if 50  <= velocity < 53:   color = '#583E9F'
    if 53  <= velocity < 55:   color = '#5F44A5'
    if 55  <= velocity < 61:   color = '#6E44A2'
    if 61  <= velocity < 64:   color = '#7D449F'
    if 64  <= velocity < 68:   color = '#8D449D'
    if 68  <= velocity < 76:   color = '#B34F7D'
    if 76  <= velocity < 80:   color = '#D95A5E'
    if 80  <= velocity < 84:   color = '#FF663F'
    if 84  <= velocity < 92:   color = '#FF5336'
    if 92  <= velocity < 96:   color = '#FF402D'
    if 96  <= velocity < 100:  color = '#FF2D25'
    if 100 <= velocity < 108:  color = '#FF4544'
    if 108 <= velocity < 112:  color = '#FF5D63'
    if 112 <= velocity < 115:  color = '#FF7582'
    if 115 <= velocity < 123:  color = '#FF939A'
    if 123 <= velocity < 127:  color = '#FFB1B3'
    if 127 <= velocity:        color = '#FFD0CC'

    return color
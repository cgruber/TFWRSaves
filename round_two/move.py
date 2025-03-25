from globals import world_size

def here():
    return (get_pos_x(), get_pos_y())

def move_diff(offset_x, offset_y):
    offset_x = offset_x % world_size
    offset_y = offset_y % world_size
    #quick_print("Abs", abs(offset_x))
    if abs(offset_x) > world_size/2:
        offset_x += -1 * world_size
    if abs(offset_y) > world_size/2:
        offset_y += -1 * world_size
    #quick_print("Moving offsets: ", offset_x, offset_y)
    while offset_x != 0:
        if (offset_x < 0):
            move(West)
            offset_x += 1
        else:
            move(East)
            offset_x -= 1
    while offset_y != 0:
        if (offset_y < 0):
            move(South)
            offset_y += 1
        else:
            move(North)       
            offset_y -= 1
    
def move_to(newx, newy):
    offset_x = newx - get_pos_x()
    offset_y = newy - get_pos_y()
    move_diff(offset_x, offset_y)

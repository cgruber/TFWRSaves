def move_to(x, y):
  #print("Moving to", x, y)
  while get_pos_x() > x:
    move(West)
  while get_pos_x() < x:
    move(East)
  while get_pos_y() > y:
    move(South)
  while get_pos_y() < y:
    move(North)

def move_to_coord(coord):
  x, y = coord
  move_to(x, y)
def right(direction):
  right_idx = {
    North: East,
    East: South,
    South: West,
    West: North,
  }  
  return right_idx[direction]
    
def left(direction):   
  left_idx = {
    North: West,
    East: North,
    South: East,
    West: South,
  }
  return left_idx[direction]

def opposite(direction):
  opposite_idx = {
    North: South,
    East: West,
    South: North,
    West: East,
  }
  return opposite_idx[direction]
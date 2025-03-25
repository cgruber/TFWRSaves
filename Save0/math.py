def here():
  return (get_pos_x(), get_pos_y())

def flat_here():
  return flatten_coord(here())

def square(num):
  return num * num

def plot_number():
  return flat_coord(
  get_pos_x(), 
  get_pos_y()
)
  
def flat_coord(x, y):
  return x * get_world_size() + y

def flatten_coord(pair):
  x, y = pair
  return flat_coord(x, y)

def edge(a, b):
  return (
    flatten_coord(a),
    flatten_coord(b),
  )
  
def reverse_edge(edge):
  a, b = edge
  return (b, a)

def plots():
  return square(get_world_size())
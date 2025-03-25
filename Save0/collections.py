def is_empty(list):
  return len(list) == 0

def peek(list):
  if is_empty(list):
    return None
  else:
    return list[len(list)-1]

def new_set():
  set = { 0 }
  set.remove(0)
  return set

def set_pop(set):
  for item in set:
    set.remove(item)
    return item # first one
  return None # no items to pop

def max_key(map):
  biggest = None
  for key in map:
    if biggest == None:
      biggest = key
    else:
      biggest = max(biggest, key)
  return biggest

def sort_set(set, forward):
  return sort_list(to_list(set), forward)

def sort_list(list, forward):
  if list == None or len(list) <= 1:
    return list
  swaps = True
  while swaps:
    swaps = False # reset
    for i in range(len(list) - 1):
      if forward:
        if list[i] > list[i+1]:
          swaps = swap(list, i, i+1)
        if list[i] < list[i+1]:
          swaps = swap(list, i, i+1)
  return list
  
def swap_elements(list, i, j):
  elem_i = list[i]
  list[i] = list[j]
  list[j] = elem_i
  return True

def reverse_list(list):
  if list != None and len(list) > 1:
    i = 0
    length = len(list)
    limit = length / 2
    while i < limit:
      swap_elements(list, i, length - 1 - i)
      i = i + 1
  return list # in-place, but return for flow

def new_list_from(list):
  new_list = []
  if list != None:
   for i in range(len(list)):
    new_list.append(list[i])
  return new_list
              
def to_list(set):
  list = []
  if set != None:
    for i in set:
      list.append(i)
  return list  
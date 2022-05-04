result=[]
def flatten(lst):
  for element in lst:
    if type(element) in (list,set, tuple):
      flatten(element)
    elif type(element)==dict:
      for x in d.items():
        flatten(x)
    else:
      result.append(element)
  return result

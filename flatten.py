def flatten(lst):
  while True:
    r=0
    new_lst=[]
    for element in lst:
      if type(element) in (list,set, tuple):
        r+=1
        new_lst.extend(element)
      elif type(element)==dict:
        for x in element.items():
          new_lst.extend(x)
        r+=1
      else:
        new_lst.append(element)
    lst=new_lst
    if r==0:
      break
  return lst

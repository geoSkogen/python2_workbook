globe = 7

def outer_func(baton):
  print(baton)
  def inner_func(numb):
    globe = numb
    print(baton, "again")
  inner_func(6)

outer_func(globe)

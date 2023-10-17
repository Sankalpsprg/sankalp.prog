#EXAMPLE2:.
def add(x,**num):
       z= x+num['a']+num['b']
       print ("addition:",z)
add(3, a=5, b=2)

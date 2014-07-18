import numpy as np


#def move_zero_row(X):
#  result = []
#  for x in X:
#    if sum(x) > 0:
#      result.append(x)
#  return np.array(result)
#

def sales_matrix():
  a = []
  d = {}
  c_t = {}
  
  for line in open('sales', 'r'):
    i = line[:-1].split('\t')
    customer_id = int(i[0])
    product_id = int(i[1])
    if c_t.has_key(customer_id):
      d[c_t[customer_id]].append(product_id)
    else:
      new_entry = len(c_t)
      c_t[customer_id] = new_entry
      d[new_entry] = [product_id]

  max_customer_id = len(d)
  max_product_id = max(map(lambda x:max(d[x]),d))

  M = np.zeros([max_customer_id,max_product_id+1])
  
  for (k,v) in d.items():
    for v_each in v:
      M[k,v_each] = 1

  return M


  

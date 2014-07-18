import pickle
import numpy as np

def save_pq(p,q):
  p.tofile("p_dump")
  q.tofile("q_dump")
  save_shape(p,q)

def load_pq():
  p = np.fromfile("p_dump")
  q = np.fromfile("q_dump")
  p_shape,q_shape = load_shape()
  p = p.reshape(p_shape)
  q = q.reshape(q_shape)
  return p,q

def save_shape(p,q):
  f = open('shape','w')
  pickle.dump([p.shape,q.shape],f)

def load_shape():
  f = open('shape','r')
  x = pickle.load(f)
  return x[0],x[1]


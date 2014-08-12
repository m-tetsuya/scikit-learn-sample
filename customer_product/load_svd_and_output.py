# coding: UTF-8
# -*- coding: utf-8 -*-

import numpy as np
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

f = codecs.open('product','r','utf-8')
line = f.readline()
 
SIZE_OF_PRODUCT=288107
product_name= [""] * SIZE_OF_PRODUCT

while line:
  b = line.rstrip().split('\t')
  if len(b) > 1:
    product_name[int(b[0])] = b[1]
  line = f.readline()
  f.close

product_name_sub = product_name[-50000:]

SVD = np.load("svd.npy")
SVD_WITH_NAME = np.c_[np.array(product_name_sub).T,SVD.T]

for i in range(1,6):
  RESULT = SVD_WITH_NAME[ SVD_WITH_NAME[:,i].argsort() ]
  np.savetxt("r" + str(i),RESULT,fmt="%s")


import numpy as np
import save_data as sd
import load_from_file as load
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix

R =  load.sales_matrix()
print R
print R.shape

svd = TruncatedSVD(n_components=2)
svd.fit(R) 
print svd.components_

#sd.save_pq(nP,nQ)
#p,q = sd.load_pq()
#U = np.dot(p.T ,q)

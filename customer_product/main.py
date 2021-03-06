import numpy as np
import save_data as sd
import load_from_file as load
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix

R =  load.sales_matrix()
print R
print R.shape

R = R[-50000:][:,-50000:]
print R.shape
svd = TruncatedSVD(n_components=5)
svd.fit(R) 
np.save("svd.npy",svd.components_)


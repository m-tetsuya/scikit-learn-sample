import numpy as np
from sklearn.decomposition import TruncatedSVD

R = np.array([
        [5, 3, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [1, 0, 0, 4],
        [0, 1, 5, 4],
        ]
    )
print R

svd = TruncatedSVD(3)
X = svd.fit(R)

print X.components_


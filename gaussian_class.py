#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gaussian_class.py
#  
#  Copyright 2017 ssd <ssd@ssd>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# http://scikit-learn.org/stable/auto_examples/preprocessing/plot_robust_scaling.html#sphx-glr-auto-examples-preprocessing-plot-robust-scaling-py


import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import make_gaussian_quantiles

import numpy as np

def main(args):

	#plt.figure(figsize=(8, 8))
	#plt.title("Gaussian divided into three quantiles", fontsize='small')
	#X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3)
	#plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
	#plt.show()

	plt.figure(figsize=(8, 8))
	plt.title("Gaussian divided i", fontsize='small')
	X1, Y1 = make_gaussian_quantiles(n_features=1, n_classes=3)
	
	feat = X1[:, 0]
	print(np.min(feat), np.mean(feat), np.max(feat) )
	plt.scatter(feat, len(feat) * [1], marker='o', c=Y1)
	plt.show()

	return 0
 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

from pca.pca import pca

from pca.pca import (
    import_example,
    hotellingsT2,
    )


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.8'

# module level doc-string
__doc__ = """
pca
=====================================================================

Description
-----------
pca is a python package that performs the principal component analysis and to make insightful plots.

Examples
--------
>>> from pca import pca
>>> # Load example data
>>> X = pd.DataFrame(data=load_iris().data, columns=load_iris().feature_names, index=load_iris().target)
>>> Initialize
>>> model = pca(n_components=3)
>>> # Fit using PCA
>>> results = model.fit_transform(X)
>>> # Make plots
>>> fig, ax = model.scatter()
>>> fig, ax = model.plot()
>>> fig, ax = model.biplot()
>>> 3D plots
>>> fig, ax = model.scatter3d()
>>> fig, ax = model.biplot3d()
>>> # Normalize out PCs
>>> X_norm = pca.norm(X)

References
----------
* https://github.com/erdogant/pca
* https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html

"""

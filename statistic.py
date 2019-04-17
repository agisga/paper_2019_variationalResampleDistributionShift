import seaborn as sns
import numpy as np
import json
from  data_generator import concatenate_data_from_dir
import config
from utils import *

def counting_label():
    # load data
    y = np.load('/Users/wangyu/Documents/LMU/Fashion_mnist/mycode/results/VAE_fashion-mnist_64_62/y.npy')

    def load_dict(path):
        with open(path) as f:
            my_dict = json.load(f)
        return my_dict

    # cluster_dict = load_dict('/Users/wangyu/Documents/LMU/Fashion_mnist/mycode/results/VAE_fashion-mnist_64_62/cluster_dict.json')
    cluster_dict = load_dict(
        '/Users/wangyu/Documents/LMU/Fashion_mnist/mycode/results/VAE_fashion-mnist_64_62/pos_index_cluster.json')

    y_0 = y[cluster_dict['0']]
    y_0 = np.sum(y_0, axis=0)

    y_1 = y[cluster_dict['1']]
    y_1 = np.sum(y_1, axis=0)

    y_2 = y[cluster_dict['2']]
    y_2 = np.sum(y_2, axis=0)

    y_3 = y[cluster_dict['3']]
    y_3 = np.sum(y_3, axis=0)

    y_4 = y[cluster_dict['4']]
    y_4 = np.sum(y_4, axis=0)
    print(y_0)
    print(y_1)
    print(y_2)
    print(y_3)
    print(y_4)

def density_estimation_GMM():
    return 0

def gromov_wasserstein_distance(data_path,num_labels,num_clusters,result_path):
    import numpy as np
    import json
    import scipy as sp
    import numpy as np
    import matplotlib.pylab as pl
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    import ot

    # z: global training, cluster according to label
    z = np.load(data_path + "/L-1/z.npy")

    with open(data_path + "/L-1/cluster_dict.json") as f:
        pos_index_dict = json.load(f)

    # dict: dictionary of data which training and clustering within label
    dict = concatenate_data_from_dir(data_path, num_labels,num_clusters)

    for i in range(num_clusters):
        # Compute distance kernels, normalize them and then display
        xs = dict[str(i)]
        xt = z[pos_index_dict[str(i)]]
        n_samples = min(xs.shape[0], xt.shape[0])
        xs = xs[:n_samples]
        xt = xt[:n_samples]
        C1 = sp.spatial.distance.cdist(xs, xs)
        C2 = sp.spatial.distance.cdist(xt, xt)
        C1 /= C1.max()
        C2 /= C2.max()

        p = ot.unif(n_samples)
        q = ot.unif(n_samples)

        gw0, log0 = ot.gromov.gromov_wasserstein(
            C1, C2, p, q, 'square_loss', verbose=True, log=True)

        gw, log = ot.gromov.entropic_gromov_wasserstein(
            C1, C2, p, q, 'square_loss', epsilon=5e-4, log=True, verbose=True)

        print(" [*] cluster "+ str(i)+": ")
        print('Gromov-Wasserstein distances: ' + str(log0['gw_dist']))
        print('Entropic Gromov-Wasserstein distances: ' + str(log['gw_dist']))

        pl.figure(1, (10, 5))

        pl.subplot(1, 2, 1)
        pl.imshow(gw0, cmap='jet')
        pl.title('Gromov Wasserstein')

        pl.subplot(1, 2, 2)
        pl.imshow(gw, cmap='jet')
        pl.title('Entropic Gromov Wasserstein')
        pl.savefig(result_path + "/WD.jpg")

# compute gromov wasserstein distance on latent space clustered by vgmm
def gromov_wasserstein_distance(data_path,num_labels,num_clusters,result_path):
    import numpy as np
    import json
    import scipy as sp
    import numpy as np
    import matplotlib.pylab as pl
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    import ot

    # z: global training, cluster according to label
    z = np.load(data_path + "/L-1/z.npy")

    with open(data_path + "/L-1/cluster_dict.json") as f:
        pos_index_dict = json.load(f)

    # dict: dictionary of data which training and clustering within label
    dict = concatenate_data_from_dir(data_path, num_labels,num_clusters)

    for i in range(num_clusters):
        # Compute distance kernels, normalize them and then display
        xs = dict[str(i)]
        xt = z[pos_index_dict[str(i)]]
        n_samples = min(xs.shape[0], xt.shape[0])
        xs = xs[:n_samples]
        xt = xt[:n_samples]
        C1 = sp.spatial.distance.cdist(xs, xs)
        C2 = sp.spatial.distance.cdist(xt, xt)
        C1 /= C1.max()
        C2 /= C2.max()

        p = ot.unif(n_samples)
        q = ot.unif(n_samples)

        gw0, log0 = ot.gromov.gromov_wasserstein(
            C1, C2, p, q, 'square_loss', verbose=True, log=True)

        gw, log = ot.gromov.entropic_gromov_wasserstein(
            C1, C2, p, q, 'square_loss', epsilon=5e-4, log=True, verbose=True)

        print('Gromov-Wasserstein distances: ' + str(log0['gw_dist']))
        print('Entropic Gromov-Wasserstein distances: ' + str(log['gw_dist']))

        pl.figure(1, (10, 5))

        pl.subplot(1, 2, 1)
        pl.imshow(gw0, cmap='jet')
        pl.title('Gromov Wasserstein')

        pl.subplot(1, 2, 2)
        pl.imshow(gw, cmap='jet')
        pl.title('Entropic Gromov Wasserstein')
        pl.savefig(result_path + "/WD.jpg")

# computer gromov wasserstein distance on data fit and transformed by T_SNE
def gromov_wasserstein_distance_TSNE(data_path,num_labels,num_clusters,result_path):
    import scipy as sp
    import matplotlib.pylab as pl
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    import ot

    d_t = load_dict(data_path+"/L-1/TSNE_transformed_data_dict.json")
    d_s = load_dict(data_path+"TSNE_transformed_data_dict.json")

    for i in range(num_clusters):
        # Compute distance kernels, normalize them and then display
        xs = d_s[str(i)]
        xt = d_t[str(i)]
        n_samples = min(xs.shape[0], xt.shape[0])
        xs = xs[:n_samples]
        xt = xt[:n_samples]
        C1 = sp.spatial.distance.cdist(xs, xs)
        C2 = sp.spatial.distance.cdist(xt, xt)
        C1 /= C1.max()
        C2 /= C2.max()

        p = ot.unif(n_samples)
        q = ot.unif(n_samples)

        gw0, log0 = ot.gromov.gromov_wasserstein(
            C1, C2, p, q, 'square_loss', verbose=True, log=True)

        gw, log = ot.gromov.entropic_gromov_wasserstein(
            C1, C2, p, q, 'square_loss', epsilon=5e-4, log=True, verbose=True)

        print('Gromov-Wasserstein distances: ' + str(log0['gw_dist']))
        print('Entropic Gromov-Wasserstein distances: ' + str(log['gw_dist']))

        pl.figure(1, (10, 5))

        pl.subplot(1, 2, 1)
        pl.imshow(gw0, cmap='jet')
        pl.title('Gromov Wasserstein')

        pl.subplot(1, 2, 2)
        pl.imshow(gw, cmap='jet')
        pl.title('Entropic Gromov Wasserstein')
        pl.savefig(result_path + "/WD_TSNE.jpg")


if __name__ == '__main__':
    gromov_wasserstein_distance_TSNE(config.data_path,10,5,config.data_path)
import numpy
from models import *
from scipy.cluster import *
from scipy.spatial.distance import cdist
from collections import deque
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def get_data():
    raw_users = FacebookUser.select()
    users = list()
    data = list()
    for user in raw_users:
        users.append(user.id)
        user_data = list()
        age = get_age(user)
        friends_count = get_friends_count(user)
        groups_count = get_groups_count(user)
        user_data.append(age)
        user_data.append(friends_count)
        user_data.append(groups_count)
        data.append(user_data)
    return users, norm(data)


def get_age(user):
    result = 2017 - user.birthday
    if result == 2017:
        result = 0
    return result


def get_friends_count(user):
    friends = JoinFriends.filter(user=user).count()
    return friends


def get_groups_count(user):
    groups = JoinGroups.filter(user=user).count()
    return groups


def norm(data):
    matrix = numpy.array(data, 'f')
    len_val = len(matrix[1, :])
    for i in range(len_val):
        local_min = matrix[:, i].min()
        if local_min != 0.0:
            matrix[:, i] -= local_min
        local_max = matrix[:, i].max()
        if local_max != 0.0:
            matrix[:, i] /= local_max
    return matrix.tolist()


def kmeans_export(centroids, data, labels):
    """Export kmeans result"""
    res = [[] for i in range(len(centroids))]
    d = cdist(numpy.array(data), centroids, 'euclidean')
    for i, l in enumerate(d):
        res[l.tolist().index(l.min())].append((labels[i], data[i]))
    return res


def work():
    names, data = get_data()
    centroids = vq.kmeans(numpy.array(data), 3, iter=200)[0]
    K_res = kmeans_export(centroids, data, names)
    kmeans_draw(K_res)


def kmeans_draw(clusters):
    """Drawing kmeans clustering result"""
    colors = deque(['r', 'g', 'b', 'c', 'm', 'y', 'k'])
    fig = plt.figure()
    ax = Axes3D(fig)
    for cluster in clusters:
        color = colors.popleft()
        for name, coord in cluster:
            x, y, z = coord
            ax.plot3D([x], [y], [z], marker='o', c=color)
    ax.set_xlabel(u'Возраст')
    ax.set_ylabel(u'Количество друзей')
    ax.set_zlabel(u'Количество групп')
    plt.show()

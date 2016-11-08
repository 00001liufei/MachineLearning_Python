import numpy as np
from matplotlib import pyplot as plt
from scipy import io as spio


def KMeans():
    data = spio.loadmat("data.mat")
    X = data['X']
    K = 3   # ������
    initial_centroids = np.array([[3,3],[6,2],[8,5]])   # ��ʼ��������
    idx = findClosestCentroids(X,initial_centroids)     # �ҵ�ÿ�����������ĸ���
    
    centroids = computerCentroids(X,idx,K)  # ���¼���������
    print centroids
    
# �ҵ�ÿ�����ݾ����ĸ����������    
def findClosestCentroids(X,initial_centroids):
    m = X.shape[0]                  # ��������
    K = initial_centroids.shape[0]  # �������
    dis = np.zeros((m,K))           # �洢����ÿ����ֱ�K����ľ���
    idx = np.zeros((m,1))           # Ҫ���ص�ÿ�����������ĸ���
    
    '''����ÿ���㵽ÿ�������ĵľ���'''
    for i in range(m):
        for j in range(K):
            dis[i,j] = np.dot((X[i,:]-initial_centroids[j,:]).reshape(1,-1),(X[i,:]-initial_centroids[j,:]).reshape(-1,1))
    
    '''����disÿһ�е���Сֵ��Ӧ���кţ���Ϊ��Ӧ�����'''    
    idx = np.array(np.where(dis[0,:] == np.min(dis, axis=1)[0]))  
    for i in np.arange(1, m):
        t = np.array(np.where(dis[i,:] == np.min(dis, axis=1)[i]))
        idx = np.vstack((idx,t))
    return idx
             

# ����������
def computerCentroids(X,idx,K):
    n = X.shape[1]
    centroids = np.zeros((K,n))
    for i in range(K):
        centroids[i,:] = np.mean(X[np.array(np.where(idx==i)),:], axis=0).reshape(1,-1)   # axis=0Ϊÿһ��
    return centroids

if __name__ == "__main__":
    KMeans()
    
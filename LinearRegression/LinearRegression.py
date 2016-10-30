import numpy as np
from matplotlib import pyplot as plt


def linearRegression(alpha=0.01,num_iters=400):
    print "��������...\n"
    
    data = loadtxtAndcsv_data("data.txt",",",np.float64)  #��ȡ����
    X = data[:,0:-1]      # X��Ӧ0��������2��                  
    y = data[:,-1]        # y��Ӧ���һ��  
    m = len(y)            # �ܵ���������
    col = data.shape[1]      # data������
    
    X,mu,sigma = featureNormaliza(X)    # ��һ��
    plot_X1_X2(X)         # ��ͼ��һ�¹�һ��Ч��
    
    X = np.hstack((np.ones((m,1)),X))    # ��Xǰ��һ��1
    
    print "\nִ���ݶ��½��㷨....\n"
    
    theta = np.zeros((col,1))
    y = y.reshape(-1,1)   #��������ת��Ϊ��
    theta,J_history = gradientDescent(X, y, theta, alpha, num_iters)
    
    plotJ(J_history, num_iters)
    
    return mu,sigma,theta   #���ؾ�ֵmu,��׼��sigma,��ѧϰ�Ľ��theta
    
   
# ����txt��csv�ļ�
def loadtxtAndcsv_data(fileName,split,dataType):
    return np.loadtxt(fileName,delimiter=split,dtype=dataType)

# ����npy�ļ�
def loadnpy_data(fileName):
    return np.load(fileName)

# ��һ��feature
def featureNormaliza(X):
    X_norm = np.array(X)            #��Xת��Ϊnumpy������󣬲ſ��Խ��о��������
    #�����������
    mu = np.zeros((1,X.shape[1]))   
    sigma = np.zeros((1,X.shape[1]))
    
    mu = np.mean(X_norm,0)          # ��ÿһ�е�ƽ��ֵ��0ָ��Ϊ�У�1�����У�
    sigma = np.std(X_norm,0)        # ��ÿһ�еı�׼��
    for i in range(X.shape[1]):     # ������
        X_norm[:,i] = (X_norm[:,i]-mu[i])/sigma[i]  # ��һ��
    
    return X_norm,mu,sigma

# ����άͼ
def plot_X1_X2(X):
    plt.scatter(X[:,0],X[:,1])
    plt.show()


# �ݶ��½��㷨
def gradientDescent(X,y,theta,alpha,num_iters):
    m = len(y)      
    n = len(theta)
    
    temp = np.matrix(np.zeros((n,num_iters)))   # �ݴ�ÿ�ε��������theta��ת��Ϊ������ʽ
    
    
    J_history = np.zeros((num_iters,1)) #��¼ÿ�ε�������Ĵ���ֵ
    
    for i in range(num_iters):  # ������������    
        h = np.dot(X,theta)     # �����ڻ���matrix����ֱ�ӳ�
        temp[:,i] = theta - ((alpha/m)*(np.dot(np.transpose(X),h-y)))   #�ݶȵļ���
        theta = temp[:,i]
        J_history[i] = computerCost(X,y,theta)      #���ü�����ۺ���
        print '.',      
    return theta,J_history  

# ������ۺ���
def computerCost(X,y,theta):
    m = len(y)
    J = 0
    
    J = (np.transpose(X*theta-y))*(X*theta-y)/(2*m) #�������J
    return J

# ��ÿ�ε������۵ı仯ͼ
def plotJ(J_history,num_iters):
    x = np.arange(1,num_iters+1)
    plt.plot(x,J_history)
    plt.xlabel("num_iters")
    plt.ylabel("J")
    plt.show()

# ����linearRegression����
def testLinearRegression():
    mu,sigma,theta = linearRegression(0.01,400)
    print "\n�����thetaֵΪ��\n",theta
    print "\nԤ����Ϊ��%f"%predict(mu, sigma, theta)
    
# ����ѧϰЧ����Ԥ�⣩
def predict(mu,sigma,theta):
    result = 0
    # ע���һ��
    predict = np.array([1650,3])
    norm_predict = (predict-mu)/sigma
    final_predict = np.hstack((np.ones((1)),norm_predict))
    
    result = np.dot(final_predict,theta)    # Ԥ����
    return result
    
    
if __name__ == "__main__":
    testLinearRegression()
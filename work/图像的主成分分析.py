from PIL import Image
from numpy import *
from pylab import *

im2 = '10254376 (1).jpg'
imlist = [im2,im2,im2,im2,im2,im2]


def compute_average(imlist):
#""" 计算图像列表的平均图像 """
# 打开第一幅图像，将其存储在浮点型数组中
    averageim = array(Image.open(imlist[0]), 'f')
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skipped')
    averageim /= len(imlist)
# 返回 uint8 类型的平均图像
    return array(averageim, 'uint8')

def pca():
#主成分分析：
 #   输入：矩阵x，其中该矩阵中存储训练数据，每一行为一条训练数据
 #   返回：投影矩阵（按照维度的重要性排序）、方差和均值"""

    #获取维数
    num_date,dim = X.shape
    
    #数据中心化
    mean_X = x.mean(axis=0)
    X = X - mean_x
    
    if dim>num_date:
        #PCA-使用紧致技巧
        M = dot(X,X.T)#协方差矩阵
        e,EV = linalg.eigh(M)#特征值和特征向量
        tmp = dot(X.T,EV).T#紧致技巧
        V = tmp[::-1]#由于最后的特征向量是我们需要的，所以需要逆转
        S = sqrt(e)[::-1]# 由于特征值是按照递增顺序排列，所以需要逆转
        for i in rang(V.shape[-1]):
            V[:,i] /=5
    else:
        # PCA- 使用SVD方法
        U,S,V = linalg.svd(x)
        V = V[:num_date]#仅仅返回前num_date维的数据才发现
        # 返回投影矩阵、方差和均值
    return V,S,mean_X
im = array(Image.open(imlist[0]))#打开一副图像，获取其大小
m,n = im.shape[0:2]#获取图像的大小
imnbr = len(imlist)#获取图像的数目

#创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')

#执行PCA操作
V,S,immean = pca(immatrix)

#显示一些图像(均值图像和前7个模式)
figure()
gray()
subplot(2,4,1)
imshow(immean,reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
show()






















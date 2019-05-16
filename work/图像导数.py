from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('1.jpg').convert('L'))

imx = zeros(im.shape)

filters.sobel(im,1,imx)
# Sobel 导数滤波器
imy = zeros(im.shape)

filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

figure()
subplot(1,4,1)
imshow(im)
subplot(1,4,2)
imshow(imx)
subplot(1,4,3)
imshow(imy)
subplot(1,4,4)
imshow(magnitude)


show()

#### 1、imageHash.py
快速计算图片的hash数值

#### 2、find_similar_images.py

通过hash数值查找相似的图片

https://github.com/JohannesBuchner/imagehash.git

HEAD: 9d0855ea65a8ac35ecdc2b2c4577ca2a515a1683


#### 3、pic_hash_cmp
test.bmp 和test.png是同一张图片的不同格式，imagehash计算出来的结果是一样的。




##### 测试环境
window下 python 2.7
```
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AM
D64)] on win32
```
##### 安装
```bash
pip install ImageHash
//运行 提示 ImportError: No module named PIL
pip install image
pip install numpy
```

##### 运行imageHash
```bash
python ./imageHash D:\Picture\1.jpg
e2434227000900d002c0002000281028f85ff00671f8e17ff103f101738020fc
```


##### 运行find_similar_images
```bash
python ./find_similar_images ahash ./

./test.png   already exists as ./test.bmp
```

##### 原理
相似图片搜索原理二(phash—c++实现)
https://blog.csdn.net/u011402197/article/details/48677841

```
理论部分主要包括以下几个步骤：
<1> 图像缩放—将图像缩放到32*32大小
<2>灰度化—对32*32大小的图像进行灰度化
<3>离散余弦变换(DCT)—对32*32大小图像进行DCT
<4>计算均值—用32*32大小图片前面8*8大小图片处理并计算这64个像素的均值
<4>得到8*8图像的phash—8*8的像素值中大于均值的则用1表示，小于的用0表示，这样就得到一个64位二进制码作为该图像的phash值。
<5>计算两幅图像ahash值的汉明距离，距离越小，表明两幅图像越相似；距离越大，表明两幅图像距离越大。
这样做能够避免伽马校正或者颜色直方图调整带来的影响。
```

imagehash使用ahash计算出来的hash数值刚好为16位。

##### 缺点
无法处理识别被旋转的图片，图片大小不同识别效果不一样。

图片等比缩放计算的hash是一样的，裁剪后图片计算的hash数值部分是相同的。


##### 扩展
imagehash中的四种图像哈希方式（phash/ahash/dhash/小波hash）

https://blog.csdn.net/sinat_26917383/article/details/78582064?locationNum=8&fps=1





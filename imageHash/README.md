
#### imageHash.py
快速计算图片的hash数值

#### find_similar_images.py

通过hash数值查找相似的图片

https://github.com/JohannesBuchner/imagehash.git
HEAD: 9d0855ea65a8ac35ecdc2b2c4577ca2a515a1683


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
python ./find_similar_images ahash D:\Picture\

D:\Picture\1.jpg   already exists as D:\Picture\1 - 副本.jpg
```
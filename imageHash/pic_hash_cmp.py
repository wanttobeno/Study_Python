from PIL import Image
import imagehash
testhash = imagehash.average_hash(Image.open('test.png'))
print(testhash)
otherhash = imagehash.average_hash(Image.open('test.bmp'))
print(otherhash)
print(testhash == otherhash)
print(testhash - otherhash)

print('--------------------')
test2hash = imagehash.average_hash(Image.open('test2.png'))
print(testhash)
print(test2hash)
print(testhash == test2hash)
print(testhash - test2hash)
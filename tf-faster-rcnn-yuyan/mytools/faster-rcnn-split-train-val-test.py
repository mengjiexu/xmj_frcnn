
# coding: utf-8

# In[1]:


import random
import numpy as np
import os


# In[2]:


def getallfiles(rootdir):
    output_files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            output_files.append(path)
    return output_files
def getpure(filename):
    return filename.split('/')[-1].split('.')[0]


# In[3]:


anno_dir = '/home/xmj/mycipan/tf-faster-rcnn-yuyan/data/VOCdevkit2007/VOC2007/Annotations/'
train_dir = '/home/xmj/mycipan/tf-faster-rcnn-yuyan/data/VOCdevkit2007/VOC2007/ImageSets/Main/'
train_txt = train_dir + 'train.txt'
test_txt = train_dir + 'test.txt'
val_txt = train_dir + 'val.txt'
trainval_txt = train_dir + 'trainval.txt'
train_percent = 0.95
val_percent = 0.2


# In[8]:


#split
files = getallfiles(anno_dir)
print(len(files))
files = list(map(getpure, files))
random.shuffle(files)
train_split = int(len(files) * train_percent)
train_files = files[:train_split]
test_files = files[train_split:]
val_split = int(len(files) * val_percent)
random.shuffle(files)
val_files = files[:val_split]


# In[9]:


with open(train_txt, 'w') as f:
    f.write('\n'.join(train_files))
with open(test_txt, 'w') as f:
    f.write('\n'.join(test_files))
with open(val_txt, 'w') as f:
    f.write('\n'.join(val_files))
with open(trainval_txt, 'w') as f:
    f.write('\n'.join(files))


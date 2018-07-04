
# coding: utf-8

# In[1]:


import os
import cv2


# In[2]:


def getallfiles(rootdir):
    output_files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            output_files.append(path)
    return output_files


# In[18]:


video_filename = '鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9001_2_jiaozheng.mp4'
video = cv2.VideoCapture(video_filename)
img_dir = video_filename.split('.')[0]
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
xml_dir = img_dir + '_xml'
if not os.path.exists(xml_dir):
    os.mkdir(xml_dir)
index = 1
while video.isOpened():
    ret, frame = video.read()
    if ret == False:
        break;
    if index % 25 != 0:
        index += 1
        continue
    cv2.imwrite(img_dir + '/'+ str(index) + '.jpg', frame)
    index += 1


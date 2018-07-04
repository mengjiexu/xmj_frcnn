# coding=utf8
from frcnn_detector import FrcnnDetector
import cv2
from simple_sort import SimpleSort
from video_utils import VideoHelper
from image_draw_utils import draw_boxes_and_id
from reader_helper import ReaderHelper
from tidy_utils import getallfiles
import time
import os

video_file_name = "/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/"
my_detector = FrcnnDetector("/home/xmj/mycipan/tf-faster-rcnn-yuyan/output/vgg16/voc_2007_trainval/default/vgg16_faster_rcnn_yuyan_iter_20000.ckpt")
video_file_name = '/home/xmj/roivision_ai/data/videos/01007506417109002/20180702090000_mpeg.mp4'
video_file_name = '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9002_2_jiaozheng.mp4'

my_simple_sort = SimpleSort()
my_reader_helper = ReaderHelper((98,141))
my_video_helper = VideoHelper(video_file_name)


def detecte_img(img_file):
    img = cv2.imread(img_file)
    cls_dets = my_detector.frcnn_predict_img(img)
    img = draw_boxes_and_id(img, cls_dets)
    cv2.imshow('img',img)
    cv2.waitKey()
    return img

# img_files = getallfiles('/home/xmj/mycipan/videoframe')
# img_files = getallfiles('/home/xmj/Desktop/温氏鱼眼unframe/ch04_20180603095319')
# for f in img_files:
#     detecte_img(f)

frame_iter = my_video_helper.get_frame_iter()
frame = next(frame_iter)
i=0
W=521
H=288
len_mode = 5
if not os.path.exists('wrong_img'):
    os.mkdir('wrong_img')
while frame is not None:
    if i % 3 != 0:
        frame = next(frame_iter)
        i += 1
        continue
    frame = cv2.resize(frame, (W, H))
    tic = time.clock()
    cls_dets = my_detector.frcnn_predict_img(frame)
    # print(time.clock() - tic)
    sort_output = my_simple_sort.update(cls_dets)
    # print(my_reader_helper.update(sort_output))
    if len(sort_output) != len_mode:
        cv2.imwrite('wrong_img/'+str(i)+'.jpg', frame)
    frame = draw_boxes_and_id(frame, sort_output)
    if len(sort_output) != len_mode:
        cv2.imwrite('wrong_img/label_'+str(i)+'.jpg', frame)
    cv2.imshow('img', frame)
    cv2.waitKey(1)
    # break
    frame = next(frame_iter)
    i+=1



    
    
    
    
    
    
    
    

# coding=utf8
import math
import numpy as np

def cal_dis(p1, p2):
    return math.sqrt(float(p1[0] - p2[0]) * (p1[0] - p2[0]) + float(p1[1] - p2[1]) * (p1[1] - p2[1]))

def cal_dis_yueduqi_center(img, bbox, yuedu_point):
    biankuang = 10
    x1, x2, y1, y2 = (int(bbox[0]), int(bbox[2]), \
                      int(bbox[1]), int(bbox[3]))
    x1 = max(0, x1 - biankuang)
    x2 = min(500, x2 + biankuang)
    y1 = max(0, y1 - biankuang)
    y2 = min(280, y2 + biankuang)
    head_point = (int((x1+x2)/2), int((y1+y2)/2))
    return cal_dis(head_point, yuedu_point), head_point

class ReaderHelper(object):
    """用于耳标号和猪身份ID的对应"""
    def __init__(self, reader_point):
        self.reader_point = reader_point
        self.label_id_dict = {}
        
    def update(self, sort_boxes, read_erbiao=None):
        """
         将耳标号和label_id进行对应
         :param sort_boxes: [[x1,y1,x2,y2,label_id],[x1,y1,x2,y2,label_id],...]
         :param read_erbiao: 在读取到耳标时输入这个参数，读取到的耳标号
         :output output：[[x1,y1,x2,y2,label_id, ''],[x1,y1,x2,y2,label_id,'1233456'],[x1,y1,x2,y2,label_id,''],...]
        """
        output = []
        if read_erbiao is None:
            for box in sort_boxes:
                box = list(box)
                if box[-1] in self.label_id_dict:
                    box.append(self.label_id_dict[box[-1]])
                else:
                    box.append('')
                output.append(box)
            return output
        else:
            dis_arrs = []
            for box in sort_boxes:
                # 获得所有的猪头到阅读器的距离,暂时只计算猪的中心到阅读器的距离
                dis, head_point = cal_dis_yueduqi_center(box, self.reader_point)
                dis_arrs.append(dis)
            if len(dis_arrs) > 1:
                arg_sort = np.argsort(dis_arrs)
                # ################使用Unet判断是否拥挤，暂时不使用#################
#                 label_unet = myunet.predictImage(copy_frame)
#                 roi_unet = label_unet[yuedu_point[1] - 32:yuedu_point[1] + 32, yuedu_point[0] - 64:yuedu_point[0] + 64]
#                 roi_sum = np.sum(roi_unet)
                # ##########################################
                if dis_arrs[arg_sort[1]] - dis_arrs[arg_sort[0]] > 25:
                    self.label_id_dict[box[arg_sort[0]][-1]] = read_erbiao
            for box in sort_boxes:
                box = list(box)
                if box[-1] in self.label_id_dict:
                    box.append(self.label_id_dict[box[-1]])
                else:
                    box.append('')
                output.append(box)
            return output

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

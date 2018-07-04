# coding=utf8
import numpy as np


def cal_iou(box1, box2):
    """
    calculate the iou
    :param box1: [x1, y1, x2, y2]
    :param box2: [x1, y1, x2, y2]
    :return:
    """
    iou = 0
#     one_x, one_y, one_w, one_h, _ = box1
#     two_x, two_y, two_w, two_h, _ = box2
    one_x, one_y, one_xx, one_yy, _ = box1
    two_x, two_y, two_xx, two_yy, _ = box2
    one_w = one_xx - one_x
    one_h = one_yy - one_y
    two_w = two_xx - two_x
    two_h = two_yy - two_y

    if (abs(one_x - two_x) < ((one_w + two_w) / 2.0)) and (abs(one_y - two_y) < ((one_h + two_h) / 2.0)):
        lu_x_inter = max((one_x - (one_w / 2.0)), (two_x - (two_w / 2.0)))
        lu_y_inter = min((one_y + (one_h / 2.0)), (two_y + (two_h / 2.0)))

        rd_x_inter = min((one_x + (one_w / 2.0)), (two_x + (two_w / 2.0)))
        rd_y_inter = max((one_y - (one_h / 2.0)), (two_y - (two_h / 2.0)))

        inter_w = abs(rd_x_inter - lu_x_inter)
        inter_h = abs(lu_y_inter - rd_y_inter)

        inter_square = inter_w * inter_h
        union_square = (one_w * one_h) + (two_w * two_h) - inter_square

        iou = inter_square / union_square * 1.0
    return iou


class SimpleSort(object):
    """用于检测框的追踪"""
    def __init__(self, iou_thresh=0.75, remember_imgs=10):
        self.iou_thresh = iou_thresh
        self.remember_imgs = remember_imgs
        self.previous_bboxes = []
        self.previous_label_arrs = []
        self.label_max = 0
        self.box2label_dicts = []
    
    def update(self, now_bbox):
        temp_label_arrs = []
        dis_arrs = []
        if len(self.previous_bboxes) == 0:
            self.previous_label_arrs.append(list(range(len(now_bbox))))
            self.previous_bboxes.append(now_bbox)
            output = []
            for i in range(len(now_bbox)):
                now_bbox[i][-1] = self.previous_label_arrs[-1][i]
                output.append(now_bbox[i])
            return output
        for i in range(len(now_bbox)):
            arg_max_arr = []
            iou_arrs = []
            for j in range(len(self.previous_bboxes)):
                iou_arr = []
                for k in range(len(self.previous_bboxes[j])):
                    iou_arr.append(cal_iou(now_bbox[i], self.previous_bboxes[j][k]))
                arg_max_arr.append(np.argmax(iou_arr))
                iou_arrs.append(iou_arr)
            arg_max_1 = 0
            for j in range(len(arg_max_arr)):
                if iou_arrs[arg_max_1][arg_max_arr[arg_max_1]] not in temp_label_arrs:
                    arg_max_1 = j
#                 else:
#                     # 处理一个大框变成两个小框时的情况，两个框id都变为新的id
#                     print(now_bbox[i],'wrong', temp_label_arrs, self.previous_label_arrs, arg_max_1, self.previous_bboxes)
#                     cv2.waitKey()
#                     self.label_max += 1
#                     temp_label_arrs.append(self.label_max)
#                     self.label_max += 1
#                     for temp_i in range(len(temp_label_arrs)):
#                         if temp_label_arrs[temp_i] == self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]]:
#                             temp_label_arrs[temp_i] = self.label_max
            if iou_arrs[arg_max_1][arg_max_arr[arg_max_1]]>self.iou_thresh:
                if self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]] not in temp_label_arrs:
                    temp_label_arrs.append(self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]])
                else:
                    self.label_max += 1
                    temp_label_arrs.append(self.label_max)
            else:
                temp_label_arrs.append(self.label_max + 1)
                self.label_max += 1
        self.previous_label_arrs.append(temp_label_arrs)
        self.previous_bboxes.append(now_bbox)
        if len(self.previous_label_arrs) > self.remember_imgs:
                self.previous_label_arrs.remove(self.previous_label_arrs[0])
                self.previous_bboxes.remove(self.previous_bboxes[0])
        output = []
        for i in range(len(now_bbox)):
            now_bbox[i][-1] = self.previous_label_arrs[-1][i]
            output.append(now_bbox[i])
        return output
    
#     def update(self, now_bbox):
#         """
#         input:[[x1,y1,x2,y2,score],[x1,y1,x2,y2,score],...]
#         output:[[x1,y1,x2,y2,label_id],[x1,y1,x2,y2,label_id],...]
#         """
#         temp_label_arrs = []
#         if len(self.previous_bboxes) == 0:
#             self.previous_label_arrs.append(list(range(len(now_bbox))))
#             self.previous_bboxes.append(now_bbox)
#             output = []
#             for i in range(len(now_bbox)):
#                 now_bbox[i][-1] = self.previous_label_arrs[-1][i]
#                 output.append(now_bbox[i])
#             return output
#         for i in range(len(now_bbox)):
#             arg_max_arr = []
#             iou_arrs = []
#             for j in range(len(self.previous_bboxes)):
#                 iou_arr = []
#                 for k in range(len(self.previous_bboxes[j])):
#                     iou_arr.append(cal_iou(now_bbox[i], self.previous_bboxes[j][k]))
#                 arg_max_arr.append(np.argmax(iou_arr))
#                 iou_arrs.append(iou_arr)
#             arg_max_1 = 0
#             for j in range(len(arg_max_arr)):
#                 if iou_arrs[arg_max_1][arg_max_arr[arg_max_1]] < iou_arrs[j][arg_max_arr[j]]:
#                     arg_max_1 = j
#             # 寻找前几帧最近的box
#             if iou_arrs[arg_max_1][arg_max_arr[arg_max_1]] > self.iou_percent:
#                 if self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]] not in temp_label_arrs:
#                     temp_label_arrs.append(self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]])
#                 else:
#                     # 处理一个大框变成两个小框时的情况，两个框id都变为新的id
#                     print(now_bbox[i],'wrong', temp_label_arrs, self.previous_label_arrs, arg_max_1, self.previous_bboxes)
#                     cv2.waitKey()
#                     self.label_max += 1
#                     temp_label_arrs.append(self.label_max)
#                     self.label_max += 1
#                     for temp_i in range(len(temp_label_arrs)):
#                         if temp_label_arrs[temp_i] == self.previous_label_arrs[arg_max_1][arg_max_arr[arg_max_1]]:
#                             temp_label_arrs[temp_i] = self.label_max
#             else:
#                 self.label_max += 1
#                 temp_label_arrs.append(self.label_max)
#         # 处理少检测的框(暂不处理)
# #         for m in range(len(previous_bboxes)):
# #             if len(now_bbox) < len(previous_bboxes[m]):
# #                 for i in range(len(provious_bboxes[m])):
# #                     if label_arrs[m][i] not in temp_label_arrs:
#         self.previous_label_arrs.append(temp_label_arrs)
#         self.previous_bboxes.append(now_bbox)
#         if len(self.previous_label_arrs) > self.remember_imgs:
#                 self.previous_label_arrs.remove(self.previous_label_arrs[0])
#                 self.previous_bboxes.remove(self.previous_bboxes[0])
#         output = []
#         for i in range(len(now_bbox)):
#             now_bbox[i][-1] = self.previous_label_arrs[-1][i]
#             output.append(now_bbox[i])
#         return output
                        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


#coding=utf8
import cv2

def draw_boxes_and_id(frame, boxs):
    """
     frame: 图片
     boxs:[[x1,y1,x2,y2,label_id],[x1,y1,x2,y2,label_id],...]
    """
    for box in boxs:
        bbox = list(map(int, box[0:4]))
        label = box[4]
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 255, 0), 2)
        now_bbox = bbox
        cv2.putText(frame, str(label)[:5], ((int)((now_bbox[0] + now_bbox[2]) / 2),
                                        int((now_bbox[1] + now_bbox[3]) / 2)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    return frame


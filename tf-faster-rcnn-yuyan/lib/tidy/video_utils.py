# coding=utf8
import cv2


class VideoHelper:
    def __init__(self, video_file_name):
        self.video_file_name = video_file_name
        self.video = cv2.VideoCapture(video_file_name)
        self.frame_count = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

    def get_frame_iter(self):
        i = 0 
        while self.video.isOpened() and i<self.frame_count:
            ret, frame = self.video.read()
            yield frame
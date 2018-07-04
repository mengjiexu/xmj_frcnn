from tidy.frcnn_detector import FrcnnDetector
import os
import cv2
import sys


def getallfiles(rootdir):
    output_files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            output_files.append(path)
    return output_files


if __name__ == '__main__':
    model_ckpt = sys.argv[1]
    frcnn_model = FrcnnDetector(model_ckpt, 0.6)
    img_dir = sys.argv[2]
    output_xml_dir = sys.argv[3]
    print('load images from ', img_dir)
    files = getallfiles(img_dir)
    for f in files:
        if f.endswith('jpg'):
            img = cv2.imread(f)
            if img is None:
                continue
            h, w, d = img.shape
            output_str = '''<annotation>
	<folder>JPEGImages</folder>
	<filename>'''+f.split('/')[-1]+'''</filename>
	<path>'''+f+'''</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>'''+str(w).split('.')[0]+'''</width>
		<height>'''+str(h).split('.')[0]+'''</height>
		<depth>'''+str(d).split('.')[0]+'''</depth>
	</size>
	<segmented>0</segmented>'''
            cls_boxes = frcnn_model.frcnn_predict_img(img)
            for box in cls_boxes:
                xmin, ymin, xmax, ymax,_ = box
                output_str += '''\n<object>
		<name>pig</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>'''+str(xmin).split('.')[0]+'''</xmin>
			<ymin>'''+str(ymin).split('.')[0]+'''</ymin>
			<xmax>'''+str(xmax).split('.')[0]+'''</xmax>
			<ymax>'''+str(ymax).split('.')[0]+'''</ymax>
		</bndbox>
	</object>'''
            output_str += '</annotation>'
            with open(output_xml_dir+'/'+f.split('/')[-1].replace('jpg', 'xml'), 'w') as f:
                f.write(output_str)




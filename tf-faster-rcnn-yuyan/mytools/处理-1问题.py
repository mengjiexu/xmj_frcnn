import os
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
    # dir = sys.argv[1]
    dir = "/home/xmj/mycipan/tf-faster-rcnn-yuyan/data/VOCdevkit2007/VOC2007/Annotations"
    files = getallfiles(dir)
    for f in files:
        output_str = ''
        lines = open(f).readlines()
        for line in lines:
            shuzi = 1
            if 'xmin' in line:
                shuzi = int(line.split('<xmin>')[-1].split('</xmin>')[0])
                if shuzi == 0:
                    shuzi = 1
                if shuzi >2:
                    shuzi -= 1
                line = '<xmin>'+str(shuzi)+'</xmin>\n'
            if 'ymin' in line:
                shuzi = int(line.split('<ymin>')[-1].split('</ymin>')[0])
                if shuzi == 0:
                    shuzi = 1
                if shuzi >2:
                    shuzi -= 1
                line = '<ymin>'+str(shuzi)+'</ymin>\n'
            if 'xmax' in line:
                shuzi = int(line.split('<xmax>')[-1].split('</xmax>')[0])
                if shuzi == 0:
                    shuzi = 1
                if shuzi >2:
                    shuzi -= 1
                line = '<xmax>'+str(shuzi)+'</xmax>\n'
            if 'ymax' in line:
                shuzi = int(line.split('<ymax>')[-1].split('</ymax>')[0])
                if shuzi == 0:
                    shuzi = 1
                if shuzi >2:
                    shuzi -= 1
                line = '<ymax>'+str(shuzi)+'</ymax>\n'
            output_str += line
        with open(f, 'w') as f:
            f.write(output_str)
        print('process', f)



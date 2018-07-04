import shutil
import os


def getallfiles(rootdir):
    output_files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            output_files.append(path)
    return output_files


if __name__ == '__main__':
    print('start')
    xml_dirs = ['/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9001_jiaozheng_xml',
                '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9002_2_jiaozheng_xml',
                '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9002_jiaozheng_xml',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9003_jiaozheng_xml',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9003_2_jiaozheng_xml',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9004_jiaozheng_xml',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9001_2_jiaozheng_xml',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/wrong_img_v1_xml']

    img_dirs = ['/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9001_jiaozheng',
                '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9002_2_jiaozheng',
                '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9002_jiaozheng',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9003_jiaozheng',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9003_2_jiaozheng',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9004_jiaozheng',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/9001_2_jiaozheng',
               '/home/xmj/mycipan/鱼眼矫正数据以及对应模型/鱼眼矫正数据（14个猪场视频）及对应模型_v2_VOCdevkit2007/wrong_img_v1']

    aim_xml_dir = '/home/xmj/mycipan/tf-faster-rcnn-yuyan/data/VOCdevkit2007/VOC2007/Annotations'
    aim_img_dir = '/home/xmj/mycipan/tf-faster-rcnn-yuyan/data/VOCdevkit2007/VOC2007/JPEGImages'

    zero_num = 0
    for dir in xml_dirs:
        files = getallfiles(dir)
        for f in files:
            fname = f.split('/')[-1]
            for i in range(zero_num):
                fname = '0' + fname
            shutil.copy(f, aim_xml_dir + '/' + fname)
        zero_num += 1

    zero_num = 0
    for dir in img_dirs:
        files = getallfiles(dir)
        for f in files:
            fname = f.split('/')[-1]
            for i in range(zero_num):
                fname = '0' + fname
            shutil.copy(f, aim_img_dir + '/' + fname)
        zero_num += 1
    xml_files = getallfiles(aim_xml_dir)
    img_files = getallfiles(aim_img_dir)
    for f in xml_files:
        fname = f.split('/')[-1].split('.')[0]
        temp = []
        for ff in img_files:
            ffname = ff.split('/')[-1].split('.')[0]
            temp.append(ffname)
        if fname not in temp:
            os.remove(f)




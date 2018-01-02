import os
import sys
import shutil

root_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(root_folder))

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' make_newdir')
        return True
    else:
        print(path + ' existed')
        return False

dataset_path = '/home/catidog/work/remake/test_dataset' #测试数据集的路径记为dataset_path
output_path = '/home/catidog/work/remake/dataset_output' #输出总路径记为output_path

video_list = os.listdir(dataset_path) #打开数据集文件夹，里面每个视频是一个文件夹，所有文件夹合成一个list

for vid in video_list: #读取每个视频，每次循环时文件名记为vid

    frame_path = os.path.join(output_path, vid, 'frame') #输出rgb,flow的路径为output_path+vid+frame或者flow
    flow_path = os.path.join(output_path, vid, 'flow')
    mkdir(flow_path)
    mkdir(frame_path)

    vid_path = os.path.join(dataset_path, vid)#数据集里每个视频的路径为dataset_path+vid
    img_list = os.listdir(vid_path)#打开视频文件夹，里面所有图片组成一个list
    #move
    for pic in img_list:
        pic_path = os.path.join(vid_path, pic)
        pic_type = pic.split('_')[0]
        #print(pic_type)
        if pic_type == 'img':
            shutil.move(pic_path, frame_path)
        else:
            shutil.move(pic_path, flow_path)

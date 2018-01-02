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

dataset_path = '/home/catidog/work/remake/test_dataset'
output_path = '/home/catidog/work/remake/dataset_output'

video_list = os.listdir(dataset_path)
#print(img_list)
for vid in video_list:

    frame_path = os.path.join(output_path, vid, 'frame')
    flow_path = os.path.join(output_path, vid, 'flow')
    mkdir(flow_path)
    mkdir(frame_path)

    vid_path = os.path.join(dataset_path, vid)
    img_list = os.listdir(vid_path)
    for pic in img_list:
        pic_path = os.path.join(vid_path, pic)
        pic_type = pic.split('_')[0]
        #print(pic_type)
        if pic_type == 'img':
            shutil.move(pic_path, frame_path)
        else:
            shutil.move(pic_path, flow_path)
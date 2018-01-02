import os
import sys
import shutil

root_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(root_folder))

img_path = '/home/catidog/work/remake/test_img'
frame_path = '/home/catidog/work/remake/output/frame'
flow_path = '/home/catidog/work/remake/output/flow'

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
mkdir(flow_path)
mkdir(frame_path)

img_list = os.listdir(img_path)
#print(img_list)
for pic in img_list:
    pic_path = os.path.join(img_path, pic)
    pic_type = pic.split('_')[0]
    #print(pic_type)
    if pic_type == 'img':
        shutil.move(pic_path, frame_path)
    else:
        shutil.move(pic_path, flow_path)



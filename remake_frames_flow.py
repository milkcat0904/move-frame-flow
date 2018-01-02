import os
import sys
import shutil

root_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(root_folder))

img_path = '/home/catidog/work/remake/test_img' #光流图和rgb的路径
frame_path = '/home/catidog/work/remake/output/frame' #rgb要放入的文件夹的路径——frame_path
flow_path = '/home/catidog/work/remake/output/flow' #光流要放入的文件夹的路径——flow_path

#定义新建文件夹函数
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists: #如果路径中的文件夹不存在，新建
        os.makedirs(path)
        print(path + ' make_newdir')
        return True
    else:
        print(path + ' existed') #如果已经存在，则输出‘existed’
        return False
mkdir(flow_path)  #新建存放rgb，光流图的文件夹
mkdir(frame_path)

#move
img_list = os.listdir(img_path) #将输入文件夹中所以的rgb，光流图存放在img_list里

for pic in img_list: #循环读图，每次循环里的图的文件名记为pic
    pic_path = os.path.join(img_path, pic) #pic的位置为img_path+pic，用pic_path表示
    pic_type = pic.split('_')[0] #将图片的文件名用'_'分开，取第一项记为'pic_type'
    if pic_type == 'img': #如果pic_type=img，则将pic移动到frame_path
        shutil.move(pic_path, frame_path) #反之，移动到flow_path
    else:
        shutil.move(pic_path, flow_path)



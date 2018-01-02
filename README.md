# move-frame-flow
批量将rgb,flow图放在指定文件夹里

1.测试一个视频
=
* 在测试文件夹中一个视频的rgb,光流图是放在一起的，现在要把两种模态放在不同的文件夹里
	
输入：	

![image](https://github.com/milkcat0904/move-frame-flow/raw/master/pic/input.PNG)	

输出：
	
![image](https://github.com/milkcat0904/move-frame-flow/raw/master/pic/output.png)

* 程序输出结果会在output文件夹中新建frame，optical_flow两个文件夹分别用来放rgb，光流图

  `frame_path`——存放rgb的文件夹路径
  
  `flow_path`——存放flow的文件夹路径

* 移动依据：
	* 将图片文件名用‘_’拆开，第一项记为`pic_type`
	
	
		if pic_type = 'img':
		
			把这个pic放在frame_path里：
			
			shutil.move(pic_path, frame_path)
			
		else：
		
			放在flow_path里
			
			shutil.move(pic_path, flow_path)

* 运行程序:

		$ python remake_frames_flow.py


2.数据集
=

* 将一个数据集里所有视频都进行移动处理
		
		$ python remake_dataset_frames_flow.py

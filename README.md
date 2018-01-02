# move-frame-flow
批量将rgb,flow图放在指定文件夹里

1.测试一个视频
==
* 在测试文件夹中一个视频的rgb,光流图是放在一起的，现在要把两种模态放在不同的文件夹里
	
输入：	

![image](https://github.com/milkcat0904/move-frame-flow/raw/master/pic/input.PNG)	

输出：
	
![image](https://github.com/milkcat0904/move-frame-flow/raw/master/pic/output.png)

* 程序输出结果会在output文件夹中新建frame，optical_flow两个文件夹分别用来放rgb，光流图

  `frame_path`——存放rgb的文件夹路径
  
  `flow_path`——存放flow的文件夹路径
  

* 运行程序:

		$ python remake_frames_flow.py

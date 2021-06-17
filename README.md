# Pose2Carton 

EE228 课程大作业，利用3D骨架控制3D卡通人物。



# Maya 环境配置

首先在https://www.autodesk.com.cn/products/maya/overview 下载maya。

在该网站中会要求一个Autodesk的账户申请，提交学生证以申请教育版权限。在成功申请之后会获得maya2020的安装包进行安装。

不要安装到系统盘（路径不要出现中文），同时系统盘应保证还有4-5G的空间。

安装成功后运行maya2020，并保持界面不要关闭。

随后添加环境变量，进入maya2020的bin文件，将该路径添加到环境变量。

打开cmd输入mayapy，若正常打开则以添加成功。

打开cmd输入
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py

mayapy get-pip.py

以及

mayapy -m pip install -i https://pypi.anaconda.org/carlkl/simple numpy

安装pip以及numpy，期间不要关闭maya页面。

在mayapy中输入

import maya

import maya.standalone

maya.standalone.initialize(name='python')

import maya.OpenMaya as om

import maya.cmds as cmds

import pymel.core as pm

import maya.mel as mel

import numpy as np

import os

import glob

若成功运行则配置完成。



# 匹配流程

10 组不带蒙皮模型匹配


在提供的 groups 文件夹中找到自己对应的编号，并在其中挑选 10 个模型，在选择模型的时候
需要注意避免非人型的模型，由于动作迁移的本体为人的动作，非人型的模型难以进行动作迁移。
选择模型之后，将其对应的.txt 文件导入 transfer.py 程序中，将模型的关节节点与程序中提供的
节点一一匹配，并运行 transfer.py 程序。


运行之后可以在 obj_seq_5_3dmodel 文件夹中查看每一个动作的 obj 文件。随后运行 vis.py 程序，
生成 447 张.png 图片，并最后生成一个.mp4 视频，在视频中即可查看模型与原模型的动作迁移情况，
若不一致则需要进行调整。


5 组带蒙皮模型匹配


在网上下载 5 个模型，利用 maya 运行 fbx_parser.py，得到.fbm 文件夹以及.obj 和.txt 文件，其
中.fbm 文件夹包含该模型的外皮.jpg 图片文件。


将.txt 文件导入 transfer.py 程序中，并使用 transfer_one_frame 以及 transfer_one_sequence 函数。
在对关节进行匹配之后，运行 transfer.py 程序，得到更新的 obj_seq_5_3dmodel 文件夹。


由于网络下载的模型都是含蒙皮的，所以我们也需要将模型进行相应的蒙皮。将.fbm 文件夹中
的.jpg 文件放入 obj_seq_5_3dmodel 文件夹，除此之外我们发现该文件夹中还有.mtl 文件的快捷方式，
找到相应的.mtl 文件（由 transfer.py 程序生成），并进行相应的编辑，利用 map_Kd 指令指向该图片
的名称。运行 vis.py 程序，即可得到蒙皮模型对应的动作迁移图片和视频。



# 新增脚本说明

如果你写了自己的脚本来处理数据或进行可视化，请在这里进行相关说明(如何使用等)； 如果没有，请忽略该模块。



# 项目结果


<image src="183834.png"/><image src="183912.png"/><image src="183939.png"/><image src="184104.png"/><image src="184213.png"/>
<image src="184250.png"/><image src="184354.png"/><image src="184421.png"/><image src="184450.png"/><image src="184641.png"/>
<image src="184702.png"/><image src="184828.png"/><image src="185550.png"/><image src="185613.png"/><image src="185659.png"/>
<image src="185732.png"/><image src="185754.png"/><image src="185820.png"/><image src="185840.png"/><image src="185900.png"/>
<image src="185921.png"/><image src="190148.png"/><image src="191110.png"/><image src="191139.png"/><image src="191204.png"/>
<image src="191226.png"/><image src="191250.png"/><image src="snapshot00.png"/><image src="snapshot0101.png"/><image src="snapshot0200.png"/>
<image src="snapshot0300.png"/><image src="snapshot0400.png"/><image src="snapshot0500.png"/>





# 协议 
本项目在 Apache-2.0 协议下开源

所涉及代码及数据的最终解释权归倪冰冰老师课题组所有

Group xx

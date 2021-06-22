# Pose2Carton 

EE228 课程大作业 利用3D骨架控制3D卡通人物 (https://github.com/yuzhenbo/pose2carton)

数据组别： 36 & 37 

数据类型： 

36: 12组匹配 + 6组蒙皮

37: 10组匹配 + 5组蒙皮



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

mayapy -m pip install -i https://pypi.anaconda.org/carlkl/simple numpy

安装pip以及numpy。

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

若遇到“找不到首选项”的提示，将C盘安装目录下的首选项文件从/maya/zh-cn文件夹复制到/maya文件夹下即可解决。



# 匹配流程

## 10 组不带蒙皮模型匹配


在提供的 groups 文件夹中找到自己对应的编号，并在其中挑选 10 个模型，在选择模型的时候
需要注意避免非人型的模型，由于动作迁移的本体为人的动作，非人型的模型难以进行动作迁移。
选择模型之后，将其对应的.txt 文件导入 transfer.py 程序中，将模型的关节节点与程序中提供的
节点一一匹配，并运行 transfer.py 程序。


运行之后可以在 obj_seq_5_3dmodel 文件夹中查看每一个动作的 obj 文件。随后运行 vis.py 程序，
生成 447 张.png 图片，并最后生成一个.mp4 视频，在视频中即可查看模型与原模型的动作迁移情况，
若不一致则需要进行调整。


## 5 组带蒙皮模型匹配


在网上下载 5 个模型，利用 maya 运行 fbx_parser.py，得到.fbm 文件夹以及.obj 和.txt 文件，其
中.fbm 文件夹包含该模型的外皮.jpg 图片文件。


将.txt 文件导入 transfer.py 程序中，并使用 transfer_one_frame 以及 transfer_one_sequence 函数。
在对关节进行匹配之后，运行 transfer.py 程序，得到更新的 obj_seq_5_3dmodel 文件夹。


由于网络下载的模型都是含蒙皮的，所以我们也需要将模型进行相应的蒙皮。将.fbm 文件夹中
的.jpg 文件放入 obj_seq_5_3dmodel 文件夹，除此之外我们发现该文件夹中还有.mtl 文件的快捷方式，
找到相应的.mtl 文件（由 transfer.py 程序生成），并进行相应的编辑，利用 map_Kd 指令指向该图片
的名称。运行 vis.py 程序，即可得到蒙皮模型对应的动作迁移图片和视频。


## 对函数的理解

在 transfer.py 中，函数 transfer_given_pose 的作用之一就是提取并分析这一树形结构，将树形结
构的节点转化为关节的标号，进而对相同的关节进行匹配并生成新的模型。


# 新增脚本说明


## 基于文本的自动匹配


由于匹配过程的关键在于将.txt 文件中的模型关节序号与 transfer.py 文件中的人体关节序号进行
一一对应，而这一过程的方法与流程较为固定。在匹配过程中发现尽管模型不同，但模型的关节名
称大都相同。因此可以考虑通过对.txt 文本进行分解，从中提取出关节名称和对应的序号，实现与人
体的自动匹配。与已有的 _lazy_get_model_to_smpl 不同的是，这里将一部分经常出现但与人体模型
名称不同的关节进行了替换，如 L,R 替换为 left,right，elbow 替换为 shoulder 等。


在 transfer.py 中已经有一部分代码通过分析节点之间的父子关系从而得到每个关节的标号，因
此可以复用这部分代码，得到字典 new_joint2index。


将字典转化为字符串。注意到有的模型在关节名称前还会有模型名称或单引号，如’mixamorig:Hips’:0。
因此在匹配之前需要将关节名称和标号提取出来。


使用 replace 和 split 函数将多余字符去掉，得到关节名称与编号的对应关系。接下来就是关节编
号与人体关节的对应。将关节名称进行一一比对，比对结果存放于字符串中，在比对结束后将字符
串转换为字典即可得到匹配结果。


可见代码automap.py。


## mtl 文件修改


在有蒙皮模型的匹配过程中，需要将.mtl文件下的 map_Kd 后的绝对路径地址修改为相对路径
地址，否则会导致找不到蒙皮文件，得到的匹配模型为灰色。可以通过文件读写实现这一过程。具
体实现思路是使用遍历.mtl文件，使用 split 提取每一行第一个单词，当检测到 map_Kd 所在行时将
其后的路径修改，并将修改后的文件写回原文件。


可见代码changemap.py。


## 使用方法


在需要对 manual_model_to_smpl 进行修改时调用即可实现自动匹配。对.mtl文件的修改在蒙皮
开始前完成即可


# 项目结果

## 36
<image src="183834.png"/><image src="183912.png"/><image src="183939.png"/><image src="184104.png"/><image src="184213.png"/>
<image src="184250.png"/><image src="184354.png"/><image src="184421.png"/><image src="184450.png"/><image src="184641.png"/>
<image src="184702.png"/><image src="184828.png"/>
<image src="snapshot00.png"/><image src="snapshot0101.png"/><image src="snapshot0200.png"/>
<image src="snapshot0300.png"/><image src="snapshot0400.png"/><image src="snapshot0500.png"/>

## 37
<image src="185550.png"/><image src="185613.png"/><image src="185659.png"/><image src="185732.png"/><image src="185754.png"/>
<image src="185820.png"/><image src="185840.png"/><image src="185900.png"/><image src="185921.png"/><image src="190148.png"/>
<image src="191110.png"/><image src="191139.png"/><image src="191204.png"/><image src="191226.png"/><image src="191250.png"/>





# 协议 
本项目在 Apache-2.0 协议下开源

所涉及代码及数据的最终解释权归倪冰冰老师课题组所有

Group 35&36

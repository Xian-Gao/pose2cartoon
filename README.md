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

这里请简单描述你熟悉/使用 匹配代码的流程，可以简述对代码的理解/各个函数作用等。





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

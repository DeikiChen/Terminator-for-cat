贼猫终结者 
---

这是一个风和日丽的周末，我把美味的鲈鱼从冰箱里拿出来解冻，睡个午觉打个游戏后，准备晚上大吃一顿……

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqd8uxjGJN9sVBAULbw5hXS9MHfW08vcxcCicQibSlSAJIIrr1TDzcoDbA/0?wx_fmt=jpeg)

美好的剧本都会紧接着一个可怕的转折……这并不是一个应该有的套路，当我准备对鱼下手的时候，万万没想到，鱼不见了？！
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqTD0lEzJhhcK2KcJHecdcUVfyIlGZ1fibpsLmlcvIWC4KkUSCfe8diaSQ/0?wx_fmt=jpeg)

不用多想，没谁了，也就家里那只馋猫能干得出来！随后，我便在屋子的某个角落，找到了正在品尝我的晚餐的那只馋猫……

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqFNTlXHybOr7INzO1Iu8mADMJZhOMwNZGxygcw8YB2WujpuiaIK9QykA/0?wx_fmt=jpeg)

**没错**,今天的主角就是这只馋猫，它总会趁人不注意的时候潜入厨房偷
吃没封装的食材，或者趁家里人都去上班的时候，将垃圾桶翻个底朝天，并且屡教不改。这次，我决定给它一些颜色看看。
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqGt5C7pZ4sUAKVxZtjj2ibq5gmIwVgYibaicpaHOibUbXQDnobb6hGCdWqQ/0?wx_fmt=jpeg)

我的脑海中浮现了一个“残忍邪恶”的报复计划：


> ### 制作一个”家用版”自动防入侵驱逐系统，让猫从此不敢再踏入厨房



更详细地说，这个被我命名为“贼猫终结者”的设备将使用计算机视觉识别运动的物体，当有猫进入摄像头监视的范围内时，便控制水枪跟随标准运动物体，并启动喷雾水枪喷射。水雾不会对猫造成伤害，但对于这只怕水的猫，足以让它忌惮三分。 

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcq4J4MRv2qg4Iiaj5zwYPmurv8dhKhpob5URBA3EicVbzl5hcRXfBw0hcA/0?wx_fmt=jpeg)

为了防止世界被破坏，为了保护世界的和平，贯彻爱与真实的邪恶……今天我就来教大家如何自制一个“贼猫终结者”，让你从此远离垃圾、饿肚子烦恼！

## 需要准备的材料

---
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqtKOPLeGC5hy3CMUj4ibSp5ZLQhAlB7iacPzIlDRyn1q2PoQa9lgicpJdg/0?wx_fmt=png)

- 树莓派及电源 × 1
- USB摄像头 ×1
- 舵机 × 2
- FPV舵机云台 ×1
- 12V小型直流隔膜泵及电源 ×1
- 水箱 × 1
- 集线盒 × 1
- 继电器模块 ×1
- 雾化喷头 ×1
- HC-SR501人体红外感应模块  ×1
- 激光二极管 ×1
- 导线若干
- 硅胶管 若干

## 选择一个核心控制器

---

首先一个“贼猫终结者”的核心控制所在就是树莓派了，**价格低廉性能好是树莓派的优点。**

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqejxICzeNe0WfPj3Z1t6vv3Nz1kanS6pfEMF7DBNShDkuZ6YwUuaToQ/0?wx_fmt=jpeg)

“贼猫终结者”中，树莓派负责计算出视频信号中是否有运动的物体、判断是否有人正在周围、控制水枪喷水。我在制作的过程中分别使用了Raspberry Pi 2B和3B，相比Raspberry Pi 2B，最新的3B版本计算能力更强，而且集成了Wi-Fi模块，少了一些牵网线或配置无线网卡之类的烦恼。

##为它找个“眼睛”
---

有了核心部分，接着就是视觉处理方面了，你要看到周围运动的物体，当然免不了一个摄像头了！
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqiaiakFfnal7xYyEx1doZKIcmwC979Qt4xjlUpUNXUQngWfU8SyzQobKA/0?wx_fmt=jpeg)
我用一个免驱USB摄像头用来获取环境图像信号。树莓派上运行Python脚本，调用OpenCV视觉库，判断出运动的物体并计算出运动物体所在的位置。由于我对计算机视觉学习还不够深入，没办法判断出运动物体是人还是猫，所以我又加了一块人体红外感应的模块。当人体红外感应模块判断有人在场时便禁止水枪运行，当没人在场时，便会允许水枪喷水。

## 水枪部分制作
---
“贼猫终结者”的水枪是由一个雾化喷头做成，当看到有贼猫来偷东西时，喷头就能喷出水雾驱赶它。通常雾化喷头需要有比较强的水压才能喷射出水雾，采用一台12V微型的隔膜泵和一个可调的雾化喷头。隔膜泵通过一个继电器控制开关，当猫进入监控的范围内，树莓派会控制继电器闭合，让隔膜泵开始运行。
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqW8hPxWItjjRuuu9iczyOAUPR4ueAIA1PGfcibyDwjiaYfmagAictlZJTVg/0?wx_fmt=jpeg)
由于单个摄像头无法分辨出运动物体的空间位置，因此我将雾化喷头的喷水面积尽量调大已确保能喷到猫，这时水雾也完全没有冲击力。

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqm4hia9puiaaNClib5j8Gp2dRHA2zP1LNcCKReOSxCqw6bfVzktfMHJY6w/0?wx_fmt=jpeg)

为了让水枪跟随瞄准运动的物体，我找了一个FPV舵机云台用来控制水枪喷射的方向。

用3D打印机打印了一个固定模块用来将喷头固定在云台上，固定模块上预留了一个圆孔用来安装激光二极管。激光二极管用来调整水枪的喷射范围与摄像头的拍摄范围重合。

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqhAzb9UG7wfgZ84hO7n5tckYpuTMnBviaAWkUGpwP0licyCjQcqKRXs1w/0?wx_fmt=gif)
>GIF使用3D打印技术做的支架

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqS0icB5ibsV4trjOXKvOIPQ5l37bZ3BlTT479nTyBsu5iaAfTwSv78m1PA/0?wx_fmt=gif)
>FPV运动状态

## OpenCV运行环境配置
---
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqANjnx9v5DzvNzCtw3mxh7ibiavbqtBMEJbh8v8QKwcDf4xVqFMa3Tj6w/0?wx_fmt=png)
在树莓派操作系统中打开终端，输入指令：

```
sudo apt-get install libcv-dev  libcvaux-dev  libhighgui-dev  opencv-doc python-opencv 
```

按回车，按系统要求输入管理员密码执行安装。安装完后，在终端输入指令：
```
python
```

按回车进入python的shell编程环境，然后输入指令
```
import cv2
```

当shell返回
```
 >>>
```
说明OpenCV计算机视觉库已经安装在树莓派上了。
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcq7BcRZ5qibCktCoTTJKWtCoN01Bg1CABydNxW4MaHYeXTmQYFNxViaQDg/0?wx_fmt=png)
>在终端中查看相关库是否安装成功

## 系统接线图与组装
---
直接上图！
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcq7XRaibdPvZJia1G9PW3JMRibicgtVZ32Ep9ZkKYu7xTGJbC8yia7TjS9IZg/0?wx_fmt=png)

##启动终结者！
---
用Pyhton的IDLE打开程序，按F5运行程序。程序运行的状态如下：
![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqVKmnPSckcIicdKXNcwojibCrLvHmYon0bd4WeAkHmO2eu5fOnzlQX2Sw/0?wx_fmt=gif)
当贼猫过来的时候，哼哼哼……看！被吓到贼猫，还敢来捣乱？

![](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqf7u8YxzBFiaKM4q82bM3cUo3MYEqXYDKp77WInjSgT3StpdftaZ9vibA/0?wx_fmt=gif)

完整视频如下：
[![IMAGE ALT TEXT HERE](http://mmbiz.qpic.cn/mmbiz/W9gSRHIR1WECS9libYhvfYJk5aTrxDQcqtKOPLeGC5hy3CMUj4ibSp5ZLQhAlB7iacPzIlDRyn1q2PoQa9lgicpJdg/0?wx_fmt=png)](https://youtu.be/PgEjKuimXfA)

# uncompyle4all

方便打站的时候扒下来Python站点的源码是pyc的时候，快速反编译，无须浪费生命🐶
~~(主要最近搞的几个都是Python站)~~

![1658467241920.png](https://img1.imgtp.com/2022/07/22/Wa11lmYj.png)

## 环境
Python 3

## 安装

```bash
pip install -r requirements.txt
```

## 使用

`-p` 参数指定路径即可，默认线程数为5
![1658467350478.png](https://img1.imgtp.com/2022/07/22/FVf2shZZ.png)

`-t` 参数可指定线程数
![1658467415912.png](https://img1.imgtp.com/2022/07/22/aylAMyvO.png)

反编译文件的具体情况会在当前文件夹下生成一个对应时间的log文件
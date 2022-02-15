---
title: Mac环境下编译安装tesseract-4.1.1
tags: []
id: '1545'
categories:
  - - 技术杂谈
date: 2021-03-05 11:39:28
---

## 1、安装依赖

```bash
# Packages which are always needed.
brew install automake autoconf libtool
brew install pkgconfig
brew install icu4c
brew install leptonica

# Packages required for training tools.
brew install pango

# Optional packages for extra features.
brew install libarchive

# Optional package for builds using g++.
brew install gcc
```

## 2、下载解压 tesseract-4.1.1.tar.gz

[https://github.com/tesseract-ocr/tesseract/releases](https://github.com/tesseract-ocr/tesseract/releases)

## 3、编译安装

```bash
cd tesseract-4.1.1
./autogen.sh
mkdir build
cd build

# Optionally add CXX=g++-8 to the configure command if you really want to use a different compiler.
../configure PKG_CONFIG_PATH=/usr/local/opt/icu4c/lib/pkgconfig:/usr/local/opt/libarchive/lib/pkgconfig:/usr/local/opt/libffi/lib/pkgconfig
make -j

# Optionally install Tesseract.
sudo make install

# Optionally build and install training tools.
make training
sudo make training-install
```

## 4、下载 eng.traineddata

[https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata) 选择你需要的语言文件下载即可，当然你也可以全部下载下来 。 **那放在哪个文件夹下呢？** **路径在哪里看呢？** 不用担心，你直接进行接下来的步骤，然后查看报错路径即可。

## 5、测试

```bash
$ tesseract 0384.jpg stdout
0 3 8 4
```

### 图片

![](https://img-blog.csdnimg.cn/20210305113441355.png)

#### 看报错路径，把 eng.traineddata 文件拷贝到缺失路径下，再次测试

> 参考：[https://tesseract-ocr.github.io/tessdoc/Compiling.html#macos](https://tesseract-ocr.github.io/tessdoc/Compiling.html#macos)
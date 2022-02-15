---
title: 如何创建 Python 库
tags: []
id: '1867'
categories:
  - - Python 开发库
date: 2021-08-27 11:16:44
---

![在这里插入图片描述](https://img-blog.csdnimg.cn/4372228c8a70408abb54de7f17bc58fb.png) 你好，我是悦创。 我最近想要去开始开发 Python 第三方库，但是发现国内这样的教程太少了，所以就我来写吧！ 还有就是曾经想创建一个 Python 库，无论是为您的工作团队还是在线的一些开源项目？在此博客中，您将学习如何操作！ 当您使用相同的开发工具 Pycharm ，你会最容易跟上我的教程，当然您也可以使用不同的工具。 本文章使用的是工具有：

*   Pycharm
*   Linux 命令行

## 第 1 步：创建一个要放置库的目录

打开命令提示符并创建一个文件夹，您将在其中创建 Python 库。 请记住： - `pwd` 您可以看到您当前的工作目录。 - `ls` 您可以列出当前目录中的文件夹和文件。 - `cd <path>` 您可以更改当前所在的目录。 - `mkdir <folder>` 您可以在当前工作目录中创建一个新文件夹。 在我的例子中，我将使用的文件夹是 `mypythonlibrary` 。将当前工作目录更改为文件夹。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/f8310083b7a1444fb43c0a7b0197fb63.png)

## 第 2 步：为您的文件夹创建一个虚拟环境

在启动您的项目时，创建一个虚拟环境来封装您的项目总是一个好主意。虚拟环境由某个 Python 版本和一些库组成。参考：[这么全的 Python 虚拟环境？不看可惜了！](https://mp.weixin.qq.com/s/-LeK-O6pO5b2SQtB_H83gw) 虚拟环境可防止以后遇到依赖性问题。 例如，在较旧的项目中，您可能使用的是较旧版本的 numpy 库。一些曾经运行良好的旧代码可能会在你更新 numpy 版本后不能正常运行了。 创建虚拟环境可以防止这种情况，当你与其他人协作时，虚拟环境也能确保你的程序在其他人的电脑上正常运行。 接下来，你要确保你当前的工作目录是你刚刚创建的目录，( `cd <path/to/folder>` ) 中创建 Python 库的文件夹。） 继续并通过键入以下内容创建虚拟环境：

```python
python3 -m venv venv
```

创建后，你现在必须使用以下命令激活环境：

```python
source venv/bin/activate
```

PS：Windows

```python
venv\Scripts\activate
```

激活虚拟环境会修改 PATH 和 shell 的变量，以指向您创建的特定虚拟环境 Python 的设置。PATH 是 Linux 和其他类 Unix 操作系统中的环境变量，它告诉 shell 在响应用户发出的命令时，去搜索哪些目录的 Python 执行环境（即准备运行的程序）。命令提示符将更改为通过添加 ( yourenvname) 来指示您当前所在的虚拟环境。 ![在这里插入图片描述](https://img-blog.csdnimg.cn/6478d000ec9d4090b18781cab7b3c217.png) 你要确保你的环境已经安装了 pip、wheel、setuptools、twine。我们稍后将需要它们来构建我们的 Python 库。

```cmd
sudo pip install wheel setuptools twine
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/48374ffc834140e2a02067bdb7ea4d94.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMjU0NzY2,size_16,color_FFFFFF,t_70) 我用的是 Linux 所以，Windows 的话，去掉 sudo。

## 第 3 步：创建文件夹结构

这一步，也就是创建我们开发库所需要的文件。 在 Pycharm 中，打开您的文件夹 mypythonlibrary（或你自己创建的文件夹名称）。它应该是这样的： ![在这里插入图片描述](https://img-blog.csdnimg.cn/43fde6f474504a368d6f17f6b7c9d799.png) 你现在可以开始向项目添加文件夹和文件。您可以通过命令提示符或在 Visual Studio Code 本身中执行此操作。

1.  创建一个名为 `setup.py` 这是创建 Python 库时最重要的文件之一！
2.  创建一个名为 `README.md` 你可以在此处编写 Markdown 以向其他用户描述我们的库内容。
3.  创建一个名为 `mypythonlib` ，或者任何您希望在 pip 安装时调用 Python 库的文件夹。（如果你想稍后发布它，该名称在 pip 上应该是唯一的。）
4.  在 `mypythonlib` 文件夹里面，创建名为 `__init__.py` 基本上，任何包含文件的 `__init__.py` 文件夹，在我们构建库的时候，包含在库中。大多数情况下，您可以将 `__init__.py` 文件留空，也就是不用写代码。导入时，其中的 `__init__.py` 将被执行，因此它应该只包含能够运行您的项目所需的最少量代码。现在，我们将保持原样。
5.  此外，在 `mypythonlib` 文件夹中，创建一个名为 `myfunctions.py`
6.  最后，在您的根文件夹中创建一个文件夹测试。在里面，创建一个空 `__init__.py` 文件和一个空的 `test_myfunctions.py`

你所创建的文件夹和代码文件，现在应如下所示： ![在这里插入图片描述](https://img-blog.csdnimg.cn/27715072092349e2a9dcab35e0d11284.png)

## 第 4 步：为您的库创建内容

要将函数放入库中，您可以将它们放入 `myfunctions.py` 文件中。例如，复制文件中的 hasrsine 函数：

```python
import numpy as np
def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the
    earth (specified in decimal degrees), returns the distance in
    meters.
    All arguments must be of equal length.
    :param lon1: longitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in meters between the two sets of coordinates
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km * 1000
```

这个函数将给出两个纬度和经度点之间的距离，单位为米。 每当您编写任何代码时，都强烈建议同时为该代码编写测试。对于 Python 测试，可以使用 pytest 和 pytest-runner 库。在虚拟环境中安装库：

```python
pip install pytest
pip install pytest-runner
pip install numpy
```

让我们为 haversine 函数创建一个小测试。复制以下内容并将其放入 `test_myfunctions.py` 文件中：

```python
from mypythonlib import myfunctions


def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008,
                                 13.404954) == 945793.4375088713
```

最后，让我们创建一个 `setup.py` 文件，它将帮助我们构建库。`setup.py` 的内容如下所示：

```python
from setuptools import find_packages, setup

setup(
    name='mypythonlib',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
)
```

## 第 5 步：设置您想要创建的包

虽然原则上 `find_packages()` 可以不带任何参数使用，但这可能会导致包含不需要的包。 所以，我们可以这么来写：

```python
setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
)
```

## 第 6 步：设置库所需的要求

注意，当你的项目被其他人作为依赖项安装时，pip 不会使用`requirements.yml`/ `requirements.txt`。 通常，为此，您必须在文件的 `install_requires` 和 `tests_require` 参数中指定依赖项 `setup.py`。 `Install_requires` 应该仅限于绝对需要的软件包列表。这是因为您不想让用户安装不必要的软件包。 **另请注意，你不需要列出属于标准 Python 库的包。** 如果你用的是 Python 自带的库，是可以不用写的，并且保证这个库是一直到现在的 Python 本版的可以使用的。 也许你还记得我们 `pytest` 、`numpy` 之前安装过这个库。当然，你不想在其中添加 `pytest` 依赖项。这个包的用户不需要它。为了仅在运行测试时自动安装它，您可以将以下内容添加到您的 `setup.py`：

```python
from setuptools import find_packages, setup

setup(
    name='mypythonlib', # 应用名
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0', # 版本号
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=["numpy==1.21.2"], # 依赖列表
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
)
```

运行：将执行存储在 “tests” 文件夹中的所有测试。

```python
python setup.py pytest
```

```python
(venv) aiyc@aiyc:~/Linux_Code/mypythonlibrary$ python setup.py pytest
running pytest
running egg_info
creating mypythonlib.egg-info
writing mypythonlib.egg-info/PKG-INFO
writing dependency_links to mypythonlib.egg-info/dependency_links.txt
writing requirements to mypythonlib.egg-info/requires.txt
writing top-level names to mypythonlib.egg-info/top_level.txt
writing manifest file 'mypythonlib.egg-info/SOURCES.txt'
reading manifest file 'mypythonlib.egg-info/SOURCES.txt'
writing manifest file 'mypythonlib.egg-info/SOURCES.txt'
running build_ext
================================================================ test session starts =================================================================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/aiyc/Linux_Code/mypythonlibrary
collected 1 item                                                                                                                                     

tests/test_myfunctions.py .  
```

## 第 7 步：构建你的库

现在所有内容都已准备就绪，我们要构建我们的库。确保您当前的工作目录是 `/path/to/mypythonlibrary`（因此是项目的根文件夹）。在您的命令提示符中，运行：

```python
python setup.py bdist_wheel
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0a0056b4457c4de8adbe6462a07482a9.png) 您的轮文件存储在现在创建的 “dist” 文件夹中。您可以使用以下方法安装您的库：

```python
pip install /path/to/wheelfile.whl
```

请注意，您还可以将您的库发布到您工作场所内联网上的内部文件系统，或发布到官方 PyPI 存储库并从那里安装它。 安装 Python 库后，您可以使用以下命令导入它：

```python
import mypythonlib
from mypythonlib import myfunctions
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh

![在这里插入图片描述](https://img-blog.csdnimg.cn/9eda5bc0126644718436e3daa7d655f7.png)
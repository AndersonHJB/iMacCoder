---
title: 五分钟内的 Python 虚拟环境
tags: []
id: '1709'
categories:
  - - 技术杂谈
date: 2021-05-24 15:47:31
---

\[toc\] 你好，我是悦创。 在 Python 中，虚拟环境用于将项目彼此隔离（例如，如果它们需要相同库的不同版本）。它们使您可以在没有管理员特权的情况下安装和管理软件包，并且不会与系统软件包管理器发生冲突。它们还允许在其他具有相同依赖项的环境中快速创建环境。 对于任何 Python 开发人员而言，虚拟环境都是至关重要的工具。并且，这是一个非常简单的工具。 让我们开始吧！Let’s get started!

## 安装

[venv](https://docs.python.org/3/library/venv.html) 模块是可用于创建虚拟环境的最佳工具 ，它是自 Python 3.3 以来标准库的一部分。 `venv` 是内置于. Python 中的，大多数用户不需要安装任何东西。但是，Debian / Ubuntu 用户将需要运行安装命令，才能使其运行（由于 Debian 默认不安装某些需要的组件）。

```linux
sudo apt-get install python3-venvvenv
```

替代（也是原始的，并且以前是标准的）虚拟环境工具是 [virtualenv](https://virtualenv.pypa.io/)。它可与 Python 2.7 一起使用，并具有一些额外的功能（通常不需要）。virtualenv 可以与系统软件包管理器一起安装，或者。`pip install --user virtualenv` **使用哪一个？** 先使用： `venv` 。两种工具以相似的方式实现相同的目标。如果其中一个不起作用，则可以尝试另一个，这样可能会更好。

> （术语注释：大多数情况下，两个工具的名称都是可互换使用的，在创建 stdlib 工具之前，“ venv” 通常被用作 “ virtualenv” 的缩写）

## 创建

我们要创建一个名为： env 的虚拟环境，所以我们在我们目标的路径下，执行如下命令：

```linux
Linux：$ python3 -m venv env
Windows：> python -m venv env
```

或者，如果您使用的是 virtualenv 来创建虚拟环境的话：

```linux
$ python3 -m virtualenv env
> python -m virtualenv env
```

之后，您将得到一个名为 env 的文件夹，其中包含名为 bin（Scripts 在Windows 上—包含由软件包安装的可执行文件和脚本，包括 python），lib（包含代码）和 include（包含 C 标头）的文件夹。 这两种工具安装 pip 和 setuptools ，但 ven v 不出货 wheel。此外，默认版本或多或少已经过时。让我们快速升级它们：

```linux
$ env/bin/python -m pip install --upgrade pip setuptools wheel
> env\Scripts\python -m pip install --upgrade pip setuptools wheel
```

## 在哪里存储虚拟环境？

尽管这些工具，使您可以将虚拟环境放置在系统中的任何位置，但这并不是可取的事情。有两种选择：

1.  对他们有一个全局环境的地位，例如`~/virtualenvs`。
2.  将它们存储在每个项目的目录中，例如`~/git/foobar/.venv`。

第一个选项可能更易于管理，有些工具可以帮助您进行管理（例如`virtualenvwrapper`，shell 自动激活脚本或以下所述的 `workon` 功能）。 第二个选项同样易于使用，但有一个警告-您必须将 venv 目录添加到 `.gitignore` 文件中（或者`.git/info/exclude` 如果您不想将更改提交到`.gitignore` ），因为您不希望在存储库中添加它（这是二进制膨胀，仅在您的计算机上有效）。 如果选择了全局虚拟环境存储选项，则可以使用以下简短函数（将其放入`.bashrc`//`.zshrc` 配置文件中）来获得激活环境的简单方法（通过运行`workon foo`）。 `virtualenvwrapper` 也有一个 `workon` 功能，尽管我认为这并不是 `virtualenvwrapper`真正必要和有用的，但该 `workon` 功能很方便，因此，这里有一种无需 `virtualenvwrapper` 以下操作的方法 ：

```bash
 export WORKON_HOME=~/virtualenvs

 function workon {
     source "$WORKON_HOME/$1/bin/activate"
 }
```

对于 Windows PowerShell 风扇，这是一个 `workon.ps1` 脚本：

```bash
 $WORKON_HOME = "$home\virtualenvs"
 $venv = $args[0]
 $cmd = "$WORKON_HOME\$venv\Scripts\activate.ps1"
 & $cmd
```

## 使用虚拟环境

有三种方式（在 Shell 中）以交互方式使用虚拟环境：

*   activation（`source env/bin/activate` 在 \* nix `env\Scripts\activate` 上运行；在Windows上 运行）-尽管有时可能无法正常工作，但它简化了工作并减少了键入次数。（安装脚本后，可能需要在 \* nix上使用它们。）`hash -r`
*   直接执行 `env/bin/python`（`env\Scripts\python`）和其他脚本，因为仅更改激活 `$PATH` 和一些帮助程序变量-这些变量对于操作不是强制性的，运行正确的变量是必需的 `python`，并且该方法是故障安全的。
*   [在子外壳中](https://gist.github.com/datagrok/2199506)（IMO，这是糟糕的UX）

无论使用哪种方法，都必须记住，不做任何这些事情，您仍将使用系统 Python 。 对于非交互式工作（例如 crontab 条目，系统服务等），激活和子外壳不是可行的解决方案。在这种情况下，您必须始终使用 Python 的完整路径。 这是一些用法示例（路径可以是相对的）：

```cmd
## *nix, activation ##
$ source /path/to/env/bin/activate
(env)$ pip install Django
(env)$ deactivate

## *nix, manual execution ##
$ /path/to/env/bin/pip install Django

## Windows, activation ##
> C:\path\to\env\Scripts\activate
(venv)> pip install Django
(venv)> deactivate

## Windows, manual execution ##
> C:\path\to\env\Scripts\pip install Django

## Windows, updating pip/setuptools/wheel ##
> C:\path\to\env\Scripts\python -m pip install -U pip setuptools wheel
```

相同的原则适用于运行 Python 本身或程序包安装的任何其他脚本。（使用 Django 时`manage.py`，`./manage.py` 需要激活才能调用它 ，也可以运行 `venv/bin/python manage.py`。）

## 移动/重命名/复制环境？

如果尝试复制或重命名虚拟环境，则会发现复制的环境不起作用。这是因为虚拟环境与创建它的 Python 以及创建它的位置密切相关。（的“可重定位”选项`virtualenv`不起作用，已弃用。） 但是，这很容易解决。无需移动/复制，只需在新位置创建一个新环境即可。然后，`pip freeze > requirements.txt` 在旧环境中运行以创建在其中安装的软件包的列表。这样，您就可以在新环境中运行以从保存的列表中安装软件包。（当然，您可以 在计算机之间进行复制。在许多情况下，它就可以工作；有时，您可能需要进行一些修改才能删除特定于 OS 的内容。）`pip install -r requirements.txt`

```cmd
$ oldenv/bin/pip freeze > requirements.txt
$ python3 -m venv newenv
$ newenv/bin/pip install -r requirements.txt
(You may rm -rf oldenv now if you desire)
```

请注意，在 Python 升级之后可能还需要重新创建虚拟环境，因此保持`requirements.txt` 虚拟环境的最新状态可能很方便 （对于许多项目，将其放入存储库）。 要 `requirements.txt` 以更复杂但仍更简单的方式管理这些文件，您可能会对[pip工具](https://github.com/jazzband/pip-tools) 感兴趣

## 常见问题

### 我正在使用 virtualenv。我是否需要为要使用它的每个 Python 安装它？

在大多数情况下，您可以用来指定其他 Python 版本，但是使用某些 Python 版本组合，该方法可能会失败。（该模块与其安装的 Python 版本相关。）`virtualenv -p pythonX env``venv`

### 我是系统上的唯一用户。我仍然需要虚拟环境吗？

是的，你需要。首先，迟早您仍需要在项目之间进行分隔。此外，如果要使用 pip 在系统范围内安装软件包，则可能最终导致系统软件包管理器和 pip 安装的软件包之间发生冲突。因此，运行 `sudo pip` 永远不是一个好主意。

### 我正在使用 Docker。我仍然需要虚拟环境吗？

在那种情况下，它们仍然是一个好主意。它们可以保护您免受 OS 映像可能包含的任何不良系统范围的 Python 软件包的影响（其中一个流行的基本 OS 就是著名的）。它们不会带来任何额外的开销，同时允许拥有一个干净的环境并能够在 Docker 外部重新创建它（例如，用于没有 Docker 的本地开发）

### 那 Pipenv 呢？

Pipenv是一个依赖项管理工具。它与大多数工作流程不兼容，并且存在许多问题。在我看来，这是不值得使用的（此外，它是否是官方推荐的工具？事实并非如此。） 考虑改用[pip-tools](https://github.com/jazzband/pip-tools)。
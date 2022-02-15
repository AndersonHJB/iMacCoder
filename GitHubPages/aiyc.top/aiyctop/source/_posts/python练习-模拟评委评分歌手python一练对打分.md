---
title: 'python练习-模拟评委评分歌手,Python,一练,对,打分'
tags: []
id: '1335'
categories:
  - - Python小练习
date: 2021-01-07 10:55:50
---

在布塔学院的某次十佳歌手比赛中，7位评委对歌手打分，计算总分时，需要去掉一个最高分，去掉一个最低分，然后输出总分和平均分。要求帮助评委会编写歌手打分程序，输入7名评委的打分，输出总分和平均分。最终效果如图所示。 ![在这里插入图片描述](https://images.gitbook.cn/7bcd0360-5093-11eb-8005-5904c8467e3a) 示例代码如下：

```python
if __name__ == '__main__':
    # 1.打印标题和分割线
    print("\033[1;35m  畅想布塔学院十佳歌手打分程序")
    print("===================================\033[0m")
    # 2.使用input函数录入7名裁判的打分
    score_str = input("请输入7名裁判的打分，用英文逗号间隔分数: \n")
    # 3.将分数使用,进行切割 得到一个列表
    # ['78.5', '67.2', '89', '98.7', '88', '99', '77']
    temp_score_list = score_str.split(",")
    # 注意: 此时列表中的分数仍是字符串 所有我们要借助map函数将列表中的每个元素转换为数值型的数据
    # [78.5, 67.2, 89.0, 98.7, 88.0, 99.0, 77.0]
    score_list = list(map(float, temp_score_list))
    # 4.分别拿到最高分和最低分
    max_score = max(score_list)
    min_score = min(score_list)
    # 5.打印输出
    print(f"去掉一个最低分: {min_score}")
    score_list.remove(min_score)
    print(f"去掉一个最高分: {max_score}")
    score_list.remove(max_score)
    # 输出有效得分
    print(f"该歌手的有效打分为: {score_list}")
    # 输出最后得分 最后得分保留一位小数
    print("该歌手的得分为: %.1f" % (sum(score_list) / len(score_list)))

```
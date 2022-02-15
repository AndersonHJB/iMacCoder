---
title: jquery第三章练习三（制作京东常见问题分类页面）
tags: []
id: '1313'
categories:
  - - JavaScript
date: 2020-12-24 17:25:28
---

## js 代码及要求如下：

```JavaScript
$(document).ready(function () {
    /* 鼠标移至“联系客服”，二级菜单以”slow“速度显示；当鼠标离开时，二
  级菜单以“fast”速度隐藏 */
    $(".menu-btn").hover(
        function () {
            $(this).next().show("slow");
        },
        function () {
            $(this).next().hide("fast");
        }
    );

    /*  鼠标一级菜单时，使用 slideDown( ) 实现二级菜单以“slow”速度显示；
  当鼠标再次单击一级菜单时，使用 slideUp( ) 实现二级菜单以”slow“速度隐
  藏 */

    let count = 0;
    $(".nav dt").click(function () {
        count++;
        if (count % 2 !== 0) $(this).nextAll().slideDown("slow");
        else {
            $(this).nextAll().slideUp("slow");
        }
    });
});
```
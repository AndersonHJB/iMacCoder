---
title: HTML5制作3D圣诞树效果
tags: []
id: '2118'
categories:
  - - uncategorized
date: 2021-12-24 15:47:46
---

你好，我是悦创。 本例给大家演示一个使用 HTML5 制作的 3D 圣诞树，非常的漂亮。我们可以通过这个例子将 HTML5 Canvas 的绘图技术深入的学习一下。 效果图如下： ![在这里插入图片描述](https://img-blog.csdnimg.cn/16950e19aee745919f6438e551215da2.png) [在线演示](https://github.aiyc.top/aiyccdn/html/christmas_trees.html) https://github.aiyc.top/aiyccdn/html/christmas\_trees.html 完整代码如下：

```markup
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
<html>
<head>
<meta charset="utf-8" >
<style>
html, body { width: 100%; height: 100%; margin: 0; padding: 0; border: 0; }
div { margin: 0; padding: 0; border: 0; }
.nav { 
        position: absolute; 
        top: 0; 
        left: 0; 
        width: 100%; 
        height: 27px; 
        background-color: white; 
        color: black; 
        text-align: center; 
        line-height: 25px;
        }
a { color: black; text-decoration: none; border-bottom: 1px dashed black; }
a:hover { border-bottom: 1px solid red; }

.previous { float: left; margin-left: 10px; }
.next { float: right; margin-right: 10px; }

.green { color: green; }
.red { color: red; }
textarea { width: 100%; height: 100%; border: 0; padding: 0; margin: 0; padding-bottom: 20px; }
.block-outer { float: left; width: 22%; height: 100%; padding: 5px; border-left: 1px solid black; margin: .block-inner { height: 68%; }
.one { border: 0; }
</style>
</head>
<body marginwidth="0" marginheight="0">
<canvas id="c" height="356" width="446">
<script>
    var collapsed = true;
    function toggle() {
        var fs = top.document.getElementsByTagName('frameset')[0];
        var f = fs.getElementsByTagName('frame');
        if (collapsed) {
            fs.rows = '250px,*';
            // enable resizing of frames in firefox/opera
            fs.noResize = false;
            f[0].noResize = false;
            f[1].noResize = false;
        } else {
            fs.rows = '30px,*';
            // disable resizing of frames in firefox/opera
            fs.noResize = true;
            f[0].noResize = true;
            f[1].noResize = true;
        }
        collapsed = !collapsed;
    }

</script>
<script>
        var b = document.body;
        var c = document.getElementsByTagName('canvas')[0];
        var a = c.getContext('2d');
        document.body.clientWidth; // fix bug in chrome.
</script>
<script>
// start of submission //
M=Math;Q=M.random;J=[];U=16;T=M.sin;E=M.sqrt;for(O=k=0;x=z=j=i=k<200;)with(M[k]=k?c.cloneNode(0):c){width=height=k?32:W=446;with(getContext('2d'))if(k>10!k)for(font='60px Impact',V='rgba(';I=i*U,fillStyle=k?k==13?V+'205,205,215,.15)':V+(147+I)+','+(k%2?128+I:0)+','+I+',.5)':'#cca',i<7;)beginPath(fill(arc(U-i/3,24-i/2,k==13?4-(i++)/2:8-i++,0,M.PI*2,1)));else for(;x=T(i),y=Q()*2-1,D=x*x+y*y,B=E(D-x/.9-1.5*y+1),R=67*(B+1)*(L=k/9+.8)>>1,i++<W;)if(D<1)beginPath(strokeStyle=V+R+','+(R+B*L>>0)+',40,.1)'),moveTo(U+x*8,U+y*8),lineTo(U+x*U,U+y*U),stroke();for(y=H=k+E(k++)*25,R=Q()*W;P=3,j<H;)J[O++]=[x+=T(R)*P+Q()*6-3,y+=Q()*U-8,z+=T(R-11)*P+Q()*6-3,j/H*20+((j+=U)>H&Q()>.8?Q(P=9)*4:0)>>1]}setInterval(function G(m,l){A=T(D-11);if(l)return(m[2]-l[2])*A+(l[0]-m[0])*T(D);a.clearRect(0,0,W,W);J.sort(G);for(i=0;L=J[i++];a.drawImage(M[L[3]+1],207+L[0]*A+L[2]*T(D)>>0,L[1]>>1)){if(i==2e3)a.fillText('Merry Christmas!',U,345);if(!(i%7))a.drawImage(M[13],((157*(i*i)+T(D*5+i*i)*5)%W)>>0,((113*i+(D*i)/60)%(290+i/99))>>0);}D+=.02},1)
// end of submission //
</script>
</body>
</html>
```

> AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。QQ、微信在线，随时响应！V：Jiabcdefh，公众号：AI悦创

![在这里插入图片描述](https://img-blog.csdnimg.cn/bcd7c66f856c40b0a024be6e2a7b4b82.png)
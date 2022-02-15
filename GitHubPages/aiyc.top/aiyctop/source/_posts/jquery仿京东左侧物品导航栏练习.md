---
title: jQuery仿京东左侧物品导航栏练习
tags: []
id: '1311'
categories:
  - - JavaScript
date: 2020-12-24 16:59:47
---

## 1、HTML 和样式部分

```css
<style type="text/css">
    html{color:#666;background:#FFF;}
    body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,i,fieldset,legend,input,textarea,p,blockquote,th,td{margin:0;padding:0;}
    body{font:12px/1.3 arial,helvetica,clean,sans-serif,\5b8b\4f53;}
    h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:normal}
    table{border-collapse:collapse;border-spacing:0;}
    img{border:none;}
    a{text-decoration:none; color:#666;}
    ul,li{list-style-type:none;}
    .nav-con{width: 1210px;margin: 0 auto;height: 44px;position: relative;}
    .nav-con-left{float: left; position: relative; width: 210px;height: 44px;z-index: 10;background: #B1191A;overflow: visible;}
    .nav-con-lefttext a{display: block;width: 190px;height: 44px;padding: 0 10px;color: white;font: 400 15px/44px "microsoft yahei";}
    .nav-variety{height: 94px;background: #c81623;}
    .thing-variety li{border-left: 1px solid #b61d1d;position: relative;z-index: 10;height: 31px;color: white;}
    .thing-variety .thname{height: 31px;}
    .thing-variety .thname h4{position: absolute;z-index: 11;height: 31px;line-height: 30px;font-size: 14px;font-weight: 400;padding: 0 10px;}
    .thing-variety .thname h4 a{color: white;}
    .thing-variety .thname span{position: absolute;right: 14px;top: 9px;width: 4px;height: 14px;  font: 400 9px/14px consolas;z-index: 1;}
    .thing-variety .showLi{background: #F7F7F7;}
    #things .showA{color: #b61d1d;}
    #things .showSpan{display: none;}
    /*****************商品分类*****************/
    .dropdown{width: 999px;position: absolute;left: 209px;top: 43px;background: #F7F7F7;border: 1px solid #b61d1d;overflow: hidden;}
    .item-brands{float: right;display: inline;width: 168px;margin: 19px 20px 10px 0;}
    .item-brands a{float: left;display: inline;margin: 1px 0 0 1px;}
    .item-brands img,.item-promotions img{border: 0;vertical-align: top;}
    .item-promotions{float: right;display: inline;width: 168px;margin-right: 20px;}
    .item-promotions a{display: block;margin-bottom: 1px;}
    .item-channels{width: 790px;float: left;display: inline;height: 24px;padding: 20px 0 0 20px;background: #F7F7F7;overflow: hidden;}
    .item-channels .channels a{float: left;display: inline-block;padding: 0 0 0 8px;margin-right: 10px;line-height: 24px;
        background: #7c7171;color: white;font-size: 12px;}
    .item-channels .channels a span{display: inline-block;margin-left: 8px;width: 23px;height: 24px;font: 400 9px/24px consolas;background: #5c5252;text-align: center; }
    .item-channels .channels a:hover{background:  #c81623;}
    .item-channels .channels a:hover span{background:#b61d1d; }
    .subitems{width: 790px;float: left;padding: 6px 0 1006px 20px;margin-bottom: -1000px;background: #F7F7F7;min-height: 409px;}
    .subitems dl{width: 100%;line-height: 2em;overflow: hidden;font-size: 12px;}
    .subitems dl dt{position: relative;float: left;width: 54px;padding: 8px 30px 0 0;text-align: right;font-weight: 700;font-size: 12px;}
    .subitems dl dt span{position: absolute;top: 13px;right: 18px;width: 4px;height: 14px;font: 400 9px/14px consolas;}
    .subitems dl dd{border-top: 1px solid #eee;width: 620px;padding: 6px 0;overflow: hidden;}
    .subitems dl dd a{float: left; padding: 0 8px;margin: 4px 0;line-height: 16px;height: 16px;border-left: 1px solid #e0e0e0;}
    .subitems .sub1 dd{border-top: none;}
    .subitems dl dt a:hover{color: #b61d1d;}
    .subitems dl dd a:hover{ color: #b61d1d;}
    .hiden{display: none;}

</style>
```

```markup
<div class="nav">
    <div class="nav-con">
        <div class="nav-con-left">
            <div class="nav-con-lefttext">
                <a href="#">全部商品分类</a>
            </div>
            <div class="nav-variety" id="things">
                <ul class="thing-variety" id="variety">
                    <li class="tab-item">
                        <div class="thname">
                            <h4><a href="#">图书、音像、电子书</a></h4>
                            <span>></span>
                        </div>
                    </li>
                    <li class="tab-item">
                        <div class="thname">
                            <h4><a href="#">彩票、旅行、充值、票务</a></h4>
                            <span>></span>
                        </div>
                    </li>
                    <li class="tab-item">
                        <div class="thname">
                            <h4><a href="#">理财、众筹、白条、保险</a></h4>
                            <span>></span>
                        </div>
                    </li>
                </ul>
                <div class="dropdown hiden">
                    <div class="fmaint clear hiden">
                        <div class="item-brands">
                            <a href="#"><img src="img/ib1.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib2.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib3.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib4.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib5.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib6.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib7.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib8.jpg" alt="" width="83" height="35"/></a>
                        </div>
                        <div class="item-channels">
                            <div class="channels">
                                <a href="#">图书频道 <span>></span></a>
                                <a href="#">音响 <span>></span></a>
                                <a href="#">电子书 <span>></span></a>
                                <a href="#">图书榜 <span>></span></a>
                                <a href="#">音乐榜 <span>></span></a>
                                <a href="#">文娱众筹馆 <span>></span></a>
                            </div>
                        </div>
                        <div class="subitems">
                            <dl class="sub1">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub2">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">智能硬件</a>
                                    <a href="#" target="_blank">流行文化</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">公益</a>
                                    <a href=#" target="_blank">其他权益众筹</a>
                                </dd>
                            </dl>
                            <dl class="sub3">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub4">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub5">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub6">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub7">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub8">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub9">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub10">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub11">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                        </div>
                        <div class="item-promotions">
                            <a href="#"><img src="img/ib9.jpg" alt="" width="168" height="134"/></a>
                            <a href="#"><img src="img/ib10.jpg" alt="" width="168" height="134"/></a>
                        </div>
                    </div>
                    <div class="fmaint clear hiden">
                        <div class="item-brands">
                            <a href="#"><img src="img/ib1.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib2.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib3.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib4.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib5.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib6.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib7.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib8.jpg" alt="" width="83" height="35"/></a>
                        </div>
                        <div class="item-channels">
                            <div class="channels">
                                <a href="#">充值缴费 <span>></span></a>
                                <a href="#">京东彩票 <span>></span></a>
                                <a href="#">培训教育 <span>></span></a>
                                <a href="#">优选机票 <span>></span></a>
                                <a href="#">火车票 <span>></span></a>
                            </div>
                        </div>
                        <div class="subitems">
                            <dl class="sub1">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub2">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">智能硬件</a>
                                    <a href="#" target="_blank">流行文化</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">公益</a>
                                    <a href=#" target="_blank">其他权益众筹</a>
                                </dd>
                            </dl>
                            <dl class="sub3">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub4">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub5">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub6">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                        </div>
                        <div class="item-promotions">
                            <a href="#"><img src="img/ib9.jpg" alt="" width="168" height="134"/></a>
                            <a href="#"><img src="img/ib10.jpg" alt="" width="168" height="134"/></a>
                        </div>
                    </div>
                    <div class="fmaint clear hiden">
                        <div class="item-brands">
                            <a href="#"><img src="img/ib1.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib2.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib3.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib4.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib5.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib6.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib7.jpg" alt="" width="83" height="35"/></a>
                            <a href="#"><img src="img/ib8.jpg" alt="" width="83" height="35"/></a>
                        </div>
                        <div class="item-channels">
                            <div class="channels">
                                <a href="#">金融首页 <span>></span></a>
                                <a href="#">尖er货 <span>></span></a>
                                <a href="#">奇趣日报 <span>></span></a>
                                <a href="#">大牌免息 <span>></span></a>
                                <a href="#">财发现 <span>></span></a>
                            </div>
                        </div>
                        <div class="subitems">
                            <dl class="sub1">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub2">
                                <dt><a href="#">众筹<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">智能硬件</a>
                                    <a href="#" target="_blank">流行文化</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">公益</a>
                                    <a href=#" target="_blank">其他权益众筹</a>
                                </dd>
                            </dl>
                            <dl class="sub3">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub4">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub5">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                            <dl class="sub6">
                                <dt><a href="#">理财<span>></span></a></dt>
                                <dd>
                                    <a href="#" target="_blank">京东小金库</a>
                                    <a href="#" target="_blank">票据理财</a>
                                    <a href="#" target="_blank">基金理财</a>
                                    <a href="#" target="_blank">定期理财</a>
                                    <a href=#" target="_blank">固收理财</a>
                                    <a href="#" target="_blank">妈妈理财</a>
                                </dd>
                            </dl>
                        </div>
                        <div class="item-promotions">
                            <a href="#"><img src="img/ib9.jpg" alt="" width="168" height="134"/></a>
                            <a href="#"><img src="img/ib10.jpg" alt="" width="168" height="134"/></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
</div>
```

## HTML 用的图片没贴，不影响效果

## 2、jQuery 部分

```javascript
$(function(){
    var $tabItem = $('#things .tab-item');//获得导航条部分
    var $fmaint = $('#things .fmaint');//获得内容部分
    var $at = $('#variety a');
    var $spant = $('#variety span');
    var $dropdown = $('.dropdown');
    $tabItem.each(function (index) {//用each方法给每个导航条添加鼠标移入移除事件
        $(this).mouseover(function () {
            $dropdown.removeClass('hiden');
            $(this).addClass('showLi');
            $fmaint.eq(index).removeClass('hiden').siblings().addClass('hiden');
            $at.eq(index).addClass('showA');
            $spant.eq(index).addClass('showSpan');
        }).mouseout(function () {
            $dropdown.addClass('hiden');
            $(this).removeClass('showLi');
            $fmaint.eq(index).addClass('hiden');
            $at.eq(index).removeClass('showA');
            $spant.eq(index).removeClass('showSpan');
        });
    });
    $fmaint.each(function (index) {//用each方法给每个内容添加鼠标移入移除事件
        $(this).mouseover(function () {
            $dropdown.removeClass('hiden');
            $tabItem.eq(index).addClass('showLi');
            $fmaint.eq(index).removeClass('hiden').siblings().addClass('hiden');
            $at.eq(index).addClass('showA');
            $spant.eq(index).addClass('showSpan');
        }).mouseout(function () {
            $dropdown.addClass('hiden');
            $at.eq(index).removeClass('showA');
            $spant.eq(index).removeClass('showSpan');
            $tabItem.eq(index).removeClass('showLi');
            $fmaint.eq(index).addClass('hiden');
        });
    });
})

```
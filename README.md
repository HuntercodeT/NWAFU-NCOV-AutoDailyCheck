# NWAFU-NCOV-AutoDailyCheck

西北农林科技大学每日健康打卡自动化脚本

![AUR](https://img.shields.io/badge/license-MIT--License%202.0-green.svg)
![GitHub stars](https://img.shields.io/github/stars/HuntercodeT/NWAFU-NCOV-AutoDailyCheck.svg?style=social&label=Stars)
![GitHub forks](https://img.shields.io/github/forks/HuntercodeT/NWAFU-NCOV-AutoDailyCheck.svg?style=social&label=Fork)

利用python中的selenium包实现健康打卡，若对您有所帮助请点个start吧！

## 声明

本项目为Python开源项目，仅用于学习交流使用。
使用者请遵守相关政策规定。对一切非法使用的后果，我们概不负责。
若本项目对您有困扰，请联系本人删除。

## 遵守防疫规定，做好个人防护。

## 概述

我有个朋友在西农读书，最近朋友认为每天打卡属实有点麻烦，特别是又没到处跑天天在学校里还要打卡，不打卡还被通报批评，这就很烦。
于是拜托我写了这么一个程序，我看了一些Github上别的学校的健康打卡程序，普遍使用的是Github Action 执行，这当然更方便，但是我看了一下西农打卡页面的源码，其中有这么一句“Get ipLocation failed”，我觉得为了安全起见，还是放在本地运行比较安全，这样ip和地理位置都是在学校的就不怕被查水表了。
当然学习交流嘛，如果有同学想要线上版的话，后期我或许会传上来，供大家交流学习，接口都抓到了，就差测试了，毕竟我只有我朋友的账号不够测试。

## 使用指南

### 准备工作
1. 下载本仓库的py文件到你的电脑上
2. 安装python和所需模块
    还是想重申，本项目仅作学习交流使用，故这一块就不介绍了，自行百度吧，本脚本需要Selenium,time模块，如果需要微信推送，则还需要requests模块。
3. edge驱动安装

    > [Microsoft Edge Driver - Microsoft Edge Developer](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
    >
    > 点击上方网址，下载和自己电脑对应的版本就好啦
    >
    > 然后放到本程序同一文件夹下
    >
4. Pushplus推送相关

    > 我感觉这是最简单的推送方式了，还不要钱
    >
    > [Pushplus(推送加)官网](http://pushplus.hxtrip.com/)
    >
    > 点击上方网站，微信登录后点击一对一推送获取Token
    >

### 正式开始

> 学号
>
> 密码
>
> 浏览器驱动路径
>
> 推送Token(可以没有，但前三个必须要)

将这四个信息填进代码最后几行的对应位置，替换掉我写的初始参数，单引号不要删，这些都是字符型数据

这样就可以运行啦

### 本地自动化

看到这你可能会想这有什么用，还不是得自己点击运行才打卡，更麻烦了不是

**当然不能白干啦**

> [windows设置定时自动运行python脚本](https://www.pianshen.com/article/13581115210/)

点击上方链接，按图示操作设置定时运行，建议下载本脚本后手动运行一次看看自己填的信息有没有问题，然后再设置计划任务。

## 注意事项

本脚本设计初衷并不是为了逃避防疫，对抗防疫工作，只是朋友觉得每天在学校还要打卡很麻烦，所以希望有这么一个脚本来取代重复性工作，因此本脚本并未涉及不在校等等特殊模块，只适用于目前在学校并且主观上无违规意图的同学交流学习。

本脚本属于初次发布，且只经过一个账号的测试，因此难免碰到问题，若有脚本本身问题请提issue，其他问题请尽量自行百度。

最后，祝早日战胜疫情，摆脱打卡。

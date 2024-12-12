# 草原探险服务器玩法介绍
## 本文作者：youpaishidifu

# menu
1. 领地系统(dom)
2. 地图画(tomap)
3. home(home)
4. 返回上一个位置(back)

## 一、领地系统(dom)
### 1. 创建领地
- 有两种方式创建领地：
1. 使用普通的弓箭(小白掉落的那种)，对着建筑，`左右键选取A、B`两点，然后根据指令提示使用`/dom create [名字]`创建
2. 在聊天框输入`dom`，点击`创建领地`，系统会根据当前环境自动创建一个(最大9x9x9)的领地，若太大、太小可进行调整
![](https://img.yunr.us.kg/api/cfile/AgACAgUAAyEGAASO2xA4AAMfZxeIgD_4AAEJx8fUKVoq66tpf1cvAAKdwDEbmWy5VP0Dt3dWLhESAQADAgADeQADNgQ)

### 2. 扩建&缩小
指令：
```
/dominion expand [大小] [领地名] //扩建领地
/dominion contract [大小] [领地名] //缩小领地
```
### 3. 转让&删除
指令：
```
/dominion give [领地名] [玩家名] force //转让领地
/dominion delete [领地名] force //删除领地
```
**请注意，领地转让&删除均为不可撤销的操作，请谨慎操作**

### 4. 领地成员&访客配置
- 成员配置<br>
输入指令`/dom`，点击`我的领地-领地名-管理`，即可配置你的领地成员，点击`添加成员-搜索成员`把玩家名字输入进去，即可自动添加。
![](https://img.yunr.us.kg/api/cfile/AgACAgUAAyEGAASO2xA4AAMgZxeSl_MIu31pk_vWZ_Yns3vq8pYAArLAMRuZbLlU52PNMsfSjvABAAMCAAN5AAM2BA)

![](https://img.yunr.us.kg/api/cfile/AgACAgUAAyEGAASO2xA4AAMhZxeTZ-bWS2pWwGdrU5mYL9CXVSwAArPAMRuZbLlUKdAHq7hBYrMBAAMCAAN5AAM2BA)

![](https://img.yunr.us.kg/api/cfile/AgACAgUAAyEGAASO2xA4AAMiZxeTbDDOD_ptPVxTGuY3mHnKFT4AArXAMRuZbLlUhItX67TqpIcBAAMCAAN5AAM2BA)

当赋予玩家`领地管理员`身份时，玩家将拥有除转让删除以外的所有权限，包括添加成员、删除成员(非管理员)权限等


- 访客配置<br>

输入指令`/dom`，点击`我的领地-领地名-管理-访客权限`即可编辑访客(非领地成员)的权限
![](https://img.yunr.us.kg/api/cfile/AgACAgUAAyEGAASO2xA4AAMjZxeVxPylHEAxz3X31wgBSXS3aHUAArjAMRuZbLlUwjr0DqMK4RgBAAMCAAN4AAM2BA)

领地成员权限＞访客权限，添加成员进入领地成员时，默认给予访客权限的同等权限，领地主可以任意配置每个成员的权限。

### 5. 领地传送
使用指令`/dom tp [名字]`传送到领地，请确保传送地点周边安全，否则可能会取消传送。在地狱、末地我们建议您使用`/sethome`来设置传送点，而不使用领地传送。<br>传送会在5秒内进行，在传送期间，不能骑乘载具，不能被骑乘。否则会`显示传送成功但实际还在原地`的情况


## 二、地图画(tomap)

### 免责声明

1. **版权方责任声明**<br>
- {% em %}本服务器运营方仅提供技术支持和平台服务，对于用户自行上传的任何音视频图片及其他带有版权的资料，运营方不承担任何直接或间接的版权责任。<br> - 用户应确保其上传的内容不侵犯任何第三方的合法权益，包括但不限于版权、商标权、专利权等知识产权，并自行审查上传内容的合法性。[%endem%]

2. **纠纷处理**<br>

- {% em %}若因用户上传的内容引发任何纠纷，包括但不限于版权侵权纠纷、名誉权纠纷等，运营方有权采取必要的措施进行处理，但运营方不对此类纠纷承担任何责任。<br>
- 用户应自行承担因上传内容所引发的任何法律责任及后果，若运营方因此造成损失，有权向用户追偿。<br>
- 运营方在收到权利方的合法通知后，有权立即删除或采取其他必要措施处理侵权内容。{% endem %}<br>

3. **法律法规遵守**
- **本声明的制定符合中华人民共和国的相关法律法规的规定，运营方将严格遵守法律法规的要求，维护网络环境的合法、健康和有序。**

### 地图画的使用：
- 为确保图片质量，请您使用服务器指定图床：[https://img.ypshidifu.cn](https://img.ypshidifu.cn/)，[https://img.yunr.us.kg/](https://yunr.us.kg/)并控制图片大小为128的倍数。因为在Mc中，一张地图的大小刚好是128X128，能完整填充展示框。请注意两个图床二选一！若都无法生成地图画，请[**联系管理员**](https://qun.ypshidifu.cn/)

使用指令`/tomap Url`获取图片，并摆出对应大小的展示框。如果是2x2，则摆出4个展示框，如果是3x3则摆出6个展示框，以此类推。尺寸越大，所需时间就越长.
将图片上传图床后，会获得一个Url，将该url替换本文的url即可

## 三、home&back

### home
可用指令：
```
/home [数字/字母] //传送到对应地点
/home bed //传送到床
/sethome [数字/字母] //设置传送点
```
使用指令`/sethome [字母/数字]`设置传送点，使用指令`/home [字母/数字]`传送至该传送点。`/home bed`快速返回重生点(床)

### back
使用指令`/back`返回上一个地点

---
欢迎您补充！补充时，请使用markdown格式，具体[参考提交文档的步骤](help.md)

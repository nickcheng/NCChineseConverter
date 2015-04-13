# NCChineseConverter #

## 简介 ##

NCChineseConverter 是一个 **基于 Objective-C** 的中文简繁正转换库. 除此之外, 本项目还包括一个 Python 的词库转换工具.

本库的基本实现原理: 从 Mediawiki 提供的[字典](http://svn.wikimedia.org/svnroot/mediawiki/trunk/phase3/includes/ZhConversion.php)中提取数据, 转换为自己需要的格式, 然后用最大正向匹配算法进行字符替换.

### 特点 ###

* 可以只使用单一词库
* 可扩充自定义词库
* 提供 NSString 的 Category

## 使用方法 ##

1. 用词典工具生成词典
2. 把生成的词典放在项目的 Resources 目录下
3. 按如下方式引用转换库和调用

```objective-c
#import "NCChineseConverter.h"
…
NSString *oriString = @"";
NSString *result = [[NCChineseConverter sharedInstance] convert:oriString 
                                                       withDict:NCChineseConverterDictTypezh2TW];
…
```

### Tool ###

下载词库并生成词典:
```
python dictgenerator.py
```

用本地词库生成词典(适用于已经下载了词库文件):
```
python dictgenerator.py n
```

利用词典工具会在当前目录生成如下词典文件:

* zh2TW.txt (简体 -> 台湾正体)
* zh2HK.txt (简体 -> 港澳繁体)
* zh2SG.txt (简体 -> 新马繁体)
* zh2CN.txt (繁体/正体 -> 大陆简体)

方便起见, 我在 `dictionary` 目录中放了转换好的词典文件. 目录名称即为词典生成时间.

注意: 请勿修改文件名, 转换库是严格按照文件名来读取词典的. 

### 自定义扩充转换词组 ###

词典工具是根据 Mediawiki 的词库来进行词典生成, 所以要等待 Mediawiki 的词库更新才能得到新的词典. 如果你有一些 Mediawiki 里没有的词语要扩充, 则可以使用该方法来使用.

使用前缀相同的字典文件来进行自定义词组的扩充, 转换库会自动加载对应的扩充字典.

比如, 把你自己的 **简体 -> 台湾正体** 词典命名为 **zh2TW.custom.txt**, 这样转换库就可以自动加载这个词典并在转换时使用.

### 备注 ###

虽然词典工具一次生成四个词典, 但是你可以视情况只使用其中一个或多个. 需要注意的是如果你没有在项目中放入某个词典文件, 那么要避免在代码里调用该字典.

## 未来改进 ##

* 增加更多转换词库
* 使用 Double-array Trie Tree 来构造原始字典, 提高搜索速度
* 改进分词算法

## 背景 ##

简繁正的问题在此不多说, 都是历史遗留问题, 具体情况可以自行查看 Wikipedia, 用自己的思考去判断([漢字簡化爭論](http://zh.wikipedia.org/wiki/漢字簡化爭論)). 在此只讨论技术相关问题.

简繁转换不是单纯的从一个字转换为另一个字, 他包含很多内容, 如:

* 各种繁体/正体. 如: 港澳繁体, 台湾正体. 再加上各个华人地区的中文(如新加坡)使用等.
* 简体和繁体的对照往往不止一对一, 而是一对二, 一对三, 甚至一对五([多繁對一簡問題](http://zh.wikipedia.org/wiki/漢字簡化爭論#.E5.A4.9A.E7.B9.81.E5.B0.8D.E4.B8.80.E7.B0.A1.E5.95.8F.E9.A1.8C))

目前比较常用的转换方式主要是 **Wikipedia 的转换方式** 和 **OpenCC**.

Wikipedia 进行简繁转换的操作流程参见: [繁简处理](http://zh.wikipedia.org/wiki/Wikipedia:繁简处理)

OpenCC 的库相对比较专业. 不过这是一个 C 库, 所以如果要在 iOS 下使用, 则需要自己把库编译成 iOS 可以使用的库再进行调用.

## 参考 ##

* [OpenCC](https://github.com/BYVoid/OpenCC)
* [Python 简繁转换](http://gerry.lamost.org/blog/?p=603)

#!/usr/bin/env python
# encoding: utf-8

import sys

WIKI_SOURCE = 'https://github.com/wikimedia/mediawiki/raw/master/languages/data/ZhConversion.php'
WIKI_SOURCE_LOCAL_FILE = 'ZhConversion.php'

# 生成转换字典
def mdic():    
    table = open(WIKI_SOURCE_LOCAL_FILE,'r').readlines()
    dic = {}
    name = []
    for line in table:
        if line[0] == ']':
            name.append(dic)
            dic = {}
        if line[0] == "'":
            word = line.split("'")
            dic[word[1]] = word[3]
    name.append(dic)
            
    name[2].update(name[0]) # 简繁通用转换规则(zh2Hant)加上台湾区域用法(zh2TW)
    name[3].update(name[0]) # 简繁通用转换规则(zh2Hant)加上香港区域用法(zh2HK)
    name[5].update(name[0]) # 简繁通用转换规则(zh2Hant)加上新加坡区域用法(zh2SG)
    name[4].update(name[1]) # 繁简通用转换规则(zh2Hans)加上大陆区域用法(zh2CN)
    
    return name[2], name[3], name[5], name[4]

def downloadWikiSource():
    """docstring for downloadWikiSource"""
    import urllib
    print 'Downloading', WIKI_SOURCE_LOCAL_FILE, '...'
    content = urllib.urlretrieve(WIKI_SOURCE, WIKI_SOURCE_LOCAL_FILE)
    print 'Download accomplished.'

def makeDictFile():
    print 'Parsing wiki source...'
    [dic_TW, dic_HK, dic_SG, dic_CN] = mdic()
    print 'Parse accomplished.'
    
    dic = {}
    dic['zh2TW'] = dic_TW
    dic['zh2HK'] = dic_HK
    dic['zh2SG'] = dic_SG
    dic['zh2CN'] = dic_CN
    
    print 'Saving dictionary files...'
    for f in dic.keys():
        filename = f + '.txt'
        file = open(filename, 'w')
        for k in dic[f].keys():
            content = k + '\t' + dic[f][k] + '\n'
            file.write(content)
        file.close()
    print 'Save accomplished.'

def main():
    v = sys.argv
    if len(v) <= 1 or v[1] != 'n':
        downloadWikiSource()
    makeDictFile()
    
if __name__ == '__main__':
    main()

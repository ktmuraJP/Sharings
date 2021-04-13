#!/usr/bin/env python3
import sys
import re

#ファイル読み込み→文字列化→辞書初期化→頻度算出→出力

str_path = sys.argv[1]  #<--読み込むファイルのパス定義。標準入力としてるけど、直でパス文字列代入でも大丈夫
#str_path = "C:\\hoge\\fuga\\" #好きなパスを代入

def scan(string):
    words = {}
    split_str = []
    # 初期化
    for word in re.split(" |\,|\.|\-|\n",string):
        if word != '':
            words[word]=0
            split_str.append(word)
    #頻度の算出
    latency(words, split_str)
    #一応ソートして出力
    return sorting(words)

def latency(dictionary, split_str):
    for word in split_str:
        if word in dictionary:
            dictionary[word] += 1

def sorting(dictionary):
    return sorted(dictionary.items(), key=lambda x:x[1],reverse=True)

if __name__=="__main__":
    with open(str_path) as fp:
        input_str = fp.read() 
        listed = scan(input_str)
        for i in listed:
            print(i)

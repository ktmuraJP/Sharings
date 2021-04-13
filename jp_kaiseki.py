#!/usr/bin/env python3
import sys

input_str = sys.argv[1]

def word_latency(string):
    for i in string.split(): 
        print(i)

if __name__=="__main__":
    print(input_str)
    word_latency(input_str)

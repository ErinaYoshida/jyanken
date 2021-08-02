# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:02:32 2021

@author: erina
"""
def can(hand):
    if 0 <= hand <= 2:
        return True
    else:
        return False

def print_hand(hand, name="ゲスト"):
    hands = {0:"グー", 1:"チョキ", 2:"パー"}
    print(name + "は" + hands[hand] + "を出しました")
    
def judge(A, B):
    if A == B:
        return "あいこ"
    elif (A == 0 and B == 1) or (A == 1 and B == 2) or (A == 2 and B == 0):
        return "勝ち"
    else:
        return "負け"
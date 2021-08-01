# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:23:37 2021

@author: erina
"""
player_name = input("名前を入力してください")
print("じゃんけんを始めます")
player_hand = int(input("何を出しますか？(0:グー, 1:チョキ, 2:パー)"))
hands = {0:"グー", 1:"チョキ", 2:"パー"}
print(player_name + "は" + hands[player_hand] + "を出しました")

import random
computer_hand = random.randint(0,3) #？randintの範囲指定
print("コンピューターは" + hands[computer_hand] + "を出しました")

def judge(A, B):
    if A == B:
        result = "あいこ"
    elif (A == 0 and B == 1) or (A == 1 and B == 2) or (A == 2 and B == 0):
        result = "勝ち"
    else:
        result = "負け"
        
judge(player_hand, computer_hand)
print("結果は" + result + "です") #NameError: name 'result' is not defined

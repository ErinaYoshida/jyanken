# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:23:37 2021

@author: erina
"""
import utils
import random

player_name = input("名前を入力してください")
print("じゃんけんを始めます")
player_hand = int(input("何を出しますか？(0:グー, 1:チョキ, 2:パー)"))

if utils.can(player_hand):
    utils.print_hand(player_hand, player_name)
    
    computer_hand = random.randint(0,2)
                #randint→(a,bとも含む)　randrange→(a含む,b含まない)or(a含まず0~)
    utils.print_hand(computer_hand, "コンピューター")
        
    result = utils.judge(player_hand, computer_hand)
    print("結果は" + result + "です")
    
else:print("0~2の数字を入力してください")
    

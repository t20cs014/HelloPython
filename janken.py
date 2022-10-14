'''
Created on 2022/10/14

@author: t20cs014
'''

import random


hand = [ [0, "グー"], [1, "チョキ"], [2, "パー"] ]

a = hand[random.randint( 0, 2 )]
b = hand[random.randint( 0, 2 )]


if( a[0] == b[0] ) :
    print( "Aの手: ", a[1], "v.s Bの手: " , b[1], " → 引き分け")
    
elif (a[0]==0 and b[0]==1) or (a[0]==1 and b[0]==2 ) or ( a[0]==2 and b[0]==0 ) :
    print( "Aの手: ", a[1], "v.s Bの手: " , b[1], " → Aの勝ち")
    
else :
    print( "Aの手: ", a[1], "v.s Bの手: " , b[1], " → Bの勝ち")





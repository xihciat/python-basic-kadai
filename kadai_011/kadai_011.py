# -*- coding: utf-8 -*-
"""kadai_011.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FsmCOAN21mvq3dcw-dRBX8DTMMKKehUQ
"""

# リストの定義
list = ["水", "金", "地", "火", "木", "土", "天", "海", "冥"]

# forループを使用してリストの内容を出力
for element in list:
    print(element)

# whileループを使用してリストの内容を出力
i = 0  # インデックスの初期化
while i < len(list):
    print(list[i])
    i += 1  # インデックスを更新
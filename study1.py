pocket = ['money', 'handwash' , 'airpod']
print("돈을 입력: ")
money = int(input()) #그냥 input을 사용하면 int가 아니라 str로 입력되 오류가 생긴다.
watch = 1
if 'money' in pocket :
  if money >= 500 :
    print ("포카칩을 사먹어~")
  elif money >= 300 :
    print ("껌을 사먹어~")
  else:
    print ("편의점을 지나쳐라~")
elif watch : pass
else: #: 뒤에는 반드시 들여쓰기가 있어야 한다.
    print ("편의점을 지나쳐라~")
#파이썬을 사용하기 위한 간단한 문법 if
# by GEEE3, April 9, 2021
# 아래와 같은 리스트 A와 B가 있다. 두 리스트를 합쳐서 출력하라
# A = [1, 2, 3], B = [5, 6]
# 첫번째 출력은 +를 사용하고, 두번째 출력은 extend() 리스트 메서드를 사용하라
A = [1, 2, 3]
B = [5, 6]

print("+를 사용:", A + B)
A.extend(B)
print("extend()를 사용:", A)
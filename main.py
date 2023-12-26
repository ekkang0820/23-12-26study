
# ABC더하기
# input_str = input()
# input_list = input_str.split()
# A = [int(x) for x in input_list]
# temp = 0
# for x in A:
#     temp = temp + x
#
# print(temp)

#4바이트마다 long 붙혀 문저열 완성하기
# longinput = int(input())
# count = int(longinput/4)
# longstr = "long "
# for x in range(1,count):
#     longstr = longstr + "long "
# longstr = longstr + "int"
#
# print(longstr)
#



#마름모 별찍기
# cnt = int(input())
# cntstar = 0
# cntblank = cnt
# str=""
#
# for x in range(0,cnt):
#     cntstar = cntstar + 2
#     for x in range(1,cntblank):
#         str = str + " "
#     for x in range(1, cntstar):
#         str = str + "*"
#     str = str + "\n"
#     cntblank = cntblank - 1
#
# for x in range(0,cnt):
#     cntblank = cntblank + 1
#     cntstar = cntstar - 2
#     for x in range(0,cntblank):
#         str = str + " "
#     for x in range(1, cntstar):
#         str = str + "*"
#     str = str + "\n"
#
#
#
# print(str)



#기러기 인도인 토마토 우영우
# str = list(input())
# restr = list(reversed(str))
# lencnt = int(len(str)/2)
# result = 1
# for x in range(0,lencnt):
#     if(str[x] != restr[x]):
#         result = 0
#
#
# print(result)



#가장 많이 사용한 알파벳
strInput = list(input().upper())
cntstr = {}
cnt = 0
result = "?"

for x in strInput:
    if cntstr.get(x) != None:
        cntstr[x] = cntstr[x] + 1
    else:
        cntstr[x] = 1

    if cntstr.get(x) > cnt:
        cnt = cntstr.get(x)
        result = x
    elif cntstr.get(x) == cnt:
        result = "?"


print(result)











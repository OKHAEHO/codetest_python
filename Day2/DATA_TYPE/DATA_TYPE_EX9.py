dic_sum = {}

dic_sum["국어"] = int(input("국어 점수를 입력하세요 : "))
dic_sum["수학"] = int(input("수학 점수를 입력하세요 : "))
dic_sum["영어"] = int(input("영어 점수를 입력하세요 : "))
dic_sum["도덕"] = int(input("도덕 점수를 입력하세요 : "))
dic_sum["물리"] = int(input("물리 점수를 입력하세요 : "))

average = sum(dic_sum.values()) / len(dic_sum) #sum()은 해당 안의 값을 다 더하기
print("평균은 ", average)
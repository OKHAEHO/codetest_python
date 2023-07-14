userid1, userid2 = input("주민번호를 입력하세요.(-로 구분) : ").split('-')
seoul_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08"]
qntks_list = ['09','10','11','12']
wjscp_list = [str(i) for i in range(1,95)]

i=0

while True :
    if len(userid1) > 6 or len(userid2) > 7 :
        print("주민번호를 잘못입력하였습니다.")
        break
    else :
        print("올바른 주민등록번호입니다.")

        while True :
            userid = userid1

            year = int(userid[0:2])
            month = int(userid[2:4])
            day = int(userid[4:6])

            if 50 <= year <= 99:
                print('생년월일: 19%d년 %d월 %d일' % (year, month, day))
                break
            elif 10 <= year < 50:
                print('생년월일: 20%d년 %d월 %d일' % (year, month, day))
                break
            elif 0 <= year <= 9 :
                print('생년월일: 200%d년 %d월 %d일' % (year, month, day))
                break         
        
        while True :
            if userid2[0] == 1 or 3 :
                print("남자입니다.")
                break
            elif userid2[0] == 2 or 4 :
                print("여자입니다")
                break #성별

        while True :
            if userid2[1:3] in seoul_list :
                print('거주지 : 서울')
                break
            elif userid2[1:3] in qntks_list :
                print("거주지 : 부산")
                break
            elif userid2[1:3] in  wjscp_list[13:16] :
                print("거주지 : 인천")
                break
            elif userid2[1:3] in  wjscp_list[16:26] :
                print("거주지 : 경기도")
                break
            elif userid2[1:3] in  wjscp_list[26:35] :
                print("거주지 : 강원도")
                break        
            elif userid2[1:3] in  wjscp_list[25:40] :
                print("거주지 : 충북")
                break           
            elif userid2[1:3] == "40" :
                print('거주지 : 대전')
                break
            elif userid2[1:3] in  wjscp_list[41:48] :
                print("거주지 : 충남")
                break 
            elif userid2[1:3] in  wjscp_list[48:55] :
                print("거주지 : 전북")
                break             
            elif userid2[1:3] in  wjscp_list[55:67] :
                print("거주지 : 전남")
                break
            elif userid2[1:3] in  wjscp_list[67:70] :
                print("거주지 : 대구")
                break     
            elif userid2[1:3] in  wjscp_list[70:82] :
                print('거주지 : 경북')
                break
            elif userid2[1:3] in  wjscp_list[82:93] :
                print("거주지 : 경남")
                break
            elif userid2[1:3] in  wjscp_list[93:96] :
                print("거주지 : 제주")
                break      # 지역
        


        break
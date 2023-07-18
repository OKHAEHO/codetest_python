# Python
#### 코딩테스트를 위한 저장소

## Day1 
파이썬 환경 설정 -완-
    - 문자열, 리스트
    .len() : 길이
    .min() : 최솟값
    .max() : 최댓값
    .find("d") : 문자열 내 d의 위치(인덱스)
    .replace('원래문자', '변경문자') : 문자 변경
    .append() : 요소 추가
    .count() : 요소 개수
    .insert(index, 값) : index위치에 값 삽입
    .remove() : 제거
    .sort() : 정렬(기본은 오름차순)
    .reverse() : 거꾸로 뒤집기
    .pop() : 마지막 요소 제거

## 실행 및 Git허브 연동 -완-
[소스 코드 : HELLOWORLD.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/helloworld.py)

## 기본 출력 실습
[소스 코드 : HelloWorld_ex.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/HelloWorld_ex.py)

[소스 코드 : DATA_INPUT_EX2.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_INPUT/DATA_INPUT_EX2.py)

[소스 코드 : DATA_CONVERT_EX3.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_CONVERT/DATA_CONVERT_EX3.py)

[소스 코드 : IF_REPEAT_EX4_1.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_REPEAT/IF_REPEAT_EX4_1.py)

[소스 코드 : IF_REPEAT_EX4_2.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_REPEAT/IF_REPEAT_EX4_2.py)

[소스 코드 : IF_REPEAT_EX4_3.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_REPEAT/IF_REPEAT_EX4_3.py)

[소스 코드 : IF_REPEAT_EX5.PY 실행 중](https://github.com/OKHAEHO/codetest_python/blob/master/Day1/DATA_REPEAT/IF_REPEAT_EX5.py)

## Day2

[소스 코드 : DATA_TYPE_EX6.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day2/DATA_TYPE/DATA_TYPE_EX6.py)

[소스 코드 : DATA_TYPE_EX7.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day2/DATA_TYPE/DATA_TYPE_EX7.py)

[소스 코드 : function_ex11.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day2/function/function_ex11.py)

[소스 코드 : function_ex12.PY 실행 완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day2/function/function_ex12.py)

## Day3
[소스 코드 : time_test.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/time_test.py)

[소스 코드 : greedy.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/greedy.py)

[소스 코드 : greedy_time.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/greedy_time.py)

[소스 코드 : card.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/card.py)

[소스 코드 : coin.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/coin.py)

[소스 코드 : xorplus.py 실행완료](https://github.com/OKHAEHO/codetest_python/blob/master/Day3/xorplus.py)

## Day 6
DFS와 BFS
데이터 탐색 = 원하는 데이터 도달

DFS : 스택, 재귀함수 이해
BFS : 큐 자료구조 이해

탐색알고리즘인데 문제 유형마다 고민을 하게 됩니다. 
그래프 탐색으로 풀어야할지 뭘 적용을 할지 뭘 해야할지 모를때는 둘 다 사용해서 풀리는지 해야한다~!
DFS -> BFS 순서로 풀어본다.

스택이란?
선입후출 : First In, Last Out (접시 쌓기)

큐?
선입선출 : First In, First Out

재귀함수 : 자기 자신을 다시 호출하는 함수
    대표 : 팩토리얼 함수
    반복연산을 하는 곳에 대표적으로 사용됨
    프로그램이 커지면 가독성이랑 컨트롤이 어려워지기 때문에 잘 안씀
    
코딩테스트는 최대한 간결하게 표현을 하려고 하기 떄문에 재귀함수로 잘 표현을 해놓았다. (그래서 읽을 줄 알아야된다.)
재귀함수를 사용하는게 짧고 편리하기는 하다.

팩토리얼 함수 : n! = n * (n-1)!

[소스코드 : DFS,BFS 실전 활용 문제 완벽 이해!](https://github.com/OKHAEHO/codetest_python/blob/master/Day6/home2.py)
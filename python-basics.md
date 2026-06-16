---
layout: default
title: "Python 기초 문법과 실습"
category: tech-fundamentals
---

<style>
  /* Sidebar Docs Layout - Dark Premium Theme */
  body {
    background-color: #0B1412 !important;
  }
  .docs-container {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
    padding-top: 80px;
    min-height: calc(100vh - 80px);
  }
  
  /* Left Sidebar */
  .docs-sidebar {
    width: 300px;
    background: rgba(15, 23, 42, 0.4);
    border-right: 1px solid rgba(16, 185, 129, 0.15);
    padding: 30px 20px;
    position: sticky;
    top: 80px;
    height: calc(100vh - 80px);
    overflow-y: auto;
  }
  .docs-sidebar::-webkit-scrollbar { width: 6px; }
  .docs-sidebar::-webkit-scrollbar-thumb { background: rgba(16, 185, 129, 0.3); border-radius: 4px; }
  
  .docs-search-wrapper {
    position: relative;
    margin-bottom: 25px;
  }
  .docs-search-wrapper i {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    color: #94a3b8;
  }
  #docs-search {
    width: 100%;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(16, 185, 129, 0.4);
    border-radius: 8px;
    padding: 12px 15px 12px 40px;
    color: #f8fafc;
    font-family: 'Pretendard', sans-serif;
    font-size: 0.95rem;
    transition: all 0.3s ease;
    box-sizing: border-box;
  }
  #docs-search:focus {
    outline: none;
    border-color: #10B981;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
  }
  
  #toc {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  #toc li {
    margin-bottom: 8px;
  }
  #toc a {
    color: #cbd5e1;
    text-decoration: none;
    font-size: 0.95rem;
    display: block;
    padding: 6px 12px;
    border-radius: 6px;
    transition: all 0.2s ease;
  }
  #toc a:hover {
    background: rgba(16, 185, 129, 0.1);
    color: #10B981;
  }
  #toc li.toc-h2 a { padding-left: 12px; font-weight: 600; }
  #toc li.toc-h3 a { padding-left: 28px; font-size: 0.9rem; color: #94a3b8; }
  
  /* Hidden class for search filtering */
  .hidden { display: none !important; }

  /* Main Content */
  .docs-content {
    flex: 1;
    padding: 40px 60px 80px 60px;
    max-width: 900px;
    color: #e2e8f0;
    line-height: 1.7;
    font-size: 1.05rem;
  }
  .docs-content h1, .docs-content h2, .docs-content h3 {
    color: #f8fafc;
    margin-top: 2em;
    margin-bottom: 0.8em;
    font-family: 'Orbitron', 'Pretendard', sans-serif;
  }
  .docs-content h2 { border-bottom: 1px solid rgba(16, 185, 129, 0.2); padding-bottom: 10px; }
  
  /* Code block margins */
  .docs-content figure.highlight {
    margin: 20px 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
  }
  
  @media (max-width: 992px) {
    .docs-container { flex-direction: column; }
    .docs-sidebar {
      width: 100%;
      height: auto;
      position: relative;
      top: 0;
      border-right: none;
      border-bottom: 1px solid rgba(16, 185, 129, 0.15);
    }
    .docs-content { padding: 30px 20px; }
  }
</style>

<div class="docs-container">
  <!-- 좌측 고정 사이드바 -->
  <aside class="docs-sidebar">
    <div class="docs-search-wrapper">
      <i class="uil uil-search"></i>
      <input type="text" id="docs-search" placeholder="Type to search...">
    </div>
    <ul id="toc">
      <!-- JS가 여기에 목차를 자동 생성합니다 -->
    </ul>
  </aside>

  <!-- 우측 메인 본문 -->
  <main class="docs-content" id="docs-content" markdown="1">

# 01장 Python Programming: 기초 및 자료형

## 01-1 자료형

### 변수(Variable)
----------------------------------------

값을 저장하는 메모리 공간  
즉, 포스트잇(변수) = 포스트잇 안에 내용(저장된 데이터)    
ex) a, b가 변수   
   → a(변수명) = 15(저장된 데이터)  
   

- 변수 이름과 값을 할당하여 사용한다.  
ex) a = 10
- 프로그램 실행 중 값 변경이 가능하다.  
ex) a = 10 -> a = 20
- 변수 이름(식별자) 자체도 값처럼 다룰 수 있다.
- 변수에 값을 넣으면 자료형으로 자동으로 정해준다.
- type(): 변수에 저장된 자료형을 확인할 때 사용


### 변수 규칙
------------------------------------------

- 영문자, 숫자, _ 사용 가능
- 숫자로 시작할 수 없다.  
ex) 1anme = '이름'
- 예약어(이미 정해져 있는 변수) 사용을 못 한다.  
ex)  if, else, while 등
- 대소문자를 구분한다.
  -> 변수 이름을 서로 다른 값으로 구별하기 때문이다.    

### 변수명 작성 
-----------------------------------------
- 의미가 명확한 이름 사용    
ex) score, name
- 단어 사이에 _ 넣어서 사용    
ex) name_student
- 길이가 너무 짧거나 긴 이름은 사용하지 않는다.

{% highlight python %}
print('안녕하세요')   # print('') '' 안에 문자열을 넣어 사용

a = 1               # 변수 a에 10의 값을 저장
print(a)            # 변수 a의 값을 출력하는 것 

a = 10              # 변수 a에 20의 값을 저장(기존 1이 10으로 바뀜)
print(a)

# 대소문자 구분
Name_student = '길동'  # 변수_이름 = 변수에 저장할 값
print(Name_student)     # 변수에 저장된 값 출력

name_student = '영희'  
print(name_student)
{% endhighlight %}

## 01-2 숫자형(Number) 자료형
----------------------------------
- 숫자형은 숫자 데이터로 저장하고 계산하는 자료형이다. 

정수형(int)
 - 소수점이 없는 숫자로 양수, 음수, 0 등으로 정수 값을 나타내는 자료형이다.  
 ex) 123, 0 , -20

실수형(float)
 - 소수점이 포함된 모든 값을 나타내는 자료형이다.  
 ex) -10.0, 0.0, 3.14, 143.12


{% highlight python %}
# 변수가 자료형을 스스로 판단하여 지정해준다.
# type() 함수를 사용하여 변수의 자료형을 확인할 수 있다.

a = 10      # 변수 a에 정수 10의 값을 할당
b = 10.12   # 변수 b에 실수 10.12의 값을 할당

print(a)
print(type(a))  # 변수 a의 자료형을 확인하고, 출력

print(b)
print(type(b)) # 변수 b의 자료형을 확인하고, 출력
{% endhighlight %}

### 숫자 자료형 연산자
----------------------------------------

데이터를 가공하기 위한 연산자이다.
- 덧셈 : +
- 뺄셈 : -
- 곱셈 : *
- 나머지 : %  
→ 홀짝 판별이나 배수 찾기에 유용
- 거듭재곱 : **
- 몫 : //  
→ 정수 결과만 필요할때
- 나눗셈 : /  
→ 연산 결과는 항상 실수형으로 나온다.

{% highlight python %}
a = 25
b = 5

number=a+b      # a(25) + b(5)의 값을 number에 저장
print(number)

number = a - b      # a(25) - b(5)의 값을 number에 저장
print(number)

number = a * b      # a(25) X b(5)의 값을 number에 저장
print(number)

# 나머지 연산자는 무조건, 실수형으로 나온다.
number = a / b      # a(25) / b(5)의 값을 result에 저장
print(number)

number = a % b      # a(25) % b(5)의 값을 number에 저장
print(number)       # 10 / 5 = 몫 : 2, 나머지 : 0
print(10 % 7)       # 10 / 7 = 몫 : 1, 나머지 : 3

number = a**b       # a(25) ** b(5)의 값을 number에 저장
print(number)

number = a//b       # a(25) // b(5)의 값을 rnumber에 저장
print(number)       # 25 / 5 = 몫 : 2, 나머지 : 0
{% endhighlight %}

### 연산자 우선순위
---------------------------------------

사칙연산과 같은 우선순위를 갖는다.

1. 괄호 ()
2. 제곱 연산자 **
3. 곱셈, 나눗셈, 나머지, 몫 연산자 (*, /, //, %)
4. 덧셈, 뺄셈 연산자 (+, -)

{% highlight python %}
# 연산자 우선순위
# 괄호
number = (3 + 3) / 2
print(number)

# 2. 제곱 연산자 **
result2 = 2 ** 3 
print("2 ** 3  =", result2)  # 오른쪽부터 계산
{% endhighlight %}

## 01-3 문자열 자료형(str)
----------------------------------------------------------
- 문자로 나열된 자료형
- 글자, 숫자 기호 등 문자열 안에 들어갈 수 있다.


-문자열을 만드는 4가지 방법-  

1. 한 줄 문자열
- '문자열'
- "문자열"  

2. 여러 줄 문자열(줄바꿈 사용)
- """문자열"""
- '''문자열'''   

- 작은따옴표(' ') 안에  큰따옴표 (" "), 큰따옴표 (" ") 안에 작은따옴표(' ') 사용 가능  
→ 문자열 안에 따옴표를 포함하기 위해 서로 다른 따옴표를 사용한다.

{% highlight python %}
# 문자열 안에 ""를 사용하기 위해 ''로 문자열을 구성.
a = 'a, 파이썬을."열심히"\n'
print(a)

# 문자열 안에 ''를 사용하기 위해 ""로 문자열을 구성.
b = "b, 파이썬을. '열심히'\n"
print(b)

# ''' '''로 씌여진 문자열은 줄바꿈, '', "" 등 거의 모든 형식을 표현할 수 있다.
c = '''c, "파"이"썬
열'심'
히\n'''
print(c)

# """ """로 씌여진 문자열은 줄바꿈, '', "" 등 거의 모든 형식을 표현할 수 있다.
d = """d, 파이썬
열심히"""
print(d)
{% endhighlight %}

### 문자열 이스케이프 코드
---------------------------------------------
문자열 안에서 출력물을 보기 좋게 정렬하기 위한 문자

문자열 안에 백슬래쉬 \ 로 시작하는 문자
 - \n : 줄 바꿈 문자 (enter 역할)
 - \t : 탭 간격 주는 문자 (tab 역할)
 - \\\\  백슬래쉬 문자
 - \\' : 작은따옴표 문자
 - \\"  : 큰따옴표 문자  

{% highlight python %}
# \' 작은따옴표 문자를 이용하여 ''로 구성된 문자열 안에서 '사용
a = '누구는 말했다.\n\'파이썬이 좋다고\''
print(a)

# \t 탭 문자를 사용하여 길이가 다른 두 문자열을 일정한 길이로 유지.
b = "115\t23\t4516"
c = "1\t31255\t456"
print(b)
print(c)
{% endhighlight %}

잘 사용하지 않는 문자
 - \r : 줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동
 - \f : 줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동
 - \a : 벨 소리
 - \b : 백 스페이스
 - \000 : 널 문자

### 문자열 연산
----------------------------------------
- 덧셈 : 문자열 + 문자열 → 문자열이 하나로 합친다.
- 곱셈 : 문자열 * 숫자 → 해당 문자열을 숫자만큼 반복한다.

문자열 결합과 반복의 활용
- 문자열 연산과 반복문을 같이 사용하면 다양한 패턴 만들 수 있다.  
ex) "*" * i,  "-"*50


{% highlight python %}
a1 = "You need "
a2 = "Python"

# 문자열 덧셈 
text = a1 + a2
print(text)

text1 = a1 * 5
print(text1)
print(a2*3)

# 문자열 곱셈을 이용하여 - 50개 출력하기
print("*"*50)
{% endhighlight %}

### 문자열 인덱싱
----------------------------------
- 문자열을 개별적으로 가리키는 고유의 번호 (값 1개를 추출)
- 양수 인덱스 : 왼쪽(시작)부터 0으로 증가   
ex)'python'  
[p][y][t][h][o][n]  
[0][1][2][3][4][5]

- 음수 인덱스 : 오른쪽(끝)부터 -1로 감소  
ex) 'python'  
[p][y][t][h][o][n]  
[-5][-4][-3][-2][-1]

{% highlight python %}
text = "You need Python"

# 양수 인덱싱: 왼쪽(0번)부터 순서대로 번호를 매김
a = text[0]          # a = "Y" (첫 번째 글자)
aa = text[-15]       # aa = "Y" (뒤에서부터 15번째, 즉 첫 번째 글자)
print(a)             
print(aa)           

# 공백(Space)도 엄연한 하나의 문자 데이터임
b = text[3]          # b = " " (You 다음의 첫 번째 공백)
bb = text[8]         # bb = " " (need 다음의 두 번째 공백)
print(b)             
print(bb)            

# 음수 인덱싱: 오른쪽(-1번)부터 거꾸로 번호를 매김
c = text[9]          # c = "P" (Python의 시작 알파벳)
cc = text[-6]        # cc = "P" (뒤에서 6번째 글자)
print(c)             
print(cc)            

# 문자열 결합: 인덱싱으로 뽑아낸 문자들을 + 연산자로 합치기
# "P" + "y" + "t" + "h" = "Pyth"
d = text[9] + text[10] + text[11] + text[12]
print(d)             #

#  마지막 글자 확인하기
last = text[-1]      # last = "n" (문자열의 맨 끝 데이터)
print(last)
{% endhighlight %}

### 문자열 슬라이싱
--------------------------------------------
문자열을 일정 범위를 통째로 잘라내는 것
- 구조: 변수명 [첫 번째항목:마지막 항목+1]
- 마지막 항목은 포함되지 않아 마지막 항목+1의 값을 지정해 주어야 한다.
- [ :10] → 첫 번쨰 항목이 공백이면 처음부터 인덱스 추출
- [5:  ] → 마지막 항목이 공백이면 끝까지 인덱스 추출


{% highlight python %}
text = "You need Python"
# good 문자 가져오기
print(text[10]+text[11]+text[12]+text[13])
print(text[10:14]) # 13번까지 뽑고 싶다면, 마지막 인덱스+1
print(text[10:])

# is 문자 2가지 방법으로 가져오기
print(text[7]+text[8])
print(text[7:9])

# 슬라이싱에 문자를 추가
a[:1] + 'y' + a[2:]
{% endhighlight %}

### 문자열 포매팅
-------------------------
문자열 속에 변수를 집어넣어 원하는 형식으로 출력
- 숫자 바로 대입(정수) 
- 문자열 바로 대입
- 변수를 통해 값을 대입 % 변수명
- 2개 이상 값 넣기 → %(변수1,변수2)

### 문자열 포맷 코드
--------------------------------
문자열 포맷 코드 헷갈리면  %s 사용
 - %s : 문자열(string), , 알아서 문자로 바꿔준다.
 - %c : 문자 1개(character)
 - %d : 정수(integer)
 - %f : 실수(Floating point)
 - %o : 8진수
 - %x : 16진수

{% highlight python %}
# 문자열 포맷 코드(%d)에 숫자를 바로 대입하는 방법.
print("옷이 %d 개가 있습니다." % 15)

# 문자열 포맷 코드(%s)에 문자열을 바로 대입하는 방법.
print("옷이 %s 있습니다." % "많이")

number = 5
# 문자열 포맷 코드에 변수를 대입하는 방법.
print("옷 %d 개가 있습니다." % number)

# 2개 이상의 문자열 포맷 코드 % (a, b)의 형식으로 사용
fruit = "옷"
number = 5
print("저는 %d개의 %s가 있습니다." %(number, fruit))

# %d를 %s로 바꾸어도 상관없음.
print("저는 %s개의 %s가 있습니다." %(number, fruit))
{% endhighlight %}

### f 문자열 포매팅
---------------------------------------------------------------------------
문자열 앞에 f만 붙이고, 중괄호 { } 안에 변수 이름을 직접 넣어서 직관적으로 만드는 문장
- 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용 가능

f, % 방식 비교하기
- % 방식 : "사과 %d 개'
- f-string 방식 : f"사과{number}개' → 가독성이 좋아진다.

{% highlight python %}
name = "권은지"
number = 5

# 기본 사용법
print(f"제 이름은 {name} 입니다.")
print(f"사과 {number}개가 있습니다.")


# 여러 변수 사용
fruit = "사과"
print(f"저는 {number}개의 {fruit}가 있습니다.")


# 연산도 가능
print(f"사과 {number + 3}개가 있습니다.")


# 정렬
print(f"{name:>10}")   # 오른쪽 정렬
print(f"{name:<10}")   # 왼쪽 정렬

# 공백 채우기
print(f"{number:05d}")  # 5자리, 빈칸 0으로 채움


# % 방식 vs f-string 방식 비교

# % 방식
print("사과 %d개가 있습니다." % number)

# f-string 방식
print(f"사과 {number}개가 있습니다.")
{% endhighlight %}

### 문자열 관련 함수
------------------------------------
 - LEN : 문자열 길이 구하기
 - COUNT : 특정 문자 수 세기
 - UPPER : 모든 문자 대문자로 변경
 - LOWER : 모든 문자 소문자로 변경
 - STRIP : 양쪽 공백 지우기
 - LSTRIP : 왼쪽 공백 지우기
 - RSTRIP : 오른쪽 공백 지우기
 - SPLIT : 문자열 원하는 형식으로 나누기
 - REPLACE : 문자열 원하는 문자열로 바꾸기
 - JOIN : 문자열 사이사이에 문자 삽입
 - STRIP : 양쪽 공백 지우기
 - FIND, INDEX : 위치 알려 주기

### LEN() 
-------------------------------------
공백, 줄 바꿈(\n)을 포함한 문자열의 길이를 구하는 함수

{% highlight python %}
# len() 함수를 이용하여 문자열의 길이 구하기
# \t와 같은 이스케이프 문자열도 1개의 문자로 취급한다.

# 함수 -> 특정한 기능을 하는 코드
text = "i love\tpython."
print(text)
print(len(text))      # text 변수의 길이를 구해서 출력한다.

text = "hi there"  # 공백
print(len(text))

text = "a!@#"      # 특수문자
print(len(text))
{% endhighlight %}

### COUNT()
----------------------------
찾고 싶은 문자 개수를 세는 함수

{% highlight python %}
text = "python"
print(text.count("a"))
{% endhighlight %}

### UPPER()
---------------------------
문자열을 모두 대문자로 변경하는 함수

{% highlight python %}
a = "hi"
a.upper()

text1 = "Python is the best choice"
text2 = "python is the best Choice"

print(text1.upper())
print(text2.upper())
{% endhighlight %}

### LOWER() 
------------------------------
 문자열을 모두 소문자로 변경하는 함수

{% highlight python %}
a = "hi"
a.lower()

text1 = "Python IS THE BEST choice"
text2 = "Python Is Good"

print(text1.lower())
print(text2.lower())
{% endhighlight %}

### STRIP()
----------------------------
양쪽 공백을 지우는 함수

{% highlight python %}
# 양쪽 공백 지우기
text = "  python  "

print(text.strip()) # 양쪽 공백 지우기
{% endhighlight %}

###  LSTRIP()
-------------------------------
왼쪽 공백을 지우는 함수

{% highlight python %}
# 왼쪽 공백 지우기
text = "  python  "


print(text.lstrip()) # 왼쪽 공백 지우기
print(text.rstrip()) # 오른쪽 공백 지우기
{% endhighlight %}

### RSTRIP()
--------------------------
오른쪽 공백 지우는 함수


{% highlight python %}
# 오른쪽 공백 지우기
text = "  python  "

print(text.rstrip())
{% endhighlight %}

### SPLIT()
------------------------------
문자열을 기준에 맞게 분리하는 함수
- a.split()처럼 괄호 안에 값이 없으면 공백, 탭, 엔터로 분리된다.
- 특정 문자를 넣으면 그 문자에 기준으로 리스트의 형식으로 저장됨

{% highlight python %}
text = "Python is the best choice"
print(text.split())       # 형식을 지정하지 않아 공백으로 분리됨.

text1 = "a,b,c,d e"
print(text1.split(','))    # 구분자를 ','로 직접 지정
{% endhighlight %}

### REPLACE() 
----------------------------
문자열 안에 원하는 문자열로 바꾸는 함수
- 구조 : replace(바뀔_문자열, 바꿀_문자열)
- 오타 수정이나 단어 치환 필수

{% highlight python %}
a = "Python is the best choice"
a.replace("Life", "Your leg")
{% endhighlight %}

###  JOIN()
---------------------------
문자열 사이에 문자를 삽입하는 함수

{% highlight python %}
text = "python is good"

# text 문자열의 모든 문자 사이사이에 ,를 삽입한다.
print('/'.join(text))
{% endhighlight %}

### FIND()
------------------------------------------
특정 문자, 문자 위치를 찾는 함수
- 찾는 값이 없으면 -1 반환


{% highlight python %}
text = "life"

print(text.find("e"))   
print(text.find("i"))
{% endhighlight %}

### index
-----------------------------------
특정 문자, 문자 위치를 찾는 함수
- 찾는 값이 없으면 에러 발생

{% highlight python %}
text = "hello"

# index()
print(text.index("e"))   # 1
# print(text.index("x")) # ValueError 발생
{% endhighlight %}

### INPUT()
---------------------------------------------------
사용자로부터 값을 입력받아 변수에 저장하는 함수
- 구조 : 변수명 = input('문자열: ')
- input() → 항상 문자열 반환
- 문자열 외의 다른 자료형을 사용하기 위해 자료형 변환을 사용해야 한다.  
ex) 숫자 계산 → 반드시 형변환 필요

{% highlight python %}
# 기본 입력 (문자열)
name = input('이름을 입력하세요: ')   # 사용자로부터 문자열 입력 받기
print(name)
{% endhighlight %}

{% highlight python %}
# 자료형 변환
# input()으로 입력받은 값은 기본적으로 문자열(str)이다.
# 따라서 숫자로 사용하려면 원하는 자료형으로 변환해야 한다.

# 변환 방법
# 정수 변환 : int(값)
# 실수 변환 : float(값)

a = input('문자열을 입력해주세요: ')           # 문자열 입력 → str 저장
b = int(input('정수를 입력해주세요: '))        # 입력값 → int 변환
c = float(input('실수를 입력해주세요: '))      # 입력값 → float 변환

print('문자열:', a)                           # 문자열 출력
print('정수:', b)                             # 정수 출력
print('실수:', c)                             # 실수 출력

# 연산 결과
print('정수 + 실수 =', b + c)                 # int + float → float로 자동 변환되어 계산됨
{% endhighlight %}

{% highlight python %}
# 문자열 상태에서의 연산 (문제 발생 예시)
a = input('숫자1: ')                
b = input('숫자2: ')                
print(a + b)                       #  2 + 3 → 23
{% endhighlight %}

## 01-4 리스트 자료형(list)
--------------------------------------------------------

- 여러 개의 데이터를 [  ]로 묶어서 하나의 변수로 사용할 수 있는 자료형이다.  
- 숫자, 문자열 등 다양한 데이터를 넣을 수 있다.  
- 데이터는 쉼표로 구분한다.  
ex) a = [1, 2, 3]
    b = ['사과', '배','체리']
    위치:     0,    1,    2

### 리스트 인덱싱
----------------------------------------------------

리스트도 문자열과 유사하게 인덱싱 및 슬라이싱이 가능하다.

인덱싱
 - 리스트에서 원하는 위치에 값을 가져오는 방법
 - 문자열이나 리스트 안에 들어있는 리스트도 하나의 값으로 본다.

중첩 리스트
- 리스트 안에 또 다른 리스트를 넣을 수 있다.  
ex) c[2][0] → c에서 2번 방에 있는 곳에서 0번 데이터 꺼내준다.


{% highlight python %}
# 비어 있는 리스트 생성
a = list()
a = []

b = ["문자열", 20, -30, '고구마']

print(b[1])   # 두번째 값
print(b[-1])  # 음수는 뒤에서부터 값이 나온다.

print("b[1]: "+ str(b[1]))        # 정수 1을 문자열 "1"로 자료형 변환

# a[1] = "문자열"에서 "자"만 출력하고 싶을때
print("b[0][1]: "+ b[0][1])   # a[1][0] = "자"

# 중첩 리스트
# 리스트 안에 또 다른 리스트가 나오면 그 리스트도 인덱스 0부터 다시 시작해서 값을 가져온다.
c = [1, 2, [3, 4, 5,["문자열", 20, -30, '고구마']]]

# c에서 3을 출력하고 싶을때
print(c[2][0])

# c에서 구를 출력하고 싶을때
print(c[2][3][3][1])
{% endhighlight %}

### 리스트 슬라이싱
-----------------------------------------------
- 리스트의 일부 구간을 잘라서 가져오는 방법
- 리스트가 중복되었을 때에는, 인덱싱한 후 슬라이싱을 해야 한다.

{% highlight python %}
# 리스트에서 끝 인덱스는 포함되지 않는다. 
a = ["문자열", 20, -30, '고구마',[3, 4, 5]]

# 문자열, 20, -30만 출력하고 싶을때
print(a[1:3]) 


# [3, 4, 5]를 출력하고 싶을때
print(a[4][0:3])

print(a[:3]) # 시작 인덱스 생략하면 처음부터 출력
print(a[1:]) # 끝 인덱스 생략하면 1부터 끝까지 출력

# number[3:7:2]로 네번째 요소부터 일곱번째 요소까지 가지고 오는데 2개씩 건너뛰면서 출력
number = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

number1 = number[3:7:2]
print(number1)
{% endhighlight %}

### 리스트 뎃셈과 곱셈
-------------------------------------

리스트 덧셈 : 더하는 리스트가 하나로 합쳐짐  
리스트 곱셈 : 곱하는 수만큼 리스트가 반복됨

{% highlight python %}
a = [1, 2, 3]
b = ['수','과일']

# 리스트 덧셈
c = a + b     # a리스트와 b리스트가 합쳐져 변수 c
print(c)

# 리스트 곱셈
print(a*2)
print(b*3)
{% endhighlight %}

### 리스트 요소 수정 삭제 및 추가
--------------------------------------------
수정 : 리스트의 요소에 접근하여 수정한다.

삭제 : del 키워드를 이용한다.

추가 : append() 함수를 사용한다.

{% highlight python %}
a = [1, 2, 3]                    # 숫자 리스트
b = ['사과', '배', '체리']         # 문자열 리스트

# 인덱스(위치): 0, 1, 2
print("b[0]:", b[0])              
print("b[1]:", b[1])              
print("b[2]:", b[2])              
print()

# 수정 (값 변경)
a[2] = 4                          # 2번 인덱스 값을 4로 변경
print("수정 후 a:", a)             # [1, 2, 4]

# 삭제
del a[1]                          # 1번 인덱스 삭제 (뒤 요소가 앞으로 이동)
print("삭제 후 a:", a)             # [1, 4]

del a[2:]   # 리스트 여러 개를 삭제

# 리스트의 추가는 리스트의 맨 뒤에 이루어진다.
# append 명령어로는 한 번에 하나의 요소만 추가가 가능하다.
a.append(4)
print(a)
a.append([5,6,7,8])
print(a)
{% endhighlight %}

### 리스트 관련 함수
-----------------------------
- LEN() : 리스트의 길이 구하기
- APPEND() : 리스트에 요소 추가
- SORT() : 리스트 정렬
- REVERSE() : 리스트 뒤집기
- INDEX() : 요소의 위치값 찾기
- INSERT() : 요소 삽입하기
- REMOVE() : 요소 제거하기
- POP() : 요소 추출하기
- COUNT() : 요소의 개수 세기

### LEN()
---------------------------
리스트 길이 구하는 함수
- 구조 : print(len(객체))

{% highlight python %}
a = ['a', 'b', 'c', ['python', 'is', 'good', [ 1, 4, 5]]]

print(len(a))     # ['python', 'is', 'good', [1, 4, 5]] -> 1개의 요소로 취급.
print(len(a[3]))  # [1, 4, 5] -> 1개의 요소로 취급.
{% endhighlight %}

### APPEND()
------------------------
리스트 요소 추가하는 함수
- 리스트의 맨 마지막에 추가

{% highlight python %}
a = [1, 4, 5]

a.append(4)
print(a)
a.append([5,6,7,8])
print(a)
{% endhighlight %}

### SORT()
---------------------
리스트 정렬하는 함수
- 기본으로 오름차순으로 정렬
- 숫자, 문자 섞여있는 경우는 오류

{% highlight python %}
a = [2, 5, 7, 6, 3, 4, 1]
print(a)

a.sort()
print(a)

b = ['z', 'a', 'b', 'e', 'l', 'k']
print(b)

b.sort()
print(b)
{% endhighlight %}

### REVERSE()
-------------------------
리스트 뒤집는 함수
- 리스트 첫 번째 요소부터 마지막 요소를 뒤집는 것

{% highlight python %}
a = ['z', 'a', 'b', 'e', 'l', 'k']
b = [2, 5, 7, 6, 3, 4, 1]

print(a)
a.reverse()
print(a)

print(b)
b.reverse()
print(b)
{% endhighlight %}

### INDEX()
-----------------------
리스트에 원하는 값이 어디에 있는지 알려주는 함수
- 리스트 안에 같은 값이 존재할 때, 가장 앞에 있는 값을 찾는다.
- 리스트 안에 없는 값을 찾을 시 에러가 발생한다.

{% highlight python %}
a = [1,2,3,4,5,1]
print(a.index(3))     # 3요소의 위치인, 2번 인덱스 출력
print(a.index(1))     # 1요소는 0, 5번 인덱스에 존재하지만, 가장 앞에 있는 0번 인덱스위치를 출력

# print(a.index(9))   # 9라는 요소가 없어 오류
{% endhighlight %}

### INSERT()
--------------------------
리스트 안에 요소를 원하는 위치에 넣을 수 있는 함수
- 구 : insert(위치, 값)

{% highlight python %}
a = [1,2,3,4,5,6,7,8,9]

a.insert(2, 6)
print(a)
{% endhighlight %}

### REMOVE()
--------------------------
리스트의 원하는 요소를 제거하는 함수
 - 중복된 값이 있을 때, 첫 번째 값만 제거한다.

{% highlight python %}
a = [1,2,3,1,4,5,6,7]

a.remove(1)
print(a)

a.remove(3)
print(a)
{% endhighlight %}

### POP()
----------------------------
리스트의 원하는 위치에 있는 요소 추출하는 함수

{% highlight python %}
a = [1,2,3,4,5,6,7]

b = a.pop(2)      # pop함수를 통해 2번인덱스(3)을 추출하여 변수 b에 저장.
print(a)
print(b)
{% endhighlight %}

### COUNT()
--------------------
리스트에 있는 원하는 요소의 개수 세기

{% highlight python %}
a = [12,3,4,5,1,2,2,45,2,1,3,4,2]
print(a)

print(a.count(2))
{% endhighlight %}

## 01-5 튜플 자료형(tuple)
--------------------------------
리스트와 비슷하게 모든 자료형을 담을 수 있는 것.
- 구조 : ()
- 값이 하나일 때는 쉼표(,) 붙어야 한다.  
ex) t1 = (2, ) → 쉼표(,) 안 붙으면 그냥 숫자
- 한 번 만들면 수정 불가(읽기 전용 느낌)
- 수정이 불가능하기 때문에 sort, insert, remove, pop과 같은 메서드가 없다.
- 사용할 수 있는 기능, 리스트 문법 구조는 거의 같다.

### 튜플 연산과 함수
-----------------------------------
1. 튜플 인덱싱
2. 튜플 슬라이싱
3. 튜플 더하기
4. 튜플 곱하기
5. LEN() 함수

{% highlight python %}
# 모든 자료형을 담을 수 있는 자료형.
t1 = (1, 2, 3, ('a', 'b', 'c'))
print(t1)

# 튜플 내부에 요소가 하나만 존재할 때 맨 뒤에 ,를 붙인다.
t2 = (2,)
print(t2)

#튜플 생성시 괄호()를 생략해도 상관없다.
t3 = 1, 2, 3
print(t3)
{% endhighlight %}

## 01-6 딕셔너리 자료형
---------------------------
번호(인덱스)로 데이터를 찾는 게 아니라, key(이름)를 통해 Value(내용) 형태로 데이터를 저장하는 구조
- 구조 : {ket1, key2, key3 ....}
- 순서대로 찾는 게 아니라 오직 Key를 통해서 Value 값을 찾는 구조
- 리스트처럼 위치(index)가 없어 인덱싱 및 슬라이싱이 불가능
- Key 값은 고유해야 하는 값(문자열, 숫자, 튜플 가능)
- 중복되는 key 사용할 수 없고 Key를 여러 번 쓰면 마지막 값만 남는다.

{% highlight python %}
dic = {'name':'pey', 'phone': 'banana', '메론': 'melon'}
dic1 = {1:'hello', 2:[1,2,3], '3':5}

print(dic)
print(dic1)
{% endhighlight %}

### 딕셔너리 쌍 추가 및 삭제
--------------------------------
### 추가
딕셔너리 Key와 Value(값)을 넣으면 하나의 쌍으로 추가된다.
- 변수[Key] = Value

### 요소 삭제
del 키워드를 사용하여 요소를 삭제한다.
 - del 변수명[Key] -> Key에 해당하는 {Key: Value} 쌍이 삭제

{% highlight python %}
# 딕셔너리 생성
# 추가 : dic[새로운 키] = 값  
# 삭제 : del dic[지울키]
student = {"name": "권은지", "age": 20}
# 새로운 요소 추가
student["grade"] = "A"
print(student)

# 기존 Key에 값 수정도 가능
student["age"] = 21
print(student)


### 요소 삭제
# del 키워드를 사용하여 요소 삭제
# del 변수명[Key] -> 해당 Key의 {Key: Value} 쌍 삭제

del student["age"]
print(student)


# 여러 개 추가 예시
student["major"] = "컴퓨터공학"
print(student)


# Key값이 중복되면, 하나를 제외한 다른 key값이 무시됨.
test_dic = {1:'one', 2:'two', 2:'둘', 3:'셋', 3:'three', 3:'삼'}
print(test_dic)
{% endhighlight %}

## 딕셔너리 관련 함수
----------------------------------------------------------
 - keys() : key 리스트 만들기
 - values() : value 리스트 만들기
 - items() : key, value 쌍 리스트 얻기(튜플값)
 - clear() : key: value 쌍 모두 지우기
 - get() : key값을 통해 value값 얻기
 - in : key가 딕셔너리에 있는지 찾아보기(true, false)

{% highlight python %}
dic = {"name": "권은지", "age": 20, "grade": "A"}

print(dic.keys())            # key 리스트
print(dic.values())         # value 리스트
print(dic.items())          # key, vlaue 리스트

print(dic.get("name"))    # 'name'의 value 없기
print('age' in dic)        # '사과' key가 딕셔너리에 있는지 조사
print('수박' in dic)        # '수박' key가 딕셔너리에 있는지 조사

dic.clear()                 # 딕셔너리 초기화
print(dic)
{% endhighlight %}

## 01-7 불 자료형(BOOL)
--------------------
참(True)과 거짓(False)을 나타내는 자료형
- True와 False는 예약어로 같이 작성하면 안되고 첫 문자를 대문자로 작성

{% highlight python %}
a = True
b = False

print(type(a))
print(type(b))
print(a)
print(b)
{% endhighlight %}

### 비교 연산자
--------------------------------------------------------
값의 비교를 통해 True, False의 값을 얻을 수 있는 연산자
- < >, ==, !=, <=, >=
- = : 대입 연산자
- == : 같다
- != : 다르다

{% highlight python %}
x = 10
y = 15

print("x==y: "+str(x == y))  
print(a == b)      
print("x!=y: "+str(x != y))
print(a != b)       
print("x>y: "+str(x > y)) 
print(a > b)       
print("x<y: "+str(x < y)) 
print(a < b)       
print("x<=y: "+str(x <= y))      
print("x>=y: "+str(x >= y))
{% endhighlight %}

### 논리 연산자
--------------------------------------------
and, or, not과 같은 논리 연산자 사용
- and : 양쪽 조건이 모두 참일 때만 True를 반환
- or : 양쪽 조건 중 하나라도 참이면 True를 반환
- not : 참과 거짓을 반대

{% highlight python %}
a = True
b = False


# and 연산자 : a와 b모두 True일 때만, True
print("True and True: "+str(a and a))
print("True and False: "+str(a and b))
print("False and True: "+str(b and a))
print("False and False: "+str(b and b))

# or 연산자 : a와 b모두 False일 때만, False
print("True or True: "+str(a or a))
print("True or False: "+str(a or b))
print("False or True: "+str(b or a))
print("False or False: "+str(b or b))

# not 연산자는 참과 거짓을 반대
print("not True: "+str(not a))
print("not False: "+str(not b))
{% endhighlight %}

## 01-8 집합 자료형(set)
---------------------------------------------------------------
중복, 순서 없이 데이터를 저장하는 구조
- set()이나 중괄호({})를 사용해서 집합 자료형을 만들 수 있음
- 주의 : s = {}로 만들면 딕셔너리가 된다.
- 중복을 허용하지 않고, 순서가 없어 인덱싱으로 요솟값을 얻을 수 없다.
- 집합 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후에 해야 한다.

### 집합의 연산

{% highlight python %}
# 교집합 : 공통 부분(&)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("교집합 (&): " + str(s1 & s2))
print("intersection(): " + str(s1.intersection(s2)))

# 합집합 : 전체 합치기(|)
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("합집합 (|): " + str(s1 | s2))
print("union(): " + str(s1.union(s2)))

#차집합 : 빼기(-)
s1 = {1, 2, 3, 4}
s2 = {3, 4}

print("차집합 s1-s2: " + str(s1 - s2))
print("차집합 s2-s1: " + str(s2 - s1))
{% endhighlight %}

### 집합 자료형 관련 함수
------------------------------------------
- add() : 값 1개 추가
- update() : 여러 개의 값 추가
- remove() : 특정 값 제거
- discard() : 존재하지 않는 값을 제거
- clear() : 모든 값 제거

{% highlight python %}
s = {1, 2, 3}

# add(): 값 1개 추가
s.add(4)
print("add 결과:", s)  # {1, 2, 3, 4}
print("add: " + str(s)) # 문자열 연결 방식


# update(): 여러 개 값 추가
s.update([5, 6])
print("update 결과:", s)  # {1, 2, 3, 4, 5, 6}
print("update: " + str(s))


# remove(): 특정 값 삭제 (없으면 에러 발생)
s.remove(1)
print("remove 결과:", s)  # {2, 3, 4, 5, 6}
print("remove: " + str(s))


# discard(): 특정 값 삭제 (없어도 에러 없음)
s.discard(2)
s.discard(100)  # 없는 값이어도 오류 없음
print("discard 결과:", s)  # {3, 4, 5, 6}
print("discard: " + str(s))


# clear(): 모든 값 삭제
# 집합을 완전히 비운다
s.clear()
print("clear 결과:", s)  # set()
print("clear: " + str(s))
{% endhighlight %}

# 02장 Python Programming: 제어문

## 02-1 if문
---------------------
### 조건문(if문)
- 조건문이 True와 False 인지 판단하여 조건 결과에 따라 수행하는 것
- if   : 만약 ~ 라면(첫번째 조건)
- elif : if에서 조건이 아닐때 추가 조건
- else : 어떤 조건에도 해당하지 않을때 마지막 

### if문의 기본 구조
------------------------------------------------------
구조1 : if와 else
- 조건문이 True면 다음 if문에서 실행하고, False면 else문에서 실행해 출력한다.
- else는 if문 없이 독립적으로 사용하지 못한다.

{% highlight python %}
if문 기본 구조
 if 조건문:
   수행할_문장1
 else:
     수행할_문장A
{% endhighlight %}

{% highlight python %}
num = 10

if num > 5:                # true라서 if문에서 실행
    print("5보다 크다")
else:
    print("5 이하이다")
{% endhighlight %}

### 구조2: if elif .... else
-----------------------------------------------
- if와 else만으로 조건을 판단하기 어려울 때 쓰는 것
- 개수 제한이 없다.
- 이전 조건문이 거짓일 때 수행


{% highlight python %}
if 조건문:
      수행할_문장1 
      ...
  elif 조건문:
     수행할_문장1
      ...
   else:
      수행할_문장1
{% endhighlight %}

### 들여쓰기
-----------------------------------------------------
- 수행할 문장이 같은 줄에 있어야 오류가 발생 하지 않는다.
- 공백문자와 탭 문자를 혼용해서 사용하지 않는다.


{% highlight python %}
# 수행할 문장에서 3번쩨 줄에 달라 오류가 발생
money = True
if money:
    print("빨리")
    print("밥을")
        print("먹어라")

# 같은 줄에 있어야 함
money = True
if money:
    print("빨리")
    print("밥을")
    print("먹어라")
{% endhighlight %}

### if 비교 연산자1
-------------------------
- '<'  작다
- '>'  크다
- '=='  ~와 같다
- '!='  ~와 같지 않다
- '>='  크거나 같다
- '<='   작거나 같다

{% highlight python %}
a = 10
b = 5

print(a < b)   # 작다 → False
print(a > b)   # 크다 → True
print(a == b)  # 같다 → False
print(a != b)  # 같지 않다 → True
print(a >= b)  # 크거나 같다 → True
print(a <= b)  # 작거나 같다 → False
{% endhighlight %}

### if 비교 연산자 연쇄 사용
-------------------------------------

{% highlight python %}
x = 5
1 < x < 10    # x가 1보다 크고 10보다 작은가?

10 <= x <= 20  # x가 10 이상 20 이하인가?


# 위에 내용과 같고 더 간결하다
x = 5
(1 < x) and (x < 10)

(10 <= x) and (x <= 20)
{% endhighlight %}

### if 조건부 표현식
-----------------------------------

{% highlight python %}
# 변수 = 참일_때_값 if 조건 else 거짓일_때_값
# 복잡한 조건이나 긴 표현식에는 가동성이 떨어지기 때문에 사용하지 않는 것이 좋다.


age = 20
if age >= 19:
    print("Adult")
else:
    print("Minor")


# 조건부 표현식 (삼항 연산자)
age = 18
result = "Adult" if age >= 19 else "Minor"
print(result)
{% endhighlight %}

### if 연산자2 
--------------------------
- and : 모두 참이어야 참이다.
- or  : 하나만 참이어야 참이다.
- not : 거짓이면 참이다.

{% highlight python %}
a = 10
b = 20


# and 예시 (둘 다 참이어야 True)
print(a > 5 and b > 15)   
print(a > 5 and b < 15)   


# or 예시 (하나만 참이어도 True)
print(a > 5 or b < 15)    
print(a < 5 or b < 15)    


# not 예시 (결과를 반대로)
print(not(a > 5))         
print(not(a < 5))
{% endhighlight %}

### if 연산자3
----------------------
in
- x가 자료형 안에 있으면 True   

not in
- x가 자료형 안에 없으면 True


{% highlight python %}
# 리스트 
# x가 자료형 안에 있으면 True  
# x가 자료형 안에 없으면 True
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)        
print(10 in numbers)       
print(10 not in numbers)   


# 문자열 
# x가 자료형 안에 있으면 True  
# x가 자료형 안에 없으면 True
text = "hello world"

print("h" in text)         
print("z" in text)         
print("z" not in text)
{% endhighlight %}

## 02-2 while문
------------------
- 조건문이 참인 동안 while 문에 속한 문장들을 반복해서 수행한다.

{% highlight python %}
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
{% endhighlight %}

{% highlight python %}
hit = 0

while hit < 5:
    hit = hit + 1
    print("Hit the tree %d times." % hit)

print("The tree has fallen.")
{% endhighlight %}

### break (강제 종료)
----------------------------------------------
반복적으로 수행하다가 while문을 빠져나가고 싶은 경우

{% highlight python %}
hit = 0

while True:
    hit = hit + 1
    print("Hit the tree %d times." % hit)

    if hit == 5:
        print("The tree has fallen.")
        break
{% endhighlight %}

### continue (조건 건너뛰기)
-----------------------------------------
아래 문장을 실행하지 않고 처음(조건문)으로 돌아간다.

{% highlight python %}
a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
{% endhighlight %}

### 무한 루프
-------------------------------------
조건이 항상 True → 무한 반복  
break 장치를 만들어야 멈춘다.


{% highlight python %}
while True:
    print("무한 반복 실행")
{% endhighlight %}

### while-else 문
---------------------------------------------
- while 문은 else와 같이 사용할 수 있다.
- 반복문이 문제없이 돌면 else가 실행된다.

주의
- break로 중간에 나가면 else 실행이 안 된다.
- break, countiune → 바로 위 반복문만 제어

{% highlight python %}
# break 사용 → else 실행 안됨
count = 0

while count < 3:
    print("count:", count)   # 현재 count 출력
    count += 1               # count 증가

    if count == 2:
        break                # 조건이 맞으면 반복문 강제 종료
else:
    print("이 문장은 실행되지 않음")  # break가 있으면 실행되지 않음
{% endhighlight %}

### 중첩 while문
---------------------------------------------
- while 문 안에 또 다른 while 문을 사용할 수 있다.
- 바깥 while이 한 번 → 안쪽 while 전체 실행

{% highlight python %}
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
{% endhighlight %}

## 02-3 for문
---------------------------
- while문과 비슷한 반복문이다.
- 리스트, 문자열 같은 반복 가능한 객체의 요소를 하나씩 꺼내서 순서대로 실행한다.

### 요구 사항
- 사용자로부터 문자열을 입력받는다.  
- 입력된 문자열에서 알파벳(a~z, A~Z)의 빈도수를 출력한다.  
- 대소문자는 구분하지 않는다.  
- 알파벳이 아닌 문자는 무시한다.  
- 알파벳은 오름차순으로 정렬하여 출력한다.

### for문 기본 구조
---------------------------------------

{% highlight python %}
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
{% endhighlight %}

### 리스트를 이용한 for문
--------------------------------------

{% highlight python %}
test_list = ['phone', 'two', 'hi'] 
for i in test_list:
    print(i)
{% endhighlight %}

### 조건문과 함께 사용한 for문
----------------------------------------

{% highlight python %}
# 조건에 따라 분기 처리가 가능하다.
fruits = ["apple", "banana", "cherry", "grape"]  # 과일 리스트

index = 0   # 과일 번호를 세기 위한 변수

for fruit in fruits:   # 리스트의 값을 하나씩 fruit에 대입
    index = index + 1   # 번호 1 증가
    
    if fruit == "banana":   # 현재 과일이 banana인지 비교
        print("%d번 과일은 내가 좋아하는 과일입니다." % index)
    else:                   # 그 외의 경우
        print("%d번 과일은 일반 과일입니다." % index)
{% endhighlight %}

### for문과 continue문 사용
---------------------------------------------
continue 문을 만나면 for 문의 처음으로 돌아간다

{% highlight python %}
# continue 문을 만나면 해당 반복을 건너뛰고 다음 반복으로 넘어간다.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue   # num이 3이면 아래 코드 실행하지 않고 다음 반복으로 이동
    
    print(f"현재 숫자: {num}")
{% endhighlight %}

### range 함수 사용
--------------------------
range : 숫자 리스트를 자동으로 만들어주는 함수  
구조 : range(시작_숫자, 끝_숫자) -> 끝 숫자 포함하지 않는다.

{% highlight python %}
# 합계
add = 0

for i in range(1, 11):
    add += i

print(add)

# 구구단(중첩 for문)
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()
{% endhighlight %}

### 리스트 컴프리헨션
-------------------------------------------
for문 안에 리스트 컴프리헨션을 사용하면 직관적인 프로그램을 만들 수 있다.

{% highlight python %}
# 조건을 만족하는 값만 처리
a = [3, 2, 6, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
{% endhighlight %}

### break 문
--------------------------
반복문을 강제로 종료

{% highlight python %}
for i in range(10):
    if i == 5:
        break
    print(i)
{% endhighlight %}

### for else 문
---------------------------------
break 없이 끝나면 else 실행

{% highlight python %}
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"현재 숫자: {num}")
    
    if num == 3:
        break
else:
    print("이 문장은 실행되지 않습니다.")
{% endhighlight %}

### enumerate 함수
------------------------------------
인덱스 순서와 값을 함께 구하고 싶을때 쓰는 함수

{% highlight python %}
# 인덱스와 값을 동시에 가져온다
fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
{% endhighlight %}

### zip 함수
-----------------------------------
여러 리스트를 동시에 순회한다.

{% highlight python %}
fruits = ['apple', 'banana', 'orange']
money = [85, 92, 78]

for fruits, money in zip(fruits,money):
    print(f"{fruits}: {money}")
{% endhighlight %}

# 04장 함수
-----------------------------
입력값을 받아 필요한 작업을 수행한 뒤  결과값울 출력하는 것
- 입력값 → 처리 → 출력값

### 함수의 구조
------------------------------------
- def : 함수를 만드는 키워드
- 함수이름 : 소문자와 언더바(-)를 사용하고 동사로 시작
- 입력값(매개변수) : 함수에 넣는 값
- return : 함수가 실행 결과를 함수 밖으로 반환하는 것

{% highlight python %}
# 함수 기본 구조
# def 함수_이름(매개변수):
#   수행할_문장1
#   수행할_문장2
#    ...
{% endhighlight %}

### 함수 안에서 → 함수 밖 변수 변경하기
----------------------------------------------------
- 숫자, 문자열 같은 자료형은 함수 안에서 바꿔도 외부에 영향이 없다.  
- 리스트나 딕셔너리같이 변경 가능한 자료형은 외부에 영향을 미친다.


-변수 방법 변경하는 2가지 방법-
1. return 사용   
 → 숫자, 문자 값 변경  
 → 여러 값을 반환해도 튜플 1개로 반환된다. ex) return a+b, a*b : (a+b, a*b)  
 → 함수 안에 return이 여러 개 있어도 처음 return만 실행  
 → 값을 안 주고 return만 쓰면 함수 종료
 
2. global 사용: 함수 밖에서 변수를 바꿈  → 권장 x

### retuen 사용하기
------------------------------------

{% highlight python %}
a = 1  # 함수 밖 변수

def increase(x):  # x는 함수 안에서만 사용하는 매개변수
    # 함수 안의 x에 1을 더한 값을 반환
    return x + 1  # 반환값(return) 사용

# 반환값으로 함수 밖 변수 a를 갱신
a = increase(a)  
print(a)
{% endhighlight %}

### global 사용
------------------------------

{% highlight python %}
# 외부 변수 의존과 오류 가능성이 있어 return 사용 권장한다.

a = 1  # 함수 밖 변수

def increase_global():
    global a  # 함수 안에서 외부 변수 a를 직접 사용
    a = a + 1  # 외부 변수 a 값을 1 증가

increase_global()  # 함수 호출
print(a)           # 2
{% endhighlight %}

### 매개변수(parameter)와 인수(arguments)
---------------------------------------------
1. 매개변수
- 함수 정의 시 입력값을 받는 변수

- 기본값 매개변수  
→ 매개변수에 미리 값을 설정하면 입력하지 않아도 자동 적용  
→ 기본값 있는 매개변수는 항상 뒤에 있어야 한다.

2. 인수 
- 함수를 호출 때 실제로 전달하는 값

주의점 
- 입력값이라고 말할 때
 → 같은 의미를 가지 여러 가지 용어 조심  
ex) 입력값 : 함수 정의에서는 매개변수 함수 호출에서는 인수    
    결과값 : 출력값, 리터값 등

{% highlight python %}
# 예제1
# a, b가 매개변수 
# 2, 6이 인수
def add_numbers(a, b):    
    return a + b           # 두 개의 숫자를 더한 결과를 반환

result = add_numbers(2, 6)   # 함수에 3과 4를 넣어 결과를 반환받음
print(result)
{% endhighlight %}

{% highlight python %}
# 기본값 매개변수

def func(name, age, man=True): # 기본값 있는 매개변수는 항상 뒤

def func(name, man=True, age):  # 에러
{% endhighlight %}

### 매개변수 지정하여 호출
------------------------------------------------------------
함수를 호출할때 매개변수 이름 지정 → 순서와 상관없이 값을 전달

{% highlight python %}
def sub(a, b):
    # 첫 번째 수에서 두 번째 수를 뺀 값을 반환
    return a - b

# 매개변수 이름을 지정하여 호출
result = sub(a=7, b=3)
print(result)  # 4

# 순서를 바꿔도 가능
result = sub(b=5, a=3)
print(result)  # -2
{% endhighlight %}

{% highlight python %}
# 예제2
def calculate_average(score1, score2, score3):
    # 세 과목 점수를 모두 더한다
    total = score1 + score2 + score3
    
    # 총점을 과목 수로 나눠 평균 계산
    avg = total / 3
    
    # 계산된 평균값을 함수 밖으로 반환
    return avg


# 함수에 점수를 넣어서 평균 계산
average = calculate_average(80, 90, 100)

# 결과 출력
print(average)  # 90.0
{% endhighlight %}

### 함수의 형태
-------------------------------------
입력값과 반환값 존재 여부 함수 4가지 유형

### 1. 입력값 O, 반환값 O (일반적인 함수)

{% highlight python %}
def greet():   # 입력값 없이 문자열을 반환
    return "Hello, Python!"

message = greet()  # 반환값을 변수에 저장
print(message)
{% endhighlight %}

### 2. 입력값 X, 반환값 O

{% highlight python %}
def get_greeting(): # 입력값 없이 문자열을 반환
    return "Hello!"

message = get_greeting()  # 반환값을 변수에 저장
print(message)
{% endhighlight %}

### 3. 입력값 O, 반환값 X

{% highlight python %}
def show_sum(x, y):  # 두 수의 합을 출력만 하고 반환값은 없음
    print("%d + %d = %d" % (x, y, x + y))

show_sum(7, 8)  # 7 + 8 = 15 출력

result = show_sum(2, 3)
print(result)   # None → 반환값이 없음을 확인
{% endhighlight %}

### 4. 입력값 X, 반환값 X

{% highlight python %}
def say_hi():   # 입력값도 없고 반환값도 없음 → 단순 출력
    print("Hi there!")

say_hi()
{% endhighlight %}

### 입력값이 여러 개인 함수 처리
-------------------------------------------
- *avg(가변 매개변수)   
→ 여러 개의 입력값을 처리할 때  
→ 여러 값을 튜플 형태로 묶어서 받는다.

- **kwargs(키워드 매개변수)   
→ 입력값을 키워드(key=value)  
→ 형태로 받아 딕셔너리로 저장

- 일반 매개변수 + *avg
→ 순서는 일반 매개변수 + *avg로 해야한다.

{% highlight python %}
def add_numbers(base, *args):
    # base : 반드시 하나는 받아야 하는 기본 값 (일반 매개변수)
    # *args : 추가로 들어오는 여러 개의 값들을 튜플로 묶어서 받음

    result = base  # 기본값으로 시작

    # args에 들어있는 값들을 하나씩 꺼내서 더함
    for num in args:
        result += num

    return result  # 최종 결과 반환


# 함수 실행 예시
print(add_numbers(10, 1, 2, 3))
# base=10, args=(1, 2, 3)
# 결과: 16
{% endhighlight %}

- 일반 매개변수 + *avg + **kwargs    
→ 순서는 일반 매개변수 + *avg + **kwargs로 해야한다.

{% highlight python %}
def my_function(name, *args, **kwargs):

    print("이름:", name)

    # args는 튜플 형태 → 반복문으로 하나씩 사용 가능
    print("추가 값들:")
    for value in args:
        print(value)

    # kwargs는 딕셔너리 형태 → key, value로 사용
    print("옵션 정보:")
    for key, value in kwargs.items():
        print(key, ":", value)


# 함수 실행 예시
my_function("철수", 1, 2, 3, age=25, city="서울")
{% endhighlight %}

### lambda 예약어
----------------------------------------
- 함수를 한 줄로 만드는 예약어
- 언제 사용  
→ 함수, def 쓰기 과하지 않을 때
- return 없어도 결과 자동 반환

lambda 구조
- 함수이름 = lambda 매개변수1, 매개변수2, ... : 표현식

{% highlight python %}
# return 없어도 결과 자동 반환
add = lambda a, b: a + b
add(3, 4)  

# def와 동일한 기능
def add(a, b):
    return a + b
{% endhighlight %}

### Docstring(독스트링)
----------------------------------
- 함수 설명 문서화하는 방법

### Docstring 구조
---------------------------------
- (""")로 문자열 작성

{% highlight python %}
def add(a, b):
    """
    두 숫자를 더하는 함수
    Parameters:
        a (int, float): 첫 번째 숫자
        b (int, float): 두 번째 숫자
    Returns:
        int, float: 두 숫자의 합
    """
    return a + b

print(add.__doc__)  # 함수 설명 출력
{% endhighlight %}

## 파일 기초에 입출력
----------------------------------

### 파일 입출력
---------------------------------------
- 파일을 통한 입출력은  데이터 파일을 저장하고 다시 불러오기 위한 방법이다.

### 파일 생성하기
- W(쓰기 모드)
- 파일이 존재하지 않으면 → 새 파일 생성
- 파일이 이미 존재하면 → 기존 내용 삭제 후 새로 작성 (덮어쓰기)

{% highlight python %}
f = open("파일이름",열기 모드)
f.close();
# // 새폴더 안에 있는 새파일을 찾아라
f = open("C:새폴더//파일이름",열기 모드)
f.close();
# 경로를 적을때 /, \,r"" 사용, 새폴더 이름 정확하게
{% endhighlight %}

### 파일을 쓰기 모드로 열어 내용 쓰기
------------------------------------------

f = open("C:새폴더//파일이름",열기 모드)  //C:새폴더//파일이름 -> 이름 짓어내기 print tkdydgkfEO

for i in range(1,11):
 // data = f{i}       // 동일 같음
  data = str(i) +
  f.write(data)

  print("문자열 파일에 쓰기")
  f.write("문자열 파일에 쓰기")

  f.close()

{% highlight python %}
# 구조: f = open("C:새폴더//파일이름",열기 모드)  

f = open("C:/새폴더/파일이름.txt", "w")

f = open("C:/새폴더/파일이름.txt", "w")

for i in range(1, 11):
    # data = f{i}       // data = str(i) +랑 동일 같음
    data = str(i) + "번째 줄입니다.\n"
    f.write(data)

    print("문자열 파일에 쓰기")
    f.write("문자열 파일에 쓰기\n")

f.close()
{% endhighlight %}

### 파일을 일는 방법
-------------------------------

1. readline 함수
→ 파일에 한 번에 한 줄씩 읽을 때 사용한다.
→ 반목문과 함께 사용하면 전체 읽기가 가능하다.
→ 사용 : 파일을 줄 단위로 처리 할 때 유용

2. readlines for문과 연결
→ 파일의 모든 줄을 읽어서 리스트 형태로 변환하는 것
→ 전체 데이터 한 번에 가져와서 처리할 떄 사용한다.
→ 사용 : 반복 처리

3. read()
→ 파일 내용을 통째로 하나의 문자열로 가져오느 것
→ 사용 : 간단한 전체 읽기


{% highlight python %}
# readline 함수
f = open("새파일.txt", "r", encoding="utf-8")

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
{% endhighlight %}

{% highlight python %}
# readlines for문과 연결
f = open("새파일.txt", "r", encoding="utf-8")

lines = f.readlines()

for line in lines:
    print(line)

f.close()
{% endhighlight %}

{% highlight python %}
# read()
f = open("새파일.txt", "r", encoding="utf-8")

data = f.read()
print(data)

f.close()
{% endhighlight %}

### 파일에 새로운 내용 추가하기
--------------------------------------------
- 'a' 모드: 파일 내용을 추가할 때 사용한다.
- 기존 데이터 유지하면서 파일의 맨 뒤에 내용 추가
- 파일 없으면 새 파일 생성

{% highlight python %}
f = open("새파일.txt", "a")

for i in range(11, 20):
    f.write(f"{i}번째 줄입니다.\n")

f.close()
{% endhighlight %}

### with문과 함께 사용
------------------------------------------------------
- whit open() : 파일을 사용한 후  close 따로 호출하지 않아도 자동으로 닫아준다.

{% highlight python %}
with open("파일.txt", "w") as f:
    f.write("Hello Python")
{% endhighlight %}

## apl란
- 서로 다른 시스템으로 주고받거나 기능을 도와주는 시스템
- 요청한 데이터를 보내주는 자동화된 시스템
- 요청한 정보: 딕셔너리 구조와 동일한 구조(필요한 부분만 가져와 사용할 수 있다.)
인덱싱,슬라이시 중요/ 리스트 형식으로 구성() -> 내부 딕셔너리 접근 
대부분의 url은 명확하게 

print(json.dumps(data, indent=3))
dumps -> 보기 좋게 정보를 보여줌
indent는 1,4


###
3가지 Apl 소개 및 활용방법
1. 고양이

주요활용
반화데이터, url, 


###아침 루틴 만들기(Routine 클래스의 routine 메소드)
1. 랜덤 고양이 사진 보여주기(메소드)
2. 오늘 서울 날씨 알려주기(메소드)
3. 오늘의 명언 출력하기(메소드)
4. 추가 기능 제공(자율)

{% highlight python %}
# 1.

import requests
from IPython.display import Image, display

def show_cat_Image():

    url  = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    cat_url = data[0]['url']

    print("오늘의 고양이 사진:")
    display(Image(url=cat_url))

def moring_routune():
    print("아침을 시작합니다.")
    show_cat_Image()

show_cat_Image()
moring_routune()
{% endhighlight %}

{% highlight python %}
#2
import requests
from datetime import datetime

def show_weather():
    latitude = 37.5665
    longitude = 126.9780
    today = datetime.utcnow().date().isoformat() 

    url = (
           f"https://api.open-meteo.com/v1/forecast?"
           f"latitude={latitude}&longitude={longitude}"
           f"&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FSeoul"
)
    response = requests.get(url)
    data = response.json()
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']

    if today in dates:
        idx = dates.index(today)
        print(f"오늘 서울 날씨: 최고 {max_temps[idx]}°C / 최저 {min_temps[idx]}°C")
    else:
        print("오늘 날씨 정보가 없습니다.")

def moring_rountune():
    print("아침을 시작합니다.")
    show_weather()

moring_rountune()
{% endhighlight %}

{% highlight python %}
#3. 
import requests

def show_daily_quote():
             
             quote = "https://zenquotes.io/api/random"
             response = requests.get(quote)
             data = response.json()

             uote = data[0]['q']
             author = data[0]['a']

             print("오늘의 명언:")
             print(f'"{quote}" — {author}')

def moring_routine():
        print("아침을 시작합니다.")
        show_daily_quote()
       
show_daily_quote()
moring_routine()
{% endhighlight %}


  </main>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const content = document.getElementById("docs-content");
  const toc = document.getElementById("toc");
  const searchInput = document.getElementById("docs-search");
  
  // 1. 본문의 H2, H3 태그를 찾아 목차(TOC) 생성
  const headers = content.querySelectorAll("h2, h3");
  let tocHTML = "";
  
  headers.forEach((header, index) => {
    // 앵커(ID) 자동 부여
    const id = "section-" + index;
    header.id = id;
    
    const level = header.tagName.toLowerCase(); // h2 or h3
    const text = header.innerText;
    
    tocHTML += `<li class="toc-${level}"><a href="#${id}" data-text="${text.toLowerCase()}">${text}</a></li>`;
  });
  
  toc.innerHTML = tocHTML;
  
  // 2. 검색(Search) 필터링 기능
  searchInput.addEventListener("input", function() {
    const query = this.value.toLowerCase().trim();
    const tocItems = toc.querySelectorAll("li");
    
    tocItems.forEach(item => {
      const linkText = item.querySelector("a").getAttribute("data-text");
      if (linkText.includes(query)) {
        item.classList.remove("hidden");
      } else {
        item.classList.add("hidden");
      }
    });
  });
});
</script>

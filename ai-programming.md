---
layout: default
title: "인공지능 기초 프로그래밍"
category: courses
author: eunji
---

<style>
  body {
    background-color: #0B1412 !important;
  }
  .gitbook-container {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
    min-height: calc(100vh - 80px);
  }
  
  /* Sidebar */
  .gitbook-sidebar {
    width: 300px;
    background: rgba(15, 23, 42, 0.4);
    border-right: 1px solid rgba(16, 185, 129, 0.15);
    padding: 30px 20px;
    position: sticky;
    top: 80px;
    height: calc(100vh - 80px);
    overflow-y: auto;
    flex-shrink: 0;
  }
  .gitbook-sidebar::-webkit-scrollbar { width: 6px; }
  .gitbook-sidebar::-webkit-scrollbar-thumb { background: rgba(16, 185, 129, 0.3); border-radius: 4px; }
  
  .gitbook-search-wrapper {
    position: relative;
    margin-bottom: 25px;
  }
  .gitbook-search-wrapper i {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    color: #94a3b8;
  }
  #gitbook-search {
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
  #gitbook-search:focus {
    outline: none;
    border-color: #10B981;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
  }
  
  .sidebar-nav {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .nav-category {
    margin-bottom: 8px;
  }
  .nav-category-title {
    color: #cbd5e1;
    font-size: 0.95rem;
    font-weight: 500;
    cursor: pointer;
    padding: 10px 12px;
    border-radius: 6px;
    transition: all 0.2s;
    line-height: 1.4;
  }
  .nav-category-title:hover, .nav-category.active .nav-category-title {
    background: rgba(16, 185, 129, 0.1);
    color: #10B981;
    font-weight: 600;
  }
  
  /* Content Area */
  .gitbook-content-area {
    flex: 1;
    padding: 40px 60px 80px 60px;
    max-width: 1000px;
    color: #e2e8f0;
    line-height: 1.7;
    font-size: 1.05rem;
    overflow-x: hidden;
  }
  .content-section { display: none; animation: fadeIn 0.4s; }
  .content-section.active { display: block; }
  
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  
  .gitbook-content-area h1, .gitbook-content-area h2, .gitbook-content-area h3 {
    color: #f8fafc;
    margin-top: 2em;
    margin-bottom: 0.8em;
    font-family: 'Orbitron', 'Pretendard', sans-serif;
  }
  .gitbook-content-area h1 { border-bottom: 2px solid rgba(16, 185, 129, 0.4); padding-bottom: 15px; color: #10B981; }
  .gitbook-content-area h2 { border-bottom: 1px solid rgba(16, 185, 129, 0.2); padding-bottom: 10px; }
  
    /* Code Block Dark Theme */
  .highlight { background: #1e1e1e !important; color: #d4d4d4 !important; padding: 15px; border-radius: 8px; font-family: 'Consolas', 'Courier New', monospace; font-size: 0.95rem; overflow-x: auto; margin: 20px 0; border: 1px solid rgba(255,255,255,0.1); }
  .highlight .k, .highlight .kv, .highlight .kd, .highlight .kn, .highlight .kp, .highlight .kr, .highlight .kt { color: #569cd6; font-weight: bold; }
  .highlight .s, .highlight .s1, .highlight .s2, .highlight .sb, .highlight .sc { color: #ce9178; }
  .highlight .c, .highlight .c1, .highlight .cm { color: #6a9955; font-style: italic; }
  .highlight .m, .highlight .mi, .highlight .mf, .highlight .mo { color: #b5cea8; }
  .highlight .nf, .highlight .nc { color: #dcdcaa; }
  .highlight .o, .highlight .ow, .highlight .p { color: #d4d4d4; }
  .highlight .err { color: #d4d4d4 !important; background-color: transparent !important; }
  .highlight .n, .highlight .nx, .highlight .nd, .highlight .ni, .highlight .ne, .highlight .nf, .highlight .nl, .highlight .nn, .highlight .nt, .highlight .nv, .highlight .vc, .highlight .vg, .highlight .vi { color: #9cdcfe; }
  .highlight .nb, .highlight .bp { color: #4ec9b0; }
    .highlight code { background: transparent !important; border: none !important; padding: 0 !important; color: inherit !important; box-shadow: none !important; }
  p > code, li > code, td > code { background: rgba(30, 30, 30, 0.8); padding: 3px 6px; border-radius: 4px; color: #4ec9b0; font-family: 'Consolas', monospace; font-size: 0.9em; border: 1px solid rgba(255,255,255,0.1); }
  
  /* Console Output Box */
  .console-output {
    background: #0f172a;
    color: #94a3b8;
    padding: 12px 15px;
    border-radius: 0 0 8px 8px;
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-top: none;
    font-family: 'Consolas', monospace;
    font-size: 0.85rem;
    white-space: pre-wrap;
    margin-top: -20px;
    margin-bottom: 25px;
  }
  
  /* Image Output */
  .output-img-container {
    background: #ffffff;
    padding: 15px;
    border-radius: 8px;
    margin-top: -10px;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    text-align: center;
  }
  .output-img-container img {
    max-width: 100%;
    height: auto;
  }

    /* Search Results View - Accordion */
  .code-accordion { background: #1e293b; border: 1px solid #334155; border-radius: 8px; margin-bottom: 15px; overflow: hidden; }
  .code-accordion summary { padding: 15px 20px; background: #0f172a; color: #10b981; font-weight: 600; cursor: pointer; list-style: none; position: relative; font-size: 1.1rem; outline: none; transition: background 0.2s; }
  .code-accordion summary:hover { background: #1e293b; }
  .code-accordion summary::-webkit-details-marker { display: none; }
  .code-accordion summary::after { content: '▼'; position: absolute; right: 20px; top: 15px; font-size: 0.9rem; color: #94a3b8; transition: transform 0.3s; }
  .code-accordion[open] summary::after { transform: rotate(180deg); }
  .accordion-content { padding: 20px; border-top: 1px solid #334155; background: #0B1412; }
  
  .search-result-snippet { color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; word-break: break-all; }
  .search-result-snippet mark { background-color: rgba(250, 204, 21, 0.8); color: #0f172a; padding: 0 3px; font-weight: bold; }
  .hidden-section { display: none !important; }
  .go-to-doc-btn { display: inline-block; margin-top: 15px; padding: 8px 16px; background: rgba(16, 185, 129, 0.1); color: #10B981; border: 1px solid #10B981; border-radius: 6px; cursor: pointer; font-size: 0.9rem; font-weight: 600; transition: all 0.2s; }
  .go-to-doc-btn:hover { background: #10B981; color: #0f172a; }

  /* Home Banner */
  .home-banner {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(15, 23, 42, 0) 100%);
    border: 1px solid rgba(16, 185, 129, 0.2);
    border-radius: 16px;
    padding: 60px 40px;
    text-align: center;
    margin-top: 40px;
  }
  .home-banner h1 { color: #10B981; margin-bottom: 20px; font-weight: 700; }
  .home-banner p { color: #cbd5e1; margin: 0; font-size: 1.15rem; line-height: 1.6; }
</style>

<div style="padding: 20px 40px 0 40px; max-width: 1400px; margin: 0 auto; font-size: 1.15rem; font-family: 'Orbitron', 'Pretendard', sans-serif;">
  <a href="{{ site.baseurl }}/" style="color: #10B981; text-decoration: none; font-weight: 600;">Home</a> 
  <span style="color: #64748b; margin: 0 10px;">/</span> 
  <span style="color: #10B981;">인공지능 기초 프로그래밍</span>
</div>

<div class="gitbook-container">

<style>
</style>

<!-- Sidebar -->
  <aside class="gitbook-sidebar">
    <div class="gitbook-search-wrapper">
      <i class="uil uil-search"></i>
      <input type="text" id="gitbook-search" placeholder="Search">
    </div>
    
    <ul class="sidebar-nav">

      <li class="nav-category" id="nav-ai-cat-0">
        <div class="nav-category-title" onclick="openCategory('ai-cat-0')">1. 선형회귀분석</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-1">
        <div class="nav-category-title" onclick="openCategory('ai-cat-1')">2. 다중회귀분석_공부시간시험성적</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-2">
        <div class="nav-category-title" onclick="openCategory('ai-cat-2')">2. 앙상블_랜덤포레스트_과일종류맞추기</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-3">
        <div class="nav-category-title" onclick="openCategory('ai-cat-3')">3. 군집분석_KMeans</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-4">
        <div class="nav-category-title" onclick="openCategory('ai-cat-4')">4. 군집분석_DBSCAN</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-5">
        <div class="nav-category-title" onclick="openCategory('ai-cat-5')">5. 로지스틱회귀분석</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-6">
        <div class="nav-category-title" onclick="openCategory('ai-cat-6')">7. KNN_수박_참외_맞추기</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-7">
        <div class="nav-category-title" onclick="openCategory('ai-cat-7')">8. K_Fold_교차검증</div>
      </li>

      <li class="nav-category" id="nav-ai-cat-8">
        <div class="nav-category-title" onclick="openCategory('ai-cat-8')">9. 그리드서치</div>
      </li>
      <li class="nav-category" id="nav-ai-cat-9">
        <div class="nav-category-title" onclick="openCategory('ai-cat-9')">10. 실습1_신용카드이상탐지</div>
      </li>

    </ul>
  </aside>

  <!-- Main Content -->
  <main class="gitbook-content-area">
    <div id="content-home" class="content-section active">
      <div class="home-banner">
        <h1>인공지능 기초 프로그래밍</h1>
        <p>머신러닝의 핵심 알고리즘 이론과 파이썬 실습 코드를 통합한 전용 공간입니다.<br>좌측 메뉴에서 학습할 모델을 선택하거나 검색창을 이용해보세요.</p>
      </div>
    </div>
<div id="content-ai-cat-0" class="content-section" markdown="1">
# 1. 선형회귀분석

# Google Colab 데이터 로드

```python
#Step 1. 구글 코랩에 한글 폰트 설정하기
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```
<pre class="console-output">Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
'rm' is not recognized as an internal or external command,
operable program or batch file.
</pre>
```python
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
study = pd.read_csv(io.BytesIO(myfile['공부시간과시험점수.csv']),
                       encoding='cp949')
study
```
```python
import os

print(os.listdir(r'C:\Users\user\Desktop\목\머신러닝실습용자료'))
```
# 이름 -> 의미 없음 분석 때 사용하지 않는 데이터
# 공부시간 -> featrue (특징)
# 시험점수 -> target(예측결과)

# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
study = pd.read_csv('./머신러닝실습용자료/공부시간과시험점수.csv',encoding='cp949')
study
```
<pre class="console-output">       이름  공부시간  시험점수
0     이원재  15.0  85.0
1     맹승주  14.5  86.5
2     안미경  14.0  86.0
3     서진수  13.5  85.5
4     황경인  13.0  85.0
5     신운무  12.0  83.0
6      권율  12.0  85.0
7      강준  11.0  82.0
8    신사임당  11.0  83.0
9     문무왕  10.5  82.0
10    김지희  10.5  81.5
11    임기승  10.0  82.0
12    강감찬  10.0  81.0
13  광개토대왕   9.5  78.0
14    이세혁   9.3  77.4
15    전우치   9.0  77.0
16    이순신   9.0  76.0
17    정진교   8.5  75.5
18   계백장군   8.5  76.0
19    왕광환   8.4  75.5
20    홍길동   8.2  75.0
21    곽재우   8.0  74.5
22    김유신   7.5  74.0
23    이승우   7.5  73.5
24    일지매   7.0  73.0</pre>
# 공통 실습 코드

```python
# data, target 정의
data = study['공부시간']
target = study['시험점수']

# 산점도 그리기
import matplotlib.pyplot as plt
plt.plot(data,target,'o')
plt.show()
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_0_8_0.png" alt="Result Graph"></div>

```python
from sklearn.model_selection import train_test_split
import numpy as np

# train, test 데이터 나누기 위해 numpy로 변경
data = study['공부시간'].to_numpy()
target = study['시험점수'].to_numpy()

# 훈련 세트와 테스트 세트로 나눕니다.
from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(
    data, target, test_size=0.2, random_state=40
)
```
```python
# 1차원 -> 2차원 변형
# scikit-learn의 입력값은 2차원 배열 형태여야 하므로 reshape(-1, 1)을 사용
import numpy as np

data = study['공부시간'].to_numpy()
target = study['시험점수'].to_numpy()

from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target, test_size=0.2, random_state=40)
```
```python
# shape 확인
훈련용_data = 훈련용_data.reshape(-1, 1)
테스트용_data = 테스트용_data.reshape(-1, 1)

print("훈련용 데이터 크기:", 훈련용_data.shape)
```
<pre class="console-output">훈련용 데이터 크기: (20, 1)
</pre>
```python
# data 전체 확인
훈련용_data
# reshape 함수에 -1을 넣으면, rows은 자동으로 입력해달라는 뜻
# 즉, column을 1개로 내가 정했으니, 남은 데이터는 알아서 row에 잘 넣어주세요.
#자동으로 가로로 되어있으니 세로로 바꿔달라는 코드
훈련용_data = 훈련용_data.reshape(-1,1)
테스트용_data = 테스트용_data.reshape(-1,1)
# shape 확인
훈련용_data
# 선형회귀모델 학습
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(훈련용_data , 훈련용_target)
# 점수 확인(lr.score는 결정계수R2에 대한 정확도를 의미합니다.)
print("훈련 세트 점수 r2:",lr.score(훈련용_data , 훈련용_target))
print("테스트 세트 점수 r2:",lr.score(테스트용_data , 테스트용_target))
```
<pre class="console-output">훈련 세트 점수 r2: 0.8869114576908868
테스트 세트 점수 r2: 0.83676625848856
</pre>
```python
# reshape 함수에 -1을 넣으면, rows은 자동으로 입력해달라는 뜻
# 즉, column을 1개로 내가 정했으니, 남은 데이터는 알아서 row에 잘 넣어주세요.
훈련용_data = 훈련용_data.reshape(-1,1)
테스트용_data = 테스트용_data.reshape(-1,1)
```
```python
# shape 확인
훈련용_data.shape
```
<pre class="console-output">(20, 1)</pre>
```python
# data 전체 확인
훈련용_data
```
<pre class="console-output">array([[13.5],
       [ 8. ],
       [14. ],
       [10. ],
       [ 8.5],
       [13. ],
       [11. ],
       [ 9. ],
       [ 7.5],
       [ 8.2],
       [15. ],
       [10.5],
       [10.5],
       [ 7.5],
       [10. ],
       [14.5],
       [ 8.5],
       [12. ],
       [11. ],
       [12. ]])</pre>
```python
# 선형회귀모델 학습
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(훈련용_data, 훈련용_target)
```
<pre class="console-output">LinearRegression()</pre>
```python
# 점수 확인(lr.score는 결정계수R2에 대한 정확도를 의미합니다.)
print(lr.score(훈련용_data , 훈련용_target))
print(lr.score(테스트용_data , 테스트용_target))
```
<pre class="console-output">0.8869114576908868
0.83676625848856
</pre>
```python
# 16이라는 값을 넣었을 때 예상 결과값 확인
lr.predict([[16]])
```
<pre class="console-output">array([90.12423029])</pre>
```python
# 16시간 공부 시 예측 점수
print("16시간 공부 예측 점수:", lr.predict([[16]]))
```
<pre class="console-output">16시간 공부 예측 점수: [90.12423029]
</pre>
```python
# 회귀계수 확인
print(lr.coef_, lr.intercept_)
```
<pre class="console-output">[1.80042161] 61.31748460585439
</pre>
```python
import matplotlib.pyplot as plt
plt.scatter(훈련용_data , 훈련용_target)
plt.plot( [5,18], [5*lr.coef_ +lr.intercept_ ,
                    18*lr.coef_ + lr.intercept_])
plt.scatter(16 , 90 ,marker="^")
plt.show()
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_0_21_0.png" alt="Result Graph"></div>

## 다항회귀분석 적용

```python
# 다항회귀분석 적용
import numpy as np
훈련용_data_poly = np.column_stack(( 훈련용_data ** 2, 훈련용_data))
테스트용_data_poly = np.column_stack((테스트용_data ** 2 , 테스트용_data))

lr = LinearRegression()
lr.fit(훈련용_data_poly , 훈련용_target)
lr.score(테스트용_data_poly , 테스트용_target)
```
<pre class="console-output">0.5052713132458201</pre>
```python
lr.predict([[16**2,16]])
```
<pre class="console-output">array([85.24161226])</pre>
```python
print(lr.score(훈련용_data_poly , 훈련용_target))
print(lr.score(테스트용_data_poly , 테스트용_target))
```
<pre class="console-output">0.9686934811074568
0.5052713132458201
</pre>

</div>
<div id="content-ai-cat-1" class="content-section" markdown="1">
# 2. 다중회귀분석_공부시간시험성적

# Google Colab 데이터 로드

```python
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
study = pd.read_csv(io.BytesIO(myfile['공부시간과시험점수2.csv']),
                       encoding='cp949')
study
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
study = pd.read_csv('./머신러닝실습용자료/공부시간과시험점수2.csv',encoding='cp949')
study
```
<pre class="console-output">       이름  공부시간  학원수  과외여부  시험점수
0     이원재  15.0    5     1  89.0
1     맹승주  14.5    5     0  86.5
2     안미경  14.0    5     1  86.0
3     서진수  13.5    4     1  85.5
4     황경인  13.0    4     0  85.0
5     신운무  12.0    4     1  83.0
6      권율  12.0    3     1  85.0
7      강준  11.0    3     0  82.0
8    신사임당  11.0    3     0  83.0
9     문무왕  10.5    3     1  82.0
10    김지희  10.5    2     1  81.5
11    임기승  10.0    2     1  82.0
12    강감찬  10.0    2     0  81.0
13  광개토대왕   9.5    2     0  78.0
14    이세혁   9.3    2     1  77.4
15    전우치   9.0    2     0  77.0
16    이순신   9.0    1     0  76.0
17    정진교   8.5    1     1  75.5
18   계백장군   8.5    1     0  76.0
19    왕광환   8.4    1     1  75.5
20    홍길동   8.2    1     0  75.0
21    곽재우   8.0    1     1  74.5
22    김유신   7.5    1     0  74.0
23    이승우   7.5    1     1  73.5
24    일지매   7.0    1     0  73.0</pre>
# 공통 실습 코드

```python
#Step 2: 훈련용 데이터셋과 테스트용 데이터셋 나누어서 분석
from sklearn.model_selection import train_test_split

# data, target 지정
# 다중회귀분석의 경우 data를 여러개 설정.
data = study[['공부시간', '학원수','과외여부']]
target = study['시험점수']

# train, test 데이터 분리

훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target, test_size=0.2, random_state=40)
```
```python
# 선형회귀분석 학습
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(훈련용_data, 훈련용_target)

# 13, 5, 0이라는 값을 넣어 예측
lr.predict([[13,5,0]])
```
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
  warnings.warn(
</pre>
<pre class="console-output">array([84.86657458])</pre>
```python
# 테스트 데이터로 스코어 확인
lr.score(테스트용_data , 테스트용_target)
```
<pre class="console-output">0.8967399286768529</pre>

</div>
<div id="content-ai-cat-2" class="content-section" markdown="1">
# 2. 앙상블_랜덤포레스트_과일종류맞추기

# Google Colab 데이터 로드

```python
#Step 1. 구글 코랩에 한글 폰트 설정하기

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```
<pre class="console-output">Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
'rm' is not recognized as an internal or external command,
operable program or batch file.
</pre>
```python
#Step 2.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
과일채소목록 = pd.read_csv(io.BytesIO(myfile['과일채소목록.csv']),
                       encoding='cp949')
과일채소목록
```
# 로컬 데이터 로드

# 공통 실습 코드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
src_data = pd.read_csv('../머신러닝실습용자료/과일채소목록.csv',encoding='cp949')
src_data
```
<pre class="console-output">      종류  무게_g  길이_cm  색상   당도
0     수박  2000   30.0   1  8.0
1     수박  2500   25.0   1  7.0
2     수박  1800   20.0   1  6.5
3     수박  1500   16.0   1  8.5
4     수박  2200   21.0   1  9.5
5     자두   100    3.5   3  6.0
6     자두   120    3.7   3  7.0
7     자두    90    2.8   3  8.0
8     자두   150    3.8   3  8.5
9     자두   110    3.6   3  7.5
10    참외   500    8.0   2  8.0
11    참외   400    7.5   2  7.2
12    참외   450    8.0   2  7.5
13    참외   400    6.5   2  6.5
14    참외   600    8.5   2  8.0
15   옥수수   450   20.0   1  3.0
16   옥수수   500   25.0   1  2.0
17   옥수수   380   22.0   1  1.5
18   옥수수   400   23.0   1  1.0
19   옥수수   350   20.0   1  1.3
20  거봉포도   280   28.0   3  8.0
21  거봉포도   250   25.0   3  7.5
22  거봉포도   220   22.0   3  7.0
23  거봉포도   270   26.0   3  8.5
24  거봉포도   290   29.0   3  9.0
25    수박  2001   30.5   1  8.1
26    수박  2501   25.1   1  7.1
27    수박  1801   20.1   1  6.6
28    수박  1501   16.1   1  8.6
29    수박  2201   21.1   1  9.6
30    자두   101    3.6   3  6.1
31    자두   121    3.8   3  7.1
32    자두    91    2.9   3  8.1
33    자두   151    3.9   3  8.6
34    자두   111    3.7   3  7.6
35    참외   501    8.1   2  8.1
36    참외   401    7.6   2  7.3
37    참외   451    8.1   2  7.6
38    참외   401    6.6   2  6.6
39    참외   601    8.6   2  8.1
40   옥수수   451   20.1   1  3.1
41   옥수수   501   25.1   1  2.1
42   옥수수   381   22.1   1  1.6
43   옥수수   401   23.1   1  1.1
44   옥수수   351   20.1   1  1.4
45  거봉포도   281   28.1   3  8.1
46  거봉포도   251   25.1   3  7.6
47  거봉포도   221   22.1   3  7.1
48  거봉포도   271   26.1   3  8.6
49  거봉포도   291   29.1   3  9.1</pre>
```python
#Step 3. 훈련용 세트와 테스트용 세트로 나눕니다.
# '무게_g','길이_cm','색상','당도'에 따른 과일종류 분류
data = src_data[['무게_g','길이_cm','색상','당도']]
target = src_data['종류']

# train, test 데이터 분리
from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target, test_size=0.3, random_state=40)
```
```python
# 각각의 데이터 확인
print(훈련용_data.shape , 테스트용_data.shape)
print(훈련용_data)
print(훈련용_target)
```
<pre class="console-output">(35, 4) (15, 4)
    무게_g  길이_cm  색상   당도
41   501   25.1   1  2.1
23   270   26.0   3  8.5
36   401    7.6   2  7.3
5    100    3.5   3  6.0
13   400    6.5   2  6.5
39   601    8.6   2  8.1
17   380   22.0   1  1.5
43   401   23.1   1  1.1
24   290   29.0   3  9.0
3   1500   16.0   1  8.5
22   220   22.0   3  7.0
40   451   20.1   1  3.1
26  2501   25.1   1  7.1
34   111    3.7   3  7.6
20   280   28.0   3  8.0
28  1501   16.1   1  8.6
14   600    8.5   2  8.0
15   450   20.0   1  3.0
30   101    3.6   3  6.1
8    150    3.8   3  8.5
46   251   25.1   3  7.6
32    91    2.9   3  8.1
9    110    3.6   3  7.5
48   271   26.1   3  8.6
42   381   22.1   1  1.6
10   500    8.0   2  8.0
31   121    3.8   3  7.1
19   350   20.0   1  1.3
47   221   22.1   3  7.1
12   450    8.0   2  7.5
1   2500   25.0   1  7.0
37   451    8.1   2  7.6
7     90    2.8   3  8.0
27  1801   20.1   1  6.6
6    120    3.7   3  7.0
41     옥수수
23    거봉포도
36      참외
5       자두
13      참외
39      참외
17     옥수수
43     옥수수
24    거봉포도
3       수박
22    거봉포도
40     옥수수
26      수박
34      자두
20    거봉포도
28      수박
14      참외
15     옥수수
30      자두
8       자두
46    거봉포도
32      자두
9       자두
48    거봉포도
42     옥수수
10      참외
31      자두
19     옥수수
47    거봉포도
12      참외
1       수박
37      참외
7       자두
27      수박
6       자두
Name: 종류, dtype: str
</pre>
```python
from sklearn.ensemble import RandomForestClassifier
# 랜덤 포레스트 모델 생성
rf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=40) #n_estimators : 트리의 개수, n_jobs : 사용할 CPU 코어 수, random_state : 랜덤 시드 설정

# 학습
rf.fit(훈련용_data, 훈련용_target)

# 예측
print(rf.predict(테스트용_data))

# score
print(rf.score(테스트용_data, 테스트용_target))
```
<pre class="console-output">['자두' '수박' '거봉포도' '참외' '거봉포도' '수박' '옥수수' '수박' '참외' '수박' '옥수수' '참외' '수박'
 '거봉포도' '옥수수']
1.0
</pre>
### 결과표 작성 및 시각화

```python
# 테스트 데이터 확인
테스트용_data
```
<pre class="console-output">    무게_g  길이_cm  색상   당도
33   151    3.9   3  8.6
29  2201   21.1   1  9.6
49   291   29.1   3  9.1
38   401    6.6   2  6.6
45   281   28.1   3  8.1
0   2000   30.0   1  8.0
18   400   23.0   1  1.0
4   2200   21.0   1  9.5
11   400    7.5   2  7.2
2   1800   20.0   1  6.5
16   500   25.0   1  2.0
35   501    8.1   2  8.1
25  2001   30.5   1  8.1
21   250   25.0   3  7.5
44   351   20.1   1  1.4</pre>
```python
from sklearn.metrics import classification_report

#예측 
pred = rf.predict(테스트용_data)

#리포트 출력 
print(classification_report(테스트용_target, pred))
```
<pre class="console-output">              precision    recall  f1-score   support

        거봉포도       1.00      1.00      1.00         3
          수박       1.00      1.00      1.00         5
         옥수수       1.00      1.00      1.00         3
          자두       1.00      1.00      1.00         1
          참외       1.00      1.00      1.00         3

    accuracy                           1.00        15
   macro avg       1.00      1.00      1.00        15
weighted avg       1.00      1.00      1.00        15

</pre>
```python
# 예측결과 데이터프레임을 만들고
예측결과 = pd.DataFrame(rf.predict(테스트용_data), columns=['예측결과'])

# concat을 통해 기존 테스트 data와 예측결과 데이터를 합친다.
result = pd.concat([테스트용_data.reset_index(drop=True), 예측결과], axis=1)
result
```
<pre class="console-output">    무게_g  길이_cm  색상   당도  예측결과
0    151    3.9   3  8.6    자두
1   2201   21.1   1  9.6    수박
2    291   29.1   3  9.1  거봉포도
3    401    6.6   2  6.6    참외
4    281   28.1   3  8.1  거봉포도
5   2000   30.0   1  8.0    수박
6    400   23.0   1  1.0   옥수수
7   2200   21.0   1  9.5    수박
8    400    7.5   2  7.2    참외
9   1800   20.0   1  6.5    수박
10   500   25.0   1  2.0   옥수수
11   501    8.1   2  8.1    참외
12  2001   30.5   1  8.1    수박
13   250   25.0   3  7.5  거봉포도
14   351   20.1   1  1.4   옥수수</pre>
```python
# k-fold 교차 검증
from sklearn.model_selection import cross_validate


# cross_validate() : 검사 결과를 자세하게 보여주는 것
scores = cross_validate(rf, data, target, cv=5, return_train_score=True)
print(scores)

```
<pre class="console-output">{'fit_time': array([0.1641922 , 0.14757276, 0.15310121, 0.13394785, 0.13378429]), 'score_time': array([0.03254294, 0.03168344, 0.03171182, 0.03411293, 0.03009343]), 'test_score': array([1., 1., 1., 1., 1.]), 'train_score': array([1., 1., 1., 1., 1.])}
</pre>
```python
# 중요 속성 지표값 출력

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
font_location = "C:/Windows/Fonts/malgun.ttf"
#plt.rc('font', family='NanumBarunGothic')


# 혹시 위 폰트가 에러 날 경우 폰트 사용하면 됩니다
font_name = fm.FontProperties(fname = font_location).get_name()
matplotlib.rc('font', family=font_name)

imp = rf.feature_importances_
print('중요속성지표값:',imp)

plt.figure()
plt.bar(range(len(imp)),imp)
plt.xticks(range(len(imp)),data.columns, rotation=90)
plt.show()
```
<pre class="console-output">중요속성지표값: [0.31303771 0.29685569 0.22213184 0.16797476]
</pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_2_14_1.png" alt="Result Graph"></div>


</div>
<div id="content-ai-cat-3" class="content-section" markdown="1">
# 3. 군집분석_KMeans

# Google Colab 데이터 로드

```python
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
fruits = pd.read_csv(io.BytesIO(myfile['과일3개.csv']),
                       encoding='cp949')
fruits
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
fruits = pd.read_csv('../머신러닝실습용자료/과일3개.csv',encoding='cp949')
fruits
```
<pre class="console-output">    종류  무게_g  길이_cm   당도
0   수박  2000   30.0  8.0
1   수박  2500   25.0  7.0
2   수박  1800   20.0  6.5
3   수박  1500   16.0  8.5
4   수박  2200   21.0  9.5
5   자두   100    3.5  6.0
6   자두   120    3.7  7.0
7   자두    90    2.8  8.0
8   자두   150    3.8  8.5
9   자두   110    3.6  7.5
10  참외   500    8.0  8.0
11  참외   400    7.5  7.2
12  참외   450    8.0  7.5
13  참외   400    6.5  6.5
14  참외   600    8.5  8.0</pre>
# 공통 실습 코드

```python
# Step 2.데이터의 분포를 그림으로 그리고 임의의 중심점 지정
import matplotlib.pyplot as plt
x1,y1 = 2000, 22
x2,y2 = 200, 2.5
x3,y3 = 500, 10

data = fruits[['무게_g','길이_cm']]
plt.figure(figsize=(7,5))
plt.title("Before", fontsize=15)
plt.plot(data["무게_g"], data["길이_cm"], "o", label="Data")
plt.plot([x1,x2,x3], [y1,y2,y3], "rD", \
         marker='*', markersize=12, label='init_Centroid')
plt.xlabel("Weight", fontsize=12)
plt.ylabel("Length", fontsize=12)
plt.legend()
plt.grid()
plt.show()
```
<pre class="console-output">C:\Users\user\AppData\Local\Temp\ipykernel_1896\4249871694.py:11: UserWarning: marker is redundantly defined by the 'marker' keyword argument and the fmt string "rD" (-> marker='D'). The keyword argument will take precedence.
  plt.plot([x1,x2,x3], [y1,y2,y3], "rD", \
</pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_3_5_1.png" alt="Result Graph"></div>

```python
# Step 3. 군집 분석을 수행합니다.
from sklearn.cluster import KMeans
import numpy as np

# 군집 분석은 비지도학습이기에, target이 없습니다.
data = fruits[['무게_g','길이_cm']]

#초기의 점을 지정할 경우
kmeans = KMeans(n_clusters=3, init = np.array([(x1,y1),(x2,y2),(x3,y3)]))

#초기의 점을 지정하지 않을 경우
#kmeans = KMeans(n_clusters=3)

# 모델 학습
kmeans.fit(data)

# k-means의 라벨과, 중심점 좌표 가져오기
data['cluster'] = kmeans.labels_
final_centroid = kmeans.cluster_centers_
```
```python
data
```
<pre class="console-output">    무게_g  길이_cm  cluster
0   2000   30.0        0
1   2500   25.0        0
2   1800   20.0        0
3   1500   16.0        0
4   2200   21.0        0
5    100    3.5        1
6    120    3.7        1
7     90    2.8        1
8    150    3.8        1
9    110    3.6        1
10   500    8.0        2
11   400    7.5        2
12   450    8.0        2
13   400    6.5        2
14   600    8.5        2</pre>
```python
#Step 4. 군집화를 진행하여 최종 결과를 확인합니다.
plt.figure(figsize=(7,5))
plt.title("After", fontsize=15)
plt.scatter(data['무게_g'],data['길이_cm'],c=data['cluster'])
plt.plot(final_centroid[:,0], final_centroid[:,1], "rD", \
         marker='*',markersize=12, label='final_Centroid')
plt.xlabel("Weight", fontsize=12)
plt.ylabel("Length", fontsize=12)
plt.legend()
plt.grid()
plt.show()
```
<pre class="console-output">C:\Users\user\AppData\Local\Temp\ipykernel_1896\379812364.py:5: UserWarning: marker is redundantly defined by the 'marker' keyword argument and the fmt string "rD" (-> marker='D'). The keyword argument will take precedence.
  plt.plot(final_centroid[:,0], final_centroid[:,1], "rD", \
</pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_3_8_1.png" alt="Result Graph"></div>

```python
# 각각의 요소에 대한 라벨 출력
print(kmeans.labels_)
```
<pre class="console-output">[0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
</pre>
```python
# [500, 20] 데이터 넣었을 때 예측값 확인
kmeans.predict([[500, 20]])
```
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but KMeans was fitted with feature names
  warnings.warn(
</pre>
<pre class="console-output">array([2], dtype=int32)</pre>
```python
# [1700, 15] 데이터 넣었을 때 예측값 확인
kmeans.predict([[1700, 15]])
```
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but KMeans was fitted with feature names
  warnings.warn(
</pre>
<pre class="console-output">array([0], dtype=int32)</pre>
```python
# 클러스터 중심과 클러스터에 속한 샘플 사이의 거리의 제곱 합 출력
print(kmeans.inertia_)
```
<pre class="console-output">610236.1279999999
</pre>
```python
#최적의 군집 개수 찾기 - Elbow Method
import matplotlib.pyplot as plt

inertia = [ ]
for i in range(2,15) :
  km = KMeans(n_clusters=i)
  km.fit(data)
  inertia.append(km.inertia_)
plt.plot(range(2,15) , inertia)
plt.show()
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_3_13_0.png" alt="Result Graph"></div>


</div>
<div id="content-ai-cat-4" class="content-section" markdown="1">
# 4. 군집분석_DBSCAN

# 테스트 데이터 생성

```python
#Step 1. 테스트용 데이터를 생성합니다.
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons

X,y = make_moons(n_samples=400 , noise = 0.1 , random_state=10)
plt.scatter(X[ :, 0] , X[ : , 1])
plt.show()
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_1_0.png" alt="Result Graph"></div>

# 테스트 코드

```python
#Step 2. Clustering 진행 정도를 보여줄 시각화함수를 생성합니다.
def cluster_result(X , y , title) :
  plt.scatter( X[y==0,0] , X[y==0,1] , c='green' , marker='o' , s=40 ,
              label="Cluster_1")
  plt.scatter( X[y==1,0] , X[y==1,1] , c='red' , marker='s' , s=40 ,
              label="Cluster_2")
  plt.title(title)
  plt.legend()
  plt.show()
```
```python
# Step 3. KMeans 클러스터링을 진행합니다.
from sklearn.cluster import KMeans

# 모델 생성(n_clusters=2, random_state=10)
km = KMeans(n_clusters=2, random_state=10)

# 모델 학습
y_km = km.fit_predict(X)

# 시각화 함수 출력
cluster_result(X, y_km, title='k-means')
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_4_0.png" alt="Result Graph"></div>

```python
# Step 4. DBSCAN 클러스터링을 진행합니다.
from sklearn.cluster import DBSCAN

# 모델 생성(eps=0.2, min_samples=15, metric='euclidean')
db = DBSCAN(eps=0.2, min_samples=15, metric='euclidean')

# 모델 학습
y_db = db.fit_predict(X)

# 시각화 함수 출력
cluster_result(X, y_db, title='DBSCAN')
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_5_0.png" alt="Result Graph"></div>

```python
plt.scatter( X[y==0,0] , X[y==0,1] , c='green' , marker='o' , s=40 ,
            label="Cluster_1")
```
<pre class="console-output"><matplotlib.collections.PathCollection at 0x250279e1d10></pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_6_1.png" alt="Result Graph"></div>

```python
plt.scatter( X[y==1,0] , X[y==1,1] , c='red' , marker='s' , s=40 ,
            label="Cluster_2")
```
<pre class="console-output"><matplotlib.collections.PathCollection at 0x2502592ac10></pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_7_1.png" alt="Result Graph"></div>

# 실습 코드

```python
### 클러스터 결과를 담은 DataFrame과 사이킷런의 Cluster 객체등을 인자로 받아 클러스터링 결과를 시각화하는 함수  
def vis_cluster_plot(clusterobj, dataframe, label_name, iscenter=True):
    if iscenter :
        centers = clusterobj.cluster_centers_
        
    unique_labels = np.unique(dataframe[label_name].values)
    markers=['o', 's', '^', 'x', '*']
    isNoise=False

    for label in unique_labels:
        label_cluster = dataframe[dataframe[label_name]==label]
        if label == -1:
            cluster_legend = 'Noise'
            isNoise=True
        else :
            cluster_legend = 'Cluster '+str(label)
        
        plt.scatter(x=label_cluster['trans1'], y=label_cluster['trans2'], s=70,\
                    edgecolor='k', marker=markers[label], label=cluster_legend)
        
        if iscenter:
            center_x_y = centers[label]
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=250, color='white',
                        alpha=0.9, edgecolor='k', marker=markers[label])
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k',\
                        edgecolor='k', marker='$%d$' % label)
    if isNoise:
        legend_loc='upper center'
    else: legend_loc='upper right'
    
    plt.legend(loc=legend_loc)
    plt.show()
```
```python
# 실험을 위한 데이터 생성
from sklearn.datasets import make_circles
import pandas as pd
import numpy as np

# 2개의 원 그리는 코드
X, y = make_circles(n_samples=1000, shuffle=True, noise=0.05, random_state=0, factor=0.5)
clusterDF = pd.DataFrame(data=X, columns=['trans1', 'trans2'])
clusterDF['target'] = y

# 그린 원 시각화
vis_cluster_plot(None, clusterDF, 'target', iscenter=False)
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_10_0.png" alt="Result Graph"></div>

```python
# KMeans로 make_circles() 데이터 셋을 클러스터링 수행.
from sklearn.cluster import KMeans

# KMeans 군집분석 객체 생성 k=2
kmeans = KMeans(n_clusters=2, max_iter=100, random_state=0)

# X에 대해 학습
kmeans_labels = kmeans.fit_predict(X)

# 학습 결과 저장
clusterDF['kmeans_cluster'] = kmeans_labels

# 시각화
vis_cluster_plot(kmeans, clusterDF, 'kmeans_cluster', iscenter=True)
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_11_0.png" alt="Result Graph"></div>

```python
# DBSCAN으로 make_circles() 데이터 셋을 클러스터링 수행.
from sklearn.cluster import DBSCAN

# DBSCAN 군집분석 객체 생성()
dbscan = DBSCAN(min_samples=25, metric='euclidean')

# X에 대해 학습
dbscan_labels = dbscan.fit_predict(X)

# 학습 결과 저장
clusterDF['dbscan_cluster'] = dbscan_labels

# 시각화
vis_cluster_plot(dbscan, clusterDF, 'dbscan_cluster', iscenter=False)
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_4_12_0.png" alt="Result Graph"></div>


</div>
<div id="content-ai-cat-5" class="content-section" markdown="1">
# 5. 로지스틱회귀분석

# Google Colab 데이터 로드

```python
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
study = pd.read_csv(io.BytesIO(myfile['공부시간과시험합격.csv']),
                       encoding='cp949')
study
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
study = pd.read_csv('./머신러닝실습용자료/공부시간과시험합격.csv',encoding='cp949')
study
```
<pre class="console-output">       이름  공부시간  시험점수 합격여부
0     이원재  15.0  85.0   합격
1     맹승주  14.5  86.5   합격
2     안미경  14.0  86.0   합격
3     서진수  13.5  85.5   합격
4     황경인  13.0  85.0   합격
5     신운무  12.0  83.0   합격
6      권율  12.0  85.0   합격
7      강준  11.0  82.0   합격
8    신사임당  11.0  83.0   합격
9     문무왕  10.5  82.0   합격
10    김지희  10.5  81.5   합격
11    임기승  10.0  82.0   합격
12    강감찬  10.0  81.0   합격
13  광개토대왕   9.5  78.0  불합격
14    이세혁   9.3  77.4  불합격
15    전우치   9.0  77.0  불합격
16    이순신   9.0  76.0  불합격
17    정진교   8.5  75.5  불합격
18   계백장군   8.5  76.0  불합격
19    왕광환   8.4  75.5  불합격
20    홍길동   8.2  75.0  불합격
21    곽재우   8.0  74.5  불합격
22    김유신   7.5  74.0  불합격
23    이승우   7.5  73.5  불합격
24    일지매   7.0  73.0  불합격</pre>
# 공통 실습 코드

```python
#Step 2: 훈련용 데이터셋과 테스트용 데이터셋 나누어서 분석
from sklearn.model_selection import train_test_split

# data  나누기
data = study['공부시간'].to_numpy()
target = study['합격여부']

# train, test 데이터 분리
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target, test_size=0.2, random_state=40)
```
```python
#Step 3. 학습 후 모델을 생성하고 예측을 수행합니다
from sklearn.linear_model import LogisticRegression
# 로지스틱회귀 모델 생성
Ir = LogisticRegression()
# 행(row)으로 되어있는 데이터, 열(column)로 나열
훈련용_data = 훈련용_data.reshape(-1,1)   
테스트용_data = 테스트용_data.reshape(-1,1)

# 모델 학습
훈련용_data = 훈련용_data.reshape(-1, 1)
테스트용_data = 테스트용_data.reshape(-1, 1)

# 모델 학습
Ir.fit(훈련용_data, 훈련용_target)

# 테스트용_data로 예측
print(테스트용_data)
print(Ir.predict(테스트용_data))

```
<pre class="console-output">[[9. ]
 [7. ]
 [9.3]
 [8.4]
 [9.5]]
['불합격' '불합격' '불합격' '불합격' '합격']
</pre>
```python
import numpy as np

# 각 항목별 확률값 출력
print(np.round(Ir.predict_proba(테스트용_data),3))
print(Ir.predict_proba(테스트용_data))
```
<pre class="console-output">[[0.668 0.332]
 [0.984 0.016]
 [0.546 0.454]
 [0.849 0.151]
 [0.461 0.539]]
[[0.66809273 0.33190727]
 [0.98418294 0.01581706]
 [0.54609343 0.45390657]
 [0.8492738  0.1507262 ]
 [0.4605282  0.5394718 ]]
</pre>
# Google Colab 데이터 로드

```python
# 다중 분류 활용-과일 종류 분류하기
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
fruit_2 = pd.read_csv(io.BytesIO(myfile['과일채소목록_2.csv']),
                       encoding='cp949')
fruit_2
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
fruit_2 = pd.read_csv('./머신러닝실습용자료/과일채소목록_2.csv',encoding='cp949')
fruit_2
```
<pre class="console-output">      종류  무게_g  길이_cm   당도 등급
0   거봉포도   291   29.1  9.1  A
1   거봉포도   290   29.0  9.0  A
2   거봉포도   281   28.1  8.1  B
3   거봉포도   280   28.0  8.0  B
4   거봉포도   271   26.1  8.6  B
5   거봉포도   270   26.0  8.5  B
6   거봉포도   251   25.1  7.6  C
7   거봉포도   250   25.0  7.5  C
8   거봉포도   221   22.1  7.1  C
9   거봉포도   220   22.0  7.0  C
10    수박  2501   25.1  7.1  C
11    수박  2500   25.0  7.0  C
12    수박  2201   21.1  9.6  A
13    수박  2200   21.0  9.5  A
14    수박  2001   30.5  8.1  A
15    수박  2000   30.0  8.0  B
16    수박  1801   20.1  6.6  D
17    수박  1800   20.0  6.5  D
18    수박  1501   16.1  8.6  B
19    수박  1500   16.0  8.5  B
20   옥수수   501   25.1  2.1  B
21   옥수수   500   25.0  2.0  B
22   옥수수   451   20.1  3.1  A
23   옥수수   450   20.0  3.0  A
24   옥수수   401   23.1  1.1  D
25   옥수수   400   23.0  1.0  D
26   옥수수   381   22.1  1.6  C
27   옥수수   380   22.0  1.5  C
28   옥수수   351   20.1  1.4  C
29   옥수수   350   20.0  1.3  C
30    자두   151    3.9  8.6  B
31    자두   150    3.8  8.5  B
32    자두   121    3.8  7.1  C
33    자두   120    3.7  7.0  C
34    자두   111    3.7  7.6  C
35    자두   110    3.6  7.5  C
36    자두   101    3.6  6.1  D
37    자두   100    3.5  6.0  D
38    자두    91    2.9  8.1  B
39    자두    90    2.8  8.0  B
40    참외   601    8.6  8.1  B
41    참외   600    8.5  8.0  B
42    참외   501    8.1  8.1  B
43    참외   500    8.0  8.0  B
44    참외   451    8.1  7.6  C
45    참외   450    8.0  7.5  C
46    참외   401    7.6  7.3  C
47    참외   401    6.6  6.6  D
48    참외   400    7.5  7.2  C
49    참외   400    6.5  6.5  D</pre>
# 공통 실습 코드

```python
#Step 2: 훈련용 데이터셋과 테스트용 데이터셋 나누어서 분석
from sklearn.model_selection import train_test_split

# data  나누기 무게, 길이, 당도를 가지고 과일의 종류를 분류
data = fruit_2[['무게_g' ,'길이_cm' ,'당도']]
target = fruit_2['종류']

# train, test 데이터 분리
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target, test_size=0.2, random_state=40)
```
```python
#Step 3. 데이터 표준화를 진행합니다
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(훈련용_data)

#data에 대해서 표준화 적용
표준화_훈련용_data = ss.transform(훈련용_data)
표준화_테스트용_data = ss.transform(테스트용_data)
```
```python
# 모델을 생성하고 테스트하고 성능을 확인합니다.
from sklearn.linear_model import LogisticRegression
import numpy as np

# 로지스틱회귀분석 모델 생성 및 학습
softmax_reg = LogisticRegression()
softmax_reg.fit(훈련용_data, 훈련용_target)

# 분류 결과 확인
print(softmax_reg.predict(표준화_테스트용_data))
# 분류 확률 확인
print(np.round(softmax_reg.predict_proba(표준화_테스트용_data),3))

# 분류 점수 확인
print(softmax_reg.score(표준화_테스트용_data, 테스트용_target))
```
<pre class="console-output">['자두' '수박' '참외' '자두' '자두' '자두' '자두' '자두' '거봉포도' '거봉포도']
[[0.078 0.211 0.113 0.309 0.289]
 [0.12  0.457 0.312 0.022 0.088]
 [0.096 0.232 0.14  0.263 0.27 ]
 [0.072 0.137 0.084 0.427 0.281]
 [0.109 0.15  0.119 0.366 0.256]
 [0.378 0.022 0.11  0.406 0.084]
 [0.178 0.066 0.111 0.464 0.181]
 [0.34  0.034 0.126 0.393 0.106]
 [0.318 0.084 0.203 0.258 0.138]
 [0.388 0.038 0.148 0.328 0.099]]
0.4
</pre>
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\linear_model\_logistic.py:406: ConvergenceWarning: lbfgs failed to converge after 100 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max_iter=100).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\utils\validation.py:2691: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
</pre>

</div>
<div id="content-ai-cat-6" class="content-section" markdown="1">
# 7. KNN_수박_참외_맞추기

# Google Colal 데이터 로드

```python
#Step 1. 구글 코랩에 한글 폰트 설정하기

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```
<pre class="console-output">Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
'rm' is not recognized as an internal or external command,
operable program or batch file.
</pre>
```python
#Step 1.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
src_data = pd.read_csv(io.BytesIO(myfile['수박과참외.csv']),
                       encoding='cp949')
src_data
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
src_data = pd.read_csv('./머신러닝실습용자료/수박과참외.csv',encoding='cp949')
src_data
```
<pre class="console-output">    종류    무게    길이
0   수박  2000  30.0
1   수박  2500  25.0
2   수박  1800  20.0
3   수박  1500  16.0
4   수박   900  10.0
5   수박  2500  33.0
6   수박  2250  23.0
7   수박  1860  17.0
8   수박  2100  21.0
9   수박  1500  17.0
10  참외   500   8.0
11  참외   400   7.5
12  참외   450   5.0
13  참외   400   4.5
14  참외   600   8.5</pre>
# 공통 실습 코드

```python
#수박과 참외의 무게와 길이
수박정보 = src_data.loc[ (src_data['종류'] =='수박'), ['무게','길이']]
참외정보 = src_data.loc[ (src_data['종류'] =='참외'), ['무게','길이']]

import matplotlib.pyplot as plt
plt.scatter(수박정보.무게,수박정보.길이)
plt.scatter(참외정보.길이,참외정보.길이)
plt.xlabel('weigth')
plt.ylabel('length')
plt.show()
```

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_6_6_0.png" alt="Result Graph"></div>

```python
import numpy as np

# np.column_stack을 통해 무게와 길이를 data 변수에 넣는다. 
data = np.column_stack((src_data.무게,src_data.길이))

# 데이터의 종류를 target에 넣는다.
target = src_data.종류

print(data)
print(target)
```
<pre class="console-output">[[2000.    30. ]
 [2500.    25. ]
 [1800.    20. ]
 [1500.    16. ]
 [ 900.    10. ]
 [2500.    33. ]
 [2250.    23. ]
 [1860.    17. ]
 [2100.    21. ]
 [1500.    17. ]
 [ 500.     8. ]
 [ 400.     7.5]
 [ 450.     5. ]
 [ 400.     4.5]
 [ 600.     8.5]]
0     수박
1     수박
2     수박
3     수박
4     수박
5     수박
6     수박
7     수박
8     수박
9     수박
10    참외
11    참외
12    참외
13    참외
14    참외
Name: 종류, dtype: str
</pre>
```python
# Step 4. 주어진 데이터를 훈련용과 테스트(검증용)으로 나눕니다.
#test_size = 0.25, random_state = 40

from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(
    data, target, test_size=0.25, random_state=40)



```
```python
# 데이터 구조(shape) 확인
print(훈련용_data.shape)
print(테스트용_data.shape)
```
<pre class="console-output">(11, 2)
(4, 2)
</pre>
```python
# Step 5. 분석하여 모델을 생성합니다.
from sklearn.neighbors import KNeighborsClassifier

#Classifler -> SVC
# knn 모델 생성
knn = KNeighborsClassifier(n_neighbors=3)
#k-nn: k 값을 필수로 지정해야한다.

# 모델 학습
knn.fit(훈련용_data, 훈련용_target)

# 모델 평가
knn.score(테스트용_data, 테스트용_target)
```
<pre class="console-output">1.0</pre>
```python
# Step 6. 모델이 정확한지 임의의 데이터로 테스트합니다.
print( knn.predict([[1000, 15]]))
```
<pre class="console-output">['수박']
</pre>
```python
# Step 7. 위 데이터의 값을 그래프로 출력하여 확인합니다.
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic') 

plt.scatter(훈련용_data[:,0], 훈련용_data[:,1])
plt.scatter(1000, 15, marker='o')
plt.xlabel('무게')
plt.ylabel('길이')
plt.show()
```
<pre class="console-output">findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 47924 (\N{HANGUL SYLLABLE MU}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 44172 (\N{HANGUL SYLLABLE GE}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 44600 (\N{HANGUL SYLLABLE GIL}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 51060 (\N{HANGUL SYLLABLE I}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
</pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_6_12_1.png" alt="Result Graph"></div>

```python
# Step 8. 최적의 k 값 찾기
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic') 

k_list = range(1,12)
accuracies = []

for k in k_list:
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(훈련용_data, 훈련용_target.values.ravel())
  accuracies.append(classifier.score(테스트용_data, 테스트용_target))

plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("최적의 이웃 값 찾기")
plt.show()
```
<pre class="console-output">findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 52572 (\N{HANGUL SYLLABLE COE}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 51201 (\N{HANGUL SYLLABLE JEOG}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 51032 (\N{HANGUL SYLLABLE YI}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 51060 (\N{HANGUL SYLLABLE I}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 50883 (\N{HANGUL SYLLABLE US}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 44050 (\N{HANGUL SYLLABLE GABS}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 52286 (\N{HANGUL SYLLABLE CAJ}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
C:\Users\user\AppData\Roaming\Python\Python313\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 44592 (\N{HANGUL SYLLABLE GI}) missing from font(s) DejaVu Sans.
  fig.canvas.print_figure(bytes_io, **kw)
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
findfont: Font family 'NanumBarunGothic' not found.
</pre>

<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_6_13_1.png" alt="Result Graph"></div>

```python
# 최적의 K 값 가지고 실행

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(훈련용_data, 훈련용_target)
knn.score(테스트용_data, 테스트용_target)   
print(knn.predict([[1000, 15]]))
```
<pre class="console-output">['수박']
</pre>
```python
#학습된 모델 저장하기와 불러서 재사용하기
import joblib

# #모델 훈련을 합니다.
# model = knn.fit(훈련용_data, 훈련용_target)

#모델을 피클 파클 파일로 저장합니다.
joblib.dump(knn, "KNN_model.pkl")
```
<pre class="console-output">['KNN_model.pkl']</pre>
```python
import joblib

# 모델을 불러서 다시 사용하기
kn2 = joblib.load('knn_model.pkl')
print(kn2.predict([[800,8]]))
```
<pre class="console-output">['참외']
</pre>

</div>
<div id="content-ai-cat-7" class="content-section" markdown="1">
# 8. K_Fold_교차검증

# Google Colab 데이터 로드

```python
#Step 1. 구글 코랩에 한글 폰트 설정하기

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```
<pre class="console-output">Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
Sudo가 이 컴퓨터에서 사용하지 않도록 설정되어 있습니다. 사용하도록 설정하려면 으로 이동하세요. ]8;;ms-settings:developers\Developer Settings page]8;;\ 설정 앱의
'rm' is not recognized as an internal or external command,
operable program or batch file.
</pre>
```python
#Step 2.분석할 데이터가 저장된 파일을 불러와서 변수에 할당합니다.
from google.colab import files
myfile = files.upload()
import io
import pandas as pd
#pd.read_csv로 csv파일 불러오기
src_data = pd.read_csv(io.BytesIO(myfile['의사결정나무_과일종류_2가지.csv']),
                       encoding='cp949')
src_data
```
# 로컬 데이터 로드

```python
#컴퓨터에서 작업하려면 아래 코드의 주석을 제거하고 실행하면 됩니다
import pandas as pd
src_data = pd.read_csv('./머신러닝실습용자료/의사결정나무_과일종류_2가지.csv',encoding='cp949')
src_data
```
<pre class="console-output">    종류    무게    길이
0   수박  2000  30.0
1   수박  2500  25.0
2   수박  1800  20.0
3   수박  1500  16.0
4   수박  1900  19.0
5   수박   600   9.0
6   참외   500   8.0
7   참외   400   7.5
8   참외   450   5.0
9   참외   400   4.5
10  참외   600   9.5
11  참외   550   8.5</pre>
# 공통 실습 코드

```python
#Step 3.주어진 데이터를 훈련용 데이터와 검증용 데이터로 나눕니다
import numpy as np

# 무게, 길이로 종류를 예측
#Dframe으로 읽어서 . to_numpy()로 변환
data = src_data[['무게', '길이']].to_numpy()
target = src_data['종류'].to_numpy()
print(data)
print(target)

# train, test 데이터 분리
from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(
    data, target, test_size=0.2, random_state=10
)
```
<pre class="console-output">[[2000.    30. ]
 [2500.    25. ]
 [1800.    20. ]
 [1500.    16. ]
 [1900.    19. ]
 [ 600.     9. ]
 [ 500.     8. ]
 [ 400.     7.5]
 [ 450.     5. ]
 [ 400.     4.5]
 [ 600.     9.5]
 [ 550.     8.5]]
['수박' '수박' '수박' '수박' '수박' '수박' '참외' '참외' '참외' '참외' '참외' '참외']
</pre>
```python
# 교차검증 없이 모델 검증합니다.
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
# 의사결정트리 분류기 모델 생성
dt = DecisionTreeClassifier(random_state=10)
# 모델 학습
dt.fit(훈련용_data, 훈련용_target)
# 훈련용 데이터 기준 score 출력
print('훈련용 데이터 기준 정확도 :', dt.score(훈련용_data, 훈련용_target))
# 테스트용 데이터 기준 score 출력
print('테스트용 데이터 기준 정확도 :', dt.score(테스트용_data, 테스트용_target))
```
<pre class="console-output">훈련용 데이터 기준 정확도 : 1.0
테스트용 데이터 기준 정확도 : 1.0
</pre>
```python
#3-Fold 교차 검증 수행
from sklearn.model_selection import cross_validate , cross_val_score
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=10)

# cross_validate() : 검사 결과를 자세하게 보여주는 것
scores_1 = cross_validate(dt, 훈련용_data, 훈련용_target, cv=3)
# cross_val_score() : 검사 결과 중에서 평균 점수만 보여주는 것
scores_2 = cross_val_score(dt, 훈련용_data, 훈련용_target, cv=3)

print('cross_validate 결과:', scores_1)
print('cross_validate 결과:', np.mean(scores_1['test_score']))
print('cross_val_score 결과:', np.mean(scores_2) )
```
<pre class="console-output">cross_validate 결과: {'fit_time': array([0.00122452, 0.00128245, 0.00084114]), 'score_time': array([0.00051212, 0.00048518, 0.00041366]), 'test_score': array([0.66666667, 1.        , 0.66666667])}
cross_validate 결과: 0.7777777777777777
cross_val_score 결과: 0.7777777777777777
</pre>
```python
#5-Fold 교차검증 수행
from sklearn.model_selection import cross_validate , cross_val_score
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=10)

# cross_validate() : 검사 결과를 자세하게 보여주는 것
scores_1 = cross_validate(dt, 훈련용_data, 훈련용_target, cv=5)
# cross_val_score() : 검사 결과 중에서 평균 점수만 보여주는 것
scores_2 = cross_val_score(dt, 훈련용_data, 훈련용_target, cv=5)

print('cross_validate 결과:', scores_1)
print('cross_validate 결과:', np.mean(scores_1['test_score']))
print('cross_val_score 결과:', np.mean(scores_2) )

```
<pre class="console-output">cross_validate 결과: {'fit_time': array([0.00119376, 0.00077987, 0.00079179, 0.00098825, 0.00059462]), 'score_time': array([0.00052547, 0.00055528, 0.00048661, 0.0005846 , 0.00034595]), 'test_score': array([0.5, 1. , 0.5, 1. , 1. ])}
cross_validate 결과: 0.8
cross_val_score 결과: 0.8
</pre>
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_split.py:813: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_split.py:813: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
</pre>

</div>
<div id="content-ai-cat-8" class="content-section" markdown="1">
# 9. 그리드서치

## GridSearch
최적의 하이퍼파라미터를 찾는 방법

```python
# 컴퓨터에서 작업하려면 아래 코드를 실행하면 됩니다
import pandas as pd
src_data = pd.read_csv('./머신러닝실습용자료/의사결정나무_과일종류_2가지.csv',encoding='cp949')
src_data
```
<pre class="console-output">    종류    무게    길이
0   수박  2000  30.0
1   수박  2500  25.0
2   수박  1800  20.0
3   수박  1500  16.0
4   수박  1900  19.0
5   수박   600   9.0
6   참외   500   8.0
7   참외   400   7.5
8   참외   450   5.0
9   참외   400   4.5
10  참외   600   9.5
11  참외   550   8.5</pre>
```python
# Step 3. 주어진 데이터를 훈련용 데이터와 검증용 데이터로 나눕니다
import numpy as np

# 무게, 길이로 종류를 예측
data = src_data[['무게', '길이']]
target = src_data['종류']
print(data)
print(target)

# train, test 데이터 분리
from sklearn.model_selection import train_test_split
훈련용_data, 테스트용_data, 훈련용_target, 테스트용_target = train_test_split(data, target)
print(훈련용_data)
print(훈련용_target)
print(테스트용_data)
print(테스트용_target)
```
<pre class="console-output">      무게    길이
0   2000  30.0
1   2500  25.0
2   1800  20.0
3   1500  16.0
4   1900  19.0
5    600   9.0
6    500   8.0
7    400   7.5
8    450   5.0
9    400   4.5
10   600   9.5
11   550   8.5
0     수박
1     수박
2     수박
3     수박
4     수박
5     수박
6     참외
7     참외
8     참외
9     참외
10    참외
11    참외
Name: 종류, dtype: str
      무게    길이
8    450   5.0
9    400   4.5
5    600   9.0
1   2500  25.0
2   1800  20.0
3   1500  16.0
4   1900  19.0
11   550   8.5
0   2000  30.0
8     참외
9     참외
5     수박
1     수박
2     수박
3     수박
4     수박
11    참외
0     수박
Name: 종류, dtype: str
     무게   길이
10  600  9.5
7   400  7.5
6   500  8.0
10    참외
7     참외
6     참외
Name: 종류, dtype: str
</pre>
```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier


parm = {'max_depth':[1,2,3]}
gs = GridSearchCV(DecisionTreeClassifier(random_state=50) , parm , n_jobs=-1)
gs.fit(훈련용_data , 훈련용_target)
```
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_split.py:813: UserWarning: The least populated class in y has only 3 members, which is less than n_splits=5.
  warnings.warn(
</pre>
<pre class="console-output">GridSearchCV(estimator=DecisionTreeClassifier(random_state=50), n_jobs=-1,
             param_grid={'max_depth': [1, 2, 3]})</pre>
```python
print(gs.best_params_)
dt = gs.best_estimator_
print(dt.score(훈련용_data , 훈련용_target))
```
<pre class="console-output">{'max_depth': 1}
1.0
</pre>
```python
#한꺼번에 여러 속성값을 찾을 경우
from sklearn.model_selection import GridSearchCV
parm = {'max_depth': range(1,10,1) ,
        'min_impurity_decrease': np.arange(0.0001,0.001 , 0.0001),
        'min_samples_split' : range(2,100,10) }
gs = GridSearchCV(DecisionTreeClassifier(random_state=50) , parm , n_jobs=-1)
gs.fit(훈련용_data , 훈련용_target)
print(gs.best_params_)
```
<pre class="console-output">c:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\sklearn\model_selection\_split.py:813: UserWarning: The least populated class in y has only 3 members, which is less than n_splits=5.
  warnings.warn(
</pre>
<pre class="console-output">{'max_depth': 1, 'min_impurity_decrease': np.float64(0.0001), 'min_samples_split': 2}
</pre>
```python
#교차검증 점수중 최고값을 확인하기
print(np.max(gs.cv_results_['mean_test_score']))
```
<pre class="console-output">0.8
</pre>
```python
# 최적의 모델로 테스트용 데이터로 최종 테스트하기
dt = gs.best_estimator_
print(dt.score(테스트용_data , 테스트용_target))
print(dt.score(훈련용_data , 훈련용_target))
```
<pre class="console-output">0.6666666666666666
1.0
</pre>

</div>
    <div id="content-ai-cat-9" class="content-section" markdown="1">

# 실습 1 신용카드 이상 탐지

데이터 준비
실습에 사용될 데이터는 Kaggle의 Credit Card Fraud Detection 데이터셋입니다. 이 데이터셋은 거래의 시간, 금액과 함께 28개의 PCA 변환된 특성들을 포함하고 있습니다. 'Class' 레이블은 사기 거래를 나타내는 1과 정상 거래를 나타내는 0으로 구분됩니다.

데이터를 불러오고, 전처리하는 기본적인 코드는 아래와 같습니다:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# 데이터를 불러옵니다.
# 불러오기 안될때: 해당 파일이 어디에 있는지 회귀, 분석 or 트리, 비지도학습 or 머신러닝실습자료 확인하기
data = pd.read_csv('./회귀, 분류/creditcard.csv',encoding='cp949')
data
```
<pre class="console-output">            Time         V1         V2        V3        V4        V5  \
0            0.0  -1.359807  -0.072781  2.536347  1.378155 -0.338321   
1            0.0   1.191857   0.266151  0.166480  0.448154  0.060018   
2            1.0  -1.358354  -1.340163  1.773209  0.379780 -0.503198   
3            1.0  -0.966272  -0.185226  1.792993 -0.863291 -0.010309   
4            2.0  -1.158233   0.877737  1.548718  0.403034 -0.407193   
...          ...        ...        ...       ...       ...       ...   
284802  172786.0 -11.881118  10.071785 -9.834783 -2.066656 -5.364473   
284803  172787.0  -0.732789  -0.055080  2.035030 -0.738589  0.868229   
284804  172788.0   1.919565  -0.301254 -3.249640 -0.557828  2.630515   
284805  172788.0  -0.240440   0.530483  0.702510  0.689799 -0.377961   
284806  172792.0  -0.533413  -0.189733  0.703337 -0.506271 -0.012546   

              V6        V7        V8        V9  ...       V21       V22  \
0       0.462388  0.239599  0.098698  0.363787  ... -0.018307  0.277838   
1      -0.082361 -0.078803  0.085102 -0.255425  ... -0.225775 -0.638672   
2       1.800499  0.791461  0.247676 -1.514654  ...  0.247998  0.771679   
3       1.247203  0.237609  0.377436 -1.387024  ... -0.108300  0.005274   
4       0.095921  0.592941 -0.270533  0.817739  ... -0.009431  0.798278   
...          ...       ...       ...       ...  ...       ...       ...   
284802 -2.606837 -4.918215  7.305334  1.914428  ...  0.213454  0.111864   
284803  1.058415  0.024330  0.294869  0.584800  ...  0.214205  0.924384   
284804  3.031260 -0.296827  0.708417  0.432454  ...  0.232045  0.578229   
284805  0.623708 -0.686180  0.679145  0.392087  ...  0.265245  0.800049   
284806 -0.649617  1.577006 -0.414650  0.486180  ...  0.261057  0.643078   

             V23       V24       V25       V26       V27       V28  Amount  \
0      -0.110474  0.066928  0.128539 -0.189115  0.133558 -0.021053  149.62   
1       0.101288 -0.339846  0.167170  0.125895 -0.008983  0.014724    2.69   
2       0.909412 -0.689281 -0.327642 -0.139097 -0.055353 -0.059752  378.66   
3      -0.190321 -1.175575  0.647376 -0.221929  0.062723  0.061458  123.50   
4      -0.137458  0.141267 -0.206010  0.502292  0.219422  0.215153   69.99   
...          ...       ...       ...       ...       ...       ...     ...   
284802  1.014480 -0.509348  1.436807  0.250034  0.943651  0.823731    0.77   
284803  0.012463 -1.016226 -0.606624 -0.395255  0.068472 -0.053527   24.79   
284804 -0.037501  0.640134  0.265745 -0.087371  0.004455 -0.026561   67.88   
284805 -0.163298  0.123205 -0.569159  0.546668  0.108821  0.104533   10.00   
284806  0.376777  0.008797 -0.473649 -0.818267 -0.002415  0.013649  217.00   

        Class  
0           0  
1           0  
2           0  
3           0  
4           0  
...       ...  
284802      0  
284803      0  
284804      0  
284805      0  
284806      0  

[284807 rows x 31 columns]</pre>

```python
# target 데이터(class)의 분포를 확인합니다.
print("Class Distribution:")
print(data['Class'].value_counts())

# 'time' 대신 대문자 'Time'으로 변경하여 컬럼을 삭제합니다.
X = data.drop(['Time', 'Class'], axis=1)
y = data['Class']

# 분리가 잘 되었는지 상위 5행 데이터 확인
X.head()
```
<pre class="console-output">Class Distribution:
Class
0    284315
1       492
Name: count, dtype: int64
</pre>
<pre class="console-output">         V1        V2        V3        V4        V5        V6        V7  \
0 -1.359807 -0.072781  2.536347  1.378155 -0.338321  0.462388  0.239599   
1  1.191857  0.266151  0.166480  0.448154  0.060018 -0.082361 -0.078803   
2 -1.358354 -1.340163  1.773209  0.379780 -0.503198  1.800499  0.791461   
3 -0.966272 -0.185226  1.792993 -0.863291 -0.010309  1.247203  0.237609   
4 -1.158233  0.877737  1.548718  0.403034 -0.407193  0.095921  0.592941   

         V8        V9       V10  ...       V20       V21       V22       V23  \
0  0.098698  0.363787  0.090794  ...  0.251412 -0.018307  0.277838 -0.110474   
1  0.085102 -0.255425 -0.166974  ... -0.069083 -0.225775 -0.638672  0.101288   
2  0.247676 -1.514654  0.207643  ...  0.524980  0.247998  0.771679  0.909412   
3  0.377436 -1.387024 -0.054952  ... -0.208038 -0.108300  0.005274 -0.190321   
4 -0.270533  0.817739  0.753074  ...  0.408542 -0.009431  0.798278 -0.137458   

        V24       V25       V26       V27       V28  Amount  
0  0.066928  0.128539 -0.189115  0.133558 -0.021053  149.62  
1 -0.339846  0.167170  0.125895 -0.008983  0.014724    2.69  
2 -0.689281 -0.327642 -0.139097 -0.055353 -0.059752  378.66  
3 -1.175575  0.647376 -0.221929  0.062723  0.061458  123.50  
4  0.141267 -0.206010  0.502292  0.219422  0.215153   69.99  

[5 rows x 29 columns]</pre>

```python
# 데이터를 훈련 세트와 테스트 세트로 분할합니다.
# 데이터 분할 예시 (이어서 실행해 보세요!)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(y_train.value_counts())
print(X_train.value_counts())

# 데이터 표준화 작업을 실시합니다,
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
<pre class="console-output">Class
0    199020
1       344
Name: count, dtype: int64
V1         V2         V3         V4         V5         V6         V7         V8         V9         V10        V11        V12        V13        V14        V15        V16        V17        V18        V19        V20        V21        V22        V23        V24        V25        V26        V27        V28        Amount
 2.055797  -0.326668  -2.752041  -0.842316   2.463072   3.173856  -0.432126   0.727706   0.608606  -0.075186   0.063504   0.350564  -0.141238   0.690972   1.275257  -0.371962  -0.601957  -0.052640  -0.330590  -0.180370   0.269765   0.844627   0.020675   0.726212   0.366624  -0.398828   0.027735  -0.060282  1.00      55
 1.302378  -0.606529  -0.681986  -1.904603   1.326623   3.436312  -1.145127   0.959147   1.671302  -1.022946  -0.191423   0.631027   0.031907  -0.031425   1.446627  -0.121820  -0.651405   0.617970   0.927600   0.005757  -0.064208  -0.080587  -0.072991   1.018136   0.663575  -0.671323   0.096801   0.028697  1.00      48
 1.245674   0.166975   0.488306   0.635322  -0.562777  -1.011073   0.014953  -0.160211   0.170362  -0.044575  -0.356749  -0.073460  -0.517760   0.406969   1.124147   0.342470  -0.374656  -0.438992  -0.116091  -0.132080  -0.262581  -0.816264   0.140304   0.357827   0.186423   0.096544  -0.035866   0.018495  8.99      46
 2.053311   0.089735  -1.681836   0.454212   0.298310  -0.953526   0.152003  -0.207071   0.587335  -0.362047  -0.589598  -0.174712  -0.621127  -0.703513   0.271957   0.318688   0.549365  -0.257786   0.016256  -0.187421  -0.361158  -0.984262   0.354198   0.620709  -0.297138   0.166736  -0.068299  -0.029585  8.99      45
 2.040211  -0.146975  -2.955934  -0.578356   2.609358   3.142642  -0.416883   0.784393   0.359902  -0.351075   0.329651   0.183508  -0.272919  -0.597437   0.583897   0.178676   0.473898  -0.498850  -0.140099  -0.120714  -0.352334  -0.996937   0.363485   0.604827  -0.264560   0.219671  -0.039209  -0.042787  1.98      42
                                                                                                                                                                                                                                                                                                                              ..
-0.415022   0.713439   1.221551  -2.108216   0.187067  -1.281616   1.118548  -0.345326   0.463473  -0.999876   1.648799   1.319156   0.299893   0.161817   0.098311  -0.474020  -0.783303   0.392973   0.106964   0.075377   0.132886   0.756938  -0.290888   0.558730   0.037363  -0.871689   0.239482  -0.020422  1.00       1
 1.993864  -0.516866  -0.620118   0.129845  -0.285128   0.395044  -0.822358   0.231591   0.995898   0.212619   0.319897   0.584204  -0.251486   0.062302   0.013795   0.684356  -0.906442   0.739436   0.043943  -0.174051   0.262526   0.884510   0.099141   0.275689  -0.195404   0.623598  -0.032455  -0.058552  5.99       1
-1.497933   0.657921   1.581568  -0.024286   0.584698   1.303031   0.609212   0.135561   0.452745   0.108640   0.521818   0.373473  -0.533295  -0.401809   0.771781  -1.879937   1.241541  -2.623211  -1.241768  -0.225079  -0.072452   0.299172   0.110048  -0.615980  -0.425883   0.263968  -0.448445   0.045178  36.99      1
 1.069777   0.072105   0.496540   1.505318  -0.380277  -0.370243   0.100551  -0.026687   0.319684  -0.131553  -0.305690   0.445453  -0.547450   0.166727  -0.073930  -0.796913   0.404795  -1.033061  -0.500426  -0.149402  -0.061991  -0.044629  -0.050485   0.400171   0.593314  -0.335160   0.031014   0.024886  45.42      1
-0.598120   0.775041   1.823394   0.312991  -0.096171  -0.391452   0.499351   0.071224  -0.017496  -0.512312  -0.122119   0.907240   0.640615  -0.420510  -0.541179  -0.995150   0.517052  -1.113362  -0.238137   0.102259   0.060615   0.568083  -0.084001   0.685003  -0.245859   0.356638   0.378580   0.206366  6.99       1
Name: count, Length: 194144, dtype: int64
</pre>

```python
# 데이터를 훈련 세트와 테스트 세트로 분할합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(y_train.value_counts())
print(y_test.value_counts())


# 데이터 표준화 작업을 실시합니다,
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

```
<pre class="console-output">Class
0    227451
1       394
Name: count, dtype: int64
Class
0    56864
1       98
Name: count, dtype: int64
</pre>

```python
# 데이터 줄이기
# (데이터 줄이거나 늘리기 가능)
# 시험:  Feature_importance를 가지고 줄이고 최대
# Feature_importance



#상관관계를 구해서, 상관관계가 높은 항목들을 병합
```

```python
# 1. 모델 학습 (반드시 fit을 먼저 해야 중요도가 계산됩니다)(냬꺼)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 2. 중요도 추출 및 데이터프레임 만들기
import pandas as pd
import numpy as np

importance_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model.feature_importances_
})

# 3. 중요도 높은 순으로 정렬
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print(importance_df.head(10)) # 상위 10개 출력
```

```python
# 로지스틱 회귀 모델을 생성하고 학습합니다.(다른 사람)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, accuracy_score
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)

# 학습된 모델로 테스트 데이터를 예측하고 평가합니다.
예측값 = lr.predict(X_test)

# 정확도, 정밀도, F1 Score를 계산 및 출력합니다.
print("Accuracy:", accuracy_score(y_test, 예측값))
print("Precision:", precision_score(y_test, 예측값, zero_division=0))
print("F1 Score:", f1_score(y_test, 예측값, zero_division=0))

# AUC 점수를 계산합니다.
lr_auc_score = roc_auc_score(y_test, lr.predict_proba(X_test)[:, 1])
print("Logistic Regression AUC score:", lr_auc_score)
```
<pre class="console-output">Accuracy: 0.9991046662687406
Precision: 0.8615384615384616
F1 Score: 0.6871165644171779
Logistic Regression AUC score: 0.9768823645102385
</pre>

## Decision Tree 로 직접해보기

```python
# 결정 트리 모델을 생성하고 학습합니다.

# 학습된 모델로 테스트 데이터를 예측하고 평가합니다.

# AUC 점수를 계산합니다.
```

```python
# 결정 트리 모델을 생성하고 학습합니다.
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, precision_score, accuracy_score, roc_auc_score
dt = DecisionTreeClassifier()


# 학습된 모델로 테스트 데이터를 예측하고 평가합니다.
dt.fit(X_train, y_train)
예측값 = dt.predict(X_test)

# 정확도, 정밀도, F1 Score를 계산 및 출력합니다.
print("Accuracy:", accuracy_score(y_test, 예측값))
print("Precision:", precision_score(y_test, 예측값, zero_division=0))
print("F1 Score:", f1_score(y_test, 예측값, zero_division=0))

# AUC 점수를 계산합니다.
dt_auc_score = roc_auc_score(y_test, dt.predict_proba(X_test)[:, 1])
print("Decision Tree AUC score:", dt_auc_score)
```
<pre class="console-output">Accuracy: 0.9990871107053826
Precision: 0.7090909090909091
F1 Score: 0.75
Decision Tree AUC score: 0.8976778105727378
</pre>

## Random Forest 로 해보기

```python
# 랜덤 포레스트 모델을 생성하고 학습합니다.


# 학습된 모델로 테스트 데이터를 예측하고 평가합니다.

# AUC 점수를 계산합니다.
```

```python
# 랜덤 포레스트 실습: 기본 모델 성능 확인 -> 중요 변수 추출 -> 상위 변수만으로 재학습
from sklearn.ensemble import RandomForestClassifier

# n_estimators: 트리 개수, n_jobs=-1: CPU 코어 전체 사용(학습 속도 개선)
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

# 1) 전체 변수로 학습/예측
rf.fit(X_train, y_train)
예측값 = rf.predict(X_test)

# 2) 분류 평가지표 출력 (불균형 데이터이므로 Accuracy만 보지 말고 Precision/F1도 함께 확인)
print("Accuracy:", accuracy_score(y_test, 예측값))
print("Precision:", precision_score(y_test, 예측값, zero_division=0))
print("F1 Score:", f1_score(y_test, 예측값, zero_division=0))

# 3) AUC 계산: predict_proba의 양성(1) 확률을 사용
rf_auc_score = roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1])
print("Random Forest AUC Score:", rf_auc_score)

# 4) Feature Importance 확인 (모델이 어떤 변수를 중요하게 보는지 해석)
import matplotlib.pyplot as plt
import numpy as np
imp = rf.feature_importances_
print("Feature Importances:", imp)

# 중요도 막대그래프
plt.figure(figsize=(10, 6))
plt.bar(range(len(imp)), imp)
plt.xlabel('column')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.show()

# 가장 중요한 변수 1개 확인
most_important_feature = np.argmax(imp)
print("Most Important Feature Index:", most_important_feature)
print("Most Important Feature Name:", X.columns[most_important_feature])

# 중요도 기준 상위 10개 변수 인덱스 추출 (내림차순)
top_10_features = np.argsort(imp)[-10:][::-1]
print("Top 10 Feature Indices:", top_10_features)
print("Top 10 Feature Names:", X.columns[top_10_features])

# 5) 상위 10개 변수만으로 다시 학습/평가하여 성능 비교
x_top_10 = X.iloc[:, top_10_features]
x_train_top_10, x_test_top_10, y_train, y_test = train_test_split(x_top_10, y, test_size=0.2, random_state=42)
x_train_top_10 = scaler.fit_transform(x_train_top_10)
x_test_top_10 = scaler.transform(x_test_top_10)

rf_top_10 = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_top_10.fit(x_train_top_10, y_train)
예측값_top_10 = rf_top_10.predict(x_test_top_10)

print("Accuracy:", accuracy_score(y_test, 예측값_top_10))
print("Precision:", precision_score(y_test, 예측값_top_10, zero_division=0))
print("F1 Score:", f1_score(y_test, 예측값_top_10, zero_division=0))

rf_top_10_auc_score = roc_auc_score(y_test, rf_top_10.predict_proba(x_test_top_10)[:, 1])
print("Random Forest (Top 10 Features) AUC Score:", rf_top_10_auc_score)
```
<pre class="console-output">Accuracy: 0.9995611109160493
Precision: 0.974025974025974
F1 Score: 0.8571428571428571
Random Forest AUC Score: 0.9526103456295292
Feature Importances: [0.01627813 0.01253408 0.01458116 0.03450583 0.01359336 0.01695684
 0.03051118 0.01284636 0.03792694 0.08218315 0.08582745 0.11929237
 0.00937955 0.11481604 0.01225088 0.08075189 0.14736601 0.02523745
 0.01262306 0.01405877 0.01387184 0.01056663 0.00875691 0.0111819
 0.00920813 0.01772546 0.01292567 0.01026412 0.01197886]
</pre>
<div class="output-img-container"><img src="{{ site.baseurl }}/assets/img/ai/out_9_15_1.png" alt="Result Graph"></div>
<pre class="console-output">Most Important Feature Index: 16
Most Important Feature Name: V17
Top 10 Feature Indices: [16 11 13 10  9 15  8  3  6 17]
Top 10 Feature Names: Index(['V17', 'V12', 'V14', 'V11', 'V10', 'V16', 'V9', 'V4', 'V7', 'V18'], dtype='str')
Accuracy: 0.9995962220427653
Precision: 0.987012987012987
F1 Score: 0.8685714285714285
Random Forest (Top 10 Features) AUC Score: 0.947902550159062
</pre>

## 퀴즈) SVM 사용해보기

```python
# SVM 실습(대용량용): LinearSVC 사용
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_score, f1_score, roc_auc_score
import time

# 실행 시간 측정 (시험에서 속도 비교 질문 대비)
start = time.time()

# 핵심 포인트: 대용량 데이터에서는 기본 SVC(RBF)보다 LinearSVC가 훨씬 빠름
svm = LinearSVC(class_weight='balanced', random_state=42, max_iter=5000)

# 학습/예측
svm.fit(X_train, y_train)
예측값 = svm.predict(X_test)

# 분류 지표 출력
print("Accuracy:", accuracy_score(y_test, 예측값))
print("Precision:", precision_score(y_test, 예측값, zero_division=0))
print("F1 Score:", f1_score(y_test, 예측값, zero_division=0))

# LinearSVC는 predict_proba가 없으므로 decision_function 점수로 AUC 계산
svm_auc_score = roc_auc_score(y_test, svm.decision_function(X_test))
print("Linear SVM AUC score:", svm_auc_score)

# 전체 소요 시간 확인
print(f"학습+예측 시간: {time.time() - start:.2f}초")
```
<pre class="console-output">Accuracy: 0.9813559917137741
Precision: 0.07793345008756568
F1 Score: 0.1435483870967742
Linear SVM AUC score: 0.981975253522906
학습+예측 시간: 2.29초
</pre>

# 가장 AUC점수가 높았던 모델 GridSearch로 튜닝하기

```python
# 가장 AUC가 높았던 Linear SVM 모델을 GridSearch로 튜닝
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, f1_score
import time

start = time.time()

# 불균형 데이터이므로 클래스 비율을 유지하는 StratifiedKFold 사용
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# 시험 포인트: C(규제 강도), class_weight(불균형 대응), max_iter(수렴 반복수)
param_grid = {
    'C': [0.01, 0.1, 1, 10],
    'class_weight': [None, 'balanced'],
    'max_iter': [3000, 5000]
}

# scoring='roc_auc'로 AUC 기준 최적 파라미터 탐색
grid = GridSearchCV(
    estimator=LinearSVC(random_state=42),
    param_grid=param_grid,
    scoring='roc_auc',
    cv=cv,
    n_jobs=-1,
    verbose=1
)

# 하이퍼파라미터 탐색 실행
grid.fit(X_train, y_train)

# 최적 모델로 테스트셋 최종 평가
best_model = grid.best_estimator_
예측값 = best_model.predict(X_test)
auc = roc_auc_score(y_test, best_model.decision_function(X_test))

print('Best Params:', grid.best_params_)
print('Best CV AUC:', grid.best_score_)
print('Test Accuracy:', accuracy_score(y_test, 예측값))
print('Test Precision:', precision_score(y_test, 예측값, zero_division=0))
print('Test F1 Score:', f1_score(y_test, 예측값, zero_division=0))
print('Test AUC:', auc)
print(f"GridSearch 소요시간: {time.time() - start:.2f}초")
```
<pre class="console-output">Fitting 3 folds for each of 16 candidates, totalling 48 fits
Best Params: {'C': 0.01, 'class_weight': 'balanced', 'max_iter': 3000}
Best CV AUC: 0.9756560185742466
Test Accuracy: 0.9813735472771321
Test Precision: 0.07800175284837861
Test F1 Score: 0.14366424535916061
Test AUC: 0.9820158085744146
GridSearch 소요시간: 9.01초
</pre>



</div>

<div id="content-search-results" class="content-section">
      <h1 style="color: #10B981; border-bottom: 2px solid rgba(16, 185, 129, 0.4); padding-bottom: 15px; margin-bottom: 30px;">🔍 검색 결과</h1>
      <div id="search-results-list"></div>
    </div>
  </main>
</div>

<script>
let previousCategory = 'home';

function openCategory(catId) {
  if(catId !== 'search-results') {
    previousCategory = catId;
  }
  
  // Hide all contents
  document.querySelectorAll('.content-section').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-category').forEach(el => el.classList.remove('active'));
  
  // Show target
  const targetContent = document.getElementById('content-' + catId);
  if (targetContent) targetContent.classList.add('active');
  
  const targetNav = document.getElementById('nav-' + catId);
  if (targetNav) targetNav.classList.add('active');
  
  // Scroll to top when changing category
  if(catId !== 'search-results') {
    window.scrollTo(0, 0);
  }
}

// Search Logic
document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("gitbook-search");
  const searchList = document.getElementById("search-results-list");
  
  // Index all content sections (excluding home and search-results)
  const sections = [];
  document.querySelectorAll('.content-section').forEach(sec => {
    if(sec.id === 'content-home' || sec.id === 'content-search-results') return;
    
    const catId = sec.id.replace('content-', '');
    const titleEl = document.querySelector(`#nav-${catId} .nav-category-title`);
    const title = titleEl ? titleEl.innerText : "";
    
    sections.push({
      id: catId,
      title: title,
      navEl: document.getElementById('nav-' + catId),
      rawText: sec.innerText,
      fullText: sec.innerText.toLowerCase()
    });
  });
  
  function getSnippet(text, query) {
    const lowerText = text.toLowerCase();
    const idx = lowerText.indexOf(query);
    if(idx === -1) return text.substring(0, 200) + "...";
    
    const start = Math.max(0, idx - 50);
    const end = Math.min(text.length, idx + query.length + 150);
    
    let snippet = text.substring(start, end);
    if(start > 0) snippet = "..." + snippet;
    if(end < text.length) snippet = snippet + "...";
    
    // safe escape and highlight
    snippet = snippet.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const safeQuery = query.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const regex = new RegExp(`(${safeQuery})`, "gi");
    snippet = snippet.replace(regex, "<mark>$1</mark>");
    return snippet;
  }
  
  searchInput.addEventListener("input", function() {
    const query = this.value.toLowerCase().trim();
    
    if (query === "") {
      // Restore all sidebar nav links
      sections.forEach(sec => {
        if (sec.navEl) sec.navEl.style.display = "block";
      });
      // Show the previously active category
      openCategory(previousCategory);
      return;
    }
    
    // Switch to search results content view
    openCategory('search-results');
    searchList.innerHTML = "";
    
    let hasResults = false;
    
    sections.forEach(sec => {
      const matchInTitle = sec.title.toLowerCase().includes(query);
      const matchInContent = sec.fullText.includes(query);
      
      if (matchInTitle || matchInContent) {
        hasResults = true;
        if (sec.navEl) sec.navEl.style.display = "block";
        
        const details = document.createElement('details');
        details.className = 'code-accordion';
        details.setAttribute('open', ''); // Keep it open for user readability
        
        const summary = document.createElement('summary');
        summary.innerHTML = sec.title;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'accordion-content';
        
        const snippet = document.createElement('div');
        snippet.className = 'search-result-snippet';
        snippet.innerHTML = getSnippet(sec.rawText, query);
        
        const btn = document.createElement('div');
        btn.className = 'go-to-doc-btn';
        btn.innerHTML = '📄 해당 노트로 이동';
        btn.addEventListener('click', () => {
          searchInput.value = "";
          sections.forEach(s => { if (s.navEl) s.navEl.style.display = "block"; });
          openCategory(sec.id);
        });
        
        contentDiv.appendChild(snippet);
        contentDiv.appendChild(btn);
        
        details.appendChild(summary);
        details.appendChild(contentDiv);
        
        searchList.appendChild(details);
      } else {
        if (sec.navEl) sec.navEl.style.display = "none";
      }
    });
    
    if (!hasResults) {
      searchList.innerHTML = `<div style="text-align:center; color:#64748b; margin-top:30px;">'${query}'에 대한 검색 결과가 없습니다.</div>`;
    }
  });
});
</script>

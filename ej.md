---
layout: post
title: "개발 언어 기초 (Languages)"
category: tech-fundamentals
author: eunji
short-description: "C언어, C#, Python, Java 통합 핵심 이론 문법 및 예제 실습 로그"
---

# 💻 개발 언어 기초 (Languages)

<style>
  .tabs-container {
    display: flex;
    gap: 30px;
    align-items: flex-start;
    margin-top: 30px;
  }
  @media (max-width: 768px) {
    .tabs-container {
      flex-direction: column;
    }
    .local-nav-vertical {
      flex-direction: row !important;
      border-right: none !important;
      border-bottom: 2px solid rgba(0, 242, 254, 0.2);
      padding-right: 0 !important;
      padding-bottom: 10px;
      overflow-x: auto;
      width: 100%;
    }
  }
  .local-nav-vertical {
    display: flex;
    flex-direction: column;
    gap: 15px;
    min-width: 160px;
    border-right: 2px solid rgba(0, 242, 254, 0.2);
    padding-right: 20px;
    position: sticky;
    top: 20px;
  }
  .local-nav-item {
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: #849ca8;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.3s ease;
    text-align: left;
    padding: 8px 12px;
    border-radius: 4px;
    white-space: nowrap;
  }
  .local-nav-item:hover, .local-nav-item.active {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.1);
  }
  .tabs-content-area {
    flex: 1;
    min-width: 0;
  }
  .tab-content {
    display: none;
  }
  .tab-content.active {
    display: block;
    animation: fadeIn 0.5s;
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
</style>

<div class="tabs-container">
  <div class="local-nav-vertical">
    <div class="local-nav-item active" onclick="openTab('overview', this)">Overview</div>
    <div class="local-nav-item" onclick="openTab('c_lang', this)">C언어</div>
    <div class="local-nav-item" onclick="openTab('py_lang', this)">파이썬</div>
    <div class="local-nav-item" onclick="openTab('cs_lang', this)">C#</div>
  </div>

  <div class="tabs-content-area">
    <div id="overview" class="tab-content active" markdown="1">
* **C언어:** 하드웨어 가속, 임베디드 저수준 메모리 수동 제어(포인터 및 주소 참조) 학습
* **C# (.NET):** 객체지향 기반의 윈도우 데스크톱 마트 관리 애플리케이션 및 비동기 GUI 구현
* **Python:** 센서 데이터 전처리 시뮬레이터, 이동 평균 필터 알고리즘 모델링 및 검증
* **Java:** JVM 가상 머신 기반 플랫폼 독립 프로그래밍 및 클래스, 인터페이스 설계
    </div>

    <div id="c_lang" class="tab-content" markdown="1">
### 📌 C/C++ 포인터와 메모리 관리
- 스택(Stack) 영역과 힙(Heap) 영역의 물리적 메모리 구분 구조.
- 포인터 변수 참조(`*`, `&`) 및 수동 동적 할당(`malloc`/`free`)의 안정적 제어.

```cpp
// C언어 메모리 수동 할당 및 안전한 해제 구조 예제 코드
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int*)malloc(sizeof(int) * 5); // 힙 영역 메모리 할당
    if (ptr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }
    
    // 할당 영역 사용 예시
    for(int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
    }
    
    // 메모리 누수 방지를 위한 해제 및 댕글링 포인터 차단
    free(ptr);
    ptr = NULL;
    
    return 0;
}
```
    </div>

    <div id="py_lang" class="tab-content" markdown="1">
(파이썬 기초 내용은 추후 채워질 예정입니다.)
    </div>

    <div id="cs_lang" class="tab-content" markdown="1">
# [Tech Stacks] C# 언어
> **C# 프로그래밍의 기초가 되는 핵심 용어, 데이터 처리, 그리고 흐름 제어(조건문)의 핵심 개념 요약**

---

## 1. 기본 문법

### 01. 기본 용어 및 출력
* **식별자 제한:** 변수, 클래스, 메서드 등에 이름을 붙일 때 C#에서 이미 키워드로 선언된 단어(예: `int`, `class`, `var` 등)는 식별자로 단독 사용할 수 없습니다.
* **Console.WriteLine():** 콘솔 창에 데이터를 출력하고 자동으로 줄을 바꿈(New Line) 해주는 C#의 표준 출력 기능입니다. 
* **문자열 보간법:** 문자열 시작 큰따옴표 앞에 `$` 기호를 붙이면, 문장 중간에 중괄호 `{}`를 열고 변수 이름을 그대로 집어넣어 출력할 수 있습니다. 문자열과 변수를 더하기 연산자(`+`)로 지저분하게 연결하지 않아도 되므로 가독성이 매우 높아집니다.

---

### 02. 기본 자료형 및 변수 선언
* **엄격한 데이터 정적 선언:** C#은 변수를 만들 때 담을 데이터의 성격을 명확히 지정해야 하며, 한 번 정해진 타입을 가볍게 무시할 수 없는 안전한 언어입니다.
* **bool 자료형의 독립성:** 참과 거짓을 표현하는 `bool` 타입은 오직 `true`와 `false`라는 문자 상태값만 가집니다. 일반 숫자를 참/거짓 조건으로 대신 사용할 수 없습니다.
* **string 자료형의 기본화:** 문자열을 다루는 `string`이 기본 자료형으로 내장되어 있어, 문자 개수에 상관없이 거대한 문장 데이터도 편리하게 저장하고 제어할 수 있습니다.

---

### 03. 연산자 및 자료형 검사
* **복합 대입 및 증감 연산자:** 변수 자신에게 값을 더하거나 빼서 곧바로 대입하는 연산자(`+=`, `-=`, `*=`, `/=`, `%=`)와, 값을 1씩 증가 또는 감소시키는 연산자(`++`, `--`)를 지원합니다.
* **GetType() 메서드:** C#의 모든 데이터는 내부에 메모리 검사 기능을 가지고 있습니다. 변수 이름 뒤에 `.GetType()`을 붙이면 해당 변수가 현재 정수형(Int32)인지, 문자열(String)인지 등 실제 자료형의 정보를 실시간으로 반환해 줍니다.

---

### 04. var 키워드 (지역 변수 타입 추론)
* **컴파일러의 자동 타입 결정:** 변수를 선언할 때 구체적인 자료형 대신 `var`를 적으면, 컴파일러가 우변에 있는 대입 데이터의 형태를 보고 자료형을 자동으로 알아내어 지정해 줍니다.
* **주의점:** 자바스크립트나 파이썬처럼 실행 중에 타입이 마음대로 변하는 언어(동적 타이핑)가 아닙니다. 컴파일하는 순간에 이미 자료형이 굳어지는 것이며, 메서드 내부의 '지역 변수'로 선언할 때만 제한적으로 사용할 수 있습니다.

---

### 05. 입력과 자료형 변환 (Type Casting)
* **Console.ReadLine():** 키보드로 입력한 값을 읽어오는 C#의 표준 입력 기능입니다. 중요한 점은 사용자가 숫자를 타이핑하더라도 컴퓨터는 무조건 '문자열(string)' 형태로 데이터를 받아들인다는 것입니다.
* **명시적 형변환의 필요성:** 문자열로 입력된 숫자를 가지고 계산(`+`, `-` 등)을 하려면, 문자열 형태를 강제로 진짜 숫자 형태로 바꾸는 변환 과정이 필수적입니다.
* **Parse 및 Convert 메서드:** C#에서는 문자열을 정수로 바꾸어 주는 `int.Parse()`나 데이터 형식을 안전하게 변경해 주는 `Convert.ToInt32()` 같은 전용 변환 기능을 제공하며, 이를 거쳐야만 정상적인 숫자 연산이 가능해집니다.


## 2. 조건문

> **상황에 따라 프로그램의 실행 흐름을 바꾸는 다양한 C# 조건문의 구조와 작동 원리 정리**

---

### 01. if / if else / if else if 조건문
* **if 조건문:** 소괄호 `()` 안의 조건식이 참(`true`)일 때만 중괄호 `{}` 안의 코드 블록을 실행합니다. C#에서는 조건식의 결과가 반드시 `bool` 타입(`true/false`)이어야만 합니다.
* **if else 조건문:** 조건식이 참일 때 실행할 포지션과, 거짓(`false`)일 때 실행할 포지션을 명확하게 이분법으로 나누어 제어할 때 사용합니다.
* **if else if 조건문:** 비교해야 할 조건이 여러 개일 때 순차적으로 조건을 검사하는 구조입니다. 위에서부터 차례대로 검사하다가 처음으로 참이 되는 블록을 만나면 해당 코드를 실행한 뒤, 아래에 남은 나머지 조건들은 전부 건너뛰고 조건문 전체를 빠져나옵니다.

---

### 02. 중첩 조건문
* **조건문 내부의 조건문:** 하나의 조건문 블록(`{}`) 내부에 또 다른 if 조건문을 집어넣어 구조화하는 방식입니다.
* **작동 원리:** 먼저 바깥쪽의 1차 조건문이 참(`true`)으로 만족해야만 안쪽에 있는 2차 세부 조건문을 검사하는 단계적 필터링 방식으로 작동합니다. 너무 깊게 중첩하면 코드의 가독성이 떨어질 수 있습니다.

---

### 03. switch 조건문
* **값 중심의 분기 처리:** 조건식의 참/거짓을 따지는 if문과 달리, 변수나 식의 '특정 값'이 무엇이냐에 따라 실행할 코드를 뚝뚝 끊어서 매칭하는 구조입니다.
* **case와 break:** `case 값:` 형태로 조건을 나열하며, 해당 case의 코드가 끝나는 지점에는 반드시 `break;` 키워드를 적어주어야 switch문을 정상적으로 탈출할 수 있습니다. 
* **default:** 어떤 case와도 일치하는 값이 없을 때 예외적으로 실행되는 영역으로, if문의 else와 같은 역할을 합니다.

---

### 04. 삼항 조건 연산자
* **한 줄로 쓰는 조건문:** `조건식 ? 참일_때의_값 : 거짓일_때의_값` 형태로 사용하는 C#의 간결한 제어 연산자입니다.
* **특징:** 단순한 조건 판단을 통해 변수에 값을 바로 대입하거나 출력할 때 코드를 획기적으로 줄여줍니다. if else문처럼 긴 코드 블록을 만들지 않고 물음표(`?`)와 콜론(`:`)만으로 깔끔하게 처리할 수 있어 자주 활용됩니다.

## 3. 반복문
# 3. 반복문과 배열

## 01. 반복문과 배열의 연계
* **데이터 집합 처리:** 배열(Array)은 같은 종류의 데이터들을 하나의 변수 이름 아래 한 줄로 나열해 둔 방 공간들과 같습니다. 
* **반복문과의 시너지:** 배열의 각 방에 접근하려면 `[0]`, `[1]`, `[2]` 같은 방 번호(인덱스)를 써야 하는데, 이 방 번호를 반복문의 변수로 처리하여 거대한 배열 데이터를 단 몇 줄의 코드로 한 번에 제어할 수 있습니다.

---

## 02. while / do while 반복문
* **while 반복문:** 소괄호 `()` 안의 조건식이 참(`true`)을 유지하는 동안 중괄호 내부의 코드를 끝없이 반복합니다. 반복을 시작하기 전에 조건식부터 먼저 검사하기 때문에, 처음부터 조건이 거짓이면 코드가 단 한 번도 실행되지 않습니다.
* **do while 반복문:** while문과 달리, 일단 중괄호 내부의 코드를 **무조건 최소 한 번은 실행**한 뒤에 하단의 조건을 검사합니다. 조건이 거짓이더라도 최초 1회 실행이 보장되어야 하는 상황(예: 메뉴판 출력 후 입력받기)에 사용됩니다.

---

## 03. for / 역 for 반복문
* **for 반복문:** `(초기식; 조건식; 증감식)` 구조를 사용하여 정해진 횟수만큼 정확하게 바퀴수를 돌릴 때 사용하는 가장 대표적인 반복문입니다.
* **역 for 반복문:** 숫자를 증가시키는 것이 아니라, 최대 수치에서 시작하여 `i--` 연산자를 통해 숫자를 깎아 내려가며 반대로 순회하는 방식입니다. 배열의 맨 마지막 칸부터 역순으로 데이터를 검사하거나 삭제할 때 데이터 위치가 꼬이지 않도록 하기 위해 자주 활용됩니다.

---

## 04. foreach 반복문 (C#의 핵심)
* **데이터 중심의 자동 순회:** 배열이나 리스트 같은 집합 데이터의 첫 번째 칸부터 마지막 칸까지 컴퓨터가 자동으로 이동하며 알맹이 데이터를 하나씩 순서대로 훑고 지나가는 방식입니다.
* **안전성과 간결함:** 개발자가 직접 `[i]` 같은 방 번호나 배열의 전체 길이를 계산해서 적어줄 필요가 없기 때문에, 인덱스 범위를 초과하는 메모리 오류를 원천 차단하는 매우 안전하고 가독성 높은 C# 전용 문법입니다.

---

## 05. 중첩 반복문
* **반복문 내부의 반복문:** 하나의 반복문 블록 내부에 또 다른 반복문 구조를 집어넣은 형태입니다.
* **작동 원리:** 바깥쪽 반복문이 딱 1바퀴 돌 때, 안쪽에 있는 내부 반복문은 지정된 횟수만큼 처음부터 끝까지 전체 한 바퀴를 완전히 다 돌고 나옵니다. 2차원 평면 좌표를 훑거나 행렬 데이터를 처리할 때 주로 사용됩니다.

---

## 06. break / continue 키워드
* **break 키워드:** 반복문을 실행하다가 이 키워드를 만나는 즉시, 남아있는 반복 횟수가 얼마나 되든 상관없이 그 자리에 멈춰 서서 **반복문 전체를 강제로 탈출**합니다. 보통 특정 데이터나 목표를 찾았을 때 불필요한 반복을 멈추기 위해 사용합니다.
* **continue 키워드:** break처럼 탈출하는 것이 아니라, 실행 중이던 해당 바퀴의 남은 아래쪽 코드들만 패스하고 **다음 바퀴의 시작 지점(조건 검사 또는 증감식)으로 점프**하여 반복을 계속 이어가게 만드는 키워드입니다. 특정 조건의 데이터만 건너뛰고 싶을 때 사용됩니다.

## 4. 클래스와 객체 지향 (기본)

### 01. 추상화(Abstraction)와 클래스 개요
* **추상화의 개념:** 복잡한 현실 세계의 사물이나 개념에서 **필요한 핵심적인 특징(속성과 행동)만 뽑아내어** 프로그램 내의 데이터 형태로 단순화하는 설계 과정입니다. 예를 들어 '마트 고객'을 추상화한다면 이름, 회원번호, 포인트 등의 데이터만 추출하는 식입니다.
* **클래스(Class)의 정의:** 추상화를 통해 뽑아낸 데이터(변수)와 기능(메서드)을 하나의 틀로 묶어놓은 **설계도**이자 프로그래머가 직접 정의하는 새로운 '참조 자료형'입니다.

---

### 02. 클래스의 생성과 사용 (인스턴스화)
* **객체(Object)와 인스턴스:** 클래스라는 설계도를 바탕으로 메모리(힙 영역)에 실제 가공되어 만들어진 실체를 '인스턴스(Instance)' 또는 객체라고 부릅니다.
* **new 키워드:** 설계도인 클래스로부터 실제 메모리를 할당받아 객체를 찍어낼 때는 반드시 `new` 키워드를 사용해야 합니다. 
* **참조 변수를 통한 접근:** 생성된 객체는 메모리 주소를 가지며, 대입된 변수 이름 뒤에 도트 연산자(`.`)를 붙여서 객체 내부의 변수나 기능들을 자유롭게 호출하고 제어할 수 있습니다.

---

### 03. 클래스의 변수 (멤버 변수와 속성)
* **인스턴스 변수(필드):** 클래스 내부 영역에 선언되어 객체가 가질 수 있는 고유한 데이터 상자들을 의미합니다. 
* **상태의 유지:** 이 변수들은 메서드 내부의 지역 변수와 달리, 객체가 메모리에 살아있는 동안 유지되며 해당 객체의 현재 '상태(State)'를 대변하는 역할을 담당합니다.
    </div>
  </div>
</div>

<script>
function openTab(tabId, element) {
  var contents = document.querySelectorAll(".tab-content");
  contents.forEach(function(content) {
    content.classList.remove("active");
  });
  var tabs = document.querySelectorAll(".local-nav-item");
  tabs.forEach(function(tab) {
    tab.classList.remove("active");
  });
  document.getElementById(tabId).classList.add("active");
  element.classList.add("active");
}
</script>
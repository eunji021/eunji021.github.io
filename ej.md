---
layout: post
title: "개발 언어 기초 (Languages)"
category: tech-fundamentals
author: eunji
short-description: "C언어, C#, Python, Java 통합 핵심 이론 문법 및 예제 실습 로그"
---

# 💻 개발 언어 기초 (Languages)

<details open>
  <summary>1. 학습한 언어 종류 및 목적 (Language Stack Overview)</summary>
  <div class="details-content" markdown="1">
* **C언어:** 하드웨어 가속, 임베디드 저수준 메모리 수동 제어(포인터 및 주소 참조) 학습
* **C# (.NET):** 객체지향 기반의 윈도우 데스크톱 마트 관리 애플리케이션 및 비동기 GUI 구현
* **Python:** 센서 데이터 전처리 시뮬레이터, 이동 평균 필터 알고리즘 모델링 및 검증
* **Java:** JVM 가상 머신 기반 플랫폼 독립 프로그래밍 및 클래스, 인터페이스 설계
  </div>
</details>

<details>
  <summary>2. 핵심 문법 및 개념 정리 (Key Concepts)</summary>
  <div class="details-content" markdown="1">
### 📌 C/C++ 포인터와 메모리 관리
- 스택(Stack) 영역과 힙(Heap) 영역의 물리적 메모리 구분 구조.
- 포인터 변수 참조(`*`, `&`) 및 수동 동적 할당(`malloc`/`free`)의 안정적 제어.

### 📌 C# & Java 객체지향 프로그래밍 (OOP)
- 캡슐화, 상속, 다형성을 활용한 유지보수가 쉬운 모듈식 구조 설계.
- 추상 클래스(Abstract Class)와 인터페이스(Interface)의 차이점 및 장단점 분석.
  </div>
</details>

<details>
  <summary>3. 주요 실습 코드 예제 및 주석 (Code Snippet & Annotation)</summary>
  <div class="details-content" markdown="1">
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
</details>

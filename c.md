---
layout: post
title: "C언어 기초 내용"
permalink: /c-language/
---
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

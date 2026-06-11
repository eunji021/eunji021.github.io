---
layout: post
title: "실시간 안전 장비 착용 여부 시스템"
category: projects
author: eunji
short-description: "ESP32 게이트웨이를 이용해 작업자 안전모와 조끼의 수집 센서 상태를 블루투스로 패킹 취합하는 관제 아키텍처"
---

<style>
  /* 탭 네비게이션 스타일 */
  .tabs-nav {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;
    border-bottom: 2px solid rgba(16, 185, 129, 0.2);
    padding-bottom: 12px;
  }
  .tab-btn {
    background: transparent;
    border: none;
    color: #64748b;
    font-size: 1.15rem;
    font-weight: 700;
    font-family: 'Pretendard', sans-serif;
    padding: 10px 24px;
    cursor: pointer;
    border-radius: 8px;
    transition: all 0.2s ease;
  }
  .tab-btn:hover {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.05);
  }
  .tab-btn.active {
    color: #10B981;
    background: rgba(16, 185, 129, 0.1);
  }
  
  /* 탭 콘텐츠 영역 스타일 */
  .tab-content {
    display: none;
    animation: fadeIn 0.4s ease-out forwards;
  }
  .tab-content.active {
    display: block;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* PPT 플레이스홀더 스타일 */
  .ppt-placeholder {
    width: 100%;
    aspect-ratio: 16 / 9;
    background: rgba(6, 9, 15, 0.6);
    border: 2px dashed rgba(16, 185, 129, 0.3);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #94a3b8;
    font-family: 'Pretendard', sans-serif;
    text-align: center;
    padding: 20px;
  }
</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-ppt">PPT</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

  <!-- 1. PPT 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content active">
    <div class="ppt-placeholder">
      <div style="font-size: 4rem; margin-bottom: 20px;">📊</div>
      <h3 style="color: #ffffff; margin-top: 0; margin-bottom: 10px; border-bottom: none; text-shadow: none;">프로젝트 발표 자료 (PPT)</h3>
      <p style="color: #94a3b8; font-size: 1rem; margin-bottom: 0;">여기에 슬라이드 이미지 또는 iframe 코드를 삽입하여 발표 자료를 보여줄 수 있습니다.</p>
    </div>
  </div>

  <!-- 2. 소개 탭 콘텐츠 -->
  <div id="tab-intro" class="tab-content" markdown="1">

## 공사장 안전장비 실시간 착용여부 시스템
* **진행 기간:** 2025.03 ~ 2025.06
* **주요 역량:** 임베디드 펌웨어 구조 설계, 여러 장치의 데이터 묶음 전송 및 타이밍 제어, 하드웨어 예외 처리 코드 구현
* **사용 기술:** C/C++ (Arduino IDE), ESP32, BLE, Bluetooth Classic, MPU6050 센서, App Inventor

---

### MY CORE ROLE & ACHIEVEMENTS (내가 주도한 핵심 성과)
* 스마트폰 앱의 블루투스 연결 한계를 중계기로 해결 (통신 성공률 100% 달성)
* 데이터가 꼬이지 않게 묶어 보내는 프로토콜 구현 (타임 슬라이싱 데이터 스트리밍)
* 센서 데이터 정제 및 1분 무동작/탈착 감지 로직 최적화

---

### 1. 프로젝트 개요 (Overview)
* **개발 배경:** 기존 수동 점검의 한계를 극복하고 안전모/안전조끼 미착용 및 낙상 사고를 실시간으로 인지하기 위함.
* **개발 목적:** 센서 데이터와 블루투스 통신을 융합해 관리자 앱으로 통합 관제하는 IoT 안전 시스템 구축.

  </div>

  <!-- 3. 코드 탭 콘텐츠 -->
  <div id="tab-code" class="tab-content" markdown="1">

### 💻 아두이노(C/C++) 펌웨어 핵심 제어 로직
추후 이곳에 실제 작성하신 아두이노 소스코드를 복사해서 붙여넣으세요. 아래는 예시 뼈대입니다.

```cpp
// [여기에 코드를 붙여넣으세요]
// 예시: 
// void setup() {
//   Serial.begin(115200);
//   // 초기화 코드
// }
//
// void loop() {
//   // 센서 데이터 수집 및 BLE 전송 로직 실행
// }
```

  </div>
</div>

<script>
  // 탭 전환 스크립트
  document.addEventListener("DOMContentLoaded", () => {
    const btns = document.querySelectorAll(".tab-btn");
    const contents = document.querySelectorAll(".tab-content");

    btns.forEach(btn => {
      btn.addEventListener("click", () => {
        // 모든 탭과 콘텐츠의 활성화 상태 제거
        btns.forEach(b => b.classList.remove("active"));
        contents.forEach(c => c.classList.remove("active"));

        // 클릭된 탭과 해당 콘텐츠 활성화
        btn.classList.add("active");
        document.getElementById(btn.getAttribute("data-target")).classList.add("active");
      });
    });
  });
</script>

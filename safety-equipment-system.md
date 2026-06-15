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
  /* 슬라이드 뷰어(Carousel) 스타일 */
  .carousel-container {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #111827;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  }
  .carousel-slide {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    opacity: 0;
    transition: opacity 0.4s ease-in-out;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
  }
  .carousel-slide.active {
    opacity: 1;
    z-index: 1;
  }
  .carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(16, 185, 129, 0.4);
    color: white;
    border: none;
    font-size: 1.5rem;
    padding: 15px 20px;
    cursor: pointer;
    z-index: 10;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .carousel-btn:hover {
    background: rgba(16, 185, 129, 0.9);
  }
  .carousel-btn.prev { left: 15px; }
  .carousel-btn.next { right: 15px; }
</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-ppt">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

    <!-- 1. 한눈에 보기 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content active">
    <div class="carousel-container" id="slide-carousel">
      <!-- 슬라이드 이미지들 -->
      <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_1.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_2.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_3.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_4.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_5.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_6.png');"></div>
      
      <!-- 컨트롤 버튼 -->
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
  </div>

  <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const nextBtn = document.querySelector('.carousel-btn.next');

    function updateButtons() {
      prevBtn.style.display = (currentSlide === 0) ? 'none' : 'block';
      nextBtn.style.display = (currentSlide === slides.length - 1) ? 'none' : 'block';
    }

    function moveSlide(direction) {
      const newIndex = currentSlide + direction;
      if (newIndex < 0 || newIndex >= slides.length) return;
      
      slides[currentSlide].classList.remove('active');
      currentSlide = newIndex;
      slides[currentSlide].classList.add('active');
      
      updateButtons();
    }
    
    // Initialize buttons on load
    updateButtons();
  </script>

  <!-- 2. 소개 탭 콘텐츠 -->
  <div id="tab-intro" class="tab-content" markdown="1">

##  전담한 역할 및 문제 해결 과정

### 1. 프로젝트 정보 및 결과물 요약
* **프로젝트 기간:** 2025년 3월 ~ 2025년 9월 
* **팀원 구성**
* **참여 인원:** 4명 
  - 팀원 (최성용): 하드웨어 회로 설계, 센서 노드 원시 코드 작성
  - 팀원 (구민서): 외형 PETG 3D 케이스 설계 및 구조물 조립
  - 팀원 (이명은): ESP32-앱 간 블루투스 통신 기초 테스트 및 디버깅, 앱 표지 디자인
* **프로젝트 개요:** 안전모에 센서를 달아 작업자가 장비를 잘 썼는지, 현장에서 쓰러지거나 넘어지지 않았는지 블루투스로 받아와 확인하는 실시간 안전 모니터링 시스템임.
* **핵심 결과물:** 앱인벤터 툴이 가진 블루투스 연결 개수 한계를 하드웨어 중계기 아이디어로 풀었음. 스마트폰 화면 하나에 여러 명의 작업자 상태가 동시에 뜨도록 화면과 통신 구조를 완성함.

---

### 2. 내가 전담한 역할
* **모바일 관제 어플리케이션(앱인벤터) 구현:** 관리자가 스마트폰으로 현장 상황을 볼 수 있도록 표 형태의 화면을 디자인하고, 들어오는 데이터를 제 칸에 뿌려주는 블록 코딩 전체를 전담함.
* **무선 통신 연결 및 데이터 설계:** 메인 중계기 기기와 스마트폰 앱 사이에 주고받을 블루투스(BLE) 데이터 형태를 직접 정의하고 연동 테스트를 진행함.

---

### 3. 개발 과정 중 발생한 문제 및 해결 내용 (트러블 슈팅)

####  01. 여러 대의 기기를 앱에 동시에 연결할 수 없는 한계 해결
> **어려움**
> 현장 작업자가 여러 명이라 안전모마다 독립된 송신 기기가 들어가야 했음. 하지만 앱인벤터 구조상 스마트폰 하나에 여러 개의 블루투스 기기를 동시에 안정적으로 직접 연결하는 것이 불가능했음.

> **해결 내용**
> 스마트폰 앱에서 기기 여러 개를 직접 잡는 방식을 포기함. 작업자들의 기기 신호를 한곳으로 모아줄 **'메인 중계기(ESP32)'**를 중간에 하나 더 두는 방식을 냈음. 각 작업자의 기기가 보낸 신호를 중간 중계기가 다 받아낸 뒤, 스마트폰 앱에는 이 중계기 1대만 연결해서 데이터를 한 번에 밀어 넣어주는 통신 구조를 만들어 문제를 해결함.

####  02. 들어오는 데이터가 섞이고 뭉개지는 오류 해결
> **어려움**
> 중간 중계기 한 대가 여러 명의 데이터를 모아서 스마트폰 앱으로 한꺼번에 던지다 보니, 앱인벤터 쪽에서 이 데이터가 누구의 데이터인지 구분을 못 해 화면에 엉뚱한 값이 찍히거나 글자가 깨지는 현상이 생김.

> **해결 내용**
> 데이터를 보낼 때 무작정 보내지 않고 `[작업자 번호/현재 위치/장비 착용 상태]` 순서로 데이터 사이에 슬래시 나 쉼표 같은 약속된 기호를 넣어서 패킷을 묶어 보내도록 수정함. 앱인벤터 블록 코딩에서는 문자열 분리(Split) 블록을 사용해 들어온 데이터를 기호 기준으로 똑똑하게 쪼갠 뒤, 화면의 `작업자1`, `작업자2` 칸에 정확히 찾아 들어가도록 로직을 짜서 데이터가 섞이는 문제를 잡았음.

####  03. 쉴 새 없이 들어오는 신호로 인한 화면 멈춤 현상 해결
> **어려움**
> 여러 명의 데이터가 블루투스를 통해 실시간으로 너무 자주 들어오다 보니, 앱인벤터 화면이 버퍼링을 버티지 못하고 수시로 멈추거나 앱이 강제로 꺼지는 현상이 발생함.

> **해결 내용**
> 무조건 신호를 계속 쏘는 방식 대신, 주기를 1~2초 간격으로 조절하고 평소에는 조용하다가 작업자가 안전모를 벗거나 쓰러지는 등의 '상태 변화'가 생겼을 때만 즉시 신호를 쏘도록 송신 방식을 바꿨음. 데이터가 들어오는 통로의 부하를 줄여주어 앱이 끊김 없이 부드럽게 작동하도록 완성함.

####  04. 중계기(Master)의 다중 데이터 수신 병목 및 유실 현상 해결
> **어려움**
> 각 작업자의 기기(Slave)들이 중계기(Master) 한 대를 향해 동시에 블루투스 신호를 보내다 보니, 데이터가 같은 시간에 겹쳐서 들어올 때 신호가 충돌하여 일부 작업자의 상태 데이터가 앱으로 전달되지 못하고 사라지는(유실) 현상이 생김.

> **해결 내용**
> 중계기(ESP32) 펌웨어 코드를 직접 수정하여 통신 안정성을 높였음. 각 작업자의 기기들이 무작작 신호를 던지지 않고, 중계기가 `작업자1 신호 줘`, `작업자2 신호 줘` 하는 식으로 순서대로 신호를 요청하고 받아오는 수신 로직을 중계기 코드로 구현함. 또한, 들어온 데이터가 겹치더라도 안전하게 임시 보관했다가 순서대로 앱에 보내주도록 중계기 내부에 데이터 버퍼링 구조를 짜넣어 데이터가 중간에 날아가는 문제를 완벽히 해결함.


## 팀 프로젝트 개요 
* **참여 인원:** 4명 
  - 팀원 (최성용): 하드웨어 회로 설계, 센서 노드 원시 코드 작성
  - 팀원 (구민서): 외형 PETG 3D 케이스 설계 및 구조물 조립
  - 팀원 (이명은): ESP32-앱 간 블루투스 통신 기초 테스트 및 디버깅, 앱 표지 디자인


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

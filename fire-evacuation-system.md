---
layout: post
title: "실시간 화재 대피 유도 시스템"
category: projects
author: eunji
short-description: "실시간 화재 감지 및 다익스트라 최적 경로 기반 가변형 대피 유도 모듈"
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
  /* Code Accordion Styles */
  .code-accordion {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    margin-bottom: 15px;
    overflow: hidden;
  }
  .code-accordion summary {
    padding: 15px 20px;
    background: #0f172a;
    color: #10b981;
    font-weight: 600;
    cursor: pointer;
    list-style: none;
    position: relative;
    font-size: 1.1rem;
    outline: none;
  }
  .code-accordion summary::-webkit-details-marker {
    display: none;
  }
  .code-accordion summary::after {
    content: '▼';
    position: absolute;
    right: 20px;
    top: 15px;
    font-size: 0.9rem;
    color: #94a3b8;
    transition: transform 0.3s;
  }
  .code-accordion[open] summary::after {
    transform: rotate(180deg);
  }
  .accordion-content {
    padding: 20px;
    border-top: 1px solid #334155;
  }
  
  /* App Inventor Viewer Styles */
  .app-inventor-viewer {
    width: 100%;
    min-height: 250px;
    background: rgba(15, 23, 42, 0.4);
    border: 2px dashed rgba(16, 185, 129, 0.4);
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 20px 0;
    text-align: center;
    font-family: 'Pretendard', sans-serif;
  }
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
        <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_1.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_2.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_3.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_4.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_5.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_6.png');"></div>
      
      <!-- 컨트롤 버튼 -->
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
      
    <!-- 프로젝트 결과물 섹션 -->
    <div style="margin-top: 40px; text-align: center;">
      <h3 style="color: #10B981; font-family: 'Orbitron', 'Pretendard', sans-serif; margin-bottom: 20px;">🔥 프로젝트 최종 결과물</h3>
      <div style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
        <img src="{{ site.baseurl }}/assets/img/projects/fire_result.png" alt="실시간 화재 대피 유도 시스템 결과물" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
        <p style="color: #94a3b8; font-size: 0.95rem; margin-top: 15px;">이곳에 <strong>fire_result.png</strong> 라는 이름으로 사진을 저장하시면 자동으로 표시됩니다.</p>
      </div>
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

# 🛠️ 실시간 화재 대피 유도 시스템 (Smart Evacuation Guide)

<details open>
  <summary>1. 프로젝트 개요 (Overview)</summary>
  <div class="details-content" markdown="1">
* **진행 기간:** YYYY.MM ~ YYYY.MM (개인 / 팀 N명)
* **기획 배경:** 
  > 화재 발생 시 고정형 비상구 안내 표시판으로 인해 작업자가 화재 방향으로 대피하는 오안내 문제를 해결하고자 기획되었습니다.
* **프로젝트 목적:** 
  > 화재 센서 로그 데이터를 기반으로 동적 대피 유도 LED 패널을 제어해 안전 대피 경로를 가이드하는 시스템을 구축합니다.
  </div>
</details>

<details>
  <summary>2. 사용 기술 및 개발 환경 (Tech Stack & Environment)</summary>
  <div class="details-content" markdown="1">
* **Core Languages:** C/C++, Python
* **Hardware & Modules:** ESP32, Flame/Smoke Sensors, LED Dot Matrix Modules, Buzzer
* **Software & Toolchain:** VS Code, PlatformIO, Arduino IDE
* **통신 프로토콜:** Wi-Fi / WebSockets, Serial, I2C
  </div>
</details>

<details>
  <summary>3. 핵심 기능 및 구현 내용 (Core Features)</summary>
  <div class="details-content" markdown="1">
* **핵심 기능 1 (실시간 센서 기반 동적 다익스트라 계산):**
  - [상세 설명] 화재 감지 센서값에 가중치를 부여하여 실시간 위험 노드를 우회하는 최적 대피 경로 계산 알고리즘.
* **핵심 기능 2 (가변형 LED 방향 표시 제어):**
  - [상세 설명] 계산된 경로 방향에 맞춰 대피 비상구 LED matrix 화살표 방향을 동적으로 스위칭하는 제어 구조.
  </div>
</details>

<details>
  <summary>4. 개발 중 겪은 문제와 해결 과정 (Troubleshooting)</summary>
  <div class="details-content" markdown="1">
### ⚠️ Issue 1: 다중 노드 센서 데이터 수집 병목 및 레이턴시
* **현상:** 
  > 센서 노드가 동시에 데이터를 게이트웨이로 전송할 때 패킷 유실 및 딜레이 발생.
* **원인 분석:** 
  > 동기식 통신 대기로 인한 CPU 차단 현상 확인.
* **해결책:** 
  > FreeRTOS 태스크 분리 및 비동기 웹소켓 통신 인터럽트 제어로 변환하여 대기 시간 단축.
  </div>
</details>

<details>
  <summary>5. 프로젝트 결과 및 느낀 점 (Conclusion & Retrospective)</summary>
  <div class="details-content" markdown="1">
* **최종 성과:** 
  > 최적 경로 수렴 시간 및 모듈 구동 테스트 성과를 정리합니다.
* **배운 점:** 
  > 그래프 탐색 알고리즘(Dijkstra)의 하드웨어 실시간 적용 및 임베디드 멀티태스킹 설계 능력을 습득한 점을 기록합니다.
  </div>
</details>

  </div>

  <!-- 3. 코드 탭 콘텐츠 -->
  <div id="tab-code" class="tab-content" markdown="1">

## 핵심 소스코드

<details class="code-accordion">
  <summary>코드 섹션 1</summary>
  <div class="accordion-content" markdown="1">

{% highlight cpp %}
// 코드를 이곳에 붙여넣으세요.
{% endhighlight %}

  </div>
</details>

  </div>
</div>

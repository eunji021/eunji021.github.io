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
  

  

  
    
<style>
/* 시뮬레이터 스타일 */
.sim-container {
  width: 100%; height: 500px;
  background: #0f172a;
  border: 4px solid #10b981; /* STABLE */
  border-radius: 12px;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
  display: flex; position: relative;
  transition: all 0.3s; overflow: hidden;
  margin-bottom: 20px;
}
.sim-container.emergency { border-color: #ef4444; box-shadow: 0 0 30px rgba(239, 68, 68, 0.6); animation: flashRed 0.8s infinite alternate; }
@keyframes flashRed { from { box-shadow: 0 0 10px #ef4444; } to { box-shadow: 0 0 50px #ef4444, inset 0 0 30px #ef4444; } }

.sim-sidebar {
  width: 250px; border-right: 2px dashed #334155; padding: 20px;
  display: flex; flex-direction: column; align-items: center; justify-content: center; background: #1e293b;
  box-shadow: 5px 0 15px rgba(0,0,0,0.3); z-index: 10;
}
.app-badge {
  background: #10b981; color: white; padding: 6px 12px; border-radius: 20px; font-weight: bold; text-align: center; margin-bottom: 30px; font-size: 1.1rem; letter-spacing: 1px; transition: background 0.3s;
}
.info-text { font-size: 0.95rem; color: #94a3b8; text-align: center; margin-bottom: 40px; line-height: 1.5; }

.fire-icon {
  width: 70px; height: 70px; cursor: grab; user-select: none;
  display: flex; align-items: center; justify-content: center; font-size: 3rem;
  background: rgba(239, 68, 68, 0.1); border-radius: 50%; border: 2px dashed rgba(239, 68, 68, 0.5);
  transition: transform 0.1s; position: absolute; z-index: 50;
}
.fire-icon:active { cursor: grabbing; transform: scale(1.1); background: rgba(239, 68, 68, 0.3); }

.fire-dock {
  width: 80px; height: 80px; border: 2px dashed #475569; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}

.sim-map {
  flex: 1; position: relative; display: flex; align-items: center; justify-content: center;
  background: radial-gradient(circle at center, rgba(16,185,129,0.05) 0%, transparent 70%);
}

.blueprint-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 15px;
  width: 90%; height: 80%; padding: 15px;
  background: rgba(255,255,255,0.02);
  border: 2px solid #334155; border-radius: 10px; position: relative;
}
.room {
  background: #1e293b; border: 2px solid #475569; border-radius: 8px;
  display: flex; align-items: center; justify-content: center; flex-direction: column;
  color: #94a3b8; font-weight: bold; font-size: 1.1rem; transition: all 0.3s;
}
.room.dropzone { border: 2px dashed #64748b; }
.room.fire { background: #ef4444 !important; border-color: #ef4444; color: white; box-shadow: 0 0 30px rgba(239, 68, 68, 0.8); }
.room.corridor { background: rgba(15, 23, 42, 0.6); border-style: dashed; }
.room.exit { background: rgba(16, 185, 129, 0.2); border-color: #10b981; color: #10b981; }


.route-path-standby {
  fill: none; stroke: rgba(16, 185, 129, 0.4); stroke-width: 6; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 15, 15;
  filter: drop-shadow(0 0 5px rgba(16, 185, 129, 0.5));
}
.route-svg {
  position: absolute; top: 0; left: 0; pointer-events: none; width: 100%; height: 100%; z-index: 5;
}
.route-path {
  fill: none; stroke: #38bdf8; stroke-width: 8; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 20, 20; animation: flowWave 0.8s linear infinite;
  opacity: 0; transition: opacity 0.3s;
  filter: drop-shadow(0 0 8px #38bdf8);
}
@keyframes flowWave { from { stroke-dashoffset: 40; } to { stroke-dashoffset: 0; } }

</style>

  <!-- 탭 버튼 영역 교체 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-simulator">체험 시뮬레이터</button>
    <button class="tab-btn" data-target="tab-ppt">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

  <!-- 체험 시뮬레이터 탭 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container" id="sim-main-fire">
      
      <div class="sim-sidebar">
        <div class="app-badge" id="fire-badge">STABLE</div>
        <div class="info-text">
          우측 평면도의 방에<br>🔥 아이콘을 드래그하여<br>화재를 발생시켜 보세요.
        </div>
        <div class="fire-dock" id="fire-dock"></div>
      </div>
      
      <div class="sim-map" id="sim-map-area">
        <div class="blueprint-grid" id="bp-grid">
          <div class="room dropzone" id="r1">Room A</div>
          <div class="room dropzone corridor" id="c1">Corridor</div>
          <div class="room dropzone" id="r2">Room B</div>
          
          <div class="room exit" id="exit1">Exit Left 🚪</div>
          <div class="room corridor" id="c2">Main Hall</div>
          <div class="room exit" id="exit2">Exit Right 🚪</div>
          

          <!-- 다익스트라 대피 경로 시각화 -->
          <svg class="route-svg" id="route-svg">
            <!-- 기본 대기 상태의 LED 스트립 (은은한 초록색) -->
            <path class="route-path-standby" d="M 16.6% 25% L 16.6% 75% L 50% 75% L 83.3% 75% M 50% 25% L 50% 75%" />

            <path class="route-path" id="route-path-1" d="" />
            <path class="route-path" id="route-path-2" d="" />
          </svg>
        </div>
      </div>
      
      <!-- 화재 아이콘 (드래그 가능) -->
      <div class="fire-icon" id="fire-icon" title="화재 발생기">🔥</div>
      
    </div>
    <p style="text-align:center; color:#94a3b8; font-size:0.95rem;">💡 화재 위치가 변경되면 실시간으로 다익스트라 최단 경로가 재계산되어 대피 유도선이 바뀝니다.</p>
  </div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Tab Navigation
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      document.getElementById(btn.getAttribute('data-target')).classList.add('active');
      
      if (btn.getAttribute('data-target') === 'tab-simulator') {
        initFirePos();
      }
    });
  });

  // Simulator Logic
  const fireIcon = document.getElementById('fire-icon');
  const fireDock = document.getElementById('fire-dock');
  const simMain = document.getElementById('sim-main-fire');
  const badge = document.getElementById('fire-badge');
  const r1 = document.getElementById('r1');
  const r2 = document.getElementById('r2');
  const c1 = document.getElementById('c1');
  
  const path1 = document.getElementById('route-path-1');
  const path2 = document.getElementById('route-path-2');
  
  let currentFireRoom = null;

  function initFirePos() {
    const dockRect = fireDock.getBoundingClientRect();
    const simRect = simMain.getBoundingClientRect();
    fireIcon.style.left = (dockRect.left - simRect.left + dockRect.width/2 - fireIcon.offsetWidth/2) + 'px';
    fireIcon.style.top = (dockRect.top - simRect.top + dockRect.height/2 - fireIcon.offsetHeight/2) + 'px';
  }

  let isDragging = false;
  let startX, startY, initialX, initialY;
  
  fireIcon.addEventListener('mousedown', dragStart);
  fireIcon.addEventListener('touchstart', dragStart, {passive: false});
  
  function dragStart(e) {
    const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
    const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
    
    initialX = fireIcon.offsetLeft;
    initialY = fireIcon.offsetTop;
    startX = clientX;
    startY = clientY;
    isDragging = true;
    
    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', dragEnd);
    document.addEventListener('touchmove', drag, {passive: false});
    document.addEventListener('touchend', dragEnd);
    
    // Clear fire state while dragging
    clearFire();
  }
  
  function drag(e) {
    if (!isDragging) return;
    e.preventDefault();
    const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
    const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
    const dx = clientX - startX;
    const dy = clientY - startY;
    fireIcon.style.left = (initialX + dx) + 'px';
    fireIcon.style.top = (initialY + dy) + 'px';
  }
  
  function dragEnd(e) {
    isDragging = false;
    document.removeEventListener('mousemove', drag);
    document.removeEventListener('mouseup', dragEnd);
    document.removeEventListener('touchmove', drag);
    document.removeEventListener('touchend', dragEnd);
    
    checkDrop();
  }
  
  function clearFire() {
    r1.classList.remove('fire');
    r2.classList.remove('fire');
    c1.classList.remove('fire');
    simMain.classList.remove('emergency');
    badge.innerText = 'STABLE';
    badge.style.background = '#10b981';
    path1.style.opacity = '0';
    path2.style.opacity = '0';
    currentFireRoom = null;
  }
  
  function checkDrop() {
    const iconRect = fireIcon.getBoundingClientRect();
    const iconCx = iconRect.left + iconRect.width/2;
    const iconCy = iconRect.top + iconRect.height/2;
    
    const rooms = [r1, c1, r2];
    let droppedRoom = null;
    
    for(let room of rooms) {
      const rect = room.getBoundingClientRect();
      if(iconCx > rect.left && iconCx < rect.right && iconCy > rect.top && iconCy < rect.bottom) {
        droppedRoom = room;
        break;
      }
    }
    
    if(droppedRoom) {
      // Snap to room center
      const simRect = simMain.getBoundingClientRect();
      const rect = droppedRoom.getBoundingClientRect();
      fireIcon.style.left = (rect.left - simRect.left + rect.width/2 - fireIcon.offsetWidth/2) + 'px';
      fireIcon.style.top = (rect.top - simRect.top + rect.height/2 - fireIcon.offsetHeight/2) + 'px';
      
      triggerFire(droppedRoom);
    } else {
      // Snap back to dock
      initFirePos();
    }
  }
  
  function triggerFire(room) {
    room.classList.add('fire');
    simMain.classList.add('emergency');
    badge.innerText = 'EMERGENCY';
    badge.style.background = '#ef4444';
    
    // Draw Routes based on Fire Location (Dijkstra simulation)
    // Grid centers approx:
    // row 1: 16.6%, 50%, 83.3%
    // row 2: 16.6%, 50%, 83.3%
    // y-coords: 25%, 75%
    
    path1.style.opacity = '1';
    if(room === r1) {
      // Fire in Room A -> Escape from c1 to c2 to exit2
      path1.setAttribute('d', 'M 50% 25% L 50% 75% L 83.3% 75%');
      path2.style.opacity = '0';
    } else if(room === r2) {
      // Fire in Room B -> Escape from c1 to c2 to exit1
      path1.setAttribute('d', 'M 50% 25% L 50% 75% L 16.6% 75%');
      path2.style.opacity = '0';
    } else if(room === c1) {
      // Fire in Corridor 1 -> Room A escapes to exit1 directly, Room B escapes to exit2 directly
      path1.setAttribute('d', 'M 16.6% 25% L 16.6% 75%');
      path2.setAttribute('d', 'M 83.3% 25% L 83.3% 75%');
      path2.style.opacity = '1';
    }
  }

  setTimeout(initFirePos, 100);
});
</script>
<!-- 1. 한눈에 보기 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content">
    <div class="carousel-container" id="slide-carousel">
      <!-- 슬라이드 이미지들 -->
        <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_1.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_2.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_3.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_4.png');"></div>
        <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/fire_slides/slide_5.png');"></div>
      
      <!-- 컨트롤 버튼 -->
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
      
    <!-- 프로젝트 결과물 섹션 -->
    <div style="margin-top: 40px; text-align: center;">
      <h3 style="color: #10B981; font-family: 'Orbitron', 'Pretendard', sans-serif; margin-bottom: 20px;">프로젝트 최종 결과물</h3>
      <div style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
        <img src="{{ site.baseurl }}/assets/img/projects/fire_result.png" alt="실시간 화재 대피 유도 시스템 결과물" onerror="this.style.display='none'" style="width: 100%; max-width: 900px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); display: block; margin: 0 auto;">
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

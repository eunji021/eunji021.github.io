---
layout: post
title: "AI 유적지 가이드 앱"
category: projects
author: eunji
short-description: "딥러닝 기반 객체 인식 모델을 모바일 장치에 내장하여 주변 유적지를 실시간으로 탐지하고 안내하는 플랫폼"
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

  /* 프로젝트 C 시뮬레이터 CSS */
  .sim-container {
    width: 100%; height: 600px;
    background: #0f172a;
    border: 4px solid #10b981; /* STABLE Green */
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    display: flex; align-items: center; justify-content: center; position: relative;
    transition: all 0.5s; overflow: hidden;
    margin-bottom: 20px;
  }
  .sim-container.scanning { border-color: #3b82f6; box-shadow: 0 0 30px rgba(59, 130, 246, 0.6); animation: pulseBlue 1.5s infinite alternate; }
  @keyframes pulseBlue { from { box-shadow: 0 0 10px #3b82f6; } to { box-shadow: 0 0 40px #3b82f6, inset 0 0 20px #3b82f6; } }

  .sim-phone {
    width: 320px; height: 520px; background: #1e293b;
    border-radius: 40px; border: 10px solid #000;
    position: relative; overflow: hidden; font-family: 'Pretendard', sans-serif;
    box-shadow: 0 20px 40px rgba(0,0,0,0.8); z-index: 5;
    display: flex; flex-direction: column;
  }
  /* 노치 */
  .sim-phone::before {
    content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%);
    width: 120px; height: 25px; background: #000; border-radius: 0 0 15px 15px; z-index: 20;
  }
  /* 하단 바 */
  .sim-phone::after {
    content: ''; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%);
    width: 120px; height: 5px; background: rgba(255,255,255,0.4); border-radius: 5px; z-index: 20;
  }

  /* 카메라 뷰 (기본 화면) */
  .camera-view {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&w=400&q=80') center/cover;
    filter: brightness(0.7) blur(2px); transition: opacity 0.5s; z-index: 10;
  }
  .crosshair {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 200px; height: 200px; border: 2px dashed rgba(255,255,255,0.4); border-radius: 10px;
  }
  
  /* 바운딩 박스 */
  .bounding-box {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 180px; height: 240px; border: 3px solid #10b981; border-radius: 5px;
    background: rgba(16,185,129,0.1); display: none; z-index: 15;
    box-shadow: 0 0 15px rgba(16,185,129,0.5);
  }
  
  .typing-text {
    position: absolute; top: -30px; left: 0; color: #10b981; font-weight: bold; font-size: 0.9rem;
    white-space: nowrap; overflow: hidden; border-right: 2px solid #10b981; width: 0;
  }
  @keyframes typeText { from { width: 0; } to { width: 100%; } }
  @keyframes blinkCursor { 50% { border-color: transparent; } }

  /* 유적지 가이드 UI 화면 */
  .guide-ui {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: #0f172a; z-index: 11; opacity: 0; pointer-events: none; transition: opacity 0.8s;
    display: flex; flex-direction: column; padding: 40px 20px 20px 20px;
  }
  .guide-ui.active { opacity: 1; pointer-events: auto; }
  
  .guide-img { width: 100%; height: 180px; background: #334155; border-radius: 12px; margin-bottom: 20px; overflow: hidden; }
  .guide-img img { width: 100%; height: 100%; object-fit: cover; }
  
  .guide-title { color: #fff; font-size: 1.5rem; font-weight: bold; margin-bottom: 5px; }
  .guide-sub { color: #94a3b8; font-size: 0.9rem; margin-bottom: 15px; }
  .guide-desc { color: #cbd5e1; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex: 1; }
  
  .audio-wave { display: flex; align-items: center; justify-content: center; gap: 4px; height: 40px; margin-bottom: 20px; }
  .wave-bar { width: 4px; background: #38bdf8; border-radius: 2px; animation: waveAnim 1s infinite alternate ease-in-out; }
  .wave-bar:nth-child(2) { animation-delay: 0.2s; } .wave-bar:nth-child(3) { animation-delay: 0.4s; } .wave-bar:nth-child(4) { animation-delay: 0.1s; } .wave-bar:nth-child(5) { animation-delay: 0.5s; }
  @keyframes waveAnim { from { height: 10px; } to { height: 35px; } }
  
  .reset-btn { background: #334155; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: background 0.2s; }
  .reset-btn:hover { background: #475569; }

  /* 드래그 앤 드롭 아이템 */
  .pagoda-icon {
    position: absolute; right: 40px; bottom: 40px; width: 100px; height: 100px; cursor: grab; z-index: 30; user-select: none;
    border-radius: 12px; overflow: hidden; border: 3px solid #cbd5e1; box-shadow: 0 10px 20px rgba(0,0,0,0.5); transition: transform 0.1s;
  }
  .pagoda-icon:active { cursor: grabbing; transform: scale(1.05); border-color: #38bdf8; }
  .pagoda-icon img { width: 100%; height: 100%; object-fit: cover; pointer-events: none; }
  
  .pagoda-dock {
    position: absolute; right: 40px; bottom: 40px; width: 100px; height: 100px; border: 2px dashed #475569; border-radius: 12px;
    display: flex; align-items: center; justify-content: center; color: #475569; font-size: 0.8rem; text-align: center;
  }
</style>
</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-simulator">체험 시뮬레이터</button>
    <button class="tab-btn" data-target="tab-ppt">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

  
  <!-- 0. 체험 시뮬레이터 탭 콘텐츠 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container" id="sim-main-ai">
      
      <div class="sim-phone">
        <div class="camera-view" id="camera-view">
          <div class="crosshair"></div>
          <div class="bounding-box" id="bounding-box">
            <div class="typing-text" id="typing-text"></div>
          </div>
        </div>
        
        <div class="guide-ui" id="guide-ui">
          <div class="guide-img">
            <img src="https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&w=400&q=80" alt="Mireuksaji">
          </div>
          <div class="guide-title">미륵사지 석탑</div>
          <div class="guide-sub">국보 제11호 | 백제 시대</div>
          <div class="guide-desc">
            익산 미륵사지 석탑은 한국에 남아있는 가장 크고 오래된 석탑입니다. 백제 무왕 시대에 건립된 것으로 추정되며, 목탑의 구조를 석재로 구현한 독특한 양식을 띠고 있습니다.
          </div>
          <div class="audio-wave">
            <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
          </div>
          <button class="reset-btn" id="btn-reset">다시 촬영하기</button>
        </div>
      </div>
      
      <div class="pagoda-dock" id="pagoda-dock">Drag Me!</div>
      <div class="pagoda-icon" id="pagoda-icon">
        <img src="https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&w=200&q=80" alt="Pagoda">
      </div>
      
    </div>
    <p style="text-align:center; color:#94a3b8; font-size:0.95rem;">💡 우측 하단의 미륵사지 사진을 스마트폰 카메라 화면 중앙으로 드래그 앤 드롭 해보세요.</p>
  </div>
<!-- 1. 한눈에 보기 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content">
    <div class="carousel-container" id="slide-carousel">
      <!-- 슬라이드 이미지 (경로를 맞춰서 수정해주세요) -->
      <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/placeholder.png');"></div>
      
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
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
            resetSimulator();
          }
        });
      });

      // Carousel Logic
      let currentSlide = 0;
      const slides = document.querySelectorAll('.carousel-slide');
      const prevBtn = document.querySelector('.carousel-btn.prev');
      const nextBtn = document.querySelector('.carousel-btn.next');

      window.moveSlide = function(direction) {
        if(!slides.length) return;
        const newIndex = currentSlide + direction;
        if (newIndex < 0 || newIndex >= slides.length) return;
        slides[currentSlide].classList.remove('active');
        currentSlide = newIndex;
        slides[currentSlide].classList.add('active');
        updateButtons();
      }

      function updateButtons() {
        if(!prevBtn) return;
        prevBtn.style.display = (currentSlide === 0) ? 'none' : 'block';
        nextBtn.style.display = (currentSlide === slides.length - 1) ? 'none' : 'block';
      }
      updateButtons();

      // Simulator Logic
      const simMain = document.getElementById('sim-main-ai');
      const cameraView = document.getElementById('camera-view');
      const guideUi = document.getElementById('guide-ui');
      const boundingBox = document.getElementById('bounding-box');
      const typingText = document.getElementById('typing-text');
      const pagodaIcon = document.getElementById('pagoda-icon');
      const pagodaDock = document.getElementById('pagoda-dock');
      const btnReset = document.getElementById('btn-reset');
      
      let isDragging = false;
      let startX, startY, initialX, initialY;
      let isScanning = false;

      function resetSimulator() {
        isScanning = false;
        simMain.className = 'sim-container';
        cameraView.style.opacity = '1';
        guideUi.classList.remove('active');
        boundingBox.style.display = 'none';
        typingText.style.animation = 'none';
        typingText.innerText = '';
        
        pagodaIcon.style.opacity = '1';
        pagodaIcon.style.transition = 'none';
        
        const dockRect = pagodaDock.getBoundingClientRect();
        const simRect = simMain.getBoundingClientRect();
        pagodaIcon.style.left = (dockRect.left - simRect.left) + 'px';
        pagodaIcon.style.top = (dockRect.top - simRect.top) + 'px';
      }

      setTimeout(resetSimulator, 100);
      btnReset.addEventListener('click', resetSimulator);

      pagodaIcon.addEventListener('mousedown', dragStart);
      pagodaIcon.addEventListener('touchstart', dragStart, {passive: false});

      function dragStart(e) {
        if(isScanning) return;
        const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
        const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
        
        initialX = pagodaIcon.offsetLeft;
        initialY = pagodaIcon.offsetTop;
        startX = clientX;
        startY = clientY;
        isDragging = true;
        pagodaIcon.style.transition = 'none';
        
        document.addEventListener('mousemove', drag);
        document.addEventListener('mouseup', dragEnd);
        document.addEventListener('touchmove', drag, {passive: false});
        document.addEventListener('touchend', dragEnd);
      }

      function drag(e) {
        if (!isDragging) return;
        e.preventDefault();
        const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
        const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
        const dx = clientX - startX;
        const dy = clientY - startY;
        pagodaIcon.style.left = (initialX + dx) + 'px';
        pagodaIcon.style.top = (initialY + dy) + 'px';
      }

      function dragEnd(e) {
        isDragging = false;
        document.removeEventListener('mousemove', drag);
        document.removeEventListener('mouseup', dragEnd);
        document.removeEventListener('touchmove', drag);
        document.removeEventListener('touchend', dragEnd);
        
        // Check if dropped near the center of the phone
        const iconRect = pagodaIcon.getBoundingClientRect();
        const simRect = simMain.getBoundingClientRect();
        
        const iconCx = iconRect.left + iconRect.width/2;
        const iconCy = iconRect.top + iconRect.height/2;
        const simCx = simRect.left + simRect.width/2;
        const simCy = simRect.top + simRect.height/2;
        
        const dist = Math.sqrt(Math.pow(iconCx - simCx, 2) + Math.pow(iconCy - simCy, 2));
        
        if (dist < 150) {
          startScan();
        } else {
          // Snap back
          pagodaIcon.style.transition = 'all 0.3s';
          const dockRect = pagodaDock.getBoundingClientRect();
          pagodaIcon.style.left = (dockRect.left - simRect.left) + 'px';
          pagodaIcon.style.top = (dockRect.top - simRect.top) + 'px';
        }
      }

      function startScan() {
        isScanning = true;
        pagodaIcon.style.transition = 'all 0.3s';
        pagodaIcon.style.opacity = '0'; // Hide dragged icon
        
        // Stage 2: Scanning
        simMain.className = 'sim-container scanning';
        boundingBox.style.display = 'block';
        typingText.innerText = '[Object: Mireuksaji Seoktap / Confidence: 98%]';
        typingText.style.animation = 'typeText 1.5s steps(40, end) forwards, blinkCursor 0.5s step-end infinite alternate';
        
        // Stage 3: Load Guide UI after scan
        setTimeout(() => {
          simMain.className = 'sim-container'; // Back to STABLE Green
          cameraView.style.opacity = '0';
          guideUi.classList.add('active');
        }, 1800);
      }

    });
  </script>

  <!-- 2. 소개 탭 콘텐츠 -->
  <div id="tab-intro" class="tab-content" markdown="1">

## 프로젝트 개요
(여기에 프로젝트 개요 내용을 입력해주세요)

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

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
  .sim-container.warning { border-color: #f59e0b; box-shadow: 0 0 20px rgba(245, 158, 11, 0.4); }
  .sim-container.emergency { border-color: #ef4444; box-shadow: 0 0 30px rgba(239, 68, 68, 0.6); animation: flashRed 0.8s infinite alternate; }
  @keyframes flashRed { from { box-shadow: 0 0 10px #ef4444; } to { box-shadow: 0 0 50px #ef4444, inset 0 0 30px #ef4444; } }
  
  .sim-app {
    flex: 1; border-right: 2px dashed #334155; padding: 20px;
    display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative;
  }
  
  /* 스마트폰 앱 UI 스타일 (아이폰 모티브) */
  .sim-app-ui {
    width: 280px; height: 550px; background: #1e293b; 
    border-radius: 35px; border: 8px solid #0f172a;
    padding: 40px 15px 20px 15px; position: relative; overflow: hidden; font-family: 'Pretendard', sans-serif;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6), inset 0 0 5px rgba(255,255,255,0.1);
  }
  /* 노치 (Dynamic Island 느낌) */
  .sim-app-ui::before {
    content: ''; position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
    width: 80px; height: 20px; background: #0f172a; border-radius: 10px; z-index: 20;
  }
  /* 하단 홈 인디케이터 */
  .sim-app-ui::after {
    content: ''; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%);
    width: 100px; height: 4px; background: rgba(255,255,255,0.3); border-radius: 4px; z-index: 20;
  }

  .app-badge {
    background: #10b981; color: white; padding: 8px 12px; border-radius: 20px; font-weight: bold; text-align: center; margin-bottom: 20px; font-size: 1.1rem; letter-spacing: 1px; transition: background 0.3s;
  }
  
  .worker-status-card {
    background: rgba(0,0,0,0.2); border-radius: 12px; padding: 12px; margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.05);
  }
  .worker-name { color: #cbd5e1; font-weight: bold; margin-bottom: 10px; font-size: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 5px; }
  
  .app-item { padding: 8px 10px; border-radius: 6px; margin-bottom: 8px; color: #10b981; font-weight: bold; display: flex; justify-content: space-between; font-size: 0.95rem; transition: all 0.3s; background: rgba(16,185,129,0.1); }
  .app-item.off { color: #ef4444; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); }
  
  .app-emergency-popup {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(239, 68, 68, 0.95);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: white; font-weight: bold; text-align: center; padding: 20px; display: none; z-index: 30;
    backdrop-filter: blur(5px);
  }
  
  /* 2인 작업자 영역 */
  .sim-workers-area {
    flex: 1.5; position: relative; display: flex; align-items: center; justify-content: space-around;
    background: radial-gradient(circle at center, rgba(16,185,129,0.05) 0%, transparent 70%);
  }
  .worker-wrapper { position: relative; width: 120px; height: 300px; display: flex; justify-content: center; align-items: flex-end; }
  
  .worker-body {
    width: 80px; height: 140px; background: #334155; border-radius: 40px 40px 10px 10px; position: absolute; bottom: 50px; transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55); z-index: 5;
    display: flex; justify-content: center;
  }
  .worker-body.fallen { transform: rotate(90deg) translate(30px, 40px); }
  .worker-name-tag { position: absolute; bottom: -25px; color: #94a3b8; font-weight: bold; font-size: 0.9rem; }
  
  .timeout-text {
    position: absolute; top: -100px; color: #ef4444; font-weight: bold; font-size: 1.5rem; display: none; width: 300px; text-align: center; left: -110px; text-shadow: 0 0 10px rgba(239,68,68,0.5); z-index: 50; pointer-events: none;
  }
  
  .drag-item {
    width: 60px; height: 60px; position: absolute; cursor: grab; z-index: 20; user-select: none;
    display: flex; align-items: center; justify-content: center; font-size: 2.5rem;
    background: rgba(255,255,255,0.05); border-radius: 50%; border: 2px dashed rgba(255,255,255,0.2);
    transition: transform 0.1s;
  }
  .drag-item:active { cursor: grabbing; border-color: #38bdf8; transform: scale(1.1); background: rgba(56, 189, 248, 0.1); }
</style>

  <!-- 체험 시뮬레이터 탭 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container" id="sim-main">
      <div class="sim-app">
        <div class="sim-app-ui">
          <div class="app-badge" id="app-badge">STABLE</div>
          
          <div class="worker-status-card">
            <div class="worker-name">👷‍♂️ 작업자 A</div>
            <div class="app-item" id="app-helmet-1"><span>안전모:</span> <span>착용</span></div>
            <div class="app-item" id="app-vest-1"><span>안전조끼:</span> <span>착용</span></div>
          </div>
          
          <div class="worker-status-card">
            <div class="worker-name">👷‍♀️ 작업자 B</div>
            <div class="app-item" id="app-helmet-2"><span>안전모:</span> <span>착용</span></div>
            <div class="app-item" id="app-vest-2"><span>안전조끼:</span> <span>착용</span></div>
          </div>
          
          <div class="app-emergency-popup" id="app-popup">
            <div style="font-size: 3.5rem; margin-bottom:15px; animation: pulse 1s infinite;">🚨</div>
            <div style="font-size: 1.2rem; line-height: 1.5;">위험 상황:<br>작업자 쓰러짐 감지!!<br>즉시 구조 바랍니다</div>
          </div>
        </div>
      </div>
      
      <div class="sim-workers-area" id="sim-area">
        <div class="timeout-text" id="timeout-text">움직임 미감지: 3</div>
        
        <div class="worker-wrapper" id="wrapper-1">
          <div class="worker-body" id="worker-body-1">
            <div class="worker-name-tag">작업자 A</div>
          </div>
          <div class="drag-item" id="helmet-1" title="안전모">🪖</div>
          <div class="drag-item" id="vest-1" title="안전조끼">🦺</div>
        </div>

        <div class="worker-wrapper" id="wrapper-2">
          <div class="worker-body" id="worker-body-2">
            <div class="worker-name-tag">작업자 B</div>
          </div>
          <div class="drag-item" id="helmet-2" title="안전모">👷</div>
          <div class="drag-item" id="vest-2" title="안전조끼">🦺</div>
        </div>
      </div>
    </div>
    <p style="text-align:center; color:#94a3b8; font-size:0.95rem;">💡 마우스로 두 작업자의 안전모와 조끼를 밖으로 드래그하여 상태 변화를 체험해보세요.</p>
  </div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Tab Navigation Logic Update
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      document.getElementById(btn.getAttribute('data-target')).classList.add('active');
      
      if (btn.getAttribute('data-target') === 'tab-simulator') {
        initPos();
        resetTimer();
      }
    });
  });

  // Simulator Logic
  const simMain = document.getElementById('sim-main');
  const appBadge = document.getElementById('app-badge');
  const appPopup = document.getElementById('app-popup');
  const timeoutText = document.getElementById('timeout-text');
  const simArea = document.getElementById('sim-area');
  
  // Worker 1 elements
  const body1 = document.getElementById('worker-body-1');
  const helmet1 = document.getElementById('helmet-1');
  const vest1 = document.getElementById('vest-1');
  const appHelmet1 = document.getElementById('app-helmet-1');
  const appVest1 = document.getElementById('app-vest-1');
  
  // Worker 2 elements
  const body2 = document.getElementById('worker-body-2');
  const helmet2 = document.getElementById('helmet-2');
  const vest2 = document.getElementById('vest-2');
  const appHelmet2 = document.getElementById('app-helmet-2');
  const appVest2 = document.getElementById('app-vest-2');

  let state = 'STABLE'; // STABLE, WARNING, EMERGENCY
  let timerWait, timerInterval;
  let countdown = 3;
  
  // State variables for items
  const gearState = { h1: true, v1: true, h2: true, v2: true };

  function initPos() {
    // Snap everyone to upright
    snapGear(helmet1, body1, 'helmet');
    snapGear(vest1, body1, 'vest');
    snapGear(helmet2, body2, 'helmet');
    snapGear(vest2, body2, 'vest');
    gearState.h1 = gearState.v1 = gearState.h2 = gearState.v2 = true;
  }

  function snapGear(el, body, type) {
    // Local coords relative to wrapper
    const wrapper = body.parentElement;
    if(type === 'helmet') {
      el.style.left = (wrapper.offsetWidth/2 - 30) + 'px';
      el.style.top = (body.offsetTop - 40) + 'px';
    } else {
      el.style.left = (wrapper.offsetWidth/2 - 30) + 'px';
      el.style.top = (body.offsetTop + 40) + 'px';
    }
  }

  // Initial call
  setTimeout(initPos, 100);

  function resetTimer() {
    if (state === 'EMERGENCY') return; 
    
    clearInterval(timerInterval);
    clearTimeout(timerWait);
    timeoutText.style.display = 'none';
    countdown = 3;
    
    timerWait = setTimeout(startCountdown, 3000);
  }

  function startCountdown() {
    if(state === 'STABLE' || state === 'EMERGENCY') return;
    
    timeoutText.style.display = 'block';
    timeoutText.innerText = `움직임 미감지: 3`;
    
    timerInterval = setInterval(() => {
      countdown--;
      timeoutText.innerText = `움직임 미감지: ${countdown}`;
      if (countdown <= 0) {
        clearInterval(timerInterval);
        triggerEmergency();
      }
    }, 1000);
  }

  function triggerEmergency() {
    state = 'EMERGENCY';
    timeoutText.innerText = "🚨 시스템 다운 🚨";
    body1.classList.add('fallen');
    body2.classList.add('fallen');
    simMain.className = 'sim-container emergency';
    appBadge.innerText = 'EMERGENCY';
    appBadge.style.background = '#ef4444';
    appPopup.style.display = 'flex';
  }

  function updateState() {
    const allGood = gearState.h1 && gearState.v1 && gearState.h2 && gearState.v2;
    
    // If all gears are put back on during EMERGENCY, reset to STABLE
    if (state === 'EMERGENCY' && allGood) {
      state = 'STABLE';
      body1.classList.remove('fallen');
      body2.classList.remove('fallen');
      appPopup.style.display = 'none';
      resetTimer();
    } else if (state === 'EMERGENCY') {
      return; 
    }
    
    if (allGood) {
      state = 'STABLE';
      simMain.className = 'sim-container';
      appBadge.innerText = 'STABLE';
      appBadge.style.background = '#10b981';
    } else {
      state = 'WARNING';
      simMain.className = 'sim-container warning';
      appBadge.innerText = 'WARNING';
      appBadge.style.background = '#f59e0b';
    }
    
    // Update UI for Worker 1
    appHelmet1.innerHTML = `<span>안전모:</span> <span>${gearState.h1 ? '착용' : '미착용!⚠️'}</span>`;
    appHelmet1.className = gearState.h1 ? 'app-item' : 'app-item off';
    appVest1.innerHTML = `<span>안전조끼:</span> <span>${gearState.v1 ? '착용' : '미착용!⚠️'}</span>`;
    appVest1.className = gearState.v1 ? 'app-item' : 'app-item off';

    // Update UI for Worker 2
    appHelmet2.innerHTML = `<span>안전모:</span> <span>${gearState.h2 ? '착용' : '미착용!⚠️'}</span>`;
    appHelmet2.className = gearState.h2 ? 'app-item' : 'app-item off';
    appVest2.innerHTML = `<span>안전조끼:</span> <span>${gearState.v2 ? '착용' : '미착용!⚠️'}</span>`;
    appVest2.className = gearState.v2 ? 'app-item' : 'app-item off';
  }

  // Click worker to stand up and reset all
  const resetAll = () => {
    if (state === 'EMERGENCY') {
      state = 'STABLE';
      body1.classList.remove('fallen');
      body2.classList.remove('fallen');
      appPopup.style.display = 'none';
      initPos();
      updateState();
      resetTimer();
    }
  };
  body1.addEventListener('click', resetAll);
  body2.addEventListener('click', resetAll);

  // Drag logic
  function setupDrag(el, body, type, key) {
    let isDragging = false;
    let initialX, initialY, startX, startY;
    
    el.addEventListener('mousedown', dragStart);
    el.addEventListener('touchstart', dragStart, {passive: false});
    
    function dragStart(e) {
      const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
      const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
      initialX = el.offsetLeft;
      initialY = el.offsetTop;
      startX = clientX;
      startY = clientY;
      isDragging = true;
      resetTimer(); 
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
      el.style.left = (initialX + dx) + 'px';
      el.style.top = (initialY + dy) + 'px';
      resetTimer(); 
    }
    
    function dragEnd(e) {
      isDragging = false;
      document.removeEventListener('mousemove', drag);
      document.removeEventListener('mouseup', dragEnd);
      document.removeEventListener('touchmove', drag);
      document.removeEventListener('touchend', dragEnd);
      
      const rect = el.getBoundingClientRect();
      const bodyRect = body.getBoundingClientRect();
      const centerX = rect.left + rect.width/2;
      const centerY = rect.top + rect.height/2;
      const bodyCX = bodyRect.left + bodyRect.width/2;
      
      let snapped = false;
      
      if (Math.abs(centerX - bodyCX) < 70) {
        if (type === 'helmet' && Math.abs(centerY - bodyRect.top) < 60) {
          snapGear(el, body, 'helmet');
          snapped = true;
          gearState[key] = true;
        }
        else if (type === 'vest' && Math.abs(centerY - (bodyRect.top + bodyRect.height/2)) < 70) {
          snapGear(el, body, 'vest');
          snapped = true;
          gearState[key] = true;
        }
      }
      
      if (!snapped) gearState[key] = false;
      updateState();
    }
  }

  setupDrag(helmet1, body1, 'helmet', 'h1');
  setupDrag(vest1, body1, 'vest', 'v1');
  setupDrag(helmet2, body2, 'helmet', 'h2');
  setupDrag(vest2, body2, 'vest', 'v2');
  
  simArea.addEventListener('mousemove', () => { if(state !== 'EMERGENCY') resetTimer(); });
});
</script>

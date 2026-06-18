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
  /* 슬라이드 뷰어(PDF Slider) 스타일 */
  .pdf-slider-relative-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
  }
  .pdf-slide {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    opacity: 0;
    transition: opacity 0.4s ease-in-out;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #1e293b;
    z-index: 1;
  }
  .pdf-slide.active {
    opacity: 1;
    z-index: 2;
  }
  .pdf-slide img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }
  .pdf-btn-side {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(16, 185, 129, 0.5);
    color: #ffffff;
    border: none;
    font-size: 1.8rem;
    font-weight: bold;
    width: 42px;
    height: 76px;
    cursor: pointer;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    border-radius: 8px;
  }
  .pdf-btn-side:hover {
    background: rgba(16, 185, 129, 0.85);
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
  }
  .pdf-btn-side.prev {
    left: 15px;
  }
  .pdf-btn-side.next {
    right: 15px;
  }
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

  /* HW Control Panel Styles */
  .hw-control-panel {
    background: #0f172a; border: 2px solid #334155; border-radius: 8px; padding: 15px; margin-top: 20px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.5); width: 100%; box-sizing: border-box;
  }
  .hw-panel-header {
    display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;
  }
  .hw-title { color: #cbd5e1; font-weight: bold; font-size: 0.9rem; }
  .hw-com { color: #10b981; font-size: 0.8rem; font-weight: bold; }
  
  .hw-buttons { display: flex; gap: 10px; margin-bottom: 15px; }
  .btn-estop {
    flex: 2; background: #ef4444; color: white; font-weight: 900; font-size: 1.2rem;
    border: 3px solid #7f1d1d; border-radius: 6px; padding: 15px 0; cursor: pointer;
    box-shadow: 0 4px 0 #7f1d1d, inset 0 2px 5px rgba(255,255,255,0.3); transition: all 0.1s;
  }
  .btn-estop:active { transform: translateY(4px); box-shadow: 0 0 0 #7f1d1d; }
  
  .btn-reset {
    flex: 1; background: #64748b; color: white; font-weight: bold; font-size: 0.9rem;
    border: 2px solid #334155; border-radius: 6px; cursor: pointer;
    box-shadow: 0 3px 0 #334155; transition: all 0.1s;
  }
  .btn-reset:active { transform: translateY(3px); box-shadow: 0 0 0 #334155; }
  
  /* Sensor Graph Canvas */
  .sensor-graph-container {
    background: #000; border: 2px solid #334155; border-radius: 4px; padding: 2px;
    height: 60px; width: 100%; position: relative; overflow: hidden; box-sizing: border-box;
  }
  .sensor-canvas { width: 100%; height: 100%; display: block; }
  .hw-error-log {
    color: #ef4444; font-family: monospace; font-size: 0.75rem; margin-top: 8px; text-align: center;
    min-height: 12px; display: none;
  }
  .hw-error-log.show { display: block; animation: flashLog 1s infinite alternate; }
  
  /* Reboot popup */
  .reboot-popup {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: white; font-size: 2rem; font-weight: bold; z-index: 100;
    opacity: 0; pointer-events: none; transition: opacity 0.3s;
  }
  .reboot-popup.show { opacity: 1; pointer-events: auto; }
  
  .sim-container.frozen { border-color: #f59e0b; box-shadow: 0 0 30px rgba(245, 158, 11, 0.6); }

</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-simulator">시뮬레이터</button>
    <button class="tab-btn" data-target="tab-overview">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">역할</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

  <!-- 1. 시뮬레이터 탭 콘텐츠 -->

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
  .app-badge.emergency { background: #ef4444; animation: badgePulse 0.5s infinite alternate; }
  @keyframes badgePulse { from { transform: scale(1); } to { transform: scale(1.1); } }
  
  .fire-icon-drag {
    width: 60px; height: 60px; font-size: 3rem; cursor: grab; user-select: none;
    transition: transform 0.1s; display: flex; align-items: center; justify-content: center;
    filter: drop-shadow(0 5px 15px rgba(239, 68, 68, 0.6)); position: relative; z-index: 50;
  }
  .fire-icon-drag:active { cursor: grabbing; transform: scale(1.1); }
  
  .sim-main-area {
    flex: 1; position: relative; background: #1e293b; overflow: hidden;
  }
  
  
  
  .lcd-bezel {
    width: 100%; padding: 12px; background: linear-gradient(145deg, #1e293b, #0f172a);
    border: 2px solid #334155; border-radius: 8px; margin-top: 30px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.5), inset 0 2px 5px rgba(255,255,255,0.1);
  }
  .lcd-display {
    width: 100%; height: 55px; background: #050505; border-radius: 4px;
    display: flex; align-items: center; justify-content: center; position: relative;
    font-family: 'Orbitron', 'Consolas', monospace; font-size: 1rem; font-weight: bold;
    color: #10b981; text-shadow: 0 0 10px #10b981, 0 0 20px #10b981; letter-spacing: 1px;
    box-shadow: inset 0 0 15px rgba(16,185,129,0.2), 0 0 5px rgba(0,0,0,0.8); overflow: hidden;
    white-space: nowrap; line-height: 1;
  }
  .lcd-display::after {
    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(0deg, rgba(0,0,0,0.3), rgba(0,0,0,0.3) 1px, transparent 1px, transparent 2px);
    pointer-events: none;
  }
  .lcd-display.danger {
    color: #ef4444; text-shadow: 0 0 10px #ef4444, 0 0 20px #ef4444; 
    box-shadow: inset 0 0 15px rgba(239,68,68,0.4); animation: blinkLcd 0.35s infinite alternate;
  }
  @keyframes blinkLcd { from { opacity: 1; } to { opacity: 0.4; } }

  /* 방재 관제 대시보드 */
  .dash-panel {
    width: 100%; margin-top: 15px; background: rgba(0,0,0,0.3); border-radius: 8px; padding: 15px;
    border: 1px solid rgba(255,255,255,0.1); font-family: 'Consolas', monospace; text-align: left;
  }
  .dash-item { color: #cbd5e1; font-size: 0.95rem; margin-bottom: 10px; display: flex; justify-content: space-between; }
  .dash-item span { font-weight: bold; color: #10b981; }
  .dash-item span.danger { color: #ef4444; animation: blinkRed 0.5s infinite alternate; }
  @keyframes blinkRed { from { opacity: 1; } to { opacity: 0.5; } }
  
  .dash-console {
    background: #000; color: #10b981; padding: 10px; border-radius: 6px; font-size: 0.8rem;
    height: 100px; overflow-y: auto; scrollbar-width: none; line-height: 1.4; border: 1px solid #334155;
  }
  
  .future-notice {
    font-size: 0.75rem; color: #94a3b8; border: 1px dashed #475569; padding: 8px; margin-top: 15px; border-radius: 5px; text-align: center; line-height: 1.3;
  }

  /* 평면도 SVG 스타일 */
  .blueprint-svg {
    width: 100%; height: 100%; display: block;
  }
  
  /* 방 바닥 및 벽면 LED 스타일 */
  .zone-bg {
    fill: #334155; transition: fill 0.3s;
  }
  .zone-bg.fire { fill: rgba(239, 68, 68, 0.4); }
  
  .wall-led {
    fill: none; stroke: rgba(16, 185, 129, 0.6); stroke-width: 8; stroke-dasharray: 10 10;
    filter: drop-shadow(0 0 5px rgba(16, 185, 129, 0.8)); transition: all 0.3s;
    pointer-events: none;
  }
  .wall-led.fire {
    stroke: rgba(239, 68, 68, 0.9); filter: drop-shadow(0 0 10px rgba(239, 68, 68, 1));
  }
  
    /* 연기 확산 효과 */
  .smoke-cloud {
    fill: rgba(15, 23, 42, 0.85); filter: blur(20px);
    transition: r 5s ease-out, opacity 1s;
    opacity: 0; pointer-events: none;
  }
  .smoke-cloud.active {
    opacity: 1; r: 350;
  }

  /* 파란색 파도타기 대피 유도선 */
  .route-path {
    fill: none; stroke: #38bdf8; stroke-width: 10; stroke-linecap: round; stroke-linejoin: round;
    stroke-dasharray: 30 20; filter: drop-shadow(0 0 10px #38bdf8);
    opacity: 0; transition: opacity 0.3s; pointer-events: none;
  }
  .route-path.active {
    opacity: 1; animation: flowWave 0.5s linear infinite;
  }
  @keyframes flowWave { from { stroke-dashoffset: 50; } to { stroke-dashoffset: 0; } }
  /* 방마다 살짝 다른 톤으로 구분감 */
  .route-path-2 { stroke: #67e8f9; filter: drop-shadow(0 0 10px #67e8f9); animation-delay: 0.1s; }
  .route-path-3 { stroke: #7dd3fc; filter: drop-shadow(0 0 10px #7dd3fc); animation-delay: 0.2s; }
  .route-path-4 { stroke: #a5f3fc; filter: drop-shadow(0 0 10px #a5f3fc); animation-delay: 0.3s; }
  .route-path-5 { stroke: #38bdf8; filter: drop-shadow(0 0 12px #38bdf8); stroke-width: 12; }
  .route-path-6 { stroke: #06b6d4; filter: drop-shadow(0 0 10px #06b6d4); animation-delay: 0.05s; }
  
  /* 텍스트 라벨 */
  .zone-label {
    fill: #cbd5e1; font-family: 'Pretendard', sans-serif; font-size: 24px; font-weight: bold;
    text-anchor: middle; dominant-baseline: middle; pointer-events: none;
  }
  
  /* 드롭존 오버레이 (보이지 않지만 드래그 이벤트를 받음) */
  .dropzone {
    fill: transparent; cursor: pointer;
  }
  .dropzone:hover { fill: rgba(255,255,255,0.05); }

</style>

  <!-- 체험 시뮬레이터 탭 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container" id="sim-main-fire">
      
      <div class="sim-sidebar">
        <div class="app-badge" id="app-badge-fire">ALL STABLE</div>
        <p style="color: #94a3b8; font-size: 0.9rem; text-align: center; margin-bottom: 40px; line-height: 1.5;">
          우측 평면도에<br>🔥 아이콘을 드래그하여<br>화재를 발생시켜 보세요.
        </p>
        <div class="fire-icon-drag" id="fire-drag" title="드래그 앤 드롭!">🔥</div>
          <div class="lcd-bezel">
            <div style="font-size: 0.65rem; color: #64748b; margin-bottom: 5px; text-align: left; font-family: 'Orbitron', sans-serif; letter-spacing: 1px;">► FIRE DETECTOR</div>
            <div class="lcd-display" id="lcd-display">ZONE: SAFE</div>
          </div>
      </div>
      
      <div class="sim-main-area" id="sim-area-fire">
        <!-- 마스터 규격 평면도 SVG (1000x600 비율) -->
        <svg class="blueprint-svg" viewBox="0 0 1000 600" preserveAspectRatio="xMidYMid meet">
          <!-- 1. 배경 영역 (바닥) -->
          <!-- 방 -->
          <rect x="20" y="80" width="120" height="100" class="zone-bg" id="bg-r1" />
          <rect x="860" y="80" width="120" height="100" class="zone-bg" id="bg-r2" />
          <rect x="20" y="420" width="120" height="100" class="zone-bg" id="bg-r3" />
          <rect x="860" y="420" width="120" height="100" class="zone-bg" id="bg-r4" />
          <rect x="350" y="190" width="300" height="100" class="zone-bg" id="bg-r5" />
          <rect x="350" y="310" width="300" height="100" class="zone-bg" id="bg-r6" />
          
          <!-- 복도 -->
          <rect x="140" y="100" width="60" height="400" class="zone-bg" id="bg-c-left" />
          <rect x="800" y="100" width="60" height="400" class="zone-bg" id="bg-c-right" />
          <rect x="200" y="100" width="300" height="60" class="zone-bg" id="bg-c-top-l" />
          <rect x="500" y="100" width="300" height="60" class="zone-bg" id="bg-c-top-r" />
          <rect x="200" y="440" width="300" height="60" class="zone-bg" id="bg-c-bot-l" />
          <rect x="500" y="440" width="300" height="60" class="zone-bg" id="bg-c-bot-r" />
          
          <!-- 2. 대피 유도선 (Dijkstra Path) - 방마다 개별 경로 -->
          <path d="" class="route-path" id="route-r1" />
          <path d="" class="route-path route-path-2" id="route-r2" />
          <path d="" class="route-path route-path-3" id="route-r3" />
          <path d="" class="route-path route-path-4" id="route-r4" />
          <path d="" class="route-path route-path-5" id="route-r5" />
          <path d="" class="route-path route-path-6" id="route-r6" />
          <path d="" class="route-path" id="route-dynamic" />


          <!-- 3. 벽면 LED 스트립 -->
          <rect x="20" y="80" width="120" height="100" class="wall-led" id="wall-r1" />
          <rect x="860" y="80" width="120" height="100" class="wall-led" id="wall-r2" />
          <rect x="20" y="420" width="120" height="100" class="wall-led" id="wall-r3" />
          <rect x="860" y="420" width="120" height="100" class="wall-led" id="wall-r4" />
          <rect x="350" y="190" width="300" height="100" class="wall-led" id="wall-r5" />
          <rect x="350" y="310" width="300" height="100" class="wall-led" id="wall-r6" />
          
          <rect x="140" y="100" width="60" height="400" class="wall-led" id="wall-c-left" />
          <rect x="800" y="100" width="60" height="400" class="wall-led" id="wall-c-right" />
          <rect x="200" y="100" width="300" height="60" class="wall-led" id="wall-c-top-l" />
          <rect x="500" y="100" width="300" height="60" class="wall-led" id="wall-c-top-r" />
          <rect x="200" y="440" width="300" height="60" class="wall-led" id="wall-c-bot-l" />
          <rect x="500" y="440" width="300" height="60" class="wall-led" id="wall-c-bot-r" />
          
          <!-- 4. 텍스트 라벨 -->
          <text x="80" y="130" class="zone-label" font-size="16">Room 1</text>
          <text x="920" y="130" class="zone-label" font-size="16">Room 2</text>
          <text x="80" y="470" class="zone-label" font-size="16">Room 3</text>
          <text x="920" y="470" class="zone-label" font-size="16">Room 4</text>
          <text x="500" y="240" class="zone-label" font-size="20">Room 5 (Main)</text>
          <text x="500" y="360" class="zone-label" font-size="20">Room 6 (Sub)</text>
          
          <text x="170" y="300" class="zone-label" font-size="12" transform="rotate(-90 170 300)">Left Corridor</text>
          <text x="830" y="300" class="zone-label" font-size="12" transform="rotate(-90 830 300)">Right Corridor</text>
          <text x="350" y="130" class="zone-label" font-size="14">Top-L Corridor</text>
          <text x="650" y="130" class="zone-label" font-size="14">Top-R Corridor</text>
          <text x="350" y="470" class="zone-label" font-size="14">Bot-L Corridor</text>
          <text x="650" y="470" class="zone-label" font-size="14">Bot-R Corridor</text>
          
          <!-- Exit 1 & 2 표시 -->
          <rect x="140" y="50" width="60" height="50" fill="#10b981" />
          <text x="170" y="75" fill="#fff" font-family="'Pretendard', sans-serif" font-weight="bold" font-size="16" text-anchor="middle" dominant-baseline="middle" pointer-events="none">EXIT 1</text>
          
          <rect x="800" y="50" width="60" height="50" fill="#10b981" />
          <text x="830" y="75" fill="#fff" font-family="'Pretendard', sans-serif" font-weight="bold" font-size="16" text-anchor="middle" dominant-baseline="middle" pointer-events="none">EXIT 2</text>

          <!-- 5. 투명 드롭존 (마우스 이벤트용) -->
          <rect x="20" y="80" width="120" height="100" class="dropzone" data-zone="r1" />
          <rect x="860" y="80" width="120" height="100" class="dropzone" data-zone="r2" />
          <rect x="20" y="420" width="120" height="100" class="dropzone" data-zone="r3" />
          <rect x="860" y="420" width="120" height="100" class="dropzone" data-zone="r4" />
          <rect x="350" y="190" width="300" height="100" class="dropzone" data-zone="r5" />
          <rect x="350" y="310" width="300" height="100" class="dropzone" data-zone="r6" />
          
          <rect x="140" y="100" width="60" height="400" class="dropzone" data-zone="c-left" />
          <rect x="800" y="100" width="60" height="400" class="dropzone" data-zone="c-right" />
          <rect x="200" y="100" width="300" height="60" class="dropzone" data-zone="c-top-l" />
          <rect x="500" y="100" width="300" height="60" class="dropzone" data-zone="c-top-r" />
          <rect x="200" y="440" width="300" height="60" class="dropzone" data-zone="c-bot-l" />
          <rect x="500" y="440" width="300" height="60" class="dropzone" data-zone="c-bot-r" />
          <rect x="140" y="50" width="60" height="50" class="dropzone" data-zone="e1" />
          <rect x="800" y="50" width="60" height="50" class="dropzone" data-zone="e2" />
        
          <!-- 6. 대피자 애니메이션 (SVG) -->
          <g id="evacuee-group" style="display: none;">
            <circle cx="0" cy="0" r="18" fill="#fcd34d" filter="drop-shadow(0 0 5px #f59e0b)" />
            <text x="0" y="2" font-size="20" text-anchor="middle" dominant-baseline="middle">🏃</text>
            <animateMotion id="evacuee-motion" dur="3s" fill="freeze" path="" />
          </g>
          
          <!-- 7. 연기 확산 그래픽 -->
          <circle id="smoke-effect" class="smoke-cloud" cx="500" cy="300" r="0" />
        </svg>
      </div>
      
      <div class="reboot-popup" id="reboot-popup-b">Rebooting...</div>
    </div>
    <p style="text-align:center; color:#94a3b8; font-size:0.95rem;">💡 화재 위치가 변경되면 실시간으로 화재를 우회하는 다익스트라 최단 경로가 재계산되어 대피 유도선이 바뀝니다.</p>
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
    });
  });

  // Simulator Elements
  const fireDrag = document.getElementById('fire-drag');
  const simMainFire = document.getElementById('sim-main-fire');
  const appBadgeFire = document.getElementById('app-badge-fire');
  const dropzones = document.querySelectorAll('.dropzone');
  
  let isDragging = false;
  let startX, startY, initialX, initialY;
  
  // Zones and Routes definition
  const zones = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'c-left', 'c-right', 'c-top-l', 'c-top-r', 'c-bot-l', 'c-bot-r', 'e1', 'e2'];
  
  // Dijkstra Graph Definition
  const graph = {
    n1: { e1: 80, n3: 340, nt: 330 },
    n2: { e2: 80, n4: 340, nt: 330 },
    n3: { n1: 340, nb: 330 },
    n4: { n2: 340, nb: 330 },
    nt: { n1: 330, n2: 330 },
    nb: { n3: 330, n4: 330 },
    e1: { n1: 80 },
    e2: { n2: 80 }
  };

  const roomNodes = { r1: 'n1', r2: 'n2', r3: 'n3', r4: 'n4', r5: 'nt', r6: 'nb' };
  const roomCoords = { r1: [80, 130], r2: [920, 130], r3: [80, 470], r4: [920, 470], r5: [500, 240], r6: [500, 360] };
  const nodeCoords = {
    n1: [170, 130], n2: [830, 130], n3: [170, 470], n4: [830, 470],
    nt: [500, 130], nb: [500, 470], e1: [170, 50], e2: [830, 50]
  };

  const fireEdges = {
    'c-left': [['n1', 'n3']],
    'c-right': [['n2', 'n4']],
    'c-top-l': [['n1', 'nt']],
    'c-top-r': [['nt', 'n2']],
    'c-bot-l': [['n3', 'nb']],
    'c-bot-r': [['nb', 'n4']],
    'e1': [['n1', 'e1']],
    'e2': [['n2', 'e2']]
  };

  function findShortestPath(startRoom, fireZoneId) {
    let g = JSON.parse(JSON.stringify(graph));
    if (fireZoneId && fireEdges[fireZoneId]) {
      fireEdges[fireZoneId].forEach(edge => {
        if(g[edge[0]] && g[edge[0]][edge[1]]) delete g[edge[0]][edge[1]];
        if(g[edge[1]] && g[edge[1]][edge[0]]) delete g[edge[1]][edge[0]];
      });
    }
    
    let startNode = roomNodes[startRoom];
    if (fireZoneId === startRoom) return null; // Trapped in room
    
    let distances = {};
    let prev = {};
    let pq = [{node: startNode, dist: 0}];
    
    Object.keys(g).forEach(n => distances[n] = Infinity);
    distances[startNode] = 0;
    
    while(pq.length > 0) {
      pq.sort((a,b) => a.dist - b.dist);
      let curr = pq.shift();
      
      if (curr.node === 'e1' || curr.node === 'e2') break;
      
      for (let neighbor in g[curr.node]) {
        let alt = distances[curr.node] + g[curr.node][neighbor];
        if (alt < distances[neighbor]) {
          distances[neighbor] = alt;
          prev[neighbor] = curr.node;
          pq.push({node: neighbor, dist: alt});
        }
      }
    }
    
    let bestExit = null;
    if (distances['e1'] < distances['e2']) bestExit = 'e1';
    else if (distances['e2'] < distances['e1']) bestExit = 'e2';
    else bestExit = 'e1';
    
    if (distances[bestExit] === Infinity) return null; // No path
    
    let path = [bestExit];
    let curr = bestExit;
    while(prev[curr]) {
      curr = prev[curr];
      path.unshift(curr);
    }
    return path;
  }

  function renderPathString(startRoom, pathNodes) {
    if(!pathNodes) return "";
    let pts = [roomCoords[startRoom]];
    pathNodes.forEach(n => pts.push(nodeCoords[n]));
    let d = `M ${pts[0][0]} ${pts[0][1]} `;
    for(let i=1; i<pts.length; i++) {
      d += `L ${pts[i][0]} ${pts[i][1]} `;
    }
    return d;
  }


  
  const dashConsole = document.querySelector('.dash-console');
  // Wait! Let's just grab elements globally if they aren't declared:
  // (We'll assume they might be declared above, but let's safely declare them)
  const dashTemp = document.getElementById('dash-temp');
  const dashStatus = document.getElementById('dash-status');
  const evacueeGroup = document.getElementById('evacuee-group');
  const evacueeMotion = document.getElementById('evacuee-motion');
  const smokeEffect = document.getElementById('smoke-effect');
  const routeDynamic = document.getElementById('route-dynamic');

  let tempInterval = null;
  let currentTemp = 24;
  let smokeTimeout = null;

  function appendLog(msg) {
    if(dashConsole) {
      dashConsole.innerHTML += `> ${msg}<br>`;
      dashConsole.scrollTop = dashConsole.scrollHeight;
    }
  }

  function triggerFire(zoneId) {
    if(typeof isFrozenB !== 'undefined' && isFrozenB) return;
    resetAll();
    
    const bg = document.getElementById('bg-' + zoneId);
    const wall = document.getElementById('wall-' + zoneId);
    if(bg) bg.classList.add('fire');
    if(wall) wall.classList.add('fire');
    
    if(simMainFire) simMainFire.classList.add('emergency');
    if(appBadgeFire) {
      appBadgeFire.innerText = 'EMERGENCY';
      appBadgeFire.classList.add('emergency');
    }
    
    const lcd = document.getElementById('lcd-display');
    if(lcd) {
      lcd.innerText = `FIRE DETECTED: ${zoneId.toUpperCase()}`;
      lcd.classList.add('danger');
    }
    
    if(dashStatus) {
      dashStatus.innerHTML = '<span class="danger">화재 발생 (경계경보)</span>';
    }
    
    currentTemp = 24;
    tempInterval = setInterval(() => {
      if(typeof isFrozenB !== 'undefined' && isFrozenB) return;
      currentTemp += Math.floor(Math.random() * 5) + 2;
      if(dashTemp) {
        dashTemp.innerText = currentTemp + '°C';
        if(currentTemp > 50) dashTemp.classList.add('danger');
      }
    }, 1000);

    if(smokeEffect && bg) {
      const zoneRect = bg.getBoundingClientRect();
      const svgRect = document.querySelector('.blueprint-svg').getBoundingClientRect();
      // Use relative SVG coords by dividing by scale, or just approximate.
      // Wait, bounding client rect can be tricky with preservesAspectRatio.
      // Better to extract x,y from the rect element itself:
      const x = parseFloat(bg.getAttribute('x'));
      const y = parseFloat(bg.getAttribute('y'));
      const w = parseFloat(bg.getAttribute('width'));
      const h = parseFloat(bg.getAttribute('height'));
      smokeEffect.setAttribute('cx', x + w/2);
      smokeEffect.setAttribute('cy', y + h/2);
      smokeEffect.classList.add('active');
    }
    
    appendLog(`[경보] ${zoneId.toUpperCase()} 구역 화재 감지! 센서 가동 중...`);
    
    setTimeout(() => {
      if(typeof isFrozenB !== 'undefined' && isFrozenB) return;
      appendLog("[시스템] 모든 구역 다익스트라 최적 경로 병렬 탐색 시작...");

      // 화재가 발생한 구역을 제외한 모든 방에서 경로 계산
      const allRooms = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6'];
      let pathCount = 0;
      let blockedCount = 0;

      // 기존 route-dynamic 초기화
      if(routeDynamic) { routeDynamic.setAttribute('d', ''); routeDynamic.classList.remove('active'); }

      // 방마다 개별 경로 SVG 요소에 그리기
      allRooms.forEach((room, idx) => {
        setTimeout(() => {
          if(typeof isFrozenB !== 'undefined' && isFrozenB) return;
          if(room === zoneId) {
            // 화재 구역 - 탈출 불가
            const routeEl = document.getElementById('route-' + room);
            if(routeEl) { routeEl.setAttribute('d', ''); routeEl.classList.remove('active'); }
            blockedCount++;
            return;
          }

          let path = findShortestPath(room, zoneId);
          const routeEl = document.getElementById('route-' + room);

          if(!path || !routeEl) {
            blockedCount++;
            appendLog(`<span class='danger'>[${room.toUpperCase()}] 경고: 탈출 불가 구역!</span>`);
          } else {
            let d = renderPathString(room, path);
            routeEl.setAttribute('d', d);
            routeEl.classList.add('active');
            pathCount++;
            appendLog(`[${room.toUpperCase()}] 최적 경로: ${room} → ${path[path.length-1] === 'e1' ? 'EXIT 1' : 'EXIT 2'}`);
          }
        }, idx * 150); // 각 방 순차적으로 150ms 간격으로 켜지는 연출
      });

      // 대피자 애니메이션은 r5(중앙)에서만
      setTimeout(() => {
        if(typeof isFrozenB !== 'undefined' && isFrozenB) return;
        const mainPath = findShortestPath('r5', zoneId);
        if(mainPath && evacueeGroup && evacueeMotion) {
          let d = renderPathString('r5', mainPath);
          evacueeGroup.style.display = 'block';
          evacueeMotion.setAttribute('path', d);
          evacueeMotion.beginElement();
        }
        appendLog(`[완료] 총 ${allRooms.length - 1}개 구역 경로 계산 완료. 대피 유도 LED 활성화.`);
      }, allRooms.length * 150 + 200);

    }, 500);
  }

  function resetAll() {

    clearInterval(tempInterval);
    currentTemp = 24;
    if(dashTemp) dashTemp.innerText = currentTemp + '°C';
    if(dashTemp) dashTemp.className = '';
    const lcd = document.getElementById('lcd-display');
    if(lcd) { lcd.innerText = 'ZONE: SAFE'; lcd.className = 'lcd-display'; }

    if(dashStatus) dashStatus.innerText = '정상';
    if(dashStatus) dashStatus.className = '';
    
    if(evacueeGroup) evacueeGroup.style.display = 'none';
    clearTimeout(smokeTimeout);
    if(smokeEffect) {
      smokeEffect.classList.remove('active');
      smokeEffect.setAttribute('r', '0');
    }

    // 모든 방/복도 화재 상태 초기화
    zones.forEach(z => {
      const bg = document.getElementById('bg-' + z);
      if(bg) bg.classList.remove('fire');
      const wall = document.getElementById('wall-' + z);
      if(wall) wall.classList.remove('fire');
      // 복도 route 초기화
      const routeZone = document.getElementById('route-' + z);
      if(routeZone) { routeZone.setAttribute('d', ''); routeZone.classList.remove('active'); }
    });
    // 방별 개별 경로 초기화
    ['r1','r2','r3','r4','r5','r6'].forEach(r => {
      const routeEl = document.getElementById('route-' + r);
      if(routeEl) { routeEl.setAttribute('d', ''); routeEl.classList.remove('active'); }
    });
    if(routeDynamic) { routeDynamic.setAttribute('d', ''); routeDynamic.classList.remove('active'); }
    const wallMid = document.getElementById('wall-c-mid');
    if(wallMid) wallMid.classList.remove('fire');
    const bgMid = document.getElementById('bg-c-mid');
    if(bgMid) bgMid.classList.remove('fire');
    
    simMainFire.classList.remove('emergency');
    appBadgeFire.innerText = 'ALL STABLE';
    appBadgeFire.classList.remove('emergency');
  }

  fireDrag.addEventListener('mousedown', dragStart);
  fireDrag.addEventListener('touchstart', dragStart, {passive: false});

  function dragStart(e) {
    const clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
    const clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
    
    initialX = fireDrag.offsetLeft;
    initialY = fireDrag.offsetTop;
    startX = clientX;
    startY = clientY;
    isDragging = true;
    fireDrag.style.position = 'absolute';
    fireDrag.style.zIndex = '1000';
    
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
    
    fireDrag.style.left = (initialX + clientX - startX) + 'px';
    fireDrag.style.top = (initialY + clientY - startY) + 'px';
  }

  function dragEnd(e) {
    isDragging = false;
    document.removeEventListener('mousemove', drag);
    document.removeEventListener('mouseup', dragEnd);
    document.removeEventListener('touchmove', drag);
    document.removeEventListener('touchend', dragEnd);
    
    // 드롭 좌표 확인을 위한 임시 숨김 처리 (요소 밑의 dropzone 파악용)
    fireDrag.style.display = 'none';
    const clientX = e.type.includes('mouse') ? e.clientX : e.changedTouches[0].clientX;
    const clientY = e.type.includes('mouse') ? e.clientY : e.changedTouches[0].clientY;
    const elemBelow = document.elementFromPoint(clientX, clientY);
    fireDrag.style.display = 'flex';
    
    if (elemBelow && elemBelow.classList.contains('dropzone')) {
      const targetZone = elemBelow.getAttribute('data-zone');
      triggerFire(targetZone);
    } else {
      // 제자리 복귀
resetAll();
      fireDrag.style.position = 'relative';
      fireDrag.style.left = 'auto';
      fireDrag.style.top = 'auto';
    }
  }
});
</script>

  <!-- ===================== 한눈에 보기 탭 ===================== -->
  <!-- ===================== 한눈에 보기 탭 ===================== -->
  <div id="tab-overview" class="tab-content">
    <style>
      .ov-media-row { display:flex; gap:20px; margin-bottom:30px; align-items:flex-start; }
      .ov-media-row > * { flex:1; min-width:0; }
      @media(max-width:700px) { .ov-media-row { flex-direction:column; } }
      .ov-media-box {
        background:#0f172a; border:2px solid #334155; border-radius:12px;
        overflow:hidden; aspect-ratio:16/9;
        display:flex; align-items:center; justify-content:center;
        color:#475569; font-size:0.9rem; text-align:center; padding:20px;
        font-family:'Pretendard',sans-serif;
      }
      .ov-media-box video,.ov-media-box img { width:100%; height:100%; object-fit:cover; display:block; }
      .ov-media-label { text-align:center; color:#64748b; font-size:0.8rem; margin-top:8px; font-family:'Pretendard',sans-serif; }
    </style>

    <div style="padding:30px 0; font-family:'Pretendard',sans-serif;">

      <!-- PDF 슬라이더 (타이틀 제거, 캐러셀 방식) -->
      <div class="pdf-slider-wrap" style="background:#0f172a; border:2px solid #334155; border-radius:12px; padding:24px; margin-bottom:20px;">
        <div class="pdf-slider-relative-wrap">
          <div class="pdf-slider-container" id="pdf-slider-fire" style="position:relative; width:100%; height:100%; background:#1e293b; border-radius:8px; overflow:hidden;">
            <div class="pdf-slide active" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.4s ease; display:flex; align-items:center; justify-content:center; color:#475569; font-size:0.9rem; text-align:center; padding:20px; font-family:'Pretendard',sans-serif;">
              <div><div style="font-size:2.5rem;margin-bottom:10px;">📂</div><div style="color:#64748b;">로딩 중...</div></div>
            </div>
          </div>
          <button class="pdf-btn-side prev" id="pdf-fire-prev">&lt;</button>
          <button class="pdf-btn-side next" id="pdf-fire-next">&gt;</button>
        </div>
      </div>


      <!-- 영상/사진 좌우 배치 (슬라이드 밑으로 이동) -->
      <div class="ov-media-row">
        <div>
          <div class="ov-media-box">
            <!-- 영상: <video src="/assets/videos/fire_demo.mp4" controls></video> -->
            <div><div style="font-size:2.5rem;margin-bottom:10px;">🎬</div><div><strong style="color:#94a3b8;">시연 영상</strong><br><span style="color:#64748b;">video 태그로 교체해 주세요</span></div></div>
          </div>
          <p class="ov-media-label">📽️ 시스템 시연 영상</p>
        </div>
        <div>
          <div class="ov-media-box">
            <!-- 사진: <img src="/assets/images/fire_hw.jpg" alt="하드웨어"> -->
            <div><div style="font-size:2.5rem;margin-bottom:10px;">📸</div><div><strong style="color:#94a3b8;">하드웨어 사진</strong><br><span style="color:#64748b;">img 태그로 교체해 주세요</span></div></div>
          </div>
          <p class="ov-media-label">🔧 실제 하드웨어 구성</p>
        </div>
      </div>

    </div>
    </div>

  <!-- ===================== 소개 탭 ===================== -->
  <div id="tab-intro" class="tab-content">
    <style>
      .intro-section { margin-bottom:32px; }
      .intro-section-title { display:flex; align-items:center; gap:10px; color:#10b981; font-size:1.2rem; font-weight:700; border-bottom:2px solid rgba(16,185,129,0.2); padding-bottom:10px; margin-bottom:16px; font-family:'Pretendard',sans-serif; }
      .intro-row { display:flex; gap:12px; margin-bottom:10px; font-family:'Pretendard',sans-serif; }
      .intro-label { color:#94a3b8; font-size:0.9rem; min-width:110px; font-weight:600; padding-top:2px; }
      .intro-value { color:#e2e8f0; font-size:0.95rem; line-height:1.7; flex:1; }
      .intro-chip { display:inline-block; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); color:#10b981; border-radius:20px; padding:3px 12px; font-size:0.8rem; margin:3px 3px 3px 0; font-family:'Pretendard',sans-serif; }
      .intro-chip.blue { background:rgba(56,189,248,0.12); border-color:rgba(56,189,248,0.3); color:#38bdf8; }
      .intro-chip.purple { background:rgba(167,139,250,0.12); border-color:rgba(167,139,250,0.3); color:#a78bfa; }
      .intro-issue-box { background:rgba(15,23,42,0.6); border-left:3px solid #f59e0b; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:14px; font-family:'Pretendard',sans-serif; }
      .intro-issue-box .issue-title { color:#f59e0b; font-weight:700; font-size:0.95rem; margin-bottom:8px; }
      .intro-issue-box .issue-row { color:#94a3b8; font-size:0.88rem; margin-bottom:4px; line-height:1.6; }
      .intro-issue-box .issue-row strong { color:#cbd5e1; }
    </style>
    <div style="padding:30px 0; font-family:'Pretendard',sans-serif;">
      <div class="intro-section">
        <div class="intro-section-title">📌 프로젝트 개요</div>
        <div class="intro-row"><span class="intro-label">진행 기간</span><span class="intro-value"><!-- 예: 2024.03 ~ 2024.06 (팀 N명) --></span></div>
        <div class="intro-row"><span class="intro-label">기획 배경</span><span class="intro-value">화재 발생 시 고정형 비상구 안내 표시판으로 인해 작업자가 화재 방향으로 대피하는 오안내 문제를 해결하고자 기획되었습니다.</span></div>
        <div class="intro-row"><span class="intro-label">프로젝트 목적</span><span class="intro-value">화재 센서 로그 데이터를 기반으로 동적 대피 유도 LED 패널을 제어해 안전 대피 경로를 가이드하는 시스템을 구축합니다.</span></div>
      </div>
      <div class="intro-section">
        <div class="intro-section-title">🛠 사용 기술 및 개발 환경</div>
        <div class="intro-row"><span class="intro-label">언어</span><span class="intro-value"><span class="intro-chip">C/C++</span><span class="intro-chip">Python</span></span></div>
        <div class="intro-row"><span class="intro-label">하드웨어</span><span class="intro-value"><span class="intro-chip blue">ESP32</span><span class="intro-chip blue">Flame/Smoke Sensors</span><span class="intro-chip blue">LED Dot Matrix</span><span class="intro-chip blue">Buzzer</span></span></div>
        <div class="intro-row"><span class="intro-label">소프트웨어</span><span class="intro-value"><span class="intro-chip purple">VS Code</span><span class="intro-chip purple">PlatformIO</span><span class="intro-chip purple">Arduino IDE</span></span></div>
        <div class="intro-row"><span class="intro-label">통신 프로토콜</span><span class="intro-value">Wi-Fi / WebSockets, Serial, I2C</span></div>
      </div>
      <div class="intro-section">
        <div class="intro-section-title">⚡ 핵심 기능</div>
        <div class="intro-row"><span class="intro-label">기능 1</span><span class="intro-value">화재 감지 센서값에 가중치를 부여하여 실시간 위험 노드를 우회하는 최적 대피 경로 계산 알고리즘 (Dijkstra)</span></div>
        <div class="intro-row"><span class="intro-label">기능 2</span><span class="intro-value">계산된 경로 방향에 맞춰 대피 비상구 LED matrix 화살표 방향을 동적으로 스위칭하는 제어 구조</span></div>
      </div>
      <div class="intro-section">
        <div class="intro-section-title">🔧 개발 중 겪은 문제와 해결 과정</div>
        <div class="intro-issue-box">
          <div class="issue-title">⚠ Issue 1: 다중 노드 센서 데이터 수집 병목 및 레이턴시</div>
          <div class="issue-row"><strong>현상:</strong> 센서 노드가 동시에 데이터를 게이트웨이로 전송할 때 패킷 유실 및 딜레이 발생</div>
          <div class="issue-row"><strong>원인:</strong> 동기식 통신 대기로 인한 CPU 차단 현상 확인</div>
          <div class="issue-row"><strong>해결:</strong> FreeRTOS 태스크 분리 및 비동기 웹소켓 통신 인터럽트 제어로 변환하여 대기 시간 단축</div>
        </div>
      </div>
      <div class="intro-section">
        <div class="intro-section-title">🏁 프로젝트 결과 및 느낀 점</div>
        <div class="intro-row"><span class="intro-label">최종 성과</span><span class="intro-value"><!-- 성과 내용 --></span></div>
        <div class="intro-row"><span class="intro-label">배운 점</span><span class="intro-value">그래프 탐색 알고리즘(Dijkstra)의 하드웨어 실시간 적용 및 임베디드 멀티태스킹 설계 능력을 습득했습니다.</span></div>
      </div>
    </div>
  </div>

  <!-- ===================== 코드 탭 ===================== -->
  <div id="tab-code" class="tab-content">
    <style>
      .code-tab-header { position:sticky; top:0; background:linear-gradient(180deg,#0f172a 80%,transparent); z-index:10; padding:20px 0 14px 0; margin-bottom:10px; font-family:'Pretendard',sans-serif; }
      .code-tab-title { color:#10b981; font-size:1.4rem; font-weight:700; display:flex; align-items:center; gap:10px; }
      .code-tab-desc { color:#64748b; font-size:0.85rem; margin-top:4px; }
      .code-accordion-new { background:#1e293b; border:1px solid #334155; border-radius:10px; margin-bottom:12px; overflow:hidden; font-family:'Pretendard',sans-serif; }
      .code-accordion-new summary { padding:16px 20px; background:#0f172a; color:#10b981; font-weight:600; cursor:pointer; list-style:none; display:flex; align-items:center; justify-content:space-between; font-size:1rem; outline:none; transition:background 0.2s; }
      .code-accordion-new summary:hover { background:#1e293b; }
      .code-accordion-new summary::-webkit-details-marker { display:none; }
      .code-accordion-new summary::after { content:'▼'; font-size:0.8rem; color:#64748b; transition:transform 0.3s; }
      .code-accordion-new[open] summary::after { transform:rotate(180deg); }
      .code-accordion-new .accordion-body { padding:20px; border-top:1px solid #334155; }
      .code-file-tag { display:inline-block; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); color:#10b981; border-radius:6px; padding:2px 10px; font-size:0.75rem; margin-bottom:10px; font-family:monospace; }
    </style>
    <div style="padding:30px 0;">
      <div class="code-tab-header">
        <div class="code-tab-title">🔢 핵심 소스코드</div>
        <div class="code-tab-desc">각 섹션을 클릭하면 코드를 펼쳐볼 수 있습니다.</div>
      </div>
      <details class="code-accordion-new">
        <summary>📄 코드 섹션 1</summary>
        <div class="accordion-body">
          <div class="code-file-tag">파일명.cpp</div>
          <pre style="background:#0f172a;color:#e2e8f0;padding:20px;border-radius:8px;overflow-x:auto;font-size:0.82rem;line-height:1.6;font-family:'Consolas',monospace;border:1px solid #334155;"><code>// 코드를 이곳에 붙여넣어 주세요</code></pre>
        </div>
      </details>
    </div>
  </div>

</div>

<script>
(function() {
  var slides = [
    '/assets/img/projects/fire_slides/slide_1.png',
    '/assets/img/projects/fire_slides/slide_2.png',
    '/assets/img/projects/fire_slides/slide_3.png',
    '/assets/img/projects/fire_slides/slide_4.png',
    '/assets/img/projects/fire_slides/slide_5.png',
    '/assets/img/projects/fire_slides/slide_6.png'
  ];
  var container = document.getElementById('pdf-slider-fire');
  var btnPrev   = document.getElementById('pdf-fire-prev');
  var btnNext   = document.getElementById('pdf-fire-next');
  if (!container || !slides.length) { return; }
  var idx = 0;
  container.innerHTML = '';
  slides.forEach(function(src,i) {
    var slide = document.createElement('div');
    slide.className = 'pdf-slide' + (i===0?' active':'');
    var img = document.createElement('img');
    img.src=src; img.alt='Slide '+(i+1);
    slide.appendChild(img); container.appendChild(slide);
  });
  function showSlide(n) {
    var els = container.querySelectorAll('.pdf-slide');
    idx = Math.max(0, Math.min(n, slides.length - 1));
    els.forEach(function(el,i){ el.classList.toggle('active',i===idx); });
    if(btnPrev) { btnPrev.style.visibility = (idx === 0) ? 'hidden' : 'visible'; }
    if(btnNext) { btnNext.style.visibility = (idx === slides.length - 1) ? 'hidden' : 'visible'; }
  }
  if(btnPrev) { btnPrev.addEventListener('click',function(){ showSlide(idx-1); }); }
  if(btnNext) { btnNext.addEventListener('click',function(){ showSlide(idx+1); }); }
  showSlide(0);
})();
</script>

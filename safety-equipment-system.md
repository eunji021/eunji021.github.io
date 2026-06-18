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
  .sim-test-btn {
    position: absolute; bottom: -70px; left: 50%; transform: translateX(-50%);
    padding: 6px 12px; background: #ef4444; color: white; border: none; border-radius: 6px;
    font-size: 0.75rem; font-weight: bold; cursor: pointer; transition: all 0.2s; white-space: nowrap;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.4); z-index: 10;
  }
  .sim-test-btn:hover { background: #dc2626; transform: translateX(-50%) translateY(-2px); }
  .sim-test-btn:active { transform: translateX(-50%) translateY(0); }

  /* HW Control Panel Styles */
  .hw-control-panel {
    background: #0f172a; border: 2px solid #334155; border-radius: 8px; padding: 15px; margin-top: 20px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
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
    height: 60px; width: 100%; position: relative; overflow: hidden;
  }
  .sensor-canvas { width: 100%; height: 100%; display: block; }
  .hw-error-log {
    color: #ef4444; font-family: monospace; font-size: 0.75rem; margin-top: 8px; text-align: center;
    min-height: 12px; display: none;
  }
  .hw-error-log.show { display: block; animation: flashLog 1s infinite alternate; }
  @keyframes flashLog { from { opacity: 0.5; } to { opacity: 1; } }
  
  
  
  

  /* Frozen state */
  .sim-container.frozen { border-color: #f59e0b; box-shadow: 0 0 30px rgba(245, 158, 11, 0.6); }
  .sim-container.frozen .drag-item, .sim-container.frozen .worker-body, .sim-container.frozen .hr-svg {
    animation-play-state: paused !important; pointer-events: none;
  }


  /* Markdown style adjustments for tabs */
  #tab-intro h1, #tab-code h1 {
    color: #10b981; font-size: 1.6rem; margin: 30px 0 15px; font-family: 'Pretendard', sans-serif; font-weight: 700;
  }
  #tab-intro h2, #tab-code h2 {
    color: #10b981; font-size: 1.3rem; margin: 25px 0 12px; font-family: 'Pretendard', sans-serif; border-bottom: 1px solid rgba(16, 185, 129, 0.2); padding-bottom: 8px; font-weight: 600;
  }
  #tab-intro h3, #tab-code h3 {
    color: #38bdf8; font-size: 1.1rem; margin: 20px 0 10px; font-family: 'Pretendard', sans-serif; font-weight: 600;
  }
  #tab-intro h4, #tab-code h4 {
    color: #cbd5e1; font-size: 1.0rem; margin: 18px 0 8px; font-family: 'Pretendard', sans-serif; font-weight: 600;
  }
  #tab-intro p, #tab-intro li, #tab-code p, #tab-code li {
    color: #94a3b8; font-size: 0.92rem; line-height: 1.7; margin-bottom: 8px;
  }
  #tab-intro strong, #tab-code strong {
    color: #e2e8f0;
  }
  #tab-intro blockquote, #tab-code blockquote {
    border-left: 3px solid #10b981; padding: 8px 16px; background: rgba(16, 185, 129, 0.05); color: #94a3b8; font-size: 0.9rem; line-height: 1.7; margin: 15px 0; border-radius: 0 6px 6px 0;
  }
  #tab-intro hr, #tab-code hr {
    border: none; border-top: 1px solid #334155; margin: 20px 0;
  }
  #tab-intro code, #tab-code code {
    background: #1e293b; color: #10b981; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; font-family: 'Consolas', monospace;
  }
  #tab-intro ul, #tab-intro ol, #tab-code ul, #tab-code ol {
    margin-left: 20px; margin-bottom: 15px;
  }
</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-simulator">💻 시뮬레이터</button>
    <button class="tab-btn" data-target="tab-overview">📊 한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">📄 소개</button>
    <button class="tab-btn" data-target="tab-code">🔢 코드</button>
  </div>

  <!-- 1. 시뮬레이터 탭 콘텐츠 -->

<style>
    /* 시뮬레이터 스타일 */
  .sim-container {
    width: 100%; height: 650px;
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
  
  /* 스마트폰 앱 UI 스타일 (아이폰 모티브 & 스크롤 추가) */
  .sim-app-ui {
    width: 280px; height: 550px; background: #1e293b; 
    border-radius: 35px; border: 8px solid #0f172a;
    padding: 40px 10px 20px 10px; position: relative; font-family: 'Pretendard', sans-serif;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6), inset 0 0 5px rgba(255,255,255,0.1);
    overflow-y: auto; overflow-x: hidden; scrollbar-width: thin; scrollbar-color: rgba(255,255,255,0.2) transparent;
  }
  .sim-app-ui::-webkit-scrollbar { width: 5px; }
  .sim-app-ui::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.2); border-radius: 5px; }
  
  /* 노치 (Dynamic Island 느낌) */
  .sim-phone-notch {
    position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
    width: 80px; height: 20px; background: #0f172a; border-radius: 10px; z-index: 20;
  }
  /* 하단 홈 인디케이터 */
  .sim-phone-home {
    position: sticky; bottom: -15px; left: 50%; transform: translateX(-50%);
    width: 100px; height: 4px; background: rgba(255,255,255,0.3); border-radius: 4px; z-index: 20; margin-top: 20px; margin-bottom: 5px;
  }

  .app-header { text-align: center; margin-bottom: 20px; margin-top: 10px; }
  .app-badge {
    background: #10b981; color: white; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 1.1rem; letter-spacing: 1px; transition: background 0.3s;
    display: inline-block;
  }
  
  .worker-status-card {
    background: rgba(0,0,0,0.2); border-radius: 12px; padding: 12px; margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.05); transition: all 0.3s; position: relative;
  }
  .worker-status-card.warning { border-color: #f59e0b; background: rgba(245, 158, 11, 0.1); }
  .worker-status-card.emergency { border-color: #ef4444; background: rgba(239, 68, 68, 0.2); animation: cardShake 0.5s infinite; }
  @keyframes cardShake { 0% { transform: translateX(0); } 25% { transform: translateX(-2px); } 75% { transform: translateX(2px); } 100% { transform: translateX(0); } }

  .worker-name { color: #cbd5e1; font-weight: bold; margin-bottom: 10px; font-size: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 5px; display: flex; justify-content: space-between; }
  .worker-name span { font-size: 0.85rem; padding: 2px 6px; border-radius: 10px; background: #10b981; color: white; }
  .worker-status-card.warning .worker-name span { background: #f59e0b; }
  .worker-status-card.emergency .worker-name span { background: #ef4444; }
  
  .app-item { padding: 8px 10px; border-radius: 6px; margin-bottom: 8px; color: #10b981; font-weight: bold; display: flex; justify-content: space-between; font-size: 0.95rem; transition: all 0.3s; background: rgba(16,185,129,0.1); }
  .app-item.off { color: #ef4444; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); }
  
  /* 심박수 그래프 */
  .heart-rate {
    height: 30px; width: 100%; margin-top: 10px; background: rgba(0,0,0,0.3); border-radius: 5px;
    position: relative; overflow: hidden; display: flex; align-items: center;
  }
  .hr-line { position: absolute; width: 100%; height: 2px; background: #ef4444; display: none; }
  .hr-svg { width: 100%; height: 100%; stroke: #10b981; fill: none; stroke-width: 2; stroke-dasharray: 60; animation: dashMove 2s linear infinite; }
  @keyframes dashMove { to { stroke-dashoffset: -120; } }
  
  .worker-status-card.warning .hr-svg { stroke: #f59e0b; animation: dashMove 0.4s linear infinite; stroke-width: 3; }
  .worker-status-card.emergency .hr-svg { display: none; }
  .worker-status-card.emergency .hr-line { display: block; }
  
  /* 앱 내 개별 긴급 팝업 */
  .app-emergency-popup {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(239, 68, 68, 0.95);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: white; font-weight: bold; text-align: center; padding: 20px; z-index: 30;
    backdrop-filter: blur(5px); opacity: 0; pointer-events: none; transition: opacity 0.3s;
  }
  .app-emergency-popup.show { opacity: 1; pointer-events: auto; }
  
  /* 2인 작업자 영역 */
  .sim-workers-area {
    flex: 1.5; position: relative; display: flex; align-items: center; justify-content: space-around;
    background: radial-gradient(circle at center, rgba(16,185,129,0.05) 0%, transparent 70%);
  }
  .worker-wrapper { position: relative; width: 120px; height: 350px; display: flex; justify-content: center; align-items: flex-end; }
  
  .worker-body {
    width: 80px; height: 140px; background: #334155; border-radius: 40px 40px 10px 10px; position: absolute; bottom: 80px; transition: transform 0.15s ease-in; z-index: 5;
    display: flex; justify-content: center; cursor: pointer;
  }
  .worker-body.fallen { transform: rotate(90deg) translate(30px, 40px); }
  .worker-name-tag { position: absolute; bottom: -25px; color: #94a3b8; font-weight: bold; font-size: 0.9rem; pointer-events: none; }
  
  .timeout-text {
    position: absolute; top: -40px; color: #ef4444; font-weight: bold; font-size: 1.2rem; display: none; width: 200px; text-align: center; left: -60px; text-shadow: 0 0 10px rgba(239,68,68,0.5); z-index: 50; pointer-events: none;
  }
  
  /* 드래그 아이템 & BLE 구름 */
  .drag-item {
    width: 60px; height: 60px; position: absolute; cursor: grab; z-index: 20; user-select: none;
    display: flex; align-items: center; justify-content: center; font-size: 2.5rem;
    background: rgba(255,255,255,0.05); border-radius: 50%; border: 2px dashed rgba(255,255,255,0.2);
    transition: transform 0.1s, border-color 0.2s, background 0.2s;
  }
  .drag-item:active { cursor: grabbing; transform: scale(1.1); }
  .drag-item.error { border-color: #ef4444; background: rgba(239, 68, 68, 0.2); animation: errorShake 0.4s; }
  @keyframes errorShake { 0% { transform: translateX(0); } 25% { transform: translateX(-5px); } 50% { transform: translateX(5px); } 75% { transform: translateX(-5px); } 100% { transform: translateX(0); } }

  .ble-cloud {
    position: absolute; top: -10px; right: -15px; width: 35px; height: 22px;
    background: rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.5); border-radius: 15px;
    display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #bae6fd; font-weight: bold;
    box-shadow: 0 0 10px rgba(56, 189, 248, 0.3); z-index: 25; pointer-events: none;
    animation: floatCloud 2s infinite alternate;
  }
  .drag-item.error .ble-cloud { background: rgba(239, 68, 68, 0.4); border-color: #ef4444; color: #fecaca; box-shadow: 0 0 15px #ef4444; }
  @keyframes floatCloud { from { transform: translateY(0); } to { transform: translateY(-5px); } }

  /* 예외 처리 팝업 (전체 뷰) */
  .system-exception-popup {
    position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(100px);
    width: 80%; background: rgba(15, 23, 42, 0.95); border: 2px solid #ef4444; border-radius: 12px;
    padding: 15px; color: #fff; z-index: 100; opacity: 0; transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 0 10px 30px rgba(0,0,0,0.8); display: flex; align-items: flex-start; gap: 15px; pointer-events: none;
  }
  .system-exception-popup.show { transform: translateX(-50%) translateY(0); opacity: 1; pointer-events: auto; }
  .sep-icon { font-size: 2.5rem; animation: pulseRed 1s infinite alternate; }
  .sep-content h4 { margin: 0 0 5px 0; color: #fca5a5; font-size: 1.1rem; }
  .sep-content p { margin: 0; font-size: 0.85rem; color: #cbd5e1; line-height: 1.4; }
  @keyframes pulseRed { from { opacity: 0.7; transform: scale(1); } to { opacity: 1; transform: scale(1.1); } }

  /* 블루투스 신호 애니메이션 영역 */
  
  .drag-item.detached .ble-cloud { background: rgba(239, 68, 68, 0.4); border-color: #ef4444; color: #fecaca; box-shadow: 0 0 15px #ef4444; animation: errorShake 0.4s; }

  .ble-signal-container { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 15; }
  .ble-signal {
    position: absolute; width: 60px; height: 3px; border-top: 4px dotted rgba(56, 189, 248, 0.9); background: transparent; height: 0;
    box-shadow: 0 0 10px #38bdf8; border-radius: 2px; opacity: 0;
  }
  @keyframes shootSignal {
    0% { transform: translateX(0) scaleX(0.5); opacity: 0; }
    20% { opacity: 1; scaleX(1); }
    100% { transform: translateX(-300px) scaleX(0.5); opacity: 0; }
  }
  .sim-test-btn {
    position: absolute; bottom: -70px; left: 50%; transform: translateX(-50%);
    padding: 6px 12px; background: #ef4444; color: white; border: none; border-radius: 6px;
    font-size: 0.75rem; font-weight: bold; cursor: pointer; transition: all 0.2s; white-space: nowrap;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.4); z-index: 10;
  }
  .sim-test-btn:hover { background: #dc2626; transform: translateX(-50%) translateY(-2px); }
  .sim-test-btn:active { transform: translateX(-50%) translateY(0); }
</style>

  <!-- 체험 시뮬레이터 탭 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container" id="sim-main">
      <div class="ble-signal-container" id="signal-container"></div>
      
      <div class="sim-app">
        <div class="sim-app-ui" id="app-ui-scroll">
          <div class="sim-phone-notch"></div>
          
          <div class="app-header">
            <div class="app-badge" id="app-badge">ALL STABLE</div>
          </div>
          
          
          
          <div class="worker-status-card" id="card-1">
            <div class="worker-name">👷‍♂️ 작업자 1 <span id="w1-badge">STABLE</span></div>
            <div class="app-item" id="app-helmet-1"><span>안전모:</span> <span>착용</span></div>
            <div class="app-item" id="app-vest-1"><span>안전조끼:</span> <span>착용</span></div>
            <div class="heart-rate">
              <svg class="hr-svg" viewBox="0 0 100 20" preserveAspectRatio="none">
                <polyline points="0,10 20,10 25,5 30,15 35,10 50,10 55,2 60,18 65,10 100,10" />
                <polyline points="100,10 120,10 125,5 130,15 135,10 150,10 155,2 160,18 165,10 200,10" />
              </svg>
              <div class="hr-line"></div>
            </div>
          </div>
          
          <div class="worker-status-card" id="card-2">
            <div class="worker-name">👷‍♀️ 작업자 2 <span id="w2-badge">STABLE</span></div>
            <div class="app-item" id="app-helmet-2"><span>안전모:</span> <span>착용</span></div>
            <div class="app-item" id="app-vest-2"><span>안전조끼:</span> <span>착용</span></div>
            <div class="heart-rate">
              <svg class="hr-svg" viewBox="0 0 100 20" preserveAspectRatio="none">
                <polyline points="0,10 20,10 25,5 30,15 35,10 50,10 55,2 60,18 65,10 100,10" />
                <polyline points="100,10 120,10 125,5 130,15 135,10 150,10 155,2 160,18 165,10 200,10" />
              </svg>
              <div class="hr-line"></div>
            </div>
          </div>
          
                    <div class="hw-control-panel">
            <div class="hw-panel-header">
              <span class="hw-title">HW Control Panel</span>
              <span class="hw-com">COM3: Connected</span>
            </div>
            <div class="hw-buttons">
              <button class="btn-estop" id="btn-estop">E-STOP</button>
              <button class="btn-reset" id="btn-reset">RESET</button>
            </div>
            <div class="sensor-graph-container">
              <canvas id="sensor-canvas" class="sensor-canvas"></canvas>
            </div>
            <div class="hw-error-log" id="hw-error-log">[SYSTEM EMERGENCY CRASHED / Error Code: 0x0F]</div>
          </div>
          
          <div class="app-emergency-popup" id="app-popup">
            <div style="font-size: 3.5rem; margin-bottom:15px; animation: pulseRed 1s infinite alternate;">🚨</div>
            <div style="font-size: 1.1rem; line-height: 1.5;" id="popup-text"></div>
          </div>
          
          <div class="sim-phone-home"></div>
        </div>
      </div>
      
      <div class="sim-workers-area" id="sim-area">
        
        <div class="worker-wrapper" id="wrapper-1">
          <button class="sim-test-btn" id="btn-nomove-1">⚠️ 움직임 정지 테스트</button>
<div class="worker-body" id="worker-body-1" title="클릭해서 일으켜 세우기">
            <div class="timeout-text" id="timeout-text-1"></div>
            <div class="worker-name-tag">작업자 1</div>
          </div>
          <div class="drag-item" id="helmet-1" title="안전모 1">🪖<div class="ble-cloud">BLE</div></div>
          <div class="drag-item" id="vest-1" title="안전조끼 1">🦺<div class="ble-cloud">BLE</div></div>
        </div>

        <div class="worker-wrapper" id="wrapper-2">
          <button class="sim-test-btn" id="btn-nomove-2">⚠️ 움직임 정지 테스트</button>
<div class="worker-body" id="worker-body-2" title="클릭해서 일으켜 세우기">
            <div class="timeout-text" id="timeout-text-2"></div>
            <div class="worker-name-tag">작업자 2</div>
          </div>
          <div class="drag-item" id="helmet-2" title="안전모 2">👷<div class="ble-cloud">BLE</div></div>
          <div class="drag-item" id="vest-2" title="안전조끼 2">🦺<div class="ble-cloud">BLE</div></div>
        </div>
        
      </div>
      
      <div class="system-exception-popup" id="exception-popup">
        <div class="sep-icon">⚠️</div>
        <div class="sep-content">
          <h4>[시스템 예외 처리 안내] 고유 ID 불일치</h4>
          <p>각 작업자의 장비(안전모/조끼)는 고유 기기 ID로 지정되어 타 작업자와 교차 착용이 불가능합니다.<br>장비가 뒤바뀔 경우 실제 산업 현장 사고 시 작업자의 데이터(위치, 맥박 등) 혼동을 초래하여 구조 골든타임을 놓칠 수 있습니다. 본 시스템은 이를 사전에 차단합니다.</p>
        </div>
      </div>
      
    </div>
    <p style="text-align:center; color:#94a3b8; font-size:0.95rem;">💡 마우스 휠로 좌측 모바일 앱을 스크롤 해보세요. 작업자의 장비를 서로 바꿔 씌우는 시도(예외 상황)도 테스트 해볼 수 있습니다.</p>
    <p style="text-align:center; color:#ef4444; font-size:0.95rem; font-weight:bold; margin-top:-10px;">💡 각 작업자 아래의 [⚠️ 움직임 정지 테스트] 버튼을 클릭하면 3초 뒤에 "움직임 없음" 경고를 시뮬레이션 할 수 있습니다.</p>
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
      }
    });
  });

  // Simulator Elements
  const simMain = document.getElementById('sim-main');
  const appBadge = document.getElementById('app-badge');
  const appPopup = document.getElementById('app-popup');
  const popupText = document.getElementById('popup-text');
  const exceptionPopup = document.getElementById('exception-popup');
  const signalContainer = document.getElementById('signal-container');
  const simArea = document.getElementById('sim-area');
  
  const worker1 = {
    id: 1, state: 'STABLE', hOn: true, vOn: true, countdown: 1, timerInterval: null, timerWait: null,
    body: document.getElementById('worker-body-1'),
    card: document.getElementById('card-1'),
    badge: document.getElementById('w1-badge'),
    hUI: document.getElementById('app-helmet-1'),
    vUI: document.getElementById('app-vest-1'),
    tText: document.getElementById('timeout-text-1'),
    wrapper: document.getElementById('wrapper-1')
  };
  
  const worker2 = {
    id: 2, state: 'STABLE', hOn: true, vOn: true, countdown: 1, timerInterval: null, timerWait: null,
    body: document.getElementById('worker-body-2'),
    card: document.getElementById('card-2'),
    badge: document.getElementById('w2-badge'),
    hUI: document.getElementById('app-helmet-2'),
    vUI: document.getElementById('app-vest-2'),
    tText: document.getElementById('timeout-text-2'),
    wrapper: document.getElementById('wrapper-2')
  };

  const gearMap = {
    'helmet-1': { w: worker1, type: 'helmet', el: document.getElementById('helmet-1') },
    'vest-1': { w: worker1, type: 'vest', el: document.getElementById('vest-1') },
    'helmet-2': { w: worker2, type: 'helmet', el: document.getElementById('helmet-2') },
    'vest-2': { w: worker2, type: 'vest', el: document.getElementById('vest-2') }
  };

  function initPos() {
    Object.values(gearMap).forEach(g => snapGear(g.el, g.w.body, g.type));
    worker1.hOn = worker1.vOn = worker2.hOn = worker2.vOn = true;
    updateGlobalState();
  }
  setTimeout(initPos, 100);

  function snapGear(el, body, type) {
    el.classList.remove('detached');
    const wrapper = body.parentElement;
    if(type === 'helmet') {
      el.style.left = (wrapper.offsetWidth/2 - 30) + 'px';
      el.style.top = (body.offsetTop - 40) + 'px';
    } else {
      el.style.left = (wrapper.offsetWidth/2 - 30) + 'px';
      el.style.top = (body.offsetTop + 40) + 'px';
    }
  }

  // --- Timeout & Emergency Logic per Worker ---
  function resetTimer(w) {
    if(w.state === 'EMERGENCY') return; // Cannot reset if fallen unless clicked
    clearInterval(w.timerInterval);
    clearTimeout(w.timerWait);
    w.tText.style.display = 'none';
    w.countdown = 1;
    w.timerWait = setTimeout(() => startCountdown(w), 500);
  }

  function startCountdown(w) {
    if(w.state === 'STABLE' || w.state === 'EMERGENCY') return;
    w.tText.style.display = 'block';
    w.tText.innerText = `미감지: 1`;
    
    w.timerInterval = setInterval(() => {
      if(isFrozen) return;
      w.countdown--;
      w.tText.innerText = `미감지: ${w.countdown}`;
      if(w.countdown <= 0) {
        clearInterval(w.timerInterval);
        triggerEmergency(w);
      }
    }, 1000);
  }

  function triggerEmergency(w) {
    w.state = 'EMERGENCY';
    w.tText.innerText = "🚨 다운 🚨";
    w.body.classList.add('fallen');
    updateGlobalState();
    
  }

  // Stand up by click
  [worker1, worker2].forEach(w => {
    w.body.addEventListener('click', () => {
      if(w.state === 'EMERGENCY') {
        // Snap gear back
        Object.values(gearMap).forEach(g => {
          if(g.w === w) { snapGear(g.el, w.body, g.type); g.el.classList.remove('detached'); if(g.type === 'helmet') w.hOn = true; else w.vOn = true; }
        });
        w.state = 'STABLE';
        w.body.classList.remove('fallen');
        updateGlobalState();
        resetTimer(w);
      }
    });
  });

  // Global State Sync
  function updateGlobalState() {
    [worker1, worker2].forEach(w => {
      const allGood = w.hOn && w.vOn;
      if (w.state !== 'EMERGENCY') {
        w.state = allGood ? 'STABLE' : 'WARNING';
      }

      // Update Card UI
      w.card.className = `worker-status-card ${w.state === 'STABLE' ? '' : w.state.toLowerCase()}`;
      w.badge.innerText = w.state;
      
      w.hUI.innerHTML = `<span>안전모:</span> <span>${w.hOn ? '착용' : '착용 불량'}</span>`;
      w.hUI.className = w.hOn ? 'app-item' : 'app-item off';
      w.vUI.innerHTML = `<span>안전조끼:</span> <span>${w.vOn ? '착용' : '착용 불량'}</span>`;
      w.vUI.className = w.vOn ? 'app-item' : 'app-item off';
    });

    // Determine Global Mode
    const st1 = worker1.state;
    const st2 = worker2.state;
    
    if (st1 === 'EMERGENCY' || st2 === 'EMERGENCY') {
      simMain.className = 'sim-container emergency';
      appBadge.innerText = 'EMERGENCY';
      appBadge.style.background = '#ef4444';
      appPopup.classList.add('show');
      
      let txt = "[위험] 쓰러짐 발생!<br>움직임 감지 안 됨!🚨<br>즉시 구조 바랍니다";
      if(st1 === 'EMERGENCY' && st2 !== 'EMERGENCY') txt = "[위험] <b>작업자 1</b> 쓰러짐 발생!<br>움직임 감지 안 됨!🚨";
      if(st2 === 'EMERGENCY' && st1 !== 'EMERGENCY') txt = "[위험] <b>작업자 2</b> 쓰러짐 발생!<br>움직임 감지 안 됨!🚨";
      if(st1 === 'EMERGENCY' && st2 === 'EMERGENCY') txt = "[위험] <b>작업자 1, 2</b> 모두 쓰러짐!<br>대형 사고 발생!🚨";
      popupText.innerHTML = txt;
      
    } else if (st1 === 'WARNING' || st2 === 'WARNING') {
      simMain.className = 'sim-container warning';
      appBadge.innerText = 'WARNING';
      appBadge.style.background = '#f59e0b';
      appPopup.classList.remove('show');
    } else {
      simMain.className = 'sim-container';
      appBadge.innerText = 'ALL STABLE';
      appBadge.style.background = '#10b981';
      appPopup.classList.remove('show');
    }
  }

  // Shoot BLE Signal Animation
  function shootSignal(el) {
    const rect = el.getBoundingClientRect();
    const simRect = simMain.getBoundingClientRect();
    const sig = document.createElement('div');
    sig.className = 'ble-signal';
    sig.style.top = (rect.top - simRect.top + 20) + 'px';
    sig.style.left = (rect.left - simRect.left - 20) + 'px';
    sig.style.animation = 'shootSignal 1s ease-in-out';
    signalContainer.appendChild(sig);
    setTimeout(() => sig.remove(), 1000);
  }

  setInterval(() => {
    Object.values(gearMap).forEach(g => {
      if((g.type === 'helmet' && g.w.hOn) || (g.type === 'vest' && g.w.vOn)) {
        if(!isFrozen && Math.random() > 0.6) shootSignal(g.el);
      }
    });
  }, 1500);

  // Drag Logic
  Object.values(gearMap).forEach(g => setupDrag(g.el, g.type, g.w));

  let exceptionTimeout = null;
  function showException() {
    exceptionPopup.classList.add('show');
    clearTimeout(exceptionTimeout);
    exceptionTimeout = setTimeout(() => exceptionPopup.classList.remove('show'), 5000);
  }

  function setupDrag(el, type, ownerWorker) {
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
      resetTimer(ownerWorker);
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
      el.style.left = (initialX + clientX - startX) + 'px';
      el.style.top = (initialY + clientY - startY) + 'px';
      resetTimer(ownerWorker);
    }
    
    function dragEnd(e) {
      isDragging = false;
      document.removeEventListener('mousemove', drag);
      document.removeEventListener('mouseup', dragEnd);
      document.removeEventListener('touchmove', drag);
      document.removeEventListener('touchend', dragEnd);
      
      const rect = el.getBoundingClientRect();
      const centerX = rect.left + rect.width/2;
      const centerY = rect.top + rect.height/2;
      
      let snapped = false;
      let wrongDrop = false;

      // Check drop on any worker
      [worker1, worker2].forEach(targetW => {
        const bodyRect = targetW.body.getBoundingClientRect();
        const bodyCX = bodyRect.left + bodyRect.width/2;
        
        if (Math.abs(centerX - bodyCX) < 70) {
          if (type === 'helmet' && Math.abs(centerY - bodyRect.top) < 60) {
            if (targetW === ownerWorker) { snapGear(el, targetW.body, 'helmet'); snapped = true; ownerWorker.hOn = true; }
            else wrongDrop = true;
          }
          else if (type === 'vest' && Math.abs(centerY - (bodyRect.top + bodyRect.height/2)) < 70) {
            if (targetW === ownerWorker) { snapGear(el, targetW.body, 'vest'); snapped = true; ownerWorker.vOn = true; }
            else wrongDrop = true;
          }
        }
      });
      
      if (wrongDrop) {
        // Bounce back animation
        el.classList.add('error');
        setTimeout(() => el.classList.remove('error'), 400);
        el.style.transition = 'all 0.3s';
        snapGear(el, ownerWorker.body, type); // bounce back to original owner
        setTimeout(() => el.style.transition = 'transform 0.1s, border-color 0.2s, background 0.2s', 300);
        showException();
        ownerWorker[type === 'helmet' ? 'hOn' : 'vOn'] = true;
        el.classList.remove('detached');
      } else if (!snapped) {
        ownerWorker[type === 'helmet' ? 'hOn' : 'vOn'] = false;
        el.classList.add('detached');
      } else {
        el.classList.remove('detached');
      }
      
      updateGlobalState();
    }
  }

  [worker1, worker2].forEach(w => {
    const startNoMovementTimer = () => {
      if(w.state === 'EMERGENCY' || !w.hOn || !w.vOn) return;
      clearTimeout(w.wheelTimer);
      w.tText.style.display = 'block';
      
      let timeLeft = 3;
      w.tText.innerText = `미감지: ${timeLeft}`;
      
      w.wheelTimer = setInterval(() => {
        if(w.state === 'EMERGENCY') { clearInterval(w.wheelTimer); return; }
        if(isFrozen) return;
        timeLeft--;
        w.tText.innerText = `미감지: ${timeLeft}`;
        
        if(timeLeft <= 0) {
          clearInterval(w.wheelTimer);
          if(w.hOn && w.vOn) {
            w.state = 'EMERGENCY';
            w.tText.innerText = "🚨 움직임 없음 🚨";
            w.body.classList.add('fallen');
            updateGlobalState();
          } else {
            w.tText.style.display = 'none';
          }
        }
      }, 1000);
    };

    const stopNoMovementTimer = () => {
      if(w.state === 'EMERGENCY') return;
      clearInterval(w.wheelTimer);
      w.tText.style.display = 'none';
    };
    
    const testBtn = document.getElementById(`btn-nomove-${w.id}`);
    if(testBtn) {
      testBtn.addEventListener('click', () => {
        if(w.state === 'EMERGENCY' || !w.hOn || !w.vOn) return;
        startNoMovementTimer();
      });
    }

  // HW Control Panel & Sensor Graph Logic
  const canvas = document.getElementById('sensor-canvas');
  let ctx = null;
  if(canvas) {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    ctx = canvas.getContext('2d');
  }
  
  let isFrozen = false;
  let graphOffset = 0;
  let graphColor = '#10b981'; // Green
  let reqAnimId = null;

  function drawGraph() {
    if(!ctx) return;
    if(isFrozen) return; // freeze graph
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = graphColor;
    
    let isEmergency = simMain.classList.contains('emergency');
    graphColor = isEmergency ? '#ef4444' : '#10b981';
    
    let yBase = canvas.height / 2;
    for(let x=0; x<canvas.width; x+=4) {
      let noise = (Math.random() - 0.5);
      let amplitude = isEmergency ? 40 : 10;
      let y = yBase + (noise * amplitude);
      if(x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    graphOffset += 2;
    reqAnimId = requestAnimationFrame(drawGraph);
  }
  if(canvas) drawGraph();

  // E-STOP & RESET
  const btnEstop = document.getElementById('btn-estop');
  const btnReset = document.getElementById('btn-reset');
  const errorLog = document.getElementById('hw-error-log');
  
  if(btnEstop) {
    btnEstop.addEventListener('click', () => {
      isFrozen = true;
      simMain.classList.add('frozen');
      if(errorLog) errorLog.classList.add('show');
      if(reqAnimId) cancelAnimationFrame(reqAnimId);
      popupText.innerHTML = "<b>[SYSTEM FROZEN]</b><br>E-STOP Activated";
      appPopup.classList.add('show');
    });
  }
  
  if(btnReset) {
    btnReset.addEventListener('click', () => {
      popupText.innerHTML = "Rebooting...<br>Please wait";
      appPopup.classList.add('show');
      setTimeout(() => {
        isFrozen = false;
        simMain.classList.remove('frozen');
        if(errorLog) errorLog.classList.remove('show');
        appPopup.classList.remove('show');
        
        // Reset workers
        [worker1, worker2].forEach(w => {
          Object.values(gearMap).forEach(g => {
            if(g.w === w) { snapGear(g.el, w.body, g.type); g.el.classList.remove('detached'); if(g.type === 'helmet') w.hOn = true; else w.vOn = true; }
          });
          w.state = 'STABLE';
          w.body.classList.remove('fallen');
          resetTimer(w);
        });
        updateGlobalState();
        drawGraph();
      }, 1000);
    });
  }

  

  });
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

      <!-- PPT 발표 슬라이드 세로 나열 -->
      <div class="slides-vertical-list" style="display:flex; flex-direction:column; gap:24px; margin-bottom:40px;">
        <img src="/assets/img/projects/safety_slides/slide_1.png" alt="Slide 1" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
        <img src="/assets/img/projects/safety_slides/slide_2.png" alt="Slide 2" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
        <img src="/assets/img/projects/safety_slides/slide_3.png" alt="Slide 3" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
        <img src="/assets/img/projects/safety_slides/slide_4.png" alt="Slide 4" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
        <img src="/assets/img/projects/safety_slides/slide_5.png" alt="Slide 5" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
        <img src="/assets/img/projects/safety_slides/slide_6.png" alt="Slide 6" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
      </div>

      <!-- 프로젝트 최종 결과물 사진 -->
      <div class="result-section" style="margin-top: 30px; margin-bottom: 40px; background:#0f172a; border:2px solid #334155; border-radius:12px; padding:24px;">
        <div class="result-section-title" style="color:#cbd5e1; font-weight:bold; font-size:1rem; margin-bottom:16px; font-family:'Pretendard',sans-serif;">🏁 프로젝트 최종 결과물</div>
        <img src="/assets/img/projects/safety_result.png" alt="safety 최종 결과물" class="result-img" style="width:100%; border-radius:8px; border:1px solid #334155; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
      </div>

      <!-- 영상/사진 좌우 배치 (슬라이드 및 결과물 밑으로 이동) -->
      <div class="ov-media-row">
        <div>
          <div class="ov-media-box">
            <!-- 영상: <video src="/assets/videos/safety_demo.mp4" controls></video> -->
            <div><div style="font-size:2.5rem;margin-bottom:10px;">🎬</div><div><strong style="color:#94a3b8;">시연 영상</strong><br><span style="color:#64748b;">video 태그로 교체해 주세요</span></div></div>
          </div>
          <p class="ov-media-label">📽️ 시스템 시연 영상</p>
        </div>
        <div>
          <div class="ov-media-box">
            <!-- 사진: <img src="/assets/images/safety_hw.jpg" alt="하드웨어"> -->
            <div><div style="font-size:2.5rem;margin-bottom:10px;">📸</div><div><strong style="color:#94a3b8;">하드웨어 사진</strong><br><span style="color:#64748b;">img 태그로 교체해 주세요</span></div></div>
          </div>
          <p class="ov-media-label">🔧 실제 하드웨어 구성</p>
        </div>
      </div>

    </div>
    </div>

  <!-- ===================== 소개 탭 ===================== -->
  <div id="tab-intro" class="tab-content" markdown="1">

# 공사장 안전장비 실시간 착용여부 시스템 
> **ESP32 중계기(Gateway) 설계 및 데이터 패킹 프로토콜 구현을 통한 다중 디바이스 통신 제약 극복**

* **진행 기간:** 2025.03 ~ 2025.06 
* **주요 역량:** 임베디드 소프트웨어 아키텍처 설계, 멀티 디바이스 데이터 패킹 및 타임 슬라이싱(Time-Slicing) 스트리밍, 임베디드 예외 처리 루틴 구현
* **사용 기술:** `C/C++ (Arduino IDE)`, `ESP32`, `Bluetooth LE (BLE Advertising)`, `Bluetooth Serial (Classic)`, `MPU6050 (I2C)`, `App Inventor`

---

## MY CORE ROLE & ACHIEVEMENTS (본인 주도 핵심 성과)
팀 프로젝트 내에서 **하드웨어 핵심 제어 아키텍처 수립 및 소프트웨어 상위 레이어(임베디드 무선 네트워크 ~ 앱 관제) 시스템 전체의 펌웨어 설계 및 통합**을 전담하여 다음과 같은 성과를 냈습니다.

1. **중계기(Gateway) 기반 무선 네트워크 파이프라인 독자 설계**
   - 모바일 플랫폼(App Inventor)의 다중 BLE 소켓 제어 한계를 극복하기 위해, ESP32를 마스터 브릿지로 레이어를 분리하는 임베디드 아키텍처 수립 및 통신 성공률 100% 달성.
2. **타임 슬라이싱(Time-Slicing) 데이터 스트리밍 프로토콜 정립**
   - 다중 작업자(2인) 노드로부터 수집된 가변 데이터를 비동기 버퍼 유실 없이 가공하고, 고유 식별자 문자열 형태로 가공하여 앱 단에 주기적으로 교차 송신하는 펌웨어 로직 구현.
3. **엣지 컴퓨팅 기반 센서 데이터 처리 및 예외 처리 루틴 구현**
   - 각 작업자 단말 내부에서 MPU6050(자이로) 및 감압 센서의 원시 데이터(Raw Data)를 1차 연산 처리하여 무동작 상태(1분 기준) 및 착용 탈착 여부를 실시간 연산하도록 제어 알고리즘 최적화.

---

## 1. 프로젝트 개요 (Overview)
* **배경:** 기존 공사 현장의 안전 관리는 CCTV 및 수동 점검에 의존하여, 작업자의 무착용 상태나 낙상 사고를 실시간으로 인지하고 즉각 대응하기 어려웠습니다.
* **목적:** ESP32 모듈과 다중 센서(압력, 자이로), 블루투스 기술을 융합하여 작업자의 안전모·안전조끼 착용 상태 및 이상 신호를 실시간으로 수집하고 관리자 앱으로 통합 관제하는 IoT 안전 시스템을 구축합니다.

# 

## 2. 시스템 및 네트워크 아키텍처 (Architecture)

### 2-1. 중계기(Gateway) 기반 네트워크 파이프라인 단계별 프로세스
안드로이드(앱 인벤터)의 OS/플랫폼 제약 조건인 '다중 블루투스 연결 불안정성'을 해결하기 위해 제가 직접 설계한 3단계 무선 네트워크 구조입니다.

1. **[1단계] 하드웨어 레벨 다중 수신 (BLE Client ──▶ Gateway)**
   - 각 작업자(Worker A, Worker B)의 안전모와 조끼에 탑재된 ESP32 노드가 압력 및 자이로 센서 데이터를 독립적으로 실시간 계측합니다.
   - 마스터 중계기(ESP32)는 각 노드의 고유 MAC 주소를 기반으로 착용 여부, 낙상 신호, RSSI 데이터를 **BLE 무선 통신**을 통해 병렬로 다중 수신합니다.
2. **[2단계] 스트리밍 데이터 패킹 및 타임 슬라이싱 스트리밍 (Gateway)**
   - 중계기 단에서 수집된 2인의 데이터를 앱이 혼선 없이 구분할 수 있도록 가공합니다.
   - 데이터 병목을 방지하기 위해 토글 변수(`sendWorker1Next`)를 활용하여 **1초 간격으로 작업자1과 작업자2의 상태 메시지를 교차 송신하는 타임 슬라이싱 기법**을 적용했습니다.
   * *구현한 데이터 스트리밍 포맷:* `"작업자1: 정상착용
"` / `"작업자2: 착용불량
"`
3. **[3단계] 실시간 데이터 파싱 및 UI 매핑 (App)**
   - 안드로이드 앱(App Inventor)은 중계기와 연결된 단일 **Classic 블루투스** 채널을 통해 끊김 없이 정제된 패킷 스트링을 수신합니다.
   - 수신된 문자열을 실시간 분리(Parsing)하여 화면 내 **Worker A와 Worker B의 개별 대시보드 UI에 독립적으로 값을 매핑**하여 실시간 다중 관제를 시각화했습니다.

### 2-2. 하드웨어 구성 사양 (Hardware Spec)
* **메인 컨트롤러:** ESP32 (송신부 헬멧 2대 / 수신부 조끼 2대 / 마스터 중계기 1대 총 5대 구성 프로토타입)
* **센서 및 모듈:** 감압 센서 (FSR RA12P), 자이로 센서 (MPU6050 계열), 능동 부저, 고휘도 LED
* **전원부:** 3.7V 리튬이온 배터리, TP4056 충전 모듈, MT3608 승압 컨버터

## CORE SOURCE CODE (내가 직접 구현한 핵심 소스코드)

### 3-1. 마스터 중계기(Gateway) 라우팅 핵심 소스코드
> **고유 MAC 주소 필터링 및 타임 슬라이싱 기반 앱인벤터 스트리밍 제어 알고리즘**

* **비동기 BLE 스캔 및 필터링:** 현장 내 수많은 BLE 신호 중 관제 대상인 작업자 1, 2의 고유 MAC 주소 패킷만 정밀 필터링하도록 설계했습니다.
* **하드웨어 엣지 데이터 디코딩:** 디바이스 노드가 보낸 팩추얼 데이터(Manufacturer Data)를 실시간 파싱하여 최종 알람 상태 변수(`'B'` 또는 `'N'`)를 정확히 추출합니다.
* **타임 슬라이싱 알고리즘 기법:** 단일 채널 직렬 통신의 병목 현상을 방지하기 위해, 토글 변수(`sendWorker1Next`)와 1000ms 주기 인터벌을 제어하여 작업자 1, 2의 데이터를 1초 간격으로 번갈아 안전하게 스트리밍합니다.


## TECHNICAL TROUBLESHOOTING (나의 문제 해결 경험)

### 앱 인벤터의 다중 디바이스 연결 한계 극복 (네트워크 구조 개선)
* **문제 상황:** 초기 설계 시 스마트폰 앱이 헬멧과 조끼의 BLE 신호를 직접 다중 수신하도록 구현하려 했으나, 앱 인벤터 플랫폼 특성상 멀티 커넥션 유지가 불가능해 신호가 유실되거나 앱이 다운되는 현상이 발생함.
* **원인 분석:** 모바일 프로토콜 환경 및 컴포넌트 특성상 다중 무선 블루투스 소켓 분할 제어의 드라이버 인터페이스 제약 확인.
* **해결 기술:** 하드웨어 단에 **ESP32 중계기(Gateway) 허브를 중간 브릿지로 상정하는 토폴로지 아키텍처 변환**을 주도함. 하드웨어 레벨(ESP32 내부 펌웨어)에서 무선 BLE 스캔을 통해 여러 작업자 장치를 수집 및 병렬 처리하고, 모바일 앱과는 1:1 Classic 블루투스 직렬 통신 구조로 단순화하여 **통신 제약 완벽 해결 및 데이터 전송 성공률 100%** 달성.

### 다중 데이터 스트리밍 시 동기화 타이밍 제어를 통한 데이터 밀림 방지
* **문제 상황:** 2인 작업자의 대량 센서 정보가 비동기적으로 중계기에 연속 인입될 때, 앱인벤터 내부 버퍼 처리 속도와 무선 송신 주기가 어긋나 UI 데이터 동기화 지연 및 다른 작업자의 모니터링 창에 데이터가 맵핑되는 결함 발생.
* **해결 기술:** 중계기 제어 펌웨어 내부에 **1000ms 주기성 전송 인터벌 인터럽트 및 토글 제어 부울 선언을 이용한 '타임 슬라이싱 교차 스트리밍' 알고리즘**을 도입함. 수신 채널을 의도적으로 정형화하고 데이터 프레임 앞단에 문자열 인덱스 식별 정보(`"작업자1:"`, `"작업자2:"`)를 확실히 패킹하여 보냄으로써 수신 정합성과 데이터 분류 가독성을 완전 확보함.

---

## 4. 결과 및 기대 효과 (Conclusion)
* **다중 관제 아키텍처 검증:** 스마트폰이나 개발 플랫폼의 제약 조건에 구애받지 않고, 중계기 설계를 통해 2인 이상의 작업자 상태를 실시간 대시보드로 안정적으로 모니터링할 수 있음을 입증했습니다.
* **소프트웨어 확장성(Scale-up):** 향후 현장 대규모 확장 시에도 모바일 앱의 복잡한 소스코드를 수정할 필요 없이, **중계기 단에서 노드 관리 로직을 추가하고 패킷 구조만 확장**하면 되므로 뛰어난 유지보수성을 가진 시스템 구조입니다.

---

## 팀 프로젝트 개요 
* **참여 인원:** 4명 
* **협업 내역:**
  - **권은지 (본인):** 하드웨어 핵심 제어 로직 구현, App Inventor 모바일 앱 개발, ESP32 중계기-앱 간 블루투스 연동 및 데이터 파싱 구현
  - 팀원 A (최성용): 하드웨어 회로 설계, 센서 노드 원시 코드 작성
  - 팀원 B (구민서): 외형 PETG 3D 케이스 설계 및 구조물 조립
  - 팀원 C (이명은): ESP32-앱 간 블루투스 통신 기초 테스트 및 디버깅 보조

  </div>

  <!-- ===================== 코드 탭 ===================== -->
  <div id="tab-code" class="tab-content" markdown="1">
    <div style="padding: 30px 0;">
      <!-- 상단 타이틀 상시 노출 -->
      <div class="code-tab-header">
        <div class="code-tab-title">🔢 핵심 소스코드</div>
        <div class="code-tab-desc">상위 1~4번 섹션은 바로 확인하실 수 있으며, 5번 전체 소스코드는 클릭하여 펼쳐볼 수 있습니다.</div>
      </div>

      <!-- 1~4번 섹션 상시 노출 -->
      <div class="code-direct-view" style="margin-bottom: 30px;">
### 1. 전체 시스템 데이터 흐름 요약
> 각 장치 간의 블루투스(BLE) 무선 통신 프로토콜을 맞춰 시스템 전체가 실시간으로 유기적으로 동작하도록 구조를 설계함.

* **[1단계] 작업자 헬멧 (Slave): 센서 데이터 연산 및 판정**
  * **낙상 감지:** 자이로 센서(MPU6050) 가속도 변화량이 **`0.3`** 이하로 떨어지는 상태가 **`60초`** 지속되면 위험 상태로 판정함. (구동 초기 **`3초`**간은 센서 안정화 시간 예외 처리)
  * **미착용 감지:** 감압 센서 값이 **`30`** 이하로 떨어지면 미착용으로 판정해 자체 부저를 구동함.
  * **BLE 데이터 송출:** 판정 결과에 따라 무선 광고 신호 영역에 **`B:N`**(정상) 또는 **`B:B`**(위험) 포맷을 실어 주변에 뿌림.
  * **구역 이탈 감지:** 특정 기준 비콘의 MAC 주소를 필터링해 신호 강도(RSSI)가 **`-50dBm`** 이하로 떨어지면 위험 상태(`weakSignalDetected`)로 판정해 부저를 울림.

* **[2단계] 중계기 (Master): 데이터 취합 및 앱 전송**
  * **데이터 스캔:** 중계기 ESP32가 주변의 `WORKER1_MAC`, `WORKER2_MAC` 주소를 필터링해 `B:B` / `B:N` 상태 값을 스캔함.
  * **앱 시리얼 전송:** 취합한 데이터를 앱인벤터가 읽기 쉽도록 **`"작업자1: 착용불량"`** 또는 **`"작업자1: 정상착용"`** 한글 문자열로 변환하고 개행 문자(`
`)를 붙여 클래식 블루투스 시리얼로 앱에 최종 송신함.

---

### 2. 내가 전담한 핵심 코드 및 상세 설명

#### 중계기 제어 및 앱 송신 메인 코드 (`Relay_Master_Code.ino`)
* **핵심 로직 설명:** * 고유 MAC 주소 매칭과 `toLowerCase()` 함수를 통해 현장 노이즈 신호를 원천 차단함.
  * 앱인벤터의 다중 연결 한계를 깨기 위해, `millis()` 함수 기반의 타임 스케줄러로 **`1초(1000ms)`**마다 `sendWorker1Next` 플래그를 토글시켜 작업자 1과 2의 데이터를 교차 전송함.

```cpp
cpp
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

// 실물 보드의 고유 MAC 주소 고정 (필터링 설계)
const String WORKER1_MAC = "ec:e3:34:bf:80:9e";
const String WORKER2_MAC = "ec:e3:34:bf:e6:aa";

BLEScan* pBLEScan;
const int SCAN_TIME = 2;

struct WorkerData {
  bool dataReceived = false;
  int rssi = 0;
  String advData = "";
  char buzzerState = 'N'; 
};

WorkerData worker1, worker2;

unsigned long lastSendTime = 0;
const unsigned long SEND_INTERVAL = 1000; // 1초 전송 주기
bool sendWorker1Next = true;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String mac = advertisedDevice.getAddress().toString();
    mac.toLowerCase(); // 대소문자 무선 데이터 예외 처리

    if (mac == WORKER1_MAC || mac == WORKER2_MAC) {
      String adv = advertisedDevice.getManufacturerData().c_str();
      if (adv.length() == 0) {
        adv = advertisedDevice.toString().c_str();
      }

      int rssi = advertisedDevice.getRSSI();
      char buzzerChar = 'N';

      if (adv.length() > 0) {
        char lastChar = adv.charAt(adv.length() - 1);
        if (lastChar == 'B' || lastChar == 'N') {
          buzzerChar = lastChar;
        }
      }

      if (mac == WORKER1_MAC) {
        worker1.dataReceived = true;
        worker1.rssi = rssi;
        worker1.advData = adv;
        worker1.buzzerState = buzzerChar;
      } else {
        worker2.dataReceived = true;
        worker2.rssi = rssi;
        worker2.advData = adv;
        worker2.buzzerState = buzzerChar;
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  SerialBT.begin("RelayDeviceBT"); // 앱인벤터와 연동될 블루투스 이름
  
  BLEDevice::init("Relay-Device");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  BLEScanResults* results = pBLEScan->start(SCAN_TIME, false);
  if (results->getCount() == 0) {
    worker1.dataReceived = false;
    worker2.dataReceived = false;
  }
  pBLEScan->clearResults();

  // 1초마다 작업자 데이터를 교차 전송하여 데이터 과부하 및 튕김 방지
  if (millis() - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = millis();

    if (sendWorker1Next) {
      if (worker1.dataReceived) {
        String message = "작업자1: ";
        message += (worker1.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자1: 데이터 없음");
      }
    } else {
      if (worker2.dataReceived) {
        String message = "작업자2: ";
        message += (worker2.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자2: 데이터 없음");
      }
    }
    sendWorker1Next = !sendWorker1Next; // 플래그 토글
  }
  delay(100);
}
```

---

### 3. BLE 거리 판정 및 이탈 감지 로직 코드 (BLE_Distance_Scanner.ino)
* **핵심 로직 설명:** * 기준이 되는 비콘(targetMac)의 RSSI 무선 강도를 체크하여 -50dBm 이하로 떨어지면    작업자가 구역을 이탈한 것으로 보고 부저 경고 신호를 발생시킴.
* 메모리 오버플로우를 막기 위해 스캔 후 clearResults()로 버퍼를 즉각 초기화함.

```cpp
cpp
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>

#define BUZZER_PIN 4 

int scanTime = 3; 
BLEScan* pBLEScan;

String targetMac = "ec:e3:34:be:48:2a"; 
int targetRSSI = -50; 
bool weakSignalDetected = false;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    String foundMac = advertisedDevice.getAddress().toString().c_str();
    foundMac.toLowerCase();

    if (foundMac == targetMac) {
      int rssi = advertisedDevice.getRSSI();

      if (rssi < targetRSSI) {
        weakSignalDetected = true; 
      } else {
        weakSignalDetected = false; 
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER_PIN, OUTPUT); 

  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  weakSignalDetected = false; 
  pBLEScan->start(scanTime, false);
  pBLEScan->clearResults();

  if (weakSignalDetected) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500);
    digitalWrite(BUZZER_PIN, LOW);
    delay(1500); 
  } else {
    digitalWrite(BUZZER_PIN, LOW); 
    delay(2000); 
  }
}
```

---

### 4. MIT APP Inventor(앱 인벤터)

<div style="margin-top:16px; text-align:center;">
  <img src="/assets/img/projects/앱.png" alt="App Inventor 블록 코드" style="width:100%; max-width:800px; border-radius:8px; border:1px solid #334155;">
  <p style="color:#64748b; font-size:0.8rem; text-align:center; margin-top:8px;">App Inventor 블록 코드 전체 구성</p>
</div>

      </div>

      <!-- 5번 전체 소스코드 아코디언 토글 -->
      <details class="code-accordion-new">
        <summary>📄 5. 실시간 안전 장비 착용 여부 시스템 전체적인 소스코드</summary>
        <div class="accordion-body" markdown="1">
* **작업자 MAC 주소:** esp32 마다 고유의 'MAC' 주소가 있어 'MAC' 주소만 바꿔서 사용함.

#### 5-1 MAC 주소 찾는 코드
```cpp
cpp
#include <BLEDevice.h>

void setup() {
  Serial.begin(115200);
  BLEDevice::init("");  // BLE 초기화

  String bleMac = BLEDevice::getAddress().toString().c_str();  // BLE MAC 주소 얻기
  Serial.print("BLE MAC Address: ");
  Serial.println(bleMac);
}

void loop() {
  // do nothing
}
```

#### 5-2 수신용 코드
```cpp
#### 5-2 수신용 코드
cpp
#include <Wire.h>
#include <MPU6050.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BLEAdvertising.h>

#define BUZZER2_PIN 18
#define NO_MOVEMENT_PIN 5
#define PRESSURE_PIN 34  // 감압센서 아날로그 입력 핀

const int SCAN_COUNT_MAX = 10;
const int SCAN_INTERVAL_MS = 30;
const int scanTime = 1;

String targetMac = "ec:e3:34:be:48:2a"; // 변경 필요 시 수정
int rssiThreshold = -60;

MPU6050 mpu;
unsigned long lastMovementTime = 0;
const unsigned long movementThreshold = 60000;
float movementDelta = 0.3;
int16_t ax_prev = 0, ay_prev = 0, az_prev = 0;
unsigned long startupTime = 0;
const unsigned long startupDelay = 3000;

BLEScan* pBLEScan;

std::vector<int> rssiValues;
int scanCount = 0;
unsigned long lastScanMillis = 0;

bool weakSignalDetected = false;

const int pressureThreshold = 30; // 300 이상이면 부저 안 울림
const unsigned long buzzerInterval = 1000;
unsigned long lastBuzzerToggle = 0;
bool buzzerState = false;

String lastAdvData = "NONE";

BLEAdvertising* pAdvertising;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String foundMac = advertisedDevice.getAddress().toString().c_str();
    foundMac.toLowerCase();

    if (foundMac == targetMac) {
      int rssi = advertisedDevice.getRSSI();
      String advData = advertisedDevice.getManufacturerData().c_str();

      if (advData.length() == 0) {
        advData = advertisedDevice.toString().c_str();  // 디버깅용
      }

      Serial.print("BLE 광고 데이터 수신 (");
      Serial.print(foundMac);
      Serial.print("): ");
      Serial.println(advData);

      lastAdvData = advData;
      rssiValues.push_back(rssi);
    }
  }
};

void checkMovement() {
  int16_t ax = mpu.getAccelerationX();
  int16_t ay = mpu.getAccelerationY();
  int16_t az = mpu.getAccelerationZ();

  float deltaX = abs(ax - ax_prev) / 16384.0;
  float deltaY = abs(ay - ay_prev) / 16384.0;
  float deltaZ = abs(az - az_prev) / 16384.0;

  if (millis() - startupTime > startupDelay) {
    if (deltaX > movementDelta || deltaY > movementDelta || deltaZ > movementDelta) {
      lastMovementTime = millis();
      Serial.println("정상 착용 움직임 감지됨");
    }
  }

  ax_prev = ax;
  ay_prev = ay;
  az_prev = az;
}

void setup() {
  Serial.begin(115200);
  Serial.println("헬멧 BLE 수신기 + 센서 초기화 중...");

  pinMode(BUZZER2_PIN, OUTPUT);
  pinMode(NO_MOVEMENT_PIN, OUTPUT);
  pinMode(PRESSURE_PIN, INPUT);

  digitalWrite(BUZZER2_PIN, LOW);
  digitalWrite(NO_MOVEMENT_PIN, LOW);

  Wire.begin(21, 22);
  mpu.initialize();
  delay(100);
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 연결 실패!");
    while (1) delay(1000);
  }
  Serial.println("MPU6050 연결 성공");

  ax_prev = mpu.getAccelerationX();
  ay_prev = mpu.getAccelerationY();
  az_prev = mpu.getAccelerationZ();
  lastMovementTime = millis();
  startupTime = millis();

  BLEDevice::init("Helmet-Receiver");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);

  rssiValues.clear();
  scanCount = 0;
  lastScanMillis = 0;
  weakSignalDetected = false;

  // BLE 광고 송출 초기화
  pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinInterval(0x20);
  pAdvertising->setMaxInterval(0x40);
  BLEDevice::startAdvertising();

  Serial.println("시스템 준비 완료");
}

void loop() {
  checkMovement();

  int pressureValue = analogRead(PRESSURE_PIN);
  bool isPressed = (pressureValue > pressureThreshold);
  Serial.print("감압센서 값: ");
  Serial.println(pressureValue);

  bool noMovement = (millis() - lastMovementTime > movementThreshold);
  if (noMovement) {
    Serial.println("착용불량 - 1분 이상 움직임 없음!");
    digitalWrite(NO_MOVEMENT_PIN, HIGH);
  } else {
    digitalWrite(NO_MOVEMENT_PIN, LOW);
  }

  if (millis() - lastScanMillis >= SCAN_INTERVAL_MS) {
    lastScanMillis = millis();
    if (scanCount == 0) rssiValues.clear();

    Serial.printf("스캔 %d / %d 시작
", scanCount + 1, SCAN_COUNT_MAX);
    pBLEScan->clearResults();
    pBLEScan->start(scanTime, false);

    scanCount++;

    if (scanCount >= SCAN_COUNT_MAX) {
      if (rssiValues.size() > 0) {
        long sum = 0;
        for (int rssi : rssiValues) sum += rssi;
        float avgRSSI = (float)sum / rssiValues.size();

        Serial.print("RSSI 평균값: ");
        Serial.println(avgRSSI);

        weakSignalDetected = (avgRSSI < rssiThreshold);
      } else {
        Serial.println("타겟 장치 발견 안됨.");
        weakSignalDetected = false;
      }
      scanCount = 0;
    }
  }

  int16_t ax = mpu.getAccelerationX();
  int16_t ay = mpu.getAccelerationY();
  int16_t az = mpu.getAccelerationZ();

  Serial.print("자이로센서 값 - ax: ");
  Serial.print(ax);
  Serial.print(", ay: ");
  Serial.print(ay);
  Serial.print(", az: ");
  Serial.println(az);

  Serial.print("헬멧 상태 데이터: ");
  Serial.println(lastAdvData);  // 마지막 받은 광고 데이터 출력

  bool pressureAlarm = (pressureValue < pressureThreshold);
  bool movementAlarm = noMovement;
  bool distanceAlarm = weakSignalDetected;

  bool shouldBuzz = pressureAlarm || movementAlarm || distanceAlarm;

  // 부저 제어
  if (shouldBuzz) {
    if (millis() - lastBuzzerToggle >= buzzerInterval) {
      buzzerState = !buzzerState;
      digitalWrite(BUZZER2_PIN, buzzerState ? HIGH : LOW);
      lastBuzzerToggle = millis();
    }
  } else {
    digitalWrite(BUZZER2_PIN, LOW);
    buzzerState = false;
  }

  // 광고 데이터에 부저 상태 포함시켜 송출 (매 루프마다 갱신)
  String advStr = String("B:") + (shouldBuzz ? "B" : "N");
  BLEAdvertisementData advData;
  advData.setName("Helmet-Receiver");
  advData.setManufacturerData(advStr);
  pAdvertising->setAdvertisementData(advData);
  pAdvertising->start();

  // 요약 데이터 시리얼 출력
  int avgRssi = 0;
  if (rssiValues.size() > 0) {
    long sum = 0;
    for (int rssi : rssiValues) sum += rssi;
    avgRssi = sum / rssiValues.size();
  }

  Serial.print("D:");
  Serial.print(avgRssi);  // Distance
  Serial.print(" / P:");
  Serial.print(pressureValue);  // Pressure
  Serial.print(" / G:(");
  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az);
  Serial.print(") / ");
  Serial.println(shouldBuzz ? "B" : "N");  // 부저 여부

  delay(100); // 조금 쉬기
}
```

#### 5-3 송신용 코드
```cpp
#### 5-3 송신용 코드

cpp
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

void setup() {
  Serial.begin(115200);
  Serial.println("BLE Advertiser Starting...");

  BLEDevice::init("ESP32_Advertiser");
  BLEDevice::setPower(ESP_PWR_LVL_P9);  // +9 dBm, 최대 출력 설정

  BLEServer *pServer = BLEDevice::createServer();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();

  BLEAdvertisementData advertisementData;
  advertisementData.setName("ESP32_BEACON");
  advertisementData.setManufacturerData("123456"); // 식별용

  pAdvertising->setAdvertisementData(advertisementData);
  pAdvertising->setScanResponse(false);
  pAdvertising->start();

  Serial.println("Advertising started at max TX power...");
}

void loop() {
  delay(1000);
}
```

#### 5-4 중계기 코드
```cpp
#### 5-4 중계기 코드
cpp
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

// 실물 보드의 고유 MAC 주소 고정 (필터링 설계)
const String WORKER1_MAC = "ec:e3:34:bf:80:9e";
const String WORKER2_MAC = "ec:e3:34:bf:e6:aa";

BLEScan* pBLEScan;
const int SCAN_TIME = 2;

struct WorkerData {
  bool dataReceived = false;
  int rssi = 0;
  String advData = "";
  char buzzerState = 'N'; 
};

WorkerData worker1, worker2;

unsigned long lastSendTime = 0;
const unsigned long SEND_INTERVAL = 1000; // 1초 전송 주기
bool sendWorker1Next = true;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String mac = advertisedDevice.getAddress().toString();
    mac.toLowerCase(); // 대소문자 무선 데이터 예외 처리

    if (mac == WORKER1_MAC || mac == WORKER2_MAC) {
      String adv = advertisedDevice.getManufacturerData().c_str();
      if (adv.length() == 0) {
        adv = advertisedDevice.toString().c_str();
      }

      int rssi = advertisedDevice.getRSSI();
      char buzzerChar = 'N';

      if (adv.length() > 0) {
        char lastChar = adv.charAt(adv.length() - 1);
        if (lastChar == 'B' || lastChar == 'N') {
          buzzerChar = lastChar;
        }
      }

      if (mac == WORKER1_MAC) {
        worker1.dataReceived = true;
        worker1.rssi = rssi;
        worker1.advData = adv;
        worker1.buzzerState = buzzerChar;
      } else {
        worker2.dataReceived = true;
        worker2.rssi = rssi;
        worker2.advData = adv;
        worker2.buzzerState = buzzerChar;
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  SerialBT.begin("RelayDeviceBT"); // 앱인벤터와 연동될 블루투스 이름
  
  BLEDevice::init("Relay-Device");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  BLEScanResults* results = pBLEScan->start(SCAN_TIME, false);
  if (results->getCount() == 0) {
    worker1.dataReceived = false;
    worker2.dataReceived = false;
  }
  pBLEScan->clearResults();

  // 1초마다 작업자 데이터를 교차 전송하여 데이터 과부하 및 튕김 방지
  if (millis() - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = millis();

    if (sendWorker1Next) {
      if (worker1.dataReceived) {
        String message = "작업자1: ";
        message += (worker1.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자1: 데이터 없음");
      }
    } else {
      if (worker2.dataReceived) {
        String message = "작업자2: ";
        message += (worker2.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자2: 데이터 없음");
      }
    }
    sendWorker1Next = !sendWorker1Next; // 플래그 토글
  }
  delay(100);
}
```

        </div>
      </details>
    </div>
</div>
</div>


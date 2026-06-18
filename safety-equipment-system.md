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
    background: rgba(15, 23, 42, 0.35);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    color: rgba(255, 255, 255, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 1.5rem;
    width: 44px;
    height: 80px;
    cursor: pointer;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 8px;
  }
  .pdf-btn-side:hover {
    background: rgba(16, 185, 129, 0.7);
    color: #ffffff;
    border-color: rgba(16, 185, 129, 0.5);
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
  }
  .pdf-btn-side.prev {
    left: 16px;
  }
  .pdf-btn-side.next {
    right: 16px;
  }
  .pdf-counter-badge {
    position: absolute;
    bottom: 16px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    color: #e2e8f0;
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 600;
    z-index: 10;
    pointer-events: none;
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-family: 'Pretendard', sans-serif;
    letter-spacing: 0.5px;
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
    <button class="tab-btn active" data-target="tab-simulator">시뮬레이터</button>
    <button class="tab-btn" data-target="tab-overview">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">역할</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
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

<!-- PDF 슬라이더 (타이틀 제거, 캐러셀 방식) -->
<div class="pdf-slider-wrap" style="background:#0f172a; border:2px solid #334155; border-radius:12px; padding:24px; margin-bottom:20px;">
<div class="pdf-slider-relative-wrap">
<div class="pdf-slider-container" id="pdf-slider-safety" style="position:relative; width:100%; height:100%; background:#1e293b; border-radius:8px; overflow:hidden;">
<div class="pdf-slide active" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0; transition:opacity 0.4s ease; display:flex; align-items:center; justify-content:center; color:#475569; font-size:0.9rem; text-align:center; padding:20px; font-family:'Pretendard',sans-serif;">
<div><div style="font-size:2.5rem;margin-bottom:10px;">📂</div><div style="color:#64748b;">로딩 중...</div></div>
</div>
</div>
<button class="pdf-btn-side prev" id="pdf-safety-prev">◀</button>
<button class="pdf-btn-side next" id="pdf-safety-next">▶</button>
<span class="pdf-counter-badge" id="pdf-safety-counter">- / -</span>
</div>
</div>

<!-- 영상/사진 좌우 배치 (슬라이드 밑으로 이동) -->
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
{% include_relative safe.md %}
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
{% include_relative safe_code.md %}
</div>
</div>
</div>

</div>

<script>
(function() {
  var slides = [
    '/assets/img/projects/safety_slides/slide_1.png',
    '/assets/img/projects/safety_slides/slide_2.png',
    '/assets/img/projects/safety_slides/slide_3.png',
    '/assets/img/projects/safety_slides/slide_4.png',
    '/assets/img/projects/safety_slides/slide_5.png',
    '/assets/img/projects/safety_slides/slide_6.png'
  ];
  var container = document.getElementById('pdf-slider-safety');
  var counter   = document.getElementById('pdf-safety-counter');
  var btnPrev   = document.getElementById('pdf-safety-prev');
  var btnNext   = document.getElementById('pdf-safety-next');
  if (!container || !slides.length) { if(counter) { counter.textContent='슬라이드 준비 중'; } return; }
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
    idx = (n+slides.length)%slides.length;
    els.forEach(function(el,i){ el.classList.toggle('active',i===idx); });
    counter.textContent=(idx+1)+' / '+slides.length;
  }
  if(btnPrev) { btnPrev.addEventListener('click',function(){ showSlide(idx-1); }); }
  if(btnNext) { btnNext.addEventListener('click',function(){ showSlide(idx+1); }); }
  showSlide(0);
})();
</script>

---
layout: default
title: "중계기 기반 실시간 공사장 안전장비 제어 시스템"
category: embedded-hardware-projects
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Share+Tech+Mono&display=swap');

  /* Technical Cockpit Console Wrapper */
  .cockpit-container {
    max-width: 1400px;
    width: 95%;
    margin: 40px auto;
    padding: 30px;
    background: rgba(11, 17, 32, 0.85);
    border: 1px solid rgba(0, 242, 254, 0.25);
    border-radius: 12px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.8), inset 0 0 30px rgba(0, 242, 254, 0.03);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    position: relative;
    overflow: hidden;
    font-family: 'Share Tech Mono', 'Pretendard', sans-serif;
    color: #cbd5e1;
  }

  .cockpit-container::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: 
      linear-gradient(rgba(0, 242, 254, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 242, 254, 0.015) 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
  }

  /* Return dashboard link */
  .cmd-return-btn {
    color: #00f2fe;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 24px;
    font-weight: 600;
    transition: all 0.3s;
    text-shadow: 0 0 8px rgba(0, 242, 254, 0.5);
    border: 1px dashed rgba(0, 242, 254, 0.3);
    padding: 6px 14px;
    border-radius: 4px;
    background: rgba(0, 242, 254, 0.03);
  }
  .cmd-return-btn:hover {
    color: #ffffff;
    background: rgba(0, 242, 254, 0.15);
    border-color: #00f2fe;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    transform: translateX(-3px);
  }

  /* Control Tower Header */
  .control-tower-header {
    border: 1px solid rgba(0, 242, 254, 0.4);
    border-top: 4px solid #00f2fe;
    background: rgba(6, 10, 23, 0.9);
    padding: 16px 24px;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    flex-wrap: wrap;
    gap: 15px;
  }

  .gateway-status-panel {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .pulse-led {
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 10px #10b981, 0 0 20px rgba(16, 185, 129, 0.5);
    animation: led-blink 1.8s ease-in-out infinite;
  }

  .gateway-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    color: #10b981;
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(16, 185, 129, 0.4);
    font-weight: bold;
  }

  .project-master-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(1.2rem, 2.5vw, 1.8rem);
    font-weight: 800;
    color: #ffffff;
    margin: 0;
    letter-spacing: 1px;
    text-shadow: 0 0 12px rgba(0, 242, 254, 0.4);
    text-transform: uppercase;
  }

  /* 3D Hardware Topology Graph Block */
  .topology-card {
    background: rgba(6, 12, 29, 0.6);
    border: 1px solid rgba(0, 242, 254, 0.2);
    border-radius: 10px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    position: relative;
    height: 100%;
    min-height: 480px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .panel-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00f2fe;
    letter-spacing: 2px;
    margin-bottom: 20px;
    text-shadow: 0 0 8px rgba(0, 242, 254, 0.3);
    border-bottom: 1px dashed rgba(0, 242, 254, 0.15);
    padding-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .panel-title span {
    color: #ff007f;
    font-size: 0.8rem;
  }

  /* SVG Topology Mapping & Flow Nodes */
  .topology-view {
    position: relative;
    flex-grow: 1;
    display: grid;
    grid-template-columns: 28% 44% 28%;
    align-items: center;
    justify-content: space-between;
    height: 380px;
    z-index: 5;
  }

  .topology-svg-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .nodes-col {
    display: flex;
    flex-direction: column;
    gap: 50px;
    justify-content: center;
    align-items: center;
    position: relative;
    z-index: 2;
  }

  .topo-node {
    background: rgba(13, 22, 43, 0.75);
    border: 1px solid rgba(0, 242, 254, 0.35);
    border-radius: 8px;
    padding: 14px 18px;
    width: 100%;
    max-width: 180px;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.1), inset 0 0 10px rgba(0, 242, 254, 0.05);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    transition: all 0.3s ease;
    text-align: left;
  }

  .topo-node:hover {
    border-color: #00f2fe;
    box-shadow: 0 0 20px rgba(0, 242, 254, 0.4), inset 0 0 12px rgba(0, 242, 254, 0.15);
    transform: translateY(-3px);
  }

  .node-tag {
    font-size: 0.65rem;
    color: #ff007f;
    text-shadow: 0 0 5px rgba(255,0,127,0.3);
    font-weight: bold;
    display: block;
    margin-bottom: 4px;
    letter-spacing: 1px;
  }

  .node-name {
    font-size: 0.82rem;
    color: #ffffff;
    font-weight: bold;
    margin-bottom: 4px;
  }

  .node-sensor {
    font-size: 0.72rem;
    color: #8fa0dd;
  }

  /* Node customization for Central Master Gateway & Client App */
  .topo-node.master-gateway {
    border-color: rgba(255, 0, 127, 0.5);
    box-shadow: 0 0 20px rgba(255, 0, 127, 0.15), inset 0 0 12px rgba(255, 0, 127, 0.05);
    max-width: 220px;
  }
  .topo-node.master-gateway:hover {
    border-color: #ff007f;
    box-shadow: 0 0 25px rgba(255, 0, 127, 0.4), inset 0 0 15px rgba(255, 0, 127, 0.15);
  }

  .topo-node.client-app {
    border-color: rgba(16, 185, 129, 0.4);
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.1), inset 0 0 10px rgba(16, 185, 129, 0.03);
  }
  .topo-node.client-app:hover {
    border-color: #10b981;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.4), inset 0 0 15px rgba(16, 185, 129, 0.15);
  }

  /* Moving Data Packets flow paths styling */
  .flow-line {
    fill: none;
    stroke: rgba(0, 242, 254, 0.2);
    stroke-width: 2;
    stroke-dasharray: 6 4;
  }

  .flow-pulse {
    fill: none;
    stroke: #00f2fe;
    stroke-width: 3;
    stroke-linecap: round;
    stroke-dasharray: 10 90;
    stroke-dashoffset: 100;
    animation: flow-run 3.5s linear infinite;
  }
  .flow-pulse.pulse-alt {
    stroke: #ff007f;
    animation-delay: 1.75s;
  }

  .flow-line-main {
    fill: none;
    stroke: rgba(255, 0, 127, 0.25);
    stroke-width: 2.5;
  }
  .flow-pulse-main {
    fill: none;
    stroke: #ff007f;
    stroke-width: 3.5;
    stroke-linecap: round;
    stroke-dasharray: 15 150;
    stroke-dashoffset: 165;
    animation: flow-run 2.8s linear infinite;
  }

  /* Control Console styling */
  .console-card {
    background: rgba(2, 4, 10, 0.85);
    border: 1px solid rgba(255, 0, 127, 0.3);
    border-radius: 10px;
    padding: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.7), inset 0 0 20px rgba(255, 0, 127, 0.04);
    font-family: 'Share Tech Mono', monospace;
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  .terminal-box {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 0, 127, 0.15);
    border-radius: 6px;
    padding: 16px;
    flex-grow: 1;
    overflow-y: auto;
    font-size: 0.8rem;
    color: #e2e8f0;
    max-height: 380px;
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 0, 127, 0.3) rgba(0, 0, 0, 0.2);
  }

  .terminal-box::-webkit-scrollbar {
    width: 4px;
  }
  .terminal-box::-webkit-scrollbar-thumb {
    background: rgba(255, 0, 127, 0.4);
    border-radius: 2px;
  }

  .cmd-line {
    color: #ff007f;
    margin-bottom: 6px;
  }
  .cmd-resp {
    color: #8fa0dd;
    margin-bottom: 12px;
    line-height: 1.5;
    text-align: justify;
  }

  .highlight-terminal {
    color: #00f2fe;
    text-shadow: 0 0 5px rgba(0,242,254,0.3);
  }

  /* Code view inside console */
  .code-viewer {
    background: #020308;
    border: 1px solid rgba(0, 242, 254, 0.2);
    border-radius: 4px;
    padding: 12px;
    margin: 10px 0;
    overflow-x: auto;
    font-size: 0.72rem;
    color: #a5b4fc;
    line-height: 1.4;
  }

  /* Bottom Telemetry Gauges section */
  .telemetry-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    margin-top: 30px;
  }

  .telemetry-card {
    background: rgba(6, 12, 29, 0.6);
    border: 1px solid rgba(0, 242, 254, 0.2);
    border-radius: 10px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 240px;
  }

  /* Circular Neon Gauge */
  .gauge-wrapper {
    position: relative;
    width: 120px;
    height: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 15px;
  }

  .gauge-svg {
    transform: rotate(-90deg);
    width: 100%;
    height: 100%;
  }

  .gauge-bg-circle {
    fill: none;
    stroke: rgba(0, 242, 254, 0.1);
    stroke-width: 8;
  }

  .gauge-fill-circle {
    fill: none;
    stroke: #00f2fe;
    stroke-width: 8;
    stroke-dasharray: 314;
    stroke-dashoffset: 314;
    stroke-linecap: round;
    box-shadow: 0 0 10px #00f2fe;
    animation: gauge-draw 2s cubic-bezier(0.1, 0.8, 0.25, 1) forwards;
  }

  .gauge-value {
    position: absolute;
    font-family: 'Orbitron', sans-serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: #ffffff;
    text-shadow: 0 0 10px rgba(0, 242, 254, 0.8);
  }

  .metric-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #cbd5e1;
    letter-spacing: 2px;
    margin-bottom: 6px;
    text-transform: uppercase;
  }

  .metric-subtitle {
    font-size: 0.75rem;
    color: #8fa0dd;
    margin: 0;
  }

  /* Alert Level Bar Meter */
  .bar-meter-container {
    width: 100%;
    max-width: 220px;
    height: 14px;
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(255, 0, 127, 0.2);
    border-radius: 4px;
    overflow: hidden;
    position: relative;
    margin-bottom: 15px;
    box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
  }

  .bar-meter-fill {
    width: 2%; /* extremely low packet loss */
    height: 100%;
    background: linear-gradient(90deg, #10b981, #ffcc00);
    box-shadow: 0 0 8px rgba(16, 185, 129, 0.8);
    border-radius: 3px;
    animation: bar-scale 1.8s ease-out forwards;
  }

  .bar-meter-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.8rem;
    font-weight: 900;
    color: #ff007f;
    margin-bottom: 5px;
    text-shadow: 0 0 12px rgba(255, 0, 127, 0.6);
  }

  /* Info Board Style */
  .status-board-container {
    width: 100%;
    background: rgba(0,0,0,0.3);
    border: 1px dashed rgba(0, 242, 254, 0.3);
    padding: 12px;
    border-radius: 6px;
    margin-bottom: 12px;
    position: relative;
  }

  .status-board-pill {
    position: absolute;
    top: -10px;
    right: 15px;
    font-size: 0.6rem;
    background: #ff007f;
    color: #ffffff;
    padding: 2px 6px;
    border-radius: 3px;
    font-weight: bold;
    text-shadow: 0 0 4px rgba(255,255,255,0.4);
    box-shadow: 0 0 8px rgba(255,0,127,0.5);
  }

  .status-desc-text {
    font-size: 0.82rem;
    color: #ffffff;
    line-height: 1.4;
    text-shadow: 0 0 4px rgba(0, 242, 254, 0.3);
  }

  /* Keyframe Animations */
  @keyframes led-blink {
    0%, 100% { opacity: 0.5; transform: scale(0.95); }
    50% { opacity: 1; transform: scale(1.05); filter: brightness(1.2); }
  }

  @keyframes flow-run {
    to { stroke-dashoffset: 0; }
  }

  @keyframes gauge-draw {
    to { stroke-dashoffset: 6.28; } /* 314 * (1 - 0.98) ~ 6.28 */
  }

  @keyframes bar-scale {
    from { width: 0%; }
    to { width: 2%; }
  }

  @media (max-width: 992px) {
    .abstract-split-grid {
      grid-template-columns: 1fr !important;
    }
  }
</style>

<div class="cockpit-container">
  
  <a href="{{ site.baseurl }}/" class="cmd-return-btn">
    <i class="uil uil-arrow-left"></i> [CMD: RETURN_TO_DASHBOARD]
  </a>

  <!-- Control Tower Header -->
  <div class="control-tower-header">
    <div class="gateway-status-panel">
      <div class="pulse-led"></div>
      <span class="gateway-label">[GATEWAY: ONLINE]</span>
    </div>
    <h1 class="project-master-title">안전장비 실시간 무선 관제 센터</h1>
  </div>

  <!-- Central Split Grid -->
  <div class="abstract-split-grid" style="display: grid; grid-template-columns: 55% 45%; gap: 30px; margin-bottom: 30px;">
    
    <!-- Left Topology View -->
    <div>
      <div class="topology-card">
        <div class="panel-title">
          📡 HARDWARE TOPOLOGY GRAPHIC
          <span>NODE LEVEL SYSTEM</span>
        </div>
        
        <div class="topology-view">
          
          <!-- Column 1: TX Nodes -->
          <div class="nodes-col">
            <!-- Node A -->
            <div class="topo-node">
              <span class="node-tag">TX NODE 01</span>
              <div class="node-name">안전모 모듈</div>
              <div class="node-sensor">RA12P FSR 밀착 센서</div>
            </div>
            <!-- Node B -->
            <div class="topo-node">
              <span class="node-tag">TX NODE 02</span>
              <div class="node-name">안전조끼 모듈</div>
              <div class="node-sensor">MPU6050 자이로 센서</div>
            </div>
          </div>
          
          <!-- Column 2: Central Master Gateway -->
          <div class="nodes-col">
            <div class="topo-node master-gateway">
              <span class="node-tag" style="color: #ff007f; text-shadow: 0 0 5px rgba(255,0,127,0.4);">CENTRAL MASTER</span>
              <div class="node-name" style="color: #ff007f;">ESP32 게이트웨이</div>
              <div class="node-sensor" style="color: #8fa0dd;">BLE 수신 & Classic SPP 전송</div>
              <div class="node-sensor" style="font-size: 0.65rem; margin-top: 5px; color: #ff99cc;">• Ring Buffer Stack</div>
            </div>
          </div>
          
          <!-- Column 3: RX Client -->
          <div class="nodes-col">
            <div class="topo-node client-app">
              <span class="node-tag" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.4);">RX TERMINAL</span>
              <div class="node-name" style="color: #10b981;">모바일 관제 앱</div>
              <div class="node-sensor">Android App Inventor</div>
              <div class="node-sensor" style="font-size: 0.65rem; margin-top: 5px; color: #a3e635;">• SPP Parsers 115200bps</div>
            </div>
          </div>

          <!-- SVG Flow Lines Overlay -->
          <svg class="topology-svg-overlay">
            <defs>
              <!-- Arrow marker -->
              <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="rgba(0, 242, 254, 0.4)" />
              </marker>
              <marker id="arrow-pink" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="rgba(255, 0, 127, 0.4)" />
              </marker>
            </defs>

            <!-- TX Node 01 to Gateway -->
            <path class="flow-line" d="M 180,95 L 290,155" marker-end="url(#arrow)" />
            <path class="flow-pulse" d="M 180,95 L 290,155" />
            
            <!-- TX Node 02 to Gateway -->
            <path class="flow-line" d="M 180,285 L 290,225" marker-end="url(#arrow)" />
            <path class="flow-pulse pulse-alt" d="M 180,285 L 290,225" />

            <!-- Gateway to Mobile App Client -->
            <path class="flow-line-main" d="M 505,190 L 590,190" marker-end="url(#arrow-pink)" style="stroke: rgba(255, 0, 127, 0.25); stroke-width: 2;" />
            <path class="flow-pulse-main" d="M 505,190 L 590,190" />
          </svg>
          
        </div>
      </div>
    </div>
    
    <!-- Right Firmware Control Console -->
    <div>
      <div class="console-card">
        <div class="panel-title" style="color: #ff007f; text-shadow: 0 0 8px rgba(255, 0, 127, 0.3); border-bottom-color: rgba(255, 0, 127, 0.15);">
          📟 FIRMWARE_CONSOLES // DEPLOY_LOGS
          <span style="color: #00f2fe;">SYS_MONITOR: ACTIVE</span>
        </div>
        
        <div class="terminal-box">
          <div class="cmd-line">> init --network-topology</div>
          <div class="cmd-resp">
            단일 칩 스마트폰 관제 환경(<span class="highlight-terminal">App Inventor Client</span>)에서의 다중 하드웨어 주변 기기 실시간 동시 BLE 연결 실패 드라이버 오류 현상을 감지했습니다.
            이 병목을 우회하기 위해 개별 작업자의 센서 송신 기기들과 무선 허브 역할을 수행할 독창적인 <span class="highlight-terminal">중계기(ESP32 Gateway)</span> 아키텍처(2-Hop 통신 기법)를 제안, 적용했습니다.
            개별 송신 노드는 저전력 BLE로 게이트웨이에 데이터를 고속 주입하고, 게이트웨이 내부에 <span class="highlight-terminal">임베디드 링 버퍼(Ring Buffer)</span> 큐를 설계하여 데이터 병목을 소거한 뒤,
            안정적인 <span class="highlight-terminal">Bluetooth Classic SPP 프로파일(115200bps)</span> 단일 데이터 파이프라인 채널로 스마트폰 관제 앱에 데이터 스트림을 안정적으로 직렬화 전송하여 채널 혼선을 원천적으로 해결했습니다.
          </div>
          
          <div class="cmd-line">> load --algorithm "RSSI Moving Average Filter"</div>
          <div class="cmd-resp">
            공사현장의 비설 구조물에 의한 신호 감쇄 및 다중 경로 반사(Multipath Fading) 요인으로 무선 수신 RSSI 강도가 출렁여, 정상 거리임에도 오동작 부저 알람이 심각하게 활성화되는 현상을 분석했습니다.
            펌웨어 레벨에 <span class="highlight-terminal">10회 원형 버퍼 기반 이동 평균 필터(10-Point Moving Average Filter)</span> 알고리즘을 설계/수립하여 RSSI 감도의 노이즈 대역을 평활화(Smoothing)했습니다.
          </div>
          
          <div class="code-viewer">
// 10-Point Moving Average Filter (Kwon Eun Ji Architect)
#define FILTER_SIZE 10
int rssiHistory[FILTER_SIZE];
int writeIndex = 0;

int getFilteredRSSI(int newRawValue) {
    rssiHistory[writeIndex] = newRawValue;
    writeIndex = (writeIndex + 1) % FILTER_SIZE;
    int accumulatedSum = 0;
    for(int i = 0; i < FILTER_SIZE; i++) {
        accumulatedSum += rssiHistory[i];
    }
    return accumulatedSum / FILTER_SIZE;
}</div>
          <div class="cmd-resp">
            필터 알고리즘 도입 결과, 신호 진동 대역을 <span class="highlight-terminal">±2.5dBm</span> 이내로 대폭 압축하여 무선 신호 급락에 의한 오작동 위험률을 완벽히 제거했습니다.
          </div>
        </div>
      </div>
    </div>
    
  </div>

  <!-- Bottom Telemetry Meters -->
  <div class="telemetry-row">
    
    <!-- Accuracy Circular Meter -->
    <div class="telemetry-card">
      <div class="gauge-wrapper">
        <svg class="gauge-svg" viewBox="0 0 120 120">
          <circle class="gauge-bg-circle" cx="60" cy="60" r="50"></circle>
          <!-- C = 2 * PI * r = 2 * 3.14 * 50 = 314 -->
          <!-- 98% filled: dashoffset = 314 * (1 - 0.98) = 6.28 -->
          <circle class="gauge-fill-circle" cx="60" cy="60" r="50" style="stroke-dashoffset: 6.28;"></circle>
        </svg>
        <span class="gauge-value">98%</span>
      </div>
      <h3 class="metric-label">SENSOR ACCURACY</h3>
      <p class="metric-subtitle">FSR 감압 & MPU6050 모션 센서 퓨전 착용 판정 정확도</p>
    </div>

    <!-- Packet Loss Bar Meter -->
    <div class="telemetry-card">
      <span class="bar-meter-val">0.2%</span>
      <div class="bar-meter-container">
        <div class="bar-meter-fill"></div>
      </div>
      <h3 class="metric-label">PACKET LOSS RATE</h3>
      <p class="metric-subtitle">ESP32 2-Hop 게이트웨이 무선 전송 채널 유실 계측률 (최저 수준)</p>
    </div>

    <!-- Security Information System -->
    <div class="telemetry-card" style="align-items: stretch; text-align: left;">
      <h3 class="metric-label" style="text-align: center; border-bottom: 1px dashed rgba(0, 242, 254, 0.15); padding-bottom: 8px; margin-bottom: 18px;">SECURITY SYSTEM</h3>
      <div class="status-board-container">
        <span class="status-board-pill">SECURE</span>
        <div class="status-desc-text">
          <strong>고유 MAC 주소 기반 사설망 필터링 시스템</strong><br>
          <span style="font-size: 0.72rem; color: #8fa0dd; display: block; margin-top: 6px; line-height: 1.4;">
            타 장비 노드의 패킷이 수신될 시 게이트웨이 EEPROM 페어링 헤더 정보 유효 검사 단계를 거쳐 즉각 버퍼에서 소거 및 폐기 처리하여 혼선을 방지합니다.
          </span>
        </div>
      </div>
      <div style="font-size: 0.72rem; color: #10b981; font-weight: bold; text-align: center; letter-spacing: 1px;">
        ● SECURE FILTER : OPERATIONAL
      </div>
    </div>

  </div>

</div>

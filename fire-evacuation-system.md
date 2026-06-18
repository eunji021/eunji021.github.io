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
    fill: none; stroke: #38bdf8; stroke-width: 12; stroke-linecap: round; stroke-linejoin: round;
    stroke-dasharray: 30 20; filter: drop-shadow(0 0 10px #38bdf8);
    opacity: 0; transition: opacity 0.3s; pointer-events: none;
  }
  .route-path.active {
    opacity: 1; animation: flowWave 0.5s linear infinite;
  }
  @keyframes flowWave { from { stroke-dashoffset: 50; } to { stroke-dashoffset: 0; } }
  
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
          
          <!-- 2. 대피 유도선 (Dijkstra Path) -->
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


  fireDrag.addEventListener  dashConsole.scrollTop = dashConsole.scrollHeight;
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

    zones.forEach(z => {
      document.getElementById('bg-' + z).classList.remove('fire');
      document.getElementById('wall-' + z).classList.remove('fire');
      if(document.getElementById('route-' + z)) {
        document.getElementById('route-' + z).classList.remove('active');
      }
    });
    document.getElementById('wall-c-mid').classList.remove('fire');
    document.getElementById('bg-c-mid').classList.remove('fire');
    
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

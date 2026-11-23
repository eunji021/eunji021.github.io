<style>
  .intro-section { margin-bottom: 36px; }
  .intro-section-title {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #10b981;
    font-size: 1.25rem;
    font-weight: 700;
    border-bottom: 2px solid rgba(16, 185, 129, 0.25);
    padding-bottom: 12px;
    margin-bottom: 20px;
    font-family: 'Pretendard', sans-serif;
  }
  
  /* Main Role Badge */
  .role-main-badge {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 20px;
  }
  .role-main-tag {
    background: #10b981;
    color: #0f172a;
    font-size: 0.8rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
    white-space: nowrap;
  }
  .role-main-text {
    color: #f1f5f9;
    font-size: 1.05rem;
    font-weight: 600;
  }

  /* Role Cards */
  .role-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 16px;
    margin-bottom: 10px;
  }
  .role-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 20px 22px;
    transition: border-color 0.2s, transform 0.2s;
  }
  .role-card:hover {
    border-color: rgba(16, 185, 129, 0.5);
    transform: translateY(-2px);
  }
  .role-card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  }
  .role-card-num {
    color: #10b981;
    font-family: 'Consolas', monospace;
    font-weight: 800;
    font-size: 1.1rem;
    background: rgba(16, 185, 129, 0.12);
    padding: 2px 8px;
    border-radius: 6px;
  }
  .role-card-title {
    color: #e2e8f0;
    font-weight: 700;
    font-size: 1.0rem;
  }
  .role-list {
    margin: 0;
    padding-left: 20px;
    color: #94a3b8;
    font-size: 0.92rem;
    line-height: 1.75;
  }
  .role-list li {
    margin-bottom: 8px;
  }
  .role-list li:last-child {
    margin-bottom: 0;
  }
  .role-list code {
    background: #0f172a;
    color: #38bdf8;
    border: 1px solid #334155;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
    font-family: 'Consolas', monospace;
  }

  /* Trouble Shooting (Issue Boxes) */
  .intro-issue-box {
    background: #1e293b;
    border: 1px solid #334155;
    border-left: 4px solid #f59e0b;
    border-radius: 0 10px 10px 0;
    padding: 18px 22px;
    margin-bottom: 16px;
    font-family: 'Pretendard', sans-serif;
    transition: border-color 0.2s;
  }
  .intro-issue-box:hover {
    border-color: #475569;
    border-left-color: #f59e0b;
  }
  .issue-title {
    color: #f1f5f9;
    font-weight: 700;
    font-size: 1.0rem;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .issue-badge {
    background: rgba(245, 158, 11, 0.15);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #f59e0b;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Consolas', monospace;
  }
  .issue-row {
    display: flex;
    gap: 12px;
    margin-bottom: 8px;
    align-items: baseline;
    font-size: 0.92rem;
    line-height: 1.65;
  }
  .issue-row:last-child {
    margin-bottom: 0;
  }
  .issue-label {
    font-size: 0.78rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    min-width: 68px;
    text-align: center;
    white-space: nowrap;
  }
  .issue-label.red {
    background: rgba(239, 68, 68, 0.15);
    color: #f87171;
    border: 1px solid rgba(239, 68, 68, 0.3);
  }
  .issue-label.yellow {
    background: rgba(245, 158, 11, 0.15);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.3);
  }
  .issue-label.green {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.3);
  }
  .issue-desc {
    color: #cbd5e1;
    flex: 1;
  }
  .issue-desc code {
    background: #0f172a;
    color: #38bdf8;
    border: 1px solid #334155;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
    font-family: 'Consolas', monospace;
  }
</style>

<div style="padding: 30px 0; font-family: 'Pretendard', sans-serif;">
  <!-- 3. 나의 역할 -->
  <div class="intro-section">
    <div class="intro-section-title">👤 3. 나의 역할</div>
    
    <div class="role-main-badge">
      <span class="role-main-tag">핵심 담당</span>
      <span class="role-main-text">모바일 관제 어플리케이션(앱인벤터) 구현 및 무선 통신 연결·데이터 설계</span>
    </div>

    <div class="role-cards-grid">
      <div class="role-card">
        <div class="role-card-header">
          <span class="role-card-num">01</span>
          <span class="role-card-title">1. 모바일 관제 어플리케이션(앱인벤터) 구현</span>
        </div>
        <ul class="role-list">
          <li>관리자가 스마트폰으로 현장 상황을 볼 수 있도록 표 형태의 화면을 디자인하고, 들어오는 데이터를 제 칸에 뿌려주는 블록 코딩 전체를 전담함.</li>
        </ul>
      </div>

      <div class="role-card">
        <div class="role-card-header">
          <span class="role-card-num">02</span>
          <span class="role-card-title">2. 무선 통신 연결 및 데이터 설계</span>
        </div>
        <ul class="role-list">
          <li>메인 중계기 기기와 스마트폰 앱 사이에 주고받을 블루투스(BLE) 데이터 형태를 직접 정의하고 연동 테스트를 진행함.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 5. 개발 과정 중 기술적 과제 및 극복 -->
  <div class="intro-section">
    <div class="intro-section-title">🔧 5. 개발 과정 중 기술적 과제 및 극복</div>

    <div class="intro-issue-box">
      <div class="issue-title"><span class="issue-badge">Issue 01</span> 문제 1. 여러 대의 기기를 앱에 동시에 연결할 수 없는 한계 해결</div>
      <div class="issue-row"><span class="issue-label red">문제 상황</span><span class="issue-desc">현장 작업자가 여러 명이라 안전모마다 독립된 송신 기기가 들어가야 했음. 하지만 앱인벤터 구조상 스마트폰 하나에 여러 개의 블루투스 기기를 동시에 안정적으로 직접 연결하는 것이 불가능했음.</span></div>
      <div class="issue-row"><span class="issue-label green">해결 방법</span><span class="issue-desc">스마트폰 앱에서 기기 여러 개를 직접 잡는 방식을 포기함. 작업자들의 기기 신호를 한곳으로 모아줄 <strong>'메인 중계기(ESP32)'</strong>를 중간에 하나 더 두는 방식을 냈음. 각 작업자의 기기가 보낸 신호를 중간 중계기가 다 받아낸 뒤, 스마트폰 앱에는 이 중계기 1대만 연결해서 데이터를 한 번에 밀어 넣어주는 통신 구조를 만들어 문제를 해결함.</span></div>
    </div>

    <div class="intro-issue-box">
      <div class="issue-title"><span class="issue-badge">Issue 02</span> 문제 2. 들어오는 데이터가 섞이고 뭉개지는 오류 해결</div>
      <div class="issue-row"><span class="issue-label red">문제 상황</span><span class="issue-desc">중간 중계기 한 대가 여러 명의 데이터를 모아서 스마트폰 앱으로 한꺼번에 던지다 보니, 앱인벤터 쪽에서 이 데이터가 누구의 데이터인지 구분을 못 해 화면에 엉뚱한 값이 찍히거나 글자가 깨지는 현상이 생김.</span></div>
      <div class="issue-row"><span class="issue-label green">해결 방법</span><span class="issue-desc">데이터를 보낼 때 무작정 보내지 않고 <code>[작업자 번호/현재 위치/장비 착용 상태]</code> 순서로 데이터 사이에 슬래시 나 쉼표 같은 약속된 기호를 넣어서 패킷을 묶어 보내도록 수정함. 앱인벤터 블록 코딩에서는 문자열 분리(Split) 블록을 사용해 들어온 데이터를 기호 기준으로 똑똑하게 쪼갠 뒤, 화면의 <code>작업자1</code>, <code>작업자2</code> 칸에 정확히 찾아 들어가도록 로직을 짜서 데이터가 섞이는 문제를 잡았음.</span></div>
    </div>

    <div class="intro-issue-box">
      <div class="issue-title"><span class="issue-badge">Issue 03</span> 문제 3. 쉴 새 없이 들어오는 신호로 인한 화면 멈춤 현상 해결</div>
      <div class="issue-row"><span class="issue-label red">문제 상황</span><span class="issue-desc">여러 명의 데이터가 블루투스를 통해 실시간으로 너무 자주 들어오다 보니, 앱인벤터 화면이 버퍼링을 버티지 못하고 수시로 멈추거나 앱이 강제로 꺼지는 현상이 발생함.</span></div>
      <div class="issue-row"><span class="issue-label green">해결 방법</span><span class="issue-desc">무조건 신호를 계속 쏘는 방식 대신, 주기를 1~2초 간격으로 조절하고 평소에는 조용하다가 작업자가 안전모를 벗거나 쓰러지는 등의 '상태 변화'가 생겼을 때만 즉시 신호를 쏘도록 송신 방식을 바꿨음. 데이터가 들어오는 통로의 부하를 줄여주어 앱이 끊김 없이 부드럽게 작동하도록 완성함.</span></div>
    </div>

    <div class="intro-issue-box">
      <div class="issue-title"><span class="issue-badge">Issue 04</span> 문제 4. 중계기(Master)의 다중 데이터 수신 병목 및 유실 현상 해결</div>
      <div class="issue-row"><span class="issue-label red">문제 상황</span><span class="issue-desc">각 작업자의 기기(Slave)들이 중계기(Master) 한 대를 향해 동시에 블루투스 신호를 보내다 보니, 데이터가 같은 시간에 겹쳐서 들어올 때 신호가 충돌하여 일부 작업자의 상태 데이터가 앱으로 전달되지 못하고 사라지는(유실) 현상이 생김.</span></div>
      <div class="issue-row"><span class="issue-label green">해결 방법</span><span class="issue-desc">중계기(ESP32) 펌웨어 코드를 직접 수정하여 통신 안정성을 높였음. 각 작업자의 기기들이 무작작 신호를 던지지 않고, 중계기가 <code>작업자1 신호 줘</code>, <code>작업자2 신호 줘</code> 하는 식으로 순서대로 신호를 요청하고 받아오는 수신 로직을 중계기 코드로 구현함. 또한, 들어온 데이터가 겹치더라도 안전하게 임시 보관했다가 순서대로 앱에 보내주도록 중계기 내부에 데이터 버퍼링 구조를 짜넣어 데이터가 중간에 날아가는 문제를 완벽히 해결함.</span></div>
    </div>
  </div>
</div>

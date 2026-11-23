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

    /* 프로젝트 C 시뮬레이터 CSS (클린 스마트폰 UI) */
  .sim-container {
    width: 100%; min-height: 650px;
    background: transparent;
    display: flex; align-items: center; justify-content: center; position: relative;
    margin-bottom: 20px;
  }

  .sim-phone {
    width: 340px; height: 680px; background: #fff;
    border-radius: 40px; border: 12px solid #1e293b;
    position: relative; overflow: hidden; font-family: 'Pretendard', sans-serif;
    box-shadow: 0 25px 50px rgba(0,0,0,0.5); z-index: 5;
    display: flex; flex-direction: column;
  }
  /* 노치 */
  .sim-phone::before {
    content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%);
    width: 130px; height: 30px; background: #1e293b; border-radius: 0 0 15px 15px; z-index: 50;
  }
  /* 하단 바 */
  .sim-phone::after {
    content: ''; position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%);
    width: 120px; height: 5px; background: rgba(0,0,0,0.3); border-radius: 5px; z-index: 50;
  }

  /* 카메라 뷰 (기본 화면) */
  .camera-view {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: url('/open.png') center/cover no-repeat, #000;
    transition: opacity 0.4s ease-out; z-index: 10;
  }
  
  .crosshair {
    position: absolute; top: 45%; left: 50%; transform: translate(-50%, -50%);
    width: 220px; height: 220px; border: 1px solid rgba(255,255,255,0.6);
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .crosshair::before, .crosshair::after { content: ''; position: absolute; background: rgba(255,255,255,0.8); }
  .crosshair::before { top: 50%; left: 45%; width: 10%; height: 1px; }
  .crosshair::after { left: 50%; top: 45%; height: 10%; width: 1px; }
  
  .camera-ui-top {
    position: absolute; top: 40px; width: 100%; display: flex; justify-content: space-between; padding: 0 20px; color: white;
  }
  
  /* 셔터 영역 */
  .shutter-area {
    position: absolute; bottom: 0; left: 0; width: 100%; height: 130px;
    background: rgba(0,0,0,0.6); display: flex; align-items: center; justify-content: center; z-index: 20;
  }
  .shutter-btn {
    width: 70px; height: 70px; background: #fff; border-radius: 50%; border: 4px solid #cbd5e1;
    cursor: pointer; transition: transform 0.1s, background 0.2s; display: flex; align-items: center; justify-content: center;
  }
  .shutter-btn:active { transform: scale(0.9); background: #f1f5f9; }
  .shutter-btn::inner { content: ''; width: 54px; height: 54px; background: #fff; border-radius: 50%; border: 1px solid #e2e8f0; }

  /* 플래시 이펙트 */
  .camera-flash {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: white; opacity: 0; z-index: 40; pointer-events: none;
  }
  .camera-flash.fire { animation: flashAnim 0.3s ease-out; }
  @keyframes flashAnim { 0% { opacity: 1; } 100% { opacity: 0; } }

  /* 국가 문화재청 Mock UI 화면 */
  .guide-ui {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: #f8fafc; z-index: 11; opacity: 0; pointer-events: none; transition: opacity 0.4s;
    display: flex; flex-direction: column; overflow-y: auto; overflow-x: hidden; scrollbar-width: none;
  }
  .guide-ui.active { opacity: 1; pointer-events: auto; }
  
  .mock-header {
    width: 100%; padding: 40px 15px 15px 15px; background: #fff; border-bottom: 1px solid #e2e8f0;
    display: flex; align-items: center; justify-content: center; position: sticky; top: 0; z-index: 20;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  }
  .mock-header-logo {
    font-size: 1.1rem; font-weight: 800; color: #0f172a; letter-spacing: -0.5px;
  }
  .mock-header-logo span { color: #b91c1c; } /* 포인트 컬러 */

  .guide-content { padding: 20px; flex: 1; }
  
  .guide-img { width: 100%; height: 200px; background: #e2e8f0; border-radius: 8px; margin-bottom: 20px; overflow: hidden; }
  .guide-img img { width: 100%; height: 100%; object-fit: cover; }
  
  .badge { display: inline-block; padding: 4px 10px; background: #b91c1c; color: white; font-size: 0.75rem; font-weight: bold; border-radius: 4px; margin-bottom: 10px; }
  .guide-title { color: #0f172a; font-size: 1.6rem; font-weight: 800; margin-bottom: 8px; letter-spacing: -0.5px; line-height: 1.2; }
  .guide-sub { color: #64748b; font-size: 0.9rem; margin-bottom: 20px; border-bottom: 1px solid #e2e8f0; padding-bottom: 15px; }
  
  .guide-desc { color: #334155; font-size: 0.95rem; line-height: 1.7; margin-bottom: 30px; text-align: justify; }
  
  .info-table { width: 100%; border-collapse: collapse; margin-bottom: 80px; }
  .info-table th, .info-table td { padding: 12px 10px; border-bottom: 1px solid #e2e8f0; font-size: 0.9rem; }
  .info-table th { background: #f1f5f9; text-align: left; color: #475569; width: 35%; font-weight: 600; }
  .info-table td { color: #0f172a; }

  .reset-btn-wrap {
    position: sticky; bottom: 0; left: 0; width: 100%; padding: 15px 20px 25px 20px; background: linear-gradient(to top, rgba(255,255,255,1) 70%, rgba(255,255,255,0)); z-index: 20;
  }
  .reset-btn { width: 100%; background: #0f172a; color: white; border: none; padding: 15px; border-radius: 12px; font-weight: bold; font-size: 1rem; cursor: pointer; transition: background 0.2s; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
  .reset-btn:hover { background: #1e293b; }

</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-simulator">시뮬레이터</button>
    <button class="tab-btn" data-target="tab-intro">프로젝트 설명</button>
  </div>

  <!-- 체험 시뮬레이터 탭 -->
  <div id="tab-simulator" class="tab-content active">
    <div class="sim-container">
      
      <!-- 스마트폰 단독 UI -->
      <div class="sim-phone">
        
        <!-- 1. 카메라 대기 화면 -->
        <div class="camera-view" id="camera-view">
          <div class="camera-ui-top">
            <span style="font-size: 1.2rem;">⚡</span>
            <span style="font-size: 0.9rem; font-weight: bold; background: rgba(0,0,0,0.5); padding: 2px 10px; border-radius: 10px;">AI LENS</span>
            <span style="font-size: 1.2rem;">⚙️</span>
          </div>
          <div class="crosshair">
            <div style="position: absolute; top: -5px; left: -5px; width: 20px; height: 20px; border-top: 2px solid #fff; border-left: 2px solid #fff;"></div>
            <div style="position: absolute; top: -5px; right: -5px; width: 20px; height: 20px; border-top: 2px solid #fff; border-right: 2px solid #fff;"></div>
            <div style="position: absolute; bottom: -5px; left: -5px; width: 20px; height: 20px; border-bottom: 2px solid #fff; border-left: 2px solid #fff;"></div>
            <div style="position: absolute; bottom: -5px; right: -5px; width: 20px; height: 20px; border-bottom: 2px solid #fff; border-right: 2px solid #fff;"></div>
          </div>
          <p style="position: absolute; bottom: 150px; width: 100%; text-align: center; color: white; font-size: 0.9rem; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">유적지를 스캔하려면 셔터를 누르세요</p>
          
          <div class="shutter-area">
            <button class="shutter-btn" id="shutter-btn">
              <div style="width: 56px; height: 56px; background: white; border-radius: 50%; border: 2px solid #cbd5e1;"></div>
            </button>
          </div>
        </div>

        <!-- 2. 플래시 오버레이 -->
        <div class="camera-flash" id="camera-flash"></div>

        <!-- 3. 유적지 가이드 (국가 문화재청 Mock UI) -->
        <div class="guide-ui" id="guide-ui">
          <div class="mock-header">
            <div class="mock-header-logo">🏛️ 국가문화유산포털 <span>K-Heritage</span></div>
          </div>
          
          <div class="guide-content">
            <div class="badge">국보 제11호</div>
            <div class="guide-title">익산 미륵사지 석탑</div>
            <div class="guide-sub">Iksan Mireuksaji Seoktap (Stone Pagoda)</div>
            
            <div class="guide-img">
              <!-- 촬영한 open.png 이미지가 상단에 헤더 이미지로 매핑됨 -->
              <img src="/open.png" alt="미륵사지 석탑" onerror="this.src='https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&w=400&q=80'">
            </div>
            
            <div class="guide-desc">
              이 탑은 백제 무왕(재위 600∼641) 대에 건립된 것으로 추정되며, 우리나라에 남아 있는 가장 오래되고 거대한 석탑입니다. 목조건축의 기법을 돌로 구현해 낸 독특한 양식을 지니고 있어, 백제 건축 문화의 뛰어난 수준을 보여주는 핵심 유적입니다.
            </div>
            
            <table class="info-table">
              <tr><th>지정일</th><td>1962.12.20</td></tr>
              <tr><th>소재지</th><td>전북특별자치도 익산시 금마면</td></tr>
              <tr><th>시대</th><td>백제 시대</td></tr>
              <tr><th>분류</th><td>유적건조물 / 종교신앙</td></tr>
            </table>
          </div>
          
          <div class="reset-btn-wrap">
            <button class="reset-btn" id="btn-reset">다시 촬영하기</button>
          </div>
        </div>
        
      </div>
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
    });
  });

  // Simulator Elements
  const shutterBtn = document.getElementById('shutter-btn');
  const cameraFlash = document.getElementById('camera-flash');
  const cameraView = document.getElementById('camera-view');
  const guideUi = document.getElementById('guide-ui');
  
  // Audio effect (optional if browser allows, otherwise just visual)
  // const shutterSound = new Audio('https://www.soundjay.com/camera/camera-shutter-click-01.mp3');

  shutterBtn.addEventListener('click', () => {
    // 1. 찰칵 플래시 효과
    cameraFlash.classList.add('fire');
    // try { shutterSound.play(); } catch(e) {}
    
    // 2. 0.2초 뒤 화면 전환 시작 (자연스러운 딜레이)
    setTimeout(() => {
      cameraView.style.opacity = '0';
      cameraView.style.pointerEvents = 'none';
      
      setTimeout(() => {
        guideUi.classList.add('active');
      }, 300);
      
    }, 200);
    
    // 플래시 애니메이션 클래스 제거 (재사용 위해)
    setTimeout(() => {
      cameraFlash.classList.remove('fire');
    }, 400);
  });
  
  // 리셋 버튼
  const btnReset = document.getElementById('btn-reset');
  btnReset.addEventListener('click', () => {
    guideUi.classList.remove('active');
    setTimeout(() => {
      cameraView.style.opacity = '1';
      cameraView.style.pointerEvents = 'auto';
      // 스크롤 맨 위로 초기화
      guideUi.scrollTop = 0;
    }, 400);
  });
});
</script>

  <!-- ===================== 프로젝트 설명 탭 ===================== -->
  <div id="tab-intro" class="tab-content">
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
      .intro-desc-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px 22px;
        margin-bottom: 16px;
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.75;
        font-family: 'Pretendard', sans-serif;
      }
      .intro-subtitle {
        color: #f1f5f9;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
      }

      /* Architecture Visual Flow */
      .arch-flow-wrap {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
      }
      @media(max-width: 768px) {
        .arch-flow-wrap {
          flex-direction: column;
          gap: 10px;
        }
        .arch-arrow {
          transform: rotate(90deg);
        }
      }
      .arch-step-card {
        flex: 1;
        background: #1e293b;
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 8px;
        padding: 14px 16px;
        text-align: center;
        color: #f1f5f9;
        font-weight: 700;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
      }
      .arch-arrow {
        color: #10b981;
        font-size: 1.4rem;
        font-weight: 800;
      }

      /* Role & Detail Cards Grid */
      .role-cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 16px;
        margin-bottom: 16px;
      }
      .role-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px 22px;
        transition: border-color 0.2s, transform 0.2s;
        font-family: 'Pretendard', sans-serif;
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
        font-size: 1.05rem;
        background: rgba(16, 185, 129, 0.12);
        padding: 2px 8px;
        border-radius: 6px;
      }
      .role-card-title {
        color: #e2e8f0;
        font-weight: 700;
        font-size: 0.98rem;
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
      .role-sublist {
        margin-top: 6px;
        padding-left: 18px;
        color: #cbd5e1;
        font-size: 0.88rem;
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

      /* Issue Boxes */
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

      /* Expectations Table */
      .expectations-table-wrap {
        overflow-x: auto;
        margin-top: 14px;
        margin-bottom: 18px;
        border-radius: 8px;
        border: 1px solid #334155;
      }
      .expectations-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.92rem;
        text-align: left;
      }
      .expectations-table th {
        background: #0f172a;
        color: #10b981;
        font-weight: 700;
        padding: 12px 16px;
        border-bottom: 2px solid rgba(16, 185, 129, 0.3);
        white-space: nowrap;
      }
      .expectations-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #334155;
        background: #1e293b;
        color: #cbd5e1;
      }
      .expectations-table tr:last-child td {
        border-bottom: none;
      }
      .expectations-table td:first-child {
        font-weight: 600;
        color: #f1f5f9;
        white-space: nowrap;
        border-right: 1px solid #334155;
      }

      /* Highlight Callout */
      .highlight-callout {
        background: rgba(56, 189, 248, 0.08);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-left: 4px solid #38bdf8;
        border-radius: 0 8px 8px 0;
        padding: 16px 20px;
        margin-top: 14px;
        color: #cbd5e1;
        font-size: 0.93rem;
        line-height: 1.7;
      }
      .highlight-callout strong {
        color: #38bdf8;
      }
    </style>

    <div style="padding: 30px 0; font-family: 'Pretendard', sans-serif;">
      
      <!-- 1. 프로젝트 배경 및 목표 -->
      <div class="intro-section">
        <div class="intro-section-title">🎯 1. 프로젝트 배경 및 목표</div>
        <div class="intro-desc-box">
          현장 안내판 접근의 불편함이나 전문 가이드 부재 상황을 해소하기 위해, 개별·가족 단위 관람객 및 학생 탐방객이 현장에서 유적지 사진을 촬영하면 AI 이미지 분석을 통해 유적지를 즉시 식별하고 국가유산포털 API와 연동하여 상세 정보를 제공하는 모바일 가이드 시스템입니다.
        </div>
        <div class="intro-desc-box">
          <div class="intro-subtitle">✨ 주요 기능</div>
          <ul class="role-list">
            <li><strong>앱 카메라 기반 실시간 유적지 이미지 촬영 및 연동</strong> (앱 인벤터 구동)</li>
            <li><strong>인공지능 모델을 활용한 10개 핵심 유적지 고정밀 분류</strong></li>
            <li><strong>식별된 유적지의 국가유산포털 데이터 자동 매핑 및 앱 내 상세 정보 표출</strong></li>
          </ul>
        </div>
      </div>

      <!-- 2. 시스템 아키텍처 및 작동 흐름 -->
      <div class="intro-section">
        <div class="intro-section-title">🏗️ 2. 시스템 아키텍처 및 작동 흐름</div>
        
        <!-- 전체 흐름 시각화 -->
        <div class="arch-flow-wrap">
          <div class="arch-step-card">
            <span>📷 [1. 관람객 사진 촬영]</span>
          </div>
          <div class="arch-arrow">→</div>
          <div class="arch-step-card">
            <span>🧠 [2. AI 분석 및 유적지 분류]</span>
          </div>
          <div class="arch-arrow">→</div>
          <div class="arch-step-card">
            <span>🏛️ [3. 국가유산포털 연동]</span>
          </div>
        </div>

        <!-- 세부 4단계 카드 그리드 -->
        <div class="role-cards-grid">
          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">STEP 1</span>
              <span class="role-card-title">입력 (Mobile App / Image Capture)</span>
            </div>
            <ul class="role-list">
              <li>MIT App Inventor로 개발한 모바일 앱에서 카메라 기능을 실행하여 유적지 이미지를 촬영</li>
              <li>촬영된 이미지를 AI 이미지 분석 모델의 입력 데이터로 전달</li>
            </ul>
          </div>

          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">STEP 2</span>
              <span class="role-card-title">분석 (AI Model / Image Classification)</span>
            </div>
            <ul class="role-list">
              <li>사전에 수집 및 전처리한 유적지 이미지 데이터셋을 기반으로 학습된 AI 모델을 활용</li>
              <li>입력된 이미지를 분석하여 사전에 정의된 10개 유적지 중 해당하는 대상을 분류</li>
            </ul>
          </div>

          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">STEP 3</span>
              <span class="role-card-title">정보 연동 (API / Heritage Information)</span>
            </div>
            <ul class="role-list">
              <li>AI 모델이 식별한 유적지 정보를 국가유산포털의 데이터와 매핑</li>
              <li>해당 유적지의 상세 정보 및 역사적 설명을 연동</li>
            </ul>
          </div>

          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">STEP 4</span>
              <span class="role-card-title">출력 (Mobile App / Information Display)</span>
            </div>
            <ul class="role-list">
              <li>식별된 유적지의 명칭과 관련 정보를 모바일 앱에 표시</li>
              <li>사용자가 현장에서 별도의 검색 과정 없이 유적지 정보를 확인할 수 있도록 구현</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 3. 나의 역할 -->
      <div class="intro-section">
        <div class="intro-section-title">👤 3. 나의 역할</div>
        
        <div class="role-main-badge">
          <span class="role-main-tag">전담 파트</span>
          <span class="role-main-text">AI 데이터셋 구축 및 인식 정확도 최적화</span>
        </div>

        <div class="role-cards-grid">
          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">01</span>
              <span class="role-card-title">10개 핵심 유적지 데이터셋 구축</span>
            </div>
            <ul class="role-list">
              <li>대표 유적지 10곳을 선정하고 유적지당 약 1,000장씩 원본 이미지 데이터를 수집 및 정제</li>
            </ul>
          </div>

          <div class="role-card">
            <div class="role-card-header">
              <span class="role-card-num">02</span>
              <span class="role-card-title">현장 맞춤형 다각도 데이터 증강</span>
            </div>
            <ul class="role-list">
              <li>관람객마다 촬영 위치, 각도, 거리가 다른 점을 고려하여 변형 파이프라인 구축</li>
              <ul class="role-sublist">
                <li>• <strong>각도 변형 및 회전:</strong> 다양한 관람 시점 대응</li>
                <li>• <strong>좌우 반전:</strong> 관람 동선에 따른 시각차 극복</li>
                <li>• <strong>확대 및 축소:</strong> 원거리·근거리 촬영 스케일 반영</li>
              </ul>
            </ul>
          </div>

          <div class="role-card" style="grid-column: 1 / -1;">
            <div class="role-card-header">
              <span class="role-card-num">03</span>
              <span class="role-card-title">유적지 고유 특징 중심 데이터 전처리</span>
            </div>
            <ul class="role-list">
              <li>지붕 선, 현판, 기둥 구조 등 각 유적지의 핵심 건축적 특징이 잘 드러나도록 특정 영역 이미지 편집 진행</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 5. 문제점 및 추후 개선 방안 -->
      <div class="intro-section">
        <div class="intro-section-title">⚠️ 5. 문제점 및 추후 개선 방안</div>
        
        <!-- 5-1. 문제점 -->
        <div style="margin-bottom: 24px;">
          <div class="intro-subtitle" style="color: #f59e0b; margin-bottom: 14px;">5-1. 문제점</div>
          
          <div class="intro-issue-box">
            <div class="issue-title">
              <span class="issue-badge">ISSUE 01</span>
              <span>문제 1. AI 학습 플랫폼의 이미지 등록 용량 제한</span>
            </div>
            <div class="issue-row">
              <span class="issue-label red">문제 상황</span>
              <span class="issue-desc">약 1,000장의 이미지 데이터셋을 구축했으나, AI 플랫폼의 이미지 등록 제한으로 약 200장만 학습에 활용할 수 있었음.</span>
            </div>
            <div class="issue-row">
              <span class="issue-label yellow">원인</span>
              <span class="issue-desc">플랫폼의 학습 데이터 등록 용량 제한으로 다양한 촬영 각도와 거리, 조명 환경을 반영한 데이터를 충분히 활용하지 못함.</span>
            </div>
            <div class="issue-row">
              <span class="issue-label green">결과</span>
              <span class="issue-desc">실제 관람 환경에서 촬영한 이미지에 대한 오인식 문제가 발생함.</span>
            </div>
          </div>

          <div class="intro-issue-box">
            <div class="issue-title">
              <span class="issue-badge">ISSUE 02</span>
              <span>문제 2. 다양한 촬영 환경에 따른 이미지 인식 성능 저하</span>
            </div>
            <div class="issue-row">
              <span class="issue-label red">문제 상황</span>
              <span class="issue-desc">동일한 유적지라도 촬영 각도, 거리, 조명 등에 따라 이미지 분류 결과가 달라지는 문제가 발생함.</span>
            </div>
            <div class="issue-row">
              <span class="issue-label yellow">원인</span>
              <span class="issue-desc">제한된 학습 데이터로 실제 관람객의 다양한 촬영 환경을 충분히 반영하기 어려웠음.</span>
            </div>
            <div class="issue-row">
              <span class="issue-label green">개선 방법</span>
              <span class="issue-desc">이미지 증강 범위를 확대하고 촬영 전 지역 및 유적지 유형을 선택하는 사전 필터링 기능을 기획함.</span>
            </div>
          </div>
        </div>

        <!-- 5-2. 향후 개선사항 -->
        <div>
          <div class="intro-subtitle" style="color: #38bdf8; margin-bottom: 14px;">5-2. 향후 개선사항</div>

          <!-- 1. 촬영 전 3단계 필터링 시스템 -->
          <div class="intro-desc-box">
            <div class="intro-subtitle" style="font-size: 0.98rem; color: #f1f5f9;">1. 촬영 전 3단계 필터링 시스템</div>
            <p style="margin: 0; color: #cbd5e1; font-size: 0.92rem; line-height: 1.7;">
              촬영 전 지역 및 유적지 유형을 선택하는 사전 필터링 구조를 도입하여, 이미지 촬영 전 분석 대상을 선별하고 AI의 기술적 한계를 서비스 설계 차원에서 보완하도록 기획했습니다.
            </p>
          </div>

          <!-- 2. 주요 개선 방향 -->
          <div class="intro-desc-box">
            <div class="intro-subtitle" style="font-size: 0.98rem; color: #f1f5f9;">2. 주요 개선 방향</div>
            <ul class="role-list">
              <li><strong>AI 분석 범위 최적화:</strong> 전체 유적지 중 주변 후보군 2~3곳만 선별하여 이미지 분류 효율 향상</li>
              <li><strong>위치 기반 탐색:</strong> GPS를 활용해 관람객 주변 유적지를 자동 탐색하고 검색 과정 간소화</li>
              <li><strong>예외 처리 구조 마련:</strong> AI 분류 실패 시 지역 및 유형 정보를 기반으로 국가유산포털 API와 연계한 대체 검색 제공</li>
            </ul>
          </div>

          <!-- 3. 기대 효과 -->
          <div class="intro-desc-box">
            <div class="intro-subtitle" style="font-size: 0.98rem; color: #f1f5f9;">3. 기대 효과</div>
            <div class="expectations-table-wrap">
              <table class="expectations-table">
                <thead>
                  <tr>
                    <th>개선 항목</th>
                    <th>기대 효과</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>인식 정확도</td>
                    <td>분석 후보군 축소를 통한 오분류 가능성 감소</td>
                  </tr>
                  <tr>
                    <td>데이터 효율성</td>
                    <td>제한된 학습 데이터의 한계를 사전 필터링으로 보완</td>
                  </tr>
                  <tr>
                    <td>사용자 편의성</td>
                    <td>GPS 기반 자동 탐색으로 현장 검색 부담 최소화</td>
                  </tr>
                  <tr>
                    <td>서비스 안정성</td>
                    <td>AI 인식 실패 시에도 대체 검색을 통한 정보 제공 가능</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="highlight-callout">
              <strong>핵심 개선 방향:</strong> AI 모델의 성능 개선에만 의존하지 않고, 사용자 입력 정보와 위치 기반 데이터를 결합하여 AI의 기술적 한계를 서비스 설계 차원에서 보완하고자 함.
            </div>
          </div>
        </div>

      </div>

      <!-- 6. 결론 -->
      <div class="intro-section" style="margin-bottom: 0;">
        <div class="intro-section-title">📝 6. 결론</div>

        <!-- 6-1. 프로젝트 결과 및 성과 -->
        <div class="intro-desc-box">
          <div class="intro-subtitle">6-1. 프로젝트 결과 및 성과</div>
          <p style="margin: 0 0 10px 0; line-height: 1.75;">
            이번 프로젝트를 통해 MIT App Inventor의 Personal Image Classifier를 활용한 이미지 분류 모델의 학습 과정을 경험했습니다.
          </p>
          <p style="margin: 0 0 10px 0; line-height: 1.75;">
            담당 업무로는 10개 유적지를 대상으로 약 1,000장의 원본 이미지 데이터셋을 수집, 회전, 좌우 반전, 확대 및 축소 등의 데이터 증강 작업을 진행했습니다. 또한 유적지마다 구별되는 건축적 특징이 잘 드러나도록 이미지의 특징 영역을 편집하여 AI 모델의 학습 데이터를 구축했습니다.
          </p>
          <p style="margin: 0; line-height: 1.75;">
            이를 통해 다양한 촬영 환경을 고려한 데이터셋 구성의 중요성을 이해하고 AI 이미지 분류 결과와 국가유산포털 API를 연동하여 유적지 정보를 제공하는 모바일 가이드 시스템의 구현에 참여했습니다.
          </p>
        </div>

        <!-- 6-2. 프로젝트를 통해 배운 점 -->
        <div class="intro-desc-box">
          <div class="intro-subtitle">6-2. 프로젝트를 통해 배운 점</div>
          <ul class="role-list">
            <li><strong>AI 학습 데이터 구축:</strong> 10개 유적지의 이미지 데이터를 직접 수집하고 정제하여 이미지 분류 모델의 학습용 데이터셋을 구축했습니다.</li>
            <li><strong>데이터 증강:</strong> 이미지 회전, 좌우 반전, 확대 및 축소를 적용하여 다양한 촬영 각도와 거리에 대응할 수 있도록 학습 데이터를 확장했습니다.</li>
            <li><strong>이미지 전처리:</strong> 지붕 선, 현판, 기둥 구조 등 유적지별 주요 특징이 잘 드러나도록 이미지 영역을 편집하고 학습 데이터의 품질을 개선했습니다.</li>
            <li><strong>AI 이미지 분류:</strong> MIT App Inventor Personal Image Classifier를 활용하여 유적지 이미지 학습 및 분류 과정을 경험했습니다.</li>
          </ul>
        </div>

        <!-- 6-3. 향후 개선 방향 -->
        <div class="intro-desc-box">
          <div class="intro-subtitle">6-3. 향후 개선 방향</div>
          <p style="margin: 0 0 10px 0; line-height: 1.75;">
            향후에는 이미지 학습 데이터의 다양성을 확보하고 촬영 환경에 따른 인식 성능을 개선하여 AI 분류의 정확도를 높이고자 합니다.
          </p>
          <p style="margin: 0; line-height: 1.75;">
            또한 GPS 기반 위치 정보와 지역별 필터링 기능을 활용하여 유적지 탐색 과정을 간소화하고, AI 이미지 분류에 실패하더라도 대체 검색을 통해 관련 정보를 제공할 수 있도록 시스템의 안정성과 사용자 편의성을 개선하고자 합니다.
          </p>
        </div>

      </div>

    </div>
  </div>

</div>

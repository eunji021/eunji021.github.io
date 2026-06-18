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
    background: url('./assets/images/open.png') center/cover no-repeat, #000;
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
              <img src="./assets/images/open.png" alt="미륵사지 석탑" onerror="this.src='https://images.unsplash.com/photo-1542281286-9e0a16bb7366?auto=format&fit=crop&w=400&q=80'">
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

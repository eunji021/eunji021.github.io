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
</style>

<div class="project-tabs-container">
  <!-- 상단 탭 메뉴 -->
  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-ppt">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

  <!-- 1. 한눈에 보기 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content active">
    <div class="carousel-container" id="slide-carousel">
      <!-- 슬라이드 이미지 (경로를 맞춰서 수정해주세요) -->
      <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/placeholder.png');"></div>
      
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
  </div>

<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const nextBtn = document.querySelector('.carousel-btn.next');

    function updateButtons() {
      prevBtn.style.display = (currentSlide === 0) ? 'none' : 'block';
      nextBtn.style.display = (currentSlide === slides.length - 1) ? 'none' : 'block';
    }

    function moveSlide(direction) {
      const newIndex = currentSlide + direction;
      if (newIndex < 0 || newIndex >= slides.length) return;
      
      slides[currentSlide].classList.remove('active');
      currentSlide = newIndex;
      slides[currentSlide].classList.add('active');
      
      updateButtons();
    }
    
    // Initialize buttons on load
    updateButtons();
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

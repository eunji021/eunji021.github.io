---
layout: default
title: "Python 기초 및 알고리즘"
category: tech-fundamentals
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Share+Tech+Mono&display=swap');

  /* Force premium dark radial theme with custom subtle glows */
  body {
    background-color: #080b11 !important;
    background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.08) 0%, transparent 450px),
                radial-gradient(circle at bottom left, rgba(59, 130, 246, 0.04) 0%, transparent 450px),
                #080b11 !important;
    color: #cbd5e1 !important;
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    min-height: 100vh;
  }

  /* Hide default footer to align with homepage design */
  .footer {
    display: none !important;
  }

  /* Post Container */
  .post-container {
    max-width: 900px;
    margin: 60px auto 100px;
    padding: 0 30px;
    box-sizing: border-box;
    animation: fadeUp 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
  }

  /* Return Button */
  .return-btn-custom {
    color: #818cf8 !important;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 35px;
    font-family: 'Pretendard', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    transition: all 0.2s ease;
  }

  .return-btn-custom:hover {
    color: #ffffff !important;
    transform: translateX(-4px);
  }

  /* Post Title Header */
  .post-header {
    margin-bottom: 45px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding-bottom: 25px;
  }

  .post-title {
    font-family: 'Pretendard', sans-serif !important;
    font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    text-shadow: none !important;
    margin: 0 0 12px 0;
    letter-spacing: -0.5px;
  }

  .post-subtitle {
    font-family: 'Pretendard', sans-serif !important;
    font-size: 1.05rem !important;
    color: #94a3b8 !important;
    margin: 0;
    line-height: 1.6;
  }

  /* Premium Glassmorphic Article Panel */
  .article-panel {
    background: rgba(13, 19, 31, 0.4) !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.04) !important;
    border-radius: 20px !important;
    padding: 40px !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25) !important;
    color: #e2e8f0;
    line-height: 1.8;
  }

  /* Markdown Typography Overrides */
  .article-panel h2 {
    font-family: 'Pretendard', sans-serif !important;
    color: #818cf8 !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    margin-top: 40px;
    margin-bottom: 20px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding-bottom: 12px;
    text-shadow: none !important;
  }

  .article-panel h2:first-of-type {
    margin-top: 0;
  }

  .article-panel h3 {
    font-family: 'Pretendard', sans-serif !important;
    color: #ffffff !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    margin-top: 30px;
    margin-bottom: 12px;
    text-shadow: none !important;
  }

  .article-panel p {
    font-size: 0.98rem;
    color: #94a3b8;
    margin-bottom: 20px;
    word-break: keep-all;
  }

  /* Premium Code Blocks */
  .article-panel pre {
    background: rgba(6, 9, 15, 0.85) !important;
    border: 1px solid rgba(129, 140, 248, 0.2) !important;
    border-radius: 12px !important;
    padding: 20px !important;
    margin-bottom: 30px !important;
    overflow-x: auto;
    box-shadow: inset 0 0 15px rgba(0,0,0,0.2);
  }

  .article-panel code {
    font-family: 'Share Tech Mono', monospace !important;
    color: #4ade80 !important;
    font-size: 0.9rem !important;
    background: transparent !important;
    padding: 0 !important;
  }

  /* Inline Code Tags */
  .article-panel p code {
    background: rgba(129, 140, 248, 0.1) !important;
    color: #a5b4fc !important;
    border: 1px solid rgba(129, 140, 248, 0.2) !important;
    border-radius: 4px !important;
    padding: 2px 6px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.88rem !important;
  }

  /* Centered Custom Footer */
  .custom-footer {
    text-align: center;
    padding: 40px 0 60px;
    font-family: 'Pretendard', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
  }

  .custom-footer span {
    color: #818cf8;
    margin-left: 4px;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<div class="post-container">
  
  <!-- Return Link -->
  <a href="{{ site.baseurl }}/" class="return-btn-custom">
    <i class="uil uil-arrow-left"></i> 대시보드로 돌아가기
  </a>

  <!-- Post Header -->
  <header class="post-header">
    <h1 class="post-title">Python 기초 및 알고리즘</h1>
    <p class="post-subtitle">데이터 구조 이해 및 로직 최적화 기반 다지기</p>
  </header>

  <!-- Premium Article Panel -->
  <div class="article-panel">
    
    <h2>1. 파이썬 기초 자료형 및 데이터 구조</h2>
    <p>파이썬을 강력하게 만드는 가장 큰 요소는 다루기 쉬우면서도 강력한 내장 데이터 구조입니다.</p>

    <h3>리스트 (List)</h3>
    <p>가장 기본적으로 사용되는 동적 배열입니다. 스택(Stack)으로도 활용 가능합니다.</p>
<pre><code># 리스트 생성 및 활용
numbers = [1, 2, 3, 4, 5]
numbers.append(6)    # O(1)
numbers.insert(0, 0) # O(N)
print(numbers)       # [0, 1, 2, 3, 4, 5, 6]
</code></pre>

    <h3>딕셔너리 (Dictionary)</h3>
    <p>해시 테이블(Hash Table)로 구현되어 있어 키-값(Key-Value) 쌍의 데이터를 평균 O(1)의 시간 복잡도로 탐색할 수 있습니다.</p>
<pre><code>user = {"name": "Eunji", "role": "Software Engineer"}
user["skills"] = ["Python", "C/C++", "C#"]
print(user["name"]) # Eunji
</code></pre>

    <h2>2. 핵심 알고리즘 패턴</h2>
    <p>임베디드 제어 로직이나 데이터 파싱 등에서 자주 활용되는 필수 알고리즘 패턴입니다.</p>

    <h3>탐색과 정렬 (Search & Sort)</h3>
    <p>내장 <code>.sort()</code> 함수는 Timsort 알고리즘(O(N log N))을 사용합니다. 특정 기준에 따른 정렬은 <code>lambda</code>를 활용하여 쉽게 구현할 수 있습니다.</p>
<pre><code>data = [("sensor1", 35.5), ("sensor2", 22.1), ("sensor3", 40.0)]
# 온도(두 번째 요소)를 기준으로 오름차순 정렬
data.sort(key=lambda x: x[1])
</code></pre>

    <h3>너비 우선 탐색(BFS)과 큐(Queue)</h3>
    <p>경로 탐색이나 상태 변화를 관리할 때 필수적인 BFS 알고리즘입니다. 파이썬에서는 <code>collections.deque</code>를 사용하여 성능 저하 없이 큐를 구현합니다.</p>
<pre><code>from collections import deque

def bfs_search(start_node):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        current = queue.popleft()
        print(f"Processing: {current}")
        # 다음 상태(노드)를 큐에 삽입하는 로직...
</code></pre>

  </div>
</div>

<!-- Center custom footer signature -->
<div class="custom-footer">
  Kwon <span>Eun Ji</span>
</div>

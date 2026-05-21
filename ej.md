---
layout: default
title: "Python 기초 및 알고리즘"
category: tech-fundamentals
---

<div class="container" style="max-width: 900px; padding: 60px 20px;">
  <a href="{{ site.baseurl }}/" style="color: #818cf8; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 32px; font-weight: 600;">
    <i class="uil uil-arrow-left"></i> 대시보드로 돌아가기
  </a>

  <h1 style="color: #fff; font-size: 2.5rem; margin-bottom: 16px; font-weight: 800;">Python 기초 및 알고리즘</h1>
  <p style="color: #94a3b8; font-size: 1.1rem; line-height: 1.6; margin-bottom: 48px;">
    데이터 구조 이해 및 로직 최적화 기반 다지기
  </p>

  <div class="dash-card static-card" style="background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 40px; color: #e2e8f0; line-height: 1.8;">
    
    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">1. 파이썬 기초 자료형 및 데이터 구조</h2>
    <p style="margin-bottom: 24px;">파이썬을 강력하게 만드는 가장 큰 요소는 다루기 쉬우면서도 강력한 내장 데이터 구조입니다.</p>

    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 12px;">리스트 (List)</h3>
    <p style="margin-bottom: 16px;">가장 기본적으로 사용되는 동적 배열입니다. 스택(Stack)으로도 활용 가능합니다.</p>
<pre style="background: rgba(10, 15, 25, 0.8); padding: 16px; border-radius: 8px; margin-bottom: 32px; overflow-x: auto;"><code style="color: #4ade80;"># 리스트 생성 및 활용
numbers = [1, 2, 3, 4, 5]
numbers.append(6)    # O(1)
numbers.insert(0, 0) # O(N)
print(numbers)       # [0, 1, 2, 3, 4, 5, 6]
</code></pre>

    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 12px;">딕셔너리 (Dictionary)</h3>
    <p style="margin-bottom: 16px;">해시 테이블(Hash Table)로 구현되어 있어 키-값(Key-Value) 쌍의 데이터를 평균 O(1)의 시간 복잡도로 탐색할 수 있습니다.</p>
<pre style="background: rgba(10, 15, 25, 0.8); padding: 16px; border-radius: 8px; margin-bottom: 48px; overflow-x: auto;"><code style="color: #4ade80;">user = {"name": "Eunji", "role": "Software Engineer"}
user["skills"] = ["Python", "C/C++", "C#"]
print(user["name"]) # Eunji
</code></pre>

    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px;">2. 핵심 알고리즘 패턴</h2>
    <p style="margin-bottom: 24px;">임베디드 제어 로직이나 데이터 파싱 등에서 자주 활용되는 필수 알고리즘 패턴입니다.</p>

    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 12px;">탐색과 정렬 (Search & Sort)</h3>
    <p style="margin-bottom: 16px;">내장 <code>.sort()</code> 함수는 Timsort 알고리즘(O(N log N))을 사용합니다. 특정 기준에 따른 정렬은 <code>lambda</code>를 활용하여 쉽게 구현할 수 있습니다.</p>
<pre style="background: rgba(10, 15, 25, 0.8); padding: 16px; border-radius: 8px; margin-bottom: 32px; overflow-x: auto;"><code style="color: #4ade80;">data = [("sensor1", 35.5), ("sensor2", 22.1), ("sensor3", 40.0)]
# 온도(두 번째 요소)를 기준으로 오름차순 정렬
data.sort(key=lambda x: x[1])
</code></pre>

    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 12px;">너비 우선 탐색(BFS)과 큐(Queue)</h3>
    <p style="margin-bottom: 16px;">경로 탐색이나 상태 변화를 관리할 때 필수적인 BFS 알고리즘입니다. 파이썬에서는 <code>collections.deque</code>를 사용하여 성능 저하 없이 큐를 구현합니다.</p>
<pre style="background: rgba(10, 15, 25, 0.8); padding: 16px; border-radius: 8px; margin-bottom: 16px; overflow-x: auto;"><code style="color: #4ade80;">from collections import deque

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

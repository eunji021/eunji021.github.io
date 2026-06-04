---
layout: post
title: "실시간 화재 대피 유도 시스템"
category: projects
author: eunji
short-description: "실시간 화재 감지 및 다익스트라 최적 경로 기반 가변형 대피 유도 모듈"
---

# 🛠️ 실시간 화재 대피 유도 시스템 (Smart Evacuation Guide)

## 1. 프로젝트 개요 (Overview)
* **진행 기간:** YYYY.MM ~ YYYY.MM (개인 / 팀 N명)
* **기획 배경:** 
  > 화재 발생 시 고정형 비상구 안내 표시판으로 인해 작업자가 화재 방향으로 대피하는 오안내 문제를 해결하고자 기획되었습니다.
* **프로젝트 목적:** 
  > 화재 센서 로그 데이터를 기반으로 동적 대피 유도 LED 패널을 제어해 안전 대피 경로를 가이드하는 시스템을 구축합니다.

---

## 2. 사용 기술 및 개발 환경 (Tech Stack & Environment)
* **Core Languages:** C/C++, Python
* **Hardware & Modules:** ESP32, Flame/Smoke Sensors, LED Dot Matrix Modules, Buzzer
* **Software & Toolchain:** VS Code, PlatformIO, Arduino IDE
* **통신 프로토콜:** Wi-Fi / WebSockets, Serial, I2C

---

## 3. 핵심 기능 및 구현 내용 (Core Features)
* **핵심 기능 1 (실시간 센서 기반 동적 다익스트라 계산):**
  - [상세 설명] 화재 감지 센서값에 가중치를 부여하여 실시간 위험 노드를 우회하는 최적 대피 경로 계산 알고리즘.
* **핵심 기능 2 (가변형 LED 방향 표시 제어):**
  - [상세 설명] 계산된 경로 방향에 맞춰 대피 비상구 LED matrix 화살표 방향을 동적으로 스위칭하는 제어 구조.

---

## 4. 개발 중 겪은 문제와 해결 과정 (Troubleshooting)
### ⚠️ Issue 1: 다중 노드 센서 데이터 수집 병목 및 레이턴시
* **현상:** 
  > 센서 노드가 동시에 데이터를 게이트웨이로 전송할 때 패킷 유실 및 딜레이 발생.
* **원인 분석:** 
  > 동기식 통신 대기로 인한 CPU 차단 현상 확인.
* **해결책:** 
  > FreeRTOS 태스크 분리 및 비동기 웹소켓 통신 인터럽트 제어로 변환하여 대기 시간 단축.

---

## 5. 프로젝트 결과 및 느낀 점 (Conclusion & Retrospective)
* **최종 성과:** 
  > 최적 경로 수렴 시간 및 모듈 구동 테스트 성과를 정리합니다.
* **배운 점:** 
  > 그래프 탐색 알고리즘(Dijkstra)의 하드웨어 실시간 적용 및 임베디드 멀티태스킹 설계 능력을 습득한 점을 기록합니다.

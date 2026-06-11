---
layout: post
title: "실시간 안전 장비 착용 여부 시스템"
category: projects
author: eunji
short-description: "ESP32 게이트웨이를 이용해 작업자 안전모와 조끼의 수집 센서 상태를 블루투스로 패킹 취합하는 관제 아키텍처"
---

<style>
  .post-container {
    display: flex;
    gap: 30px;
    align-items: flex-start;
    margin-top: 30px;
  }
  @media (max-width: 768px) {
    .post-container {
      flex-direction: column;
    }
    .sidebar-toc {
      border-right: none !important;
      border-bottom: 2px solid rgba(0, 242, 254, 0.2);
      padding-right: 0 !important;
      padding-bottom: 10px;
      width: 100%;
      position: static !important;
    }
  }
  .sidebar-toc {
    position: sticky;
    top: 20px;
    min-width: 300px;
    max-width: 450px;
    border-right: 2px solid rgba(0, 242, 254, 0.2);
    padding-right: 20px;
    font-family: 'Pretendard', sans-serif;
  }
  .sidebar-toc ul {
    list-style: none;
    padding-left: 0;
  }
  .sidebar-toc ul ul {
    padding-left: 15px;
  }
  .sidebar-toc li {
    margin-bottom: 10px;
  }
  .sidebar-toc a {
    text-decoration: none;
    color: #849ca8;
    font-size: 0.85rem;
    transition: color 0.2s;
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .sidebar-toc a:hover {
    color: #00f2fe;
  }
  .main-content {
    flex: 1;
    min-width: 0;
  }
  /* Hide the # 목차 title from the generated TOC */
  #markdown-toc {
    margin-top: 0;
  }
</style>

<div class="post-container">
  <div class="sidebar-toc" markdown="1">
<strong style="color:#00f2fe; margin-bottom: 10px; display: block;">목차 (Contents)</strong>
* TOC
{:toc}

<script>
  // Add title attributes so full text shows on hover
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.sidebar-toc a').forEach(a => {
      a.setAttribute('title', a.innerText);
    });
  });
</script>
  </div>
  <div class="main-content" markdown="1">

# 공사장 안전장비 실시간 착용여부 시스템 
> **ESP32 중계기(Gateway) 설계 및 데이터 패킹 프로토콜 구현을 통한 다중 디바이스 통신 제약 극복**

* **진행 기간:** 2025.03 ~ 2025.06 
* **주요 역량:** 임베디드 소프트웨어 아키텍처 설계, 멀티 디바이스 데이터 패킹 및 타임 슬라이싱(Time-Slicing) 스트리밍, 임베디드 예외 처리 루틴 구현
* **사용 기술:** C/C++ (Arduino IDE), ESP32, Bluetooth LE (BLE Advertising), Bluetooth Serial (Classic), MPU6050 (I2C), App Inventor

---

## 핵심 성과 (Core Achievements)
팀 프로젝트 내에서 **하드웨어 핵심 제어 아키텍처 수립 및 소프트웨어 상위 레이어(임베디드 무선 네트워크 ~ 앱 관제) 시스템 전체의 펌웨어 설계 및 통합**을 전담하여 다음과 같은 성과를 냈습니다.

1. **중계기(Gateway) 기반 무선 네트워크 파이프라인 독자 설계**
   - 모바일 플랫폼(App Inventor)의 다중 BLE 소켓 제어 한계를 극복하기 위해, ESP32를 마스터 브릿지로 레이어를 분리하는 임베디드 아키텍처 수립 및 통신 성공률 100% 달성.
2. **타임 슬라이싱(Time-Slicing) 데이터 스트리밍 프로토콜 정립**
   - 다중 작업자(2인) 노드로부터 수집된 가변 데이터를 비동기 버퍼 유실 없이 가공하고, 고유 식별자 문자열 형태로 가공하여 앱 단에 주기적으로 교차 송신하는 펌웨어 로직 구현.
3. **엣지 컴퓨팅 기반 센서 데이터 처리 및 예외 처리 루틴 구현**
   - 각 작업자 단말 내부에서 MPU6050(자이로) 및 감압 센서의 원시 데이터(Raw Data)를 1차 연산 처리하여 무동작 상태(1분 기준) 및 착용 탈착 여부를 실시간 연산하도록 제어 알고리즘 최적화.

---

## 1. 프로젝트 개요
* **배경:** 기존 공사 현장의 안전 관리는 CCTV 및 수동 점검에 의존하여, 작업자의 무착용 상태나 낙상 사고를 실시간으로 인지하고 즉각 대응하기 어려웠습니다.
* **목적:** ESP32 모듈과 다중 센서(압력, 자이로), 블루투스 기술을 융합하여 작업자의 안전모·안전조끼 착용 상태 및 이상 신호를 실시간으로 수집하고 관리자 앱으로 통합 관제하는 IoT 안전 시스템을 구축합니다.

# 

## 2. 시스템 아키텍처

### 2-1. 네트워크 파이프라인
안드로이드(앱 인벤터)의 OS/플랫폼 제약 조건인 '다중 블루투스 연결 불안정성'을 해결하기 위해 제가 직접 설계한 3단계 무선 네트워크 구조입니다.

1. **[1단계] 하드웨어 레벨 다중 수신 (BLE Client ──▶ Gateway)**
   - 각 작업자(Worker A, Worker B)의 안전모와 조끼에 탑재된 ESP32 노드가 압력 및 자이로 센서 데이터를 독립적으로 실시간 계측합니다.
   - 마스터 중계기(ESP32)는 각 노드의 고유 MAC 주소를 기반으로 착용 여부, 낙상 신호, RSSI 데이터를 **BLE 무선 통신**을 통해 병렬로 다중 수신합니다.
2. **[2단계] 스트리밍 데이터 패킹 및 타임 슬라이싱 스트리밍 (Gateway)**
   - 중계기 단에서 수집된 2인의 데이터를 앱이 혼선 없이 구분할 수 있도록 가공합니다.
   - 데이터 병목을 방지하기 위해 토글 변수(`sendWorker1Next`)를 활용하여 **1초 간격으로 작업자1과 작업자2의 상태 메시지를 교차 송신하는 타임 슬라이싱 기법**을 적용했습니다.
   * *구현한 데이터 스트리밍 포맷:* `"작업자1: 정상착용\n"` / `"작업자2: 착용불량\n"`
3. **[3단계] 실시간 데이터 파싱 및 UI 매핑 (App)**
   - 안드로이드 앱(App Inventor)은 중계기와 연결된 단일 **Classic 블루투스** 채널을 통해 끊김 없이 정제된 패킷 스트링을 수신합니다.
   - 수신된 문자열을 실시간 분리(Parsing)하여 화면 내 **Worker A와 Worker B의 개별 대시보드 UI에 독립적으로 값을 매핑**하여 실시간 다중 관제를 시각화했습니다.

### 2-2. 하드웨어 스펙
* **메인 컨트롤러:** ESP32 (송신부 헬멧 2대 / 수신부 조끼 2대 / 마스터 중계기 1대 총 5대 구성 프로토타입)
* **센서 및 모듈:** 감압 센서 (FSR RA12P), 자이로 센서 (MPU6050 계열), 능동 부저, 고휘도 LED
* **전원부:** 3.7V 리튬이온 배터리, TP4056 충전 모듈, MT3608 승압 컨버터

## 핵심 소스코드

### 3-1. 라우팅 소스코드
> **고유 MAC 주소 필터링 및 타임 슬라이싱 기반 앱인벤터 스트리밍 제어 알고리즘**

* **비동기 BLE 스캔 및 필터링:** 현장 내 수많은 BLE 신호 중 관제 대상인 작업자 1, 2의 고유 MAC 주소 패킷만 정밀 필터링하도록 설계했습니다.
* **하드웨어 엣지 데이터 디코딩:** 디바이스 노드가 보낸 팩추얼 데이터(Manufacturer Data)를 실시간 파싱하여 최종 알람 상태 변수(`'B'` 또는 `'N'`)를 정확히 추출합니다.
* **타임 슬라이싱 알고리즘 기법:** 단일 채널 직렬 통신의 병목 현상을 방지하기 위해, 토글 변수(`sendWorker1Next`)와 1000ms 주기 인터벌을 제어하여 작업자 1, 2의 데이터를 1초 간격으로 번갈아 안전하게 스트리밍합니다.


## 트러블슈팅 (Troubleshooting)

### 네트워크 구조 개선
* **문제 상황:** 초기 설계 시 스마트폰 앱이 헬멧과 조끼의 BLE 신호를 직접 다중 수신하도록 구현하려 했으나, 앱 인벤터 플랫폼 특성상 멀티 커넥션 유지가 불가능해 신호가 유실되거나 앱이 다운되는 현상이 발생함.
* **원인 분석:** 모바일 프로토콜 환경 및 컴포넌트 특성상 다중 무선 블루투스 소켓 분할 제어의 드라이버 인터페이스 제약 확인.
* **해결 기술:** 하드웨어 단에 **ESP32 중계기(Gateway) 허브를 중간 브릿지로 상정하는 토폴로지 아키텍처 변환**을 주도함. 하드웨어 레벨(ESP32 내부 펌웨어)에서 무선 BLE 스캔을 통해 여러 작업자 장치를 수집 및 병렬 처리하고, 모바일 앱과는 1:1 Classic 블루투스 직렬 통신 구조로 단순화하여 **통신 제약 완벽 해결 및 데이터 전송 성공률 100%** 달성.

### 다중 데이터 스트리밍 시 동기화 타이밍 제어를 통한 데이터 밀림 방지
* **문제 상황:** 2인 작업자의 대량 센서 정보가 비동기적으로 중계기에 연속 인입될 때, 앱인벤터 내부 버퍼 처리 속도와 무선 송신 주기가 어긋나 UI 데이터 동기화 지연 및 다른 작업자의 모니터링 창에 데이터가 맵핑되는 결함 발생.
* **해결 기술:** 중계기 제어 펌웨어 내부에 **1000ms 주기성 전송 인터벌 인터럽트 및 토글 제어 부울 선언을 이용한 '타임 슬라이싱 교차 스트리밍' 알고리즘**을 도입함. 수신 채널을 의도적으로 정형화하고 데이터 프레임 앞단에 문자열 인덱스 식별 정보(`"작업자1:"`, `"작업자2:"`)를 확실히 패킹하여 보냄으로써 수신 정합성과 데이터 분류 가독성을 완전 확보함.

---

## 4. 결과 및 기대 효과 (Conclusion)
* **다중 관제 아키텍처 검증:** 스마트폰이나 개발 플랫폼의 제약 조건에 구애받지 않고, 중계기 설계를 통해 2인 이상의 작업자 상태를 실시간 대시보드로 안정적으로 모니터링할 수 있음을 입증했습니다.
* **소프트웨어 확장성(Scale-up):** 향후 현장 대규모 확장 시에도 모바일 앱의 복잡한 소스코드를 수정할 필요 없이, **중계기 단에서 노드 관리 로직을 추가하고 패킷 구조만 확장**하면 되므로 뛰어난 유지보수성을 가진 시스템 구조입니다.

---

## 팀 프로젝트 개요 
* **참여 인원:** 4명 
* **협업 내역:**
  - **권은지 (본인):** 하드웨어 핵심 제어 로직 구현, App Inventor 모바일 앱 개발, ESP32 중계기-앱 간 블루투스 연동 및 데이터 파싱 구현
  - 팀원 A (최성용): 하드웨어 회로 설계, 센서 노드 원시 코드 작성
  - 팀원 B (구민서): 외형 PETG 3D 케이스 설계 및 구조물 조립
  - 팀원 C (이명은): ESP32-앱 간 블루투스 통신 기초 테스트 및 디버깅 보조

  </div>
</div>

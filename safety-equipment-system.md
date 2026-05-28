---
layout: default
title: "안전장비 실시간 착용여부 시스템"
category: embedded-hardware-projects
---

<div class="container" style="max-width: 900px; padding: 60px 20px;">
  <a href="{{ site.baseurl }}/" style="color: #818cf8; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 32px; font-weight: 600; transition: color 0.3s;">
    <i class="uil uil-arrow-left"></i> 대시보드로 돌아가기
  </a>

  <h1 style="color: #fff; font-size: 2.5rem; margin-bottom: 16px; font-weight: 900; letter-spacing: -0.02em;">공사장 안전장비 실시간 착용여부 시스템</h1>
  <p style="color: #94a3b8; font-size: 1.15rem; line-height: 1.6; margin-bottom: 48px;">
    실시간 센서 데이터 기반 안전 모니터링 시스템 구축
  </p>

  <div class="dash-card static-card" style="background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 48px; color: #e2e8f0; line-height: 1.8; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    
    <!-- 팀원 및 역할 분담 -->
    <div style="background: rgba(99, 102, 241, 0.1); border-left: 4px solid #818cf8; border-radius: 0 8px 8px 0; padding: 24px; margin-bottom: 48px;">
      <h3 style="color: #818cf8; font-size: 1.2rem; margin-top: 0; margin-bottom: 16px; font-weight: 700;">👥 팀원 및 역할 분담</h3>
      <ul style="list-style-type: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
        <li><strong style="color: #fff; font-weight: 600;">권은지 (본인):</strong> 하드웨어 핵심 제어 로직 구현, App Inventor 모바일 앱 개발, ESP32 중계기-앱 간 블루투스 연동 및 데이터 파싱(Parsing) 구현</li>
        <li><strong style="color: #cbd5e1;">최성용:</strong> 회로 설계 및 센서 연동, 전체 하드웨어 코딩 개발 담당</li>
        <li><strong style="color: #cbd5e1;">구민서:</strong> 3D 프린팅 케이스 설계, 구조물 조립 및 하드웨어 납땜 작업</li>
        <li><strong style="color: #cbd5e1;">이명은:</strong> ESP32-앱 간 블루투스 통신 로직 구성, 네트워크 안정성 테스트 및 앱 기능 디버깅</li>
      </ul>
    </div>

    <!-- 1. 프로젝트 개요 -->
    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; font-weight: 700;">1. 프로젝트 개요 (Overview)</h2>
    <ul style="margin-bottom: 48px; padding-left: 20px; display: flex; flex-direction: column; gap: 12px;">
      <li><strong style="color: #fff;">배경:</strong> 기존의 공사 현장 안전 관리는 CCTV 모니터링이나 수동 점검에 의존하여, 작업자의 무착용 상태나 돌발 사고(낙상 등)를 실시간으로 확인하고 즉각 대응하는 데 한계가 있었습니다.</li>
      <li><strong style="color: #fff;">목적:</strong> ESP32 모듈과 다중 센서(압력, 자이로), 그리고 블루투스(BLE/Classic) 기술을 융합하여 작업자의 안전모 및 안전조끼 착용 상태를 실시간 감지하고, 이상 발생 시 즉각 경고 및 모바일 관제가 가능한 IoT 안전 관리 시스템을 구축합니다.</li>
    </ul>

    <!-- 2. 시스템 및 네트워크 아키텍처 -->
    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; font-weight: 700;">2. 시스템 및 네트워크 아키텍처 (Architecture)</h2>
    
    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 16px; margin-top: 32px;">📡 2-1. 하드웨어 구성 (Hardware Spec)</h3>
    <ul style="margin-bottom: 32px; padding-left: 20px; display: flex; flex-direction: column; gap: 12px;">
      <li><strong style="color: #cbd5e1;">메인 컨트롤러:</strong> ESP32 (송신부 헬멧 / 수신부 조끼 / 마스터 중계기 총 3대 활용)</li>
      <li>
        <strong style="color: #cbd5e1;">센서 장치:</strong>
        <ul style="margin-top: 8px; margin-bottom: 8px; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; color: #94a3b8;">
          <li><strong style="color: #a5b4fc;">감압 센서 (FSR RA12P):</strong> 헬멧 내부 압력을 측정하여 실제 착용 여부 판별</li>
          <li><strong style="color: #a5b4fc;">자이로 센서 (MPU6050 계열):</strong> 작업자의 기울기 및 움직임을 감지하여 낙상/동작 정지 상태 인식</li>
        </ul>
      </li>
      <li><strong style="color: #cbd5e1;">경고 장치:</strong> 능동 부저(Buzzer), 고휘도 LED (빨강)</li>
      <li><strong style="color: #cbd5e1;">전원부:</strong> 3.7V 리튬이온 배터리, TP4056 충전 모듈, MT3608 승압 컨버터</li>
    </ul>

    <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 16px; margin-top: 32px;">🔗 2-2. 중계기(Gateway) 기반 네트워크 파이프라인</h3>
    <div style="background: rgba(15, 23, 42, 0.6); padding: 20px; border-radius: 8px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.05);">
      <h4 style="color: #f87171; font-size: 1.1rem; margin-top: 0; margin-bottom: 12px;">🚨 기존 구조의 한계점 및 확장 요구사항</h4>
      <ul style="margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; font-size: 0.95rem; color: #cbd5e1;">
        <li>앱 인벤터(Android) 환경에서는 다중 BLE 장치(안전모, 안전조끼 등)와 동시에 안정적인 멀티 커넥션(Multi-connection)을 유지하는 데 인터페이스 및 드라이버 제약이 컸음.</li>
        <li>단일 스마트폰 앱이 여러 센서 노드와 직접 통신할 때 발생하는 데이터 병목 현상과 연결 끊김 문제를 해결해야 했음.</li>
        <li>특히 앱 화면에서 <strong style="color: #fff;">작업자들의 착용 상태를 실시간으로 개별 모니터링</strong>할 수 있도록 데이터 전송 안정성 확보가 필요함.</li>
      </ul>
    </div>
    <div style="background: rgba(16, 185, 129, 0.1); padding: 20px; border-radius: 8px; margin-bottom: 48px; border: 1px solid rgba(16, 185, 129, 0.2);">
      <h4 style="color: #34d399; font-size: 1.1rem; margin-top: 0; margin-bottom: 12px;">💡 해결 방안: ESP32 중계기(Gateway) 아키텍처 도입</h4>
      <ul style="margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; font-size: 0.95rem; color: #cbd5e1;">
        <li>앱 인벤터의 통신 제약을 극복하기 위해 <strong style="color: #fff;">ESP32 1대를 중간 '마스터 중계기(Gateway)'로 추가 배치</strong>하여 하드웨어 레벨에서 네트워크 홉을 분리함.</li>
        <li>앱에서 실시간 관제 화면을 검증하기 위해 <strong style="color: #fff;">우선 2인(Worker A, Worker B)의 데이터를 처리하는 프로토타입</strong>으로 구축함.</li>
      </ul>
    </div>

    <!-- 3. 문제 해결 및 피드백 반영 -->
    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; font-weight: 700;">3. 문제 해결 및 피드백 반영 (Troubleshooting)</h2>
    
    <h3 style="color: #fbbf24; font-size: 1.2rem; margin-bottom: 16px; margin-top: 32px;">⚠️ Issue 1: BLE RSSI 신호 세기 불안정 및 오작동</h3>
    <ul style="margin-bottom: 32px; padding-left: 20px; display: flex; flex-direction: column; gap: 12px;">
      <li><strong style="color: #cbd5e1;">현상:</strong> 공사 현장의 장애물 및 주변 환경 요인으로 인해 RSSI 원시 데이터(Raw Data)가 순간적으로 튀어서, 거리가 가까움에도 불구하고 미착용으로 오인식해 부저가 울리는 현상 발생.</li>
      <li><strong style="color: #fff;">해결책:</strong> 소프트웨어 필터링 도입. RSSI 값을 연속으로 10회 측정하여 평균값을 산출하는 <strong style="color: #818cf8;">이동 평균(Moving Average) 방식의 필터링 로직</strong>을 소프트웨어에 적용하여 거리 측정의 신뢰도를 대폭 향상시킴.</li>
    </ul>

    <h3 style="color: #fbbf24; font-size: 1.2rem; margin-bottom: 16px; margin-top: 32px;">⚠️ Issue 2: 현장 적응을 위한 외형 및 다중 인식 고려</h3>
    <ul style="margin-bottom: 48px; padding-left: 20px; display: flex; flex-direction: column; gap: 12px;">
      <li><strong style="color: #cbd5e1;">하드웨어 내구성:</strong> 산업 현장의 열악한 내습/내열 환경을 고려하여 3D 프린팅 케이스 제작 시 일반 PLA 대신 <strong style="color: #fff;">PETG 필라멘트</strong>를 사용하여 내구성을 보완함.</li>
      <li><strong style="color: #cbd5e1;">다중 장치 혼선 방지:</strong> 여러 작업자가 함께 근무하는 환경을 고려하여, 고유 <strong style="color: #fff;">MAC 주소 기반의 2차 필터링 사설망 구조</strong>를 설계하여 타 장치와의 혼선을 예방함.</li>
    </ul>

    <!-- 4. 결과 분석 및 기대 효과 -->
    <h2 style="color: #818cf8; font-size: 1.6rem; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; font-weight: 700;">4. 결과 분석 및 기대 효과</h2>
    <ul style="margin-bottom: 16px; padding-left: 20px; display: flex; flex-direction: column; gap: 16px;">
      <li>
        <strong style="color: #fff; font-size: 1.1rem; display: block; margin-bottom: 4px;">🎯 안전율 제고</strong>
        <span style="color: #94a3b8;">안전장비 미착용 및 낙상 사고를 실시간으로 자동 관제하여 현장 골든타임 확보 가능.</span>
      </li>
      <li>
        <strong style="color: #fff; font-size: 1.1rem; display: block; margin-bottom: 4px;">🚀 네트워크 확장성</strong>
        <span style="color: #94a3b8;">하드웨어 중계기 구조 덕분에 향후 작업자 장비가 늘어나더라도 앱 소스코드 수정 최소화 및 원활한 다중 제어 기대.</span>
      </li>
    </ul>

  </div>
</div>

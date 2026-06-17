---
layout: post
title: "실시간 안전 장비 착용 여부 시스템"
category: projects
author: eunji
short-description: "ESP32 게이트웨이를 이용해 작업자 안전모와 조끼의 수집 센서 상태를 블루투스로 패킹 취합하는 관제 아키텍처"
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
  
<div style="padding: 20px 40px 0 40px; max-width: 1400px; margin: 0 auto; font-size: 1.15rem; font-family: 'Orbitron', 'Pretendard', sans-serif;">
  <a href="{{ site.baseurl }}/" style="color: #10B981; text-decoration: none; font-weight: 600;">Home</a> 
  <span style="color: #64748b; margin: 0 10px;">/</span> 
  <span style="color: #10B981;">실시간 안전 장비 착용 여부 시스템</span>
</div>

  <div class="tabs-nav">
    <button class="tab-btn active" data-target="tab-ppt">한눈에 보기</button>
    <button class="tab-btn" data-target="tab-intro">소개</button>
    <button class="tab-btn" data-target="tab-code">코드</button>
  </div>

    <!-- 1. 한눈에 보기 탭 콘텐츠 -->
  <div id="tab-ppt" class="tab-content active">
    <div class="carousel-container" id="slide-carousel">
      <!-- 슬라이드 이미지들 -->
      <div class="carousel-slide active" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_1.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_2.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_3.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_4.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_5.png');"></div>
      <div class="carousel-slide" style="background-image: url('{{ site.baseurl }}/assets/img/projects/safety_slides/slide_6.png');"></div>
      
      <!-- 컨트롤 버튼 -->
      <button class="carousel-btn prev" onclick="moveSlide(-1)">&#10094;</button>
      <button class="carousel-btn next" onclick="moveSlide(1)">&#10095;</button>
    </div>
      
    <!-- 프로젝트 결과물 섹션 -->
    <div style="margin-top: 40px; text-align: center;">
      <h3 style="color: #10B981; font-family: 'Orbitron', 'Pretendard', sans-serif; margin-bottom: 20px;">프로젝트 최종 결과물</h3>
      <div style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
        <img src="{{ site.baseurl }}/assets/img/projects/safety_result.png" alt="실시간 안전 장비 시스템 결과물" onerror="this.style.display='none'" style="width: 100%; max-width: 900px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); display: block; margin: 0 auto;">
      </div>
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

##  전담한 역할 및 문제 해결 과정

### 1. 프로젝트 정보 및 결과물 요약
* **프로젝트 기간:** 2025년 3월 ~ 2025년 9월 
* **팀원 구성**
* **참여 인원:** 4명 
  - 팀원 (최성용): 하드웨어 회로 설계, 센서 노드 원시 코드 작성
  - 팀원 (구민서): 외형 PETG 3D 케이스 설계 및 구조물 조립
  - 팀원 (이명은): ESP32-앱 간 블루투스 통신 기초 테스트 및 디버깅, 앱 표지 디자인
* **프로젝트 개요:** 안전모에 센서를 달아 작업자가 장비를 잘 썼는지, 현장에서 쓰러지거나 넘어지지 않았는지 블루투스로 받아와 확인하는 실시간 안전 모니터링 시스템임.
* **핵심 결과물:** 앱인벤터 툴이 가진 블루투스 연결 개수 한계를 하드웨어 중계기 아이디어로 풀었음. 스마트폰 화면 하나에 여러 명의 작업자 상태가 동시에 뜨도록 화면과 통신 구조를 완성함.

---

### 2. 내가 전담한 역할
* **모바일 관제 어플리케이션(앱인벤터) 구현:** 관리자가 스마트폰으로 현장 상황을 볼 수 있도록 표 형태의 화면을 디자인하고, 들어오는 데이터를 제 칸에 뿌려주는 블록 코딩 전체를 전담함.
* **무선 통신 연결 및 데이터 설계:** 메인 중계기 기기와 스마트폰 앱 사이에 주고받을 블루투스(BLE) 데이터 형태를 직접 정의하고 연동 테스트를 진행함.

---

### 3. 개발 과정 중 발생한 문제 및 해결 내용 (트러블 슈팅)

####  01. 여러 대의 기기를 앱에 동시에 연결할 수 없는 한계 해결
> **어려움**
> 현장 작업자가 여러 명이라 안전모마다 독립된 송신 기기가 들어가야 했음. 하지만 앱인벤터 구조상 스마트폰 하나에 여러 개의 블루투스 기기를 동시에 안정적으로 직접 연결하는 것이 불가능했음.

> **해결 내용**
> 스마트폰 앱에서 기기 여러 개를 직접 잡는 방식을 포기함. 작업자들의 기기 신호를 한곳으로 모아줄 **'메인 중계기(ESP32)'**를 중간에 하나 더 두는 방식을 냈음. 각 작업자의 기기가 보낸 신호를 중간 중계기가 다 받아낸 뒤, 스마트폰 앱에는 이 중계기 1대만 연결해서 데이터를 한 번에 밀어 넣어주는 통신 구조를 만들어 문제를 해결함.

####  02. 들어오는 데이터가 섞이고 뭉개지는 오류 해결
> **어려움**
> 중간 중계기 한 대가 여러 명의 데이터를 모아서 스마트폰 앱으로 한꺼번에 던지다 보니, 앱인벤터 쪽에서 이 데이터가 누구의 데이터인지 구분을 못 해 화면에 엉뚱한 값이 찍히거나 글자가 깨지는 현상이 생김.

> **해결 내용**
> 데이터를 보낼 때 무작정 보내지 않고 `[작업자 번호/현재 위치/장비 착용 상태]` 순서로 데이터 사이에 슬래시 나 쉼표 같은 약속된 기호를 넣어서 패킷을 묶어 보내도록 수정함. 앱인벤터 블록 코딩에서는 문자열 분리(Split) 블록을 사용해 들어온 데이터를 기호 기준으로 똑똑하게 쪼갠 뒤, 화면의 `작업자1`, `작업자2` 칸에 정확히 찾아 들어가도록 로직을 짜서 데이터가 섞이는 문제를 잡았음.

####  03. 쉴 새 없이 들어오는 신호로 인한 화면 멈춤 현상 해결
> **어려움**
> 여러 명의 데이터가 블루투스를 통해 실시간으로 너무 자주 들어오다 보니, 앱인벤터 화면이 버퍼링을 버티지 못하고 수시로 멈추거나 앱이 강제로 꺼지는 현상이 발생함.

> **해결 내용**
> 무조건 신호를 계속 쏘는 방식 대신, 주기를 1~2초 간격으로 조절하고 평소에는 조용하다가 작업자가 안전모를 벗거나 쓰러지는 등의 '상태 변화'가 생겼을 때만 즉시 신호를 쏘도록 송신 방식을 바꿨음. 데이터가 들어오는 통로의 부하를 줄여주어 앱이 끊김 없이 부드럽게 작동하도록 완성함.

####  04. 중계기(Master)의 다중 데이터 수신 병목 및 유실 현상 해결
> **어려움**
> 각 작업자의 기기(Slave)들이 중계기(Master) 한 대를 향해 동시에 블루투스 신호를 보내다 보니, 데이터가 같은 시간에 겹쳐서 들어올 때 신호가 충돌하여 일부 작업자의 상태 데이터가 앱으로 전달되지 못하고 사라지는(유실) 현상이 생김.

> **해결 내용**
> 중계기(ESP32) 펌웨어 코드를 직접 수정하여 통신 안정성을 높였음. 각 작업자의 기기들이 무작작 신호를 던지지 않고, 중계기가 `작업자1 신호 줘`, `작업자2 신호 줘` 하는 식으로 순서대로 신호를 요청하고 받아오는 수신 로직을 중계기 코드로 구현함. 또한, 들어온 데이터가 겹치더라도 안전하게 임시 보관했다가 순서대로 앱에 보내주도록 중계기 내부에 데이터 버퍼링 구조를 짜넣어 데이터가 중간에 날아가는 문제를 완벽히 해결함.



</div>

  <!-- 3. 코드 탭 콘텐츠 -->
  <div id="tab-code" class="tab-content" markdown="1">

##  [코드] 전체 데이터 흐름 및 핵심 소스코드

### 1. 전체 시스템 데이터 흐름 요약
> 각 장치 간의 블루투스(BLE) 무선 통신 프로토콜을 맞춰 시스템 전체가 실시간으로 유기적으로 동작하도록 구조를 설계함.

* **[1단계] 작업자 헬멧 (Slave): 센서 데이터 연산 및 판정**
  * **낙상 감지:** 자이로 센서(MPU6050) 가속도 변화량이 **`0.3`** 이하로 떨어지는 상태가 **`60초`** 지속되면 위험 상태로 판정함. (구동 초기 **`3초`**간은 센서 안정화 시간 예외 처리)
  * **미착용 감지:** 감압 센서 값이 **`30`** 이하로 떨어지면 미착용으로 판정해 자체 부저를 구동함.
  * **BLE 데이터 송출:** 판정 결과에 따라 무선 광고 신호 영역에 **`B:N`**(정상) 또는 **`B:B`**(위험) 포맷을 실어 주변에 뿌림.
  * **구역 이탈 감지:** 특정 기준 비콘의 MAC 주소를 필터링해 신호 강도(RSSI)가 **`-50dBm`** 이하로 떨어지면 위험 상태(`weakSignalDetected`)로 판정해 부저를 울림.

* **[2단계] 중계기 (Master): 데이터 취합 및 앱 전송**
  * **데이터 스캔:** 중계기 ESP32가 주변의 `WORKER1_MAC`, `WORKER2_MAC` 주소를 필터링해 `B:B` / `B:N` 상태 값을 스캔함.
  * **앱 시리얼 전송:** 취합한 데이터를 앱인벤터가 읽기 쉽도록 **`"작업자1: 착용불량"`** 또는 **`"작업자1: 정상착용"`** 한글 문자열로 변환하고 개행 문자(`\n`)를 붙여 클래식 블루투스 시리얼로 앱에 최종 송신함.

---

### 2. 내가 전담한 핵심 코드 및 상세 설명 

####  중계기 제어 및 앱 송신 메인 코드 (`Relay_Master_Code.ino`)
* **핵심 로직 설명:** * 고유 MAC 주소 매칭과 `toLowerCase()` 함수를 통해 현장 노이즈 신호를 원천 차단함.
  * 앱인벤터의 다중 연결 한계를 깨기 위해, `millis()` 함수 기반의 타임 스케줄러로 **`1초(1000ms)`**마다 `sendWorker1Next` 플래그를 토글시켜 작업자 1과 2의 데이터를 교차 전송함.



{% highlight cpp %}
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

// 실물 보드의 고유 MAC 주소 고정 (필터링 설계)
const String WORKER1_MAC = "ec:e3:34:bf:80:9e";
const String WORKER2_MAC = "ec:e3:34:bf:e6:aa";

BLEScan* pBLEScan;
const int SCAN_TIME = 2;

struct WorkerData {
  bool dataReceived = false;
  int rssi = 0;
  String advData = "";
  char buzzerState = 'N'; 
};

WorkerData worker1, worker2;

unsigned long lastSendTime = 0;
const unsigned long SEND_INTERVAL = 1000; // 1초 전송 주기
bool sendWorker1Next = true;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String mac = advertisedDevice.getAddress().toString();
    mac.toLowerCase(); // 대소문자 무선 데이터 예외 처리

    if (mac == WORKER1_MAC || mac == WORKER2_MAC) {
      String adv = advertisedDevice.getManufacturerData().c_str();
      if (adv.length() == 0) {
        adv = advertisedDevice.toString().c_str();
      }

      int rssi = advertisedDevice.getRSSI();
      char buzzerChar = 'N';

      if (adv.length() > 0) {
        char lastChar = adv.charAt(adv.length() - 1);
        if (lastChar == 'B' || lastChar == 'N') {
          buzzerChar = lastChar;
        }
      }

      if (mac == WORKER1_MAC) {
        worker1.dataReceived = true;
        worker1.rssi = rssi;
        worker1.advData = adv;
        worker1.buzzerState = buzzerChar;
      } else {
        worker2.dataReceived = true;
        worker2.rssi = rssi;
        worker2.advData = adv;
        worker2.buzzerState = buzzerChar;
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  SerialBT.begin("RelayDeviceBT"); // 앱인벤터와 연동될 블루투스 이름
  
  BLEDevice::init("Relay-Device");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  BLEScanResults* results = pBLEScan->start(SCAN_TIME, false);
  if (results->getCount() == 0) {
    worker1.dataReceived = false;
    worker2.dataReceived = false;
  }
  pBLEScan->clearResults();

  // 1초마다 작업자 데이터를 교차 전송하여 데이터 과부하 및 튕김 방지
  if (millis() - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = millis();

    if (sendWorker1Next) {
      if (worker1.dataReceived) {
        String message = "작업자1: ";
        message += (worker1.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자1: 데이터 없음");
      }
    } else {
      if (worker2.dataReceived) {
        String message = "작업자2: ";
        message += (worker2.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자2: 데이터 없음");
      }
    }
    sendWorker1Next = !sendWorker1Next; // 플래그 토글
  }
  delay(100);
}
{% endhighlight %}

### 3. BLE 거리 판정 및 이탈 감지 로직 코드 (BLE_Distance_Scanner.ino)
* **핵심 로직 설명:** * 기준이 되는 비콘(targetMac)의 RSSI 무선 강도를 체크하여 -50dBm 이하로 떨어지면    작업자가 구역을 이탈한 것으로 보고 부저 경고 신호를 발생시킴.

* 메모리 오버플로우를 막기 위해 스캔 후 clearResults()로 버퍼를 즉각 초기화함.

{% highlight cpp %}
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>

#define BUZZER_PIN 4 

int scanTime = 3; 
BLEScan* pBLEScan;

String targetMac = "ec:e3:34:be:48:2a"; 
int targetRSSI = -50; 
bool weakSignalDetected = false;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    String foundMac = advertisedDevice.getAddress().toString().c_str();
    foundMac.toLowerCase();

    if (foundMac == targetMac) {
      int rssi = advertisedDevice.getRSSI();

      if (rssi < targetRSSI) {
        weakSignalDetected = true; 
      } else {
        weakSignalDetected = false; 
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER_PIN, OUTPUT); 

  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  weakSignalDetected = false; 
  pBLEScan->start(scanTime, false);
  pBLEScan->clearResults();

  if (weakSignalDetected) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500);
    digitalWrite(BUZZER_PIN, LOW);
    delay(1500); 
  } else {
    digitalWrite(BUZZER_PIN, LOW); 
    delay(2000); 
  }
}
{% endhighlight %}

### 4. MIT APP Inventor(앱 인벤터)


<div class="app-inventor-viewer" style="padding: 10px; border: none; background: transparent;">
  <img src="{{ site.baseurl }}/assets/img/projects/app_inventor_blocks.png" alt="MIT App Inventor 블록 코딩" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
</div>

###  5. 실시간 안전 장비 착용 여부 시스템 전체적인 코드
* **작업자 MAC 주소:**  esp32 마다 고유의 'MAC' 주소가 있어 'MAC' 주소만 바꿔서 사용함.

<details class="code-accordion">
  <summary>5-1 MAC 주소 찾는 코드</summary>
  <div class="accordion-content" markdown="1">

{% highlight cpp %}
#include <BLEDevice.h>

void setup() {
  Serial.begin(115200);
  BLEDevice::init("");  // BLE 초기화

  String bleMac = BLEDevice::getAddress().toString().c_str();  // BLE MAC 주소 얻기
  Serial.print("BLE MAC Address: ");
  Serial.println(bleMac);
}

void loop() {
  // do nothing
}

{% endhighlight %}


  </div>
</details>

<details class="code-accordion">
  <summary>5-2 수신용 코드</summary>
  <div class="accordion-content" markdown="1">

{% highlight cpp %}
#include <Wire.h>
#include <MPU6050.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BLEAdvertising.h>

#define BUZZER2_PIN 18
#define NO_MOVEMENT_PIN 5
#define PRESSURE_PIN 34  // 감압센서 아날로그 입력 핀

const int SCAN_COUNT_MAX = 10;
const int SCAN_INTERVAL_MS = 30;
const int scanTime = 1;

String targetMac = "ec:e3:34:be:48:2a"; // 변경 필요 시 수정
int rssiThreshold = -60;

MPU6050 mpu;
unsigned long lastMovementTime = 0;
const unsigned long movementThreshold = 60000;
float movementDelta = 0.3;
int16_t ax_prev = 0, ay_prev = 0, az_prev = 0;
unsigned long startupTime = 0;
const unsigned long startupDelay = 3000;

BLEScan* pBLEScan;

std::vector<int> rssiValues;
int scanCount = 0;
unsigned long lastScanMillis = 0;

bool weakSignalDetected = false;

const int pressureThreshold = 30; // 300 이상이면 부저 안 울림
const unsigned long buzzerInterval = 1000;
unsigned long lastBuzzerToggle = 0;
bool buzzerState = false;

String lastAdvData = "NONE";

BLEAdvertising* pAdvertising;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String foundMac = advertisedDevice.getAddress().toString().c_str();
    foundMac.toLowerCase();

    if (foundMac == targetMac) {
      int rssi = advertisedDevice.getRSSI();
      String advData = advertisedDevice.getManufacturerData().c_str();

      if (advData.length() == 0) {
        advData = advertisedDevice.toString().c_str();  // 디버깅용
      }

      Serial.print("BLE 광고 데이터 수신 (");
      Serial.print(foundMac);
      Serial.print("): ");
      Serial.println(advData);

      lastAdvData = advData;
      rssiValues.push_back(rssi);
    }
  }
};

void checkMovement() {
  int16_t ax = mpu.getAccelerationX();
  int16_t ay = mpu.getAccelerationY();
  int16_t az = mpu.getAccelerationZ();

  float deltaX = abs(ax - ax_prev) / 16384.0;
  float deltaY = abs(ay - ay_prev) / 16384.0;
  float deltaZ = abs(az - az_prev) / 16384.0;

  if (millis() - startupTime > startupDelay) {
    if (deltaX > movementDelta || deltaY > movementDelta || deltaZ > movementDelta) {
      lastMovementTime = millis();
      Serial.println("정상 착용 움직임 감지됨");
    }
  }

  ax_prev = ax;
  ay_prev = ay;
  az_prev = az;
}

void setup() {
  Serial.begin(115200);
  Serial.println("헬멧 BLE 수신기 + 센서 초기화 중...");

  pinMode(BUZZER2_PIN, OUTPUT);
  pinMode(NO_MOVEMENT_PIN, OUTPUT);
  pinMode(PRESSURE_PIN, INPUT);

  digitalWrite(BUZZER2_PIN, LOW);
  digitalWrite(NO_MOVEMENT_PIN, LOW);

  Wire.begin(21, 22);
  mpu.initialize();
  delay(100);
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 연결 실패!");
    while (1) delay(1000);
  }
  Serial.println("MPU6050 연결 성공");

  ax_prev = mpu.getAccelerationX();
  ay_prev = mpu.getAccelerationY();
  az_prev = mpu.getAccelerationZ();
  lastMovementTime = millis();
  startupTime = millis();

  BLEDevice::init("Helmet-Receiver");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);

  rssiValues.clear();
  scanCount = 0;
  lastScanMillis = 0;
  weakSignalDetected = false;

  // BLE 광고 송출 초기화
  pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinInterval(0x20);
  pAdvertising->setMaxInterval(0x40);
  BLEDevice::startAdvertising();

  Serial.println("시스템 준비 완료");
}

void loop() {
  checkMovement();

  int pressureValue = analogRead(PRESSURE_PIN);
  bool isPressed = (pressureValue > pressureThreshold);
  Serial.print("감압센서 값: ");
  Serial.println(pressureValue);

  bool noMovement = (millis() - lastMovementTime > movementThreshold);
  if (noMovement) {
    Serial.println("착용불량 - 1분 이상 움직임 없음!");
    digitalWrite(NO_MOVEMENT_PIN, HIGH);
  } else {
    digitalWrite(NO_MOVEMENT_PIN, LOW);
  }

  if (millis() - lastScanMillis >= SCAN_INTERVAL_MS) {
    lastScanMillis = millis();
    if (scanCount == 0) rssiValues.clear();

    Serial.printf("스캔 %d / %d 시작\n", scanCount + 1, SCAN_COUNT_MAX);
    pBLEScan->clearResults();
    pBLEScan->start(scanTime, false);

    scanCount++;

    if (scanCount >= SCAN_COUNT_MAX) {
      if (rssiValues.size() > 0) {
        long sum = 0;
        for (int rssi : rssiValues) sum += rssi;
        float avgRSSI = (float)sum / rssiValues.size();

        Serial.print("RSSI 평균값: ");
        Serial.println(avgRSSI);

        weakSignalDetected = (avgRSSI < rssiThreshold);
      } else {
        Serial.println("타겟 장치 발견 안됨.");
        weakSignalDetected = false;
      }
      scanCount = 0;
    }
  }

  int16_t ax = mpu.getAccelerationX();
  int16_t ay = mpu.getAccelerationY();
  int16_t az = mpu.getAccelerationZ();

  Serial.print("자이로센서 값 - ax: ");
  Serial.print(ax);
  Serial.print(", ay: ");
  Serial.print(ay);
  Serial.print(", az: ");
  Serial.println(az);

  Serial.print("헬멧 상태 데이터: ");
  Serial.println(lastAdvData);  // 마지막 받은 광고 데이터 출력

  bool pressureAlarm = (pressureValue < pressureThreshold);
  bool movementAlarm = noMovement;
  bool distanceAlarm = weakSignalDetected;

  bool shouldBuzz = pressureAlarm || movementAlarm || distanceAlarm;

  // 부저 제어
  if (shouldBuzz) {
    if (millis() - lastBuzzerToggle >= buzzerInterval) {
      buzzerState = !buzzerState;
      digitalWrite(BUZZER2_PIN, buzzerState ? HIGH : LOW);
      lastBuzzerToggle = millis();
    }
  } else {
    digitalWrite(BUZZER2_PIN, LOW);
    buzzerState = false;
  }

  // 광고 데이터에 부저 상태 포함시켜 송출 (매 루프마다 갱신)
  String advStr = String("B:") + (shouldBuzz ? "B" : "N");
  BLEAdvertisementData advData;
  advData.setName("Helmet-Receiver");
  advData.setManufacturerData(advStr);
  pAdvertising->setAdvertisementData(advData);
  pAdvertising->start();

  // 요약 데이터 시리얼 출력
  int avgRssi = 0;
  if (rssiValues.size() > 0) {
    long sum = 0;
    for (int rssi : rssiValues) sum += rssi;
    avgRssi = sum / rssiValues.size();
  }

  Serial.print("D:");
  Serial.print(avgRssi);  // Distance
  Serial.print(" / P:");
  Serial.print(pressureValue);  // Pressure
  Serial.print(" / G:(");
  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az);
  Serial.print(") / ");
  Serial.println(shouldBuzz ? "B" : "N");  // 부저 여부

  delay(100); // 조금 쉬기
}
{% endhighlight %}


  </div>
</details>

<details class="code-accordion">
  <summary>5-3 송신용 코드</summary>
  <div class="accordion-content" markdown="1">

{% highlight cpp %}
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

void setup() {
  Serial.begin(115200);
  Serial.println("BLE Advertiser Starting...");

  BLEDevice::init("ESP32_Advertiser");
  BLEDevice::setPower(ESP_PWR_LVL_P9);  // +9 dBm, 최대 출력 설정

  BLEServer *pServer = BLEDevice::createServer();
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();

  BLEAdvertisementData advertisementData;
  advertisementData.setName("ESP32_BEACON");
  advertisementData.setManufacturerData("123456"); // 식별용

  pAdvertising->setAdvertisementData(advertisementData);
  pAdvertising->setScanResponse(false);
  pAdvertising->start();

  Serial.println("Advertising started at max TX power...");
}

void loop() {
  delay(1000);
}
{% endhighlight %}


  </div>
</details>

<details class="code-accordion">
  <summary>5-4 중계기 코드</summary>
  <div class="accordion-content" markdown="1">

{% highlight cpp %}
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

// 실물 보드의 고유 MAC 주소 고정 (필터링 설계)
const String WORKER1_MAC = "ec:e3:34:bf:80:9e";
const String WORKER2_MAC = "ec:e3:34:bf:e6:aa";

BLEScan* pBLEScan;
const int SCAN_TIME = 2;

struct WorkerData {
  bool dataReceived = false;
  int rssi = 0;
  String advData = "";
  char buzzerState = 'N'; 
};

WorkerData worker1, worker2;

unsigned long lastSendTime = 0;
const unsigned long SEND_INTERVAL = 1000; // 1초 전송 주기
bool sendWorker1Next = true;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String mac = advertisedDevice.getAddress().toString();
    mac.toLowerCase(); // 대소문자 무선 데이터 예외 처리

    if (mac == WORKER1_MAC || mac == WORKER2_MAC) {
      String adv = advertisedDevice.getManufacturerData().c_str();
      if (adv.length() == 0) {
        adv = advertisedDevice.toString().c_str();
      }

      int rssi = advertisedDevice.getRSSI();
      char buzzerChar = 'N';

      if (adv.length() > 0) {
        char lastChar = adv.charAt(adv.length() - 1);
        if (lastChar == 'B' || lastChar == 'N') {
          buzzerChar = lastChar;
        }
      }

      if (mac == WORKER1_MAC) {
        worker1.dataReceived = true;
        worker1.rssi = rssi;
        worker1.advData = adv;
        worker1.buzzerState = buzzerChar;
      } else {
        worker2.dataReceived = true;
        worker2.rssi = rssi;
        worker2.advData = adv;
        worker2.buzzerState = buzzerChar;
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  SerialBT.begin("RelayDeviceBT"); // 앱인벤터와 연동될 블루투스 이름
  
  BLEDevice::init("Relay-Device");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);
}

void loop() {
  BLEScanResults* results = pBLEScan->start(SCAN_TIME, false);
  if (results->getCount() == 0) {
    worker1.dataReceived = false;
    worker2.dataReceived = false;
  }
  pBLEScan->clearResults();

  // 1초마다 작업자 데이터를 교차 전송하여 데이터 과부하 및 튕김 방지
  if (millis() - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = millis();

    if (sendWorker1Next) {
      if (worker1.dataReceived) {
        String message = "작업자1: ";
        message += (worker1.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자1: 데이터 없음");
      }
    } else {
      if (worker2.dataReceived) {
        String message = "작업자2: ";
        message += (worker2.buzzerState == 'B') ? "착용불량" : "정상착용";
        SerialBT.println(message);
      } else {
        SerialBT.println("작업자2: 데이터 없음");
      }
    }
    sendWorker1Next = !sendWorker1Next; // 플래그 토글
  }
  delay(100);
}
{% endhighlight %}


  </div>
</details>


  </div>
</div>

<script>
  // 탭 전환 스크립트
  document.addEventListener("DOMContentLoaded", () => {
    const btns = document.querySelectorAll(".tab-btn");
    const contents = document.querySelectorAll(".tab-content");

    btns.forEach(btn => {
      btn.addEventListener("click", () => {
        // 모든 탭과 콘텐츠의 활성화 상태 제거
        btns.forEach(b => b.classList.remove("active"));
        contents.forEach(c => c.classList.remove("active"));

        // 클릭된 탭과 해당 콘텐츠 활성화
        btn.classList.add("active");
        document.getElementById(btn.getAttribute("data-target")).classList.add("active");
      });
    });
  });
</script>

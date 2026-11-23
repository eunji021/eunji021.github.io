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

<style>
/* Code Editor Box & Syntax Highlighting Styles */
#tab-code .highlighter-rouge,
#tab-code .code-editor-box {
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 8px;
  margin: 14px 0 24px 0;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
  font-family: 'Consolas', 'Fira Code', 'Courier New', monospace;
}

#tab-code .code-editor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #1e293b;
  border-bottom: 1px solid #334155;
  padding: 8px 14px;
}

#tab-code .code-editor-dots {
  display: flex;
  align-items: center;
  gap: 6px;
}

#tab-code .mac-dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  display: inline-block;
}
#tab-code .mac-dot.red { background: #ef4444; }
#tab-code .mac-dot.yellow { background: #f59e0b; }
#tab-code .mac-dot.green { background: #10b981; }

#tab-code .code-lang-label {
  color: #94a3b8;
  font-size: 0.75rem;
  font-weight: 700;
  font-family: 'Consolas', monospace;
  margin-left: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

#tab-code .code-copy-btn {
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #10b981;
  padding: 4px 10px;
  border-radius: 5px;
  font-size: 0.75rem;
  font-weight: 600;
  font-family: 'Pretendard', sans-serif;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
#tab-code .code-copy-btn:hover {
  background: #10b981;
  color: #0b1412;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
}
#tab-code .code-copy-btn.copied {
  background: #10b981 !important;
  color: #0b1412 !important;
}

#tab-code .highlight,
#tab-code pre {
  background: #0f172a !important;
  margin: 0 !important;
  padding: 16px 18px !important;
  border: none !important;
  border-radius: 0 !important;
  overflow-x: auto !important;
}

#tab-code .highlight code,
#tab-code pre code {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  color: #e2e8f0 !important;
  font-family: 'Consolas', 'Courier New', monospace !important;
  font-size: 0.88rem !important;
  line-height: 1.65 !important;
  display: block;
}

/* Syntax Highlighting Tokens */
#tab-code .highlight .k, #tab-code .highlight .kd, #tab-code .highlight .kn,
#tab-code .highlight .kp, #tab-code .highlight .kr, #tab-code .hl-keyword {
  color: #569cd6 !important; font-weight: bold;
}
#tab-code .highlight .kt, #tab-code .hl-type {
  color: #4ec9b0 !important; font-weight: bold;
}
#tab-code .highlight .s, #tab-code .highlight .s1, #tab-code .highlight .s2,
#tab-code .highlight .sb, #tab-code .highlight .sc, #tab-code .hl-string {
  color: #ce9178 !important;
}
#tab-code .highlight .c, #tab-code .highlight .c1, #tab-code .highlight .cm, #tab-code .hl-comment {
  color: #6a9955 !important; font-style: italic;
}
#tab-code .highlight .m, #tab-code .highlight .mi, #tab-code .highlight .mf,
#tab-code .highlight .mo, #tab-code .hl-number {
  color: #b5cea8 !important;
}
#tab-code .highlight .nf, #tab-code .highlight .nc, #tab-code .hl-func {
  color: #dcdcaa !important;
}
#tab-code .highlight .n, #tab-code .highlight .nv, #tab-code .highlight .vi,
#tab-code .highlight .na, #tab-code .hl-ident {
  color: #9cdcfe !important;
}
#tab-code .highlight .o, #tab-code .highlight .ow, #tab-code .highlight .p, #tab-code .hl-op {
  color: #d4d4d4 !important;
}
#tab-code .highlight .nb, #tab-code .highlight .bp, #tab-code .hl-builtin {
  color: #4ec9b0 !important;
}
</style>

### 2-1. 중계기 핵심 코드 (전담 파트)

**1. 작업자별 BLE 데이터 구분**

```cpp
const String WORKER1_MAC = "ec:e3:34:bf:80:9e";
const String WORKER2_MAC = "ec:e3:34:bf:e6:aa";

WorkerData worker1, worker2;
```

**2. BLE 데이터 수신 및 작업자 구분**

```cpp
void onResult(BLEAdvertisedDevice advertisedDevice) override {
    String mac = advertisedDevice.getAddress().toString();
    mac.toLowerCase();

    if (mac == WORKER1_MAC || mac == WORKER2_MAC) {
        String adv = advertisedDevice.getManufacturerData().c_str();

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
```

**3. BLE 및 Bluetooth Serial 초기화**

```cpp
SerialBT.begin("RelayDeviceBT");

BLEDevice::init("Relay-Device");
pBLEScan = BLEDevice::getScan();
pBLEScan->setAdvertisedDeviceCallbacks(
    new MyAdvertisedDeviceCallbacks()
);
pBLEScan->setActiveScan(true);
```

**4. 작업자별 상태 정보 앱으로 전송**

```cpp
if (millis() - lastSendTime >= SEND_INTERVAL) {
    lastSendTime = millis();

    if (sendWorker1Next) {
        if (worker1.dataReceived) {
            String message = "작업자1: ";
            message += (worker1.buzzerState == 'B')
                ? "착용불량" : "정상착용";
            SerialBT.println(message);
        } else {
            SerialBT.println("작업자1: 데이터 없음");
        }
    } else {
        if (worker2.dataReceived) {
            String message = "작업자2: ";
            message += (worker2.buzzerState == 'B')
                ? "착용불량" : "정상착용";
            SerialBT.println(message);
        } else {
            SerialBT.println("작업자2: 데이터 없음");
        }
    }

    sendWorker1Next = !sendWorker1Next;
}
```

### 2-2. 수신용, 송신용 핵심 코드

**1. 착용불량 상태 판단 (수신용)**

```cpp
bool pressureAlarm = (pressureValue < pressureThreshold);
bool movementAlarm = noMovement;
bool distanceAlarm = weakSignalDetected;

bool shouldBuzz = pressureAlarm || movementAlarm || distanceAlarm;
```

**2. 착용 상태를 BLE 광고 데이터로 송신 (수신용)**

```cpp
String advStr = String("B:") + (shouldBuzz ? "B" : "N");

BLEAdvertisementData advData;
advData.setName("Helmet-Receiver");
advData.setManufacturerData(advStr);

pAdvertising->setAdvertisementData(advData);
pAdvertising->start();
```

**3. BLE 송신 장치 초기화 (송신용)**

```cpp
BLEDevice::init("ESP32_Advertiser");
BLEDevice::setPower(ESP_PWR_LVL_P9);
```

**4. BLE 광고 데이터 설정 및 송신 (송신용)**

```cpp
BLEAdvertisementData advertisementData;
advertisementData.setName("ESP32_BEACON");
advertisementData.setManufacturerData("123456");

pAdvertising->setAdvertisementData(advertisementData);
pAdvertising->setScanResponse(false);
pAdvertising->start();
```

### 2-3. ESP32의 각 MAC 주소 찾는 코드

**1. ESP32 BLE MAC 주소 확인**

```cpp
BLEDevice::init("");

String bleMac = BLEDevice::getAddress().toString().c_str();

Serial.print("BLE MAC Address: ");
Serial.println(bleMac);
```

<script>
(function() {
  function attachCodeHeaders() {
    var codeBlocks = document.querySelectorAll('#tab-code div.highlighter-rouge, #tab-code .code-editor-box');
    codeBlocks.forEach(function(block) {
      if (block.querySelector('.code-editor-header')) return;
      var header = document.createElement('div');
      header.className = 'code-editor-header';
      header.innerHTML = '<div class="code-editor-dots"><span class="mac-dot red"></span><span class="mac-dot yellow"></span><span class="mac-dot green"></span><span class="code-lang-label">C++</span></div><button class="code-copy-btn" type="button">📋 복사</button>';
      var btn = header.querySelector('.code-copy-btn');
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        var codeEl = block.querySelector('code');
        if (!codeEl) return;
        var text = codeEl.innerText || codeEl.textContent;
        navigator.clipboard.writeText(text).then(function() {
          btn.innerHTML = '✓ 복사됨';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.innerHTML = '📋 복사';
            btn.classList.remove('copied');
          }, 2000);
        }).catch(function(err) {
          console.error('복사 실패:', err);
        });
      });
      block.insertBefore(header, block.firstChild);

      // Client syntax highlight fallback if not highlighted by Rouge
      var codeEl = block.querySelector('code');
      if (codeEl && !codeEl.querySelector('span')) {
        var raw = codeEl.textContent;
        var escaped = raw
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;');
        escaped = escaped.replace(/(\/\/[^\n]*)/g, '<span class="hl-comment">$1</span>');
        escaped = escaped.replace(/(".*?")/g, '<span class="hl-string">$1</span>');
        escaped = escaped.replace(/\b(const|void|bool|char|int|override|if|else|true|false|new|return)\b/g, '<span class="hl-keyword">$1</span>');
        escaped = escaped.replace(/\b(String|WorkerData|BLEAdvertisedDevice|BLEDevice|BLEScan|BLEAdvertisementData|BluetoothSerial)\b/g, '<span class="hl-type">$1</span>');
        escaped = escaped.replace(/\b(onResult|getAddress|toString|toLowerCase|getManufacturerData|c_str|length|charAt|getRSSI|begin|init|getScan|setAdvertisedDeviceCallbacks|setActiveScan|millis|println|setAdvertisementData|setName|setPower|setScanResponse|start|print)\b/g, '<span class="hl-func">$1</span>');
        escaped = escaped.replace(/\b(\d+)\b/g, '<span class="hl-number">$1</span>');
        codeEl.innerHTML = escaped;
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachCodeHeaders);
  } else {
    attachCodeHeaders();
  }
  document.querySelectorAll('.tab-btn').forEach(function(b) {
    b.addEventListener('click', function() {
      setTimeout(attachCodeHeaders, 50);
    });
  });
})();
</script>

---

### 3. BLE 거리 판정 및 이탈 감지 로직 코드 (BLE_Distance_Scanner.ino)
* **핵심 로직 설명:** * 기준이 되는 비콘(targetMac)의 RSSI 무선 강도를 체크하여 -50dBm 이하로 떨어지면    작업자가 구역을 이탈한 것으로 보고 부저 경고 신호를 발생시킴.

* 메모리 오버플로우를 막기 위해 스캔 후 clearResults()로 버퍼를 즉각 초기화함.

```cpp
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
```

### 4. MIT APP Inventor(앱 인벤터)

<details class="code-accordion">
  <summary>5. 실시간 안전 장비 착용 여부 시스템 전체적인 코드</summary>
  <div class="accordion-content" markdown="1">

* **작업자 MAC 주소:**  esp32 마다 고유의 'MAC' 주소가 있어 'MAC' 주소만 바꿔서 사용함.



<details class="code-accordion">
  <summary>5-1 MAC 주소 찾는 코드</summary>
  <div class="accordion-content" markdown="1">



```cpp
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
```



  </div>
</details>


<details class="code-accordion">
  <summary>5-2 수신용 코드</summary>
  <div class="accordion-content" markdown="1">


```cpp
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
```



  </div>
</details>


<details class="code-accordion">
  <summary>5-3 송신용 코드</summary>
  <div class="accordion-content" markdown="1">



```cpp
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
```



  </div>
</details>


<details class="code-accordion">
  <summary>5-4 중계기 코드</summary>
  <div class="accordion-content" markdown="1">


```cpp
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
```



  </div>
</details>


  </div>
</details>

#include <SPI.h>

#define LDR_PIN A0         // 조도 센서 핀
#define LED_BUILTIN 13
unsigned long ledStartTime = 0; // LED 켜진 시간 기록
bool isCounting = false;        // LED가 켜져 있는 상태에서 40초 카운트 여부

int LED_DURATION = 40000;

void setup() {
  Serial.begin(9600);        // 시리얼 통신 시작
  pinMode(LED_BUILTIN, OUTPUT); 
}

void loop() {
  // 조도 센서 상태 확인
  checkLDR();

  if (isCounting && millis() - ledStartTime >= LED_DURATION) {
    isCounting = false; // 카운트 종료
    Serial.println("40초가 경과되었습니다. 조도 센서를 다시 확인합니다.");
  }
  delay(1000);
}


void checkLDR() {
  if (!isCounting) { 
    int ldrValue = analogRead(LDR_PIN);
    Serial.println(ldrValue);

    if (ldrValue > 300) {
      Serial.println("ON");
      ledStartTime = millis(); 
      isCounting = true;
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)       
    }

    else {
      Serial.println("OFF");
    }

    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(1000);
  }
}

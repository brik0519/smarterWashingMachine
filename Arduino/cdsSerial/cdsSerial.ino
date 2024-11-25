#include <SPI.h>

#define LDR_PIN A0         // 조도 센서 핀
#define LED_BUILTIN 13
#define LED_DURATION = 40000;

bool isCounting = false;        // LED가 켜져 있는 상태에서 40초 카운트 여부
int ldrValue = 0;

void setup() {
  Serial.begin(9600);        // 시리얼 통신 시작
  pinMode(LED_BUILTIN, OUTPUT); 
}

void loop() {
  // 조도 센서 상태 확인
  checkLDR();
  // Serial.println(ldrValue);
  delay(1500);
}


void checkLDR() {
  ldrValue = analogRead(LDR_PIN);
  if (ldrValue > 500/*900*/) {
    Serial.println("ON");
    digitalWrite(LED_BUILTIN, HIGH);
    isCounting = true;
  }

  else {
    Serial.println("OFF");
    digitalWrite(LED_BUILTIN, LOW);   // LED 끄기
    isCounting = false;
  }
}

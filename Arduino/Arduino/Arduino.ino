// WebLED

String inByt;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);  // Corrected pinMode

    Serial.begin(9600);
    Serial.setTimeout(10);
}

void loop() {
    // Keep loop empty as per original code
}

void serialEvent() {
    inByt = Serial.readStringUntil('\n');

    if (inByt == "on")
        digitalWrite(LED_BUILTIN, HIGH);
    else if (inByt == "off")  // Corrected == for comparison
        digitalWrite(LED_BUILTIN, LOW);
    else
        Serial.println("Unknown command");  // Optional message for clarity
}

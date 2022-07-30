int gelenveri1 = 0;
int led = 5;
void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  //digitalWrite(LEDpini, HIGH); // 13 numaralı pine bağlı LED'i yak
 //delay(1000);      // 1 saniye bekle( LED 1 saniye boyunca yanar)
 //digitalWrite(LEDpini, LOW);  // 13 numaralı pine bağlı LED'i söndür
 //delay(1000);      // 1 saniye bekle( LED 1 saniye boyunca yanar)
 if (Serial.available()>0)
 {
  gelenveri1 = Serial.read();
 }
 if (gelenveri1 == '1')
 {
  digitalWrite(led,HIGH);
  }
  else if (gelenveri1 == '0')
 {
  digitalWrite(led,LOW);
  }
 }

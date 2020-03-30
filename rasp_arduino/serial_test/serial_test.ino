char dataString[50] = {0};
int a =0; 
int b =0;

void setup() {
Serial.begin(9600);              //Starting serial communication
pinMode(LED_BUILTIN, OUTPUT);
}
  
void loop() {
  a++;                          // a value increase every loop
  sprintf(dataString,"%02X",a); // convert a value to hexa 
  Serial.println(dataString);   // send the data
  delay(1000);                  // give the loop some break
  b = Serial.read();
  if (b >= 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000); 
    digitalWrite(LED_BUILTIN, LOW);
  }
}

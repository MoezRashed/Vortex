const int r1=13,r2=12,l1=11,l2=10;
char t;
void setup() {
// put your setup code here, to run once:
pinMode(r1,OUTPUT);   //right motors forward
pinMode(r2,OUTPUT);   //right motors reverse
pinMode(l1,OUTPUT);   //left motors forward
pinMode(l2,OUTPUT);   //left motors reverse
}
void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()){
  t = Serial.read();
 }
if(t == 'F'){            //move forward
  digitalWrite(r1,HIGH);
  digitalWrite(r2,LOW);
  digitalWrite(l1,HIGH);
  digitalWrite(l2,LOW);
}
else if(t == 'B'){      //move reverse
  digitalWrite(r1,LOW);
  digitalWrite(r2,HIGH);
  digitalWrite(l1,LOW);
  digitalWrite(l2,HIGH);
}
else if(t == 'L'){      //turn right--left side rotates in forward & right side rotate in reverse direction
  digitalWrite(r1,HIGH);
  digitalWrite(r2,LOW);
  digitalWrite(l1,LOW);
  digitalWrite(l2,HIGH);
  delay(200);
  t = 'S';
}
else if(t == 'R'){      //turn left--right side rotate in forward direction ,left side motors rotate in reverse
  digitalWrite(r1,LOW);
  digitalWrite(r2,HIGH);
  digitalWrite(l1,HIGH);
  digitalWrite(l2,LOW);
  delay(200);
  t = 'S';
}
else if(t == 'S'){      //STOP (all motors stop)
  digitalWrite(r1,LOW);
  digitalWrite(r2,LOW);
  digitalWrite(l1,LOW);
  digitalWrite(l2,LOW);
}
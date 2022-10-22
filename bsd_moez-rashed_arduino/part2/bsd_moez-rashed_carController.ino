#define m1in1 9
#define m1in2 10
#define m2in1 11
#define m2in2 12
#define up 5
#define down 6
#define left 7
#define right 8

//m1 for motor number 1
//motor 1 left wheel
//motor 2 right wheel
//m2 for motor number 2
//in1 for input1 
//in2 for input2

void setup() 
{
 pinMode(m1in1,OUTPUT);
 pinMode(m1in2,OUTPUT);
 pinMode(m2in1,OUTPUT);
 pinMode(m2in2,OUTPUT);
 pinMode(up,INPUT);
 pinMode(down,INPUT);
 pinMode(left,INPUT);
 pinMode(right,INPUT);
}

void loop() 
{
  if(digitalRead(up) == HIGH)
  {
    delay(50);
  	forward();
  }
  if(digitalRead(down) == HIGH)
  {
    delay(50);
    back();
  }
  if (digitalRead(left) == HIGH)
  {
    delay(50);
    left();
  }
  if (digitalRead(right) == HIGH)
  {
    delay(50);
    right();
  }

}
void forward()
{
  digitalWrite(m1in1,HIGH);
  digitalWrite(m2in1,HIGH);
  digitalWrite(m1in1,LOW);
  digitalWrite(m1in2,LOW);
}
void back()
{
  digitalWrite(m1in1,LOW);
  digitalWrite(m2in1,LOW);
  digitalWrite(m1in2,HIGH);
  digitalWrite(m2in2,HIGH);
}
void left()
{
  digitalWrite(m1in1,LOW);
  digitalWrite(m2in1,HIGH);
  digitalWrite(m1in2,LOW);
  digitalWrite(m2in2,LOW);
}
void right()
{
  digitalWrite(m1in1,HIGH);
  digitalWrite(m2in1,LOW);
  digitalWrite(m1in1,LOW);
  digitalWrite(m2in2,LOW);
}
#define red 9
#define yellow 10
#define green 11
#define button 12
int flag;
void setup() 
{
 pinMode(red,OUTPUT);
 pinMode(yellow,OUTPUT);
 pinMode(green,OUTPUT);
 pinMode(button,INPUT);
 digitalWrite(button, HIGH); 
 flag = 0;
}

void loop() 
{
  if(flag == 0)
  {
    delay(500);
  	redd();
  }
  else if(flag == 1)
  {
    delay(500);
     yelloww();
  }
  else if ( flag ==2)
  {
    delay(500);
      greenn();
  }
  if (digitalRead(button) == LOW)
  {
    delay(10);
       flag++;
    if(flag > 2) 
    {
     flag = 0;
    }
  }
  
}
void redd()
{
  digitalWrite(red,HIGH);
  digitalWrite(yellow,LOW);
  digitalWrite(green,LOW);
}
void yelloww()
{
  digitalWrite(red,LOW);
  digitalWrite(yellow,HIGH);
  digitalWrite(green,LOW);
}
void greenn()
{
  digitalWrite(red,LOW);
  digitalWrite(yellow,LOW);
  digitalWrite(green,HIGH);
}
      
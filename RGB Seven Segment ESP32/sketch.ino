int a = 2, b = 4, c = 16, d = 17, e = 5, f = 18, g = 21;
int sevensegpins[7] = {2, 4, 16, 17, 5, 18, 21};
int red = 12, green = 13, blue = 14;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello, ESP32!");
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // use fn or fn2
  digitalWrite(red, HIGH);
  fn2();
  digitalWrite(green, HIGH);
  fn2();
  digitalWrite(green, HIGH);
  digitalWrite(red, LOW);
  fn2();
  digitalWrite(green, LOW);
  delay(10); // this speeds up the simulation
}

void fn(){
  //nine
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
  delay(1000);

  //eight
  digitalWrite(e, HIGH);
  delay(1000);

  //seven
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(f, LOW);
  digitalWrite(g, LOW);
  delay(1000);

  //six
  digitalWrite(b, LOW);
  digitalWrite(f, HIGH);
  digitalWrite(g, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(d, HIGH);
  delay(1000);

  //five
  digitalWrite(e, LOW);
  delay(1000);

  //four
  digitalWrite(a, LOW);
  digitalWrite(d, LOW);
  digitalWrite(b, HIGH);
  delay(1000);

  //three
  digitalWrite(f, LOW);
  digitalWrite(a, HIGH);
  digitalWrite(d , HIGH);
  delay(1000);

  //two 
  digitalWrite(c, LOW);
  digitalWrite(e, HIGH);
  delay(1000);

  //one 
  digitalWrite(a, LOW);
  digitalWrite(g, LOW);
  digitalWrite(d, LOW);
  digitalWrite(e, LOW);
  digitalWrite(c, HIGH);
  digitalWrite(b, HIGH);
  delay(1000);

  //zero 
  digitalWrite(a, HIGH);
  digitalWrite(f, HIGH);
  digitalWrite(e, HIGH);
  digitalWrite(d, HIGH);
  delay(1000);

  //turnoff
  digitalWrite(e, LOW);

}

void fn2(){
  int data[10][7] ={
    {1,1,1,1,0,1,1},  //9
    {1,1,1,1,1,1,1},  //8
    {1,1,1,0,0,0,0},  //7
    {1,0,1,1,1,1,1},  //6
    {1,0,1,1,0,1,1},  //5
    {0,1,1,0,0,1,1},  //4
    {1,1,1,1,0,0,1},  //3
    {1,1,0,1,1,0,1},  //2
    {0,1,1,0,0,0,0},  //1
    {1,1,1,1,1,1,0}   //0
  };
  for(int i = 0; i<10; i++){
    for(int j = 0; j<7; j++){
      digitalWrite(sevensegpins[j], data[i][j]);
    }
    delay(1000);
  }
}

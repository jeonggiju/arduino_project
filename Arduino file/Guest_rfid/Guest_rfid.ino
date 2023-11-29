#include <SPI.h>  //spi통신에 필요한 라이브러리
//SPI : 마이크로컨트롤러와 주변장치 사이의 데이터를 주고받을 때 사용되는 통신 방식
// Serial 병행 Interface
#include <MFRC522.h>   //MFRC522 RFID모듈에 필요한 라이브러리
// SS(Slave Select), RST(Reset)

#define SS_PIN 10 
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
int Red = 8;  //핀번호로 선언 (핀번호가 뭐임)
int Green = 7;   //핀번호로 선언
int buzzer = 6;    //핀번호로 선언

void setup() 
{
  Serial.begin(9600);   // 시리얼 통신 초기화
  SPI.begin();      // spi 버스 초기화 
  pinMode(Red,OUTPUT);
  pinMode(Green,OUTPUT);
  mfrc522.PCD_Init();   // MFRC522 초기화 
}

void loop() 
{
  digitalWrite(Red, HIGH); // 초기에 빨강을 키고, 초록을 끔
  digitalWrite(Green,LOW);
  
  // 새로운 카드 찾기
  if ( ! mfrc522.PICC_IsNewCardPresent())  //새로운 RFID 카드가 있는지 확인하는 함수(RFID가 처음에 있는건지 확인)
  {
    return;
  }
  // 카드중 하나 선택
  if ( ! mfrc522.PICC_ReadCardSerial()) //새로운 카드가 발견되면 이함수를 호출하여 카드 선택
  {
    return;
  }

  digitalWrite(Red, LOW);  //red 꺼짐
  digitalWrite(Green,HIGH);   //green 켜짐 
  tone(buzzer,50,50);    //시에조부저(핀번호, 음역대, 길이)
  String content= "";
  byte letter;
  
  //mfrc522.uid(고유식별자).size(크기)
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "); //0x10 -> 16 
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  } //카드의 UID(고유식별자)가 16진수 및 연결된 문자열 형식으로 시리얼 모니터에 출력

  Serial.println();
  delay(1500);
} 
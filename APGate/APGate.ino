/*APGate: Arduino PhotoGate para uso nos dispositivos de portas óticas dos Laboratórios
de Ensino de Física do CCA-UFSCar.

Esse codigo deve ser carregado na placa Arduino UNO que deve operar em conjunto
com os hardwares Shield Photogate e sensores óticos. A comunicao deve ser feita com
o software PyQtGate.

Joao Teles, jteles@cca.ufscar.br

Last update: Mar 03 2017
--------------------------------

Analog pin 0: canal 1
Analog pin 1: canal 2
Analog pin 2: canal 3
Analog pin 3: canal 4
Analog pin 4: canal 5
Analog pin 5: canal 6
*/

//Defines for setting and clearing register bits for faster analog readings
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

char msg_co[9] = "Photo_co";	//Signal from pc asking to connect
char msg_ok[9] = "Photo_ok";	//Connection confirmation signal from arduino to pc
char msg_st[9] = "Photo_st";	//Signal from pc confirming sequence start
char msg_t[9]  = "01234567";

int i, v;
int y[7];
unsigned char a, b;
unsigned char a3, a2, a1, a0;
unsigned long t0, t;

void erase_msg_t(void);


void setup() {

	// set prescale to 16 (128 is the default) for improving analog reading time:
	sbi(ADCSRA,ADPS2) ;
	cbi(ADCSRA,ADPS1) ;
	cbi(ADCSRA,ADPS0) ;

	Serial.begin(115200);

}


void loop() {

	//Read command message from pc:
	if (Serial.available() > 7)
		for (i = 0; i < 8; i++) msg_t[i] = Serial.read();

	//Confirmation of pc-arduino communication:
	if (strcmp(msg_t, msg_co) == 0) {
		for (i = 0; i < 8; i++) 
			Serial.write(msg_ok[i]);
	}

	//Acquisition start:
	if (strcmp(msg_t, msg_st) == 0) {

		while (Serial.available() < 2) {}
		a = Serial.read();
		b = Serial.read();

		v = ((int)a)*256 + ((int)b);

		t0 = micros();

		while (Serial.available() == 0) {

			y[0] = analogRead(0);
			y[1] = analogRead(1);
			y[2] = analogRead(2);
			y[3] = analogRead(3);
			y[4] = analogRead(4);
			y[5] = analogRead(5);

			t = micros()-t0;

			for (i = 0; i < 6; i++) {
				a1 = y[i]/256;
				a0 = y[i]%256;

				Serial.write(a0);
				Serial.write(a1);
			}

			a3 = t/16777216;
			a2 = (t-a3*16777216)/65536;
			a1 = (t-a3*16777216-a2*65536)/256;
			a0 = t-a3*16777216-a2*65536-a1*256;

			Serial.write(a0);
			Serial.write(a1);
			Serial.write(a2);
			Serial.write(a3);

			delay(v);

		}

		erase_msg_t();

	}

}


void erase_msg_t(void) {
	for (i = 0; i < 8; i++) msg_t[i] = '9';
}


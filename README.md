# photogate

Photogate for Learning Physics Labs has the purpose to develop and deploy the hardware and software system used in the learning physics laboratories of the "Centro de Ciências Agrárias" in the "Universidade Federal de São Carlos" (CCA-UFSCar). The project uses the Arduino platform for signal acquisition.

The software part is composed of two codes. The first one, PyQtGate is developed in PyQt and corresponds to the graphical user interface that runs in a laptop or desktop computer. The second one, APGate, is the code to be uploaded in the Arduino, written in C, that will communicate with the PyQtGate code in order to transfer the photogate signals.

The hardware part is composed of three pieces: (i) the Arduino Uno board, (ii) a Photogate Shield for Arduino Uno developed in this project and (iii) set of optical sensors, also developed in this project. The Photogate Shield for Arduino circuit designs can be also acessed and forked in the EasyEDA website (https://easyeda.com/jocoteles).

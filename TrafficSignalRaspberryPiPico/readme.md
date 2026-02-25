<h1>Traffic Signal using Raspberry Pi Pico Micropython</h1>
🚥<p>Suppose you are a traffic police sitting in your office on side of the road, from where you can view and control the traffic.</p>
<p>You are having three traffic light coloured pushdown buttons kept on your table, whose wires are connected to the traffic lights and a LCD board aside the lights.</p>
<p>On pressing a button, the respective coloured light gets toggled, and correspondingly a message appears on the LCD.</p>
<h2>More Specifically:</h2>
<ul>
  <li>On pressing the red button, the red light gets toggled, that is, if the red light is on, it will get turned off, and vice versa.</li>
  <li>Same for the yellow and green lights. </li>
  <li>Corresponding to the on lights, a message will show up on the LCD board. For red light, the message is 'Stop!', for yellow 'Wait!', and for green 'Go!'. The message string will appear on the lcd corresponding to the lights. </li>
</ul>
<h2>Platform, program and tools used</h2>
<ul>
  <li>🛠️Wokwi Raspberry Pi Pico Micropython for creating circuit and writing python program.</li>
  <li>Raspberry Pi Pico, an RP2040 microcontroller board with dual-core ARM Cortex-M0+ processor, 264k of internal RAM, and flexible Programmable I/O (PIO) feature.</li>
  <li>LEDs and Pushdown buttons.</li>
  <li>LCD 1602 I2C, an I2C configuration LCD with 2 lines, 16 characters per line.</li>
</ul>

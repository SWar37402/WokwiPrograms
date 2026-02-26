<h1>Roll The Dice!🎲</h1>
<a href='https://wokwi.com/projects/456998192450626561'>link</a>
<h4>Ever played a game where a player needs to roll two dice during their turn? And the player who gets gets same number on both the dice wins the game.</h4>
<h2>🧰Tools and programs</h2>
<li>
  <ul>Wokwi simulation platform</ul>
  <ul>Raspberry Pi Pico 2040 microcontroller board.</ul>
  <ul>Two separate seven segment displays to show the numbers on each dice.</ul>
  <ul>📺 An LCD to display dice and numbers, and respective string messages.</ul>
  <ul>A potentiometer to control the throw of each dice.</ul>
</li>
<h2>Stepwise simulation execution</h2>
<li>
  <ul>Initially the potentiometer is at left most position, denoting 0 potentiometer value, and righmost point denotes 65535 potentiometer value.</ul>
  <ul>If the user rotates knob to less or equal to one-third of total rotation, none of the dice will roll.</ul>
  <ul>If the user places knob between one-third to two-third of total rotation from inital position, one dice will roll.</ul>
  <ul>Similiarly if the user places knob between two-third to complete rotation from initial position, both the dice will roll.</ul>
  <ul>Both the dice current status will be displayed on LCD.</ul>
  <ul>If both the seven segment displays the same number, a "You Win" string will additionally be displayed and the program will stop to execute, the user will have to restart the program for new game.</ul>
</li>



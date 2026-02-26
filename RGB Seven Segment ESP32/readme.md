<h1>RGB Seven Segment Countdown🚦</h1>
<a href = 'https://wokwi.com/projects/456410006691360769'>link</a>
<h4>Virtual Simulation of a traffic signal changing signals every 10 seconds with countdown from 9 to 0.</h4>
<h2>Tools and program</h2>
<li>
  <ul>⌨️ESP 32 microcontroller.</ul>
  <ul>RBG LED</ul>
  <ul>Seven Segment Display(1 digit)</ul>
</li>
<p>The simulation starts with blinking of red light and countdown of 9 to 0 on seven segment, with delay of 1s. Then the light changes to yellow, and further to green repeating the same process. The program runs in cyclic order, meaning red light blinks after green light.</p>
<p>The Arduino Sketch File, contains two independent functions fn() and fn2() for displaying the countdown on seven segment from 9 to 0 with 1s delay, for each colour lights respectively. Both functions perform the same work with different programming logic.</p>

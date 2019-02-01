# Bowling Kata #
This is a project to help introduce Test Driven Development (TDD). Here you will create an application to score a game of bowling.

## Bowling ##
A game of bowling contains ten frames. A frame may have one, two, or three throws of the bowling ball depending on how many pins are knocked down. A frame does not score until it is complete.

[Bowling via WikiPedia](https://en.wikipedia.org/wiki/Bowling)

## Scoring ##
The scoring of a frame is dependent on the number of pins knocked down and on which throw of the ball knocked those pins down.

The game is scored as the sum of all frames.

### A Basic Frame ###
If the total of pins knocked down is less then ten, a frame has two throws and the score is the some of those throws.

e.g. First throw is one, and second throw is two, the score is three

### A Spare Frame ###
If the first throw knocks down fewer than ten pins, and the total of the first throw and the second throw equal ten then the frame is a spare frame.

A spare frame has two throws plus the first throw of the next frame.

e.g., First throw is one, second throw is nine, third throw is four and fourth throw is two. Then the first frame contains a one, a nine, and a four for a total of fourteen. The second frame contains a four and a two for a total of six.

### A Strike Frame ###
If the first throw of a frame knocks down all ten pins then it is a strike frame. A strike frame has three throws in it; however, all throws except the first also populate other frames.

e.g., First throw knocks down all ten pins. Second throw knocks down three pins. Third throw knocks down seven pins. Fourth throw knocks down eight pins. Fifth throw knocks down one pin.

The first frame is a strike containing a ten, a three, and a seven for a total of twenty.

The second frame is a spare containing a three, a seven, and an eight for a total of eighteen.

The third frame is a basic frame containing an eight and a one for a score of nine.

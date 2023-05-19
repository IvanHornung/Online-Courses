# Animation Library Classes

## Animation
- Records the current 'value' of the property being animated
- Records the status of the animation (currently running, stopped, etc)
- status: 'stopped', yPosition: 110px

## AnimationController
- Starts, stops, restarts the animation
- Records the duration of the animation
- duration: 1 second, start(), stop()

## Tween
- Described the range that the value being animated spans
- start with a value of 0px end with a value of 200px

## AnimatedBuilder
- Takes an animation and a 'builder' function.
- Every time the animation ticks (changes value), builder reruns
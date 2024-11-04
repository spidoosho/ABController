# ABController

Test task 2 for Next Generation Test Runner Internship.

## Structure

1. `NumberGenerator` package is the Program A defined in the task. It implements class `Generator` which in `init`
   requires `min_value` and `max_value`. Then user can call `start_cycle` which will read command and print output until
   user inputs `SHUTDOWN_OUTPUT_CONST`.
2. `SubprocessController` package handles subprocess handling. It starts subprocess by running command
   of `sys.executable`, path to the package and given arguments. Then it gives subprocess input to stdin and prints
   output from subprocess' stdout. Subprocess is closed using shutdown phrase.
3. `main.py` is simulating user usage by running `NumberGenerator` using `SubprocessController`, generating
   100 integers and calculating average and median.

> **_NOTE:_**  I would like to apologize for my humor (naming the project ABC).

## Decision-making

- I decided to add entrypoint for the `NumberGenerator`, since it works with `stdin` and `stdout`, which makes it like a
  standalone program in my opinion. I would consider it as a package if it would work with method parameters and output
  instead.
    - It still can be used as a package, meaning it would work the same without the entrypoint (for those few developers
      who need it as a package).
    - `class Generator` might seem a bit of an overkill in this example, but I opt for
      it because of future proofing. Someone someday might need expand the project, for example to save a last
      generated integer and for that case is the class perfect.
    - `min_value` and `max_value` could be edited using commands (like `SetMax 100`). I did not like the idea, because I
      want to keep the one argument commands.
- `SubprocessController` is left without entrypoint instead, because it should be used as a controller to control
  something and not as a standalone program. I decided for the `subprocess` package (instead of `multiprocessing`) for
  the ease of piping `stdin` and`stdout`. The issue I ran into is that it cannot recognize when the `stdout` is empty
  (meaning it cannot recognize if subprocess printed one or more lines). That is why this controller works only for one
  line outputs only.
- Program B is split into`main.py` and `SubprocessController` because it did not make sense to me to have it in the same
  program. I feel like it is more like a user using controller package to run generator package for his own use of
  manipulations of random integers. I may look at a situation differently, but I think my thinking makes sense.

## Feelings and impressions

I would like to thank you for this task. I really enjoyed solving this task and of the 4 JetBrains internship tasks that
I have decided to do, I like this one the most. Not because it is easy or the easiest, but because it is challenging
enough and requires proper thinking to get it right.

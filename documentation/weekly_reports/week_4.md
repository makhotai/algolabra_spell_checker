# Weekly report 4
This week I implemented unrestricted variant of Damerau-Levenshtein distance based on restricted variant that I have made myself earlier. This edit distance algorithm was much more complicated to understand than I expected. So I ended up replayng educational videos for a couple of times and drawning schemes how it should work. Afterall, I took some logic of pseudocode from Wikipedia as a reference. Running tests was quite useful: I detected some mistakes in my code, which resulted in longer distance calcilations than it should be. The problem was wrong symbol (1 insted of i), which took me about half of an hour to realize.

I added the full distance version to spell checker and UI, so the application uses advanced version. Since I have not run any performance tests I decided not to delete restricted version yet.

In addition, I implemented some tests using Hypothesis. I also would like to run performance tests and do more emperical testing next week.

Writing documentation was quite time-consuming. Unfortunately, I have not enough time this week to write `implementation.md` properly. So I am going to polish that next week.


## Time spent

| date | time |
| ----- | ------------- |
| 21.9  | 2 h            |
| 22.9  | 1.5 h            |
| 23.9  | 3 h            |
| 24.9  | 3 h            |
| 25.9  | 2 h            |
| 26.9  | 2 h            |

**week total: 13.5 h**
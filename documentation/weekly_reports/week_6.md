# Weekly report 6
This week I wrote the user guide and improved the sorting of suggested words. The program now suggests spelling corrections based first on edit distance and then on the length of the common prefix when the distances are equal, instead of using only alphabetical order.

For example, before the program would return:
```
possible suggetion(s) for 'ystava': 
('antava', 2)
('ostaa', 2)
('ostaja', 2)
('ottava', 2)
**('ystävä', 2)**
```

And now it returns:
```
possible suggetion(s) for 'ystava': 
**('ystävä', 2)**
('antava', 2)
('ostaa', 2)
('ostaja', 2)
('ottava', 2)
```
So I guess that this change to make the spelling suggestions more useful in most cases.

Additionally, I modified the UI code so that the program asks the user which word list to load.

I also ran the comparison test that I mentioned in my week 5 report. I described test results in `testing.md` in [Empirical testing section](./documentation/testing.md#empirical-testing)

I also added a couple of unit tests for sorting spelling suggestions (based on distance and then words' beginning).


## Time spent

| date | time |
| ----- | ------------- |
| 6.10  | 1 h            |
| 9.10  | 2 h            |
| 10.10  | 5 h            |

**week total: 8 h**
# Generate random Sprint/Branch name.

SPRINTGEN is a simple python program that randomly picks two words from an approved list to create a Sprint/Branch name.

GETRAW generates an approved list of words for use by SPRINTGEN. The raw list should contain a single word on each line. Words that are between 4 and 8 characters in length and pass a profanity check are saved to an approved file in JSON format for use by SPRINTGEN.

The [wordlist.txt](https://www.mit.edu/~ecprice/wordlist.10000) included in this project is credited to [Eric Price](https://www.cs.utexas.edu/~ecprice/)

## Profanity Check
Profanity checks are performed using the `alt-profanity-check` library. This is documented [here](https://pypi.org/project/alt-profanity-check)
Use pip to install:
```
 pip install alt-profanity-check
```

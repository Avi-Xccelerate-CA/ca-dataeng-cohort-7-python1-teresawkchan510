# FTDS-week0-test

### Problem 1

There is a dispensary in need of a tool that gives its very sickly patients medicine according to their needs. Every patient has 6 attributes and each of those attributes have a vitamin supplement that increases their respective attribute by 10 points, namely:

- HP
- Attack
- Defense
- Special Attack
- Special Defense
- Speed


Because the vitamin supplements only increase attribute points by 10, specific needs of a patient that aren’t in the multiple of 10 aren’t taken into account.

Therefore, the dispensary also has injections that decrease an attribute by 1 so that they can account for those values that aren’t multiples of 10.

Given a list of integers as input that is in order of HP, Attack, Defense, Special Attack, Special Defense and Speed as the needs of 1 patient, create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.


Note that the patient can only be treated if his total attribute needs do not exceed 500 and that each attribute’s maximum value is 250. If a patient doesn’t meet these requirements, the dispensary will not give medicine out to them.

Example 1:

```
Needs of the patient (Input):

[250, 0, 250, 0, 0, 0] → needs 250 HP and 250 Defense

250 HP = 25 vitamins * 10

250 Defense = 25 vitamins * 10

Output:
[(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
```


Example 2:

```
Needs of the patient (Input):

[223, 12, 126, 0, 37, 12] → needs 223 HP, 12 Attack, 126 Defense, 37 Special Defense and 12 Speed

223 HP = 23 vitamins * 10 – 7 injections * 1

12 Attack = 2 vitamins * 10 – 8 injections * 1

126 Defense = 13 vitamins * 10 – 4 injections * 1

37 Special Defense = 4 vitamins * 10 – 3 injections * 1

12 Speed = 2 vitamins * 10 – 8 injections * 1

Output:
[(23,7), (2,8), (13,4), (0,0),(4,3), (2,8)]
```

Example 3:

```
Needs of the patient (Input):

[500, 1, 2, 3, 4, 5]

Sum of total points is more than 500. Therefore, no medicine is given.

Output:
‘No medicine given’
```

Example 4:

```
Needs of the patient (Input):

[260, 1, 2, 3, 4, 5]

Sum of total points is less than 500 but one of the attributes has a need of more than 260. Therefore, no medicine is given.

Output:
‘No medicine given’
```

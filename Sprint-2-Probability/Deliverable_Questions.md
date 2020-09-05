# Hermione Granger and the Distributions of Probability

## Disclaimer

This problem set is a work of fan fiction. Hermione Granger and related characters were created by J.K. Rowling. Please don't sue me.

<img src="https://64.media.tumblr.com/d85b44001002bb249c42b27e00d8dccb/tumblr_nzrkzfmjZW1s5b5tzo1_500.jpg" width="35%" />

## Honor Code

Edit this section to include a statement of the Honor Code.

## List Your Team Members

Edit this section to include a list of everyone on your team.

## Instructions

Answer the following questions, which cover discrete probability distributions, expected values, and conditional probabilities.

You can type your answers in this document or upload a scanned handwritten file.

## Questions

### Wizard People, Dear Reader?

Hermione Granger is pretty sure she’s a witch, because she read in a book that having very curly hair is a sign of latent mystical power. Also, one time an owl landed on her head. However, she didn’t receive a letter from Hogwarts on her 11th birthday.

After reading several books and pamphlets, Hermione is pretty sure that

```
P(She's a witch) = .75
P(Not receiving a letter | She's a witch) = .03  (because owls are actually pretty dumb)
P(Not receiving a letter | She's not a witch) = .99   
```

Under these assumptions, what is the probability that Hermione really is a witch even though she didn’t get a letter?

Tip: use Bayes' Rule,

```
             P(A) * P(B | A)
P(A | B) =  -----------------
                  P(B)

where

A = She's a witch
B = Not receiving a letter

P(B) is therefore the total probability of not receiving a letter.
``` 

### Hat Problem

Hermione and Harry made it to Hogwarts!

Students arriving at Hogwarts are sorted into one of the four residential houses -- Gryffindor, Hufflepuff, Ravenclaw, and Slytherin -- by the magical Sorting Hat.

In theory, the Hat is supposed to examine each student's personality, consider his or her wishes, and then place the student into the most appropriate house. However, after a thousand years, the Hat has gotten pretty lazy, so it has simplified its sorting process into a two-step algorithm:

1. All evil students go into Slytherin, obviously.

2. Everybody else is just randomly sorted into one of the four houses, with a 40% probability of being put into Hufflepuff and a 20% probability of being put into each of the three other houses.

Hermione is shocked when she's sorted into Slytherin! She's never thought of herself as evil, but now that she considers it, becoming the future Dark Lady of Magical Britain does have some appeal...

If 10% of new Hogwarts students are evil, what is the probability that a randomly chosen Slytherin is evil?

Tip: the value you want is `P(Evil | Slytherin)`.


### Dragon's Dice

<img src="https://64.media.tumblr.com/908ee88323640428f9cbda47df177a38/tumblr_nke6rsvC3C1s5b5tzo1_500.jpg" width="35%"/>

Hermione has settled into a nice routine with her fellow Slytherins. During the day, she eats meals in the Great Hall, reads about famous Dark Wizards in the library, and attends her classes. During the evening, she practices jinxing the Hufflepuffs, does her homework, and plays wizard games with her new friends, Daphne Greengrass and Tracey Davis.

One of their games is called Dragon's Dice. It's a simple gambling game, similar to one offered at Muggle carnivals.

Hermione picks a number 1-6 and rolls three fair dice (instead of numbers, the dice are marked with enchanted, moving images of dragons). If her number comes up *k* = 1, 2, or 3 times, she wins *k* galleons. If it does not
appear on any of the dice, she loses one galleon.

What is Hermione's expected long-run win or loss from playing Dragon's Dice?

Tip: the number of successes in a roll is binomially distributed.


### Urn While You Learn

Hogwarts is filled with all kinds of wonderous magical objects: talking portraits, deadly moving stairs, secret passages, and the largest collection of magical urns in Western Europe.

There's an urn on the fourth floor with a strange property: every time Hermione takes a ball out, the urn randomly chooses and discards another ball!

Suppose the urn contains 10 black balls and 5 red balls. If Hermione draws two balls, what is the probability that the second ball is red?

### Arithmancy

The discrete uniform distribution is defined over a finite set of integer values

```
{a, a+1, a+2, ..., b}
```

each of which is equally likely to be observed.

Rolling a six-sided die is a special case of the discrete uniform distribution with `a = 1` and `b = 6`. Rolling a 20-sided die would have `a = 1` and `b = 20`.

Prove that the expected value of a discrete uniform distribution with `a = 1` and `b = n` is

```
        n + 1 
E[X] = -------
          2
```
Hint: Each of the `n` values is equally likely to be observed.

Hint-hint: There's going to be a summation. You can look up the result if you don’t remember it.


### Birthday Attack

There are a total of 40 students in Hermoine's year at Hogwarts.

Birthdays are important in the Wizarding World. Sharing a birthday with another witch or wizard can create a magical bond between the two of you, leading to all sorts of ridiculous hijinks. This is why wizard twins are always crazy.

What's the probability that no two students in Hermoine's year share the same birthday?

Tip: Assume that there are 365 possible birthdays (wizards can't be born on Leap Days) and that wizards are equally likely to be born on any day of the year.

Tip-Tip:

Suppose there are only two students, Hermoine and Draco Malfoy.

```
P(Both are born on two different days) = (365 / 365) * (364 / 365)
```

Hermoine's birthday can be on any day, but Draco's must occur randomly on one of the other 364 days.

What if there are three students? How about more?
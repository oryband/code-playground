#!/usr/bin/env python
"""
Your room is being decorated. On the largest wall you would to paint a skyline.
The skyline consists of rectangular buildings arranged in a line. The buildings are all of the same width,
but they may have different heights. The skyline shape is given as an array whose elements
specify the heights of consecutive buildings.

For example, consider an array: [1,3,2,1,2,1,5,3,3,4,2]:

          X
          X  X
     X    XXXX
     XX X XXXXX
    XXXXXXXXXXX

You would like to paint the skyline using continuous horizontal brushstrokes. Every horizontal stroke
is one unit hgih and arbtrarily wide. The goal is to calculate the minimum number of horizontal brushstrokes needed.
For example, the above shape can be painted using nine horizontal brushstrokes.

Starting from the bottom, you can paint the skyline in horizontal stripes with 1,3,2,2,1 brushstrokes per respective stripe.

Write a function that given a non-empty array consisting of N integers (represnting heights),
returns the minimum number of horizontal brushstrokes needed to paint the shape represented by the array.

The functions should return -1 if the number of brushstrokes exceeds 1,000,000,000

The answer for the above example is 9 brushstrokes.

For another example: [5,8], the function should return 8, as you must paint on horizontal stroke at each height from 1 to 8:

     X
     X
     X
    XX
    XX
    XX
    XX
    XX

For the following array: [1,1,1,1] the function should return 1, as you can paint this shape using a single horizontal stroke.

Write an EFFICIENT algorithm.
Assume 1 <= N <= 100,000 and height range is from 1 to 1,000,000,000
"""
one_billion = 1_000_000_000

def paint_skyline(skyline):
    # calculate necessary brushstrokes for each level (starting from 1)
    brushstrokes = 0
    for level in range(1, max(skyline)+1):
        # find first tower that reaches current level.
        # NOTE since level <= max(skyline), we'll definintely find at least
        # one tower that reaches the current level.
        tower = 0
        while tower < len(skyline):
            if level <= skyline[tower]:
                brushstrokes += 1
                if brushstrokes > one_billion:
                    return -1
                tower += 1
                break

            tower += 1

        # add addditional brushstrokes for every tower which DOESN'T reach
        # the current level (as long as there's another one somewhere after it
        # that does reach the current level)
        stroke_interrupted = False
        while tower < len(skyline):
            if skyline[tower] > level:
                # current tower doesn't reach current level.
                # in the next iterations we'll search fo a tower that again
                # reaches current level
                stroke_interrupted = True
            elif stroke_interrupted:  # skyline[tower] <= level
                stroke_interrupted = False

                brushstrokes += 1
                if brushstrokes > one_billion:
                    return -1

            tower += 1

    return brushstrokes


def paint_skyline_efficient(skyline):
    # add brushstrokes for every two consequent towers,
    # where the first one is higher than the second one
    brushstrokes, height_diff = 0, 0
    for tower in skyline:
        brushstrokes += (height_diff - tower) if tower < height_diff else 0
        height_diff = tower

    # add the last tower height as brushstrokes
    return brushstrokes + tower



if __name__ == '__main__':
    # print(paint_skyline([1,3,2,1,2,1,5,3,3,4,2]), 'expected: 9')
    print(paint_skyline_efficient([1,3,2,1,2,1,5,3,3,4,2]), 'expected: 9')

    # print(paint_skyline([5,8]), 'expected: 8')
    print(paint_skyline_efficient([5,8]), 'expected: 8')

    # print(paint_skyline([9]), 'expected: 9')
    print(paint_skyline_efficient([9]), 'expected: 9')

    # print(paint_skyline([1,1,1,1]), 'expected: 1')
    print(paint_skyline_efficient([1,1,1,1]), 'expected: 1')


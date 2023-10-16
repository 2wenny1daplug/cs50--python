"""// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
} 
"""

#get_string and print, with concatenation
from cs50 import get_string

answer = get_string("what's your name? ")

print("hello," + answer)
 
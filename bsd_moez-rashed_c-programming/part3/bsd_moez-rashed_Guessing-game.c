#include <stdio.h>
#include<stdbool.h>  

int main()
{
    int winningNum = 60 , numOfGuesses = 10 , yourGuess;

    bool found = false;

    while(numOfGuesses > 0)
    {   
        if(numOfGuesses == 1) printf("you have %d guess!\nEnter your guess : " , numOfGuesses);
        else printf("you have %d guesses!\nEnter your guess : " , numOfGuesses);

        scanf("%d" , &yourGuess);
        
        if(yourGuess == winningNum) 
        {
            found = true;
            break;
        }
        numOfGuesses--;
    }

    if (found == true) printf("You won!");
    else printf("You lost!");

    return 0;
}
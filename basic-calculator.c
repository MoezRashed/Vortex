#include <stdio.h>

int main()
{
    long double firstNum , secondNum;
    long double result;
    char operation;

    printf("Enter the intended operation as a symbol.\n");
    scanf("%c" , &operation);

    printf("Enter the numbers respectivley.\n");
    scanf("%LF%LF" , &firstNum , &secondNum);
    
    if(operation == '+') result = firstNum + secondNum;
    else if (operation == '-') result = firstNum - secondNum;
    else if (operation == '*') result = firstNum * secondNum;
    else if (operation == '/')
    {
        if (secondNum == 0) 
        {
            printf("Cannot divide by zero.");
            return 0;
        }
        else result = firstNum / secondNum;
    }
    else 
    {
        printf("You entered an invalid operator.");
        return 0;
    }


    printf("Result is : %LF" , result);

    return 0;
}
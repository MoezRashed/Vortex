#include <stdio.h>

int main()
{
    double firstNum , secondNum , thirdNum , average , sum;

    printf("Enter 3 numbers.\n");
    scanf("%lf%lf%lf" , &firstNum , &secondNum , &thirdNum);

    sum = firstNum + secondNum + thirdNum;
    average = sum / 3.00;

    printf("The Sum is : %lf\nThe average is : %lf" , sum , average);
    
    return 0;
}
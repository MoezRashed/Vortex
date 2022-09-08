#include <stdio.h>

char pyramid[26];

void solve(int height)
{   int index = 0;

    for (int i = 1 ; i <= height ; i++)
    {
       for(int j = 1 ; j <= height - i ; j++) 
       {
        pyramid[index] = ' ';
        index ++;
       }
       for(int j = 1 ; j <= (2 * i -1) ; j++)
       {
        pyramid[index] = '*';
        index++;
       }
       pyramid[index] = '\n';
       index++;
    }
    pyramid[index] = 0;
    for(int i = 0 ; i < index ; i++) printf("%c" , pyramid[i]);
}

int main()
{
    
    int height;

    printf("Please Enter the pyramid height : ");

    scanf("%d" , &height);
    while(height < 2 || height > 5) 
    {   
        printf("Please enter a number between 2 and 5 : ");
        scanf("%d" , &height);
    }

    solve(height);

    return 0;
}
#include <stdio.h>

int main()
{
    char colour[20];
    char pluralNoun[20];
    char celebrity[25];

    printf("Enter Colour , plural noun and celebrity Respectively.");

    scanf("%s%s%s" , colour , pluralNoun , celebrity);

    printf("roses are %s, " , colour);
    printf("%s are blue\n" , pluralNoun);
    printf("Duuuuude, I LOVE %s." , celebrity);
    return 0;
}
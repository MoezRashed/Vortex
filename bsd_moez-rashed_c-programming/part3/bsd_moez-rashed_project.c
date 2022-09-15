#include<stdio.h>
#include<math.h>

//r=Right tringle , c=circle , s=square ,p=pyramid

void square(int height)
{
   for(int i=0;i<height;i++)
   {
    for(int j=0;j<height;j++) printf("*");
    printf("\n");
   }
}

void circle(int height)
{
  float dist;
  // for horizontal movement
  for (int i = 0; i <= height; i++) 
  {
    // for vertical movement
    for (int j = 0; j <= height; j++) {
      dist = sqrt((i - height/2) * (i - height/2) +
                  (j - height/2) * (j - height/2));
      // dist should be in the range (radius - 0.5)
      // and (radius + 0.5) to print stars(*)
      if (dist > (height/2) - 0.5 && dist < (height/2) + 0.5)
        printf("*");
      else
       printf(" ");
    }
   printf("\n");
  }
}

void pyramid(int height)
{
    for(int i=1;i<=height;i++){
    for(int z=1;z<=(height-i);z++){
    printf(" ");}
    //to print *
    for(int symbol=1;symbol<=((2*i)-1);symbol++)
    printf("*");
    printf("\n");
  }
}

void R_triangle(int height)
{
for(int i=0;i<height;i++){
    for(int j=0;j<=i;j++){
        printf("*");
    }
    printf("\n");
}
}

typedef struct q{
int height;
char shape;
}S;

int main()
{
S Var;

printf("To print the following shapes enter the equivalent character\nRight triangle : r\nSquare : s\nPyramid : p\nCircle : c\n");

printf("Please enter shape character : ");
scanf("%c",&Var.shape);
printf("Please enter shape height : ");
scanf("%d",&Var.height);

while(Var.height < 2)
{
    printf("Please enter a number greater than 2 : ");
    scanf("%d",&Var.height);
}

if(Var.shape=='s') square(Var.height);
else if(Var.shape=='r') R_triangle(Var.height);
else if(Var.shape=='p') pyramid(Var.height);
else if (Var.shape=='c')circle(Var.height);
else printf("Invalid charachter!");

return 0;
}
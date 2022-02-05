// Things I didn't know

/* \0 is the null termination character and it is used to mark the end of a string. In C/C++ the null character ends the string. */
// -----INPUT-----
#include <stdio.h>
int main()
{
    printf("Hello\0World");
}
/* -----OUTPUT-----
Hello
/ -----OUTPUT----- */

/* In a for loop, all the expressions in parenthesis are optional. Two semicolons are compulsory even though there are no expressions. */
// -----INPUT-----
#include <stdio.h>
int main()
{
    for(;;) // infinite loop
    {
        printf("HelloWorld");
    }
}
/* -----OUTPUT-----
HelloWorldHelloWorldHelloWorldHelloWorldHelloWorld.....
/ -----OUTPUT----- */

/* The purpose of using extra curly braces is to provide scope-limit. */
// -----INPUT-----
#include <stdio.h>
int main()
{
    int i = 10;
    {
        int j = 5;
    }
    printf("%d %d", i, j);
}
/* -----OUTPUT-----
Status: Compilation Error
error: ‘j’ undeclared (first use in this function)
printf("%d %d", i, j);
                   ^
/ -----OUTPUT----- */
#include <limits.h>

//Function to accept three integers and either 
//return truncated output or -1 if error occurred
int doMath(int a, int b, int c)
{
    if (0 == b)
    {
        return INT_MAX - 1;
    }
    else
    {
        return ((a / b) - c);
    }
}

//compiled with: gcc -fPIC -shared -o mylib.so q6.c
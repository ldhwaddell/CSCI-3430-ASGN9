//Function to accept three integers and either 
//return truncated output or -1 if error occurred
int doMath(int a, int b, int c)
{
    if (0 == c)
    {
        return -1;
    }
    else
    {
        return ((a * b) / c);
    }
}

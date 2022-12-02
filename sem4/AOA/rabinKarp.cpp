#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;

#define d 250

void rabinKarp(char pat[], char text[], int q)
{

    int i, j;
    int M = strlen(pat);
    int N = strlen(text);
    int p=0;
    int t=0;
    int h = 1;

    for (i = 0; i < M - 1; i++)
        h = (h * d) % q;

    for (i = 0; i < M; i++)
    {
        p = (d * p + pat[i]) % q;
        t = (d * t + text[i]) % q;
    }

    for (i = 0; i < N - M; i++)
    {

        if (p == t)
        {
            bool flag = true; //
            for (j = 0; j < M; j++)
            {
                if (text[i + j] != pat[j])
                {
                    flag = false;
                    break;
                }
            }

            if (flag)
                printf("pattern was found on index %d\n", i);
        }

        if(i<N-M){
        // t = (d * t + text[i]) % q;
            t = (d*(t-text[i]*h) + text[i+M])%q;

            if(t<0)
                t = t+ q;
        }
    }
}

int main()
{

    char txt[] = "GEEKS FOR GEEKS";
    char pat[] = "GEEK";

    // A prime number
    int q = 101;

    // Function Call
    rabinKarp(pat, txt, q);


    return 0;
}
#include<stdio.h>
#include<string.h>
using  namespace std;

void search(char * pat,char* text){

    int M = strlen(pat);
    int N = strlen(text);

    for(int i=0;i<= N - M ;i++){

        int j;
        for(j = 0 ; j< M;j++){
            if(text[i+j]!= pat[j])
                break;
        }

        if(j==M)
            printf("pattern was found on index %d \n",i);

    }

}


int main(){

    char txt[] = "AABAACAADAABAAABAA";
    char pat[] = "AABA";
    search(pat, txt);


    return 0;
}
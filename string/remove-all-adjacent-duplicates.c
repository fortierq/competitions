#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct 
{
    char c;
    int n;
} repetition;

char *removeDuplicates(char *s, int k)
{
    int sz = strlen(s);
    repetition stack[sz];
    int j = -1;
    for (size_t i = 0; i < sz; i++)
    {
        if (j == -1 || s[i] != stack[j].c) {
            j++;
            stack[j].c = s[i];
            stack[j].n = 1;
        }
        else
        {
            stack[j].n++;
            if (stack[j].n == k) {
                stack[j].n = 0;
                j--;
            }
        }
    }
    char *res = (char*)malloc(sizeof(char)*sz);
    int l = 0;
    for (int k=0; k <= j; k++) {
        for (int i=0; i < stack[k].n; i++) {
            res[l] = stack[k].c;
            l++;
        }
    }
    return res;
}

int main()
{
    char *s = removeDuplicates("pbbcggttciiippooaais", 2);
    printf("%s", s);
    return 0;
}
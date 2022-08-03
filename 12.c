#include <stdio.h>

int main(void) {
    float n1, n2;
    char op;
    printf("Enter two numbers seperated by an operator (i.e. +, -, x, /,)\nE.g. 10-9\n");
    scanf("%f %c %f", &n1, &op, &n2);

    float res;
    switch(op) 
    {
    case '+':
        res = n1 + n2;
        break;
    case '-':
        res = n1 - n2;
        break;
    case 'x':
        res = n1 * n2;
        break;
    case '/':
        res = n1 / n2;
        break;
    default:
        printf("%c is an invalid operator", op);
        return 1;
    }
    printf("Your answer is %f", res);

    return 0;
}
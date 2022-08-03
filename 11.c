#include <stdio.h>

int main(void){
    float n1, n2, n3, n4;
    printf("Enter four space-seperated numbers: ");
    scanf("%f %f %f %f", &n1, &n2, &n3, &n4);
    float avg = (n1+n2+n3+n4)/4;
    printf("%f is the average.", avg);

    return 0;
}
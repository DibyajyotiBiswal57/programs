#include <stdio.h>
int main() {
    float a, b, c;
    printf("Enter three numbers: ");
    scanf("%f %f %f", &a, &b, &c);
    printf("Sum: %.2f\n", a + b + c);
    return 0;
}

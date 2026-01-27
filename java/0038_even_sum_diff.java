import java.util.Scanner;

class weird_operations3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        int result;

        if (num1 % 2 == 0 && num2 % 2 == 0) {
            result = num1 + num2;
            System.out.println("Both numbers are even. Their sum is: " + result);
        } else {
            result = num1 * num2;
            System.out.println("At least one number is odd. Their product is: " + result);
        }

        scanner.close();
    }
}

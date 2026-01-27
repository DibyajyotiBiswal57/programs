import java.util.Scanner;

public class smaller_number {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        int smallerNumber;

        if (num1 < num2) {
            System.out.println("The smaller number is: " + num1);
        } 
        else {
            System.out.println("The smaller number is: " + num2);
        }


        scanner.close();
    }
}
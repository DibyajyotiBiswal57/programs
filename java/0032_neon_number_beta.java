import java.util.Scanner;

public class neons_number {
    public static void main(String[] args) {

        System.out.println("This program checks if a number is neon number or not.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number: ");
        double num = scanner.nextDouble(); 
        if (num/9==0 || num%10==9)
        {
            System.out.println("It is a neon's number.");
        }
        else
        {
            System.out.println("It is not a neon's number.");
        }
        
        scanner.close();
    }
}

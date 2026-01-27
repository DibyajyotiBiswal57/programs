import java.util.Scanner;

public class add_3_numbers {
    public static void main(String[] args) {

        System.out.println("This program adds 3 numbers.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double a = scanner.nextDouble(); 

        System.out.print("Enter second number: ");
        double b = scanner.nextDouble(); 

        System.out.print("Enter third number: ");
        double c = scanner.nextDouble(); 

        double sum = a+b+c;


        System.out.println("The sum is " +sum);
        
        scanner.close();
    }
}

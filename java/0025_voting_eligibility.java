import java.util.Scanner;

public class voting_eligibility {

    public static void main(String[] args) {
        System.out.println("This program checks if a person is eligible to vote or not.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("You are eligible to vote.");
        } else {
            System.out.println("You are not eligible to vote.");
        }

        scanner.close();
    }
}

import java.util.Scanner;

public class child_or_adult {

    public static void main(String[] args) {
        System.out.println("This program checks if a person is a child or an adult.");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("You are an adult.");
        } else {
            System.out.println("You are a child.");
        }

        scanner.close();
    }
}

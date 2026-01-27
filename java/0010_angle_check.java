import java.util.Scanner;

public class is_it_complementary_or_supplementary
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("This program tells you if 2 angles are complementary or supplementary.");
        System.out.println("Enter the first angle:");
        int angle1 = scanner.nextInt();
        System.out.println("Enter the second angle:");
        int angle2 = scanner.nextInt();

                if (angle1 + angle2 == 90) {
            System.out.println("The angles are complementary.");
        } else if (angle1 + angle2 == 180) {
            System.out.println("The angles are supplementary.");
        } else {
            System.out.println("The angles are neither complementary nor supplementary.");
        }
        scanner.close();
    }
}
        

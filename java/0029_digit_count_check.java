import java.util.Scanner;
public class number_teller
{
    public static void main(String args[])
    {
        System.out.println("This program checks whether a number has a, two or more digits."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        double a = scanner.nextDouble();
        if(a/10==0)
        System.out.println("It is a single digit number.");
        else if (a/100==0)
        System.out.println("It is a double digit number.");
        else
        System.out.println("It has more digits.");
        scanner.close();
    }
}

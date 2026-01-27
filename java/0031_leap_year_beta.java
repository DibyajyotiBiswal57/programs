import java.util.Scanner;
public class leap_year
{
    public static void main(String args[])
    {
        System.out.println("This program checks whether a year is a leap year or not."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        double a = scanner.nextDouble();
        if(a/4==0)
        System.out.println("It is a leap year.");
        else
        System.out.println("It is not a leap year.");
        scanner.close();
    }
}

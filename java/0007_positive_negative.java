import java.util.Scanner;
public class positive_or_negative
{
    public static void main(String args[])
    {
        System.out.println("This program checks whether a number is positive or negative or 0."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        double a = scanner.nextDouble();
        if(a>0)
        System.out.println("It is a positive number.");
        else if (a==0)
        System.out.println("It is 0");
        else if (a<0)
        System.out.println("It is a negative number.");
        scanner.close();
    }
}

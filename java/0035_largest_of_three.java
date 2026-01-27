import java.util.Scanner;
public class largest_number
{
    public static void main(String args[])
    {
        System.out.println("This program prints the largest of 3 numbers."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the first number:");
        double a = scanner.nextDouble();
        System.out.println("Enter the second number:");
        double b = scanner.nextDouble();
        System.out.println("Enter the third number:");
        double c = scanner.nextDouble();
        if(a>b && a>c)
        System.out.println(a+" is the largest number.");
        else if(b>c && b>a)
        System.out.println(b+" is the largest number.");
        else if(c>b && c>a)
        System.out.println(c+" is the largest number.");
        scanner.close();
    }
}

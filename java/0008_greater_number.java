import java.util.Scanner;

public class greater_than_or_equal
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("This program takes 2 number and tells which number is greater");
        System.out.println("Enter the first number:");
        double a = scanner.nextInt();
        System.out.println("Enter the second number:");
        double b = scanner.nextInt();

        if(a==b)
        {

        System.out.print("The numbers are equal. ");
        }
        
        else if(a>b)
        {
        System.out.println(a+" is greater than " +b);
        }
        
        else if(b>a)
        {
        System.out.println(b+" is greater than " +a);
        }
        scanner.close();
    }
}
        

import java.util.Scanner;
public class even_or_odd
{
    public static void main(String args[])
    {
        System.out.println("This program checks whether a number is even or odd."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        double a = scanner.nextDouble();
        if(a%2==0)
        System.out.println("The number is even.");
        else 
        System.out.println("The number is odd.");
        scanner.close();
    }
}

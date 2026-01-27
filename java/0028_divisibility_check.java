import java.util.Scanner;
public class divisible_by_7_or_3
{
    public static void main(String args[])
    {
        System.out.println("This program checks whether a number is divisible by 7 or 3 or both."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        double a = scanner.nextDouble();
        if(a%7==0 & a%3!=0)
        System.out.println("It is only divisible by 7.");
        else if (a%3==0 & a%7!=0)
        System.out.println("It is only divisible by 3.");
        else if (a%3==0 & a%7==0)
        System.out.println("It is divisible by both 7 and 3.");
        scanner.close();
    }
}
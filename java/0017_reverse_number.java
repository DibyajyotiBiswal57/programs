import java.util.Scanner;
public class reversed_number
{
    public static void main(String args[])    
    {
        System.out.println("This program accepts a 3 digit number and reverses the digits.");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a 3-digit number:");
        int no = scanner.nextInt();
        if ((no>999)||(no<100))
        {
        System.out.println("It is not a 3 digit number.");
        }
        else 
        {
        int no1=no/100;
        int no3=no%10;
        int no1and2=no/10;
        int no2=no1and2%10;
        System.out.println("The reversed number is:" +no3+no2+no1);
        }
        scanner.close();
    }
}

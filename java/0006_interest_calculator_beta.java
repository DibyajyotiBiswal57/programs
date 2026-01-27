import java.util.Scanner;
public class simple_interest
{
    public static void main(String args[])
    {
        System.out.println("This program finds the simple interest on a given sum of money.");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the principle:"); 
        double p = scanner.nextDouble();
        System.out.println("Enter the time(in years):"); 
        double r = scanner.nextDouble();
        System.out.println("Enter the rate of interest:"); 
        double t = scanner.nextDouble();
        double si=p*r*t/100;
        System.out.println("The simple interest is Rs."+si); 
    }
}

import java.util.Scanner;
public class discount
{
    public static void main(String args[])
    {
        System.out.println("This program gives the discount on a certain price."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a price:");
        double a = scanner.nextDouble();
        double discount;
        double price;
        if(a<0)
        {
        System.out.println("Invalid Price");
    }
        else if(a>10000)
        {
        discount=a*10/100;
        price=a*90/100;
        System.out.println("The discount is"+discount);
        System.out.println("The price is"+price);
    }
    else if(a<10000)
    {
        discount=a*7.5/100;
        price=a*92.5/100;
        System.out.println("The discount is"+discount);
        System.out.println("The price is"+price);
    }
        scanner.close();
    }
}

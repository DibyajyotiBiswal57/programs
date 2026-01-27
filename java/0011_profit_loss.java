import java.util.Scanner;

public class profit_and_loss
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("This program finds the profit or loss for a given cost and selling price.");
        System.out.println("Enter the cost price:");
        double cp = scanner.nextInt();
        System.out.println("Enter the selling price:");
        double sp = scanner.nextInt();

        if(cp>sp)
        {

        System.out.println("It is a loss");
        double loss=cp-sp;
        System.out.println("The loss is "+loss);
        double lpercent=loss/cp*100;
        System.out.println("The loss percent is "+lpercent);
        }
        
        else if(cp<sp)
        {
        
        System.out.println("It is a profit");
        double profit=sp-cp;
        System.out.println("The profit is "+profit);
        double ppercent=profit/cp*100;
        System.out.println("The profit percent is "+ppercent);
        }
        
        else if(cp==sp)
        {
        
        System.out.println("There is neither a profit nor a loss.");
        double loss=cp-sp;
        double profit=sp-cp;
        System.out.println("The loss is "+loss);
        System.out.println("The profit is "+profit);
        double lpercent=loss/cp*100;
        double ppercent=profit/cp*100;
        System.out.println("The loss percent is "+lpercent);
        System.out.println("The profit percent is "+ppercent);
        }
        scanner.close();
    }
}
        

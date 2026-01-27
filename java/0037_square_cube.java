import java.util.Scanner;
public class cube_or_square
{
    public static void main(String args[])
    {
        System.out.println("This program lets you find the square or cube of a number."); 
        Scanner scanner = new Scanner(System.in);
        System.out.println("Do you want to find the cube or square?");
        System.out.println("For cube press'C'");
        System.out.println("For square press'S'");
        String a = scanner.nextLine();
        double sqr;
        double cube;
        if(a=="S")
        {
        System.out.println("Enter the number:");
        double input = scanner.nextDouble();
        sqr=input*input;
        System.out.println("The answer is: "+sqr);
    }
        else if(a=="C")
        {
        System.out.println("Enter the number:");
        double input = scanner.nextDouble();
        cube=input*input*input;
        System.out.println("The answer is: "+cube);
    }
        scanner.close();
    }
}

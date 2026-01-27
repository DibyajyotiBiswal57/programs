import java.util.Scanner;

public class swapping
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("This program swaps two numbers.");
        System.out.println("Enter a number");
        int a = scanner.nextInt();
        System.out.println("Enter another number");
        int b = scanner.nextInt();
        int c=a;
        a=b;
        b=c;
        System.out.println("The swapped numbers are "+a+" and "+b);
        scanner.close();
}
}

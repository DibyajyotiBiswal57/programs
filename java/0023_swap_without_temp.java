import java.util.Scanner;

public class swapping_without_3rd_var
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("This program swaps two numbers.");
        System.out.println("Enter a number");
        int a = scanner.nextInt();
        System.out.println("Enter another number");
        int b = scanner.nextInt();
      a=a+b;
      b=a-b;
      a=a-b;
        System.out.println("The swapped numbers are "+a+" and "+b);
        scanner.close();
}
}
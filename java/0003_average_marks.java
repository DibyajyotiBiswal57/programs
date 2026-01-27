import java.util.Scanner;

public class average_score {
    public static void main(String[] args) {

        System.out.println("This program finds the average of 4 marks.");
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter 4 marks");
        System.out.println("1: ");
        double a = scanner.nextDouble(); 

        System.out.println("2: ");
        double b = scanner.nextDouble(); 

        System.out.println("3: ");
        double c = scanner.nextDouble(); 
      
        System.out.println("4: ");
        double d = scanner.nextDouble(); 

        double aver = (a+b+c+d)/4; 


        System.out.println("The average is: " +aver);
    }
}

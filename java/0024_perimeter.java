import java.util.Scanner;

public class perimeter
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("This program finds out the perimeter of a square, rectangle, circle, parallelogram, rhombus or trapezium.");
        System.out.println("Choose the shape");
        System.out.println("For square, type '1'");
        System.out.println("For rectangle, type '2'");
        System.out.println("For circle, type '3'");
        System.out.println("For parallelogram, type '4'");
        System.out.println("For rhombus, type '5'");
        System.out.println("For trapezium, type '6'");
        System.out.println("For triangle, type '6'");
        System.out.println("Enter your choice:");
        int choice = scanner.nextInt();

        if(choice==1)
        {

        System.out.print("Enter the side of the square: ");
        double side = scanner.nextInt();
        System.out.println("Your side is " +side);
        
        double perimeter= 4*side;
        System.out.println("The perimeter of the square is " +perimeter);
        }
        
        else if(choice==2)
        {
        System.out.print("Enter the length of the rectangle: ");
        double len = scanner.nextInt();
        System.out.println("Your length is " +len);
        
        System.out.print("Enter the breadth of the rectangle: ");
        double bre = scanner.nextInt();
        System.out.println("Your breadth is " +bre);
        
        double perimeter= 2*(len+bre);
        System.out.println("The perimeter of the rectangle is " +perimeter);
        }
        
        else if(choice==3)
        {
        System.out.println("Enter the radius of the circle: ");
        double rad = scanner.nextInt();
        System.out.println("Your radius is " +rad);
        
        double perimeter= Math.PI*2*rad;
        System.out.println("The perimeter of the cirle is " +perimeter);
        }
        else if(choice==4)
        {
        System.out.print("Enter the length of the parallelogram: ");
        double bas = scanner.nextInt();
        System.out.println("Your length is " +bas);
        
        System.out.print("Enter the breadth of the parallelogram: ");
        double hei = scanner.nextInt();
        System.out.println("Your breadth is " +hei);
        
        double perimeter= 2*(bas+hei);
        System.out.println("The perimeter of the parallelogram is " +perimeter);
        }
        else if(choice==5)
        {
        System.out.print("Enter the side of the rhombus: ");
        double side = scanner.nextInt();
        System.out.println("The side is " +side);
        
        double perimeter= 4*side;
        System.out.println("The perimeter of the rhombus is " +perimeter);
        }
        else if(choice==6)
        {
        System.out.print("Enter the sides of the trapezium: ");
        double s1 = scanner.nextInt();
        double s2 = scanner.nextInt();
        double s3 = scanner.nextInt();
        double s4 = scanner.nextInt();
        System.out.println("The lengths are " +s1+", "+s2+", "+s3+" and "+s4);
        
        double perimeter= (s1+s2+s3+s4);
        System.out.println("The perimeter of the trapezium is " +perimeter);
        }
        else if(choice==7)
        {
        System.out.print("Enter the sides of the triangle: ");
        double s1 = scanner.nextInt();
        double s2 = scanner.nextInt();
        double s3 = scanner.nextInt();
        System.out.println("The lengths are " +s1+", "+s2+" and "+s3);
        
        double perimeter= s1+s2+s3;
        System.out.println("The perimeter of the triangle is " +perimeter);
        
        scanner.close();
    }
}
}

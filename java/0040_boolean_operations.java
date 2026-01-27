import java.util.Scanner;

public class rectangle_or_cylinder {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();

        System.out.print("Enter a boolean value (true/false): ");
        boolean isRectangle = scanner.nextBoolean();

        if (isRectangle) {

            double area = num1 * num2;
            double perimeter = 2 * (num1 + num2);

            System.out.println("Area of rectangle: " + area);
            System.out.println("Perimeter of rectangle: " + perimeter);
        } else {

            double height = num1;
            double radius = num2;

            double surfaceArea = 2 * Math.PI * radius * (radius + height);
            double volume = Math.PI * Math.pow(radius, 2) * height;

            System.out.println("Surface area of cylinder: " + surfaceArea);
            System.out.println("Volume of cylinder: " + volume);
        }

        scanner.close();
    }
}

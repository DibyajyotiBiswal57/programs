import java.util.Scanner;

class rectangle_or_cylinder {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the first number: ");
    double num1 = scanner.nextDouble();

    System.out.print("Enter the second number: ");
    double num2 = scanner.nextDouble();

    // Basic validation: dimensions should be finite and non-negative
    if (Double.isNaN(num1) || Double.isInfinite(num1)
        || Double.isNaN(num2) || Double.isInfinite(num2)
        || num1 < 0.0 || num2 < 0.0) {
      System.out.println("Invalid input: dimensions must be finite, non-negative numbers.");
      scanner.close();
      return;
    }

    System.out.print("Enter a boolean value (true/false): ");
    boolean isRectangle = scanner.nextBoolean();

    // Guard against overflow in rectangle area and perimeter calculations
    // Ensure that num1 * num2 and 2 * (num1 + num2) stay within the double range.
    double maxDimensionForArea = Math.sqrt(Double.MAX_VALUE);
    double maxDimensionForPerimeter = Double.MAX_VALUE / 4.0;
    double maxDimensionForRectangle = Math.min(maxDimensionForArea, maxDimensionForPerimeter);

    if (num1 > maxDimensionForRectangle || num2 > maxDimensionForRectangle) {
      System.out.println("Input too large: both numbers must be less than or equal to " + maxDimensionForRectangle);
      scanner.close();
      return;
    }

    if (isRectangle) {

      double area = num1 * num2;
      double perimeter = 2 * (num1 + num2);

      System.out.println("Area of rectangle: " + area);
      System.out.println("Perimeter of rectangle: " + perimeter);
    } else {

      double height = num1;
      double radius = num2;

      // Guard against overflow/underflow in surface area and volume calculations
      // Use a conservative upper bound for dimensions to keep results within double range.
      double maxDimensionForVolume = Math.cbrt(Double.MAX_VALUE / Math.PI);
      double maxDimensionForSurfaceArea = Math.sqrt(Double.MAX_VALUE / (4.0 * Math.PI));
      double maxDimension = Math.min(maxDimensionForVolume, maxDimensionForSurfaceArea);

      if (radius > maxDimension || height > maxDimension) {
        System.out.println("Input too large: radius and height must be less than or equal to " + maxDimension);
        scanner.close();
        return;
      }

      double surfaceArea = 2 * Math.PI * radius * (radius + height);
      double volume = Math.PI * Math.pow(radius, 2) * height;

      System.out.println("Surface area of cylinder: " + surfaceArea);
      System.out.println("Volume of cylinder: " + volume);
    }

    scanner.close();
  }
}

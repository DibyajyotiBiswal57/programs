import java.util.Scanner;

class add_3_numbers {

  private static double readBoundedDouble(Scanner scanner, String prompt) {
    final double MAX_ABS_VALUE = Double.MAX_VALUE / 4.0;
    while (true) {
      System.out.print(prompt);
      if (!scanner.hasNextDouble()) {
        System.out.println("Invalid input, please enter a numeric value.");
        scanner.next();
        continue;
      }
      double value = scanner.nextDouble();
      if (!Double.isFinite(value)) {
        System.out.println("Value must be a finite number. Please try again.");
        continue;
      }
      if (Math.abs(value) > MAX_ABS_VALUE) {
        System.out.println("Value is too large in magnitude. Please enter a smaller number.");
        continue;
      }
      return value;
    }
  }

  public static void main(String[] args) {

    System.out.println("This program adds 3 numbers.");

    Scanner scanner = new Scanner(System.in);

    double a = readBoundedDouble(scanner, "Enter first number: ");
    double b = readBoundedDouble(scanner, "Enter second number: ");
    double c = readBoundedDouble(scanner, "Enter third number: ");

    // Guard against overflow when adding the three numbers
    double partial = a + b;
    if (!Double.isFinite(partial)) {
      System.out.println("Intermediate sum is too large to be represented safely.");
      scanner.close();
      return;
    }
    double sum = partial + c;
    if (!Double.isFinite(sum)) {
      System.out.println("Final sum is too large to be represented safely.");
      scanner.close();
      return;
    }

    System.out.println("The sum is " + sum);

    scanner.close();
  }
}

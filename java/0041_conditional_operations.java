import java.util.Scanner;

class weird_operations4 {
  public static void main(String args[]) {
    System.out.println("Weird operations.");
    Scanner scanner = new Scanner(System.in);
    System.out.println("For checking whether the 2 numbers are equal, press 'a'");
    System.out.println("For checking whether the first number is equal, press 'M'");
    System.out.println("For multiplying the 2 numbers, press any other key");
    String a = scanner.nextLine();
    System.out.println("Enter the number:");
    double no1 = scanner.nextDouble();
    double no2 = scanner.nextDouble();
    if (a == "a") {
      if (no1 == no2) System.out.println("The numbers are equal");
      else System.out.println("The numbers are not equal");
    } else if (a == "M") {
      if (no1 % 9 == 0) System.out.println("The number is divisible by 9");
      else System.out.println("The number is not divisible by 9");
    } else {
      if (Double.isFinite(no1) && Double.isFinite(no2)) {
        double product = no1 * no2;
        if (Double.isFinite(product)) {
          System.out.println("The product is: " + product);
        } else {
          System.out.println("The product is too large in magnitude to be represented safely.");
        }
      } else {
        System.out.println(
            "One or both input numbers are not finite; cannot compute a reliable product.");
      }
    }
    scanner.close();
  }
}

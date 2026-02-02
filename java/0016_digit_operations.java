import java.util.Scanner;

class weird_operations {
  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter a 3-digit number:");
    int no = scanner.nextInt();
    if ((no > 999) || (no < 100)) {
      System.out.println("It is not a 3 digit number.");
    } else {
      int no1 = no / 100;
      int no3 = no % 10;
      int no1and2 = no / 10;
      int no2 = no1and2 % 10;
      int sum = no1 + no2;
      int prod = no1 * no3;
      System.out.println("The first digit is:" + no1);
      System.out.println("The second digit is:" + no2);
      System.out.println("The third digit is:" + no3);
      System.out.println("The sum of the first and third digits is: " + sum);
      System.out.println("The product of the first and third digits is: " + prod);
    }
    scanner.close();
  }
}

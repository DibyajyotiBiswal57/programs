# Java Language Guide

## Introduction
Java is a high-level, object-oriented programming language developed by Sun Microsystems (now owned by Oracle). It's designed to be platform-independent, meaning code written in Java can run on any device that has a Java Virtual Machine (JVM). Java is widely used for building web applications, mobile apps (Android), enterprise software, and more.

## Getting Started
To start programming in Java, you need:
- **Java Development Kit (JDK)**: Includes the JVM and development tools.
- **Integrated Development Environment (IDE)**: Such as Eclipse, IntelliJ IDEA, or Visual Studio Code with Java extensions.

### Installing JDK
Download the latest JDK from Oracle's website or use OpenJDK.

### Your First Java Program
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Save this as `HelloWorld.java` and compile with `javac HelloWorld.java`, then run with `java HelloWorld`.

## Basic Syntax
Java is case-sensitive. Every statement ends with a semicolon (`;`). Code is organized in classes.

### Variables
Variables store data. Declare them with a type:
```java
int age = 25;           // Integer
double price = 19.99;   // Decimal
char letter = 'A';      // Single character
boolean isTrue = true;  // True or false
String name = "Java";   // String of characters
```

### Data Types
- **Primitive**: int, double, char, boolean, byte, short, long, float
- **Reference**: Objects like String, arrays, etc.

## Control Structures
### If-Else
```java
if (age > 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}
```

### Loops
- **For Loop**:
  ```java
  for (int i = 0; i < 5; i++) {
      System.out.println(i);
  }
  ```

- **While Loop**:
  ```java
  int i = 0;
  while (i < 5) {
      System.out.println(i);
      i++;
  }
  ```

## Object-Oriented Programming
Java is OOP-focused. Everything is a class or object.

### Classes and Objects
```java
public class Car {
    String model;
    int year;

    public Car(String model, int year) {
        this.model = model;
        this.year = year;
    }

    public void display() {
        System.out.println("Model: " + model + ", Year: " + year);
    }
}

// Usage
Car myCar = new Car("Toyota", 2020);
myCar.display();
```

### Inheritance
```java
public class ElectricCar extends Car {
    int batteryLife;

    public ElectricCar(String model, int year, int batteryLife) {
        super(model, year);
        this.batteryLife = batteryLife;
    }
}
```

## Exception Handling
Handle errors gracefully:
```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
} finally {
    System.out.println("Execution complete");
}
```

## Collections
Java provides collections for storing groups of objects:
- **ArrayList**: Dynamic array
- **HashMap**: Key-value pairs

```java
import java.util.ArrayList;
import java.util.HashMap;

ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");

HashMap<String, Integer> map = new HashMap<>();
map.put("One", 1);
map.put("Two", 2);
```

## Best Practices
- Use meaningful variable and method names.
- Follow Java naming conventions (camelCase for variables, PascalCase for classes).
- Handle exceptions properly.
- Use comments to explain code.
- Keep methods short and focused.

## Next Steps

1. Browse Java solutions in `/java` folder
2. Try solving problems yourself before looking at solutions
3. Compare your solution with the repository's
4. Contribute missing solutions!

## Resources
- Official Java Documentation: [Oracle Docs](https://docs.oracle.com/javase/)
- Tutorials: [W3Schools Java](https://www.w3schools.com/java/)
- Online Java compiler: [Online Java Compiler](https://onecompiler.com/java)

---

[← Back to Language Guides](Language-Guides.md) | [C Guide →](Language-Guide-C.md)

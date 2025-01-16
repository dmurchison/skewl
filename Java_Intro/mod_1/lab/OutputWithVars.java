package mod_1.lab;
import java.util.Scanner;

public class OutputWithVars {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int userNum = 0;
      int userNum2 = 0;

      System.out.println("Enter integer: ");
      userNum = scnr.nextInt();


      System.out.print("You entered: ");
      System.out.println(userNum);

      // Add code to output userNum squared and cubed
      System.out.print(userNum + " squared is ");
      System.out.println(userNum * userNum);

      System.out.print("And " + userNum + " cubed is ");
      System.out.println(userNum * userNum * userNum + "!!");

      // Enter another integer
      System.out.println("Enter another integer: ");
      userNum2 = scnr.nextInt();

      System.out.print(userNum + " + " + userNum2 + " is ");
      System.out.println(userNum + userNum2);

      System.out.print(userNum + " * " + userNum2 + " is ");
      System.out.println(userNum * userNum2);

      return;
   }
}

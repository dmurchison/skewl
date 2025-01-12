package mod_1;

import java.util.Scanner;

public class Salary {

    public static void main (String [] args) {
        int wage;

        Scanner scnr = new Scanner(System.in);
        wage = scnr.nextInt();

        System.out.print("Salary is ");
        System.out.println(wage * 40 * 52);

        scnr.close();
    }
}

/*
 * This program calcs anything
 * Author: Duncan Murchison
 * Date: Jan 6, 2025
 */


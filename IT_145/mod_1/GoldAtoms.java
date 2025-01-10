package mod_1;

import java.util.Scanner;

public class GoldAtoms {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double avogadrosNumber = 6.02e23; // Approximation of atoms per mole
        double gramsPerMoleGold = 196.9665;
        double gramsGold;
        double atomsGold;

        System.out.print("Enter grams of gold: ");
        gramsGold = scnr.nextDouble();

        atomsGold = gramsGold / gramsPerMoleGold * avogadrosNumber;

        System.out.print(gramsGold + " grams of gold contains ");
        System.out.println(atomsGold + " atoms");
    }
}

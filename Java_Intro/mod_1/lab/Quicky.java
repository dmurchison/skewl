package mod_1.lab;
import java.util.Scanner;

public class Quicky {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double x;
        double y;
        double z;

        x = scnr.nextDouble();
        y = scnr.nextDouble();
        z = Math.abs(y) / x;

        // with only one decimal place
        System.out.printf("%.1f\n", z);
        return;
    }
}

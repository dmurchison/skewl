package mod_1.int_div_and_mod;

public class EachDigit {
    public static void main(String[] args) {
        int num = 12345;
        int digit1;
        int digit2;
        int digit3;
        int digit4;
        int digit5;

        digit1 = num / 10000;
        digit2 = (num % 10000) / 1000;
        digit3 = (num % 1000) / 100;
        digit4 = (num % 100) / 10;
        digit5 = num % 10;

        System.out.println(digit1);
        System.out.println(digit2);
        System.out.println(digit3);
        System.out.println(digit4);
        System.out.println(digit5);
    }
}

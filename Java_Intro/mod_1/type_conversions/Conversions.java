package mod_1.type_conversions;

public class Conversions {
    public static void main(String[] args) {
        int kidsInClass1;
        int kidsInClass2;
        int numClasses;

        kidsInClass1 = 7;
        kidsInClass2 = 8;
        numClasses = 2;

        System.out.println((kidsInClass1 + kidsInClass2) / (numClasses));

        System.out.println((double)(kidsInClass1 + kidsInClass2) / (double)(numClasses));
    }
}

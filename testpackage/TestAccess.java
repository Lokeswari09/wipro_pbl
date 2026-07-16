package testpackage;

public class TestAccess {

    public static void main(String[] args) {

        Foundation f = new Foundation();

        // System.out.println(f.var1); // Private - cannot access

        System.out.println("Default : " + f.var2);
        System.out.println("Protected : " + f.var3);
        System.out.println("Public : " + f.var4);
    }
}
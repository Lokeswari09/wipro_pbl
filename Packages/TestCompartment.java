package Packages;

public class TestCompartment {

    public static void main(String[] args) {

        Compartment c = new Compartment(10.5, 8.2, 6.3);

        System.out.println("Height : " + c.getHeight());
        System.out.println("Width : " + c.getWidth());
        System.out.println("Breadth : " + c.getBreadth());
    }
}
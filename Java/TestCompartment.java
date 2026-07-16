package Java;

import com.wipro.automobile.ship.Compartment;

public class TestCompartment {
    public static void main(String[] args) {
        Compartment shipCompartment = new Compartment(15.5, 20.0, 30.5);

        System.out.println("Ship Compartment Dimensions:");
        System.out.println("Height: " + shipCompartment.getHeight());
        System.out.println("Width: " + shipCompartment.getWidth());
        System.out.println("Breadth: " + shipCompartment.getBreadth());
    }
}
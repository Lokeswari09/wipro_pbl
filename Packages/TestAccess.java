package Packages;

import testpackage.Foundation;

public class TestAccess {
    public static void main(String[] args) {
        Foundation obj = new Foundation();

        System.out.println("var4 (public): " + obj.var4);
    }
}
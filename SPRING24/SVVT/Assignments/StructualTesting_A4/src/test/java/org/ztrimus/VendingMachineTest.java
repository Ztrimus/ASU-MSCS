package org.ztrimus;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class VendingMachineTest {
    // Exact amount testcases
    @Test
    public void testCandyExactAmount() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(20, "candy"));
    }

    @Test
    public void testCokeExactAmount() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(25, "coke"));
    }

    @Test
    public void testCoffeeExactAmount() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(45, "coffee"));
    }

    // More than enough
    @Test
    public void testCokeMoreThanEnough() {
        assertEquals("Item dispensed and change of 25 returned", VendingMachine.dispenseItem(50, "coke"));
    }

    @Test
    public void testCandyMoreThanEnough() {
        assertEquals("Item dispensed and change of 5 returned", VendingMachine.dispenseItem(25, "candy"));
    }

    @Test
    public void testCoffeeMoreThanEnough() {
        assertEquals("Item dispensed and change of 20 returned", VendingMachine.dispenseItem(65, "coffee"));
    }

    // Insuffcient funds
    @Test
    public void testCoffeeInsufficientFunds() {
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy or coke.", VendingMachine.dispenseItem(44, "coffee"));
    }

    @Test
    public void testCandyInsufficientFundsLowBoundary() {
        assertEquals("Item not dispensed, missing 5 cents. Cannot purchase item.", VendingMachine.dispenseItem(15, "candy"));
    }

    @Test
    public void testCokeInsufficientFundsJustBelowCost() {
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy.", VendingMachine.dispenseItem(24, "coke"));
    }

    // Boundary values for insufficient funds
    @Test
    public void testCandyInsufficientFundsBoundary() {
        assertEquals("Item not dispensed, missing 1 cents. Cannot purchase item.", VendingMachine.dispenseItem(19, "candy"));
    }

    @Test
    public void testCokeInsufficientFundsBoundary() {
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy.", VendingMachine.dispenseItem(24, "coke"));
    }

    @Test
    public void testCoffeeInsufficientFundsBoundary() {
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy or coke.", VendingMachine.dispenseItem(44, "coffee"));
    }

    @Test
    public void testNoPurchasePossible() {
        assertEquals("Item not dispensed, missing 20 cents. Cannot purchase item.", VendingMachine.dispenseItem(0, "candy"));
        assertEquals("Item not dispensed, missing 25 cents. Cannot purchase item.", VendingMachine.dispenseItem(0, "coke"));
        assertEquals("Item not dispensed, missing 45 cents. Cannot purchase item.", VendingMachine.dispenseItem(0, "coffee"));
    }
}

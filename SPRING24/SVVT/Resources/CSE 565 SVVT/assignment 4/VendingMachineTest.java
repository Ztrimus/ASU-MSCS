import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class VendingMachineTest {
    @Test
    public void candy1() {
        assertSame(VendingMachine.dispenseItem(20, "candy"), "Item dispensed.");
    }

    @Test
    public void coffee1() {
        assertSame(VendingMachine.dispenseItem(45, "coffee"), "Item dispensed.");
    }
    
    @Test
    public void coke1() {
        assertSame(VendingMachine.dispenseItem(25, "coke"), "Item dispensed.");
    }
    
    @Test
    public void coffee2() {
        assertEquals(VendingMachine.dispenseItem(40, "coffee"), "Item not dispensed, missing 5 cents. Can purchase candy or coke.");
    }

    @Test
    public void coke2() {
        assertEquals(VendingMachine.dispenseItem(24, "coke"), "Item not dispensed, missing 1 cents. Can purchase candy.");
    }
    
    @Test
    public void candy2() {
        assertEquals(VendingMachine.dispenseItem(30, "candy"), "Item dispensed and change of 10 returned");
    }

    @Test
    public void candy3() {
        assertEquals(VendingMachine.dispenseItem(15, "candy"), "Item not dispensed, missing 5 cents. Cannot purchase item.");
    }
    
    @Test
	public void notSameInstances() {
		final VendingMachine v1 = new VendingMachine();
		final VendingMachine v2 = new VendingMachine();
		assertNotEquals(v1, v2);
	}
    

}
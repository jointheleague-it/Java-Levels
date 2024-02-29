# 99 Extra 04 Tea Party


 <div id="moduleIndex">
  # Tea Party
  You are hosting a formal Tea Party. Your task is to welcome your guests properly. Here are the rules
for welcoming guests:



If the guest has been knighted by the Queen and is male, use the title "Sir" before their name to
greet them, otherwise if the guest is a male, use the title "Mr." before their name.


If the guest has been knighted by the Queen and is female, use the title "Lady" before their name to
greet them, otherwise if the guest is a female, use the title "Ms." before their name.

Add code to the class below to support the greeting rules above.
  ```

public class TeaParty {
    public String welcome(String name, boolean isWoman, boolean isKnighted) {
        
    }
}

```
  Here is some JUnit Test code to check your welcome method. Run the tests and check that the green
"pass" bar is displayed.
  ```

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TeaPartyTest {
	/**
	 * Jane Austen is a woman, so say “Hello Ms. Austen”. 
	 * George Orwell is a man, so say “Hello Mr. Orwell”. 
	 * Isaac Newton was knighted, so say "Hello Sir Isaac Newton".
	 **/

	@Test
	public void testIsWomanNotKnighted() {
		TeaParty teaParty = new TeaParty();
		assertEquals("Hello Ms. Austen", teaParty.welcome("Austen", true, false));
	}

	@Test
	public void testIsManNotKnighted() {
		TeaParty teaParty = new TeaParty();
		assertEquals("Hello Mr. Orwell", teaParty.welcome("Orwell", false, false));
	}

	@Test
	public void testIsManKnighted() {
		TeaParty teaParty = new TeaParty();
		assertEquals("Hello Sir Isaac Newton", teaParty.welcome("Isaac Newton", false, true));
	}
	
	@Test
	public void testIsWomanKnighted() {
		TeaParty teaParty = new TeaParty();
		assertEquals("Hello Lady Laura", teaParty.welcome("Laura", true, true));
	}

}
    
```
 </div>


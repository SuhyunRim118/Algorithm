import java.math.BigInteger;
import java.util.Scanner;
import java.math.*;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        BigInteger num1, num2;

        num1 = sc.nextBigInteger();
        num2 = sc.nextBigInteger();

        System.out.println(num1.add(num2));
    }
}

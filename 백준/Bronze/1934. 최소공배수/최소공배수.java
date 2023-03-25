import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int testcase = sc.nextInt();
		int greater=0;
		int smaller=0;

		for(int i=0;i<testcase;i++) {
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			int gcd = gcd(num1, num2);

			System.out.println(num1*num2 / gcd);
		}
    }

    public static int gcd(int a, int b) {
        int r = 0;

        while(b!=0) {
            r = a%b;

            a = b;
            b = r;
        }

        return a;
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int pay = sc.nextInt();
        int rest = 1000-pay;
        int count = 0;

        while(rest!=0) {
            if(rest>=500) {
                count++;
                rest -= 500;
            }
            else if(rest>=100) {
                count++;
                rest -= 100;
            }
            else if(rest>=50) {
                count++;
                rest -= 50;
            }
            else if(rest>=10) {
                count++;
                rest -= 10;
            }
            else if(rest>=5) {
                count++;
                rest -= 5;
            }
            else if(rest>=1) {
                count++;
                rest -= 1;
            }
        }

        System.out.println(count);
    }
}

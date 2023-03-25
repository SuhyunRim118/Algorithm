import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] num = new int[9];
        int number = sc.nextInt();
        int length = (int)(Math.log10(number) + 1);
        int max = 0;

        for(int i=0;i<length;i++) {
            if(number%10==9) num[6]++;
            else num[number%10]++;

            number /= 10;
        }

        if(num[6]%2==0) num[6] /= 2;
        else num[6] = num[6]/2+1;

        for(int i=0;i<9;i++) {
            if(num[i] > max) {
                max = num[i];
            }
        }
        System.out.print(max);
    }
}

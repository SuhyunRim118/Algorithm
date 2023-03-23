import java.util.Scanner;
import java.lang.Math;

public class Main { 
    public static void main(String[] args) {
        int[] nums = new int[10];
        int number;
        int mult = 1;
        int length = 0;

        Scanner sc = new Scanner(System.in);

        for(int i=0;i<3;i++) {
            number = sc.nextInt();
            mult = mult * number;
        }

        length = (int)(Math.log10(mult)+1);

        for(int i=0;i<length;i++) {
            nums[mult%10]++;
            mult /= 10;
        }
        
        for(int i=0;i<10;i++) {
            System.out.println(nums[i]);
        }
    }
}

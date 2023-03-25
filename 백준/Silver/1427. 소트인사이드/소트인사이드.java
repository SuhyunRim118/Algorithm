import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();
        int length = (int)(Math.log10(number)+1);
        int[] nums = new int[length];

        for(int i=0;i<length;i++) {
            nums[i] = number % 10;
            number /= 10;
        }

        Arrays.sort(nums);

        for(int i=length-1;i>-1;i--) {
            System.out.print(nums[i]);
        }
    }
}

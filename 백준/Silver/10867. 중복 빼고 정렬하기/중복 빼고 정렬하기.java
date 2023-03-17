import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int testcase = sc.nextInt();
        int[] nums = new int[testcase];
        int previous = 0;

        for(int i=0;i<testcase;i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);

        for(int i=0;i<testcase;i++) {
            if(i!=0) {
                if(previous!=nums[i]) {
                    System.out.print(nums[i] + " ");
                    previous = nums[i];
                }
            }
            else {
                System.out.print(nums[i] + " ");
                previous = nums[i];
            }
        }
    }
}

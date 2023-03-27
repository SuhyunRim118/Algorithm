import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        int[] arA = new int[testcase];
        int[] arB = new int[testcase];
        int sum = 0;

        for(int i=0;i<testcase*2;i++) {
            if(i>=testcase) {
                arB[i-testcase] = sc.nextInt();
            }
            else arA[i] = sc.nextInt();
        }
        Arrays.sort(arA);
        Arrays.sort(arB);

        for(int i=0;i<testcase;i++) {
            sum += (arA[i]*arB[testcase-i-1]);
        }
        System.out.println(sum);
    }
}
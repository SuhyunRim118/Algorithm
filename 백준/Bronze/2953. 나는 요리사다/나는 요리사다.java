import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] sum = {0, 0, 0, 0, 0};
        int score;
        int max=0;
        int maxIndex=0;

        for(int i=0;i<5;i++) {
            for(int j=0;j<4;j++) {
                score = sc.nextInt();
                sum[i] += score;
            }
        }

        for(int i=0;i<5;i++) {
            if(i==0) {
                max = sum[i];
                maxIndex = i+1;
            }
            else {
                if(sum[i]>max) {
                    max = sum[i];
                    maxIndex = i+1;
                }
            }
        }

        System.out.println(maxIndex + " " + max);
    }
}

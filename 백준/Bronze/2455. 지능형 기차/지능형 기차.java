import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] people = new int[4][2];
        int sum = 0;
        int max = 0;


        for(int i=0;i<4;i++) {
            people[i][0] = sc.nextInt();
            people[i][1] = sc.nextInt();

            sum = sum + people[i][1] - people[i][0];

            if(sum > max) max = sum;
        }

        System.out.println(max);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = 0;
        int totalscore = 0;
        String result;

        int testcase = sc.nextInt();

        for(int i=0;i<testcase;i++) {
            result = sc.next();

            for(int j=0;j<result.length();j++) {
                if(result.charAt(j)=='O') score++;
                else score = 0;

                totalscore += score;
            }
            System.out.println(totalscore);

            score = 0;
            totalscore = 0;
        }
    }
}

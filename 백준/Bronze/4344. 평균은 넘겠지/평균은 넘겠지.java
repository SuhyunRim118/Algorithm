import java.text.DecimalFormat;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        int testcase;
        int students;
        int sum = 0;
        double average;
        int overAverage = 0;
        double overAv;

        DecimalFormat form = new DecimalFormat("0.000");

        Scanner sc = new Scanner(System.in);
        testcase = sc.nextInt();

        for(int i=0;i<testcase;i++) {
            students = sc.nextInt();
            int[] test = new int[students];

            for(int j=0;j<students;j++) {
                test[j] = sc.nextInt();
                sum = sum + test[j];
            }

            average = sum*1.0/students;

            for(int j=0;j<students;j++) {
                if(test[j] > average) overAverage++;
            }

            overAv = overAverage * 1.0 / students;

            System.out.println(form.format(Math.round(overAv*100000)/1000.0) + "%");
            
            sum = 0;
            overAverage = 0;
        }
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int testcase = sc.nextInt();

        int[][] age = new int[testcase][2];
        String[] name = new String[testcase];

        for(int i=0;i<testcase;i++) {
            age[i][0] = sc.nextInt();
            age[i][1] = i;
            name[i] = sc.next();
        }

        Arrays.sort(age, Comparator.comparingInt(o1->o1[0]));

        for(int i=0;i<testcase;i++) {
            System.out.println(age[i][0] + " " + name[age[i][1]]);
        }
    }
}
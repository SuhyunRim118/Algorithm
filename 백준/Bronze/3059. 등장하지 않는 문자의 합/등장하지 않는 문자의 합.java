import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
        String[] str = new String[testcase];

        for(int i=0;i<testcase;i++) {
            int[] alp = new int[26];
            int total = 0;

            str[i] = sc.next();
            for(int j=0;j<str[i].length();j++) {
                alp[str[i].charAt(j)-'A']++;
            }

            for(int j=0;j<26;j++) {
                if(alp[j]==0) total += (int)(j+'A');
            }
            System.out.println(total);
        }
    }
}

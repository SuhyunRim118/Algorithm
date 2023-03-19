import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int testcase = sc.nextInt();

        for(int i=0;i<testcase;i++) {
            int numReverse = 0;
            int count=0;
            int sum = 0;

            int num = sc.nextInt();
            int keep = num;
            int length = (int)(Math.log10(num)+1);

            for(int j=0;j<length;j++) {
                numReverse += ((keep%10) * Math.pow(10, length-j-1));
                keep /= 10;
            }

            sum = num + numReverse;
            String str = Integer.toString(sum);

            for(int j=0;j<str.length()/2;j++) {
                if(str.charAt(j)==str.charAt(str.length()-j-1)) count++;
            }

            if(count==str.length()/2) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sec = 0;
        int totalsec = 0;

        String str = sc.next();

        for(int i=0;i<str.length();i++) {
            if(str.charAt(i)>='A' && str.charAt(i)<='C') sec = 3;
            else if(str.charAt(i)>='D' && str.charAt(i)<='F') sec = 4;
            else if(str.charAt(i)>='G' && str.charAt(i)<='I') sec = 5;
            else if(str.charAt(i)>='J' && str.charAt(i)<='L') sec = 6;
            else if(str.charAt(i)>='M' && str.charAt(i)<='O') sec = 7;
            else if(str.charAt(i)>='P' && str.charAt(i)<='S') sec = 8;
            else if(str.charAt(i)>='T' && str.charAt(i)<='V') sec = 9;
            else if(str.charAt(i)>='W' && str.charAt(i)<='Z') sec = 10;
            
            totalsec += sec;
        }
        System.out.println(totalsec);
    }
}
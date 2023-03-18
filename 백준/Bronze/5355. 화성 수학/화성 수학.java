import java.text.DecimalFormat;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase;
        String oper;
        float number = 0;
        int check = 0;

        DecimalFormat form = new DecimalFormat("0.00");

        testcase = sc.nextInt();

        while(true) {
            oper = sc.next();

            if(Character.isDigit(oper.charAt(0))==true) {
                if(check!=0) System.out.println(form.format(Math.round(number*100)/100.0));
                number = Float.parseFloat(oper);
                check++;
            }
            else {
                if(oper.equals("@")) number *= 3;
                else if(oper.equals("%")) number += 5;
                else if(oper.equals("#")) number -= 7;
            }

            if(sc.hasNext()==false) {
                System.out.println(form.format(Math.round(number*100)/100.0));
                break;
            }
        }
    }
}

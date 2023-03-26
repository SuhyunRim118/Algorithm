import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int callNum;
        int sec;
        int young = 0;
        int min = 0;

        callNum = sc.nextInt();

        for(int i=0;i<callNum;i++) {
            sec = sc.nextInt();
            
            young += (sec/30)*10 +10;
            min += (sec/60)*15 +15;
        }

        if(young==min) System.out.println("Y M " + young);
        else if(young<min) System.out.println("Y " + young);
        else if(young>min) System.out.println("M " + min);
    }
}

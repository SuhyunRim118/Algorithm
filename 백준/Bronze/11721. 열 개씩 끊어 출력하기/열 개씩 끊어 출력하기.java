import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String sentence;

        sentence = sc.next();

        for(int i=0;i<sentence.length();i++) {
            System.out.print(sentence.charAt(i));

            if((i+1)%10==0) System.out.print("\n");
        }
    }
}

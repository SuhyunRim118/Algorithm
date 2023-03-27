import java.util.Arrays;
import java.util.Scanner;

public class Main { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word;
        int[] alp = new int[26];
        int max = 0;
        int maxIndex = 0;
        int check = 0;
        
        word = sc.next();

        for(int i=0;i<word.length();i++) {
            if(Character.isUpperCase(word.charAt(i))) {
                alp[word.charAt(i) - 'A']++;
            }
            else alp[word.charAt(i) - 'a']++;
        }

        for(int i=0;i<26;i++) {
            if(max<alp[i]) {
                max = alp[i];
                maxIndex = i;
                check = 0;
            }
            else if(alp[i]>0 && max==alp[i]) {
                check = -1;
            }
        }

        if(check != -1) System.out.println((char)(maxIndex + 'A'));
        else if(check==-1) System.out.println("?");
    }
}

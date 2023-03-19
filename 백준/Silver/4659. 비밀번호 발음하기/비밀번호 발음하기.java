import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String password = sc.next();
        int consonant = 0;
        int vowel = 0;
        int checkVowel = 0;
        char previous = ' ';
        int check = 0;

        while(!password.equals("end")) {
            for(int i=0;i<password.length();i++) {
                if(password.charAt(i)=='a' || password.charAt(i)=='e' || password.charAt(i)=='i' || password.charAt(i)=='o' || password.charAt(i)=='u') {
                    checkVowel++;
                    vowel++;
                    consonant = 0;
                }
                else {
                    consonant++;
                    vowel = 0;
                }

                if(previous == password.charAt(i)) {
                    if(password.charAt(i)!='e' && password.charAt(i)!='o') {
                        check = -1;
                        break;
                    }
                }
                
                if(vowel==3 || consonant==3) {
                    check = -1;
                    break;
                }
                previous = password.charAt(i);
            }

            if(check==0 && checkVowel>0) System.out.println("<" + password + "> is acceptable.");
            else System.out.println("<" + password + "> is not acceptable.");

            consonant = 0;
            vowel = 0;
            check = 0;
            checkVowel = 0;
            previous = ' ';

            password = sc.next();
        }
    }
}
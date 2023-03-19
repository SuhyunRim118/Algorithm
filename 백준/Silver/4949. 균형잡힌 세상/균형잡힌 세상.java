import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		while(sc.hasNext()) {
			int check = 0;
			String str = sc.nextLine();
			if(str.equals(".")) break;

			List<Character> open = new ArrayList<>();
			
			for(int i=0;i<str.length();i++) {
	            if(open.size()==0 && (str.charAt(i)==')' || str.charAt(i)==']')) {
	            	check = -1;
	            	break;
	            }
	            
	            if(str.charAt(i)=='(') open.add(str.charAt(i));
	            else if(str.charAt(i)==')') {
	                if(open.get(open.size()-1)!='(') {
	                	check = -1;
	                	break;
	                }
	                else open.remove(open.size()-1);
	            }
	            
	            else if(str.charAt(i)=='[') open.add(str.charAt(i));
	            else if(str.charAt(i)==']') {
	                if(open.get(open.size()-1)!='[') {
	                	check = -1;
	                	break;
	                }
	                else open.remove(open.size()-1);
	            }
	        }
	        if(check==-1 || open.size()!=0) System.out.println("no");
	        else System.out.println("yes");
		}
    }
}
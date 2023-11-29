import java.io.*;
import java.util.*;

public class Main{
    public static int t;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(br.readLine());
        for(int i = 0; i < t; i++){
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()){
                StringBuilder sb = new StringBuilder(st.nextToken());
                System.out.print(sb.reverse()+" ");
            }
            System.out.println();
        }
    }
}
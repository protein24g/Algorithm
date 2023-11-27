import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[][] ary = new char[5][15];

        for (int i = 0; i < 5; i++){
            String str = br.readLine();
            for (int j = 0; j < str.length(); j++){
                ary[i][j] = str.charAt(j);
            }
        }
        for (int j = 0; j < ary[0].length; j++){
            for (int i = 0; i < 5; i++){
                if (ary[i][j] == 0) continue;
                bw.write(ary[i][j]);
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
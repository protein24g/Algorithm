import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        int s = 0;
        for (int i = 1; i <= n; i++){
            s += i;
        }
        System.out.println(s);
    }
}
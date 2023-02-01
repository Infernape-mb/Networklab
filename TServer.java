import java.io.*;  
import java.net.*; 
//import java.util.Scanner; 
public class TServer {  
public static void main(String[] args){  
try{  
ServerSocket ss=new ServerSocket(6666);  
Socket s=ss.accept();//establishes connection   
DataInputStream dis=new DataInputStream(s.getInputStream());  
String  str=(String)dis.readUTF(); 
File file = new File(
    "A:\\Notes\\netlab\\random.txt");
BufferedReader br
    = new BufferedReader(new FileReader(file));
String st;

while ((st = br.readLine()) != null)

    // Print the string
    System.out.println(st);
//System.out.println("message= "+str);  
ss.close();  
}catch(Exception e){System.out.println(e);}  
}  
}  
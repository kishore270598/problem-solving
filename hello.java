import java.io.PrintStream;

public class hello
{
    public static void main(String a[]) 
    { 
        
     Adding ad = new Adding();
     int x=ad.add(2,3);
    System.out.println(x);
    }


}

class Adding 
{
  public int add (int x,int y)
  {
     int sum =0;
     sum= x+y;
    return sum;
    
  }

}


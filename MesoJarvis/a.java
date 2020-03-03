public class MyThread implements Runnable {
void run() {
System.out.print("running... ");
}
public static void main(String [] args) {
MyThread mythread = new MyThread ();
Thread t = new Thread(mythread);
 t.start();
}
}
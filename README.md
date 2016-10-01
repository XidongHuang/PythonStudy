
# PythonStudy
The profile about studying Python.
And there are some study notes, they might be improved along with more and more studying.

Study Notes:

<h2>1. Placeholders:</h2><br>
  Python: %r, %s, %d. They can be used for number, string, boolean, 
  but usually use %s and %r just debugging (%r is raw programmer's vision variable)
  <br>
  Note: <br>
  Java String also can use %s as placeholder<br>
  
  ```Java
  String domain = "Hello";
  int num = 5;
  String str = String.format("%s, today is July %sth.", domain, num);
  System.out.println(str);
  ```
  
  SQL use "?"<br>
  
  ```Java
  String sql = "SELECT name, owner, species, picture FROM test1 WHERE name=?";
  ps = connection.prepareStatement(sql);
  ps.setString(1, "Tom");
  ``` 
 
<h2>2. Variable Argument List</h2><br>
Python: Use *args as variable argument, and it will be passed in a list into the method.<br>
  ```Python
  def print_two(*args):
	arg1, arg2 = args # the variables in args list will be assigned to arg1 and arg2 respectively.<br>
	print("arg1: %r, arg2: %r" % (arg1, arg2))

  ```

Java: After JDK 5.0, Java has its own variables argument list. It also can be a container for many variables, but the container is array, not list.<br>
```Java
  public int sum(int... nums){
	int sum = 0;
	for(int i : nums){
		sum += i;

	}
	return sum;
  }
```
notes: In Java, the variables argument list must be the only one the the last argument in method signature: <br> 
```Java
  public int sum(int num1, int num2, int... nums){
	...
  }
```
<h2>3. sys.argv </h2><br>
Python's sys.argv can stored system arguments. sys.argv[0] is the current python file script, so the arguments from outside should be read from sys.argv[1]. It also can pass files from outside. <i>Python3.5 ex17.py test.txt new.txt</i>, passing arguments into the python program.<br>

```Python
from sys import argv

script, from_file, to_file = argv # Assign system arguments to those three variables

```
Java: the interesting point is that the args[] array in Java main method also can receive arguments from outside.<br>
```Java
public class Example{
	public static void main(String[] args){
		for(String s : args){
			System.out.print(s);
		}

	}
}
/*---------------------------------------------*/
/*
Javax Example.java
Java Example 123 hello word

then the main method will print
123
hello
word
*/
```


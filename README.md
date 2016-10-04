
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
<h2>4. List, Dictionary (Map)</h2><br>
Data Structure is an very important part of OOP languages, and List, Map (Dictionary), Set are all very classical in it. So this part I would try to display what are different and what are same between Java and Python. 
<h4>List</h4><br>
<b style="color: #f00">Similarities:</b><br>
No matter in Java or Python, the length of List is changable, beginning index is 0, the orders of its values are beased on their adding order, also at the bottom is formed by array, and it can contain any kind of types, like Object, primitives, String. <i>(In Java, List can store any type if itself has no Generics restrict type)</i><br>
<b style="color: #f00">Differences:</b><br>
<i>Create</i>
```Python
# Python
a_list =  ['1', 1, '1', 'String', 5.40]
# [1, 1, 1, String, 5.40]
```
```Java
List list = new ArrayList();
// []

// create List with Generics Type
List<Integer> intList = ArrayList<Integer>();
// []
```
<i>Add</i>
```Python
a_list.append("adding one")
# [1, 1, 1, String, 5.40, adding one]
```
```Java
list.add("adding one Java");
//[adding one java]

// Generics one
intList.add(888);
// [888]
```
<i>Delete</i>
```Python
# Python has "del" method to remove element in list
rmovIndxNo = 3
del a_list[rmovIndxNo]
# [1, 1, 1, 5.40]
```
```Java
list.remove(0);
//[]

//Generics one
intList.remove(0);
//[]
```
<i>Change</i>
```Python
# Python list is mutable
a_list[0] = "new index 0"
# [new index 0, 1, 1, 1, 5.40]
```
```Java
list.add("old index 0");
//[old index 0]
list.set(0, "new index 0");
//[new index 0]

// same as Geneircs one
```
<i>Check</i>
```Python
print(a_list[2])
# 1
```
```Java
System.out.print(list.get(0));
//new index 0
```
Notes: CPython uses an array of pointers; Jython uses an ArrayList, IronPython uses an array too.<br>
But in Java, List is the sub-interface of Collection interface. It has ArrayList, LinkedList two main list implementing classes(Vector is too old to use). For ArrayList, it is still formed by array on the bottom, but Linked list is formed by double-linked list construction, which is very convenient and more efficient than ArrayList in field of adding, deleting continually. <i>Both are not synchronized(not Thread safe)</i><br>
<h4>Dictionary/Map</h4><br>
No matter in Dictionary or Map, they are all constructed as {Key: Values}.<br>
To be Continue...

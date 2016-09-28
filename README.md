
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
        

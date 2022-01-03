## [java对象传值知识点]

1.Java参数传递</br>
连接：https://www.programminghunter.com/article/4232485982/</br>
当基本数据类型（Boolean，byte，char，String，int，Long，float，double）作为参数传递时，传递的是实参值的副本，即传的是值，无论在函数中怎么操作这个副本，实参的值是不会被改变的。</br>
在Java中，当对象作为参数传递时，实际上传递的是一份“引用的拷贝”。 （实际传递的是对象的引用），即形参被改变时，原有实际参数也会改变</br>

2.java中打印：System.out.print()
boolean b = true;
System.out.println("输出boolean类型" + b);
println和print的差别，就是最后会换行
printf是格式化输出的形式。
%d：输出整型类型数据
%c：输出字符类型数据
%f：输出浮点类型数据，小数部分最多保留6位
%s：输出字符串数据

3.对象之间不能直接用“=”赋值
两对象之间使用“=”是将引用所指地址进行赋值，而不是内存块的内容。
通过“=”运算符，此时list2与list1指向同一块内存地址，list2原先分配的内存地址被回收

4.List、Set互转
list转set Set<String> set = new HashSet<>(list);
set转list List<String> list_1 = new ArrayList<>(set);

5.计算二维数组的和：2个for循环然后相加
  
6.递归：要有整体思想，不能跳进去去想
  
### [HashMap]()
1.HashMap遍历的四种方法
https://blog.csdn.net/scgyus/article/details/79105211

Map<Integer, Integer> map = new HashMap<Integer, Integer>();
for(Map.Entry<Integer, Integer> entry:map.entrySet()) {
  entry.getKey();
  entry.getValue();
}

### [HashSet]()
参考：http://fishleap.top/pages/e71d81/#_3-%E6%B3%A8%E6%84%8F
1.HashSet的三种输出方式
 toString  		System.out.print(h);//默认调用toString
 foreach    for(Object object : h)  System.out.print(object);
 Iterator   Iterator i = h.iterator();  while(i.hasNext()){ System.out.print(i.next()); }

2.向Collection接口的实现类的对象中添加obj数据时，要求obj所在类要重写equals():
判断Set集合是都包含指定的对象  contains(Object o);

在判断时会调用obj对象所在类的equals()方法：equals方法默认比较地址，需要重写来比较内容。String、File、Date、包装类默认重写了equals方法
equals(Object obj)：要想返回true，需要当前集合和形参集合的元素都相同(包括元素的顺序)
调用Arrays类的静态方法asList()：基本数据类型数组会被当做一个对象，需要使用包装类对象数组当形参
Collection coll = new ArrayList();
coll.add(123);
coll.add(new Person("Jerry",20));
coll.add(new String("Tom"));
coll.add(false);

// 在判断时会调用obj对象所在类的equals()方法：equals方法默认比较地址，需要重写来比较内容
// 1.contains(Object obj):判断当前集合中是否包含obj
boolean contains = coll.contains(123);
System.out.println(contains);	// true
// String、File、Date、包装类重写了equals方法
System.out.println(coll.contains(new String("Tom")));	// true
// Person没有重写equals方法时：false；重写了equals方法：true
System.out.println(coll.contains(new Person("Jerry",20)));




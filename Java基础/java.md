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

常用数据结构

### [基本数据类型]()

数组
int[] dp = new int[n];
初始化：Arrays.fill(dp, Integer.MAX_VALUE);  //pay attention do not forget initialize the array.
静态初始化数组：int[] array = new int[]{10, 20, 30, 40, 50};
动态初始化数组：int[] array = new int[50];  

int[][] nums = new int[m][n];
int a[][]={{1,2,3},{4,5,6}};
int m = nums.length;   行数
int n = nums[0].length;   列数
  
排序数组:Arrays.sort(str1);
数组对比:Arrays.equals(str1, str2);  
  
数组和集合的区别：数组可以重复，集合不能重复，用于去重
  
Char 
==  判断是否相等 
  
String方法
int length() 返回此字符串的长度
isEmpty() 判断字符串是否为空。 
contains(CharSequence chars) 判断是否包含指定的字符系列。
str1.equals(str2) 判断是否相等  
char charAt(int index) 返回指定索引处的 char 值。
int compareTo(Object o) 把这个字符串和另一个对象比较。  
int compareTo(String anotherString) 按字典顺序比较两个字符串。
String concat(String str) 将指定字符串连接到此字符串的结尾。

ArrayList
  
LinkedList
求长度：size()
boolean add(E e)：在链表后添加一个元素，如果成功，返回true，否则返回false；  
void addFirst(E e)：在链表头部插入一个元素；
E remove()；移除链表中第一个元素；
E get(int index)：按照下边获取元素；  
void push(E e)：与addFirst一样，实际上它就是addFirst；
E pop()：与removeFirst一样，实际上它就是removeFirst；
add()和offer()的区别：
offer方法-尝试将元素添加到队列中，如果无法添加元素（例如，队列已满），则返回false；如果添加了元素且不引发任何特定异常，则返回true。
add方法-尝试将元素添加到队列中，如果添加了元素，则返回true；如果当前没有可用空间，则抛出IllegalStateException。 
    
队列之间可以直接赋值吗？ 可以， queue1 = queue2;
  

subset subsequence    
  
### [集合使用方法]()
  
Queue 
Queue is a data structure. The basic idea of this structure is first in and first out.
定义：Queue<String> queue = new LinkedList<>();
获取队列长度 int size()
添加元素到队尾 boolean offer()  
取队首元素并删除	E poll()
取队首元素但不删除	E peek()
  
Stack
Stack is a data structure. The basic idea of this structure is last in and first out.
Stack<Character> stack = new Stack<Character>();  
判断栈是否为空: boolean empty()	 
把元素压栈:Object push(E)；
把栈顶的元素“弹出”: Object pop()；
取栈顶元素但不弹出: Object peek()。  
    
HashSet 
It is used to store a collection of elements that are not repeated. It mainly provides the following methods:
Set<String> set = new HashSet<>();
获取长度：set.size()
将元素添加进Set<E>：boolean add(E e)
将元素从Set<E>删除：boolean remove(Object e)
判断是否包含元素：boolean contains(Object e)
  
HashMap
HashMap getOrDefault(key, defaultValue)  used to get the value mapped with specified key. If no value is mapped with the provided key then the default value is returned. 
HashMap遍历：  
1.for(Map.Entry<> entry : map.entrySet())
2.Integer key:map.keySet()
3.迭代器 Iterator<Map.Entry<Integer, Integer>> entries = map.entrySet().iterator();
  
Heap
is a kind of data structure but not a class, so we always use PriorityQueue as a class to use
  


  
  
  
  
  



---
title: Java 7-2 List的使用
tags: []
id: '1659'
categories:
  - - 厦门工学院Java答案
date: 2021-05-09 23:15:47
---

## 2、List的使用

本题练习列表的使用。 定义 Person 类 定义私有属性 String name,int age, 使用 Eclipse 生成每个属性 setter 、getter，有参 Person(String name,int age) 、无参 构造方法，toString 方法。 定义 Main 类，在 main 方法中 定义 List list = new ArrayList(); 用键盘给变量 n 赋值 生成 n 个 Person 对象并添加到列表中，该 Person 的 name 和 age 通过键盘给出 循环列表，输出列表所有 Person 对象信息（调用 toString 方法） 输入一个字符串表示姓名，判断该字符串表示的 Person 对象在List中是否存在，如果存在，输出该Person，否则输出此人不存在。 输入格式: 先一行输入n表示对象个数，然后每行输入一个Person对象的name和age 一行输入一个人的姓名对其进行查询 输出格式: 对每一对象，在一行中输出对象的信息。 对查询的人员，查到输出该人的信息，否则输出此人不存在。 输入样例: 在这里给出一组输入。例如：

```java
3
zhang 23
li 44
wang 33
li3
zhang 23
li 44
wang 33
```

may 输出样例: 在这里给出相应的输出。例如：

```java
Person [name=zhang, age=23]
Person [name=li, age=44]
Person [name=wang, age=33]
Person [name=li, age=44]Person [name=zhang, age=23]
Person [name=li, age=44]
Person [name=wang, age=33]
此人不存在
```

## 答案

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        ArrayList<Person>list=new ArrayList<>();

        Scanner in=new Scanner(System.in);
        int n=in.nextInt();

        for(int i=0;i<n;i++) {
            Person p=new Person(in.next(),in.nextInt());
            list.add(p);
            System.out.println(p.toString());
        }
        String l=in.next();
        int i;
        for(i=0;i<list.size();i++) {
            if(list.get(i).getName().equals(l)) {
                System.out.println(list.get(i).toString());
                break;
            }

        }
        if(i==list.size()) {
            System.out.println("此人不存在");
        }
    }

}
class Person{
    private String name;
    private int age;

    public Person(String name,int age) {
        this.age=age;
        this.name=name;
    }
    public Person() {
        this.age=age;
        this.name=name;
    }



    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + "]";
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }

}
```
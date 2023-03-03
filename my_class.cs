using System;

class Cat {
  private string name; // Кличка
  private int age; // Возраст
  private float weight; // Вес
  private bool poroda; //  false - без породы, true - породистый

  public Cat(string n, int a, float w, bool p) {
    this.name = n;
    this.age = a;
    this. weight = w;
    this.poroda = p;
  } // Конец конструктора класса

  public void Meow() {
    Console.Write(this.name);
    Console.WriteLine(" сказал Мяу");
  } // Конец метода Мяу
  
} // Конец реализации класса


class Program {
  public static void Main (string[] args) {
    Cat c1 = new Cat("Барсик", 14, 2.5f, false);
    Cat c2 = new Cat("Мурзик", 10, 5.5f, true);

    c1.Meow();
    c2.Meow();
    
  }
}

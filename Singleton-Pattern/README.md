There can be only one!- -- Connor MacLeod

# Singleton Object

This folder contains an implementation of the Singleton design pattern in Python. The Singleton pattern restricts the instantiation of a class to a single instance and provides a global point of access to that instance.

## What is Singleton?

The Singleton pattern is a creational design pattern that ensures a class has only one instance while providing a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system.

In this implementation, we have defined a `SingletonObject` class, which serves as an example of a Singleton pattern.

## Implementation Details

### Private Class

Inside the `SingletonObject` class, we have a private class named `__SingletonObject`. The leading double underscores indicate that this is a private class, and it should not be accessed or used outside the original class definition. This private class contains the functionality of the Singleton object.

The private class has an object attribute called `val` and two methods:
- `__init__`: This method initializes the object.
- `__str__`: This method is called when you use the object in a print statement.

### Class Attribute

There is a class attribute called `instance`, which is common to all objects instantiated from the `SingletonObject` class. Initially, it is set to `None`, indicating that no instance exists when the script starts executing.

### The `__new__` Method

In the `__new__` method, we see a different parameter pattern: it takes `cls` as a parameter instead of the usual `self`. This is because `__new__` is a class method. It receives the class itself as a parameter and then uses this class definition to construct a new instance of the class.

Within `__new__`, the code checks whether an instance of the private class exists. If no instance exists (i.e., `SingletonObject.instance` is `None`), it creates a new instance of the private class and assigns it to the `instance` class variable. Finally, the `__new__` method returns the class instance.

### `__getattr__` and `__setattr__` Methods

The `__getattr__` and `__setattr__` methods are modified to relay attribute access to the private class stored in the `instance` class variable. This allows attribute access to behave as if the outer object has these attributes.

### Demonstration of Singleton Behavior

The `self.val` attribute is set to demonstrate that the object remains the same even if the script attempts to instantiate it multiple times. This behavior showcases the Singleton pattern in action.

## How to Use

To use this Singleton pattern implementation, you can create instances of the `SingletonObject` class. However, no matter how many times you create an instance, you'll always get the same instance.

```python
singleton_instance1 = SingletonObject()
singleton_instance2 = SingletonObject()

# Both instances are the same
print(singleton_instance1 is singleton_instance2)  # This will print True
```

## Conclusion

The Singleton pattern is a useful design pattern for scenarios where you need to ensure that a class has only one instance. It provides a straightforward way to manage shared resources and global settings across an application. This implementation serves as a clear example of how to create a Singleton in Python.

Feel free to explore and use this implementation in your projects where Singleton behavior is required.

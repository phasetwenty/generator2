# Glossary

There is terminology I've applied to this project to help clarify some concepts.

## Object

This is the root concept of the system, encapsulating any _thing_ we want to randomly generate. From a modeling standpoint, an **object** is a collection of **properties**, of which there can be 1 or more. An object has a fixed set of _properties_ at runtime. Each object has exactly 1 **property** with the **label** "name".

## Property

A property can be thought of as a descriptive facet of an object; the more properties an object has, the more varied an object can be in its world. A property is represented as a pair, consisting of a **label** and an **instance**.

## Label

A label is just what it sounds like: a label for a property. It explains what part of the object the instance refers to. An object's labels are fixed at runtime, and may have similar representations across objects. In the future there may be more to establish relationships between labels, but for now they are tied purely to their parent object.

## Instance

An instance is one of the set of values that a property can exhibit. Put another way, an instance is typically the randomized element(s) of an object.

# Example

Suppose we want to model a nonplayer character called a Peasant. In our example, we'll say that a Peasant can have a name, profession and age. Its name can be either Alice or Bob; its profession can be bartender, blacksmith or farmer; its age can be 20, 30 or 40.

First, we would create an **object** named "Peasant" (note that this name is not its name property; that will be clarified in a future version). Its **properties** are "name", "profession" and age. One property will have the **label** "name"  with **instances** "Alice" and "Bob"; one property will have the label "profession" with instances "bartender", "blacksmith" and "farmer", etc.

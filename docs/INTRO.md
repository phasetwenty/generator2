# Glossary

There is terminology I've applied to this project to help clarify some concepts.

## Object

This is the root concept of the system, encapsulating any _thing_ we want to randomly generate. From a modeling standpoint, an object is a collection of _properties_, of which there can be 0 or more. An object has a fixed set of _properties_ at runtime.

## Property

A property can be thought of as a descriptive facet of an _object_; the more properties an _object_ has, the more varied an _object_ can be in its world. A property is represented as a pair, consisting of a _descriptor_ and an _instance_.

## Descriptor

A descriptor is like a label for a _property_; it explains what part of the _object_ the _instance_ refers to. An _object's_ descriptors are fixed at runtime, and may have similar representations across _objects_. In the future there may be more to establish relationships between descriptors, but for now they are tied purely to their parent _object_.

## Instance

An instance is one of the set of values that a _property_ can exhibit. Put another way, an instance is typically the randomized element(s) of an _object_. A _property_ must have 2 or more instances. If it had 1, we would not consider it randomizable.
 
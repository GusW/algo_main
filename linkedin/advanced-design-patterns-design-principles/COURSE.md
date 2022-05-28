# Advanced Design Patterns: Design Principles

## Design Principles

![Mental Map](./images/mental_map.png)

- Guidelines, not rules, or laws
- Observed to result in good object-oriented designs
- Help us to avoid bad object-oriented design

### Symptons of Bad Design

- Rigidity
- Fragility
- Immobility

![Fundamental Principles](./images/fundamental_principles.png)

### Encapsulate What Varies

- Identify the aspects of your application that vary and separate them from what stays the same
- Look for code that changes with every new requirement
- Alter or extend the code that varies without affecting code that doesn't
- Basis of almost every design pattern

![Encapsulate What Varies](./images/encapsulate_what_varies_1.png)
![Encapsulate What Varies](./images/encapsulate_what_varies_2.png)
![Encapsulate What Varies](./images/encapsulate_what_varies_3.png)

### Favor composition over inheritance

- `HAS-A` is better than `IS-A`
- Instead of inheriting behavior, we can compose our objects with new behaviors
- Composition often gives us more flexibility, even allows behavior changes at runtime

![Favor composition over inheritance](./images/has_a_better_than_is_a_1.png)
![Favor composition over inheritance](./images/has_a_better_than_is_a_2.png)
![Favor composition over inheritance](./images/has_a_better_than_is_a_3.png)

### Loose coupling

- Components should be independent, relying on knowledge of other components as little as possible
- Reduces the dependency between components

![Loose Coupling](./images/loose_coupling_1.png)
![Loose Coupling](./images/loose_coupling_2.png)
![Loose Coupling](./images/loose_coupling_3.png)

### Program to Interfaces

- Program to interfaces, not implementations
- where possible, components should use abstract classes or interfaces instead of a specific implementation
- Program to a `super type`
- We always have to instantiate a concrete type however
- Allows you to better exploit polymorphism
- Frees classes from knowledge of concrete types
- Improves extensibility and maintainability

![Program to Interfaces](./images/program_to_interfaces_1.png)
![Program to Interfaces](./images/program_to_interfaces_2.png)

### Single Responsibility Principle

- Look at change in your class: are parts of it changing while other parts aren't?
- Change only matters if it really happens (if the class isn't changing then, why bother?)

![Single Responsibility](./images/single_responsibility_1.png)
![Single Responsibility](./images/single_responsibility_2.png)

### Open-closed principle

- Our object-oriented designs should be open for extension, but closed for modification
- Allow new behavior without rising changes to proven code
- Improve maintainability and extensibility of a design

![Open Closed](./images/open_closed_1.png)
![Open Closed](./images/open_closed_2.png)
![Open Closed](./images/open_closed_3.png)

### Liskov's subistitution principle

- You should always be able to substitute subtypes for their base class
- Classic Rectangle/Square area problem

![Liskov Substitution](./images/liskov_1.png)
![Liskov Substitution](./images/liskov_2.png)
![Liskov Substitution](./images/liskov_3.png)

### Interface segregation principle

- Cohesion
  - How strong are the relationships between an interface's methods
- Highly cohesive interfaces lead to more maintainable and more flexible systems
- Segregate inerfaces as necessary to keep them focused and cohesive

![Interface Segregation](./images/interface_segregation_1.png)
![Interface Segregation](./images/interface_segregation_2.png)
![Interface Segregation](./images/interface_segregation_3.png)
![Interface Segregation](./images/interface_segregation_4.png)
![Interface Segregation](./images/interface_segregation_5.png)
![Interface Segregation](./images/interface_segregation_6.png)
![Interface Segregation](./images/interface_segregation_7.png)
![Interface Segregation](./images/interface_segregation_8.png)
![Interface Segregation](./images/interface_segregation_9.png)

### Dependency inversion principle

- High-level modules should not depend on low-level modules
- Helps design software that is reusable and resilient to change
- All relationships should invilve abstract classes of interfaces
- Abstractions allow details to remain isolated from each other

![Dependency Inversion](./images/dependency_inversion_1.png)
![Dependency Inversion](./images/dependency_inversion_2.png)
![Dependency Inversion](./images/dependency_inversion_3.png)
![Dependency Inversion](./images/dependency_inversion_4.png)

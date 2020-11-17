## Summary
You will be demoing an object oriented design of a zoo.

## Instructions
_Note 11/16/20: We are doubling this as a debugging exercise. On solution.py, there are the errors in the class methods that will need to be resolved. Either reproduce these errors while demoing, or clear the comments and open solutions.py to start debugging._

You will be demoing an object oriented design of a zoo. Be sure to talk about why certain attributes or methods go on the class and why others go on the instance. Also, highlight the hierarchy between the `Zoo` class and `Animal` classes.


- Create a `Zoo` class.
  - Attributes: `catalog` (of all animals in the zoo)
  - Methods: `add_animal`
- Create an `Animal` class.
  - Attributes: `name`, `species`
  - Methods: `make_noise`
- Create species classes (`Cow`, `Pig`) that extend the `Animal` class.
  - Each species should provide data for upper attributes, but then have additional attributes and methods that pertain specifically to that species. This will help demonstrate the hierarchy of the class system. For example, you can also create a `Cat` class with methods for `groom`ing or `prr`ing.

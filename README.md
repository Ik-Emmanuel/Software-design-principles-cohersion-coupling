# Software design principles :Cohersion & Coupling
Understanding better software design principles with Python. Cohesion and coupling refers to how easily software code can be changed, extended or scaled up  

## Cohesion
cohesion - a degree to which the elements of a class or function belong together. Strong or High cohesion refers to functions that contain elements that belong together and just do specified things. clear responsibility and not doing too much and having unrelated things (having just one task only) makes it easily reusable and changed. Low cohesion code contains to many things going on within a given function.

## Coupling 
Measuring how dependent two parts of a code are on each other.  Having high coupling can be problematic because code modifications are harder to track and  it leads to changing things in different places which becomes difficult upon code scale. Low code coupling the most ideal and this can be archived by: passing only the data that function needs, rather than calling another method within 


# Steps 
- check to see where data or information resides,  and how it is accessed 
- group  code around that so that codes are closer to the information that it uses.
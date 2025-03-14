# Software-Projekt  

## Router  

The `app.py` file serves as the main entry point for handling requests in the Flask application. It defines the available endpoints, processes incoming data, and returns a response.  

Each route requires the following JSON input:  
- The **student graph** (the submitted solution, **mandatory**).  
- Either the **graph** (initial state) or the **input values** (elements to be added or removed)—or **both**.  

Inside the route's function, the task is programmatically solved using the **GraphTreeNode** or **RedBlackTreeNode** classes. The student's submission is then **evaluated** against the expected solution, and feedback with an appropriate score is returned.  

## Classes  

These classes provide the foundation for handling graphs and evaluating student solutions.  

### **GraphTreeNode**  
A basic binary tree node with:  
- A **value** (cannot be `None`).  
- **Left and right children** (must be `GraphTreeNode` or `None`).  
- **Getter and setter methods** for all attributes.  

### **RedBlackTreeNode**  
An extension of `GraphTreeNode` for Red-Black Trees, featuring:  
- An additional **color** attribute (`"red"` or `"black"`).  
- Validation to ensure only **valid colors** are set.  
- **Getter and setter methods** for all attributes.  

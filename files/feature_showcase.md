# Markdown+ Feature Showcase

Welcome to the Markdown+ feature showcase! This document demonstrates all the features of the application.

## Themes

You can choose from 6 different dark themes using the theme selector in the sidebar. Your preference is saved automatically.

## Table of Contents

The table of contents on the left is automatically generated from the headers in your document. Click "Prikaži sadržaj" to toggle its visibility.

## Images

Images from the local `files/images` directory are properly displayed:

![Test Image](/files/images/test.png)

## Code Blocks with Syntax Highlighting

Code blocks are automatically colorized with language-specific highlighting:

```python
def hello_world():
    print("Hello, World!")
    for i in range(10):
        print(f"Number: {i}")

class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"
```

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}

const person = {
    name: "John",
    age: 30,
    greet() {
        return `Hi, I'm ${this.name} and I'm ${this.age} years old.`;
    }
};

// Arrow function
const add = (a, b) => a + b;
```

Each code block has a "Copy" button in the top-right corner for easy copying.

## YouTube Integration

Simply paste a YouTube link and it will be automatically converted to an embedded player:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Custom Font

The application uses a custom font for improved readability.

## Responsive Design

All content is properly sized to fit within the viewing area without horizontal scrolling.
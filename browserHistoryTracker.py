import webbrowser


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        print(f"Pushing {item}...\n")
        self.stack.append(item)

    def pop(self):
        print("Popping item from stack...")
        if len(self.stack) == 0:
            raise IndexError("Stack underflow. Cannot pop from an empty stack.")
        popped = self.stack[-1]
        self.stack.pop()
        print(f"Popped {popped} from stack\n")
        return popped

    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty.")
        top_lmnt = self.stack[-1]
        return f"Top element: {top_lmnt}"

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# Browser History Tracker


class BrowserHistory:
    def __init__(self):
        self.history = Stack()
        self.forward_stack = Stack()

    def visit_page(self, url):
        self.history.push(url)
        print("The URL has been pushed onto the stack")
        webbrowser.open(url)
        self.forward_stack = Stack()

    def goback(self):
        if self.history.size() > 1:
            popped_elmnt = self.history.pop()
            self.forward_stack.push(popped_elmnt)
            new_url = self.history.peek()
            webbrowser.open(new_url)
        elif self.history.is_empty():
            print("Your history is empty.")

    def show_history(self):
        if self.history.is_empty():
            print("No browsing history available")
            return
        tab = 0
        while tab < len(self.history.stack):
            print(self.history.stack[tab])
            tab += 1

    def clear_history(self):
        if self.history.is_empty():
            print("No browsing history available")
            return
        self.history.stack = []
        print("Browsing history successfully cleared")

    def go_forward(self):
        if self.forward_stack.is_empty():
            print("No pages to open")
            return
        popped_elmnt = self.forward_stack.pop()
        self.history.push(popped_elmnt)
        webbrowser.open(popped_elmnt)


bh = BrowserHistory()

while True:
    user_input = input("Enter one of the commands listed below:\n\nvisit\nback\nforward\nhistory\nclear\n\n").lower()
    parts = user_input.split()
    if user_input == "exit":
        break

    if parts[0] == "visit":
        if len(parts) > 1:
            bh.visit_page(parts[1])
        else:
            print("Please enter a URL to visit")
    elif parts[0] == "back":
        bh.goback()
    elif parts[0] == "forward":
        bh.go_forward()
    elif parts[0] == "history":
        bh.show_history()
    elif parts[0] == "clear":
        bh.clear_history()
    else:
        print("Unknown or Invalid command.")

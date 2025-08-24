from collections import deque
import datetime

class ChatMessage:
    """Represents a single message with content and a timestamp."""
    def __init__(self, content, timestamp=None):
        self.content = content
        # Use current time if not provided, for both sending and undo/redo
        self.timestamp = timestamp or datetime.datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%H:%M:%S')}] {self.content}"

class ChatHistoryManager:
    """Manages chat messages using a queue for history and a stack for undo."""

    def __init__(self):
        # Queue for storing message history (FIFO)
        self.message_queue = deque()
        # Stack for undo actions (LIFO)
        self.undo_stack = []

    def send_message(self, content):
        """Adds a new message to the history and the undo stack."""
        new_message = ChatMessage(content)
        self.message_queue.append(new_message)
        self.undo_stack.append(new_message)
        print(f"Message sent: '{new_message.content}'")

    def undo_last_message(self):
        """Removes the last sent message from the history."""
        if not self.undo_stack:
            print("No recent messages to undo.")
            return

        # Pop the last action from the stack
        last_sent_message = self.undo_stack.pop()
        
        # Remove the message from the queue.
        # This is not a simple O(1) operation for a deque, so we need to rebuild it or search.
        # A more efficient design for a large number of messages might use a doubly linked list.
        # For simplicity, we'll demonstrate a search and remove approach.
        
        found = False
        temp_queue = deque()
        while self.message_queue:
            message = self.message_queue.popleft()
            if message.timestamp == last_sent_message.timestamp and message.content == last_sent_message.content:
                print(f"Undoing message: '{message.content}'")
                found = True
            else:
                temp_queue.append(message)
        
        self.message_queue = temp_queue
        
        if not found:
            print("Error: Message to undo was not found in the history.")


    def view_history(self):
        """Displays the entire message history in chronological order."""
        if not self.message_queue:
            print

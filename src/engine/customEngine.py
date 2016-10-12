# playing around with cocos and pyglet
import cocos
import pyglet
class KeyDisplay(cocos.layer.Layer):

    # If you want that your layer receives director.window events
    # you must set this variable to 'True'
    is_event_handler = True

    def __init__(self):

        super( KeyDisplay, self ).__init__()

        self.text = cocos.text.Label("", x=100, y=280 )

        # To keep track of which keys are pressed:
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = 'Keys: '+','.join (key_names)
        # Update self.text
        self.text.element.text = text
    def on_key_press (self, key, modifiers):
        self.keys_pressed.add (key)
        self.update_text()
    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove (key)
        self.update_text()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = 'Keys: '+','.join (key_names)
        # Update self.text
        self.text.element.text = text

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(KeyDisplay()))
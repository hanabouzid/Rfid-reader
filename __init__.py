from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

class RfidReader(MycroftSkill):
    def __init__(self):
        super(RfidReader, self).__init__(name="RfidReader")

    @intent_handler(IntentBuilder("").require("login"))
    def handle_login(self):
        try:
            id, t = reader.read()
            self.speak_dialog("login", data={"name": t, "id": id})
        finally:
            GPIO.cleanup()


def create_skill():
    return RfidReader()

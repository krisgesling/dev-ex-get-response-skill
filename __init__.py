from mycroft import MycroftSkill, intent_file_handler


class DevExGetResponse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('response.get.ex.dev.intent')
    def handle_response_get_ex_dev(self, message):
        self.speak_dialog('response.get.ex.dev')


def create_skill():
    return DevExGetResponse()


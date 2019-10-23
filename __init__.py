from mycroft import MycroftSkill, intent_file_handler


class DevExGetResponse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ask.me.a.question.intent')
    def handle_ask_question(self, message):

        user_response = self.get_response(dialog='what.to.ask',
                                          validator=validator,
                                          on_fail=on_fail)
        self.log.info('user_response: {}'.format(user_response))
        self.speak_dialog('success')

        def validator(utterance):
            """ A validator function returns True or False to indicate if the
                response recieved is valid.

                Parameters:
                    utterance (str): the response received from the user

                Returns:
                    bool:
                        - If True, get_response will return the utterance.
                        - If False, the on_fail argument will be called, and
                          get_response will return None.

            This function is contained within this intent handler. It is an
            example of an inner or nested function meaning it is scoped to
            the handle_ask_question function and cannot be used elsewhere.
            """

            self.log.info("Utterance: {}".format(utterance))

            # Check if the utterance contains any vocab from valid.response.voc
            is_valid = self.voc_match(utterance, valid.response)

            return is_valid

        def on_fail(utterance):
            """ A function that is called in the event that the validator
                returns False. It can be used

                Parameters:
                    utterance (str): the response received from the user

                Returns:
                    str: dialog filename or string to speak
            """

            self.log.info("Utterance: {}".format(utterance))

            user_response = self.ask_yesno('try.again')

            return 'try.again' if user_response is None else 'okay'

    def common_validator(self, utterance):
        """ This is a validator function that may be used by multiple intents.
        """
        self.log.info("Utterance: {}".format(utterance))
        # Check if the utterance contains the string 'something'
        is_valid = 'something' in utterance
        return is_valid

def create_skill():
    return DevExGetResponse()

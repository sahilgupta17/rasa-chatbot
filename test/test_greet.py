from rasa_nlu.model import Interpreter
nlu_model = Interpreter.load('./models/chatbot.tar.gz/')
print(nlu_model.parse('good morning, how are you today?'))
print(nlu_model.parse('does covid spread through air'))
print(nlu_model.parse('what is going on?'))
print(nlu_model.parse('how is life'))
print(nlu_model.parse('good evening'))
print(nlu_model.parse('how is the day for you'))


#print(nlu_model.parse(''))
#print(nlu_model.parse(''))
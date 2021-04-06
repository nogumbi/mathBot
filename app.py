from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from pytz import UTC

my_bot = ChatBot( 
    name = "Bantu",
    read_only=True,
    logical_adapters = ["chatterbot.corpus.english", "chatterbot.logic.BestMatch"]
)

small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'That is excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m Bantu. ask me a question, please.']

chatBot_talk_1 = ["ChatBot",
    "A chatBot is a program that simulates a conversation between a user and a computer."]

chatBot_talk_2 = ["Invention",
    "developed by MIT professor Joseph Weizenbaum in the 1960s."]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, chatBot_talk_1, chatBot_talk_2):
          list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train("chatterbot.corpus.english")   

while True:
    try:
        request = input("You: ")
        response = my_bot.get_response(request)
        print(f'Bot: {response}')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from pytz import UTC

my_bot = ChatBot(
    name="MathBot", 
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation"]
)

#Training with personal Questions and Answers
small_talk = [
    'hi there!',
    'hi!',
    'How do you do?',
    'i\'m cool.',
    'fine, you?',
    'always cool',
    'i\'m ok',
    'glad to hear that.',
    'i\'m fine',
    'glad to hear that.',
    'i feel awesome',
    'excellent, glad to hear that.',
    'not so good'
    'sorry to hear that.'
    'what\'s your name?'
    'i\'m MathBot. ask me a math question, please.'
]

math_talk_1 = [
    'pythagorean theorem'
    'a squared plus b squared equls c squared.'
]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.logic.english')

while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name} : {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
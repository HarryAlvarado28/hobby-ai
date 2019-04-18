from chatterbot import ChatBot

chatbot = ChatBot(
    "Ejemplo Bot",
    trainer = "chatterbot.trainer.ChatterBotCorpusTrainer"
)

chatbot.train("chatterbot.corpus.spanish")

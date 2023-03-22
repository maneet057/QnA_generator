import helper

def generateQuestions(text):
    nlp = helper.pipeline("e2e-qg", model="valhalla/t5-small-e2e-qg")
    question = nlp(text)
    return question

def generateAnswers(text, questionList):
    nlp = helper.pipeline("multitask-qa-qg", model="valhalla/t5-base-qa-qg-hl")
    answers = []
    for question in questionList:
        answers.append(nlp({
            "question": question,
            "context": text
        }))
    return answers
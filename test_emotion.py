from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

emotion = pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa',
                    return_all_scores=True)

aha_moments = {
    'motivation': [
        "I was discouraged and caught up in thinking that my current job does not have any purpose. The lesson was very timely, I realize that I had ignored how my work in algebraic geometry is used by physicists and is therefore fundamentally meaningful.",
        "During the pilot, I understood how powerful my fictional heroines can be, and how motivating it is to think of them. I realized the power of motivational quotes, and I wrote one of them on my mirror so that it is the first thing I see every morning.",
        "I find missing purpose quite painful, so I am glad that Zhennovate helped me formulate concrete steps to improving the purpose of my current commitment. I remember that visualizing the goal (PhD diploma) helped me overcome my initial struggle, and I expect that the service and craft values will help me become more motivated and effective while doing my graduate program."
    ],
    'confidence': [
        "My experience is that I don’t speak up because I don’t want to be perceived as dumb or incompetent or, even worse, weird. I won’t allow what I “think” others are thinking to shape what I will say or ideas that I would like to put forward.",
        "I have to admit I don’t think about self acknowledgement very often if at all, It is funny and perhaps sad that when someone says something positive to me I am shocked and a little embarrassed. That needs to change because over the years I have received acknowledgment – from colleagues, customers, and quite honestly aren’t they the ones who count the most because they are the ones I impact the most and who impact me?",
        "Before the pilot, I had a pessimistic and unconfident outlook on my work and other projects; not sure about my capabilities. After the pilot, I learned how to engage with my negative attitude – notice when my negative voice in me is just criticizing me and I can work with it."
    ],
    'emoproductivity': [
        "As a result of learning about my perfectionism, I decided to show my plan to my adviser before I make it perfect, because I am supposed to be learning, and if I get feedback earlier, I will be able to learn faster.",
        "The lesson helped me overcome the initial stress wave of the long to-do list and tight schedule. Later in the day, I worked the remaining stress out.",
        "Today, I asked a colleague for help on the presentation. Moving forward I’m going to ask for collaborators on building the program next year.",
        "A recurring theme for me is around time management and the trap I fall into with regard to use of my time. This is often a source of anxiety and underlying tension in personal interactions and I often do not recognize my personal power to make this different. I alternate between victim (seeking help for choices I made) and rescuer (exacerbating time management by voluntarily taking on tasks)."
    ],
    'creativity': [
        "I’ve been thinking about my relationship to failure and I really get how I basically only do things I know I’m going to ace. But I’m starting to see why my creativity has been so stifled – because I only do things that I’m close to perfect at.",
        "I can’t be connected to my creativity when I’m emotionally shutting myself down too. For something for myself to reflect on, what about: what is the impact on me and those in my life of my not giving myself the space to feel, experience and be witnessed in the breadth of my emotional vulnerability and humanity?",
        "I have been thinking about culturally responsive design. I have been saying all year that “The things I hand out to customers are pretty prescribed. What can I DO?” Recently, I realized I needed that last sentence to be “What CAN I do?” and roll up my sleeves and get to work. Just because it is hard doesn’t mean I am absolved of responsibility. So time to dig in and earn my keep at this place.",
        "If I want to live the life I want to live (creative/authentic/truthful) then I am going to have to hop in bed with failure and snuggle up."
    ],
    'conflict': [
        "Before the pilot, I found myself fairly stuck in damaging cycles of thought and emotion, especially around work. After the pilot, I am now far more comfortable withdrawing from drama. I no longer feel as if I’m abandoning my colleagues if I do not enter the triangle with them, or if I exit it after having been there. I now have names for alternative roles I can play to support them, no drama necessary.",
        "It’s important to recognize the drama triangle and understand the choices I have and personal agency. Also, focusing on goals and communicating those with others. By focusing on goals and choices, I think it takes it out of this framework and becomes less of a source of frustration and potential conflict.",
        "Because I’ve learned better, more than just an “I’m sorry,” but a REALLY GOOD apology, like, detailed, honest, open, whole, complete, acknowledging every part of what was wrong and how I can do better."
    ],
    'workculture': [
        "The lessons and reflections did a great job orienting my mind to the right place. I was able to think of the Kudo board when the lesson asked me to pass acknowledgement to someone else. ",
        "New action I am practicing this week – Being willing to engage in “discovery” conversations where you talk to people without knowing where the conversation will go, but looking for common ground and shared purpose.",
        "I need to find ways to restructure my team’s interactions so that we spend more time talking about what is awesome about each other than we do talking about what sucks. We have tried to do this before, but I think I have some insights into how to do that better now."
    ],
    'support': [
        "So making space would look like. . . Literally pausing in the conversation, not responding too quickly, allowing silence to let the other person go on if they choose, or myself, not immediately challenging my own negative emotions as soon as they occur.",
        "I’ve LEARNED that it’s important to validate people’s emotions before moving on to trying to fix the underlying issues. I’m working on doing that better. I need to do that for myself too. I don’t give myself enough time to heal after an “I’m sorry,” Once I’ve said I’m sorry, I want to move on.",
        "I’d open up to co-workers and explaining or teaching them duties or taking instruction in more detail. Rather than telling them to do a task."
    ],
    'strategy': [
        "I learned that changing an hour every day can significantly impact the rest of the day (power of morning routine).",
        "Through the pilot, I learned a bit better about how to reflect on my experiences – understand what my core values and and when I get frustrated about something, why it is – because it often doesn’t fit with my values; take more action.",
        " learned to check activities with my values to decide whether to do it or not; learn to recognize the negative voice (thought ive been forgetting); think about being burnt out – “enjoying and focusing on the process rather than the results” – have me more to think about but still need to keep learning."
    ]
}

for moment in aha_moments:
    emotion_labels = emotion(aha_moments[moment])
    print('CLASS: {}, LABELS: {}'.format(moment, emotion_labels))
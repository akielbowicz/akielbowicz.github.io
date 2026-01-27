---
layout: default
title: "Resonant Coding: A Method to Master AI Chaos"
lang: en
---
# Resonant Coding: A Method to Master AI Chaos

*This post is also available in [Spanish](/2026/01/25/resonant-coding.html).*

*This article adapts ideas from Charly's post on Resonant Coding[^charly] and is an adaptation of what was presented in last week's fridAI[^fridai]. It assumes no prior technical knowledge.*

### The problem: people doing whatever

For some months now I've been leading a development team at Mercado Libre, building something from scratch to support Financial Planning. The team was new, with few experienced people, which meant I had to review almost everything. And at the same time, the company was pushing us to use Artificial Intelligence to "accelerate"[^accelerate].

The result was a fairly absurd paradox: we found ourselves flooded with AI-generated code that was hard to understand, didn't always meet minimum quality requirements, and turned reviews into an endless back-and-forth. Instead of going faster, we were stuck.

Frustrated, I started looking for references. That's how I found the ideas of Steve Yegge and Dex Horthy[^context-eng], which gave me a framework to start building something. This is the synthesis we ended up applying in the team.

And here's the curious part: at the end of October, the quality of the code they delivered suddenly improved. For a couple of days I thought we had achieved something. That the method was working.

Then I discovered that one of the tools we were using had updated itself.

It wasn't us. It was the software. And if the software could improve without our intervention, it could also get worse. Or change in ways we didn't understand. We couldn't depend on that. Coincidentally, around that time the book *[Vibe Coding](https://itrevolution.com/product/vibe-coding-book/)* came out, which validated many of the ideas I had been developing.

For our process not to depend on the randomness of an update, we need to stop seeing AI as a magical black box and understand how it actually works. Only by knowing its limits can we design something that compensates for them.

### Understanding the beast

Before talking about the method, a necessary detour. Without understanding how these language models (LMs)[^lm] work, nothing that follows will make sense.

What you need to know:
- They are **text predictors**. Like your phone's autocomplete, but trained on an amount of data that's hard to conceptualize without resorting to astronomical metaphors.
- **They have no memory**. Every time you talk to them it's like the first time. What some tools call "memory" is a trick: they save part of the conversation and silently paste it at the beginning of each new message[^memory].
- **Their attention is limited**. And the longer the text you give them, the worse they work.
- **They're not predictable**. For the same question they can give different answers.

To understand the attention issue, let's do an exercise. You're at lunch and you ask: "What can I cook?". The possible answers are infinite and probably useless. Now ask: "I need to prepare something for 6 friends on Sunday, something easy, I have chicken, potatoes and tomatoes". The constrained question guides toward a useful answer. The same thing happens with AI.

The problem is that attention gets "dirty". The best way to think about it is with an analogy that came to me during a conversation about camping: imagine you went camping and to wash dishes you have to go to the river with a bucket to fetch water.

- With one dish, the bucket is more than enough.
- With ten, the water starts to get murky and you have to be careful.
- With a hundred, the water is so dirty that the last dishes come out worse than they went in.
- And if at some point you throw something greasy into the bucket—irrelevant information, contradictory instructions—the water becomes unusable for everything that follows.

To take advantage of that limited attention, you need to be careful about what you put in and divide big problems into smaller parts, using a "clean bucket of water" for each one. When you manage to match the information you give with its attention capacity, the system "resonates" and the quality of the response improves dramatically.

### The Rule of 5

Here comes the second ingredient, something Steve Yegge calls the **"Rule of 5"**[^rule5]. It's not so much a rule as an iterative refinement process. The simplified version: when you generate something, you pass it through five successive filters.

1.  **Draft:** Create the initial content. It doesn't matter if it's perfect, what matters is that everything is there. Prefer breadth over depth.
2.  **Correctness:** Is it correct? Fix errors, inconsistencies, things the model might have made up.
3.  **Clarity:** Is it understandable? Simplify, eliminate jargon, explain everything clearly.
4.  **Edge Cases:** What could go wrong? Is there something unusual we're not considering?
5.  **Excellence:** Is this the best we can do? Optimize, polish, improve.

The five steps don't always have to be applied in that order or always completely. Sometimes a document needs more work on clarity than on correctness. The point is to have a review structure, not to follow it blindly. This cycle applies to each phase of the method.

### The method: three movements

I won't describe this as a recipe because in practice it's messier than that. But there are three general movements that repeat.

#### Research

Before doing anything, you need to understand the problem. You ask the model to investigate what already exists, to identify the important parts and how they connect to each other, to find relevant documentation. The model does this fairly well because it's essentially reading and synthesis.

But—and this is important—the document it generates has to be reviewed exhaustively. The models are very good, but there are always things they miss because they don't exist concretely in the project materials. They're ideas or knowledge that's implicit in people's heads. Human review is the opportunity to make it explicit.

#### Planning

With the research document already reviewed, we start a new conversation (clean bucket) and generate an action plan. The trick: each task in the plan has to be small enough to fit in a single bucket. If a task is "build the entire user system", it's too big. If it's "add password verification on the login screen", we're better off.

Each of these small tasks goes, again, through the Rule of 5. A poorly defined plan can generate thousands of lines of incorrect code, and by that point it's too late[^shift].

#### Implementation

By this point it should be almost mechanical. We already have almost completely defined what's going to be done, so there's not much room for the model to deviate or invent new things. And this is where they really shine: it costs them nothing to modify twenty files, create validation tests, reorganize complete structures. What would take a person hours, for them is a matter of seconds.

At the end, we apply the Rule of 5 to the complete set again.

### From task to template

The good thing about this process is that it's reusable. It doesn't just deliver a working program; it leaves you with a byproduct of instructions and criteria that have already been filtered through the Rule of 5. These pieces of knowledge become reusable templates.

For example, Charly used deep research tools to study methodologies and protocols from other professions—launching a rocket, performing surgery, organizing a World Cup—and now he can apply them in his own processes. These are procedures that have been thoroughly studied and now we can take advantage of them.

### Quick start guide

To turn this from essay to something actionable, here's the practical breakdown.

#### The three experts

Imagine you have three experts in a room. You wouldn't talk to all three at once about the same topic. Assign each one a task:

**The Researcher (Conversation 1):** Your goal is to understand. Ask them to act as an expert on the topic, to explain the key concepts and summarize them. Then review the summary with the Rule of 5. If it needs improvements, *start a new conversation*, paste the summary and ask them to refine it.

**The Strategist (Conversation 2):** Your goal is to plan. Clean bucket. Paste the researcher's summary and ask for a step-by-step plan. Review it. Each step has to be as small as possible, so it can't be divided further.

**The Executor (Conversations 3+):** For each step of the plan, new conversation. Execute, verify the result, refine if needed.

#### Why so many conversations

Every time you start a new conversation, you ensure the AI only sees relevant and refined information. In long conversations, the context fills up with drafts, corrections and doubts, and that dirties the water.

A tip: at the end of each phase, ask it to summarize the result in a clean block so you can copy it easily.

#### The art of asking

The quality of the response depends on the quality of the question.

**Vague request:** "Help me plan an event."

**Clear request:** "I need to plan a fundraising event for an animal shelter. The goal is to raise $5,000. The event will be in a park in three months, we expect 100-150 people. Give me a plan that includes: possible activities (costume contest, adoption booth), planning timeline, and how to promote it on social media. The tone should be enthusiastic and community-focused."

#### Be the director, not the spectator

Your role is to direct. Before accepting a response, filter it:
- Is it correct?
- Is it understandable at first glance?
- What could go wrong?
- Is it the best it can be, or just "acceptable"?

If it doesn't meet the bar, ask for an improvement. And if you have style preferences, save them and pass them at the start of each conversation.

### Finding resonance

A poorly given instruction can generate hundreds of lines of incorrect code. A poorly defined plan, tens of thousands. That's why this process is vital. The results of each step have to be reviewed by people. The models are very good, but the knowledge that only exists in the team's heads—implicit, not written anywhere—still has to be contributed by us.

There's something that bothers me about the dominant narrative around AI: the idea that it lets you "go faster". It's not exactly false, but it's misleading. If what we do is send everything at once, we're going to keep burning trees just for the pleasure of watching them burn[^energy].

This method is not a shortcut. It takes more time than throwing an instruction at the model and hoping something good comes out. But that time is recovered multiplied because errors are detected early, work doesn't have to be redone, and when something is finished you already know it's right[^future-work].

The idea of taking a process to something more structured brings me back to the Wave Station[^waves] in the courtyard of building 2 at university during Physics Week. Someone grabs a rope and starts shaking it. At first it's pure chaos, waves crashing into each other. But if you find the right frequency, something happens: the chaos orders itself. Points appear that don't move and points that oscillate to the maximum. Structures that sustain themselves because the system entered resonance.

With this method we do something similar: we adjust the process to find the frequency at which the team vibrates[^phorma].

### What's next

There's something that kept nagging at me while writing this: today I can generate code that's better than what I could write alone, and in a fraction of the time. That has consequences that go beyond productivity.

Where are our jobs heading when the tasks that used to define a "professional" can be done by anyone with access to these tools? How will it affect people just starting out, who haven't yet had time to build the judgment to evaluate what the machine generates? How do we train new generations for a world where execution is increasingly cheap but judgment remains scarce?

And there's another layer I don't want to ignore: tokens cost money[^tokens]. Every query has a price. Some companies give you a monthly quota; when it runs out, it runs out. Others charge per use. In any case, we're entering a new form of consumption where "thinking" has a direct and measurable cost. What happens when you run out of tokens in the middle of a project? How do you decide what's worth asking the machine and what isn't? This method isn't just a way to work better—it's also a way to be strategic with a resource that isn't infinite.

And perhaps the most uncomfortable question: who will have access to these tools and who won't? The disparity that could generate is something I want to explore more carefully.

These are questions I don't have resolved, but that I want to develop in future posts.

---
### Notes

[^charly]: Charly's original post on [Resonant Coding](https://charly-vibes.github.io/microdancing/en/posts/resonant-coding) has more technical details and concrete examples.

[^fridai]: The ***fridAIs*** are bi-weekly one-hour meetings we hold in the team to share practices about using AI at work.

[^accelerate]: "Accelerate" is one of those words that in corporate contexts simultaneously means everything and nothing. It can mean "produce more" or "spend less" or "adopt the trendy technology" or some combination of the above.

[^context-eng]: Dex Horthy's "Context Engineering" ideas can be explored in this [technical document](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md). It's dense but worth it.

[^lm]: **LM (Large Language Model)**: A type of artificial intelligence program trained to understand and generate text in a way similar to a human. Essentially, probabilistic text predictors that are very advanced.

[^memory]: What some tools call "memory" is actually a trick: they save part of the previous conversation and add it to the new message. It has limits, and when they're exceeded you have to trim. Something is always lost.

[^rule5]: Steve Yegge's Rule of 5 is in his [original documentation](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml).

[^shift]: The practice of detecting errors as early as possible is known as "shift-left". The idea is that the sooner you find a problem, the cheaper it is to fix.

[^energy]: It's not just a metaphor. Every query to a language model consumes energy and resources. Using them without criteria has a real cost.

[^future-work]: The implications of these changes are profound. In a future post I want to explore what skills we'll need to adapt, and also a more critical view of who will have access to these tools and the disparity that could generate.

[^waves]: The Wave Station is a physics experiment that shows the phenomenon of resonance. You can see a [video demonstration](https://www.youtube.com/watch?v=6zBknO95rB4) from Physics Week at UBA.

[^phorma]: I apply these same methodologies to scientific research and industry through my venture [phorma scientific](https://phorma.sh/).

[^tokens]: Model providers (Anthropic, OpenAI, Google) charge by the number of tokens processed, both input and output. A token is approximately a word or part of a word. Tools like Cursor or GitHub Copilot include a monthly quota; when it runs out, you either pay more or wait until next month. This creates a new economy where you have to think about when and how you use each query.

---

---
layout: default
title: "Beyond the Prompt: Building Software with Intentionality"
lang: en
---

# Beyond the Prompt: Building Software with Intentionality

Since I decided to [take the first step](/2026/02/18/the-first-step-en.html) and leave behind known structures, one obsession has dominated my thoughts: how to preserve the sense of craft in an age of near-infinite production. Writing code has shifted from manual carving to heavy machinery operation, but the problem is that today we are operating these machines without blueprints and in the dark.

We can raise structures at terminal velocity, but that speed is a trap. Without a clear design, we end up accumulating digital debris faster than we can understand it. In a post by Charly on [Walk this WAI](https://charly-vibes.github.io/microdancing/en/posts/walk-this-wai.html), he speaks about the philosophy of intentionality and why it makes no sense to insist on hand-coding tasks that the machine has already solved. Today, I want to bring that down to earth and show exactly what the workflow I am implementing looks like, step by step.

#### **The Problem of Blind Automation**

The most common mistake today is treating these tools like an automatic hammer that doesn't need blueprints. If you ask for code without context, you get a structure that stands by pure chance. The true leap in quality doesn't happen through simple *prompting*[^incitations], but through the design of a robust work ecosystem[^aix].

For the machine to work with us rather than against us, we first need to build an infrastructure where the system can **resonate**[^resonant-coding]. It’s not just about firing off commands; it’s about building an environment specifically designed so that our intent doesn’t get lost in the noise.

This is where **WAI**[^wai] comes in. As we work, AI generates a wealth of knowledge artifacts—research, usage details, technical decisions—that usually end up scattered. WAI was born to orchestrate all of that, ensuring that best practices and quality definitions aren't something we "have to remember to do," but are integrated by design into the production flow.

Only on this foundation of control and orchestration can we apply the five non-negotiable moments of my workflow:

#### **Phase 1: Audit and Mapping**
Before moving a single brick, you must understand what is already built: both in the specifications and the actual code. This is a forensic audit to know where we stand. This is the first **guardrail**: if you don't have clear foundations, you cannot project a serious renovation.

#### **Phase 2: Delta Design (The Proposal)**
With the map ready, we define what we are going to touch and, above all, how we will validate that the change is consistent. We use **OpenSpec**[^openspec] to generate a change proposal that includes the design of the tests.

This is where we apply the first major **backpressure** filter: we subject the proposal to the **Rule of 5**[^rule5] and specialized review protocols[^incitations-review]. If the design is unconvincing or has cracks, it goes **back to the drawing board** immediately. We don't move forward until the intent is bulletproof; correcting things here is almost free.

#### **Phase 3: Atomic Fragmentation (Beads)**
Once the proposal is firm and reviewed, we break it down into minimum units of work: **beads**[^beads]. We create tickets with clear dependencies so they can be worked on autonomously.

#### **Phase 4: Refining the Work (Ticket Review)**
Before implementing, we go over everything with a fine-tooth comb. We review the tickets together, applying the **Rule of 5** once again. This is the moment to polish every detail; the system forces us to achieve excellence before the machine starts producing code.

#### **Phase 5: Implementation and Closing**
Only now do we implement, ticket by ticket. Each one closes with its own final review to ensure that what was built fits perfectly into the slot we originally designed.

---

#### **The Value of Craft in the AI Era**

Many ask me if this workflow sets technical experience aside. My answer is that it empowers it more than ever. To direct the machine, you need to know what to ask, how to evaluate architecture, and where the dangerous edges of the technology lie.

But this path also works in reverse: it is the key for non-technical people to begin building. **Today, you no longer need to know how to program** in the traditional sense to raise a system, but what is non-negotiable is following a clear methodology. My goal is to provide these creators with the rigor and processes necessary so that their vision doesn't get diluted into a fragile structure.

As Charly’s post says, the ethical response to the hyper-velocity of AI is the **antidote of the pause**: producing less, but thinking much more. This is the core of my new chapter as a consultant: helping others evolve from the **execution of details** to **systemic mastery**.

It’s not about learning to use a new tool; it’s about redesigning our relationship with technology. It's about stopping the fight against the current and starting to build the dams that give shape and purpose to the water.

---

### **Notes**

[^aix]: **AIX (AI Experience):** The practice of designing the development environment (config files, documentation, rules) assuming the primary user is an AI agent. Good AIX drastically reduces hallucinations by giving the machine clear "guardrails."

[^incitations]: **Incitations:** My personal collection of recognition protocols and thinking structures on [GitHub](https://github.com/charly-vibes/incitaciones).

[^wai]: **WAI:** A knowledge and tool orchestrator designed to capture research, decisions, and best practices, ensuring the development infrastructure maintains quality across every artifact produced. See the project on [GitHub](https://github.com/charly-vibes/wai).

[^openspec]: **OpenSpec:** An open standard for defining what a program should do in a way that is readable for language models, facilitating AI autonomy without losing traceability.

[^resonant-coding]: **Resonant Coding:** A method for mastering AI chaos by tailoring the process to find the frequency at which the team vibrates. Read more in [my previous post](/2026/01/25/resonant-coding-en.html).

[^rule5]: **Rule of 5:** An iterative refinement process (Draft, Correct, Clarity, Edge Cases, Excellence) that ensures quality at every step.

[^incitations-review]: **Incitations Review:** Specialized audit protocols (security, architecture, readability) that are part of my collection of **prompts and metaprompts** on [GitHub](https://github.com/charly-vibes/incitaciones).

[^beads]: **Beads:** Atomic units of work representing a minimal and independent change. Chained together, they form the complete history of implementation. Concept based on the work of [Steve Yegge](https://github.com/steveyegge/beads).

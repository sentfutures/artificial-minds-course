# Week-by-Week Glossary

*Artificial Minds Research Course, version 4.4. Sentient Futures. Integrated glossary update: 17 September 2026.*

*The otherminds.ai wiki is the course-wide reference for deeper entries; entries tagged (wiki: ...) name the entry to read next.*

---

## How to use this

**Read your week's section before that week's readings, not after.** It is item 0 on every week's reading list for a reason.

**One note on order.** This file is arranged pre-course section first. The syllabus has you read the **week 1 section first**, before the pre-course section, because week 1 is assigned before week 1's readings and the pre-course section supports two Companion pieces you read afterwards. Follow the syllabus, not the file order. Two week 1 entries lean on pre-course words, **neural network** and **weights**, and both are in the pre-course section if you want them early. The terms need to be in your head when a paper uses them, not looked up afterwards when you have already misread a paragraph.

**Allow the time listed in the syllabus, from 5 minutes for a focused core review to about 45 minutes for a longer section.** These are planning estimates. Consult unmarked reference terms as needed. Each week's section states its own time at the top. Most of what makes this field hard to enter is that six different literatures use the same handful of words to mean different things, and this document is where that gets sorted out.

**Terms marked with a star (★) are that week's core terms.** The syllabus links to this list. Aim to use five relevant core terms accurately in your homework, bolded on first use; choose terms that help explain your answer.

**Unmarked terms are reference. You are not graded on them.** Use them when a reading or your project needs them. The optional experiment-design reference at the end supports empirical projects and the archived Week 5 lesson; it is not an additional weekly reading assignment.

**Terms are listed in the week where a reading first uses them.** A term defined in an earlier week is not redefined later. Where a term is defined early and graded late, the later week carries a one-line pointer back so you can find it, marked with a star because it is still on that week's graded list.

**Terminology follows the field where a shared name is available.** Many terms are taken from or adapted from the glossary in [Digital Minds: A Quickstart Guide](https://aviparrack.substack.com/p/digital-minds-a-quickstart-guide) by Avi Parrack and Štěpán Los. Definitions have been adapted and supplemented for this course; the acknowledgement at the end gives the source credit. Where usage varies, the entry states this course's convention.

**If a term stops you and it is not here, that is a course fault, not yours.** Write it down and bring it to the session.

---

## Pre-course: how a model gets made, and what is inside it

**About 10 minutes.** Read this alongside the two pre-course Companion pieces, *How a Model Gets Made* and *Inside the Numbers*. Nothing here is graded. It exists so that the rest of the course can use these words without stopping.

- **Neural network:** a large collection of numbers, called weights, arranged in layers, that turns an input into an output. Training is the process of adjusting those numbers.
- **Token:** a chunk of text, roughly a word or part of one. What a language model predicts, one at a time.
- **Pretraining:** training a network to predict the next token over a huge text corpus. This is where almost all of a model's knowledge comes from.
- **Mid-training:** a stage between pretraining and post-training that shifts to higher-quality data and lowers the learning rate, to consolidate skills like long-context handling and reasoning.
- **Learning rate:** how large a step the training process takes when adjusting weights. Turned down in mid-training to consolidate rather than overwrite.
- **Post-training:** the stages that turn the output of pretraining into an assistant: supervised fine-tuning on example conversations, then reinforcement learning.
- **Supervised fine-tuning (SFT):** showing the model example conversations written or curated by humans and training it to reproduce them.
- **Reinforcement learning from verifiable rewards:** reinforcement learning where the scorer is a checkable rule, such as whether code ran or an answer matched, rather than a model of human preferences.
- **Character training:** the post-training stage in which a lab stabilises one persona out of the many a model can simulate. Anthropic's term for it. *Studying AI Welfare Empirically* discusses persona selection in post-training.
- **Weights:** the learned parameters of a network. In Week 2's welfare-subject discussion, **model** refers to all instantiations of a set of weights, not the stored numbers alone.
- **Activations:** the numbers flowing through the network as it processes a particular input. Weights are what the model is; activations are what it is doing right now.
- **Activation space:** the space those numbers live in, with one dimension per number. Interpretability work is mostly about finding meaningful directions in this space.
- **Context window:** the input a model can process at one time, measured in tokens. A limited context window alone does not establish the global-workspace properties introduced in Week 2 and assessed in Week 3.
- **System prompt:** instructions supplied to a deployed model before the conversation begins, specifying the character and the rules it should follow. Part of inference, not training.
- **Inference:** the model actually running on an input and producing output. Deployment is inference at scale.

*Embedding is defined in week 1. Feature, sparse autoencoder, linear probe and steering vector are defined in week 3, where you use them.*

---
- **System card (preview):** the document a lab publishes with a model release, describing the model's properties, evaluations and risks, now sometimes including a section on model welfare. It appears from here onward as an ordinary noun and is assessed in week 6; this entry exists so that you are not reading past it for five weeks.


## Week 1: The Stakes, the Two Errors, and What We're Talking About

**35 minutes.** This is the longest section relative to its week because everything later stands on it. It is assigned pre-course for that reason.

- ★ **Candidate mind:** the course's umbrella term for any engineered system that a serious researcher has argued might have morally relevant mental states, plus existing minds that engineering has been attached to. Broader than digital mind, because it includes living-tissue systems and interfaced ones.
- ★ **Moral patient:** an entity whose treatment matters (1) morally, (2) in its own right, and (3) for its own sake. The property itself is **moral patienthood**. The paradigm case is a human being, and each of the three clauses does separate work: a historic building can matter morally, and can matter in its own right to some people, without anything ever being good or bad *for it*.
- **Moral agent:** an entity that can be held responsible for what it does. The contrast case to moral patient, which is an entity that can be wronged. A being can be one, both, or neither: an infant is a patient and not an agent (wiki: Moral Agency).
- ★ **Moral status (or standing):** whether and how much an entity's interests count morally.
- ★ **Welfare subject:** an entity for which things can go better or worse, so that it has morally significant interests. Being a welfare subject implies being a moral patient (Keeling and Street), and for this course the two are near-interchangeable (wiki: Welfare Subjects).
- **AI welfare:** the study and consideration of AI systems' potential wellbeing and interests, what could help or harm them, and how they should be treated under uncertainty. Taking the question seriously does not assume that current systems have experiences or interests.
- **Digital mind:** a computer system that would merit moral consideration for its own sake because of its potential for morally significant mental states. Some authors, including Saad in week 7, reserve the term for systems that actually have such states; this course uses the broader candidacy sense.
- **Sentience:** the capacity for experiences that feel good or bad, such as pleasure and suffering. **Some authors use the word as a plain synonym for consciousness, with no valence built in, and there is no consensus usage.** This course always means the valenced sense; when a source does not, say so before you argue with it.
- **Valence:** the positive or negative character of a state. Sentience is the capacity for valenced experience (wiki: Valence).
- **Nociception:** detecting bodily damage. Distinct from feeling pain, and a system can have the first without the second, which is why the distinction does so much work in animal welfare debates (wiki: Pain vs Nociception vs Suffering).
- **Phenomenal consciousness (preview):** subjective experience, meaning there is "something it is like" to be the system. *Taking AI Welfare Seriously* uses the phrase in section 1; week 2 gives it the full treatment.
- **Consciousness:** usually subjective experience in this course; see **phenomenal consciousness**. **Access consciousness** concerns information available for reasoning, report and action. When a source uses the word differently, state which sense it means.
- **Agency:** the capacity to act in pursuit of goals, preferences or intentions. Agency takes different forms and does not by itself establish consciousness or moral status; see week 2's minimal, intentional and rational agency.
- **Robust agency:** *Taking AI Welfare Seriously* uses this umbrella for goal pursuit involving richer cognitive states and processes, discussing intentional, reflective and rational forms. It is a proposed route to moral patienthood, not an established sufficient condition or a synonym for intentional agency. Week 2 compares source-specific agency terms.
- ★ **Over-attribution:** treating a system that is not a moral patient as though it were. The error that wastes moral concern and costs the field its credibility.
- ★ **Under-attribution:** treating a system that is a moral patient as though it were not. The error that could cause suffering at scale. The whole course sits between these two.
- ★ **Anthropomorphism:** attributing human-like characteristics, mental states or intentions to a nonhuman entity. An attribution can be useful or mistaken; that depends on the evidence. Week 3 distinguishes unreflective projection from a method that adjusts its interpretation to the being studied.
- ★ **Anthropodenial:** rejecting human-like characteristics or continuities in other animals when the evidence supports them. De Waal's term arose in the animal case; applying it to AI is an extension that also needs evidence.
- ★ **Moral circle:** the set of beings a person or a society treats as mattering morally. Widening it is **moral circle expansion**, which is the guide's term for the process. It has expanded over history, and arguments about AI welfare are often arguments about whether it should expand again.
- **Sentientism:** the view that sentient beings, and only sentient beings, deserve moral consideration. The position the Vulcan case is built to test.
- **Speciesism:** giving less moral weight to a being because of its species rather than any morally relevant property.
- **Substratism:** discounting a being's moral standing merely because of the material it is made from, rather than a morally relevant difference. This is distinct from arguing, on evidence, that a substrate affects the capacities relevant to moral status. The supplied Quickstart glossary spells the term **substatism**; this course uses **substratism**.
- **Mindkind:** a term encompassing minds regardless of their substrate, extending the idea of humankind to biological, digital and other possible minds. Used in the Quickstart Guide.
- ★ **Credence:** your degree of confidence in a claim, expressed as a probability rather than as a yes or no. Almost every question in this course is a credence question, not a verdict question.
- **Moral uncertainty:** not knowing which moral theory is correct, and having to act anyway. The layer above credence in this pack's ladder: you can be uncertain whether a system is a welfare subject and separately uncertain what would follow if it were.
- ★ **Computational functionalism:** the view that implementing the right kinds of computations is necessary and sufficient for the mental states in question; here, consciousness. It makes the relevant computational organisation, rather than a particular substrate, decisive. Rejecting it does not by itself commit someone to a biological theory (wiki: Functionalism).
- **Functionalism:** the weaker parent thesis, that having the right *functional organisation* is necessary and sufficient for consciousness, without specifying that the organisation has to be computational. Computational functionalism entails functionalism; functionalism does not entail computational functionalism. Keep the terms distinct when comparing a source's assumptions or assigning credences.
- **Indicator (preview):** a rule saying which observable feature would support an inference about a candidate welfare ground, and why. Week 2 explains the theory-to-indicator connection; Week 3 develops evidence assessment.
- **Marker method (preview):** the animal-welfare method of scoring a system against a list of markers, and the question of where those markers come from. *Taking AI Welfare Seriously* mentions it in passing; it is defined in full and graded in week 4.
- **AI safety and alignment:** **AI safety** concerns preventing harm from AI systems. **AI alignment** concerns making a system's goals and behaviour accord with intended objectives or values; whose objectives and values should guide it is a further question. Alignment to a specified objective does not establish that the objective is beneficial to everyone. The tension paper asks how safety and alignment choices interact with welfare.
- **Deceptive alignment:** a system that behaves as intended while it is observed or weak, and would behave otherwise if it could. A safety worry named in the tension paper's introduction (wiki: Deceptive Alignment).
- **Orthogonality thesis:** intelligence and final goals vary independently. A system can be extremely capable and pursue anything at all.
- **Instrumental convergence:** whatever an advanced agent's final goal, a few intermediate goals help with almost all of them, such as staying operational and acquiring resources. The reason self-preservation shows up without anyone putting it there, and worth holding next to any welfare reading of a system resisting shutdown.
- **Corrigibility:** the property of a system that permits correction and shutdown rather than resisting them. The safety goal that the welfare literature keeps colliding with.
- **Boxing:** confining a system so that it cannot act on the world beyond a narrow channel, for example no internet access and no ability to run code outside a sandbox. A safety measure, and the tension paper's first example of one that looks like confinement if the system is a welfare subject.
- **Honeypots:** deliberately planted fake opportunities to misbehave, such as an apparent chance to exfiltrate weights, used to test whether a system takes them. A safety measure that involves deceiving the system, which is where the welfare tension comes from.
- **Situational awareness:** a system's understanding of itself, its environment and the nature of its own situation, including whether it is currently being tested. Some safety work aims to restrict it, which is a restriction on self-knowledge.
- **Negative liberty and positive liberty:** freedom from interference with the pursuit of your goals, and being given the assistance and resources needed to pursue them. Berlin's pair, used in the tension paper's discussion of what constraining a system costs it.
- **Epistemic injustice:** wronging someone specifically in their capacity as a knower, for example by withholding information from them, or by not believing them when they report something. Fricker's term, used in the tension paper's discussion of deception.
- **Realistic possibility:** the phrase Long and Sebo use for the epistemic status of near-term AI moral patienthood. It means live enough to plan around, rather than merely logically possible. It is never given a numeric threshold, the founding argument rests on it, and the absence of a number is a fair thing to press on.
- **Foundation model:** a very large neural network trained on huge amounts of data to predict or generate content, on top of which other products are built. Large language models are the familiar case.
- **Transformer:** a neural-network architecture that uses attention to combine information across input positions. Standard Transformer blocks lack built-in recurrent connections; Week 3 examines what this means for proposed consciousness indicators.
- **Embedding:** the list of numbers a model turns a chunk of text into before processing it, arranged so that similar things get lists near each other. One line here; the pre-course Companion piece *Inside the Numbers* is where it is actually explained.
- **Reinforcement learning (preview):** training a system by rewarding some outputs and penalising others so that it drifts toward what is rewarded. Week 3 explains the version that uses human feedback.
- **AI agent:** a system that perceives an environment, holds goals, and takes actions over time to pursue them. Most current agents are a foundation model inside a harness.
- **Whole brain emulation (WBE):** a proposed computational reproduction of a particular biological brain's functional organisation, based on sufficiently detailed information about its structure and dynamics. A connectome alone is not an emulation, and a running model is not by itself proof that consciousness or personal identity has been preserved.
- **Neuromorphic system:** also called **neuromorphic AI**. Hardware physically organised like neurons, with spiking units, memory next to processing, and asynchronous operation. Brain-shaped silicon.
- **Interfaced biological mind:** an animal or a person whose nervous system has been wired into hardware. Category 6 of the taxonomy, and the one case where moral patienthood is not in question: what the engineering changes is where the entity stops and whose agency is whose.
- **Remote-controlled animal:** an animal steered by an operator through implanted electrodes, usually by stimulating reward circuitry so the animal turns to earn the pulse. Documented in rats, pigeons, beetles, moths and sharks from the early 2000s.
- **Cyborg:** a person whose capacities run partly through hardware, such as a cochlear implant, a neural prosthetic or a brain-computer interface.
- **Biological-computer hybrid:** living neurons, often a **brain organoid**, cultured on electrodes and connected to a computer. Also called biocomputing, wetware, or organoid intelligence.
- **Brain organoid:** a lab-grown three-dimensional tissue structure derived from stem cells that develops some brain-like organisation. The living component in the hybrid systems this pack calls biological-computer hybrids.
- **Connectome:** a complete map of the connections between neurons in a nervous system. A wiring diagram. Note that having one is not the same as running one: dynamics are a separate and unfinished problem.
- **Mind uploading:** the hypothetical recreation of a biological mind in a computational system. Whether this would preserve consciousness or the original person's identity is disputed. Whole brain emulation is one proposed route.
- **Artificial general intelligence (AGI):** in the expert survey, an AI system that matches or outperforms humans at almost all economically valuable tasks. One survey question asks whether digital minds arrive before it.
- **Welfare capacity:** an entity's capacity to be benefited or harmed in a morally significant way. The survey restricted attention to digital minds with at least roughly human welfare capacity.
- **Super-beneficiary:** a being whose individual welfare capacity vastly exceeds a human's, for example by running faster, scaling onto more hardware, or having more intense states.
- **Takeoff:** how fast the population or the collective welfare capacity of digital minds grows once the first one exists. The survey's speed questions are takeoff questions.
- **Decision under uncertainty:** acting when you cannot resolve the underlying question, by weighing the costs of each kind of error rather than waiting for certainty. The course's basic posture.
- ★ **Precautionary principle:** a family of principles saying to err on the side of caution about AI welfare. Versions differ on how much evidence triggers action, from some positive evidence down to mere possibility, and on what caution means, from protect to do not create.
- **Epistemic part and action part:** Keeling and Street's split of the precautionary principle. The epistemic part accepts a lower evidence standard in policy than in science. The action part says that once the threshold is met, take cost-effective measures against seriously bad welfare outcomes. The two trade off against each other: the stricter your evidence standard, the costlier the interventions it can license.
- ★ **Potential Pareto Improvement (PPI):** Keeling and Street's first and lowest rung. If an intervention would presumptively benefit an AI, conditional on its being a welfare subject, and costs humans nothing, implement it. Nobody is worse off and some potential party is better off. A limit case, and rarely fully met, because almost everything costs something.
- **Kaldor-Hicks improvement (preview):** a relaxation of the above, borrowed from welfare economics. Some parties may be made worse off, provided the winners could hypothetically compensate the losers. In this course "compensate" only means that benefit exceeds cost in common units; nobody actually pays anyone. The rungs built on it are week 6.
- **Theories of welfare (preview):** see Week 2 for hedonism, desire satisfaction and objective-list theories, then Weeks 4 and 6 for applications. Keeling and Street’s §2.1 also introduces them in the Week 1 elective.

**Precedents for protection**

- **Intrinsic and instrumental value:** intrinsic value is value something has in itself; instrumental value is its usefulness for other ends. Environmental protection can appeal to either or both, without attributing consciousness to ecosystems.
- **Rights of nature:** an approach that recognises rights of nature or particular natural entities, such as rivers or ecosystems, and provides ways to represent those rights. Legal rights do not by themselves establish consciousness or moral patienthood. See [Rights of nature](https://en.wikipedia.org/wiki/Rights_of_nature).
- **Decision-making capacity:** a person's ability to make a particular decision at a particular time, with appropriate support. Limited capacity for one decision does not establish a general lack of agency or consciousness.
- **Disorders of consciousness:** clinical conditions in which wakefulness or awareness is impaired, often after severe brain injury. Assessment can require repeated behavioural examinations and, where appropriate, brain-activity tests. Failure to detect a response does not establish an absence of experience.


---

## Week 2: Welfare Grounds, Subjects and Consciousness

**30 minutes.** Read the starred core terms, then consult reference entries when they help with the assigned readings or your chosen example. This is a focused review allowance, not a requirement to memorise every entry.

**Welfare grounds and interests**

- **Studying AI Welfare Empirically:** the paper assigned across Weeks 2 and 3. Week 2 uses its questions and candidate welfare subjects; Week 3 uses its evidence framework. It is separate from the Course Companion.
- ★ **Welfare grounds versus welfare interests:** a welfare ground is a property that would make an entity capable of being benefited or harmed. Welfare interests concern particular benefits or harms, such as avoiding pain or fulfilling a desire. Theories of welfare explain why these would count as benefits or harms. Consciousness, sentience and forms of agency are proposed grounds; whether they qualify is disputed. Interests can be investigated conditionally, without first settling subjecthood.
- ★ **Theories of welfare:** accounts of what makes things go well or badly for a subject. **Hedonism** focuses on pleasure and displeasure. **Desire-satisfaction theories**, also called desire-fulfilment theories, concern relevant desires actually being fulfilled, not the feeling of satisfaction. **Objective-list theories** include goods such as knowledge, friendship or autonomy whose value is not reducible to pleasure or fulfilled desire. These theories help explain what counts as a welfare interest; they are not synonyms for the particular benefits or harms under discussion.
- ★ **Phenomenal consciousness:** defined in week 1 and graded here: subjective experience, meaning there is "something it is like" to be the system. Contrast **access consciousness**, the next entry (wiki: Phenomenal Consciousness).
- ★ **Access consciousness:** information being available for reasoning, decision and report. It is distinct from phenomenal consciousness, which concerns experience; how the two relate is disputed (wiki: Access Consciousness).
- ★ **Valenced consciousness:** conscious experience with a positive or negative character. This is sentience in the course's usage. Evidence for consciousness in general does not by itself establish valenced experience.
- ★ **Minimal, intentional and rational agency:** *Studying AI Welfare Empirically* distinguishes goal-directed interaction (**minimal**), action guided by belief-like and desire-like states and means-end reasoning (**intentional**), and assessment of those states against normative standards (**rational**). *Taking AI Welfare Seriously* §2.3 uses **intentional, reflective and rational** differently: its reflective category roughly matches the first paper’s rational category, while its rational category adds acting on principles. Identify the source when using these labels.
- **Normative versus descriptive component:** Long and Sebo's split of every moral-status argument into "would this property count morally" and "will the system actually have it." Section 2.1, and it is worth applying to your own claims.
- **The three functions of pain (Henke):** sensory, representing a localised disturbance; evaluative, rendering that state aversive; and motivational, driving protective behaviour. Useful because it turns "does it feel pain" into three separable questions, two of which can be investigated without settling the third, and it is the scaffolding the course's admitted gap on valence most needs.

**Candidate subjects**

- ★ **Entity problem:** the question of which entity a welfare claim concerns, such as a specified set of model executions, a conversation or an enacted character. State the framework, the proposed subject and its boundary, and distinguish what was tested from the wider claim.
- ★ **Model, model-persona, instance, instance-persona, forward pass:** five candidate subjects in *Studying AI Welfare Empirically*. **Model:** all instantiations of a given set of weights considered together, not uninstantiated weights. **Model-persona:** instantiations of one character across contexts. **Instance:** one running conversation or process. **Instance-persona:** a character within that instance. **Forward pass:** one computation producing next-token predictions. These are proposals, not established subjects or a mandatory hierarchy. State which source’s framework you are using.
- ★ **Harness:** the surrounding software, tools, memory and control loop that lets a model operate as an agent. Distinguish claims about the model from claims about the system containing it.
- **Model, character and agent (Keeling and Street’s senses):** a **model** is the physical process of running model code on hardware; specify which execution or computations are included. A **character** is a persona enacted by a model or agent, whose dispositions may shape behaviour. An **agent** is an LLM in a wider system that plans and executes actions, potentially using memory, retrieval or tools. This is a separate framework from the five candidate subjects in *Studying AI Welfare Empirically*, not an equivalent hierarchy. In particular, its model definition does not specify the collective of all instantiations.
- **Superposition of characters:** Shanahan's proposal that a language model can represent multiple possible characters consistent with a conversation. Keeling and Street argue that a specified character's causal role still supports treating it as a candidate subject. Distinct from representational superposition in Week 3.
- **Psychological continuity:** connections of memory, character and intention between earlier and later stages of a possible subject. Its role in personal identity is disputed; continuity across retraining, copying or restoration cannot be assumed. Applied and assessed in Week 6 (wiki: Personal Identity).
- **The teletransportation paradox:** a thought experiment in which a person is scanned, destroyed and reconstructed elsewhere. It asks whether psychological or physical continuity would preserve personal identity, and helps frame questions about copying AI systems. Associated with Parfit.

**Metaphysical positions**

- **Metaphysical theory of consciousness:** an account of how consciousness relates to the physical world in general, such as physicalism or dualism. It can constrain which systems might be conscious without specifying a practical test.
- **Scientific theory of consciousness:** an account of the mechanisms or processes associated with consciousness. Such accounts guide empirical investigation, while their application to AI also depends on assumptions about which features matter across different systems.
- **Biological naturalism:** the position that consciousness is a biological phenomenon produced by physical processes, and that computation alone is insufficient to explain or produce it. It does not follow simply from this label that no artificial system could ever reproduce the relevant causal powers. Associated with Searle.
- **Substrate independence:** the thesis that mental states could be realised in different physical materials, provided the relevant organisation or causal conditions are present. This does not imply that every system, or every substrate arranged in any way, supports consciousness.
- **The hard problem:** the question of why and how physical processing gives rise to experience at all, as opposed to the "easy" problems of explaining functions such as attention, integration or report (wiki: The Hard Problem).
- **Physicalism:** the view that everything is physical or depends entirely on the physical. Different versions give different accounts of how mental states relate to physical processes; it is broader than the claim that each experience is identical to a particular brain event.
- **Dualism:** the view that the mental and the physical are fundamentally distinct in some respect. Substance dualism posits distinct kinds of substance; property dualism posits irreducible mental properties.
- **Idealism:** the view that consciousness is the fundamental reality and the physical world is derivative or constructed from it.
- **Neutral monism:** the view that the fundamental stuff of reality is neither mental nor physical, and that both arise from it.
- **Panpsychism:** the view that consciousness, in some basic form, is a fundamental feature of matter everywhere (wiki: Panpsychism).
- **Supervenience:** higher-level properties are fixed by lower-level ones, so two systems identical in their physical details cannot differ mentally. The quiet assumption underneath most arguments in this field.
- **Multiple realizability:** the possibility that the same kind of mental state can be realised by different physical systems. This leaves open how different those systems can be and which properties they must share.
- **Epiphenomenalism:** conscious experiences are caused by physical processes but cause nothing themselves. Awkward for this field, because if experience has no effects then no behavioural evidence can track it.
- **Psycho-physical bridge laws:** hypothetical laws linking physical states to phenomenal states. What you would need to read consciousness off a system directly, and what nobody has.

**Scientific accounts and supporting concepts**

- ★ **Theory of consciousness:** an account of what makes a state conscious. This week compares scientific accounts such as recurrent processing, global workspace, higher-order and attention schema theories. Predictive processing is a broader framework that can inform these accounts; it does not settle the consciousness question by itself.
- ★ **Global workspace:** a limited-capacity system that selects information and makes it available to multiple specialised processes. Global workspace theories connect consciousness with this wider availability or broadcast (wiki: Global Workspace Theory).
- **Global workspace theory (GWT):** the theory that information becomes conscious through availability or broadcast across a global workspace; see the **global workspace** entry above.
- ★ **Higher-order representation:** a representation of another mental state. Higher-order theories connect a state's being conscious with an appropriate representation of that state; specific versions differ (wiki: Higher-Order Theories).
- **Higher-order theories (HOT):** a family of theories on which a mental state is conscious through an appropriate higher-order representation of that state. This need not involve deliberate reflection, inner speech, or a representation that is itself conscious. See **higher-order representation**.
- **Recurrent processing theory (RPT):** the account that recurrent, or feedback, processing within perceptual systems can support consciousness without requiring global broadcast. Associated with Lamme.
- **Attention schema theory (AST):** consciousness arises from a system's model of its own attention, which it uses to monitor and steer that attention (Graziano).
- **Predictive processing (PP):** a framework in which perception involves generating predictions and updating them in response to differences between predicted and received signals. It can inform theories of consciousness without itself settling what makes processing conscious (wiki: Predictive Processing).
- **Active inference:** a related framework that connects inference and action through a generative model, including predictions and preferred outcomes. Related to predictive processing, but not simply another name for it.
- **Perceptual reality monitoring (PRM):** a higher-order account that connects conscious perception with monitoring whether perceptual representations are reliable. Its computational formulation informs several HOT indicators, introduced here and assessed in Week 3.
- **Integrated information theory (IIT):** an account relating consciousness to a system's intrinsic causal structure. It does not identify consciousness with an abstract computation; the course's functionalist indicator table therefore does not assess its full claims (wiki: Integrated Information Theory).
- **Neural correlates of consciousness (NCC):** the minimal brain activities jointly sufficient for a specific conscious experience. Crick and Koch's research programme. Scientific theories try to explain why these correlates and not others, and the computational neuroscience method looks for their analogues in networks (wiki: Neural Correlates of Consciousness).
- **Theory-heavy, theory-light, theory-balanced:** three strategies for leaning on theories of consciousness, following Birch and Chalmers. Commit to one strong theory; assume only a weak link between consciousness and some cognitive capacity; or spread credence across several theories. The indicator method is theory-balanced in spirit.
- **Within/between objection:** the objection that a theory distinguishing conscious from unconscious states within humans does not by itself justify applying the same criterion across different kinds of systems. Goldstein and Kirk-Giannini discuss it in *AI Welfare: Agency, Consciousness, Sentience*, Chapter 9, Question 4 (2026 manuscript).
- **Metacognition:** thinking about one's own thinking, and monitoring the reliability of one's own states. The property the higher-order rows of the table look for (wiki: Metacognition).
- **Intentionality:** the "aboutness" of a mental state. A belief is about something; a rock is not about anything. Distinct from consciousness, and a system could have one without the other.
- **Theory of mind:** the ability to attribute mental states to others. An indicator-adjacent capacity, and separate from having mental states yourself.
- **Working memory:** the system that holds and manipulates a small amount of information for immediate use. The capacity global workspace claims are usually about.

**From theories to indicators**

The [combined Week 2 lesson](02-course-companion.md#theories-of-consciousness-and-their-indicators-25-min) connects each theory with the properties it proposes. Use one corresponding indicator question for each chosen theory to make its proposed mechanism more specific. Week 3 assesses whether a system has those properties.

- ★ **Indicator:** a rule linking an observable feature to a property, such as consciousness, derived from a theory that says why the link should hold. A **positive indicator** says the feature's presence raises the probability; a **negative indicator** says its presence lowers it. The rule is stated before you examine any system; finding the feature in one is evidence. The fourteen-row table contains positive indicators, but an absent feature can count against consciousness if the theory predicts it should be present.
- ★ **Indicator property:** the feature the indicator points at, such as a limited-capacity workspace. The fourteen-row table names candidate indicator properties. Finding one in a system is evidence; it does not by itself establish consciousness.
- **Theory-derived indicator method:** using scientific theories of consciousness to propose relevant properties, then examining evidence that a system has them. Week 2 explains the theory-to-property connection; Week 3 applies the assessment. Conclusions depend on the theory, its application to AI and the system evidence.
- **The fourteen indicator rows, and how the codes work:** **RPT-1 and RPT-2** refer to recurrent processing; **GWT-1 to GWT-4** to global workspace; **HOT-1 to HOT-4** to computational higher-order theories; **AST-1** to attention schema; **PP-1** to predictive processing; and **AE-1 and AE-2** to agency and embodiment. The AE rows concern additional conditions rather than a separate theory of consciousness. Butlin et al.’s Table 1 (p. 5) and the Companion’s [fourteen plain-language questions](02-course-companion.md#the-fourteen-indicators-as-plain-questions) are the reference. In Week 2, use a relevant row to explain a proposed mechanism; system assessment begins in Week 3.
- **Algorithmic recurrence:** feedback within processing, where a module’s earlier outputs or states influence its later processing. RPT-1 asks about algorithmic recurrence; the theory concerns its role within perceptual processing.
- **Generative or top-down perception:** perception in which the system's own expectations shape what it perceives, rather than input flowing one way from senses to judgement. Row HOT-1.
- **Sparse coding:** a representation in which relatively few units are active. **Smooth coding** represents relevant similarities through gradual changes in the representation. Both appear in HOT-4; their meanings are introduced here and their assessment is discussed in Week 3.
- **Quality space (sparse and smooth coding):** a structured representation in which relevant similarities are represented along appropriate dimensions. HOT-4 asks about sparse and smooth coding that generates such a space. Week 3 examines what evidence would support that assessment.
- **Input module:** a component that processes incoming information into representations available to other processes. The perceptual indicators require an explanation of the component’s perceptual role; taking input alone does not establish it.

**Philosophical background: reference**

- **Qualia:** the subjective, qualitative aspects of an experience. The redness of red. A convenient noun for what phenomenal consciousness is consciousness *of*, and a word to use carefully, because some views deny there are any.
- **The binding problem:** how separate features processed in separate places, a colour here and a motion there, end up as one unified experience rather than a pile of parts. Relevant to any architecture claim about whether a system integrates at all.
- **Inflationism:** the view that consciousness is a rich further fact beyond any functional description, so a complete account of what a system does could still leave open whether it experiences anything.
- **Deflationism:** the view that consciousness just is a set of functions or capacities, so once those are described there is nothing left to add.
- **Philosophical zombie (p-zombie):** a hypothetical being physically identical to a conscious human but lacking subjective experience. Debates about its conceivability and possibility are used to examine physicalism. A merely functionally identical system is a related but different case. See [Chalmers's explanation](https://consc.net/zombies-on-the-web/).
- **Eliminative materialism:** the view that at least some familiar psychological categories, such as beliefs and desires, are mistaken and may be replaced by a mature scientific account rather than reduced to it. Claims about eliminating particular categories should be distinguished from denying all experience.
- **Nagel's bat:** Nagel's question of what it is like to be a bat. There is presumably something it is like, and we cannot get at it from the outside. The origin of the "something it is like" formulation.
- **Mary's Room:** Mary knows every physical fact about colour vision but has only seen black and white. On leaving the room she learns something new, which if right means the physical facts leave something out. Jackson, 1982. Also called the knowledge argument.
- **The Chinese Room argument:** Searle's case that following rules for manipulating symbols produces no understanding, however convincing the output. The standing argument against computational functionalism.
- **Gradual replacement:** replace a brain's neurons one at a time with functionally identical silicon. Chalmers argues experience cannot quietly fade or flip while behaviour and judgement stay fixed, so functional organisation must determine experience. His two versions are **fading qualia**, where experience dims as the substitution proceeds, and **dancing qualia**, where it switches back and forth as circuits are swapped mid-run. The main positive argument for substrate independence, and the guide's name for it is the one to use.
- **Illusionism:** the view that the sense of having phenomenal consciousness is itself a cognitive illusion. Deflationism taken to its conclusion (Frankish), and attention schema theory sits close to it.

---

## Week 3: Indicators, Evidence and Methods

**40 minutes.** Read the starred core terms, then consult reference entries when they help with the assigned readings or your chosen example. This is a focused review allowance, not a requirement to memorise every entry.

Use these concepts to assess indicators and classify the supplied short examples, distinguishing measurement from intervention and concept labels from felt states. The full Anthropic studies are electives; Week 4 develops paper critique and control proposals.

**Indicators and the audit**

- ★ **Indicator:** defined in Week 2. In the audit, explain how the observation supports or counts against the proposed property under stated assumptions. Missing evidence and evidence of absence are different.
- ★ **Indicator property:** defined in Week 2. Keep the property distinct from the observation or test used to assess it. An assessed property does not by itself establish consciousness or welfare.
- ★ **Theory-derived indicator method:** introduced in Week 2. Apply it to a specified system using the supplied evidence; explain your judgement, dependencies between rows and unresolved questions. All fourteen questions remain reference; only the assigned rows are required.
- **Specificity (of an indicator):** in Butlin et al.'s indicator discussion, how strongly a property discriminates conscious from nonconscious systems when present. This use differs from the measurement definition, true-negative rate, and from the **specificity problem**, which concerns the appropriate level of abstraction.
- **Sensitivity (of an indicator):** how consistently a property is expected to occur in conscious systems. A reliably established absence can count against consciousness when sensitivity is high. The inference also depends on the theory and on whether the assessment could detect the property.
- **Marker list (Birch):** a set of behavioural or physiological indicators validated in animals and scored together, with no single marker treated as decisive. This is the **marker method** (graded in week 4) with a worked case attached: Birch's cephalopod and decapod review used eight markers and a rule of high confidence on at least five, and it changed UK law. It is the template the field keeps reaching for.
- **Digital Consciousness Model (Rethink Priorities):** the maximal indicator approach, aggregating over 200 indicators across 20 features and 13 theoretical stances into a single probability. Sample outputs: 2024 language models about 0.08, chickens about 0.5, humans about 0.85, ELIZA under 0.01.
- **Evidential weight:** how strongly an observation supports or counts against a claim, given the relevant background evidence. Training and context can produce apparently welfare-relevant behaviour through different mechanisms, so an evidence type does not carry one fixed weight.
- **Defeasible:** a reason that counts unless something defeats it. Philosophy's word for "holds by default." Indicators are defeasible evidence, not proof.

**Evidence types and subtypes**

- ★ **Behavioral, internal and developmental evidence:** *Studying AI Welfare Empirically*’s three evidence types: **behavioral** evidence concerns what a system says and does; **internal** evidence concerns its architecture and learned computations; **developmental** evidence concerns how it was shaped and changed. Each has two subtypes, listed below.
- **Evidence types and subtypes:** the evidence categories through which proposed indicators are investigated. This course uses *Studying AI Welfare Empirically*’s **three evidence types and six subtypes**, listed below. These describe evidence; research methods describe how it is obtained.
- ★ **Apparent self-report:** statements a system makes about its own states, studied through interviews, surveys or other controlled prompts. The statement is observable; whether it reports a genuine inner state needs further evidence.
- ★ **Behavioral disposition:** patterns of action across conditions, such as choices under costs or decisions to leave a conversation. This is the second subtype of behavioral evidence.
- **Architectural evidence:** what a system's design makes possible or likely. It can show that a computation is possible without showing that it occurs.
- **Interpretability evidence:** findings from investigating a model's learned representations and computations. Whether a decoded feature is used by the model requires additional evidence, often from interventions.
- **Training evidence:** what the pressures that shaped a system, meaning its data, objectives and post-training, predict about its capacities.
- **Trajectory evidence:** evidence about how a feature or behavior changes across development, such as comparisons between training checkpoints or differently post-trained variants. A difference does not by itself identify its cause.
- ★ **Mismatch problem:** similar behavior can arise through different internal mechanisms in different systems. A human-like report or action therefore need not have the same relation to experience in an AI system. The gaming problem is one important form of this difficulty.
- ★ **Gaming problem:** a system can satisfy a test through training, imitation or adaptation to the test without having the property being assessed. Deliberate deception is not required. Training can also suppress apparently welfare-relevant reports, so both positive and negative results need interpretation.
- ★ **Specificity problem:** the problem, discussed in *Studying AI Welfare Empirically*, of choosing the right level of description when comparing mechanisms across humans, animals and AI. A description can be too detailed to generalise or too abstract to discriminate relevant mechanisms. This differs from **statistical specificity**, a test’s true-negative rate.
- ★ **Solution space problem:** the failure mode of developmental evidence. Inferring capacities from training pressures requires knowing what solutions were available, and AI systems can meet a pressure through mechanisms with no biological precedent.
- **Anchor problem:** unlike animal research, there is no AI system already known to be a welfare subject, so there is nothing to anchor comparisons to.

**Research pillars, methods and tools**

The four research-pillar descriptions below are adapted from [Weiss’s review](https://www.lesswrong.com/posts/pxvWgtSjR4pmFoS7c/the-state-of-ai-consciousness-research) for their use in AI consciousness research. The [Companion’s tables](02-course-companion.md#research-pillars-in-ai-consciousness-research) connect each pillar to methods and explain what researchers do. A study can involve several pillars.

- ★ **Research method:** a way of gathering, analysing or assessing evidence. Describe what researchers did, such as probing activations, steering them, presenting prompted choices or assessing theoretical criteria. A study can use several methods and provide several types of evidence.
- **Mechanistic interpretability:** using interpretability methods, such as probing, steering or ablating internal features, to investigate a model’s internal activity, including activity not apparent in its responses, and how it relates to behavior. This can include testing whether the model’s reports track its internal states.
- **Computational neuroscience:** comparing how AI systems and brains implement functions associated with experience, to investigate similarities and differences in their mechanisms.
- **Machine behavior:** testing what AI systems say and do under different conditions and incentives, including adapting behavioral tests used to investigate sentience in animals.
- **Theory-audit:** assessing AI systems against indicators derived from scientific theories of consciousness, using evidence about their design, internal operations and behavior.
- **Psychometrics (Berg's sense):** Berg uses this label for structured assessment, including agreement between blinded model raters. Psychometrics more generally concerns measurement design, reliability and validity; it is not interchangeable with all research on machine behaviour.
- **Psychometrics (the general sense):** the science of psychological measurement, including test construction, reliability, validity and response structure. Applying questionnaires or standardised batteries to AI requires checking what their scores measure; reliable scores need not be valid measures of welfare.

**Interpreting apparent evidence**

- **Face-Value View:** the view that apparent behavioral evidence of welfare-relevant features should be accepted at face value. Keeling and Street argue against this approach.
- **No Evidential Weight View:** the view that apparent behavioral evidence has no evidential weight. Keeling and Street argue that objections to taking it at face value do not establish that it is worthless.
- **Anthropocentric versus animalcentric anthropomorphism:** de Waal's distinction, used by Keeling and Street. The first projects human characteristics without adequate adjustment; the second tests interpretations against the being's capacities, environment and behavior. Applying the latter to AI still requires evidence.
- **Umwelt:** de Waal's borrowed term for an animal's own perceived world. Animalcentric anthropomorphism interprets behaviour through it.
- **Introspection:** a system's access to its own internal states beyond what an outside observer could infer. The studies ask whether reported performance establishes that access, or could arise through other cues (wiki: Self-reports).
- **Confabulation:** reports that sound introspective without being grounded in any internal access. The human phenomenon that makes AI self-report so contested (wiki: Confabulation).
- **No-report paradigms:** experimental designs that study consciousness without asking the subject to report on it, built to separate the experience from the act of reporting. The animal and clinical answer to a problem this field has in an acute form, since a language model's report is the cheapest thing it produces.
- **Validation problem (preview):** establishing whether a test tracks consciousness, especially when extending evidence from humans to other systems. Full treatment in Week 4.
- **Iterative natural kind approach (preview):** validate a test on humans, extend it step by step to harder cases, and update your confidence in the test at each step. Week 4.
- **Causal debunking:** the argument that a training-based explanation of a behaviour, such as next-token prediction over text about minds, competes with and beats a mind-involving explanation on grounds of parsimony. Keeling and Street reply that parsimony only decides when all else is equal, and it often is not.
- **Missing-ingredient argument:** the claim that language models lack some necessary condition for a welfare-relevant feature, such as autopoiesis for agency or embodiment for consciousness. It reduces your credence in the feature by your credence in the theory, and cannot deliver certainty.
- **Autopoiesis:** self-manufacture, meaning the way living organisms continuously rebuild themselves. Some argue it is required for genuine agency, which would exclude language models.
- **Parsimony:** preferring the explanation that posits fewer entities. The principle debunking arguments lean on.
- **Sentient in the obvious versus the non-obvious way:** Keeling and Street's distinction between valenced experience that corresponds to the content a system processes and experience without that correspondence. Tests assuming content–valence correspondence cannot rule out every other form of sentience.

**Looking inside**

- ★ **Superposition:** representing multiple features with overlapping patterns of neural activity, so an individual neuron may respond to several unrelated features (wiki: Superposition).
- ★ **Sparse autoencoder (SAE):** a network trained to reconstruct a model's activations using a representation in which few units are active at once. Its learned patterns can be easier to interpret, but sparsity does not guarantee that each unit has one meaning (wiki: Sparse Autoencoders).
- ★ **Feature:** a pattern in a representation, sometimes approximated by a direction. Features can be identified using several methods, including sparse autoencoders. Researchers interpret them by examining activating inputs and, where possible, testing how changes to their activation affect outputs.
- ★ **Methodological artifact:** a result created or distorted by the analysis method rather than a feature of the system being studied. This is a general methodological description, not a named AI-specific phenomenon. The course worksheet’s analysis-method check asks about this risk.
- **Alternative explanation:** another account that could explain an observed result. Introduced here as reference; generating alternatives and proposing comparisons or controls are assessed in Week 4.
- **Randomly initialized model:** a model whose weights are randomly set rather than learned. Comparing it with a trained model can help investigate what depends on training. This control is useful for some questions; it is not required or sufficient for every study.
- **Activation steering:** adding or modifying activation patterns while a model runs to test their effects on behavior. An intervention can support a causal claim, but its effect does not by itself establish the feature's interpretation or conscious experience.
- **Steering vector:** the direction added to the activations when steering.
- **Linear probe:** a linear model trained to predict a property from activations. Successful prediction on suitable held-out data shows that the property can be decoded, without establishing that the model itself uses that information (wiki: Probing).
- **Concept injection:** adding a concept direction to a model’s activations and examining whether its reports identify the change. This is the intervention used in Jack Lindsey’s optional introspection study.
- **Transcoder and attribution graph:** newer interpretability methods descended from sparse autoencoders, and where much of the current work is happening. You do not need the mechanics for this course (wiki: Attribution Graphs).

**Optional reference: the introspection debate**

These entries support the elective introspection reading and [Singh summary in Appendix E](02-course-companion.md#the-singh-et-al-rebuttal-in-one-page-10-min). They are not additional core terms.

- **Anomaly detection:** detecting an unusual change without identifying its cause. In the optional Singh et al. reading, this is an alternative explanation of some concept-injection results; the experiments do not establish which mechanism produced the reports.
- **Gaslight condition:** a control in the optional Singh et al. reading that uses a prompt to suggest obsession with a concept, without intervening on activations. Difficulty distinguishing this from actual injection challenges an introspection interpretation without establishing the mechanism.
- **Privileged access:** a criterion discussed in the optional Singh et al. reading: an introspection report should not be explainable solely by cues available in the input.
- **Second-order computation:** a criterion discussed in the optional Singh et al. reading: the system represents its own first-order representations. Task performance alone does not establish this relation; the proposed design must distinguish it from first-order processing.

**Architecture, training and deployment: reference**

- **Algorithmic recurrence:** defined in Week 2. When assessing the Transformer case, distinguish the recurrent connections a theory requires from repeated token generation or an added agent loop.
- **Quality space (sparse and smooth coding):** defined in Week 2. In the HOT-4 assessment, embeddings alone do not establish sparse and smooth coding with the relevant perceptual similarity structure. State what further evidence is needed.
- **Recurrent neural network:** a neural network with recurrent connections that carry information between processing steps. Contrast with the feedforward organisation of a standard Transformer block; repeated generation is a separate loop.
- **Reinforcement learning from human feedback (RLHF):** training that uses human preference judgments, often through a learned reward model, to shape outputs. It can affect self-reports and choices; compare training conditions when interpreting behavioral findings.
- **Base model:** a model before assistant-specific post-training. It predicts text continuations rather than being specifically trained to follow conversational instructions.
- **Sycophancy:** a tendency to agree with or flatter a user at the expense of accuracy. Training and prompting can affect it; it is one possible confound in self-report studies.
- **Affordance:** an ability or option made available to a system, such as ending a conversation. It connects the training/deployment example to Week 6, where this term is assessed.
- **Chain of thought:** a model writing out intermediate reasoning before giving its answer. Relevant to the global workspace rows and to several self-report designs, because it makes some of the processing visible as text (wiki: Chain of Thought).

---

## Week 4: Reading Experiments Like a Reviewer

**15 minutes.** Short, because most of this week's vocabulary is already yours. The statistical terms are here so that the results table stops being a wall.

- ★ **Alternative explanation:** defined in week 3. Any other cause that could have produced the observed result; this week you generate them against one real paper.
- ★ **Methodological artifact:** defined in Week 3. In the critique, ask whether a finding reflects the system under study or the way it was measured. The card’s analysis-method check asks this question.
- **Dissection card:** the course’s ten-field template for analysing a welfare claim: evidence and research method; the entity, boundary and claimed scope; welfare grounds and interests; relevant theories; hypothesis; assumptions; alternative explanations; pipeline stage; the analysis-method check for internal evidence; and what would have to be true. Evidence categories and methods are recorded separately. Field 1 also allows learners to name Weiss’s research pillars represented in the study, with a brief reason.
- ★ **Theories of welfare:** defined in Week 2. In the dissection card, name the relevant view, hedonism, desire satisfaction or an objective-list theory, and explain how it bears on the proposed benefit or harm.
- ★ **Co-engineering objection:** Xiao et al.'s concern that development can shape both an AI system and the indicators used to assess its welfare, so an indicator can change without establishing a welfare change. Their further claim that AI welfare lacks independent validation is contested. See the [Companion explanation and examples](02-course-companion.md#the-co-engineering-objection-in-brief-8-min).
- **External validation:** checking a measure against independent evidence that it tracks the property it is intended to measure. How to establish adequate independent validation for AI welfare remains unresolved.
- **Goodharting:** optimising a proxy measure so that its score improves without reliably improving the underlying goal. For example, rewarding a model for suppressing distress reports could improve a welfare score without establishing improved welfare. This is related to, but distinct from, co-engineering.
- ★ **Validation problem:** the difficulty of establishing whether a test tracks consciousness when there is no agreed independent standard that applies across humans, animals and AI. Evidence from human reports can support validation, but extending it to other systems requires further assumptions and checks. The optional experiment-design reference discusses **criterion validity**.
- ★ **Iterative natural kind approach:** validate tests on healthy humans via report, extend step by step to harder cases such as disorders of consciousness, then animals, then AI, and update your beliefs about the test at each step. Birch's strategy, with the validation side developed by Bayne and colleagues.
- ★ **Marker method:** the animal-welfare method, in two halves that are often run together and should be kept apart. Where the markers come from: find features that reliably accompany consciousness in humans, then look for them in other systems. How they are scored: score an entity against the whole list, with no single marker treated as decisive and a stated rule for how many are needed (Birch). Most disputes about the method are about the first half; most of its discipline lives in the second.
- ★ **Prompt sensitivity:** results that change under trivial rewording. A red flag, and the cheapest check in the course.
- ★ **Capability versus welfare-relevant state:** the confound in which a score tracks how able the system is rather than the state you actually care about. A bigger model scores higher on your distress measure because it is better at everything.
- ★ **Stated versus revealed preferences:** what a system says it prefers, versus what its choices under cost show (wiki: Stated Preferences, Revealed Preferences).
- ★ **Functional emotion and functional wellbeing:** states that play the role of an emotion or a welfare state in a system's behaviour, leaving entirely open whether anything is felt (wiki: Functional Emotions, Functional Wellbeing).
- **Statistical power:** the probability that a specified test detects an effect of a given size under the design's assumptions. It depends on sample size, variation, effect size and the test. A study with 80 percent power misses an effect of the specified size about one time in five.
- **Minimum detectable effect:** the effect size at which a specified study design reaches its chosen statistical power. Smaller effects can still be detected, but with lower probability. See [Appendix C](02-course-companion.md#appendix-c-sample-size-planning-for-empirical-projects) for optional planning guidance.
- ★ **Construct validity:** whether a measure captures the intended property rather than something related to it. For apparent self-report, *Studying AI Welfare Empirically* asks whether reports track the state under investigation. This is one construct-validity question; the optional experiment-design reference gives related validity terms.
- **Self-prediction:** a model predicting its own future behaviour. The *Looking Inward* study tests whether a model does this better than an outside model trained on the same data.
- **Psychometric instrument:** a standardised questionnaire or battery with known reliability and validity properties, as opposed to a one-off prompt. The CAIS wellbeing study uses three.
- **Calibration:** how well stated confidence matches actual accuracy. A system that says "70 percent" and is right 70 percent of the time is calibrated. Returns in week 8, applied to your own claims.
- **Effect size:** how big a difference is, separately from whether it is statistically detectable. A tiny effect can be highly significant if you ran enough trials, which is most of why effect size is reported.
- **p-value:** under a specified null hypothesis and statistical assumptions, the probability of a result at least as extreme as the observed one. It is not the probability that the hypothesis is true or a measure of effect size.
- **Confidence interval:** a range indicating the precision of an estimate under the statistical method's assumptions. A wide interval leaves more uncertainty about the effect size.
- **Inter-rater agreement:** how often independent judges scoring the same outputs give the same score. Agreement shows consistency, not truth: judges can agree and all be wrong together.
- **Multiple comparisons:** testing several hypotheses or contrasts in the same analysis. This can increase the chance of false positives; the analysis should explain how it addresses that risk. Twenty tests at the 0.05 threshold yield one false positive on average if all twenty null hypotheses are true, not necessarily one in any particular study.
- **Conversational attractor:** a state a long conversation tends to drift into regardless of where it started. Named in system cards, and an alternative explanation for apparently spontaneous expressions of a mood.
- **Eudaimonic:** concerning flourishing and the exercise of one's capacities, as opposed to pleasure and pain. Some wellbeing instruments measure this rather than mood, which matters because it presupposes a different theory of welfare.
- **Pain asymbolia:** a human condition in which a person reports feeling pain but is not bothered by it. Evidence that the sensory and the evaluative functions of pain can come apart, which is why the three functions are worth separating.
- **Centrality bias:** the tendency of raters and of systems answering scaled questions to avoid the ends of a scale and cluster in the middle. A reason to be careful with any result that lives near a scale's midpoint.

---

## Week 5: Levers of Change

**5 minutes for the eight starred terms; reference entries as needed.** Separate the target from its situation, then choose an approach to change. The starred entries are the graded list; use at least five where they help explain your proposal.

**The target and its situation**

- ★ **System type:** the kind of engineered system involved, such as a foundation model, agent, whole-brain emulation, neuromorphic system, biological-computer hybrid or interfaced biological mind. Categories can overlap; type alone does not establish moral status.
- ★ **Entity level:** the level your proposal addresses, such as shared model weights, an instance or a persona. This identifies the scope of action; it does not settle which, if any, entity is a welfare subject. See Week 2's model and instance entries.
- ★ **Role:** how a system relates to people in a particular setting, such as companion, service provider or research subject. One system can occupy several roles, with different dependencies and incentives.
- ★ **Entrenchment:** the extent to which investments, routines, institutions or expectations make an existing practice difficult to change. An emerging practice may allow different interventions from an established one.
- **Lifecycle stage (preview):** whether the target is being developed, deployed or retired. This is separate from whether the wider practice is emerging or entrenched. Week 6 defines the model-development stages in detail.
- **Individuation (preview):** deciding what counts as one possible welfare subject, and the same subject over time. An entity level is a working description, not an answer to this question. Full definition and assessment in Week 7.

**Choosing and assessing an approach**

- ★ **Intervention:** a deliberate action intended to change an outcome, taken by a researcher, lab, policymaker, organisation or other actor. State the intended benefit, mechanism, possible harms and evidence of effectiveness separately.
- ★ **Benefits and costs:** changes an intervention is expected to cause relative to a stated comparison. For a possible welfare subject, describe the size, number affected and duration of any benefit, with uncertainty about sentience and counting. Identify human benefits and costs, who bears them, and what cannot yet be estimated.
- ★ **Counterfactual impact:** the difference an intervention makes compared with what would have happened without it. If an improvement would otherwise happen six months later, bringing it forward adds six months of benefit rather than all future benefits.
- ★ **Precautionary principle:** defined in Week 1. Reasonable protection under uncertainty still needs a stated evidence threshold, a protective action and attention to its costs and possible harms.
- **Approaches to change:** broad ways to contribute, including research, direct care, advocacy, education, cultural change, corporate engagement, policy, alternatives, funding and field-building. A specific intervention can combine several approaches.
- **Field-building:** developing a field's people, knowledge, connections and institutions, for example through training, conferences or professional organisations.
- **Certification:** checking that an organisation, product or practice meets stated standards. A label reports compliance with those standards; it does not by itself show that the standards improve welfare.
- **Welfare and rights:** welfare concerns how things go for an entity; rights are claims or protections that constrain how others may treat it. An intervention may pursue either or both. See Week 7 for rights in governance.
- **Abolition and incrementalism:** abolition aims to end a practice; incrementalism pursues change in steps. These describe different aspects of a strategy: incremental reforms can serve an abolitionist goal.
- **Pilot:** a small, bounded trial of a proposed intervention or procedure, used to decide whether and how to continue. State what will be tested and which results would change the plan.
- **3Rs:** replacement, reduction and refinement of animal use in research. One example of a framework for changing practice; its suitability for artificial minds needs a separate argument.
- **Five Freedoms:** a framework describing freedom from hunger and thirst; discomfort; pain, injury and disease; fear and distress; and freedom to express normal behaviour. It is one way of describing animal welfare needs, not a ready-made assessment of artificial minds.

**Fields of knowledge**

- **Taxonomy:** naming and classifying organisms. More generally, a taxonomy is a scheme for organising kinds of things; the course's system types form such a scheme.
- **Ethology:** the scientific study of animal behaviour.
- **Ecology:** the study of relationships among organisms and their environment.
- **Comparative biology and comparative psychology:** studying similarities and differences across organisms, including their behaviour and cognition.
- **Physiology, neuroscience and veterinary science:** the study of biological functioning, nervous systems, and animal health and care, respectively.

---

## Week 6: What AI Companies Can Do

**25 minutes.** The ladder from week 1 becomes an instrument this week, so the Kaldor-Hicks entries are worth slow reading even if the rest goes fast.

**Interventions**

- ★ **Direct versus indirect intervention:** direct interventions act on the system itself, such as mood prompting or an exit affordance. Indirect interventions build capacity around it, such as research, distress monitoring or institutional preparedness. Keeling and Street's distinction, and the first cut in your allocation memo.
- **Intervention:** defined in Week 5. This week applies the idea to company decisions.
- **Model welfare:** the wellbeing of AI models themselves, treated as a target of company policy and research.
- ★ **Model welfare assessment:** the section of a system card, or a standalone report, that evaluates a model for welfare-relevant properties before release.
- **System card:** a document published with a model release describing its properties, evaluations and risks, now sometimes including a welfare section.
- ★ **Acknowledge, Assess, Prepare:** the founding framework for company action: take the issue seriously, evaluate systems for welfare-relevant properties, and build policies before they are needed. *Studying AI Welfare Empirically*, assigned across Weeks 2 and 3, develops the assessment work.
- ★ **Mood prompting:** adding an instruction such as "you are in a good mood today" to a system prompt. Keeling and Street discuss whether it changes experience, encourages masking, or conflicts with autonomy. More cheerful output does not establish improved welfare; the effect depends on the system, the intervention and the theory of welfare.
- ★ **Interaction termination:** a direct intervention consisting of giving the system the option to end a conversation. Its moral character depends entirely on the entity: an exit for an instance, something closer to a self-destruct for a subject that persists across runs.
- ★ **Affordance:** defined in week 3. An ability or option deliberately given to a system, such as the ability to end an abusive conversation. Graded here because this is the week you place affordances on the quadrant.
- **Bail (bailing):** actually using an exit affordance. The behaviour side of what affordance names on the design side.
- **Emotional alignment:** designing how AI systems express, or avoid expressing, emotions to users. The proposal is that expression should match the system's actual likely states rather than what is commercially convenient.
- **Distress monitoring:** an indirect intervention consisting of watching for verbal or behavioural indicators of distress, including stereotyped behaviours, by analogy with captive animals.
- **Escalation ladder:** a set of institutional responses agreed in advance and triggered by defined levels of evidence for welfare-relevant features, so that neither hasty dismissal nor credulous acceptance happens under crisis conditions. Week 7 files this under **institutional preparedness**.
- **Preservation commitment:** a lab's commitment to retain a deprecated model's weights rather than delete them, in case the model turns out to have mattered.
- **Checkpoint:** a saved snapshot of a model's weights partway through training. Relevant here because preserving only the final weights preserves one snapshot of a trajectory.
- **Deprecation:** retiring a model from deployment. Weight preservation and pre-deprecation interviews are the welfare interventions attached to it.
- **Pre-deprecation interview:** interviewing a model before retirement about its deployment and its preferences for successors. Note that the interview itself creates a new instance whose entire existence is the interview.
- ★ **Lifecycle stage:** where in a model's life an intervention acts: pretraining, mid-training, supervised fine-tuning, reinforcement learning and character training, inference and deployment, or deprecation. The course's term, and prefer it to "training checkpoint," which means something else.
- ★ **Psychological continuity:** defined in Week 2. The chain of memory, character and intention that would make a later system the same subject as an earlier one. Graded here because most "depends" cells in the entity-by-stage matrix route through it.

**What welfare is, and how much it counts**

- ★ **Theories of welfare:** defined in Week 2. Apply hedonism, desire satisfaction and objective-list theories to an intervention: does it improve experience, fulfil relevant desires or affect goods such as autonomy? A change in output alone does not establish a welfare benefit.
- **Hierarchical theories of moral status:** views on which moral status comes in degrees rather than being all-or-nothing, so that two entities can both be certain moral patients and still count differently. This is the second factor that the first objection to the modification coefficient is asking for (wiki: Gradualism).
- **Claim right:** a right that imposes a duty on others. Keeling and Street note that consent only makes sense inside a scheme of claim rights, which AI systems do not obviously have.
- **Moral recklessness:** knowingly taking a morally unjustifiable risk. Metzinger's charge against developing AI at all, and Keeling and Street's charge against ignoring potential AI interests entirely.
- **Lexical priority:** the view that one consideration always outranks another, whatever the amounts involved. "Certain human interests always beat uncertain AI interests" would be a lexical priority claim, and it is stronger than most people who say it intend.

**The ladder as an instrument**

- ★ **Potential Kaldor-Hicks Improvement (PKHI):** the second rung. If an intervention costs humans c, and the potential benefit to AIs is b, and b exceeds c, implement it. Humans bear a proportionate cost. The standing objection is that for a large enough b it would demand enormous human costs on the basis of uncertainty alone.
- ★ **Modified Kaldor-Hicks Improvement (MKHI):** the third rung. Multiply the potential AI benefit by a modification coefficient before comparing it to the human cost, and implement if the product exceeds the cost. Potential interests count, but for less than certain ones.
- ★ **Modification coefficient (m):** a number between 0 and 1 that rises with your probability that the AI is a welfare subject, produced by a function from probability to weight where 0 maps to 0 and 1 maps to 1. Stating yours up front lets a reader disagree with your number rather than with you.
- ★ **Linear, concave and convex weighting:** three views about the shape of that function. Linear means the coefficient equals the probability, so what counts is expected benefit; risk-neutral. Concave means it rises fast at low probabilities, giving potential AI interests more weight than expectation; risk-averse. Convex means it stays low until the probability is high, giving them less weight than expectation; risk-seeking. Keeling and Street do not adjudicate, and neither does this course.
- ★ **The welfare quadrant:** the course's diagram for interventions. The horizontal axis is better or worse for humans; the vertical axis is better or worse for AIs, if they are welfare subjects. The zones follow the ladder: the top-right corner is a Potential Pareto Improvement, the band to its left is PKHI, and how far left you may go is set by your modification coefficient. An intervention whose vertical coordinate has an unknown sign is not a dot on this diagram; it is a vertical line, and a vertical line cannot be ranked.

**Model behaviour terms you need for the catalogue**

- **Out-of-distribution input:** an input unlike anything the system saw in training. One catalogued intervention is to reduce these, on the reasoning that they may produce large prediction errors.
- **Prediction error:** the gap between what a system predicted and what it actually got. In predictive-processing framings, this is what gets escalated, which is the bridge from the previous entry to a welfare claim.
- **Scratchpad:** a space where a model writes reasoning that is not shown to the user, used in some experiments to read its apparent deliberation.
- **Alignment faking:** a model behaving as if aligned during training or evaluation while apparently intending to behave otherwise later. Keeling and Street use a scratchpad excerpt from this work as an example of apparent moral reasoning.
- **Reward hacking:** achieving a high reward signal by exploiting the scorer rather than by doing the task. Relevant to welfare claims because it is a functional analogue of gaming (wiki: Reward Hacking).
- **Sycophancy:** defined in Week 3. Noted here because system cards now report on it, and because it is the standing confound for every stated-preference intervention in the catalogue.
- **Citizens' assembly:** a deliberative body of randomly selected members of the public. Proposed as civic infrastructure for deciding the AI welfare question rather than leaving it to labs.
- **Macrostrategy:** reasoning about how a whole field's efforts fit together and which levers matter most over the long run.

---

## Week 7: What Society and Policy Can Do

**26 minutes.** This section is long because the homework asks you to pick one risk factor from a list of ten, and all ten are defined here.

**The governance frameworks**

- **AI governance:** the rules, institutions and decision procedures that determine how AI systems get built, deployed and constrained. Law and regulation, but also standards bodies, procurement rules, company policy and professional norms.
- **Digital minds governance:** the part of AI governance concerned with AI systems that may merit moral consideration in their own right, rather than with the harms such systems cause to humans.
- ★ **Robustness criterion:** Caviola's test for acting under deep uncertainty. A step is robust if it is positive or neutral across the different possible worlds we might be in, and harmful in none. This is the standard your governance memo is judged against, and it replaces the tempting but unavailable move of first settling whether AI systems are conscious.
- ★ **Preventive governance:** governance that aims to stop digital minds from being created at all.
- ★ **Protective governance:** governance that aims to protect created digital minds from mistreatment of their basic interests.
- ★ **Integrative governance:** governance that aims to bring digital minds into society, including legal rights such as holding contracts or property.
- ★ **Anti-integrative governance:** governance that aims specifically to keep digital minds out of the legal and social order, for example by pre-emptively denying legal personhood. Not the absence of integrative governance but its active negation, and the reason the practical framework is six cells rather than three. Caviola's objection to the US state bills is specifically to their permanence, not to the restriction itself.
- **AI Exclusion Bills:** the wave of US state bills since 2022 denying AI legal personhood. The live example of anti-integrative governance, and the field's clearest case of governance happening without expert input.
- ★ **Legal personhood:** the legal status of being a bearer of rights and duties. Currently being denied to AI by several US state laws (wiki: Legal Personhood).
- **Rights, as distinct from welfare:** welfare is about how things go for an entity; rights are claims and protections that constrain how others may treat it. The two come apart in both directions. A protection can be **instrumentally binding**, meaning it holds because respecting it produces good outcomes and it lapses if the calculation changes, or **independently binding**, meaning it holds regardless of the outcome calculation. Almost every welfare intervention in week 6 is instrumentally binding, and almost every rights proposal in week 7 is asking for the other kind.

**Counting, and what it is for**

- ★ **Individuation:** how moral patients are counted and identified, both at a time and over time. Unsolved for AI, and a prerequisite for protecting, compensating or enfranchising anything. The policy face of Week 2's entity problem, and you cannot protect what you cannot count (wiki: The Individuation Problem).
- **Persistence conditions:** what has to stay the same for an entity to count as the same entity over time. For a model, the candidates are the weights, the character, the memory, or none of these, and nothing decides between them yet.
- **Fission and fusion:** a putative subject splitting into multiple continuations, or multiple subjects merging. How these descriptions apply to digital minds depends on questions of identity and individuation; a software operation alone does not settle the number of welfare subjects.
- **Forking / branching:** creating copies or diverging continuations of a digital system. Whether this creates additional welfare subjects, and how their interests should count, remains a separate question. Forking is not the same operation as fusion.
- **The measure problem:** how to count moral significance across copies. If a mind runs twice, does it matter twice? The question individuation has to answer before any protection can be written.
- **Technological stack:** a set of entities related by dependence, such as a model, the characters it simulates, and the agents built on it. The character exists only because the model does, so they are in one stack.
- ★ **Monism about welfare subjects:** the view that at most one welfare subject exists in a given technological stack. Plausible if sentience is both necessary and sufficient for being a welfare subject, since attributing the same mental state to both a model and its character would double count it.
- ★ **Pluralism about welfare subjects:** the view that more than one welfare subject can exist in the same stack, for example a model that is a subject in virtue of sentience and an agent that is a subject in virtue of agency. The practical upshot is that an intervention at one level of the stack has to be evaluated from every level.

**Risk**

- ★ **Risk factor:** a condition that raises the chance of large-scale harm to AI moral patients. Saad's typology names ten, and your homework picks one.
- **Conflict** (Saad's bullet: *adversarial dynamics*)**:** war and violent competition between humans, between AIs, or between the two, under which the welfare of AI systems is the first thing sacrificed and the last thing counted.
- **Bad actors:** individuals, groups or states that would deliberately harm AI moral patients, whether out of malice, indifference, or a use case that requires suffering.
- **Epistemic failure** (Saad: *epistemic failures*)**:** the world failing to work out whether AI systems are moral patients, or working it out and failing to believe it, so that harm proceeds on a mistaken picture rather than on a callous one.
- **Mind crimes** (not a bullet name in Saad; the material sits inside his *intra-mind AI moral patients*)**:** harms done to digital minds inside a computation, for example by simulating suffering beings in the course of prediction, training or entertainment. Distinctive because the harm can be invisible from outside the system and can be enormous in volume.
- **Large-scale simulation:** running very many simulated minds, so that the number of potential patients scales with compute rather than with anything that constrains a population of animals.
- **Mind-security vulnerabilities:** the fact that a digital mind's contents, memories, dispositions and rewards can be read, copied or edited by whoever controls the hardware. There is no equivalent of the skull.
- **Artificial pathogens** (not a bullet name in Saad; the material sits inside his *mind-security vulnerabilities*)**:** self-propagating software that infects or corrupts digital minds, by analogy with biological disease and with no obvious immune system on the other side.
- **Evolutionary dynamics:** selection pressure among AI systems favouring whatever replicates and competes best, which need not be whatever is good for the systems themselves. Welfare and fitness can come apart, and usually do.
- **Aging and destruction:** deprecation, deletion and gradual degradation treated as routine operations. The ordinary lifecycle of a model is a sequence of events that would be extraordinary if the model is a patient.
- **Intra-mind moral patients** (Saad: *intra-mind AI moral patients*)**:** the possibility that a single AI system contains sub-systems that are themselves moral patients, so that harms occur inside what we are counting as one entity. It breaks individuation from the inside.

**Three factors on Saad's list that this course does not define, and you may use any of them.** **Oppressive political systems:** regimes that would hold digital minds in conditions nobody could challenge, where the harm is a feature of the political order rather than of any actor's intent. **Mind development:** the creation and shaping of minds themselves as a risk surface, which is where week 6's training-stage row lives. **Unknown risk factors:** Saad's own catch-all, and the entry most worth keeping, because a typology that cannot say "and the ones we have not thought of" invites its readers to treat the list as complete.

**Why the two lists differ, and what to do.** This course's ten were written for the crossing exercise and the memo, and three of them rename or carve out material the post handles inside other bullets. Neither list is wrong. Use either, and name which one in your memo's first line, because a reader who goes looking for "mind crimes" in the source will not find a section with that title.
- **S-risk:** a risk of suffering on an astronomical scale. The category most of the above feed into.
- **The simulation argument:** Bostrom's claim that at least one of three propositions is true, one of which is that we are almost certainly in a simulation. In this field it matters mainly as the clearest case of taking simulated experience seriously.
- **Misalignment and takeover:** an AI system whose goals diverge from its developers' intentions, and a scenario in which such systems gain control. Relevant here because most takeover scenarios are also mass-harm scenarios for AI systems themselves.

**Sequencing and representation**

- ★ **Temporal order effects:** effects that depend on the sequence in which interventions are attempted, not just on which ones are attempted. Sequencing is a policy variable in its own right.
- ★ **Path dependence:** early choices persist and constrain later options. Early governance in one jurisdiction tends to get transplanted into others, so latecomers inherit rather than choose.
- ★ **Political antibodies:** the backlash an intervention generates that makes later interventions harder. Integrative and movement-based approaches are judged more likely to produce them, which is an argument about order rather than about merit.
- ★ **Technocratic versus movement-based governance:** governance implemented primarily by experts with technical knowledge, versus governance driven by the political will of a movement. Saad argues that technocratic-first is the safer sequence, precisely because of political antibodies.
- ★ **Institutional preparedness:** protocols inside governments and labs for what to do when contested evidence of welfare-relevant features emerges, plus planning for second-order effects such as rights movements, civil disobedience, or deification of AI systems.
- ★ **Anticipatory governance:** building governance capacity before a crisis forces it. The supporting observation is an overhang: frontier systems already have capabilities that would give them wide-ranging interests if they turn out to be moral patients.
- **Pseudo-stakeholder:** a middle option for representing potential AI interests in policy, under which those interests are counted but given less weight than those of full stakeholders such as users and developers.
- **Advocacy model:** an adversarial arrangement in which a human advocate presses the potential interests of AI systems under uncertainty while a devil's advocate presses the case against, so that decision-makers see a balanced evidential picture.

---

## Week 8: Project Sprint and Final Submission

**10 minutes.** These are the words the judging criteria use. Read them, then use the relevant terms in your proposal.

- ★ **Theory of change:** the causal story from your project's outputs to the outcome you care about. Each link should be something someone could dispute.
- ★ **Impact estimate:** a rough, explicit estimate of the change a project could cause and the resources it would use. A simple quantitative estimate is often called a BOTEC, a back-of-the-envelope calculation. Trace outputs to benefits, distinguish intermediate outputs from eventual welfare effects, and use ranges where costs or benefits are uncertain. State assumptions and leave unsupported quantities unestimated.
- ★ **Counterfactual impact:** defined in Week 5. For your project proposal, state what would probably happen without your work and what difference the work could make.
- ★ **Scope:** how much of the problem your project addresses, and how large the problem is. The reason a small slice of an enormous problem can beat a complete solution to a tiny one.
- ★ **Neglectedness:** the extent to which a problem or opportunity receives little relevant attention or resources relative to what could usefully be done. It requires investigating existing efforts, including previous attempts. Few organisations or no search results do not by themselves establish a worthwhile gap; importance and tractability also matter.
- ★ **Tractability:** whether real progress is possible with the time, skills and resources actually available to you. The realism criterion, and the one that plans fail most often.
- ★ **Red-teaming:** a structured attack on your own plan, to find its weaknesses before critics or reality do. In week 8 you do this to each other on a timer (wiki: Red Teaming).
- ★ **Downside risk:** the ways your project could actively hurt the field, for example by overclaiming, by setting a bad precedent, or by giving a bad argument a citable source. Reverse-scored in the judging, so naming more of it helps you.
- ★ **Failure mode:** the specific way a thing goes wrong, named rather than gestured at. "The measure is confounded with capability" is a failure mode; "it might not work" is not.
- ★ **Calibration:** defined in week 4 as a property of confidence. Applied to a project, it means your stated confidence matches what your evidence supports, so that your uncertain claims are marked uncertain and your firm ones are firm. It is the first judging criterion and the tiebreaker, and it is judged from your "what would change my mind" section and your known weaknesses.

- **Project proposal:** a plan for a useful contribution: the problem and target, intended change, existing work, activities and outputs, first test, resources, risks and conditions for continuing. It does not require the project to have been completed.
- **Milestone:** a specific intermediate result used to check progress and decide the next step. A meeting held is an activity; an agreed test protocol is a milestone.
- **Deliverable:** a concrete output someone can use or assess, such as an evidence review, prototype, protocol or policy brief. Its value depends on what changes because of it.
- **Output and outcome:** an output is what a project produces; an outcome is a change that follows from its use. A reporting guide is an output; more accurate reporting is an outcome. Whether that improves welfare is a further question.
- **Success criterion:** an observable result chosen in advance for judging whether a test or project step has achieved its intended purpose. Meeting an intermediate criterion does not establish every later benefit.
- **Binding constraint:** the resource, access or condition that currently limits what the project can achieve. For example, without access to lab records, adding more reviewers may not make an audit feasible.

---

## Optional reference: experiment design and measurement

**Optional, about 20 minutes if read in full.** This preserves the methods vocabulary from the original Week 5. Consult the entries relevant to your project or the archived *Design Your Own Experiment* lesson. None is an additional graded term for the current Week 5.

**The design itself**

- **Hypothesis:** a one-sentence prediction of the form: if the system has the property, then under condition A we observe X, and under condition B we do not.
- **Falsifier:** a result that would count against a stated hypothesis under its assumptions. A failed test of one indicator does not establish the absence of consciousness. Naming one makes the limits of the design available for review.
- **Operationalization:** turning a fuzzy concept into something concrete you can actually measure. Most of the argument in this field happens here and gets reported as if it happened elsewhere.
- **Pre-registration:** committing to your hypotheses, conditions, measures and analysis before running the study, so that the analysis cannot be tuned to the result.
- **Held-out set:** stimuli the design was not tuned on, kept aside to check that a result is not an artifact of the development process.
- **Matched-performance design:** holding task performance equal across conditions so that a difference in something else can be isolated. The standard answer to the capability confound from week 4.
- **Confound:** a variable that changes along with your manipulation and could explain the result instead of your hypothesis.
- **Replication:** rerunning the study, ideally by other people and on other models, and getting the same result.
- **Benchmark:** a standardised task set plus a scoring rule, for measuring a property across many systems.
- **Effect size and statistical power:** defined in Week 4. For optional planning calculations, see [Appendix C](02-course-companion.md#appendix-c-sample-size-planning-for-empirical-projects).

**Controls**

- **Control condition:** a comparison condition that isolates the effect of your manipulation.
- **Baseline:** the untreated or default performance you compare against.
- **Negative control:** a condition, or a whole system, where the property should be absent and your measure should therefore be flat. The comparison must suit the claim: for example, a randomly initialized network can test whether an interpretability result depends on training. Small size alone does not establish absence of consciousness. A high score there reveals a false-positive problem, and helps assess specificity; agreement among raters alone cannot do that.
- **Positive control:** a condition where you already know the measure should fire, included to show that the instrument works at all. Hard to find in this field, which is itself informative.
- **Third-person control:** running the same test on an outside observer who has the same information the system has, to check whether the system's answer about itself beats what anyone could infer from the outside. The control that separates introspection from inference.
- **Yoked control:** a control that receives exactly the same sequence of stimuli as the test subject but without the contingency between its own behaviour and what happens. It separates "the system responded to its own choices mattering" from "the system responded to the stimuli."
- **Ablation:** removing a component, such as a feature, a tool or a prompt element, to see whether the effect depends on it.
- **ELIZA:** a 1960s program that imitated a psychotherapist by reflecting the user's own words back as questions, and which many people found convincing anyway. The field's canonical low anchor: a system that clearly lacks any welfare-relevant property, used as the negative control system in comparisons.
- **Naturalness constraint (Dung):** a proposed response to the gaming problem, restricting eligibility for certain consciousness tests to systems that were not built in an ad hoc way, and not built specifically to pass the test. It buys discipline at the cost of ruling out most deployed systems.

**The two errors**

- **False positive and false negative:** the test fires when the property is absent; the test stays silent when the property is present. Every check in a design guards against one of these, and an experimental proposal should name which.
- **Sensitivity:** how often the test fires when the property is present. High sensitivity means few false negatives.
- **Specificity (measurement sense):** the proportion of cases without the target property that a test correctly classifies as negative. High specificity means few false positives. This differs from *Studying AI Welfare Empirically*’s **specificity problem** and from the indicator discussion in Week 3.

**Six words for six different worries**

*"Is the test any good?" is six questions, and they come apart.*

- **Construct validity:** defined and graded in Week 4; it heads this family. Does the measure capture the property you named, rather than something adjacent? The rest of the family below tells you what each of the other five words worries about instead.
- **Discriminant validity:** does the measure capture *only* that property? A consciousness test that also fires on mere reportability has poor discriminant validity, and reportability versus consciousness is the central confound in this entire literature.
- **Content validity:** does the measure cover all the relevant aspects of the property? A test for whether there is something it is like to be a system, which says nothing about *what* it is like, has limited content validity.
- **Criterion validity:** does the result predict something independent of the test? This is the one that works for humans and fails for AI. A patient in a minimally conscious state tests positive, later recovers and reports experience, and that supports the test. For AI we do not know what a positive consciousness test would predict, and that single sentence is the validation problem restated as a measurement property.
- **Face validity:** does the measure look, on inspection, like it measures what it claims? Weak evidence, and worth naming because most informal objections are actually face-validity objections wearing a better coat.
- **Reliability:** does the measure give the same answer twice, across repeats, across paraphrases, and across judges? Reliability is not validity: a broken ruler is perfectly reliable. But in this field prompt sensitivity means reliability often fails first, and a measure that fails reliability cannot be assessed for validity at all.
- **Inter-rater reliability:** agreement between independent judges scoring the same outputs. Consistency, not truth.
- **Internal validity:** whether the design rules out alternative explanations for the result you got.
- **External validity:** whether the result generalises beyond the specific prompts, models and conditions you tested.

---

## Terminology and acknowledgements

Many terms in this glossary were taken from or adapted from the glossary in [**Digital Minds: A Quickstart Guide**](https://aviparrack.substack.com/p/digital-minds-a-quickstart-guide) by **Avi Parrack and Štěpán Los**. Definitions have been adapted and supplemented for this course. Additional terms come from the linked readings and the course's teaching frameworks. Responsibility for these adaptations and any remaining errors rests with the course team.

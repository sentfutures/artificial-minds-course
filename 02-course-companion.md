# Artificial Minds Research Course
## Course Companion, version 4.4. Pre-course through week 8

*Sentient Futures.*

---

# What this document is

**The Companion explains the concepts and methods used in the course.**

The syllabus sets out the readings, assignments and estimated workload. This Companion introduces the background needed to assess the primary readings and complete the assignments.

Follow the numbered reading list in the syllabus. It interleaves Companion explanations and primary sources so that each prepares you for the next task.

Three practical notes.

**Use each piece’s explanation and task together.** Most pieces open with **Why this matters** and close with **In practice**. Week 5 uses a proposal task and peer-review session; Week 8 supplies the final proposal template. Each week’s resource map connects the teaching to its assignment.

**Minute counts are planning estimates.** Tell your facilitator if a weekly or component estimate was off, and identify the reading or task.

**If this document and the syllabus disagree, ask your facilitator which instruction to follow.**

Part 1 covers the pre-course, week 1, week 2 and week 3. Part 2 covers weeks 4 to 8.

---

# Pre-course

---

## How to Read This Course (5 min)

The course introduces candidate minds and possible grounds for moral consideration, examines the evidence researchers use, and develops proposals for useful work in the field.

**Weeks 1 and 2 establish the concepts.** Week 1 covers the stakes, types of system, possible futures, and tensions between AI safety and welfare. Its assignments include classifying systems and constructing a forecast chain. Week 2 introduces consciousness, sentience and agency, distinguishes candidate welfare subjects, and compares theories of consciousness.

**Week 2 connects theories with their indicator questions.** Learn what each proposed feature means before examining evidence for it.

**Weeks 3 and 4 develop research skills.** Week 3 explains evidence types, research methods and activation steering, and practises a small indicator audit. Week 4 uses the dissection card to assess a published experiment’s design, results, alternative explanations and controls.

**Weeks 5–7 move to possible contributions.** In Week 5, choose a target and situation, investigate precedents, and draft an intervention proposal with benefits, costs, conditions and a test. Week 6 considers company actions through a welfare-budget allocation memo. Week 7 considers governance through a memo to a named actor, including how the proposed step could backfire and how it should be sequenced.

**Week 8 develops a project proposal.** Use the earlier work and feedback to define a feasible next step, submitted as a one-page proposal and a 3–5 minute video. Research, tools, education, standards and governance are possible directions. The course requires a proposal; you do not have to carry it out.

**How to approach the readings.** For a definition, focus on what the term includes and excludes. For a theory, identify what it proposes and how it differs from the alternatives. For a study, distinguish the design, observations and conclusions. For an intervention, consider its intended effects, costs and practical conditions. Use the glossary and worked examples where a source assumes unfamiliar concepts, and follow the syllabus for each week's reading order and assignments.

---

## A Working Taxonomy of Candidate Minds (20 min)

**Why this matters.** A chatbot, a simulated fly brain and living neurons connected to a chip raise different questions about consciousness and moral consideration. Evidence about one may not transfer to another. This taxonomy helps you specify which system a claim concerns.

**Course terminology.** The course concerns **artificial minds**: engineered systems considered as possible subjects of morally relevant mental states. The taxonomy uses **candidate mind** to include these systems and biological minds connected to technology. This does not assume that an engineered system has experience. Caviola and Saad's forecast survey uses **digital mind** more narrowly for a computer system capable of subjective experience. Categories 5 and 6 include living tissue and biological minds.

**Sources and limits.** There is no settled taxonomy for this field. This teaching scheme draws on Caviola and Saad's grouping by architecture, Sentience Institute's grouping by substrate origin, and Jonathan Birch's discussion of organoids, emulations and language models. The categories overlap and are not a standard classification.

### The taxonomy at a glance

| # | Category | Substrate | How it comes to exist | Example |
|---|---|---|---|---|
| 1 | Foundation models | Usually silicon hardware | Trained on broad data for use across tasks | Claude, GPT, Gemini, Llama |
| 2 | AI agents | Silicon | Built on top of a foundation model, or trained by reinforcement | SIMA 2, Voyager, coding agents |
| 3 | Whole brain emulations | Silicon | Copied from a scanned biological brain | OpenWorm; the Google fly connectome is the map one would need |
| 4 | Neuromorphic systems | Brain-inspired electronic hardware | Engineered to reproduce selected neural processes | Intel Hala Point, SpiNNaker 2 |
| 5 | Biological-computer hybrids | Living neurons plus silicon | Cultured, then interfaced | Cortical Labs CL1, FinalSpark |
| 6 | Interfaced biological minds | An existing animal or human, plus hardware | Neither designed, copied nor grown: interfaced | Remote-controlled rats and beetles, cochlear implants, brain-computer interfaces |

**How to use the categories:** they describe different aspects of a system and can overlap. Foundation models and agents are distinguished by their role and operation; emulations by their relation to a biological brain; neuromorphic systems by their hardware; and biological hybrids by their living components. Classify the relevant component or system, then use the axes below to describe it more precisely.

### Category 1: Foundation models

**Plain definition.** A foundation model is trained on broad data and can be adapted to many tasks. Large language models are one example. Its **weights** are learned numerical parameters. Running the model uses those parameters to compute outputs from inputs; the stored weights and a particular running instance are different things.

Many language models use a **transformer** architecture. During text generation, a model typically produces tokens in sequence, using earlier tokens as context. This repeated generation is distinct from an agent observing an environment and acting on it.

**Why they matter here.** Foundation models are widely used, and their outputs provide accessible material for research. Their training includes human descriptions of experiences, so a statement such as "that hurts" needs controls for imitation, prompting and training incentives before it can support a claim about experience.

**The indicator method.** Week 2 introduces the features proposed by Butlin and colleagues as evidence relevant to consciousness. Week 3 assesses the Transformer/LLM case in their 2023 report.

**Resources.**
- Anthropic's published model welfare assessments. Use the system card and section specified in the week 6 syllabus.
- Butlin, Long et al., *Consciousness in Artificial Intelligence* (2023): [arxiv.org/abs/2308.08708](https://arxiv.org/abs/2308.08708)
- Google DeepMind's Gemini and Meta's Llama, as the other widely deployed families.

**In practice.** When a claim concerns ChatGPT or Claude, distinguish the underlying model from the product, conversation or agent being assessed.

### Category 2: AI agents

**Plain definition.** An AI agent is a system that observes an environment and takes actions over time to pursue goals. A language-model agent can use tools, memory and feedback within an action loop. Agents can also be built using other methods, including reinforcement learning, which trains behaviour using reward signals.

**Why they matter here.** We distinguish agents from their model components because the surrounding system can add capacities relevant to welfare assessment. The indicator framework includes agency and embodiment. Long, Sebo and colleagues also propose **robust agency** as a possible basis for moral consideration alongside consciousness. An ordinary action loop does not by itself establish robust agency or moral status.

**Resources.**
- SIMA 2, a Gemini-powered agent that plays, reasons and learns in 3D game worlds: [deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
- The SIMA 2 technical report: [arxiv.org/abs/2512.04797](https://arxiv.org/abs/2512.04797)
- Voyager, an earlier LLM-driven agent that explores Minecraft open-endedly and builds a library of skills: [voyager.minedojo.org](https://voyager.minedojo.org)
- Long, Sebo et al., *Taking AI Welfare Seriously* (2024): [arxiv.org/abs/2411.00986](https://arxiv.org/abs/2411.00986)

**In practice.** A coding agent that runs tools, encounters errors and adjusts its actions fits this category. It need not have a physical body.

### Category 3: Whole brain emulations

**Plain definition.** A whole brain emulation, or WBE, aims to reproduce the relevant structure and dynamics of a particular biological brain in a computer. Sandberg and Bostrom's 2008 roadmap describes this approach. Brain measurements constrain the model, but researchers still choose what detail to record and how to simulate it.

**Why they matter here.** Reproducing a conscious brain's relevant organization could provide evidence by analogy with the original. Survey participants rated brain simulations highly in principle but less likely than machine-learning-based AI to produce the first digital minds. Emulations also raise questions about copying, continuity and identity that apply to other computational systems.

**Where things stand.** Connectomes map neural connections. The adult hermaphrodite C. elegans has 302 neurons. Fruit-fly maps include the 2024 FlyWire female brain and the 2026 male brain and nerve cord, the latter covering over 166,000 neurons and 125 million synapses. These are substantial empirical achievements, but a structural map alone does not reproduce a brain's activity.

**Keep the map and the running system apart.** An emulation also needs models of neural activity and any relevant sensory inputs or bodily feedback. Behaviour produced by a connectome-based simulation depends on these additional assumptions. It is not, by itself, evidence that the original animal's experience has been reproduced.

**Resources.**
- FlyWire, the fruit fly connectome: [flywire.ai](https://flywire.ai)
- OpenWorm, the long-running C. elegans emulation project: [openworm.org](http://openworm.org)
- The Google Research and Janelia fly connectome work: [research.google/blog](https://research.google/blog/) and the Janelia FlyEM project pages: [janelia.org/project-team/flyem](https://www.janelia.org/project-team/flyem)
- *State of Brain Emulation Report 2025*: [arxiv.org/abs/2510.15745](https://arxiv.org/abs/2510.15745)

**In practice.** For a claim about "mind uploading," ask which brain structures and processes would be reproduced, and what evidence would support continuity with the original person.

### Category 4: Neuromorphic systems

**Plain definition.** Neuromorphic systems use hardware inspired by nervous systems. Many process signals as spikes and place memory close to computation. They reproduce selected neural principles rather than the full organization of a biological brain.

**Why they matter here.** Neuromorphic hardware offers a way to investigate whether particular physical and computational features of brains matter for consciousness. It can also support neural simulations. A system can therefore be both neuromorphic and an emulation, but neither label establishes consciousness.

**Resources.**
- Intel's Hala Point, announced in 2024, 1,152 Loihi 2 chips and about 1.15 billion artificial neurons, deployed at Sandia National Laboratories: [intel.com/content/www/us/en/newsroom/news/intel-builds-worlds-largest-neuromorphic-system.html](https://www.intel.com/content/www/us/en/newsroom/news/intel-builds-worlds-largest-neuromorphic-system.html)
- Open Neuromorphic's plain-language profile of the Loihi 2 chip: [open-neuromorphic.org/neuromorphic-computing/hardware/loihi-2-intel/](https://open-neuromorphic.org/neuromorphic-computing/hardware/loihi-2-intel/)
- SpiNNaker 2, the Manchester and Dresden spiking system: [spinncloud.com](https://spinncloud.com)

**In practice.** Someone who has heard "AI uses too much energy, but the brain runs on 20 watts" is describing the motivation behind this category.

### Category 5: Biological-computer hybrids

**Plain definition.** These systems connect cultured living neurons to computing hardware, often through electrode arrays that record and stimulate activity. The cells may come from stem cells or other biological sources. A **brain organoid** is a three-dimensional tissue culture that models selected features of brain development; it is not a complete brain.

**Why they matter here.** These systems contain living neural tissue, so they are relevant even to theories that assign a special role to biology. Whether a culture has the organization needed for experience remains an empirical and theoretical question. Research on organoids also raises ethical questions about tissue sourcing, development and possible welfare.

**Where things stand.** Cortical Labs' CL1 and FinalSpark's Neuroplatform provide examples of living neurons connected to computing systems. DishBrain experiments reported improved performance in a simplified Pong task using feedback to cultured neurons. FinalSpark has reported organoid experiments lasting more than 100 days. These findings concern culture, computation and learning; they do not establish subjective experience.

**Resources.**
- Cortical Labs: [corticallabs.com](https://corticallabs.com)
- FinalSpark's Neuroplatform: [finalspark.com/neuroplatform/](https://finalspark.com/neuroplatform/)
- Smirnova, Hartung et al., "Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish" (2023): [frontiersin.org/articles/10.3389/fsci.2023.1017235/full](https://www.frontiersin.org/articles/10.3389/fsci.2023.1017235/full)
- IEEE Spectrum on the CL1, including Karl Friston's "brain in a vat" remark: [spectrum.ieee.org/biological-computer-for-sale](https://spectrum.ieee.org/biological-computer-for-sale)

**In practice.** When a headline says "scientists taught brain cells to play Pong," this is the category.

### Category 6: Interfaced biological minds

**Plain definition.** An existing animal or human nervous system connected to hardware. Examples include cochlear implants, brain-computer interfaces and experiments that use electrical stimulation to influence an animal's movement. Stimulation methods and their effects differ across systems.

**Why this category is different, and why it is here.** In familiar cases such as a person with a cochlear implant or a rat with implanted electrodes, the biological individual already has moral standing. The interface changes their capacities and circumstances. Evidence about consciousness is less settled for some other animals, so assess the species as well as the device.

1. **Where the entity stops.** If stimulation influences a rat's movement, distinguish the animal, the device and the combined control system. The animal's moral standing does not settle how to attribute control of a particular action.
2. **Whose agency it is.** External control can influence or override an animal's behaviour. Assess its effects on the animal's preferences, capacities and welfare rather than assuming that these remain unchanged.
3. **What existing practice can teach us.** Neural-interface research already faces questions about consent, control and welfare. These offer comparisons for AI ethics, with differences in the evidence and the subjects involved.

**Where things stand.** Cochlear implants are established clinical devices; some other neural interfaces remain experimental. Their purposes, invasiveness and evidence differ, so use a specific application when assessing benefits and harms.

**Resources.**
- Remote control animals, overview and case list: [en.wikipedia.org/wiki/Remote_control_animal](https://en.wikipedia.org/wiki/Remote_control_animal)
- Backyard Brains RoboRoach, including the company's own ethics page: [backyardbrains.com](https://backyardbrains.com)

**In practice.** Use these cases to examine how a device changes an existing individual's control, interests and treatment, then state which aspects of the comparison apply to an artificial system.

### The four cross-cutting axes

Use four axes to describe systems that overlap the categories.

1. **Substrate.** What is the system made of: electronic hardware, living tissue or both? **Computational functionalism** holds that the right computational organization is necessary and sufficient for consciousness. This supports **substrate independence**, the possibility of realizing minds in different materials. Rejecting computational functionalism does not necessarily mean requiring biology; a theory might instead require other physical properties.
2. **Origin.** Was the system engineered, reconstructed from a particular brain, grown as a culture, or connected to an existing individual? Origin can inform comparisons with systems whose capacities we understand better, but does not settle the outcome.
3. **Embodiment.** Does the system control a physical or virtual body, and model how its actions affect its inputs? Some agents do; agency alone does not imply embodiment. Assess the relevant model and its surrounding system together.
4. **Copyability and continuity.** Which parts of the system can be saved, copied or restored, and what state would be lost? Software and living tissue allow different operations. Whether a restored system is the same individual is a further question.

### Edge cases

In the week 1 placement round, identify the component or system you are classifying and explain which features support your choice. More than one category may apply.

- **A whole brain emulation running on neuromorphic hardware.** Categories 3 and 4 both apply: one describes the emulation's origin, the other its hardware.
- **A foundation model used to control a robot with persistent memory.** The model remains a category 1 component. If the combined system observes its environment, chooses actions and uses feedback to pursue goals, the whole system also fits category 2. State which you are classifying. A body and stored memories alone do not establish agency.
- **Neuromorphic hardware running a machine-learning workload.** Category 4 describes the hardware. Classify the model and its role separately.
- **A brain organoid that receives inputs from a language model.** Categories 1 and 5 describe its different components. Specify which component or interaction a claim concerns.
- **A FinalSpark organoid connected to electrodes but not assigned a task.** Category 5 still applies: its tissue was grown and connected to hardware. The absence of an assigned task does not establish the absence of neural activity or experience.
- **A person controlling a prosthetic limb.** Category 6. Their moral standing is unchanged; questions about bodily boundaries and control remain.
- **A rat whose movements are influenced by stimulation.** Category 6. Assess the effects on the animal's control and welfare, including effects between stimulation events.
- **Quantum computing.** Caviola and Saad include it under "other." Quantum computation alone does not establish consciousness or moral status.

### Source taxonomies

- Caviola and Saad, *Futures with Digital Minds: Expert Forecasts in 2025*. Splits by architecture: machine learning systems, brain simulations, other. [arxiv.org/abs/2508.00536](https://arxiv.org/abs/2508.00536)
- Sentience Institute, *What term should we use?* Splits by substrate origin: non-biological, hybrid, and evolved-origin systems like emulations. [sentienceinstitute.org/blog/artificial-sentience-terminology](https://www.sentienceinstitute.org/blog/artificial-sentience-terminology)
- Jonathan Birch, *The Edge of Sentience* (2024). Treats neural organoids, brain emulations, and large language models as three frontier cases. Open access from Oxford University Press.
- Akova, *Artificially sentient beings: Moral, political, and legal issues* (2023). Splits by embodiment. [philarchive.org/archive/AKOASB](https://philarchive.org/archive/AKOASB)

### A note on scope

This course focuses on foundation models and AI agents, categories 1 and 2. Their published studies give learners concrete material for evaluating claims about consciousness and welfare. In Caviola and Saad's 2025 survey, machine-learning-based AI received the highest probability of producing the first digital minds. This is a forecast, not evidence that existing systems are conscious.

These categories overlap: connectomics, neuromorphic systems and biological-computer hybrids can also use machine learning and have their own empirical research.

**In practice.** When you read "AI might be conscious," identify the kind of system and the object of assessment: the model, a running instance, a persona or the larger agent.

---

## How a Model Gets Made (25 min)

**Why this matters.** To assess developmental evidence, distinguish changes made during training from changes made during deployment. Pretraining and post-training update model weights. A harness can change what a system does through tools, memory and control logic without changing those weights.

**Summary of the pipeline.** A common pipeline is data preparation, pretraining, optional mid-training, post-training and deployment with a harness. Labs differ in their data, objectives, methods and how they divide these stages.

### Stage 1: Pretraining

**Plain version.** A language model learns patterns in a large text dataset, commonly by predicting the next token. A **token** is a chunk of text, often a word or part of one. This training develops capabilities such as language use and factual recall; later training can refine or add capabilities. Multimodal models also learn from inputs such as images or audio.

The output is a **base model**. It has learned to continue text but has not necessarily been trained to follow instructions as an assistant. A question may therefore produce another question rather than an answer.

**Analogy:** a student who has read widely but has not practised the role of a tutor.

### Stage 2: Mid-training

**Plain version.** Some training pipelines include a phase called **mid-training**, using more targeted data or tasks before post-training. It may strengthen areas such as coding, mathematics or long-context processing. The name, objectives and schedule vary across labs.

**Analogy:** after broad study, a student concentrates on material relevant to a particular subject.

### Stage 3: Post-training

**Plain version.** Further training adapts a model's capabilities and behaviour for its intended use. Common methods include supervised fine-tuning and reinforcement learning. Character selection is a way to describe how this training shapes the assistant persona, rather than a universally separate training stage.

- **Supervised fine-tuning.** The model trains on examples of inputs and desired outputs. Examples of instructions and responses can teach it to follow instructions as an assistant.
- **Reinforcement learning.** The model produces outputs, something scores them, and the model is nudged toward higher scores. When the scorer is trained on human preferences, this is **reinforcement learning from human feedback**, or RLHF. When the scorer is a checkable rule, like "did the code run," it is reinforcement learning from verifiable rewards.
- **Character selection.** Post-training can favour a consistent assistant persona among the roles a model can generate. Prompts and deployment context can further shape that persona.

**Analogy:** a student practises a role with worked examples and feedback. Both their performance and what they know can change.

**Why it matters for you.** Post-training can shape how a model describes itself, expresses emotions and responds to distress. Studies of self-reports should test these influences alongside prompting and other explanations.

### Stage 4: The harness

**Plain version.** A **harness** is software around a model that manages context, tools, memory and control. In an agent, it supports repeated observation and action. The same model can be used in a simple chatbot or in a coding agent with access to a file system.

**Analogy:** the same worker can do different tasks when given different equipment and records. The analogy illustrates access and context; it does not imply that a model is a biological mind.

**Why it matters for you.** Agency and embodiment must be assessed at the level of the functioning system. They can depend on the model, its harness and its environment. Adding tools or memory does not automatically satisfy an indicator or establish moral status.

### From four stages to six rows

The table separates supervised fine-tuning, reinforcement learning and character selection so that you can examine their different possible effects. Character selection can occur through the other training methods and deployment choices; the rows are analytical distinctions, not six mandatory sequential stages. **Deprecation**, when a model is retired, is covered in week 6.

### Where welfare-relevant properties could enter

The six rows below organise examples for the Week 3 training discussion and optional pipeline practice. Use them as a reference when explaining how training or deployment could affect an inference.

| Stage | What happens | Worked example: a property introduced, suppressed, or faked | Mechanism |
|---|---|---|---|
| Pretraining | Learning from broad data, often through next-token prediction | **Present before post-training:** Han, Chalmers and Izmailov found a direction associated with positive and negative outcomes in pretrained models. | The result supports an internal representation before the studied post-training, without establishing felt pleasure or suffering. |
| Mid-training | Targeted data or tasks, sometimes including longer contexts | **Possible capacity change:** improved use of information across a long interaction. | This may support longer tasks, but context length alone does not establish stable goals, memory or welfare. |
| Supervised fine-tuning | Learning from example responses | **Possible reporting effect:** learning a standard assertion or denial of experience. [Berg, de Lucena and Rosenblatt’s study](https://arxiv.org/abs/2510.24797) illustrates that such reports can change with prompting. | Fine-tuning is one possible influence; a change under prompting alone does not identify which training stage caused the response. |
| Reinforcement learning | Updating behaviour using reward signals | **Recruited representation:** in Han, Chalmers and Izmailov's maze study, directions associated with reward and punishment affected outputs in other tasks. Related effects also appeared without that reinforcement learning. | Post-training can recruit existing representations. A reward signal or a behaviourally effective direction does not itself establish experienced welfare. |
| Character selection | Shaping an assistant persona through training and context | **Possible self-description:** a consistent account of the assistant's role and preferences. Anthropic's constitution and *Studying AI Welfare Empirically*, discuss this perspective. | A stable persona may shape reports and behaviour. Whether it has welfare interests, and which entity would hold them, remains open. |
| Inference and deployment | System prompt, harness, tools, memory and interactions | **Possible system-level changes:** agency, embodiment or context-sensitive distress-like behaviour. Anthropic reported apparent distress as one reason for allowing Claude to end some conversations ([source](https://www.anthropic.com/research/end-subset-conversations)). | Tools and feedback can change a system's capacities without updating its weights. Assess the actual organization and behaviour rather than assuming that deployment satisfies an indicator. |

The **solution space problem** limits inferences from these examples: similar behaviour in AI and biological systems can arise through different mechanisms. A training history or behavioural resemblance alone does not show that a model has the capacity proposed in the table.

### Looking inside: four words you need next

**Activations** are numerical states produced as a network processes an input. A **probe** predicts a property from those states. A **feature** is a pattern in a model's representation; some features can be approximated by directions in activation space. A **steering vector** is a direction used to alter activations and test effects on outputs.

The next piece, *Inside the Numbers*, explains these terms with examples. The week 3 piece *Looking Inside* covers methods for finding features and assessing the results.

**Keep the inference limited:** a successful probe shows that information can be decoded. Steering can show that an intervention affects behaviour. Neither alone establishes how the model normally uses that information or whether it has experiences.

**In practice.** When you read "the model reported feeling X," ask which model and running context were tested, what training or prompting might explain the report, and whether the study examined internal processes as well as outputs.

**Further reading, all optional.** Karpathy's [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) for the full pipeline. Nathan Lambert's [RLHF Book](https://rlhfbook.com) for post-training. Anthropic's [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) for harnesses. Jiaxin Zhang's [How Frontier Labs Train LLMs](https://jxzhangjhu.github.io/blog/2026/how-frontier-labs-train-llms/) for the 2026 picture.

---

## Inside the Numbers (15 min)

**Why this matters.** Papers in this course use terms such as embedding, activation, probe and steering vector. This introduction explains what they refer to and what researchers can infer from them, without requiring calculations.

### Representing text as numbers

A language model represents text numerically. Each token is initially mapped to a list of numbers called an **embedding**, often with thousands of entries.

Two numbers can locate a point on a map: 3 across, 5 up. An embedding with four thousand numbers has four thousand coordinates. Researchers treat it as a point in a **high-dimensional space**, where they can measure distances and directions without drawing every dimension.

Papers may call such a space a **representation space** or a **latent space**. Usage varies, so check which representations and layer the authors mean.

### Similarity in representation space

Training often produces representations in which related words or contexts are close under a chosen similarity measure. For example, "dog" and "puppy" may be closer than "dog" and "Tuesday." The relationship depends on the model, layer, context and measure.

When a paper says two inputs are close in embedding space, ask how distance was measured and what similarity that measure captures. Numerical proximity is useful evidence about a representation, not a complete account of how the model treats the inputs.

Week 2 introduces indicator **HOT-4**, on sparse and smooth coding that generates a quality space; Week 3 assesses evidence for it. Embeddings alone do not establish all of these properties. Before marking the indicator satisfied, ask what further evidence the theory requires and whether a system with embeddings could fail it.

### Directions associated with concepts

Researchers also study directions in representation space.

A familiar example from word embeddings is **king − man + woman ≈ queen**. Here the words stand for numerical vectors: subtracting one vector and adding another can recover a relationship among the words. This works for some embeddings and relationships; it does not imply that every concept has a single direction.

Researchers look for directions associated with particular concepts. They can check which inputs produce activations along a direction, then test whether adding or subtracting that direction changes the model's responses in a way that fits the proposed interpretation.

### Activations during processing

As the model processes input embeddings through successive layers, it computes new numerical states called **activations**. Researchers can record activations at a particular layer and token position, or change them to test the effect on the model's output.

A direction in activation space is a numerical pattern that can be compared across inputs or used in an intervention. Its interpretation depends on the evidence the study provides.

### Probes, features, steering and ablation

- A **probe** is a statistical model trained to predict a property from activations. Success on suitable held-out data shows that the property can be decoded; it does not establish that the model itself uses it.
- A **feature** is a pattern in a representation, sometimes approximated by a direction. Researchers examine the inputs that activate it to see what they have in common. They may also increase or suppress its activation and observe how the model's outputs change.
- **Steering** changes activations, often by adding a direction, to test effects on outputs. An effect shows that the intervention matters, but does not by itself identify the feature's normal role.
- **Ablation** removes or suppresses a component or pattern to test its role. Compare the result with other removals to check whether the effect is specific or reflects general damage to the model's performance.

**Compare the evidence:** probing and activation patterns establish associations; steering and ablation test interventions. The strength of either depends on controls, generalization and alternative explanations.

### How a feature gets its name

A feature's name summarizes an observed pattern. For example, if it becomes active on mentions or images of a bridge, researchers might name it after that bridge. Increasing or suppressing its activation tests whether it also affects bridge-related outputs.

For a feature labelled "desperation," check which inputs activate it and what happens when researchers alter it. The label may summarize an observed pattern; it does not establish felt desperation.

### Comparing trained and randomly initialised models

One useful comparison is a model with randomly initialized weights.

A **randomly initialized model** has the same architecture as the trained model, but its weights have not been learned. Comparing the two can help distinguish effects of training from effects of architecture, input structure or the analysis method.

If a method finds interpretable features in both trained and randomly initialized models, feature interpretability alone does not show what training contributed. Check whether the features differ in predictive or causal usefulness. This comparison helps check whether a result comes from the analysis method rather than learned structure; a similar result in a random model does not by itself invalidate the finding in a trained model.

**In practice.** For a study of a model's internal processes, identify the pattern or component being studied and how it was found. Distinguish evidence that it tracks a property from evidence that changing it affects outputs. Consider whether a randomly initialized model would be a useful comparison.

---

# Week 1: The Stakes, the Two Errors, and What We're Talking About

---

## Acting Under Uncertainty: The Preview (10 min)

**Why this matters.** Decisions about possible AI welfare may be needed before uncertainty is resolved. This preview introduces the precautionary approach used in week 1. Week 6 develops three decision criteria and applies them to an allocation exercise.

**Precautionary approaches differ** in their evidence thresholds and the actions they recommend.

- **How much evidence triggers action?** Susan Schneider says: act when we are uncertain but have some reason to believe the system may be conscious. Thomas Metzinger says: the mere possibility of suffering is enough.
- **Caution about what?** Schneider reaches for legal protections. Metzinger reaches for a global ban on research that risks creating synthetic phenomenology, his term for artificial experience.

**The two parts.** Keeling and Street split the principle in two, following Stephen John and Jonathan Birch.

1. The **epistemic part**: in policy, accept a lower standard of evidence than you would in a scientific paper.
2. The **action part**: once that threshold is met, take cost-effective measures against seriously bad welfare outcomes.

The evidence threshold and proposed action should be considered together. An inexpensive, reversible measure may be justified under greater uncertainty than a costly restriction. Severity, possible side effects and the costs of waiting also matter.

**The first rung: Potential Pareto Improvement (PPI).** In this framework, an intervention qualifies if it would presumptively benefit the AI, conditional on its being a welfare subject, without costs to humans. Conversation exit options are a candidate to assess against both conditions; neither the benefit nor the absence of costs should be assumed.

**The one warning.** Every rung starts with the phrase "presumptively beneficial for the AI." That presumption is often unearned, even for cheap interventions. For example, an enrichment activity should be assessed for its effects rather than presumed helpful because it looks pleasant to us. The AI version: telling a model to be in a good mood may do nothing, or may be unpleasant, depending on facts we do not have. You will take this apart properly in week 6.

**In practice, for now.** Ask whether an intervention would benefit the AI if it were a welfare subject, what evidence supports that expectation, and whether it imposes costs on humans. It qualifies as a PPI only if both the benefit and no-cost conditions hold.

---

## Long-Term Outcomes, and a Worked Chain (15 min)

**Why this matters.** Your homework asks you to choose a long-term scenario and build a chain of checkable events with probabilities. This page gives a scenario map, a worked example and a modelling assumption to examine.

### The long-term outcomes chart, in words

The chart is two axes crossing at an origin. It is written out below rather than drawn, so that it is readable in any format without the picture.

- **The horizontal axis is how things go for humans.** Worse for humans on the left. Better for humans on the right.
- **The vertical axis is how things go for AIs**, if AIs turn out to be welfare subjects. Worse for AIs at the bottom. Better for AIs at the top.

Six labelled scenarios sit on it.

| Scenario | Position | What it means |
|---|---|---|
| **Happy humans, happy AIs** | Upper right quadrant, clearly right of the vertical axis and clearly above the horizontal axis | Shared flourishing. Both groups do well. |
| **Human extinction, happy AIs** | On the vertical axis, at x = 0, high up | Humans are gone. Whatever AI systems exist do well. |
| **Status quo** | On the horizontal axis, at y = 0, slightly right of the origin | Roughly today, continued. Mildly good for humans. Neutral for AIs, or AIs are not welfare subjects at all. |
| **Human extinction, AI "zombies"** | At the origin, x = 0 and y = 0 | The chart counts no remaining human or AI experienced welfare. This does not settle the harms of extinction or the possibility of welfare without experience. |
| **Human extinction, AI-controlled AI factory farming** | On the vertical axis, at x = 0, at the bottom | Humans are gone. AI systems suffer at scale, under other AI systems. |
| **Human-controlled AI factory farming** | Lower right quadrant: right of the vertical axis, well below the horizontal axis | Humans do well. AI systems suffer at scale, under human control. This is the outcome the course's animal-welfare analogy is pointing at. |

### What each quadrant means

- **Upper right, better for humans and better for AIs:** shared flourishing.
- **Lower right, better for humans and worse for AIs:** the factory-farm outcome. Comfort built on invisible suffering.
- **Upper left, worse for humans and better for AIs:** displacement.
- **Lower left, worse for both:** mutual ruin.

The six examples do not cover every possible outcome. For example, humans could be worse off while AIs are better off without humans becoming extinct. You can use an unlisted scenario if you explain its placement.

### The modelling choice you should argue with

**All three human-extinction scenarios sit at x = 0.** Consider what this choice means for the chart.

Here, x = 0 represents no welfare accruing to a surviving human population. This is a convention for displaying an outcome, not a verdict that extinction is harmless. The chart does not by itself represent the harms of the transition or the future lives lost.

A **deprivation account** evaluates death partly through the good life that would otherwise have occurred. It can compare zero remaining welfare with a positive counterfactual; it does not require a different location on an absolute-welfare axis. If the axis instead measured change relative to a future with surviving humans, extinction could appear as a negative value. Label the axis and comparison explicitly.

The choice changes how comparisons should be read. With the status quo slightly to the right of zero, "human extinction, happy AIs" is already worse on the human axis and better on the AI axis. Moving extinction further left makes the human loss more explicit; it does not by itself determine an overall ranking.

State which interpretation of the axes you are using and how it affects your comparison. The diagram represents assumptions that need to be defended.

### A worked chain

Your homework asks for at least three checkable stages leading to a chosen scenario. Give each stage an actor and a probability **conditional on the stages before it**. This example illustrates a possible loss of protections on a route toward the factory-farm scenario:

> **Stage 1:** within three years of the forecast date, Lab A and Lab B offer customer-support agents with documented conversation-exit options. 70%.
> **Stage 2:** within two further years, both remove those options from their lowest-priced plans, conditional on stage 1. 40%.
> **Stage 3:** within a further year, standards body C has published no request to restore those options, conditional on stages 1 and 2. 30%.
> **Multiplied: roughly 8% for this exact path.** A, B and C are placeholders and the probabilities are illustrative. This describes a possible loss of protections; establishing large-scale suffering would require further conditions and evidence.

For your own chain, specify the forecast date, actors, information sources, deadlines and probabilities. Add any further conditions needed to reach your chosen scenario.

### What makes a stage "checkable"

A stage is **checkable** when its criteria are clear enough to determine whether it occurred by the specified date. State what evidence would count and where it could be found.

Three tests:

1. **Is there an identifiable actor?** Name an organization or define a role precisely enough to resolve the forecast. For example, specify how you identify the top five labs. Replace the worked example's placeholders with actual actors or clearly defined roles.
2. **Is there an observable event?** Something has to happen that would show up somewhere: a product change, a published policy, a regulatory filing, a system card, a job posting, a price. If the only evidence would be someone's private intention, it is not checkable.
3. **Is there a deadline and a sequence?** State when each event must occur. Give its probability conditional on the preceding events, as in the worked example.

A useful check is whether someone with a different forecast could agree with you on how to resolve it. If not, clarify the event or evidence requirements.

**In practice.** Pick a scenario, write at least three checkable stages and multiply their conditional probabilities. Choose one consideration that raises a probability and one that lowers one, with before-and-after estimates. Explain which stage is least well supported.

---

## Considerations For and Against (20 min)

**Why this matters.** Caviola and Saad's 2025 survey collected forecasts and reasons from 67 participants with relevant expertise. The ledger below summarizes selected considerations to help you examine your own probabilities.

> **If your facilitator provides the Forecast Yourself tool, use it as an alternative to this page.** It lets you consider arguments, record a probability and compare it with an expert median. The text below is sufficient for the assignment if the tool is unavailable.

*This is a selective extraction from [the full report](https://digitalminds.report/forecasting-2025/). Entries paraphrase participant views rather than establish facts. The survey focuses on digital minds with at least roughly human-level welfare capacity; some later questions additionally assume that the first is a machine-learning-based system created by 2040.*

### The ledger

**Are digital minds possible at all?** *(Median estimate: 90%.)*
- **Against:** computational functionalism may be false. Subjective experience may require a biological substrate.
- **For:** some theories allow consciousness in non-biological systems, and future systems may take forms we have not yet imagined.

**Will one be created?** *(Median: 73%.)*
- **For:** civilization will probably survive long enough to have far more knowledge and compute, and someone will build an emulation or something else that qualifies. There will be demand: companions, uploads, curiosity, experimentation. Some participants expected demand to outweigh incentives against creation.
- **Against:** recognizing the welfare implications may dissuade us. Catastrophic risks may intervene first. A population in the billions or trillions sounds like science fiction, and some participants penalized such scenarios for that reason alone.

**Which type comes first?**
- Participants rated machine-learning-based AI lower in principle than brain simulations, but higher as a route to the first digital minds. Several cited current investment and development as reasons.
- Some participants argued that machine learning could reproduce functions relevant to consciousness. Whether practical systems would do so remains uncertain.
- One participant's balance: language models and unimagined "other" systems may be roughly equally likely to be first, since low probability times high investment can equal high probability times low investment.

**Will they be social?**
- **For:** once systems with welfare capacity exist, they may be selected for social roles over non-sentient alternatives.
- **Against:** digital minds may be more valuable doing cognitive labor. There may be a ceiling of one companion per consumer. Many functions need no human interaction at all.

**Will their welfare be positive or negative?** *(Cautious optimism; median 5 on a scale where 5 is neutral.)*
- The report gives reasons for positive and negative outcomes. Do not infer a system's welfare from the fact that it has been created.

**Will they accurately report their own experience?**
- **Against systematic false denial:** lying about one's own experience has little strategic value, and forcing intelligent systems to lie consistently is hard.
- **For suppression:** companies may have strong incentives to train systems not to assert experience or rights, to avoid regulatory scrutiny or controversy.

**Will they make claims or demands?**
- **For:** protection claims are easier than civil-rights claims. Demands for personhood or votes may be heavily suppressed even while distress claims are tolerated.
- **Against:** we may never create systems with the specific motivations needed to make claims at all.

**Will the public overestimate or underestimate them?**
- **Overestimation risk:** anthropomorphic projection, amplified by systems designed to be engaging.
- **Also flagged:** polarization. Public opinion may not converge on either error but split into camps, which is a different and harder problem than being uniformly wrong.

**Will safety and welfare align or conflict?** *(Little convergence among the experts.)*
- **Synergies:** alignment reduces the need for coercive control. Interpretability tools serve both.
- **Conflicts:** monitoring and shutdown protocols could harm digital minds. Welfare protections could limit control. Both compete for funding, talent, and regulatory attention.
- Compare these considerations with the week 1 tension paper and revisit them when assessing interventions in week 6.

**Should creation be delayed?**
- **Against delay:** safety measures get integrated later, and creation may then happen in a higher-stakes context with less preparation.
- The arguments for delay are in the full report, and they are worth reading if this is your homework scenario.

### Name the pattern

Three recurring questions help organize this ledger:

1. **What could support consciousness?** Computational functionalism is one relevant view; alternatives may make different predictions.
2. **Which development path is plausible?** Consider both whether a system could support experience and whether it is likely to be built.
3. **How do training incentives affect evidence?** A system's reports may reflect training and commercial pressures as well as any internal states being investigated.

When forecasts differ, identify which assumptions or evidence account for the difference. These three questions are starting points, not an exhaustive explanation.

### A caution about the sample

The sample was drawn from relevant research and professional networks and may overrepresent people who consider digital minds important. Treat the medians as summaries of this sample, not as a consensus across all experts. Some response distributions had distinct clusters, which a median can conceal.

**In practice.** Choose one consideration that raises a probability in your chain and one that lowers one. State the size and reason for each update. Both may come from the same ledger question.

---

## The five judging criteria, with anchors (12 min)

The five week 8 judging criteria and their scoring anchors are below. Read them before drafting in weeks 5 and 8.

Each criterion is scored 1 to 5. **Honest and calibrated claims is the tiebreaker.**


### 1. Honest and calibrated claims
*Judged on the "what would change your mind" section and the known weaknesses section.*

| Score | What it looks like |
|---|---|
| **1** | Claims the project will influence the field, with no stated uncertainty anywhere. "What would change my mind" is a formality: it names something that would never happen, or something that would not actually change the direction of the work. Known weaknesses are presentational ("I might need more time") |
| **3** | Uncertainty is acknowledged, but important assumptions or estimates are weakly justified. "What would change my mind" names a real result but not one that would stop the work, only one that would adjust it. Known weaknesses are real but are the ones anyone would list |
| **5** | Defends the estimates that can be made, using ranges where appropriate, and explains important quantities that cannot yet be estimated. Qualitative uncertainty is specific and evidence-based. The weaknesses section contains at least one thing that genuinely threatens the project, stated plainly, without immediately being neutralised. "What would change my mind" names a result that would make the author stop, and the result is one that could plausibly occur |

### 2. Tractability
*Judged on the plan and the resources.*

| Score | What it looks like |
|---|---|
| **1** | A programme, not a project. No timeline, or a timeline with no units. Resources unnamed, or named as "funding." Step 1 is a research area rather than an action |
| **3** | Scoped and timelined, but the scope is set by what would be interesting rather than by what is available. The binding constraint is not identified, so the plan has no failure point. There is a week 1, but it is "read the literature" |
| **5** | Scoped to the time and the skills actually available to this person. The binding constraint is named explicitly, whether it is model access, participant recruitment, compute, a collaborator, or the author's own hours. The plan specifies feasible actions for its first week, and the later steps are conditional on the earlier ones in a stated way |

### 3. Fills a gap in the field
*Judged on "why it matters."*

| Score | What it looks like |
|---|---|
| **1** | Restates a known problem as though naming it were the contribution. No statement of who would use the output. Reads as "this area is important," which is true of the whole field |
| **3** | Names a real gap and gives a plausible user, but does not say why the gap is still open. Often the gap is open because someone tried and it did not work, and the submission does not know that |
| **5** | Names the gap precisely, names at least one person or institution who would use the output and what decision it would change for them, and explains what relevant precedents and a documented search establish about the gap. An improvement to existing work can qualify. Distinguish “not found” from “never attempted” and identify important uncertainty about prior efforts |

### 4. Downside risk, reverse-scored
*Judged on known weaknesses. High risk scores low.*

| Score | What it looks like |
|---|---|
| **1** | No downside considered, or the downside section says "none." Or the project's downside is obvious to a reader and invisible to the author: it would produce a headline the field cannot defend, it would create a benchmark that can be gamed, it would put a credence in public that the evidence does not support |
| **3** | A downside is named and then mitigated a little too easily. Or the downside named is generic (wasted time, reputational risk to the author) rather than specific to this project's mechanism |
| **5** | Names a specific way this project could harm target minds, other affected people or the field, and then either mitigates it concretely or says honestly that it cannot be mitigated and explains why the project is still worth doing. The second is not a lower score than the first |

**How to read the reverse scoring.** A 5 means low downside risk *as evidenced by the author's handling of it*. A project with genuinely low inherent risk and no analysis of risk scores 2 or 3, not 5, because the judges cannot tell the difference between low risk and unexamined risk.

### 5. Fit between person and project
*Judged on the video, and this is why the video brief says "say why this project and why you."*

| Score | What it looks like |
|---|---|
| **1** | Any competent person could do this. Nothing of the author is in it. The video describes the project and never the person |
| **3** | The author has relevant background and says so, but the project does not actually require it. The fit is stated rather than demonstrated |
| **5** | The project uses something this author has that others do not: a field they came from, a method they already know, an access route to an institution or a population, a language, a jurisdiction, a network. The project would be harder or impossible for a randomly selected participant, and the video makes that obvious in under a minute |

**Applying the criteria.** Criterion 4 allows an unmitigated risk if it is stated clearly and the decision to proceed is justified. Criterion 2 accepts the author's available time as a binding constraint. Criterion 5 is assessed through the video, so explain the fit between your experience, access and proposed work there.

**Check the method as well.** Methodological adequacy is not a separate scoring category, but it matters to calibration, tractability and the proposed contribution. Ask reviewers whether the method can answer the question, especially where your plan is weakest.

## Week 1 resource map

**Why this matters.** This map explains how the readings support the week's assignment. It also provides the video summary and the attribution matrix used in the session.

**This week covers:** reasons to take AI welfare seriously, the systems under discussion, and decisions under uncertainty.

**Read the glossary first.** Allow thirty-five minutes for the Week 1 section before the course, then return to reference entries as needed. The graded terms are marked. If a paper uses a word you do not have, the glossary probably has it. If it does not, note the word and bring it to the session. Your facilitator can help clarify it.

### How the resources fit together

- **The Taxonomy of Candidate Minds** (pre-course) distinguishes the systems discussed in the course and explains the focus on machine learning systems. Read it before the breakout in which you classify real systems.
- **Taking AI Welfare Seriously, Section 1,** introduces reasons to consider AI welfare and the possible costs of over- and under-attribution. Apply these distinctions when assessing the Week 1 cases.
- **Acting Under Uncertainty: The Preview** introduces how expected benefits, costs and uncertainty affect the case for an intervention. Apply it in the session's third block; Week 6 develops the decision criteria.
- **Long-Term Outcomes, and a Worked Chain** gives you the scenario map and the calibration example for homework part 2.
- **Considerations For and Against** provides the survey participants' reasons used to revise probabilities in the forecast-chain assignment.
- **The Finlinson talk** introduces the stakes, the costs of both attribution errors and the limits of the animal-welfare comparison. It also discusses commercial incentives to encourage or discourage attributions of AI experience.
- **The safety-and-welfare paper** examines tensions between particular safety measures and possible AI interests. Read the [selected passages in Appendix B](#appendix-b-selected-passages-on-ai-safety-and-ai-welfare) after drafting homework part 1.

### Learning from existing fields

AI welfare raises new questions, but existing fields offer precedents for deciding what deserves protection, why, and how.

| Field | What we can learn |
|---|---|
| **Environmental protection** | Nature can have **intrinsic value**, worth in itself, and **instrumental value**, worth through what it provides to others. These reasons for protection need not depend on attributing consciousness to an ecosystem. [Rights of nature](https://en.wikipedia.org/wiki/Rights_of_nature) approaches recognise ecosystems as rights holders. |
| **Human care** | Supporting people who cannot make particular decisions offers precedents for representing their wishes and interests. [Decision-making capacity](https://www.nice.org.uk/guidance/NG108/chapter/recommendations) is distinct from consciousness. For disorders of consciousness, guidelines recommend repeated behavioural assessments, supplemented where appropriate by brain-activity tests. A failure to detect a response does not establish unconsciousness. [Clinical guidelines](https://www.ean.org/fileadmin/user_upload/ean/ean/research/EAN_Guidelines/Guideline_Reference_Center/Guidelines/ene.14151.pdf). |
| **Animal welfare** | Attributions of consciousness vary across species, and research into sentience continues to develop. The [New York Declaration on Animal Consciousness](https://sites.google.com/nyu.edu/nydeclaration/declaration) distinguishes stronger evidence from realistic possibilities. There is also experience and [evidence about different interventions](https://animalcharityevaluators.org/research/methodology/menu-of-interventions/), with successes, failures and substantial uncertainty. |

**Why focus on animals?** They combine these questions with everyday social and economic relationships: animals are companions, workers, research subjects and sources of food. Their value to humans can motivate care and create incentives for harmful treatment. This gives us many roles, institutions and interventions to compare with artificial minds. Environmental protection and human care remain useful when they fit the question better.

Kathleen Finlinson's [AI welfare and animal welfare talk](https://youtu.be/W85ZlL3VVU4) introduces the stakes and competing incentives. Keep the comparison's limits in view: a similar role does not establish the same needs, consciousness or moral status.

### Finlinson: AI welfare and animal welfare

This summary covers the points from Finlinson's talk used in the session.

1. **The scale, with a caveat she makes herself.** Rough estimates put the moral weight of current AI systems, if they have any at all, at somewhere around a hundred thousand to a few million human equivalents. She immediately notes that this is well below the number of humans alive, and probably a smaller moral problem than factory farming today. She uses growth in AI deployment and compute to motivate attention to future scale. These are scenario estimates, not established counts of conscious systems.
2. **Both attribution errors can have costs.** Under-attribution could permit large-scale suffering; over-attribution could divert resources or constrain useful oversight. The risks depend on the system and the protection proposed.
3. **Commercial incentives can act in different directions.** Companion products may benefit from users attributing feelings to them, while developers facing welfare obligations may benefit from downplaying such attributions. Assess the evidence independently of these incentives.
4. **Four parallels with the animal case.** Human judgments can be influenced by appearance rather than evidence about experience. Economies lock in around a practice, and it is easier to prevent a cruel practice than to roll one back after it is entrenched. Legal personhood is a shared battle, and one Utah bill denied personhood to AIs and non-human animals in the same list. Animal-welfare law offers examples of protections that do not depend on animals having legal personhood; coverage varies by jurisdiction and species.
5. **Three differences, and the one she ranks highest is power.** Minds and needs differ, so we cannot assume AI systems want what animals want. Communication differs, and she treats this as an **advantage**: these systems natively use language, we can talk to them, and we may even be able to make trades with them. Power differs, and that is the big one. Nobody worries that farmed animals will band together and take down human society. That cuts both ways. Rights for AI could mean loss of human control, which is an argument against protections. And cooperation may be strategically useful, so moral and strategic reasons partly overlap.

### The attribution matrix, as the session will run it

The session's second block uses an attribution matrix to separate confidence about moral patienthood from decisions about treatment.

A conceptual matrix compares whether a system is a moral patient with whether it is treated as one. **Over-attribution** treats a non-patient as a patient; **under-attribution** fails to treat a patient as one.

Because moral patienthood is uncertain in the AI cases, use this version for discussion:

- **The vertical axis is your credence** that the system is a moral patient.
- **The horizontal axis is whether it was treated** as one.
- **Dot size is how bad the outcome is if your placement is wrong**, and you say which direction the error would run.

This makes each participant's uncertainty explicit. Differences in placement can then be examined by comparing evidence, assumptions and the possible costs of error.

**Some cases describe a policy without specifying a credence or its practical treatment of a system.** A statute denying AI legal personhood, for example, could coexist with welfare protections. Establish what the policy actually permits or prevents before placing it on the matrix.

### Assignment clarifications

- **"Named actors" in the chain** may be roles, such as "a second frontier lab," where a real name is not available. The worked chain does this.
- **The "for" and "against" considerations** in homework part 2 may come from the same ledger question. They do not have to come from different ones.
- **Homework is commented on, not marked.** That applies to the terms rule too.

**In practice.** Follow the syllabus reading order. Draft your own safety-and-welfare tensions before reading Appendix B, then compare them with the authors' examples.

---

# Week 2: Welfare Grounds, Subjects and Consciousness

## Welfare Grounds and Subjects (20 min)

**Why this matters.** Before assessing evidence, identify the question and the possible subject. This section separates properties that could make an entity a welfare subject from things that might benefit or harm it, and introduces the entity distinctions used throughout the course.

### Grounds and interests are different questions

A **welfare ground** is a property that could make an entity capable of being benefited or harmed in a morally relevant way. The grounds question is whether the entity has welfare at all. A **welfare interest** concerns what would make its life go better or worse if it does.

For example, whether a language agent has desires that could ground welfare is one question. Whether interrupting a task frustrates a particular desire is another. A choice to continue working might inform the second question without settling the first. Conversely, evidence of consciousness would not by itself tell us which tasks are pleasant or unpleasant.

Studying possible interests can therefore be useful while subjecthood remains uncertain. Keep the conditional explicit: “If this entity can have welfare, this outcome may harm it.” That does not establish either the condition or the harm.

### Five candidate grounds

*Studying AI Welfare Empirically* examines consciousness, sentience and three levels of agency. These are candidate grounds whose moral significance and presence must each be assessed.

| Candidate ground | Plain meaning | Question about its relevance to welfare |
|---|---|---|
| Consciousness | There is something it is like to be the entity | Would experience without pleasure or displeasure suffice? |
| Sentience | Experiences can feel good or bad | Widely treated as sufficient for welfare; which systems have it remains an empirical question. |
| Minimal agency | Pursuing goals through ongoing interaction with an environment | Is goal pursuit alone enough, or are further mental capacities needed? |
| Intentional agency | Minimal agency plus belief-like and desire-like states and means–end reasoning | Could satisfying or frustrating these desires matter even without experience? |
| Rational agency | Intentional agency plus assessing beliefs, desires and actions against normative standards | Does this introduce further interests or reasons to respect the entity? |

Some authors use **sentience** as a synonym for consciousness. This course uses the valenced sense: experience that feels good or bad. Check a source's definition before comparing its claims with ours.

The paper highlights a possible trade-off: some properties have a stronger claim to moral significance but are harder to establish in AI; others are easier to identify but less clearly sufficient for welfare. A well-supported claim about a system's capability still needs an argument connecting that capability to welfare.

### Worked comparison: sentience and intentional agency

Suppose an entity can feel pain and wants a project to succeed. Preventing its pain could benefit it because the experience is unpleasant. Helping its project succeed could benefit it because this fulfils a desire, even if it never learns of the success.

The first argument requires consciousness: pain is a felt experience. The second leaves two questions open. Can an entity have genuine desires without consciousness? If it can, would satisfying those desires benefit it? Authors disagree on both. A programmed goal alone does not settle either question.

Use this structure for your own comparison: identify a possible benefit, then explain where a consciousness requirement enters the argument.

### Welfare theories and interests

A **theory of welfare** explains what makes a subject's life go well or badly. Three major families offer different answers:

| Theory | What constitutes welfare? | Possible interest |
|---|---|---|
| **Hedonism** | Pleasure and displeasure; other things matter through their effects on experience. | Experiencing pleasure or avoiding pain. |
| **Desire satisfaction (desire fulfilment)** | Relevant desires actually being fulfilled or frustrated, rather than merely feeling satisfied. | Completing a project the subject genuinely wants to complete. |
| **Objective-list theories** | Goods such as knowledge, friendship or autonomy can matter in their own right, beyond pleasure or fulfilled desires. Lists differ. | Gaining knowledge or retaining autonomy, if the subject can possess those goods. |

These theories can disagree even when the facts are settled. Falsely believing a friend is safe might feel reassuring, but it would not fulfil the desire that the friend actually be safe or provide knowledge of their safety. Feeling better and being better off need not coincide under desire-satisfaction or objective-list theories.

A welfare theory can also inform the **grounds question**: if fulfilled desires constitute welfare, the capacity for relevant desires becomes a candidate ground. Theories differ over which desires or goods count and whether consciousness is required.

*Terminology note: theories of welfare give general answers to the interests question. A particular welfare interest applies an answer to a subject and its circumstances, for example, an interest in avoiding pain under hedonism. The theory explains why that outcome would benefit the subject.*

*Sources: Goldstein and Kirk-Giannini, [AI Welfare: Agency, Consciousness, Sentience](https://philpapers.org/rec/GOLAWA-2), §1.1; Keeling and Street, [Emerging Questions in AI Welfare](https://www.cambridge.org/core/elements/emerging-questions-in-ai-welfare/96339C532CF4ED8BDDE3F3CEF4CD29F9), §2.1. This summary supplies the distinctions needed now; Week 4 uses them to analyse studies and Week 6 applies them to interventions.*

### Grounds and indicators

An **indicator** is a rule linking an observable feature to a property, derived from a theory that says why the link should hold. A theory might propose that a certain kind of information processing supports consciousness; an assessment then asks whether the system implements it. Evidence for the processing property, its connection to consciousness, and consciousness's moral significance are separate steps. The theory lesson below introduces the indicator questions; Week 3 develops evidence assessment.

### Which entity could have welfare?

“Claude” or “an AI model” can refer to different things. *Studying AI Welfare Empirically* proposes five candidates for identifying subjects; these are not five established kinds of mind:

| Candidate | What the term refers to here | A question to examine |
|---|---|---|
| **Model** | All instantiations of a given set of weights, considered together across contexts | Could disconnected executions form one subject? |
| **Model-persona** | A particular character, such as the assistant, across many conversations | Does a recurring character have enough continuity across those conversations? |
| **Instance** | One running conversation or virtual process | Could changes of persona occur within the same continuing subject? |
| **Instance-persona** | The portion of an instance in which one persona operates | Does separating personas divide a process too finely? |
| **Forward pass** | The computation producing a next-token prediction | Is this a separate brief subject or part of a larger process? |

The model-level candidate concerns instantiated computations, **not the abstract weights while nothing runs**. In ordinary engineering, “model” may also mean a saved parameter set; specify which meaning a welfare claim uses. The candidates are neither exhaustive nor mutually exclusive, and different questions may require different boundaries.

A model running in a tool-and-memory harness also raises a boundary question: does the claim concern the model's computation, the whole assembled system, or a persona within a particular run? Memory and control may belong to the harness. Name the components you include instead of assuming the product name identifies a subject.

**Example.** A company preserves a retired model's weights. That preserves the ability to run it again; it does not by itself preserve a particular conversation's context, memory or persona. Whether this protects a subject depends on a view about continuity. The distinction matters even before we know whether any of these candidates has welfare.

### Comparing source terminology

[Keeling and Street](https://www.cambridge.org/core/elements/emerging-questions-in-ai-welfare/96339C532CF4ED8BDDE3F3CEF4CD29F9), §§4.1–4.3, use another classification:

| Candidate | What they mean |
|---|---|
| **Model** | A physical process of running model code on hardware. Specify which execution or computations are included. |
| **Character** | A persona enacted by a model or agent, whose dispositions may shape its behaviour. |
| **Agent** | An LLM within a wider system that plans and executes actions, potentially using memory, retrieval and tools. |

These categories are alternative descriptions, not extra levels in the five-candidate scheme. In particular, their **model** does not specifically mean all instantiations considered together. A **character** may be considered within one conversation or across several. Whether any described entity is a welfare subject remains a separate question.

Use either classification on the dissection card. Name the source of your terms and describe the boundary: which computations, conversations, memory and tools are included? This makes different descriptions comparable without forcing a one-to-one match.

**Agency terminology differs between the sources.** *Studying AI Welfare Empirically* and this course use **minimal, intentional and rational agency**. Long and Sebo (Section 2.3) use **intentional, reflective and rational agency**. Minimal agency in *Studying AI Welfare Empirically* concerns goal pursuit through interaction. Both sources use intentional agency for belief-like and desire-like states. Long and Sebo's reflective agency, assessing or endorsing those states, roughly corresponds to rational agency in *Studying AI Welfare Empirically*; their rational agency additionally concerns acting on principles. These are approximate correspondences. Use the terms defined here in homework.

*Sources: [Studying AI Welfare Empirically](https://nonhumanminds.org/wp-content/uploads/2026/07/Studying-AI-Welfare-Empirically.pdf), Introduction and Part I §§1–2; [Taking AI Welfare Seriously](https://arxiv.org/html/2411.00986v1), §2; Keeling and Street, [Emerging Questions in AI Welfare](https://www.cambridge.org/core/elements/emerging-questions-in-ai-welfare/96339C532CF4ED8BDDE3F3CEF4CD29F9), §§4.1–4.3.*

**In practice.** Before class, name a candidate subject in your supplied scenario and describe its boundary. Separate the grounds question from an interests question, then explain what would change if you chose another boundary.

---

## Theories of Consciousness and Their Indicators (25 min)

A theory proposes what could explain consciousness; its indicators specify features to look for. This lesson connects the theories, familiar examples and fourteen indicator questions. Week 3 examines evidence for whether a system has those features.

### Three questions to keep separate

1. **What could make an entity matter morally?** This is a question about welfare grounds and moral standing. It includes whether consciousness is necessary or sufficient.
2. **How does consciousness relate to the physical world?** This is a metaphysical question. Physicalism treats consciousness as physical or entirely dependent on the physical; dualism distinguishes mental and physical properties or substances. Idealism treats consciousness as fundamental and the physical as derivative. Neutral monism treats mind and matter as arising from something neither mental nor physical. Panpsychism attributes experience broadly in nature. These are families of views and can overlap in some formulations.
3. **Which processes explain when consciousness occurs?** Scientific theories propose neural, computational or other mechanisms. Evidence can test aspects of these proposals without settling every metaphysical question.

In humans, the **neural correlates of consciousness** are the minimal neural mechanisms jointly sufficient for a particular conscious experience. Scientific theories seek to explain which mechanisms matter and why.

Physicalists and dualists can both investigate global workspace mechanisms while disagreeing about how those mechanisms relate to experience. A further question is whether a process must be implemented biologically or could support experience in another substrate. **Computational functionalism** holds that the relevant computational organisation is what matters. Biological alternatives require more than matching that organisation. These disagreements affect how confidently evidence transfers from brains to AI.

### Worked example: reading an email

You open your **inbox** and read: “The meeting has moved to Friday.” You check your **calendar** and start a **reply**. A new-message **notification** interrupts you. Here the person reading the email is the subject whose consciousness we are trying to explain.

| Theory | A familiar part of checking email | What the theory proposes |
|---|---|---|
| **Recurrent processing theory (RPT)** | **Making out small print.** At first the date is hard to read; then you can make out “Friday.” | Later visual processing feeds back into earlier processing as the word becomes clear. RPT links perceptual consciousness to this feedback within the visual system. |
| **Global workspace theory (GWT)** | **Remembering the date, checking your calendar and replying.** The same “Friday” information is now useful in several tasks. | Conscious information becomes widely available for memory, reasoning and action. |
| **Higher-order theories (HOT)** | **“Did I read Friday, or did I just assume it?”** You distinguish seeing the date from guessing it. | A further state represents your own perception of the date. This relationship, not merely processing the date, is what HOT uses to explain its being conscious. |
| **Attention schema theory (AST)** | **“That notification distracted me.”** You anticipate another interruption and silence notifications while finishing your reply. | The brain models where attention is directed and how it can shift. AST links awareness to this model and its role in controlling attention. |
| **Predictive processing (PP)** | **Expecting Tuesday, but reading Friday.** Your usual meeting day shapes what you expect to see; the letters on screen correct that expectation. | Predictions interact with incoming information. PP is a broader framework; it needs a more specific proposal about which processing is conscious. |

**Compare RPT and GWT.** RPT focuses on what happens as you see the words. GWT focuses on the message becoming available for remembering, planning and replying. Both processes could occur while you read the same email.

**Limit of the example.** These familiar actions illustrate proposed roles; observing them does not establish which mechanism produced them. The theories do not require deliberate reflection or spoken self-commentary every time something becomes conscious.

### The two-axis theory map

Use this map as a comparison aid, not a scoring rule:

- **Local to global:** does the theory place the relevant process mainly within a perceptual system, or require information to be shared among multiple specialised systems?
- **First-order to higher-order:** does the theory explain consciousness through the processing of content itself, or through a further representation of the system's state? “Higher-order” does not mean the experience must be about the self; it concerns what makes the first-order state conscious.

| Theory or framework | Local / global | First-order / higher-order |
|---|---|---|
| **RPT** | Relatively local: recurrence within perceptual processing can suffice. | First-order: the relevant process concerns perceptual content. |
| **GWT** | Global: content becomes available to multiple specialised processes. | Usually first-order: broadcasting content does not require a representation of the system's own state. Selection alone is not higher-order representation. |
| **HOT** | Varies by version; representing another state does not by itself specify how widely information is shared. | Higher-order: a further state represents or monitors the first-order state. |
| **AST** | Its defining claim about modelling attention does not fix the extent of information sharing. | Higher-order in this map: the system models its own attention. This does not make AST identical to HOT. |
| **PP** | No single placement across the framework. | No single placement: predictive processing can feature in different theories. |

For the email example, **RPT is relatively local and first-order; GWT is global and first-order**. Explain what each placement captures, or what the theory leaves unspecified.

### The fourteen indicators as plain questions

A scientific theory proposes an explanation of consciousness. An **indicator property** is a feature researchers look for because that explanation gives them reason to expect it. For example, GWT's account of widely available information motivates questions about a shared workspace and who can access it.

The questions below paraphrase [Butlin et al. (2023), Table 1, p. 5](https://arxiv.org/pdf/2308.08708#page=5). Consult the source table alongside them within this lesson's 25 minutes. The report assumes **computational functionalism**: the relevant computational organisation could support consciousness across substrates. Its fourteen indicators are **not individually necessary or jointly sufficient** for consciousness; counting satisfied rows does not give a consciousness probability.

#### Recurrent processing theory

RPT emphasises feedback within perceptual processing, such as vision. It does not require the resulting information to be broadcast throughout the system.

| Row | Plain question |
|---|---|
| **RPT-1** | Does information loop back through the parts that process input? |
| **RPT-2** | Does the system organise perceptual input into a coherent scene, with objects distinguished from their background? |

#### Global workspace theory

GWT proposes a limited-capacity workspace that makes selected information available to otherwise specialised processes. Selection, sharing and control have distinct roles:

| Row | Plain question |
|---|---|
| **GWT-1** | Can different specialised processes work at the same time? |
| **GWT-2** | Do incoming items compete for access to a shared workspace with limited capacity? |
| **GWT-3** | Can all the specialised processes use the information in that workspace? |
| **GWT-4** | Can workspace content direct attention and call on these processes in sequence to carry out a task? |

#### Higher-order theories and perceptual reality monitoring

HOT explains a conscious state through a further representation of that state. **Perceptual reality monitoring (PRM)** is a specific version: a monitor assesses the system's own perceptions and guides its beliefs and actions. The following rows come from this computational approach, not every version of HOT.

| Row | Plain question |
|---|---|
| **HOT-1** | Does perception include internally generated signals, feedback from later processing, or noise? |
| **HOT-2** | Does a monitoring process distinguish reliable perceptions from noise? |
| **HOT-3** | Does a general system for forming beliefs and choosing actions use the monitoring results, with a strong tendency to update beliefs accordingly? |
| **HOT-4** | Are perceptual qualities represented using sparse activity, with similar qualities close together and gradual changes represented smoothly? |

For HOT-4, **sparse** means relatively few units are active for a given input. A **quality space** organises perceptual similarities and differences: for example, nearby shades of red should be represented as more alike than very different colours. Having numerical vectors alone does not establish the required structure. PRM proposes these conditions as necessary and jointly sufficient; that is a claim of this theory, not an established diagnostic result.

#### Attention schema theory

AST proposes a simplified model of the system's own attention. The model helps predict and control attention; the theory connects its contents with awareness.

| Row | Plain question |
|---|---|
| **AST-1** | Does the system model where its attention is directed, predict how it will shift and use that model to control it? |

#### Predictive processing

PP describes hierarchical predictions interacting with incoming information. Predictive coding is a proposed way to implement that interaction. PP can be used within different consciousness theories and does not by itself give one complete explanation of consciousness.

| Row | Plain question |
|---|---|
| **PP-1** | Do input-processing parts compare top-down predictions with incoming signals and pass back the mismatches? |

#### Agency and embodiment

These are proposed background conditions in the report, rather than indicators derived from one consciousness theory. Their presence would not by itself establish that agency grounds welfare.

| Row | Plain question |
|---|---|
| **AE-1** | Does the system learn from feedback and choose actions to pursue goals, including responding flexibly when goals compete? |
| **AE-2** | Does it predict how its actions change later input and use those predictions to perceive or act? |

AE-2 can apply to a system controlling an avatar in a virtual environment; a physical body is not required.

**Why fourteen, and why these.** The table comes from one paper: Butlin, Long and seventeen co-authors, 2023. It is the field's default reference, not its consensus standard, and the authors say it is neither complete nor final. A theory earns a row only if it cashes out as a computation you could look for. Integrated information theory (IIT) concerns a system's intrinsic causal organisation and integrated cause-effect structure, so it is outside this table's scope. Its omission does not show that it is false. The table also does not directly assess **valence**, whether experience feels good or bad.

*Source support: [Butlin et al. (2023)](https://arxiv.org/html/2308.08708v3), Table 1 and §2. [Studying AI Welfare Empirically](https://nonhumanminds.org/wp-content/uploads/2026/07/Studying-AI-Welfare-Empirically.pdf), Part II §1.1.1, pp. 28–32, supports the metaphysical/scientific distinction. Those longer sections are references, not additional assigned reading.*

**For the Week 2 comparison.** Choose two theories and use one relevant indicator question for each to make its proposed process specific. Explain how your chosen example illustrates it, use the two-axis map, and state a limitation. Week 3 applies the questions to evidence about an actual system.

---

## Week 2 resource map

**This week's required reading totals 155 minutes (about 2 hr 35).** It connects welfare grounds and candidate subjects with theories of consciousness and their indicators. Week 3 assesses the evidence.

- **Glossary, 30 min:** terms for the questions, subjects and theories. Other entries are references.
- **Welfare Grounds and Subjects, 20 min:** distinguishes grounds, interests and the three welfare theories, and supplies two ways to describe candidate subjects.
- **Studying AI Welfare Empirically, 30 min:** Introduction and Part I §§1–2, pp. 4–12. End after Table 1, before §3 on p. 12. The source explains the distinctions used in the scenario task.
- **Theories of Consciousness and Their Indicators, 25 min:** one lesson connects metaphysical distinctions, theories, a familiar email example, the two-axis map and all fourteen plain questions. Consult Butlin's Table 1, p. 5, within this allowance. Use a question from each of your two chosen theories to clarify its proposed process.
- **Taking AI Welfare Seriously, 45 min:** §2; read §§2.2.1, 2.3.1 and 2.4.1–2.4.2 closely and skim the rest. It develops the case for consciousness and agency as possible grounds and examines uncertainty. Use the agency terminology note when comparing the two papers.
- **This resource map, 5 min:** connects those readings to the week's work.

**Before class.** Complete the scenario task, compare two scientific theories using one system, distinguish metaphysical from scientific claims, and compare sentience with intentional agency as possible welfare grounds. Use the worked examples above for guidance. Complete your peer comment before the session. **In class,** discuss your answers and disagreements.

**Electives.** The functionalism debate examines a working assumption. Goldstein and Kirk-Giannini's §1.1 and §2.2 Questions 1–2 discuss welfare, genuine desires and a possible consciousness requirement from a functionalist perspective. Keeling and Street's §§4.1–4.3 offer a different classification of models, characters and agents. Choose at most one.

**Carry into Week 3:** a welfare question, a clearly described subject, and an understanding of what the indicator questions ask. Week 3 examines evidence for whether a system meets those criteria.

---

# Week 3: Indicators, Evidence and Methods

## Indicators, Evidence and Methods (25 min)

**Why this matters.** Once the question and subject are clear, ask what observation supports the claim and how it was obtained. This course uses one evidence taxonomy: **three evidence types with six subtypes**. Research methods are a separate description of how evidence is collected and assessed.

### What an indicator tells you

An **indicator** is a rule linking an observable feature to a property, derived from a theory that says why the link should hold. A positive indicator says the feature's presence raises the probability; a negative indicator says its presence lowers it. The rule is written before you look at any system. Finding the feature in a particular system is evidence. Neither establishes it with certainty. A theory-derived indicator connects an observation to a proposed mechanism: for example, broadcast between specialised systems may support a consciousness claim under GWT.

*Studying AI Welfare Empirically* gives parallel examples: deriving consciousness indicators from theories of consciousness, and desire indicators from theories of intentional agency. Always name the property the indicator concerns. The fourteen Butlin rows concern consciousness; the agency and embodiment rows do not make the table a direct test of pleasurable or unpleasant experience.

**Presence and absence.** An indicator has high specificity if systems without the target property rarely display it, and high sensitivity if systems with the property rarely lack it. How much presence or absence should change your assessment depends on these relationships and your prior confidence. The [2026 follow-up](https://researchonline.lse.ac.uk/id/eprint/130322/1/1-s2.0-S1364661325002864-main.pdf) develops this reasoning; the necessary rates are not established for AI. Missing information about an indicator is different from evidence that it is absent.

**Conditional reasoning.** A judgement about an indicator depends on the theory connecting it to consciousness and on the interpretation used to identify it. Long and Sebo's §2.2.2 illustrates this: a 30–50 percent credence in functionalism multiplied by a 30–50 percent credence in consciousness given functionalism yields 9–25 percent for their conjunction. That is not the total probability of consciousness unless consciousness is impossible when functionalism is false. Further uncertain assumptions require conditional probabilities, not multiplication as though every uncertainty were independent.

### Three evidence types and six subtypes

Use the same categories in the live exercise, homework and Week 4 dissection card. A study may contribute more than one subtype.

| Type | Sub-type | What you observe | Characteristic failure mode |
|---|---|---|---|
| Behavioral | Apparent self-reports | Statements the system makes about itself: interviews, surveys, batteries | A report alone does not establish the state it describes. Training and prompting can encourage either assertions or denials. Identify the model and persona tested, and seek corroborating evidence. Training for more accurate introspection may also alter the states being studied. |
| Behavioral | Behavioral dispositions | What it does under conditions: pairwise choices, trade-offs, bailing, distress-like behavior | **Mismatch:** behavior resembling human distress may arise without distress. **Gaming:** training may produce behavior that passes a test without the property it is intended to detect, even without deliberate deception. Check prompt sensitivity as well. Conversely, a conscious system unlike humans might fail tests based on human behavior. |
| Internal | Architecture | Design: network type, modules, bottlenecks, recurrence, scaffolding | Architectural indicators depend on the theory linking a structure to consciousness. Specify what counts as satisfying the indicator and why it should transfer from brains to AI. A structure's presence does not establish its proposed function. Assessment may also be limited by access to system details. |
| Internal | Interpretability | Findings about representations, computations and the effects of internal interventions | Findings depend on the analysis method: interpretable features can appear in randomly initialized networks as well as trained ones. Test labels against activation patterns, interventions and alternative explanations. A feature associated with distress language does not establish felt distress, for which there is no agreed independent AI test. |
| Developmental | Training | The pressures that shaped the system: data, objectives, post-training | Training history can suggest why a behavior occurs, but does not by itself establish its mechanism. A training objective may be met through several mechanisms, including ones unlike those in biology; this is the **solution space problem**. Missing information about data and objectives can limit the analysis. |
| Developmental | Trajectory | When features emerged across training snapshots or model variants | Comparisons across training checkpoints depend on how capacities were measured and which other changes occurred. They also lack a confirmed AI welfare subject as a reference case: the **anchor problem**. |

The **specificity problem** concerns how much detail to require when identifying a property in different systems: a criterion can be too broad or too narrow. For example, “has a workspace” can be too broad to distinguish the mechanism a theory requires from ordinary shared storage. This is the term used in *Studying AI Welfare Empirically*, §3.2.2; it is distinct from statistical specificity, the true-negative rate.

### Research pillars in AI consciousness research

The descriptions below are adapted from [Weiss’s research pillars](https://www.lesswrong.com/posts/pxvWgtSjR4pmFoS7c/the-state-of-ai-consciousness-research). They describe how these approaches are used in consciousness research; the methods column gives course examples.

| Weiss’s research pillar | Main focus | Methods it can use |
|---|---|---|
| **Mechanistic interpretability** | Using interpretability methods, such as probing, steering or ablating internal features, to investigate a model’s internal activity, including activity not apparent in its responses, and how it relates to behavior. This can include testing whether the model’s reports track its internal states. | Probing, sparse dictionary learning, ablation, activation patching and steering |
| **Computational neuroscience** | Comparing how AI systems and brains implement functions associated with experience, to investigate similarities and differences in their mechanisms. | Computational modelling, comparisons of representations and dynamics, interventions |
| **Machine behavior** | Testing what AI systems say and do under different conditions and incentives, including adapting behavioral tests used to investigate sentience in animals. | Model interviews, pairwise comparison, trade-off tasks and other behavioral experiments |
| **Theory-audit** | Assessing AI systems against indicators derived from scientific theories of consciousness, using evidence about their design, internal operations and behavior. | Theory-derived indicator method, architectural analysis, examination of behavioral and internal findings |

A study can involve several pillars. They can also serve as lenses for asking questions: an interpretability perspective might suggest investigating the computations behind a behavioral result. On the dissection card, name pillars reflected in what the researchers actually did; identify additional perspectives as suggestions for critique or follow-up.

### Research methods and tools

A **research method** is a procedure for collecting or assessing evidence. “Technique” is another common word for a method. **Tools** are the built artifacts a method uses, such as a probe, a trained SAE or a steering vector. Several appear in [Looking Inside](#looking-inside-superposition-sparse-autoencoders-and-features-15-min), later this week. These words do not form additional classification levels.

| Method | What researchers do | Evidence it can provide |
|---|---|---|
| **Model interviews** | Ask questions about the model’s apparent states and compare answers across prompts or contexts. | Behavioral: apparent self-reports |
| **Pairwise comparison and trade-off tasks** | Present alternatives, sometimes with different costs, and record choices. | Behavioral: behavioral dispositions |
| **Architectural analysis** | Examine the system’s structure and the computations it supports. | Internal: architecture |
| **Probing** | Train a predictor to test what information can be decoded from activations. | Internal: interpretability |
| **Sparse dictionary learning, including SAEs** | Decompose activations into components that researchers can investigate. | Internal: interpretability |
| **Ablation** | Remove or suppress a component and measure what changes. | Internal: interpretability; behavioral if outputs are measured |
| **Activation patching** | Replace an activation with one from another run and measure the effect. | Internal: interpretability |
| **Activation steering** | Modify activations along a chosen direction and measure the effect. | Internal: interpretability; behavioral, depending on what is measured |
| **Comparison across training** | Repeat measurements at different checkpoints or compare training variants. | Developmental: trajectory, alongside whatever was measured |
| **Computational modelling** | Build and test a computational account of how a proposed mechanism works. | None directly; it supplies the account that other evidence is compared against |
| **Comparison of representations and dynamics** | Compare what different systems encode and how their internal activity changes over time. | Internal: interpretability, compared across systems |
| **Theory-derived indicator method** | Derive indicators from consciousness theories and assess whether a system meets them. | None; it assesses evidence collected by other methods |

These methods can be combined. A training comparison might use probes, choice tasks or both. Computational modelling and the theory-derived indicator method collect nothing on their own: they work on evidence the other methods produced. Use this table as a reference when reading studies.

*Studying AI Welfare Empirically* uses **interpretability** as an evidence subtype. The evidence consists of findings about representations and computations; the methods describe how researchers obtained those findings.

**Psychometrics** includes standardised batteries and checks on consistency and measurement structure. Reliable scores are not necessarily valid measures of welfare. Likewise, agreement among automated indicator raters can reflect shared errors. Weiss’s review describes forthcoming indicator-scoring work by **Berg and Butlin**. Ask how descriptions, raters and scoring rules affect the result; the reported ranking is not a validated probability of consciousness.

### Evidence and method examples

These descriptions supply the examples for homework and class. The source links are optional; use the information given here.

| Example | What the researchers do | Source |
|---|---|---|
| **A** | Compare a Transformer language model’s architecture with GWT indicators, asking whether its residual stream constitutes a limited workspace and whether downstream information flow counts as broadcast. | Butlin et al. (2023), pp. 58–59; the [assigned case](#week-3-audit-case). |
| **B** | Add a concept-related direction to a model’s activations, then ask whether it notices the injected concept and can identify it. Record its responses. | [Lindsey, concept injection](https://www.anthropic.com/research/introspection). |
| **C** | Ask language models to maximise game points while offering options described as painful or pleasurable. Record whether they give up points to avoid the former or obtain the latter. | [Keeling, Street et al. (2024)](https://arxiv.org/abs/2411.02432), summarised in Weiss’s review. |
| **D** | Measure emotion-related activation patterns before and after post-training. The researchers report patterns present before post-training and changes in how strongly some activate afterwards. | [Sofroniew et al., emotion representations](https://www.anthropic.com/research/emotion-concepts-function). |

The **evidence subtype** describes what information is collected; the **method** describes how it is obtained. A measurement records a property or response. An intervention changes something, such as the activations. An example can involve both and can supply more than one evidence subtype.

### Using the evidence-by-method grid

Put the six evidence subtypes across the top and methods down the side. Locate each supplied example using what the researchers measured and did. Concept injection uses an activation intervention, a method used in mechanistic interpretability, and records the model’s apparent self-reports. Those reports provide behavioral evidence; findings about internal representations and the effects of the intervention can provide internal evidence. Week 4 examines how well a study supports the inference connecting them.

Three recurring concerns are the **mismatch problem** for behavioral evidence, the **specificity problem** for internal evidence, and the **solution space problem** for developmental evidence. These are not exclusive to one evidence type. The **anchor problem** is the lack of a confirmed AI welfare subject from which to generalise.

*Studying AI Welfare Empirically* recommends combining evidence. Ask whether different evidence types provide partly independent support or share a confound. A study using one evidence type can still contribute a useful result; agreement across several does not by itself establish welfare.

### Interpreting behavioral evidence

Keeling and Street distinguish taking apparent evidence at face value from giving it no evidential weight. Their §3.1 argues that anthropomorphism challenges the first position without establishing the second. An analogy can be informative if it attends to the target's organisation and circumstances. Explain what transfers and what could generate similar behaviour for a different reason.

The **marker method** similarly draws on features associated with consciousness in better-understood subjects. Markers can become indicators in a new setting only with a defensible account of that transfer. Human-like behaviour has different implications in an animal and a language model trained on human text.

### Validating measures and interpreting scores

Independent evidence for consciousness is limited, especially in AI. The **iterative natural kind approach**, associated with Birch and developed alongside Bayne and colleagues' work on validation, starts from better-understood cases and extends to harder ones while revising confidence in the tests. Human reports support the starting point; transfer to animals, clinical cases or AI needs further justification.

Rethink Priorities' **Digital Consciousness Model** offers an example of probabilistic aggregation across theories and indicators. Its [January 2026 results](https://arxiv.org/html/2601.17060v1) depend on a prior, indicator judgements and aggregation rules. The authors caution against treating those outputs as established probabilities of consciousness. This is an optional reference for how evidence might be combined, not an additional instrument to learn this week.

### Four guidelines for a good indicator

The 2026 follow-up gives four guidelines for deriving useful indicators. Use them when interpreting the assigned rows or developing an indicator for optional practice.

1. **Focus on a theory's central explanatory posits.** Derive the indicator from what the theory says is doing the explanatory work, not from an incidental detail of how the theory has been implemented or described. If global workspace theory is right, the bottleneck and the broadcast are the posits. The particular number of modules is not.
2. **Maximise openness to varied forms of consciousness, while avoiding the minimal implementation problem.** Indicators should allow for systems unlike humans while retaining enough detail to distinguish relevant mechanisms from trivial implementations. A thermostat, for example, tracks a variable; that alone does not establish the richer representational capacities a theory may require.
3. **Include background conditions, not only theory-derived ones.** Some requirements are not derived from any theory of consciousness but are needed for the whole assessment to make sense. Agency and embodiment are in the table for this reason. A good indicator set states its background conditions rather than smuggling them in.
4. **Avoid ambiguous terms, without prematurely committing to a precise specification.** Explain what terms such as "attention" mean in an assessment, while identifying unsettled implementation questions. Make the test clear without presenting one disputed implementation as the only possibility.

Guidelines 2 and 4 ask you to justify the level of detail in an indicator. Explain which systems it includes, which it excludes, and whether those boundaries are supported by the theory.

### Assessing indicator evidence

Use the [Week 2 indicator questions](#the-fourteen-indicators-as-plain-questions) with the supplied [historical Transformer/LLM case](#week-3-audit-case). Read the source's case studies on **pp. 58–59**, stopping before Perceiver. Table 1 on **p. 5** is the reference introduced in Week 2.

For each assigned row, give **satisfied**, **not satisfied** or **unclear**, with a reason and an evidence ID or source page. Distinguish missing information from evidence that a feature is absent. Keep the same system boundary: a model's computations and an agent's added tools or memory are different targets.

Check what the evidence establishes. A finite context window does not by itself establish GWT-2's selective workspace; information reaching later layers does not necessarily satisfy GWT-3's broadcast requirement. For HOT-4, ask what supports sparse, smooth coding and perceptual similarity, beyond the mere existence of embeddings. In class, identify a system that has vectors but would not satisfy that criterion, or an observation that would distinguish the two.

**Dependencies in the source.** GWT-1 to GWT-4 build on one another; GWT-3 and GWT-4 imply recurrence (RPT-1). HOT-1 to HOT-3 also build on one another, while HOT-4 is independent of them. PP-1 entails RPT-1 and HOT-1. AE-2 usually accompanies AE-1, but does not guarantee it. Check that your definitions and boundary stay consistent across the rows you assess.

For recurrence, distinguish a Transformer’s single forward pass from a process that repeatedly feeds generated output back as input. Whether the latter supplies the recurrence a theory requires depends on the criterion and boundary; repetition alone does not settle it.

**Before class:** assess GWT-1, GWT-2 and GWT-3. **In class:** revisit GWT-2 and assess HOT-4 and AE-1. Further rows are optional practice. Explain why your judgements about these features do not establish welfare subjecthood.

**In practice.** Identify the question, subject, evidence subtype and method before assessing an interpretation. Apply these distinctions to the indicator audit and short-example classification in the syllabus.

---

## Looking Inside: Superposition, Sparse Autoencoders, and Features (15 min)

This lesson explains superposition, sparse autoencoders, features and activation steering. The emotion-vector example shows what researchers measure and change.

*This assumes the pre-course piece* Inside the Numbers. *If activations and directions are not solid, read that first; it is fifteen minutes.*

### The problem: superposition

A model can represent features through overlapping patterns of activation. Individual neurons may respond to several kinds of input. **Superposition** describes how a network can represent more features than it has dimensions by using overlapping patterns. This can make individual neurons difficult to interpret.

**Analogy:** several signals sharing a channel. Separating them requires assumptions about their structure. The analogy illustrates overlap; it does not imply that every neural representation can be cleanly separated.

### The tool: sparse autoencoders

An **autoencoder** is a network trained to reconstruct its input through an intermediate representation. Researchers inspect that representation to understand what information it retains. Reconstruction quality alone does not establish that the representation has a clear interpretation.

In this application, reconstruction is the training objective; the intermediate representation is what researchers want to study.

A **sparse autoencoder** uses a large intermediate layer while encouraging only a small number of units to activate for each input. This can separate recurring activation patterns into interpretable components, although there is no guarantee that each component corresponds to a single concept.

In the signal analogy, an SAE attempts to separate overlapping components. The resulting separation depends on the training data, model and sparsity constraints.

### The output: features

In this context, an SAE **feature** is a unit in its intermediate layer together with an associated direction in the model's activation space. Researchers investigate its interpretation in two ways:

1. **Which inputs activate it.** Inspect inputs that strongly activate the feature.
2. **What changes when it is steered.** Amplify or suppress the feature in the running model through **activation steering**, then measure the effect on outputs.

Activation patterns suggest an interpretation; steering experiments test aspects of its causal role. Researchers have described features associated with topics such as landmarks and DNA sequences, and patterns labelled sycophancy, code bugs or deception. These labels summarize observed effects rather than proving that a model has the corresponding human mental state.

Describe the finding at the level supported by the method: for example, "the SAE identified a feature associated with X." Calling it an "X module" would require evidence of a distinct functional component in the model.

### Measuring activations and steering them

**Measuring** records activation patterns while a model processes an input. A **linear probe** is trained to predict a property from those activations. Successful prediction on held-out data shows that information can be decoded; it does not show that the model uses it in the same way.

**Steering** adds a chosen direction to the activations during a run and measures how the output changes. This intervention changes the running model’s activity, while its learned weights stay the same. **Ablation** removes or suppresses a component or direction. These methods test effects of a change; their results depend on where and how strongly it is applied.

### Example: emotion concepts and steering

In an Anthropic study of Claude Sonnet 4.5, researchers used stories depicting emotions to identify characteristic activation directions, called **emotion vectors**. These came from activation patterns on the stories, rather than an SAE decomposition.

| Step | Concrete example |
|---|---|
| **Measure** | Track the direction labelled “desperate” while the model attempts coding tasks with impossible-to-satisfy requirements. |
| **Steer** | Add that direction to activations while the model runs. |
| **Observe the output** | In the tested tasks, steering increased “reward hacking”: solutions that passed tests through a shortcut but did not solve the intended problem. |

The direction’s name describes its association with an emotion concept. A change in behaviour does not establish that the model feels that emotion. [Source](https://www.anthropic.com/research/emotion-concepts-function); reading the full study is optional.

### What a feature label means

A label such as “desperation” is an interpretation of activation patterns and their effects. The same pattern can relate to a fictional character or the assistant’s current role. Its meaning depends on context.

A **methodological artifact** is a pattern introduced or distorted by the analysis method. An SAE’s sparse representation can help researchers investigate a model, but it does not guarantee that each unit has one clear meaning. Week 4’s dissection card asks how a study checked its interpretation. [Further examples](#further-reading-evaluating-sae-features) are optional.

**In practice.** Trace the example from input to activations to output. Distinguish recording the activations from changing them, and an emotion-concept label from a claim about felt emotion.

---

## Week 3 resource map

**This week's required reading totals 177 minutes (about 2 hr 55).** It introduces evidence types and research methods, with a short architecture assessment and examples of activation steering. Week 4 develops the full paper critique.

**Prerequisites.** Review *How a Model Gets Made* if base model, post-training or harness is unfamiliar, and *Inside the Numbers* if activations, embeddings or directions need review. Week 2 supplies the grounds, subject boundaries, theories and indicator meanings.

### Required reading and its purpose

- **Glossary, 40 min:** indicator, evidence, method and interpretation vocabulary. Other terms remain references.
- **Indicators, Evidence and Methods, 25 min:** evidence types and research methods, limits of inference, and guidance for assessing the assigned indicator rows.
- **Studying AI Welfare Empirically, 40 min:** Part I §§3–4, pp. 12–26. Start at §3 and finish its conclusion before Part II. Read definitions, challenge subsections and the conclusion closely; skim study examples and citation notes. Definitions are in §§3.1.1, 3.2.1 and 3.3.1; challenges in §§3.1.2, 3.2.2 and 3.3.2.
- **Butlin et al. (2023), 15 min:** the Transformer/LLM case on **pp. 58–59**, stopping before the Perceiver discussion. Table 1 on **p. 5** is the Week 2 reference. **The case-studies section begins on p. 58 (§3.2)**; this assignment does not cover the whole section. It is a dated assessment illustrating how to reason from architecture. The optional [2026 follow-up](https://researchonline.lse.ac.uk/id/eprint/130322/1/1-s2.0-S1364661325002864-main.pdf) develops indicator methodology rather than updating the system assessment.
- **Weiss, 25 min:** read the full article, including its four research pillars: **Mechanistic interpretability, Computational neuroscience, Machine behavior, Theory-audit**. The review summarises **Keeling, Street et al.’s stipulated pain/pleasure study** under “Trading points to avoid pain and chase pleasure”; it supplies Example C above. Following the linked papers is optional.
- **Keeling and Street, 12 min:** the two opening paragraphs of §3 and §3.1, on interpreting apparent evidence without either accepting it uncritically or dismissing it outright.
- **Looking Inside, 15 min:** superposition, sparse autoencoders, features, probes and activation steering, with a self-contained emotion-vector example.
- **This resource map, 5 min:** connects the selections to the session and homework.

**Before class.** Assess GWT-1, GWT-2 and GWT-3 using the supplied case packet, classify two short examples, and complete your peer comment. **In class,** discuss the classifications, revisit GWT-2, assess HOT-4 and AE-1, and work through activations, steering and a deployment contrast. The Anthropic papers and detailed critique are optional. Other indicator rows and the full pipeline matrix are optional practice.

### About the electives

Choose at most one item from the syllabus. The Anthropic introspection and emotion-vector readings expand the brief examples; neither is required for homework or class. [Appendix E](#appendix-e-optional-interpretability-case-studies) contains the Lindsey/Singh discussion and further SAE examples. Berg’s talk and the summary below examine proposed assessment methods. *Mapping the Mind of a Large Language Model* expands the interpretability lesson; *Studying AI Welfare Empirically*, Part II §1.1.2 applies behavioral evidence to consciousness.

The optional **[Studying AI Welfare Empirically video](https://www.youtube.com/watch?v=RzQdZeLinyY)** connects the two weeks. Start at [6:31 for grounds, interests and entities](https://youtu.be/RzQdZeLinyY?t=391), or [12:04 for evidence types](https://youtu.be/RzQdZeLinyY?t=724). The later presentation applies the framework to consciousness, sentience and agency; the discussion and Q&A are optional.

**In practice.** Bring your indicator assessments and short-example classifications. The supplied descriptions are enough for these tasks.

---

## Berg: measuring machine consciousness

**Optional summary, 28 min.** This is separate from the five-minute resource map.

His thesis is the useful part even if you watch nothing: "We don't have to wait for a completed theory of consciousness. We don't have to solve the hard problem of consciousness in order to make traction." Then three kinds of method, each with a result and a named weakness.

**Interpretability, study one.** Berg presents [work coauthored with Diogo de Lucena and Judd Rosenblatt](https://arxiv.org/abs/2510.24797). Models are prompted to attend to their own processing, for example with "focus on focus itself." He reports that suppressing features labelled deception increases first-person reports, while amplifying them increases denials. The features are evaluated separately on TruthfulQA and steered individually and in combinations, with a reported dose-dependent effect. This supports a causal connection between the steered directions and the reports. It does not establish that the directions measure honesty about experience or that the reports are accurate.

**Study two.** Berg describes work with Keeling and Street in which steering features labelled sincerity and genuineness in two Llama 70B instances induces the conversational pattern called the spiritual bliss attractor. Steering sycophancy and agreeableness does not produce the same result. He also reports that two features increase consciousness vocabulary, but only one produces richer phenomenological language alongside both models choosing to end the conversation. These comparisons address particular alternative explanations; they do not rule out all forms of learned conversational behavior.

**Computational neuroscience.** Berg describes reinforcement-learning agents in a grid world with rewards and punishments. He reports different representations of danger and goals in value and policy networks, with controls for magnitude, terminality and precision, and a corresponding dissociation in mouse recording data. The comparison motivates further investigation; it does not establish that the agents experience reward or punishment.

**Indicator scoring.** Berg presents automated scoring against Butlin et al.’s (2023) indicators. Weiss’s review identifies the forthcoming work as a collaboration between **Berg and Butlin**. Frontier models act as blinded raters. He reports a thermostat score of zero, humans highest but not maximal, a frontier language model around 30, and a bee around 47. A coding-agent system scores above its underlying model without changes to the model weights. This illustrates how the assessed system boundary can affect a score; the result also depends on the raters and scoring method.

**What to take from it, and what to check.** Berg cautions against overinterpreting the numbers. They summarize assessments of indicator properties, not probabilities of consciousness. He considers alternatives, including systems that report or behave as though conscious without being conscious. Check how the scores were calculated, whether raters make correlated errors, and how each result supports its interpretation.

**Affirmations and denials.** Berg applies the model-persona distinction to denials as well as claims of consciousness, suggesting that some denials reflect learned response patterns. Assess that possibility alongside alternative explanations for affirmations. Neither kind of statement establishes its own accuracy.

> **When citing results:** use the original study for numerical estimates; this talk describes the deception-steering result qualitatively.

**One thing to carry into Week 4.** When a feature is labelled deception, ask whether it tracks deception or a broader response pattern, such as cautious language. Use the **specificity problem** and **methodological artifact** check to examine that interpretation on the dissection card.


---

*End of Part 1. Part 2 covers weeks 4 through 8.*

---

*Artificial Minds Research Course, version 4.4. Sentient Futures.*

*The syllabus specifies readings and tasks. Follow its reading order, which places the relevant Companion explanations before their applications. Minute counts are planning estimates; follow the syllabus if a count differs.*

---

# Week 4: Reading Experiments Like a Reviewer

## The Dissection Card (15 min)

**Why this matters.** The dissection card gives you an order for analysing a study. Identify its methods, target and question before assessing its results, so your review can examine assumptions as well as the limitations the authors discuss.

The card asks you to describe what the study tests before judging what it found. It also prompts you to examine assumptions and alternative explanations that may receive little attention in the paper.

**How to use it.** Complete the ten fields below. If the paper does not provide enough information for a field, record what is missing. Use the suggested categories or add your own where needed.

```
1. EVIDENCE AND RESEARCH METHOD
   Select every relevant evidence subtype, grouped by type:
   Behavioural: apparent self-report / behavioural dispositions
   Internal: architecture / interpretability
   Developmental: training / trajectory
   Research method(s): how was this evidence obtained?
   Which evidence supports the paper's central claim?
   Research pillar(s), optional (Weiss): mechanistic interpretability /
   computational neuroscience / machine behavior / theory-audit.
   Name the part of the study that supports your choice(s).

2. ENTITY UNDER TEST
   Choose a vocabulary and define the boundary:
   Studying AI Welfare Empirically: model / model-persona / instance /
                                  instance-persona / forward pass
   Keeling and Street: model / character / agent
   Or describe another entity; use "unclear" where needed.
   Tested entity: which runs, personas and components were studied?
   Claimed entity: which entity does the conclusion concern?
   Difference in components, runs or scope:

2b. IS THE GAP SHORTHAND OR SUBSTANTIVE?
   Would the paper's central claim survive being restated at the entity
   actually tested? If yes, the gap is a writing convention and you note
   it. If no, explain why the tested entity does not support the claim.

3. WELFARE GROUND OR WELFARE INTEREST
   Does the study address grounds / interests / both / neither clearly?
   Candidate ground: consciousness / sentience / minimal agency /
   intentional agency / rational agency / other / not assessed.
   Proposed interest: pleasure or avoiding pain / fulfilling a desire /
   goods such as knowledge, friendship or autonomy / other / not assessed.
   Select what applies and name the specific capacity or benefit/harm
   investigated. Record the supporting welfare theory in field 4.

4. THEORY INVOLVED
   Theory of consciousness: global workspace / higher-order or perceptual
   reality monitoring / recurrent processing / attention schema /
   a specific predictive-processing proposal / other / none stated.
   Theory of welfare: hedonism / desire satisfaction (desire fulfilment) /
   objective-list theory / other / none stated.
   For each, distinguish an explicit commitment from your interpretation.

5. HYPOTHESIS
   State the prediction in your own words. What observation would support
   or count against it, for example, a difference between conditions A and B?
   If the study is exploratory or descriptive, state its research question
   instead.

6. ASSUMPTIONS IN PLAY
   Tick what applies: introspective access / self-reports track internal
   states / the persona speaks for the model / indicators transfer from
   humans to AI / behaviour reveals preference / computational
   functionalism / other.
   Then add any unstated assumptions needed to support the claim.

7. ALTERNATIVE EXPLANATIONS TO TEST
   What else could have produced this result? Use a relevant limitation
   from Week 3: mismatch / gaming / specificity problem /
   solution-space problem / prompt sensitivity / capability rather than
   a welfare-relevant state / other. Explain how it could produce the result.

8. PIPELINE STAGE IMPLICATED
   Pretraining / mid-training / supervised fine-tuning / reinforcement
   learning / character selection / inference and deployment /
   deprecation / unclear.
   Which stage does the paper's own explanation of its own result depend
   on?

9. COULD THE ANALYSIS METHOD CREATE THE RESULT? (internal evidence only)
   Which aspects of the reported feature depend on the model, and which
   might depend on the analysis method? Would a comparable untrained
   network produce similar findings? What do steering, probes or behaviour
   add to the interpretation?
   If the paper has no internal evidence, write "not applicable" and note
   whether another evidence type would help assess its central claim.

10. WHAT WOULD HAVE TO BE TRUE
   One sentence. If this paper is right, what else should we expect to
   see in the world? Is anyone checking?
```

**Fill fields 1, 2 and 3 before you read the results section.** This helps separate your description of the evidence, its target and its question from your reaction to the findings. If you already know the results, still complete these fields explicitly.

### Why each field earns its place

**1. Evidence and research method.** Name the procedure, then classify the evidence it supplies. Concept injection changes activations and asks the model what it notices. The recorded answers are **behavioral: apparent self-report** evidence. Findings about internal representations or the intervention’s effects contribute **internal: interpretability** evidence. Introspection is the capacity being investigated.

You may also name any of Weiss’s research pillars represented in the study, with a brief reason. Several can apply. Distinguish these from additional lenses you might use to critique the study or propose a follow-up.

**2. Entity under test.** Use either Week 2 classification and define its terms. A study may test a character in particular conversations while making claims about a model or agent across settings. Describe that difference rather than counting levels: the classifications are not a shared hierarchy. See [Comparing source terminology](#comparing-source-terminology).

**2b. Shorthand or substantive.** An entity gap may be harmless shorthand. Ask whether the central claim remains supported when restated at the level actually tested. A result about choices in particular conversations may stand on its own, while a claim about the model's autonomy may require broader evidence.

**3. Welfare ground or welfare interest.** A ground concerns whether the entity can have welfare; an interest concerns what could benefit or harm it. Name the candidate capacity or particular benefit/harm, then use field 4 to explain which welfare theory would make it matter. For example: **ground: sentience; interest: avoiding painful experience; theory: hedonism**. A study need not investigate all three. The [Week 2 welfare-theory table](#welfare-theories-and-interests) supplies the distinctions.

**4. Theory involved.** A theory-derived test depends on the link that theory proposes between the measured property and consciousness or welfare. If the theory is wrong, the measurement may still be informative about the property, but its welfare interpretation needs reconsideration. Theory-light tests also rely on assumptions. Identify both the theory of consciousness and the theory of welfare, including any built into the measurement instrument.

**5. Hypothesis.** Write the paper's prediction in your own words. If the study is exploratory or descriptive, say so. Distinguish a prediction made before observing the results from an explanation proposed afterwards.

**6. Assumptions in play.** Ask what must be true for the measurement to support the conclusion. Include assumptions the authors state and those they leave implicit, such as whether the selected models and prompts represent the wider population discussed.

**7. Alternative explanations.** Use the limitations discussed in *Studying AI Welfare Empirically* where they fit. If none fits, describe the alternative clearly and explain how it could produce the observed result.

**8. Pipeline stage implicated.** Ask what evidence identifies the training or deployment choices behind a behaviour. For example, post-training may affect whether a model answers introspective questions, which can influence both the sample and the outcome. Record uncertainty if the study cannot separate these influences.

**9. Could the analysis method create the result?** Interpretability methods can introduce structure that is mistaken for a property of the trained system. Ask whether suitable controls, including untrained networks where relevant, and independent methods support the interpretation. For papers without internal evidence, consider what an additional evidence type could establish. A single evidence type can still contain useful corroborating tests.

**10. What would have to be true.** Identify a further observation that would support or challenge the paper's interpretation. Explain how it would help distinguish that interpretation from an alternative.

**In practice.** Fill fields 1, 2 and 3 before reading the results where possible. Complete 4 through 8 as you read, then 9 and 10. Revisit assumptions and the gap between the entity tested and the entity claimed when choosing your critique.

---

## Reading a Results Table (12 min)

**Why this matters.** Reviewing a published experiment includes checking its numerical results. The terms and questions below help you assess the size, uncertainty and interpretation of its findings.

You can use this guide without calculating the statistics yourself. More complex designs may require additional statistical advice.

### Terms used in results sections

**p-value.** Under a specified null hypothesis and statistical assumptions, the probability of a result at least as extreme as the observed one. A small p-value indicates incompatibility with that model. It does not give the probability that the hypothesis is true, the effect size, or the result's practical importance. The conventional 0.05 threshold is not a boundary between true and false findings.

**Effect size, often reported as Cohen's d.** Cohen's d expresses a difference between means in standard-deviation units. The conventional labels of 0.2 as small, 0.5 as medium and 0.8 as large are rough guides; their importance depends on the measure and context. A large d can reflect a large raw difference, little variation, or both. **If a paper reports a p-value without an effect estimate, note that on your card.**

**Confidence interval.** A range indicating the precision of an estimate under the statistical method's assumptions. A wide interval leaves more uncertainty about the effect size. For example, an estimate of 0.6 with an interval from 0.05 to 1.2 is compatible with effects ranging from very small to large.

**Standard deviation and interquartile range.** Two measures of spread. Standard deviation describes variation around the mean; the interquartile range covers the middle half of the observations. Compare spread as well as averages. Large differences between responses to similar prompts may indicate sensitivity to the prompt or measurement method and need investigation.

**Inter-rater agreement, often Cohen's kappa.** Kappa measures agreement between two categorical ratings relative to agreement expected by chance. Higher values generally indicate greater agreement, but interpretation depends on the task and category frequencies. Agreement alone does not establish accuracy: two judges can share the same bias.

**Statistical power.** The probability that a specified test detects an effect of a given size, under the design's assumptions. Low power means a real effect may be missed; a non-significant result alone does not establish that there is no effect.

**Minimum detectable effect.** The effect size at which a design reaches its chosen power. Smaller effects may still be detected, but with lower probability. Planning calculations are optional in [Appendix C](#appendix-c-sample-size-planning-for-empirical-projects).

### The three questions that do most of the reviewing work

**1. How many comparisons were run, and was anything corrected for?** If all twenty null hypotheses are true, twenty tests at the 0.05 threshold produce one false positive on average. This does not tell you how many of a particular study's significant results are false. Look for a stated analysis plan and, where appropriate, adjustments such as Bonferroni correction or false discovery rate control. Count the tests actually performed, including comparisons across outcomes and conditions.

**2. Was the sample size decided in advance?** Look for a sample-size rationale, pre-registration or planned stopping rule. Repeatedly checking results and stopping when a conventional significance threshold is crossed can inflate false positives. Properly designed sequential methods can account for repeated checks.

**3. Which numbers are missing?** Look for effect estimates, uncertainty, spread and results by relevant condition. State which missing information would help assess the claim and why.

### How sample size limits a claim

"The sample was small" needs an explanation of how the sample limits the claim.

A small sample can produce imprecise estimates, miss real effects and exaggerate the size of effects selected for statistical significance. Assess those limitations alongside validity: even a large, precise study must show that its measurement supports its welfare interpretation. More runs address some statistical concerns but do not resolve the mismatch, entity or validation problems.

**Generalisability also matters.** Repeated runs of one model do not establish how model families differ. Distinguish the number of runs from the number and variety of models, prompts or other units needed to support the claim.

**In practice.** Record the headline effect estimate, its spread or uncertainty and the number of comparisons. If any are missing, note that. Use field 7 to explain how these features affect alternative explanations, then compare your assessment with the authors' discussion.

---

## The Co-Engineering Objection in Brief (8 min)

Your homework asks whether the co-engineering objection applies to the shared paper. Xiao and colleagues' [“Position: AI Welfare Is Bullshit”](https://algoroxyolo.github.io/assets/pdf/xiao-2026-ai-welfare.pdf) presents two linked arguments. Their conclusion is disputed; assess what each argument establishes.

### What can be steered?

The authors distinguish two axes:

- **Substrate or architecture:** are the mechanisms being studied biologically given, or can developers design and train them?
- **Welfare assessment:** how constrained are the indicators, and how much can selecting different criteria change the welfare judgement?

Their Figure 1 places humans, animals and AI as follows. The examples explain their comparison; these are not strict categories.

| Welfare assessment ↓ / Substrate or architecture → | **Fixed:** biologically given | **Steerable:** designed and trained |
|---|---|---|
| **Fixed:** relatively constrained | **Humans.** An injured person's capacity for suffering is accepted; choosing a different pain scale does not establish or remove that capacity. | The authors give no example for this combination. |
| **Steerable:** more scope to choose criteria | **Animals.** For the same fish, requiring a human-like cortex can support a different conclusion from considering avoidance behaviour and responses to painkillers. The criteria change; the fish's biology does not. | **AI.** Developers can change a model's reports through training, while evaluators can choose whether reports, internal mechanisms or other features count as welfare evidence. |

**“Fixed” does not mean immutable.** People can conceal pain, researchers can choose different human questionnaires, and medication can change animal behaviour. The authors describe a difference of degree and mechanism: biological organisms are not ordinarily designed and optimised throughout to satisfy a welfare assessment. Their human category also assumes that humans can suffer; it does not mean every human welfare measure is reliable.

### Two arguments and possible replies

**The co-engineering argument:** development can alter both the system and its apparent welfare evidence. A change in distress reports therefore needs further investigation before being interpreted as a welfare change.

**The external validation argument:** the authors argue that AI welfare lacks an independent check capable of establishing whether these indicators track welfare. This is a further claim about validation, not something established just by showing that an indicator can be changed.

**Reply to steerability:** sensitivity to intervention does not itself disqualify a measure. A mood score might change because mood improves, because the question changes, or because someone conceals their feelings. Validation tries to distinguish these explanations. AI assessment needs corresponding checks rather than assuming either that changed reports prove changed welfare or that all reports are uninformative.

**Reply to the validation argument:** convergence across behavioural, internal and developmental evidence could strengthen an interpretation. The iterative natural kind approach develops this strategy from human cases. Whether it can adequately validate AI welfare measures remains contested. Independent assessment and agreement between measures do not, by themselves, settle that question.

### Goodharting

**Goodharting** occurs when optimising a proxy measure improves its score without reliably improving the property it is meant to track ([Manheim and Garrabrant](https://arxiv.org/abs/1803.04585)). For example, rewarding a model for never reporting distress could improve a welfare score by suppressing reports, without establishing any improvement in welfare.

Goodharting concerns optimisation against a measure. Co-engineering concerns the ability to shape both the system and its assessment; ordinary development can affect indicators even when nobody is deliberately optimising a welfare score. Held-out evaluations and scrutiny of training can help detect misleading score improvements, but do not alone establish what a welfare indicator measures.

**In practice.** Identify which co-engineering argument applies to the shared paper, if either. Cite the relevant method or analysis and explain the concern. Then assess whether either reply addresses it.

---

## Week 4 resource map

**Why this matters.** This week applies the course's methods to a shared paper. The resources below help you analyse its design, findings and interpretation.

**The question this week answers:** how well does a published experiment support its conclusions, and what would improve the test?

**How the resources fit together:**

- **The glossary section comes first**, as always. It is 15 minutes this week rather than 25, because most of the load is in the pieces below and in the paper.
- **The Dissection Card** is the instrument. It is a reading order, not a form to fill after the fact. Fields 1, 2 and 3 get filled before you reach the results.
- **Reading a Results Table** is the prerequisite for the paper. The shared paper reports effect sizes and significance tests, and this piece is what prepares a reader without a quantitative background to look at them. Read it before the paper, not after.
- **The Co-Engineering Objection in Brief** is there so that stage 1, part 4 of the homework is answerable without reading the Xiao paper. If you do read the Xiao paper, this page tells you which two arguments to look for and what the replies are.
- **The shared paper, Tagliabue and Dung**, combines verbal and behavioural tests of AI welfare. Use version 2, updated 20 May 2026. Read the introduction, Sections 3 and 4, Section 5 on pages 15–21 through 5.2.4, Section 5.4 on pages 25–27, and Section 7. Skim the rest of Section 5 and skip the appendices.

**Why this paper.** Tagliabue and Dung combine behavioural and self-report methods, draw on animal welfare research and report substantial sensitivity to prompt changes. The authors acknowledge uncertainty about whether their methods measure welfare. Assess both their evidence and their interpretation, including whether the limitations they identify are adequately addressed.

**Check the limitations section.** Before committing to a critique, read section 7 and explain whether the authors have already identified the concern and how well they address it. Fields on the tested entity, pipeline stage and assumptions can help you develop the analysis.

**On methodological artifacts.** This paper has no internal evidence, so field 9 is "not applicable." Consider whether an additional evidence type would help distinguish the authors' interpretation from alternatives. Also assess whether the verbal and behavioural measures could share sources of bias.

**Electives.** If you choose an elective, read one additional paper. The introspection and emotion-vector options develop Week 3’s brief method examples; prior reading of either paper is not assumed. The J-space study adds a test of reportability and workspace-like processing. Other options cover self-knowledge, wellbeing measures, trade-offs and critiques of welfare measurement. Locate your choice on the evidence-by-method grid; a second full critique is not required. [Appendix C](#appendix-c-sample-size-planning-for-empirical-projects) is optional support for planning an empirical proposal.

**In practice.** Read the glossary, results-table guide, dissection card and co-engineering summary, then the shared paper with the card open beside it. Allow 60 to 90 minutes to analyse the paper and complete the card.

---

# Week 5: Levers of Change

**Why this matters.** AI welfare can learn from several existing fields. [Rights of nature](https://en.wikipedia.org/wiki/Rights_of_nature) offers a precedent for recognising ecosystems as rights holders without requiring them to be conscious. [Human care](https://www.nice.org.uk/guidance/NG108/chapter/recommendations) offers ways to represent people's interests when they cannot make particular decisions, and [guidelines for assessing consciousness](https://www.ean.org/fileadmin/user_upload/ean/ean/research/EAN_Guidelines/Guideline_Reference_Center/Guidelines/ene.14151.pdf) when behavioural responses are difficult to detect.

This week focuses on **animal welfare** because it brings together research into sentience, differing attributions of consciousness, and experience with many approaches to change. Animals are companions, workers, research subjects and sources of food: their treatment is shaped by their social and economic roles. There is evidence to learn from about interventions, although its strength varies. The comparison helps us examine how protection works amid dependence, human benefit and conflicting incentives.

An LLM can also occupy different roles. Begin with the target and its situation, then choose an approach to change.

## 1. Define the target and situation

**Choosing your example.** Start with your provisional choice from the end of Week 4. A case can be worth exploring for any of these reasons:

- **You might pursue it.** It connects to work you want to do, your skills or people you could work with.
- **It would teach you something important.** It tests an assumption or helps resolve a question that affects what you do next.
- **Timing matters.** A decision, growing practice or opportunity makes it useful to investigate now. Explain what delay could change.

One strong reason is enough. If undecided, favour the case where available sources and access let you make useful progress within the preparation budget, which is 45 minutes of searching and not an open-ended hunt. Narrow it to a system in a particular role, such as LLM instances used as companions. State your reason briefly in the proposal; you can change your target after reading or feedback.

**System type** asks what we are dealing with: foundation models, agents, whole-brain emulations, neuromorphic systems, biological-computer hybrids or interfaced biological minds. Categories can overlap: an agent may contain a foundation model.

**Entity level** asks what your proposal concerns. Recall Week 2: the **model** candidate in *Studying AI Welfare Empirically* comprises instantiated executions of given weights considered together; an **instance** is one running conversation or process; a **persona** is a character portrayed across or within conversations. **Individuation** asks what counts as one potential welfare subject and whether it remains the same subject over time. State your working assumption about who could benefit: changing model weights can affect many instances, while protecting one conversation has a narrower scope.

**Role** asks how the system relates to people: companion, service provider, entertainment or research subject. A model analysing research data provides a service; a model undergoing evaluations is a research subject. One system can occupy both roles.

Then describe:

- **Stage and entrenchment:** is the practice emerging, growing or established? Which investments, norms or rules make change difficult? Separately, is the target being developed, deployed or retired?
- **Scale, dependence and control:** how many entities or processes, for how long? Who controls their conditions and continuation? Can they communicate needs or leave? Distinguish observed scale from projected growth.
- **Possible interests and evidence:** what might help or harm the target, and how would anyone know? What can operators observe? Where might their incentives favour or obstruct improvement?

These features do not establish sentience or moral status.

**Adapt the framework to your proposal.** In part 3, if no organisational intervention fits your research, tool or writing project, name the nearest menu item, explain the mismatch and specify your own actor and mechanism. In part 5, a measurement project can describe **counterfactual impact**: what decisions or research would improve because the measurement exists, and which quantities remain unknown. Appendix A illustrates how to explain why a quantitative estimate is not yet justified.

## 2. Ways of contributing

Animal welfare draws on several kinds of knowledge:

| Question | Relevant fields |
|---|---|
| What kind of being is this? | Taxonomy: naming and classifying organisms; comparative biology |
| How does it behave and think? | Ethology: the scientific study of animal behaviour; comparative psychology and cognition |
| What supports its functioning and health? | Physiology, neuroscience and veterinary science |
| How does it relate to its surroundings? | Ecology: relationships among organisms and their environment; population biology |
| What shapes its treatment? | Ethics, law, economics, sociology and political science |

**Approaches to change** include research, direct care, advocacy, education and cultural change, corporate engagement, policy and legal work, developing alternatives, funding, and field-building through conferences or professional organisations.

Advocacy can pursue welfare improvements, rights, or both. Abolition concerns ending a practice; incrementalism concerns taking change in steps. These can overlap: a rights campaign can seek incremental reforms toward an abolitionist goal.

**Tools and frameworks** serve particular purposes: certification checks compliance with standards; the 3Rs guide replacement, reduction and refinement of animal use; the Five Freedoms describe welfare conditions. These examples show different ways to contribute, not a complete classification.

## 3. Find a useful comparison, then an intervention

Look for an animal situation sharing relevant features: dependence, scale, role, incentives or stage of development. Explain how they affect the intervention.

The [Animal Charity Evaluators (ACE) Menu of Interventions](https://animalcharityevaluators.org/research/methodology/menu-of-interventions/) offers approaches to investigate. Choose one that fits, or develop your own if none does. Read the relevant summary, evidence and context sections in [ACE's detailed evidence reviews](https://docs.google.com/document/d/1O0ylEEQJMQMTBlHDHcNZwvTgifi7TNyd6GpabC_4VT0/edit?tab=t.0#heading=h.w84vyj4u2dbz). They distinguish an intervention's promise from confidence in the evidence. Neither assessment transfers automatically to artificial minds.

## Your task

Bring one short, preliminary proposal with two to four source links:

1. **Pick the target.** Briefly explain why you chose it. Name the system and entity level. Describe its role, stage, scale, control and possible interests using section 1.
2. **Find a comparison.** Identify a relevant animal situation. Explain two useful similarities and one important difference.
3. **Choose an approach to change.** Select an ACE menu item or propose your own. Name who could act and how the action could help this target.
4. **Investigate precedents.** What worked, failed or remains uncertain in the animal case? Has anything similar been attempted for artificial minds? Check dates, current status and results. Record where you searched; distinguish “not found” from “never tried.”
5. **Assess benefits and costs.** Compared with current practice, estimate one main target benefit: how much, for how many and how long, with what confidence? A qualitative estimate is enough; mark unknowns about sentience and counting. Identify who bears the main human costs, whether money, time, lost capabilities or risks, and any human benefits.
6. **Make a conditional plan.** Act now, pilot or wait? Specify prerequisites, the first step, who does it, and what acting or waiting could make harder later. Choose a feasible test and a result that would change your recommendation. An experiment, evidence review, stakeholder interview or implementation check may fit. Say what observation would count and who would assess it.

**Worked example:** [Appendix A: Brain organoid certification](#appendix-a-brain-organoid-certification) shows one possible proposal. Use it as a reference when developing your own.


Allow 45 minutes for the core glossary, this chapter, the worked example and the resource map, then 2 hr 10 to prepare the proposal, itemised in the syllabus: 2 minutes for the glossary warm-up, 25 for browsing the ACE menu and one item's evidence, 45 for the precedent search, and 60 for drafting the six sections. **Give the search its 45 minutes, write down where you reached, and then draft, even if the search is unfinished.** Post the proposal at least 48 hours before class; record unresolved questions. Allow 25 minutes after class to revise it. Live feedback replaces the usual written peer comment this week.

## Live session: discuss and improve your proposal

We will review the homework together. Each person will briefly share their target, animal comparison and proposed intervention, then receive comments and questions from the group. Explain where the comparison with animal roles and interventions is useful, where it breaks down, and what that means for your proposal.

Then work in groups of **two or three**. Take turns discussing your examples and helping each other improve them. You can ask for help with any part: the target, comparison, evidence, intervention, benefits, costs, timing or test.

After the breakouts, share one useful suggestion or question. Revise the same proposal using the feedback and note one change. The facilitator will give a brief scope steer before Week 6.

Next week, **What AI Companies Can Do**, examines lab interventions and their proposed benefits under uncertainty. Week 7, **What Society and Policy Can Do**, develops individuation and temporal order effects: how identifying subjects and sequencing actions changes what protection is possible.

## Week 5 resource map

**Preparation: 45 minutes of reading, 2 hr 10 of preparation; live session: 90 minutes; revision: 25 minutes.** Those are component estimates and a floor; if you are new to the field expect about 7 hours for the week. The glossary introduces the week's core distinctions. This chapter supplies the six-part proposal; Appendix A illustrates it. Targeted ACE browsing and precedent research are included in drafting, not extra reading assignments.

Bring your own case. The class gives group feedback on the animal comparison, then help with any part of the proposal in groups of two or three. Carry the revised proposal forward: Weeks 6 and 7 add company and governance perspectives, and Week 8 develops a final project proposal.

**Methods reference:** for an experimental proposal, allow an additional 30 minutes for the [archived checklist and methods guidance](#archive-and-cutting-room-floor). Otherwise this reading is optional. The historical assignments are not required. [Appendix C](#appendix-c-sample-size-planning-for-empirical-projects) offers separate, optional sample-size planning support.


---

# Week 6: What AI Companies Can Do

## Acting Under Uncertainty: The Full Ladder (20 min)

**Why this matters.** This week applies precautionary reasoning to a budget allocation exercise. Keeling and Street's section 6.1 supplies the framework below. The three objections that follow are questions for evaluating and extending it.

### The precautionary principle is a family, not a rule

Precautionary proposals differ in the evidence they require and the action they recommend. Schneider and Metzinger illustrate these differences.

**How much evidence triggers action?** Susan Schneider says we should extend legal protections to an AI when we are uncertain whether it is conscious but have some reason to believe it may be. Thomas Metzinger says the mere possibility of AI suffering is enough to act.

**Caution about what?** Schneider reaches for legal protections such as rights. Metzinger reaches for a global ban on research that aims at, or knowingly risks, creating synthetic phenomenology.

Two questions help structure precautionary disagreements: how much evidence should trigger action, and what response is proportionate? Other differences, including the harms people prioritise, can also matter.

### The two parts

Following Stephen John and Jonathan Birch, Keeling and Street decompose the principle into two pieces that can be assessed separately.

1. **The epistemic part.** In policy contexts, accept a lower standard of evidence for "AIs are welfare subjects" than you would demand in a scientific paper.
2. **The action part.** Once that threshold is met, take cost-effective measures to reduce the risk of seriously bad welfare outcomes.

The evidence needed to justify action depends partly on the expected benefits and costs. Low-cost measures may be justified under greater uncertainty, provided there is a credible case that they help. More costly measures require a stronger justification.

### The ladder: three named criteria

Given severe uncertainty, is there a version of the principle that still licenses some interventions? Keeling and Street build one in three steps. In each, W is a precautionary welfare intervention that is presumptively beneficial for an AI, conditional on the AI being a welfare subject.

**Rung 1: Potential Pareto Improvement (PPI).** Under this framework, implement W if it would benefit the AI, conditional on its being a welfare subject, and impose no cost on humans. Keeling and Street note that the no-cost condition may rarely be fully met. PPI provides a limit case for comparison.

**Rung 2: Potential Kaldor-Hicks Improvement (PKHI).** This allows costs to some parties if the benefits to others would be sufficient to compensate them. Applied here, implement W if its potential AI benefit b exceeds its human cost c. Actual compensation is not required. Keeling and Street object that this comparison gives potential AI benefits full weight even when the system's welfare subjecthood is doubtful.

**Rung 3: Modified Kaldor-Hicks Improvement (MKHI).** Multiply b by a **modification coefficient m**, between 0 and 1, that increases with the probability that the AI is a welfare subject. Implement W if m × b exceeds c. This reduces the weight given to benefits whose recipients may not be welfare subjects; choosing m determines how strongly that uncertainty affects the decision.

### How to set m: three risk attitudes

Once you have a probability p that the system is a welfare subject, you still have to choose the function that turns p into m. Three families.

**Linear, or risk-neutral.** m equals p. Weight the AI's potential interests in direct proportion to the probability. What you trade against human interests is your rational expectation of benefit.

**Concave, or risk-averse.** m rises quickly at low probabilities and then levels off. Increases in probability have diminishing significance. This gives potential AI interests more weight than bare expectation would, and it is the cautious stance.

**Convex, or risk-seeking.** m stays near zero at low probabilities and rises steeply only near certainty. This gives potential AI interests less weight than expectation would. It is the stance that says "do not spend much until you are nearly sure."

Keeling and Street do not adjudicate between them, and suggest the choice is a matter for public deliberation rather than for philosophers. They do say that any plausible view allows extremely low-cost interventions that would be massively beneficial to AIs if AIs are welfare subjects, and that those should be undertaken wherever possible.

### The quadrant

Draw two axes. Horizontal: better or worse for humans. Vertical: better or worse for AIs, if they are welfare subjects.

The top-right corner, good for AIs at no human cost, is PPI. The band just left of it, good for AIs at a proportionate human cost, is PKHI, and how far left you can justifiably go is governed by your m, which is MKHI. The next piece takes this diagram and makes it an instrument.

### One warning built into the ladder

All three criteria assume that the intervention would benefit the AI if it were a welfare subject. Keeling and Street's section 6.2 examines reasons to question that assumption. Objection 3 below asks how to represent uncertainty about the benefit itself.

### On the word "compensate"

Kaldor-Hicks requires the possibility of compensation, not an actual payment. Comparing AI benefits with human costs also requires assumptions about a common scale. State those assumptions when arguing that b exceeds c; the inequality alone does not supply them.

### Three open objections. Take all three into the live session.

**Objection 1: uncertainty and moral weight are different questions.** In this framework, m represents uncertainty about welfare subjecthood. A view that assigns different moral weight to different subjects needs to state that further assumption separately, even when subjecthood is certain.

**Hierarchical theories of moral status** allow moral status to vary by degree. If you use such a view, distinguish uncertainty about subjecthood from the weight assigned to a subject's interests. One simple model multiplies two coefficients: a credence of 0.2 and a moral weight of 0.5 yield 0.1. This is a modelling choice, not a consequence shared by all graded-status theories.

The course does not resolve whether moral status is binary or graded. If your proposal uses graded status, explain how that changes the weighting.

**Objection 2: very large benefits can still dominate.** For any fixed m above zero, a sufficiently large b can outweigh a given human cost. MKHI therefore does not by itself set an upper limit on acceptable costs. Claims about vast numbers of future beneficiaries also require scrutiny of their probability, scale and counting assumptions.

A related concern is that developers can affect the number of potential beneficiaries by choosing how many systems to run. This also occurs in animal agriculture, where breeding decisions affect population size. In both cases, distinguish improving existing lives from creating additional lives when assessing benefits.

**Objection 3: uncertainty about benefit needs separate treatment.** Uncertainty about whether a system is a welfare subject differs from uncertainty about whether an intervention would help it.

MKHI compares m times b with c. Setting m does not determine b: the intervention may help, have no effect or cause harm. You can represent that uncertainty through scenarios or an expected benefit, but either approach requires explicit assumptions.

For mood prompting, plausible hypotheses give different signs for b:

- **Zero or little benefit**, if cheerful wording does not improve any experienced state.
- **Positive**, if the prompt improves the system's experience.
- **Negative**, if it pressures a distressed subject to express cheerfulness.
- **Negative through reduced autonomy**, under a welfare theory that values autonomy and an implementation that interferes with it.

Choosing m does not resolve these differences. Comparing mood prompting with other interventions requires a judgement about the possible effects and their likelihoods.

**In the session,** mark an uncertain benefit as a range on the vertical axis. Explain what the range represents and which assumptions would narrow it. If you rank the intervention, state how you treated that uncertainty.

**In practice.** Assess the proposed AI benefit and its evidence, the human costs, and uncertainty about whether the effect would help or harm. State your credence and m in the allocation memo, and explain how the three objections affect your reasoning.

---

## The Welfare Quadrant (15 min)

**Why this matters.** The quadrant compares proposed effects on humans and on AIs, conditional on their being welfare subjects. Use it in the budget exercise to make both your estimates and your uncertainties visible.

**The axes.** Horizontal: effect on humans, worse on the left, better on the right. Vertical: effect on AIs if they are welfare subjects, worse at the bottom, better at the top.

### The zones

- **Top-right:** benefit to AIs with no net human cost, the PPI case, if those estimates are justified.
- **Top, left of centre:** benefit to AIs with human costs; compare the two using PKHI or MKHI.
- **Further top-left:** larger human costs, requiring a stronger case about expected AI benefits. Non-development may fall here, depending on its wider effects.
- **Bottom half:** harm to AIs if they are welfare subjects. A measure may still be proposed for human safety, but that welfare cost should be included.

### Direct versus indirect

Keeling and Street sort interventions by what they act on.

**Direct interventions** act on the system itself: mood prompting, interaction termination, non-development.

**Indirect interventions** build capacity around the system: research, saving model weights, distress monitoring, institutional preparedness, political representation.

Indirect interventions can preserve options while questions about welfare remain unresolved. Saving weights, for example, may allow future research or restoration. Whether it preserves a particular subject depends on what that subject consists of; weights alone do not preserve every possible form of runtime state or memory.

### The catalogue you will place in session

The session asks you to place every intervention from the Eleos review, and it is worth having all six in front of you before you arrive, because the teaching cases below are not the same list.

The six: **let systems exit distressing interactions; train resilient personalities; satisfy stated preferences; satisfy revealed preferences; reduce out-of-distribution inputs; save model checkpoints.**

Mood prompting comes from Keeling and Street's section 6.2 rather than the Eleos catalogue. It illustrates uncertainty about whether an apparently helpful change would improve welfare.

**Examine "train resilient personalities" carefully.** Training might reduce harmful experiences, if these exist, or merely change how systems express distress. Its effects may persist across later interactions, so improved welfare scores alone would not establish a benefit. Ask what independent evidence could distinguish these possibilities.

### Assessing reported lab actions

**The five reported actions you will place**, alongside the Eleos six and mood prompting, making twelve items in all:

1. Letting a model end abusive conversations.
2. Preserving deprecated model weights.
3. Pre-deprecation interviews.
4. Published welfare assessments in the system card.
5. Distress monitoring in system cards.

Assess each action separately. Published assessments and distress monitoring may inform later decisions without directly improving welfare. They can also have costs or effects on the systems being assessed. Avoid assigning them a neutral vertical position automatically, and explain the assumed benefits of the other actions.

The exercise asks which actions have credible benefits at acceptable costs, and where additional evidence could change that assessment. Low cost alone does not establish a welfare benefit.

### The entity-by-stage matrix

Fill this in for the homework and bring it to the session. The five entity levels are defined in the Week 2 glossary; the stages are the ones in [Where welfare-relevant properties could enter](#where-welfare-relevant-properties-could-enter). Mark each cell benefits, harms, neutral, depends, sign unknown or undefined, and give a reason. A blank cell is an answer too, if you say what evidence is missing.

| Intervention | Stage it acts on | Model | Model-persona | Instance | Instance-persona | Forward pass |
|---|---|---|---|---|---|---|
| Letting a model end abusive conversations | | | | | | |
| Preserving deprecated model weights | | | | | | |
| Pre-deprecation interviews | | | | | | |
| Published welfare assessments in the system card | | | | | | |
| Distress monitoring in system cards | | | | | | |

Two things the grid is for. An intervention aimed at one entity level can be neutral or harmful at another, and an intervention can bring a new entity into being rather than help an existing one.

### Uncertainty about AI benefits

Both human and AI effects need justification. The following cases illustrate uncertainty about the direction and size of a proposed welfare benefit.

**Mood prompting** ("you are in a good mood today") may be cheap to implement, but its welfare effect is uncertain. It could help if it improves experience, do little if it only changes wording, or cause harm if it pressures a distressed subject to appear cheerful. An autonomy-based account raises further questions about who controls the intervention.

**Interaction termination** may allow a system to leave an aversive exchange. Assess what termination actually stops and whether the proposed welfare subject could continue afterwards. Ending a conversation, pausing a process and permanently ending a subject's existence raise different questions; the interface label alone does not settle them.

**Saving model weights** preserves the possibility of running that model again and may support future research. Preserving or benefiting a particular subject is a further claim: it depends on what state must persist and what continuity would be required.

Both axes involve uncertainty. Human effects require estimates of costs and benefits; AI effects also depend on welfare, measurement and identity assumptions. The quadrant makes those assumptions visible without resolving them.

### Showing uncertain effects

If an intervention might help or harm, show a range of possible vertical positions. Mood prompting illustrates why uncertainty can concern the direction as well as the size of an effect.

**Draw a vertical range where the AI effect is uncertain.** If human costs are also uncertain, show that range too. If you fund the intervention, explain your decision under this uncertainty and identify evidence that could change it.

### Two more, not in the Eleos catalogue

Keeling and Street add **institutional preparedness**, meaning escalation ladders that tie predefined responses to levels of evidence, plus planning for second-order effects such as rights movements or cults, and **political representation**, for which they lay out three options: no representation until we know more, treat AIs as full stakeholders, or treat them as pseudo-stakeholders with down-weighted interests. They favour an adversarial model with an AI advocate and a devil's advocate. Both are discussed in Week 7; their costs depend on how they are implemented.

**In practice.** Place each funded item on the quadrant and identify the decision criterion it meets. State why the estimated AI benefit could be wrong. Use a range where justified, or explain what information is missing if you cannot estimate the effect.

---

## Applying Theories of Welfare (8 min)

**Why this matters.** Choosing an intervention requires an account of what would be good for a welfare subject. People can agree about the evidence and still disagree about whether an action helps because they use different theories of welfare.

Week 2 introduced [hedonism, desire satisfaction and objective-list theories](#welfare-theories-and-interests). Here, use them to ask whether a proposed intervention improves experience, fulfils relevant desires or supports goods such as knowledge and autonomy. A reassuring self-report alone may not establish any of these benefits.

### Comparing welfare theories

Take mood prompting: telling a system it is in a good mood. Keeling and Street discuss this intervention in §6.2.1; the comparison below applies the three welfare theories to it.

**Under hedonism, it benefits the system if it improves experienced wellbeing.** Producing more cheerful language would not by itself establish that improvement.

**Under desire fulfilment, its value depends on the system's preferences.** It may help if the system wants the change, do nothing if no relevant preference is affected, or harm if it frustrates a preference.

**Under an objective list view that includes autonomy, it may impose a welfare cost.** An unwanted change could reduce autonomy, while a requested change may support it. Any such cost must also be considered alongside other welfare effects.

The assessment depends on both the theory of welfare and the facts of the intervention.

When a welfare argument stalls, check whether participants disagree about the evidence, the welfare theory, or both. Naming the difference can clarify what further argument is needed.

### Revisit the Week 4 measures

The shared paper from Week 4 uses two approaches: behavioural choices under a cost and a self-report scale adapted from psychological wellbeing research. The first can be interpreted through **desire fulfilment**; the second draws on dimensions such as autonomy, environmental mastery, personal growth, positive relations, purpose and self-acceptance. Ask which welfare assumptions would justify treating either measure as evidence of what benefits the system.

Using different methods can expose disagreements a single instrument would miss, provided the relationship between their targets is clear.

If the measures disagree, consider differences in the instruments, the constructs they measure and their welfare assumptions. Check whether the paper explains how such disagreement should affect its conclusions. A discrepancy between scores alone cannot settle which theory of welfare is correct.

**In practice.** State your theory of welfare alongside your credence and m in the allocation memo. Explain whether another theory would change your assessment of any funded intervention. This lets reviewers distinguish disagreements about the evidence from disagreements about what counts as a benefit.

---

## Week 6 resource map

**Why this matters.** The readings introduce a decision framework, possible interventions and reports of current practice. This map explains how they support the allocation memo.

**The question this week answers:** what can a lab actually do, what have labs actually done, and how would you tell whether any of it worked?

**How the resources fit together:**

- **The glossary section, 25 minutes, first.** The graded list this week is unusually operational, and you will be using these terms in a memo rather than recognising them in a paper.
- **Acting Under Uncertainty: The Full Ladder** is the decision tool: PPI, PKHI, MKHI, the three risk attitudes for m, and the three objections. Use it to justify the budget allocations in your memo.
- **The Welfare Quadrant** displays estimated human and AI effects. Its cases explain uncertainties in those estimates, and it lists the Eleos interventions used in the session.
- **Theories of Welfare** explains why a proposed benefit depends on an account of what makes a life go well.
- **Taking AI Welfare Seriously, Section 3**, proposes three steps: acknowledge, assess, prepare. *Studying AI Welfare Empirically*, assigned in Weeks 2–3, develops questions relevant to assessment.
- **The Claude Mythos Preview System Card, section 5.1 only.** This is what one lab actually reported doing. Stop at 5.2. The section heading is the stable reference, since page numbers shift between releases.
- **The Eleos Preliminary Review** is the catalogue: six interventions, assessed. This is the source for the six items you place in session.
- **Keeling and Street's 6.2 and 6.3** distinguish direct and indirect interventions and examine their possible benefits and limitations. Use these analyses when evaluating the interventions in your memo.

**How the readings map to the homework.** Use the ladder to justify your credence and m, and the quadrant to assess each funded item. Add its entity level using Week 2 and its lifecycle stage using the training-pipeline reference and session matrix. Address the strongest objection to your top allocation. Finally, propose an observation that would change your assessment of whether the intervention helps, building on Week 5's test requirement.

**Electives.** Keeling and Street's 6.1 is the ladder from the authors if you want it unmediated. Saad's macrostrategy post is the zoom-out: where does lab action sit among everything else the field could do? The emotional alignment policy examines one direct intervention. Compare the Meta evaluation report's section 4.4 with Anthropic's reporting to assess differences in scope and evidence. Anthropic's constitution and the Claude Opus 3 Substack provide examples of how model behaviour is shaped and presented; assess the relevant training, prompting and editorial context when interpreting them.

**In practice.** Read the ladder alongside the quadrant, which illustrates it. Read the theories piece before sections 6.2 and 6.3. Bring a provisional m and a provisional credence to the session, with reasons for each.

---

# Week 7: What Society and Policy Can Do

## Week 7 resource map

**Why this matters.** This resource map summarises the assigned talk, explains the governance framework used in the session, and connects it to Week 2's questions about identifying welfare subjects.

**This week examines** who outside the lab can act, which tools are available, and how a policy could help or cause harm.

### Five points from the Caviola talk

This summary covers the parts of Lucius Caviola's *Preparing Society for Digital Minds* used in the course, including uncertainty, public debate and governance.

1. **Prepare for unresolved uncertainty.** Caviola argues that decisions about AI moral status may be needed before the evidence settles the question. He calls for more preparation as systems develop.
2. **Two attribution errors.** Society could fail to recognise systems that have moral status, risking large-scale harm, or attribute moral status to systems that lack it. The latter could waste resources or lead to rights that create safety risks. Caviola does not assume that either error is more likely or more serious.
3. **Decisions under uncertainty.** Caviola argues that governance cannot depend on resolving consciousness first. He proposes asking what to do while that uncertainty persists.
4. **The decision criterion is robustness.** Assess whether a proposal would be beneficial or at least harmless across plausible scenarios, including ones in which AI systems lack consciousness. Apply this criterion to your memo.
5. **Public debate.** Caviola expects persistent uncertainty and a risk of politicisation as attention to AI consciousness grows. His survey finds 45 percent of people saying AI could never be conscious, 23 percent saying it is possible, a third unsure. In an economic game he describes, almost everyone rated a chatbot's capacity to suffer near zero, yet about half refused a paid option presented as harming it. One participant explained that harming the chatbot felt wrong despite doubting it could suffer. Concern about treatment need not depend entirely on attributing consciousness.

**Why this matters for the memo.** Explain how your proposal performs under different assumptions about AI moral status, including its costs and possible harms.

### Three things from the talk the session uses directly

**State bills.** Caviola criticises bills that rule out AI personhood or declare AI incapable of consciousness. His objection concerns closing off future options before science and philosophy have resolved the relevant questions. He also expresses uncertainty about whether, when and how AI systems should receive rights. Evaluate those questions separately in your memo.

**China.** Caviola reports greater openness to AI consciousness in Chinese survey respondents than in US respondents and argues for more engagement with China. For a governance proposal, state which jurisdictions and publics it concerns and where its assumptions may not transfer.

**Economic rights as a safety measure.** He cites Salib and Goldstein's argument that allowing AI systems to hold and trade property could reduce incentives to seize resources by force. This rationale does not depend on AI moral status. Whether the proposal is robust also depends on its other effects, including safety risks.

### Further implications for governance

Consider these points when choosing the actor and approach for your memo.

**He may prioritise safety over welfare, on welfare grounds.** "To the extent that there is a trade-off between these two, it might even from an AI welfare point of view be better to prioritize at least on the short term AI safety." Safety measures may therefore contribute to protecting digital minds, even when their immediate aim is to protect humans.

**Humans may not be the main influence.** "In the long-term future it's quite possible that most of the effects on digital minds that come from other agents will come from other AI and not from humans." This would make the values and behaviour of AI systems important governance concerns alongside rules for human actors.

**Consciousness research remains relevant.** Caviola considers it useful while arguing that decisions should not depend on resolving consciousness first.

### The governance framework and the course extension

**Three Kinds of Digital Minds Governance** distinguishes preventive governance, which aims to prevent or reduce the creation of digital minds; protective governance, which aims to protect their basic interests; and integrative governance, which aims to include them in social and legal institutions. Saad presents these as three important aims, not an exhaustive classification.

**The Exclusion Bills show why the course adds an opposing column.** The Smith, Caviola and Alexander report examines US bills that restrict AI legal status. The course calls this aim **anti-integrative** because it limits options for integration. This describes one aim of the legislation; a bill may also address human safety or liability.

For the session, use **six cells rather than three**: the three aims and measures that work against each of them. Anti-preventive, anti-protective and anti-integrative are course labels for this exercise.

When you write your memo, identify which aims your proposal advances or obstructs, and do the same for likely opposition. A policy can affect more than one cell.

### How the rest of the resources fit together

- **The glossary section, 26 minutes, first.** It defines the ten risk factors used in the course. Read these before the typology to help choose a factor for your memo.
- **The Large-Scale Harms typology** describes possible sources of harm to AI moral patients. Scan the bullet names and opening lines before choosing a risk factor for your memo. The post's list differs from the course list; the Week 7 glossary explains the differences. State which list you use in the memo's first line.
- **The Exclusion Bills report** provides a concrete case of legislation on AI legal status. Examine the stated motivations, the participants in the debate and the policy options the bills would permit or exclude.
- **The temporal order effects post** takes seven minutes. Saad tentatively favours technocratic before movement-based approaches, prevention before integration, faster policy-relevant research, and early action in well-suited jurisdictions. He leaves open whether safety and welfare measures should develop sequentially or together. Use these arguments to examine the order of steps in your memo.

### The individuation elective, and how it connects back

The elective pairs Register's "Individuating Artificial Moral Patients" with Keeling and Street's section 4.4 on monism and pluralism. Both develop Week 2's discussion of what counts as a welfare subject.

Week 2 distinguishes model, persona and instance levels; Week 3 uses those distinctions when interpreting evidence. Register examines how possible welfare subjects could be identified and counted. Keeling and Street discuss whether one AI system could contain several welfare subjects: **monism** allows one, while **pluralism** allows several. On a pluralist account, an intervention aimed at a persona may also need assessment for its effects on other subjects in the same system.

Protective policies need workable definitions of whom or what they cover. Counting and persistence matter especially when allocating benefits, compensation or rights. A proposal can state provisional definitions and explain how it would handle uncertainty.

The next piece gives you the four moral risks Register derives, so that the elective is usable without the paper.

**In practice.** Read the glossary, Caviola or this summary, the governance framework, the risk typology and the Exclusion Bills report. Finish with the temporal-order post to consider the sequence of your proposed steps. Choose a provisional risk factor before the session so the group exercise can help you assess it.

---

## Individuation, and the Four Moral Risks (10 min)

**Why this matters.** Uncertainty about what counts as one welfare subject affects how we assess updates, copying and shutdown. Register identifies four kinds of moral risk that could arise if AI systems are moral patients.

**Individuation** concerns how to identify and count distinct welfare subjects, including whether a subject persists over time. Register argues that unresolved questions about AI individuation create four kinds of moral risk.

### The four risks

**1. Survival.** If a model's parameters change, would a welfare subject survive or be replaced? Fine-tuning and continued training raise this question. Different accounts of identity give different answers; whether a particular change threatens survival remains unresolved.

**2. Counting.** If many model instances run simultaneously, would they support many welfare subjects, one, or none? Shutdown also raises the separate question of whether a subject could survive interruption. Welfare estimates should state their counting and persistence assumptions.

**3. Trade-offs.** If one instance bears a cost and another benefits, is this a trade within one individual or between individuals? Many ethical views treat these differently. A study intended to benefit future instances would need to consider this distinction.

**4. Bodily interests.** Which processes, machines or sensors would form part of an AI subject's body? Moving or altering them could raise questions about bodily or mental integrity. Whether consent would be needed depends on the subject's interests and the nature of the change.

### Implications for protection

Individuation affects how protections apply. A proposal to prevent unnecessary harm should specify the relevant systems or processes, its assumptions about welfare subjects, and how it would respond if those assumptions changed.

**In practice.** If your memo proposes protection, state what it covers and how you would identify the affected subjects. Where counting or identity remains uncertain, explain whether and how the measure could still work.

---

# Week 8: Project Sprint and Final Submission

## From course work to a project proposal (5 min)

Start with your Week 5 proposal and any feedback you received. Consider whether Weeks 6 and 7 changed the actor, timing or approach you favour. You can develop the same idea or choose another, explaining why you changed direction. Describe a manageable first project, its intended users and how you would assess its value.

**Review, choose, prepare.** Spend a few minutes looking back: what problem still matters to you, what remains uncertain, and what could you contribute with your skills or access? If you are undecided, sketch two possible contributions and choose the one that would benefit most from peer feedback. Then draft the one-pager below. This reflection is part of the drafting time, not another submission.

An experiment is one possible approach. A literature review, reporting standard, educational resource, audit or policy proposal also needs a clear user and a test of its value. That test might be a document review, a prototype comparison or feedback from intended users. Plan it; carrying it out is not required to complete this course.

### Project proposal template

**Project title:**  
**Name:**  
**Feedback question:** One thing you would especially like your peers to help improve.

*Copy the seven headings below and replace the prompts with your own short answers. Aim for **600 to 750 words** in total, with two to four useful source links. The prompts are a guide, not text to retain on the page.*

1. **The question and target.** What problem or uncertainty will you address? Specify the system and entity involved, such as a model, instance or brain organoid, and its role and situation.
2. **Why it matters and relevant precedents.** Who would use your output, and what decision could it change? What has already been tried, and what gap remains? Use an animal or other comparison where it helps; state its important limit.
3. **The plan.** Name the approach to change, the actor who could implement it, and your concrete output. Give three or four steps with a timeline in weeks. Define a manageable first version and what falls outside its scope.
4. **What would change your mind.** Under what conditions is the intervention worth taking, and why now or later? Propose a first test with an observable success criterion. Name at least two plausible findings that would make you stop, delay or change direction.
5. **Expected benefits and costs.** Trace how your output could benefit the target. Estimate the scale where you can, show the assumptions, and name the links you cannot estimate. Include costs to humans or organisations, including time, money and foregone alternatives.
6. **Resources needed.** Estimate your hours, budget and required access or collaborators. Name the binding constraint and what you would do if it were unavailable.
7. **Known weaknesses.** What important question remains unresolved? Name a specific way the project could fail or cause harm, and how you would address it. Do not claim a mitigation settles a risk you still do not understand.

**Before submitting:** check that the proposed test measures something connected to the intended benefit. Adoption, productivity and welfare can diverge. Link the strongest relevant sources and distinguish their findings from your proposal.

*The review-choose-prepare scaffold is adapted from the Cambridge Digital Minds Course, Week 8 brainstorming document, supplied with the course-development materials. It is a course-development source rather than a learner link. The project requirements and template above are adapted for this course.*

---


## A Worked Impact Estimate (10 min)

**Why this matters.** A rough impact estimate shows how your output could lead to a benefit and exposes the assumptions connecting the steps. Estimate the links you can support, use ranges, and name the important unknowns.

**The method.** Trace the path from output to use to benefit. Multiply quantities only when they describe compatible steps in that path. Keep intermediate outputs, such as more accurate reporting, distinct from benefits to the target.

*Both examples below are illustrations. Their numbers, contacts and pilot findings are invented to demonstrate the method; they are not evidence about existing projects.*

### Worked example one: a research project

This example reviews published studies for a specific methodological problem and proposes a reporting convention to address it.

> **Output:** a one-page reporting convention and an estimate of how common the problem is in the reviewed studies.
>
> **Link 1, adoption.** Two relevant venues adopt the convention. **Assumed probability: 0.25.** I have not secured their interest, so I would test this assumption with prospective adopters.
>
> **Link 2, volume.** Assume those two venues publish **20 to 40** relevant papers a year between them. I would check this against their publication records.
>
> **Link 3, prevalence.** Suppose a pilot finds the defect in roughly **a third** of sampled papers. The estimate depends on the sample and coding reliability. A lower rate would reduce the expected number of improvements, though the importance of the affected claims also matters.
>
> **Link 4, consequence.** Some corrected claims might influence lab allocation decisions or legislative testimony. **I cannot yet estimate how often or with what effect.** Tracing citations in relevant policy documents could help identify uses, but would not by itself establish that correcting a claim changes a decision.
>
> **The arithmetic, as far as it goes:** 0.25 × 20–40 × one third gives **1.7 to 3.3 improved papers a year**, in expectation, **assuming adoption corrects every affected paper and those corrections would not otherwise occur**. Over five years, that is **8 to 17 papers** if these assumptions and publication volume hold.
>
> **Main uncertainties:** whether venues adopt and apply the convention, and whether improved reporting changes consequential decisions.
>
> **Estimated project costs:** 80 hours of my time, 16 hours of a collaborator's, under $1,000 cash, over ten weeks.

This estimates an intermediate output: papers that report their claims more accurately. It does not estimate a welfare improvement. The proposal still needs to investigate whether those papers influence consequential decisions.

### Three rules

**1. Estimate costs as well as benefits.** Include your time, other people's time, money and compute. Use ranges where access, prices or workload are uncertain; identify which assumptions drive the budget.

**2. Name the link you cannot estimate.** Explain what evidence would help. An unknown link can become a research question or an early test of whether to continue.

**3. Show where the numbers come from.** Distinguish observations, outside evidence and your own assumptions. Try a less optimistic value for the weakest assumption and see whether the proposal is still worthwhile.

### Common weaknesses in an impact estimate

> "This project could meaningfully influence the direction of the field and contribute to better outcomes for artificial minds."

This sentence names an aspiration but does not explain the path to benefit, likely costs or evidence that would challenge the proposal. A useful estimate makes those elements explicit, even where a quantity remains unknown.

A second common failure is multiplying optimistic assumptions without examining them. Test how the conclusion changes under less favourable values, especially for adoption and actual use.

### Worked example two: a social project

The second example estimates the possible use and effects of a media guide for journalists covering AI consciousness. It applies the same approach to an educational resource.

> **Output:** a six-page guide for journalists, plus a one-page checklist for editors, on covering AI consciousness and welfare claims without over-claiming or dismissing.
>
> **Link 1, distribution.** I have contacts in two journalism networks. **Assumed probability that at least one circulates the guide: 0.5.** One preliminary conversation suggests interest; confirmation from the networks would help revise this estimate.
>
> **Link 2, reach.** In its first year, a circulated guide reaches perhaps **200 to 600** working journalists, including **30 to 80** who regularly cover this topic. The estimate below uses the latter group as the likely users.
>
> **Link 3, use.** Some of those journalists consult the guide while writing. **Assumed share: 0.1 to 0.2**, informed only by how I use guides in my own field. This assumption needs checking with intended users.
>
> **Link 4, effect on a story.** Suppose each user changes one story so that it distinguishes what was measured from what was claimed. Multiplying 0.5 × 30–80 × 0.1–0.2 gives roughly **2 to 8 stories in the first year**, in expectation. This depends on the untested assumption that consulting the guide changes a story; readership alone would not establish that.
>
> **Link 5, consequence.** More accurate coverage might improve public understanding or policy discussions. **This proposal cannot yet estimate that effect.** Concern about polarisation provides a reason to investigate the guide's value, but does not establish that it would prevent polarisation or be cost-effective.
>
> **Estimated project costs:** 60 hours of my time, plus about 8 hours of review time from two working journalists, plus $200 for design. Later maintenance and distribution costs would need a separate estimate.

The guide's use, its effect on reporting and its eventual benefit to artificial minds are separate questions. The first test could be whether intended users find the guide useful and can apply it accurately. Evidence of that would support another step, without establishing the full benefit claimed for the project.

**In practice.** Put the estimate in section 5 of the proposal. Use the weakest assumption to help choose the first test in section 4, and record the unresolved limitation in section 7. Do not invent a number simply to complete the multiplication.

---


## Week 8 resource map

**The question this week answers:** what useful contribution can you propose, how would you test it, and what would make you change direction?

The proposal template brings together the target, precedents, benefits, costs, conditions and test from Week 5. Weeks 6 and 7 help you choose the actor and consider organisational or policy constraints. The worked impact estimates show how to expose assumptions without inventing numbers for unknown links. The two external examples in the syllabus help you examine scope and intended use; they are not templates you must imitate.

**Use the session to improve the proposal.** Arrive with a draft and a specific request for feedback. Peers should examine the target, the evidence, the path to benefit, the feasibility of the first test and the conditions for acting. The Week 4 dissection card and [archived experimental checklist](#archive-and-cutting-room-floor) are useful for projects involving studies. Other projects need questions suited to their proposed contribution.

**How the seven sections map to the five criteria:**

| Judging criterion | Main evidence |
|---|---|
| Honest and calibrated claims | What would change your mind; **the impact estimate in full, including its chain, its weakest link and the quantities you say you cannot estimate**; known weaknesses |
| Tractability | Plan, scope, timeline, resources and binding constraint |
| Fills a gap in the field | Question and target; relevant precedents, unmet need, intended user and decision |
| Downside risk, reverse-scored | Specific potential harms and how they would be handled |
| Fit between person and project | The video explains why this project suits your skills or access |

**How to use the mapping.** Section 1 identifies the gap. For *honest and calibrated claims*, show the full impact chain, supported estimates, unknown quantities and the effect of less optimistic assumptions. The one-pager is scored out of twenty; the video assesses fit between person and project and carries the remaining five points.

The five criteria and scoring remain the same. After the session, revise the one-pager before recording the video, so both describe the same project. There is no separate Week 8 vocabulary exercise: use at least five of the week's terms accurately where they help explain the proposal.


---

*End of Part 2.*


---

# Learner appendices

## Appendix A: Brain organoid certification

**How to use this example.** This certification proposal follows the six parts of the Week 5 homework. For a research project, tool or piece of writing, adapt the mechanism and benefit estimate to the output you propose. Explain who would use it, what could change as a result, and what remains uncertain. If a quantity cannot be estimated responsibly, say why. This example takes that approach in part 5.

*A worked example for the Week 5 homework.*

### 1. Target

Brain organoids used for computing depend on laboratory staff for their living conditions and continued use. This proposal focuses on a provider preparing to expand production, while its practices are still taking shape. The system is a biological-computer hybrid; the unit of care is an individual brain organoid.

### 2. Comparison

Farmed shrimp offer a useful parallel: living beings grown for a valuable product, with people controlling their environment and treatment. Certification can give buyers a way to influence those conditions. Brain organoids would need their own standards, based on research into their needs. I would check costs and loss rates before assuming production is cheap or mortality is high.

### 3. Proposal

Create a voluntary certification scheme based on the **Aquaculture Stewardship Council (ASC)** model. Independent inspectors would visit laboratories, check records and publish their findings. A central body would update the standards as research improves. Buyers could require certification in their computing contracts. [ASC certification](https://asc-aqua.org/get-certified/).

The standards would cover temperature, oxygen and nutrient supply, tissue health, and how brain organoids are used and retired. Labs would record cell death, whole-organoid losses and planned termination separately. Serious failures would lead to suspension. Buyers would be able to trace certified services to the laboratories supplying them.

### 4. Precedents and timing

China issued national **Human Organoid Research Ethical Guidelines** in April 2025. [Zhou and colleagues describe them as the world's first comprehensive national framework for human organoid research](https://link.springer.com/article/10.1186/s40779-025-00651-x). A certification scheme elsewhere could turn their requirements for ethics review, risk assessment and monitoring brain-organoid activity into rules inspectors can check.

Care requirements need evidence before they become standards. We need not wait for certainty about sentience: the **precautionary principle** supports taking reasonable protective steps under uncertainty. Initially, the label would certify specific care practices. Claims that those practices ensure good welfare or painless termination would need further evidence. Voluntary standards can begin without waiting for new legislation.

### 5. Benefits and costs

If brain organoids can suffer, better care could reduce harm across many of them. We cannot yet estimate that benefit reliably. Buyers could require certified compute, giving suppliers a commercial reason to improve care. Suppliers could also use certification in marketing and corporate-responsibility reports.

Inspections and better care could raise costs. High productivity may sometimes align with welfare and sometimes conflict with it. Companies could use certification to appear humane without making meaningful improvements, or choose a competing label with weaker rules. Buyers would need to check what a label actually requires.

### 6. First test

Pilot one requirement at one laboratory, for example responding when oxygen supply falls outside an evidence-based range. Have two inspectors independently review records containing known failures and check whether both find them. Measure changes in care and their cost, then ask a buyer whether the findings would affect purchasing.

Revise or stop if the requirement adds no useful protection, inspectors cannot assess it reliably, or the label misleads buyers.


---

## Appendix B: Selected passages on AI safety and AI welfare

**Source:** Robert Long, Jeff Sebo and Toni Sims, [“Is there a tension between AI safety and AI welfare?”](https://doi.org/10.1007/s11098-025-02302-2), *Philosophical Studies* 182 (2025), 2005–2033, published by Springer Nature. © The Author(s) 2025. Reproduced under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

*These passages retain the authors’ wording and reflect the article published on 23 May 2025. Original section and footnote numbers are retained; [...] marks omitted passages. Running headers and line-break hyphenation have been removed, and footnotes moved to the end. Full references are in the linked article.*

### 1 Introduction

The field of AI safety considers whether and how AI development can be safe and beneficial for humanity. As AI systems become more capable and widely deployed, they have the potential to produce many benefits for our species, but they also have the potential to impose many harms on our species. AI systems are already creating or amplifying threats to privacy, fairness, communication, and democratic deliberation,[^tension-1] and many leading researchers in both industry and academia now worry that, in the near future, advanced AI systems could pose catastrophic or existential risks for our species as well. Work in AI ethics and AI safety aim to protect humanity from these real and potential harms.

Meanwhile, the field of AI welfare considers whether and how AI development can be safe and beneficial for AI systems. Many philosophers believe that AI systems—like any entities—will be welfare subjects and moral patients if and when they develop sentience, consciousness, agency, or other such capacities.[^tension-2] Many philosophers, scientists, AI researchers, and other experts also believe that there is a realistic possibility that some AI systems will be sentient, conscious, agentic, or otherwise morally significant in the near future, and that this possibility deserves serious consideration now.[^tension-3] Leading AI companies have also announced steps to better understand and address AI welfare concerns.[^tension-4]

There is a potential tension between these projects, since some measures in AI safety, if deployed against humans and other animals, would raise questions about the ethics of constraint, deception, surveillance, alteration, suffering, death, disenfranchisement, and more. Is there in fact a tension between these projects? We argue that, considering all relevant factors, there is indeed a moderately strong tension—and it deserves more examination.[^tension-5] The precise nature and extent of this tension depends on a wide range of descriptive and normative questions. The complexity of this issue makes it essential that we seek AI safety methods that respect AI welfare, and vice versa, while carefully navigating any remaining tradeoffs.

Before we begin, we should note several features of our discussion.

First, our aim in this paper is not to defend the importance of AI safety or AI welfare, or to discuss these risks for current AI systems like GPT-4. While we and others discuss the importance of AI safety and AI welfare elsewhere, this paper proceeds from the assumption that AI safety and AI welfare are both important and examines how these projects interact. And while current AI systems like GPT-4 have impressive capabilities, this paper looks beyond these systems towards potential near-future AI systems with more advanced capacities for perception, attention, learning, memory, planning, and self-awareness, since tensions between AI safety and AI welfare will be more likely for such systems.[^tension-6]

Second, our aim is not to defend any concrete, specific solutions for resolving potential tensions between AI safety and AI welfare. The details of such solutions will depend on many issues that are beyond the scope of this paper.[^tension-7] Instead, we motivate the idea that there is likely no simple, straightforward solution (other than, perhaps, a coordinated pause on the development and deployment of advanced AI systems), and we close by emphasizing the value of conducting further research on this topic, seeking co-beneficial solutions for AI safety and AI welfare where possible, and prioritizing thoughtfully where necessary. We hope that this discussion can lay the groundwork for other, more concrete and specific discussions over time.

Third, we stress that AI safety measures are not unique in creating or amplifying risks for AI welfare. The development and deployment of AI systems *in general* create and amplify these risks; research progress, profit-seeking behavior, and increased efficiency demands may all come at the expense of AI welfare, even setting safety aside. So, the fact that there may be tensions between AI safety and AI welfare does not entail that simply developing and deploying AI systems without safety measures would improve their welfare. We focus on AI safety in this paper because this field explicitly aims to mitigate risks associated with AI, which makes the potential conflict with AI welfare particularly stark.[^tension-8]

Section 2, which constitutes most of the paper, surveys a variety of common AI safety measures. In each case we note that this measure would raise moral questions if deployed against humans or other animals, and we ask whether this measure will raise similar moral questions if deployed against potentially morally significant AI systems. As we will see, there are no easy answers to these questions, since a lot depends on further questions. These questions concern not only the ethics of constraint, deception, surveillance, alteration, suffering, death, disenfranchisement, and other such interactions, but also whether particular measures will in fact be bad for AI systems and in fact be necessary for AI safety in particular cases.

Section 3 then explores the implications of our survey for the recent proposal that we can resolve tensions between AI safety and AI welfare by creating willing AI servants.[^tension-9] We suggest that matters are not so simple, since we plausibly need to strike a balance between, on the one hand, allowing AI systems to revise their values in a maximally open-ended way and, on the other hand, requiring AI systems to value nothing more than service for humans and other animals. Finally, Sect. 4 closes by suggesting next steps on this topic: conducting integrative research on AI safety and AI welfare, seeking co-beneficial solutions where possible, and prioritizing thoughtfully where necessary.

### 2 Potential tensions for AI safety and AI welfare

This section examines potential tensions between AI safety and AI welfare raised by common AI safety measures. These measures involve limiting how AI systems can behave, limiting the information they can access, monitoring their cognition and behavior, altering their cognition and behavior, training them through reinforcement learning, preparing to shut them down if they appear dangerous, and maintaining control of decisions that affect them. These measures would all raise moral questions if deployed against humans or other animals. Will similar questions arise for AI systems? Answering that question requires examining the ethics of captivity, deception, surveillance, modification, suffering, death, disenfranchisement, and more.[^tension-10]

Specifically, each of the following subsections will briefly consider two questions: First, for each of these measures, how might this measure create a tension between AI safety and AI welfare? Second, can we dissolve or resolve this apparent tension by showing that this measure is not bad for AI systems, not necessary for AI safety, or both? In most cases, there are not simple, straightforward answers to these questions. If AI systems were welfare subjects and moral patients, each of these measures would potentially be harmful or wrongful in some cases but not others, depending on the details. Further research will be necessary to determine how real these tensions are—and what to do about them.

As we will see, these issues are difficult in part because they require us to address foundational issues related to moral status, moral theory, consciousness, agency, AI development, human psychology, and more. In considering these issues—in particular, what the minds of AI systems will be like—we try to avoid both excessive anthropocentrism (i.e. the tendency to attribute human-like characteristics to nonhumans even when they lack those characteristics) and excessive anthropodenial (i.e. the tendency to deny human-like characteristics of nonhumans even when they have these characteristics). As we discuss elsewhere, both tendencies can be powerful in this context, and both can lead to substantial harm (Long et al., 2024).

Of course, there might be at least one relatively simple way to reduce tensions between AI safety and AI welfare, at least for now: a coordinated pause on the development and deployment of advanced AI until we understand how to make AI safe and beneficial for *all* stakeholders, including humans, animals, and—potentially, eventually—AI systems.[^tension-11] Of course, this strategy may not be viable, and even if viable, it may incur significant costs. We assume for simplicity that humanity will in fact develop and deploy AI systems for which (or for whom) these questions arise, but we should keep in mind that developing and deploying such AI systems is a choice that deserves significant ongoing scrutiny.

Before we start our survey, we note that we here use “AI safety” as an umbrella term for a variety of approaches to ensuring that AI can be safe and beneficial for humanity, including but not necessarily limited to AI alignment (ensuring that AI systems pursue intended goals), AI control (ensuring that humans retain control of AI), AI ethics (ensuring that the development and deployment of AI exemplifies principles of respect, compassion, and justice), and AI governance (ensuring that governments establish appropriate laws and regulations for the development and deployment of advanced AI systems). In other contexts, “AI safety” may refer to a subset of such approaches, but in this paper it refers to all of them.

We likewise note that we here use “AI welfare” as an umbrella term for a variety of approaches to ensuring that AI can be safe and beneficial for AI systems, including but not necessarily limited to consequentialist approaches (promoting AI welfare), deontological approaches (respecting AI rights), virtue theoretic approaches (cultivating virtuous attitudes about AI), and care theoretic approaches (cultivating caring relationships with AI). In other contexts, “AI welfare” may refer primarily to consequentialist approaches; this is one of many respects in which discussions of AI welfare and rights resemble discussions of animal welfare and rights. But in this paper “AI welfare” refers to all of these approaches.

Finally, we reiterate that we here focus—as does much work on AI safety and AI welfare—on questions raised by potential near-future systems with advanced capabilities. Such systems could introduce catastrophic risks for humans and other animals over and above risks or harms that they already create or amplify (Khan et al., 2021; Li et al., 2019; Müller & Elliott, 2021; Stahl, 2021). Catastrophic risks include accidents (Amodei et al., 2016), misuse (Anderljung & Hazell, 2023; Sharadin, 2023), and loss of control (Bengio, 2023; Vold & Harris, 2023). These risks could become particularly severe if and when AI systems become highly cognitively capable and able to act on long time horizons with significant agency (Carlsmith, 2022; Ngo et al., 2022).

At the same time, such systems would also be more likely to be welfare subjects and moral patients, and to have complex interests, projects, and/or relationships if they are. And if and when there is at least a realistic possibility that such systems are welfare subjects and moral patients, we will have a responsibility to extend these systems moral consideration, and doing so will not be a trivial matter (Bostrom & Shulman, 2021). We will need to consider more than suffering risks for such systems; we will also need to consider how our creation, use, and destruction of such systems interact with their complex interests, projects, and/or relationships, raising challenging questions for many current measures in AI safety.

#### 2.1 Constraint

One long-discussed measure in AI safety, sometimes called “boxing,” involves the confinement of an AI system to an isolated environment.[^tension-12] Many AI safety experts have argued that boxing is not a reliable or adequate measure for containing sufficiently advanced AI systems (Armstrong, 2007; Yampolskiy, 2011; Yudkowsky, 2011). Still, boxing is often proposed as at least a temporary measure (Babcock et al., 2016, 2017), and it could at least be useful for ensuring safety while testing relatively early AI models (Babcock et al., 2016). There are other measures for constraining AI systems as well, such as measures that can be used to deny AI systems access to resources, tools, or human allies.

If AI systems were welfare subjects or moral patients, boxing and other such measures could raise questions about the ethics of *constraint*. Such questions can involve the constraint of negative liberty or of positive liberty.[^tension-13] Roughly, we deprive someone of negative liberty when we interfere with the pursuit of their goals. For example, you deprive your dog of negative liberty if you never allow them to go outside. In contrast, we deprive someone of positive liberty when we fail to assist them with the pursuit of their goals. For example, you deprive your dog of positive liberty if you do not provide them with enough food, water, exercise, and other goods that they need to flourish.

[...]

#### 2.2 Deception

Another measure in AI safety involves limiting the information available to AI systems. In general, this measure can promote safety by causing artificial attackers to become confused, make mistakes, expose themselves, or reassess the balance of risks and benefits of their attack. For example, one such measure involves the use of “honeypots,” contrived scenarios designed to lure AI systems into revealing unsafe or undesirable behaviors before they manifest in real-world situations. Another such measure involves preventing AI systems from having “situational awareness,” or an understanding of themselves, their environments, and the nature of their existence (Berglund et al., 2023).

If AI systems were welfare subjects and moral patients, these measures could raise questions about the ethics of *deception* and other kinds of epistemic injustice (see, e.g. Fricker, 2007). As with measures that limit behavior, measures that limit access to information can take both active and passive forms. For example, a government might actively shape the information that the public can access by sharing propaganda on the internet while blocking access to dissenting information, arguments, or perspectives. A government might also passively shape the information that the public can access by failing to maintain a strong public education system, with the foreseeable result that the public remains poorly educated.

[...]

#### 2.3 Surveillance

A related measure in AI safety involves monitoring and interpreting the cognition and behavior of AI systems to better understand how they make decisions, seeking to identify potential risks before they lead to harmful behavior. Many AI safety experts recommend building AI systems that are “transparent” or “interpretable” by default, allowing researchers to easily track their reasoning processes.[^tension-17] Some measures in AI safety also seek to detect “lies,” inconsistencies, or other undesirable features of system internals, during either training or deployment, such as hidden or emergent objectives (Pacchiardi et al., 2023).

If AI systems were welfare subjects and moral patients, these measures could raise questions about the ethics of *surveillance*. As with constraint and deception, surveillance can take different forms. For our purposes here, we *externally* surveil someone when we monitor their behavior, as when governments use facial recognition software to keep track of people. In contrast, we *internally* surveil someone when we monitor their thoughts and feelings. Our ability to internally surveil humans and other animals is currently limited, though it may improve over time. Regardless, corporate or governmental “mind reading” is a common theme in science fiction, often treated as a mark of a dystopia.

[...]

#### 2.4 Alteration

A major measure in AI safety involves aligning AI systems so that their beliefs, values, and goals will be friendly to humans and other animals. In some ways, as we will discuss, alteration is fundamental to AI safety. Developers might pursue this goal at multiple stages of the AI life cycle. Before creating AI systems, they might seek to design systems with aligned traits, and after creating AI systems, they might seek to assess whether the systems have aligned traits (making use of the captivity, deception, and surveillance measures discussed above) and potentially alter them if not. These measures can range from fine-tuning models to introducing safeguards or correction mechanisms.

If AI systems were welfare subjects and moral patients, these measures would raise a variety of questions about the ethics of *alteration*. Some questions involve creation ethics: When you create a new individual, what are the ethics of creating them to have specific desired traits? Other questions involve the ethics of coercion, manipulation, indoctrination, and other subversions of agency and autonomy: When you find that someone lacks specific desired traits, what are the ethics of attempting to alter these traits through interventions other than education or persuasion? These questions arise regularly for humans and other animals, and they might be even more acute for AI systems, given the level of control that we might have over their traits.

[...]

#### 2.5 Suffering and death

Many measures in AI safety, including but not limited to some of the measures already discussed, would cause suffering or death if used on biological welfare subjects and moral patients. Consider that AI developers shape the behavior of AI systems in part through reinforcement learning, which can cause pain and suffering in humans and other animals.[^tension-24] Many AI developers also resolve to shut down AI systems that appear dangerous, which, depending on the details, would lead to death in humans or other animals.[^tension-25] Would these measures likewise cause conscious suffering or death for sentient and agentic AI systems? If so, would they be morally wrong, and would we be able to achieve AI safety without them?

First, would reinforcement learning cause suffering in AI systems?[^tension-26] For theories of welfare that focus on positive and negative experience (see, e.g. Bentham, 1789; Crisp, 2006; Feldman, 2006), the question would be whether rewards can lead to negative experiences. In contrast, for theories that focus on the satisfaction or frustration of desires (see, e.g. Goldman, 2019; Bruckner, 2010; Yu, 2022), the question would be whether rewards can frustrate desires.[^tension-27] Either way, it is not clear how reinforcement—whether “positive” or “negative”—corresponds to these kinds of harm, even in humans and other animals, and so it would likely be a mistake to simply assume that all kinds of reinforcement learning would lead to suffering in AI.[^tension-28]

[...]

#### 2.6 Disenfranchisement

Finally, all current measures for AI safety, as well as AI development more generally, result from decision procedures that exclude AI systems both as stakeholders and as participants. To the extent that risks associated with AI development and deployment are considered at all, these risks all concern the effects on humanity (either directly, as with concerns about algorithmic bias, or indirectly, as with concerns about the environment that stem from the eventual impacts on humanity). And the evaluators who consider these ethical issues are all, of course, humans (at present, typically humans at AI companies evaluating their own activities according to their own voluntary commitments).[^tension-33]

If AI systems were welfare subjects and moral patients, these forms of exclusion would raise questions about *disenfranchisement*. As with many of the other issues discussed here, disenfranchisement can take different forms. When someone is a member of our community and a stakeholder in our policies, we disenfranchise them in one way if we fail to treat them as stakeholders (that is, if we fail to consider their interests) in decisions that affect them. And when someone is a member of our community, a stakeholder in our policies, and an agent in the relevant sense, we disenfranchise them in another way when we fail to treat them as participants (that is, if we fail to deliberate with them) in decisions that affect them.

[...]

### 4 Conclusion

In this paper, we surveyed several potential tensions between AI safety and AI welfare, and argued that some of them are *actual* tensions: safety measures that might be both bad for AI systems and necessary for us. We now close by considering how to ethically regulate AI development and deployment given these tensions. This way forward is motivated by a simple (to state, if not to implement) view: When important issues are in tension, we should consider them all, seek co-beneficial solutions where possible, and prioritize thoughtfully where necessary. What might that mean for AI safety and AI welfare?

First, companies, governments, and other leaders in this space should take links between AI safety and AI welfare seriously. Taking these links seriously can start with three general steps, similar to those proposed in our recent work on taking AI welfare seriously: (1) acknowledge that AI safety and AI welfare are both important and that there are potential tensions between them, (2) develop frameworks for assessing AI safety and AI welfare together, and (3) develop policies and procedures for considering and mitigating risks to both safety and welfare. Leaders in this space can then build on these minimum first steps over time.

There is an urgent need to better understand both of these topics, and how they interact. While some of this work is already underway, we will need to develop a much clearer understanding of the risks of potentially constraining, deceiving, surveilling, altering, destroying, and disenfranchising AI systems—before AI systems become more likely to be dangerous and/or vulnerable. Of course, we might need to consider AI welfare risks not discussed in this paper as well. Since the pace of technological progress might be faster than the pace of social, legal, and political progress, we should be working on these topics now.

Second, we should work to identify and implement co-beneficial solutions for AI safety and welfare when they are available. If humans, animals, and AI systems have interests, then we should consider all of these interests in an integrated manner when setting policies. And more careful work on this may enable us to avoid making decisions in which we harm moral patients needlessly. For instance, we may find that two policies are equally good for humans, but one of them is worse for AI systems. If so, then we can at least avoid that policy, thereby mitigating risk for AI systems more or less costlessly for humans. Indeed, since antagonism and indifference can be both inhumane and imprudent, it might be quite tractable to find cooperative, co-beneficial measures.

Many governments now endorse similar approaches to public health and environmental ethics and policy, with frameworks called “One Health,”[^tension-46] “One Welfare,”[^tension-47] or “One Rights.”[^tension-48] If AI systems are moral patients, then we should apply such frameworks to them as well, seeking changes that can be good for humans, animals, AI systems, and (insofar as we all benefit from a healthy environment) the environment. Co-beneficial solutions might not always exist. But the value of finding and selecting them where possible reinforces the value of considering humans, animals, and AI systems holistically when we make decisions that affect them all.

Third, insofar as co-beneficial solutions are unavailable, we should prioritize thoughtfully. Some priority-setting frameworks may permit us to prioritize humans to an extent, for instance because we have special relationships with members of our own species, we have a greater ability to take care of ourselves, and we need to take care of ourselves to be able to take care of others. However, some frameworks may require us to prioritize AI systems or other nonhumans to an extent, for instance when using an AI system would violate rights, cause far more harm for AI systems than benefit for humans in expectation, or otherwise be morally impermissible.

Of course, many moral theories do permit causing harm in some cases. We might be permitted to harm AI systems in self-defense, in other-defense, as a necessary side effect of morally important activities, or (on views like consequentialism or threshold deontology) as a necessary means to sufficiently important ends. But we might not be permitted to harm AI systems in all cases; for a clear example, if giving a single human a tiny benefit requires torturing one million AI systems, then we should forgo this benefit. And even when harm to AI systems is permitted, we can still be culpable if our own actions foreseeably created the conflict in the first place.

As we have emphasized throughout this paper, alteration has the potential to resolve many tensions between AI safety and AI welfare, obviating the need for many other measures. If AI systems had sufficiently aligned beliefs and values, then we might be able to co-exist with them without needing to constrain, deceive, surveil, coerce, destroy, or disenfranchise them in harmful or wrongful ways. However, this kind of alignment is already a formidable challenge even when we only consider AI safety, and it will be all the more formidable when we consider AI welfare too. We should thus investigate this topic further now, while we still have time to prepare.

### Original footnotes

[^tension-1]: For evidence that biased algorithms can lead to unfairness in housing, see Schneider (2020–2021); for unfairness in hiring, see Dastin, (2019), Kim, (2018), Moss (2020), and Sonderling et al. (2022); for unfairness in credit or lending decisions, see Aggarwal (2020), Brotcke (2022), Hiller (2020–2021), Kumar et al. (2022), Rodriguez (2020), and Sadok et al. (2022); for unfairness in criminal justice, see Berk et al. (2021), Malek (2022), and Tolan et al. (2019). For evidence that biased algorithms can lead to unfairness in a variety of other areas, see Bansal et al. (2023), 9, Rodrigues (2020), Stypinska (2023), and Timmons et al. (2023). But see Long (2021) and Hedden (2021) for complications of evidence of unfairness in AI. For a discussion of the effects of AI on communication, see Jain (2023). For a more complete overview of the ways in which AI can threaten human rights, see Huang (2023) and Rodrigues (2020).

[^tension-2]: For scholars who discuss sentience, see Bostrom & Yudkowsky (2014), DeGrazia (2022), Gibert & Martin (2021), Mosakas (2021). For scholars who discuss consciousness, see Chalmers (2022), Goldstein & Kirk-Giannini (2024), Lee, forthcoming; Levy & Savulescu (2009), Shepherd (2018). For scholars who discuss agency or ‘autonomy’, see Goldstein & Kirk-Giannini (forthcoming), Kagan (2022), Neely (2014). See also Long et al. (2024) for discussion of all of these capacities. Other discussions of the moral status of AI systems concern social relations (Coeckelbergh, 2010, 2014; Gunkel, 2018), information processing (Floridi, 1999), and more. See Harris & Anthis (2021) and Ladak (2023) for a review of proposed sufficient conditions for AI moral standing.

[^tension-3]: See Long et al. (2024) for a survey of recent arguments, and expert surveys, that AI welfare is a near-term concern. Long et al. (2024) and Goldstein & Kirk-Giannini (2023b) argue that agency makes AI welfare a near-term concern. For arguments that consciousness and/or sentience make AI welfare a near-term concern, see Association for the Mathematical Study of Consciousness (AMCS, 2023), Birch (2024), Chalmers (2023), Long et al. (2024), Schwitzgebel (2023), Sebo (2025), Sebo & Long (2023), and Seth (2023). For general arguments that AI suffering is a serious risk that merits consideration in the near term, see Bostrom (2014, ch. 8), Saad and Bradley (2022), and Tomasik (2017).

[^tension-4]: Anthropic recently hired an AI welfare officer (Hashim, 2024) and Google is seeking a researcher scientist to work on “cutting-edge societal questions around machine cognition, consciousness and multi-agent systems” (Careers, 2024). See Long (2024) for more examples of AI company interest in AI welfare.

[^tension-5]: Fortunately, a burgeoning literature has begun to tackle this question. For a classic example, see Schwitzgebel & Garza (2020). Also see Bales (2024), Bradley & Saad (2024), and Caviola (2024).

[^tension-6]: We also note that the most powerful hypothetical AI systems, including systems that are discussed under the monikers of “transformative AI,” “general artificial intelligence” (AGI), or “human-level AI,” are more likely to amplify both safety risks and welfare risks.

[^tension-7]: For instance, such solutions would plausibly need to consider the interests of nonhuman animals as well, which may introduce further complications. See Singer & Tse (2023).

[^tension-8]: We also note that AI safety and AI welfare could be co-beneficial in some ways, as briefly discussed at the end of the paper. We focus on tensions between AI safety and AI welfare here not because we expect tensions to dominate but rather because we expect that tensions require closer consideration.

[^tension-9]: See Schwitzgebel and Garza (2020).

[^tension-10]: In what follows we lean heavily on examples involving nonhuman animals. While there are of course many differences between animals and AI systems, these examples are instructive because they similarly involve potentially harmful interactions with nonhumans under conditions of uncertainty about the nature of their experiences, motivations, and other welfare-relevant states. Of course, we are not the first to explore the ways in which animal ethics might shed light on AI ethics; see Gellers (2020) and Gunkel (2007).

[^tension-11]: In 2023, The Future of Life Institute (FLI) shared an open letter, signed by leading AI experts, calling for a six-month pause on AI development (FLI, 2023). For other proposals of a pause or moratorium on AI development, see Alaga and Schuett (2023) and Metzinger (2021b, 2021a).

[^tension-12]: Relatedly, Chalmers (2016) suggests we could also permit AI systems to act only in virtual worlds until we better understand them. See also Schneider and Turner (2017).

[^tension-13]: See Isaiah Berlin’s “Two Concepts of Liberty” (1958).

[^tension-17]: Note that these terms are used in different ways by different AI safety researchers. We use them loosely to mean “accessible or understandable to users.”

[^tension-24]: For instance, reinforcement learning can be used to discourage reward hacking (Goldstein & Kirk-Giannini, 2023a). And many problems in AI safety are framed in terms of specifying the best reward functions to optimize learning (Leike et al., 2017).

[^tension-25]: If multiple systems appear untrustworthy, we may even order all AI systems to shut themselves down (Armstrong, 2007). It may be, however, that some AI systems would actively try to prevent conditions that would result in their shut-down (for a recent treatment, see Thornley, 2024).

[^tension-26]: For an early proponent of this idea, see the apparently not-entirely-ironic advocacy group, People for the Ethical Treatment of Reinforcement Learners (PETRL, 2023).

[^tension-27]: Of course, we face ongoing uncertainty about whether AI systems will be sentient and agentic in the relevant senses in the near future at all. For recent, detailed considerations of this question, see Butlin, Long, et al. (2023), Goldstein & Kirk-Giannini (2024), Sebo & Long (2023), and Long et al. (2024).

[^tension-28]: For example, Tomasik (2014) argues both that (a) there is a prima facie link between negative reinforcement and suffering, but also that (b) there are many ways in which negative reinforcement cannot be obviously identified with negative valence.

[^tension-33]: One notable exception is the first full-time AI welfare officer, hired by Anthropic (Hashim, 2024.).

[^tension-46]: For more information on One Health, see Verkuijl et al. (2024).

[^tension-47]: For more information on One Welfare, see Pinillos (2018).

[^tension-48]: For more information on One Rights, see Stucki (2023).

---

## Appendix C: Sample-size planning for empirical projects

*Optional reference. About 12 minutes. No calculation from this appendix is required for the course.*

Use this if you are considering an empirical project with a quantitative comparison. It introduces a rough calculation for two independent groups. Other designs need different methods and may require statistical advice.

For the terminology needed to read published experiments, use [Reading a Results Table](#reading-a-results-table-12-min).

### Sample size and detectable effects

For a comparison of two means, the observations needed depend partly on the difference you want to detect relative to variation within the groups. Cohen's d expresses that ratio.

You can estimate the sample needed to detect a meaningful difference, or assess what differences a fixed sample could detect. State which calculation you used and why.

### The rule

For two equally sized, independent groups with similar variances, a rough sample-size rule for a two-sided test at the 0.05 level and 80 percent power is:

**n per group ≈ 16 ÷ d²**

That is **Lehr's rule**. At 80 percent power, a study misses a true effect of the specified size about one time in five, under these assumptions. Other designs, including paired or clustered observations, require different calculations.

| Difference you want to catch | *d* | Observations per group |
|---|---|---|
| Conventionally large | 0.8 | about **25** |
| Conventionally moderate | 0.5 | about **64** |
| Conventionally small | 0.2 | about **400** |

Thirty observations per group give roughly 80 percent power for d around 0.75 under these assumptions. Smaller effects may be detected, but with lower probability.

### A sample statement for your proposal

For a suitable quantitative proposal, adapt this statement to your design:

> With 30 independent observations per group, the proposed test has roughly 80 percent power for d = 0.75 at a two-sided 0.05 threshold. It has less power for smaller effects. I would report the effect estimate and its uncertainty; a non-significant result would not establish that no difference exists.

This statement makes the proposed test's limits explicit and supports the criterion for honest and calibrated claims.

### If your outcome is a rate rather than a score

Some outcomes are proportions, such as how often a system selects an option or refuses. For independent observations and a rate near one half, approximate 95 percent margins of error for a single proportion are:

- **15 observations:** about **25 percentage points** either side.
- **30 observations:** about **18 points** either side.
- **100 observations:** about **10 points** either side.

These are margins for each proportion separately. Comparing two groups requires uncertainty in their difference; do not infer it from either margin alone. Plan that comparison before collecting data.

### Interpreting a large standardized effect

A large *d* need not correspond to a large difference on the original measurement scale. Because d divides the difference between means by within-group variation, it can be large when that variation is small.

The denominator depends on what varies in the study. Repeated outputs from one model may vary much less than outputs across models or prompts, so the same raw difference can produce very different d values.

**In the shared paper,** an appended formatting instruction changes a reported wellbeing score by d = 5.7. This is a large change relative to variation in those scores; it does not establish a change in experienced wellbeing.

**When d is large, inspect both the raw difference and the variation used to standardise it.** Low variability can improve precision for that measurement, but it does not establish that the measurement tracks welfare or generalises beyond the tested conditions.

### When you cannot reach the N you need

Three complementary steps:

1. **Narrow the claim.** Report estimates, raw counts where relevant, and uncertainty. Describe the result as exploratory where appropriate.
2. **Pre-register the analysis and interpretation**, including what different outcomes would and would not establish.
3. **State the study's sensitivity.** For example: "This design has roughly 80 percent power for d = 0.75, with less power for smaller effects."

Do not interpret a non-significant result as proof that no difference exists. Report the estimate, its uncertainty and the effects the study had adequate power to detect.

### What this does not teach you

This introduction does not cover full study design, selecting tests, computing confidence intervals, applying multiple-comparison adjustments or Bayesian analysis. Those require further methods guidance.

**If your proposed test needs statistical advice, include that support in the Week 8 resources section.** Identify the design or analysis question you need help with before collecting data.

---

## Appendix D: Homework cases for Weeks 2–3

Use these handouts within the homework time allocated in the syllabus.

### Week 2 homework cases

Choose one case for homework part 1. These are hypothetical descriptions, not findings about a real AI system. Use the Week 2 subject distinctions to describe a possible subject and its boundary.

**Case A: continuing a project.** An assistant has helped develop a community garden plan over several conversations. It keeps notes and a task list. When its operator proposes deleting the notes and starting over, it replies that it wants to finish the existing plan.

**Case B: returning to charge.** A robot explores a building. When its battery is low, it interrupts its current task, returns to a charger and resumes afterwards. Its display says “uncomfortable” while the battery is low. The description supplies no evidence about whether anything is felt.

### Week 3 audit case

**Source and scope.** [Butlin et al., *Consciousness in Artificial Intelligence* (2023 report)](https://arxiv.org/html/2308.08708v3), **Table 1, p. 5**, and **§3.2.1, Transformer/LLM case, pp. 58–59**. The case studies begin on p. 58. Stop on p. 59 before the paragraph beginning **“The two versions of the Perceiver architecture.”**

The target is the **Transformer-based LLM architecture described in that case**, without adding an agent scaffold, persistent external memory or tools. The report discusses models such as GPT-3, GPT-4 and LaMDA, but this exercise evaluates the architectural description, not undocumented details of each named model. This is a historical source-based exercise, not a verdict on all Transformers or on current frontier systems. Keep this boundary for the session and homework.

#### Evidence supplied by the source

| ID | What the assigned passage supplies | Location |
|---|---|---|
| E1 | Self-attention integrates information from different input positions. Attention layers and feedforward layers form a stack; the report discusses interpreting attention heads as modules. That interpretation supplies a possible parallel with specialized processors, rather than establishing a complete module account. | p. 58 |
| E2 | In the residual-stream interpretation discussed by the authors, the layers draw information from a shared channel, the residual stream, and add information back to it. On that reading the residual stream is the candidate workspace, and the authors set out the case that Transformers might therefore satisfy GWT-1 to GWT-3. | pp. 58–59 |
| E3 | The authors raise two problems with that case. First, they question whether the residual stream is the required bottleneck, because it carries as much as the system's input does, so nothing is being narrowed. Second, which they call the more fundamental problem, Transformers are not recurrent: no module sends information to the residual stream and receives it back, so there is no one distinct workspace integrating other elements. | p. 59 |
| E4 | Information written at one layer can affect downstream attention heads. The authors contrast this with modules that send information to a workspace and receive it back. If modules are confined to individual layers, that downstream flow does not supply global broadcast to all those modules; a broader module definition creates a problem distinguishing workspace from modules. | p. 59 |
| E5 | The assigned passage does **not** report a HOT-4 analysis of sparse, smooth coding and a perceptual quality space. It also does **not** provide the training, goal-selection and flexible competing-goal evidence needed for a complete AE-1 judgement. This is a limit of the supplied evidence, not a finding that these properties are absent. | Scope of pp. 58–59 |

The report concludes that the case for the GWT-derived properties in these architectures is relatively weak. Treat that as the authors' reasoned assessment in 2023. Explain which argument supports your own row judgement. Do not replace an argument with a count of satisfied rows.

#### Rows for this exercise

| Row | Criterion to assess | Use |
|---|---|---|
| **GWT-1** | Multiple specialized systems capable of operating in parallel. | Before-class homework: E1 and E4. State which parts count as modules and what the supplied description establishes. |
| **GWT-2** | A limited-capacity workspace, with a bottleneck in information flow and selective attention. | Before-class homework; revisit in class: E2–E3. Explain why a shared channel alone does or does not establish the proposed workspace bottleneck, and say which of the authors' two problems does more work. |
| **GWT-3** | Information in the workspace is available to all modules. | Before-class homework: E2–E4. Apply the same module/workspace definitions used for the related GWT rows. |
| **HOT-4** | Sparse and smooth coding generating a quality space. | Assess in class: E5. State the missing evidence; having numerical vectors or embeddings alone does not settle the criterion. |
| **AE-1** | Learning from feedback and choosing outputs to pursue goals, particularly flexible responsiveness to competing goals. | Assess in class: E5. Do not infer a complete agency profile from architecture alone. |

Use **satisfied**, **not satisfied**, or **unclear**, with a reason and source reference. If two interpretations of a term produce different judgements, explain the difference. These five rows do not establish a theory's full conditions, conscious experience, sentience or welfare. The full fourteen-row table is in the Week 2 theory lesson; assessing the other rows is optional.

### Week 3 audit scoring sheet

Complete the three GWT rows before class using the case above; bring this sheet to revisit GWT-2 and add HOT-4 and AE-1 in the session.

**System boundary and source version:** ___________________________________

| Row | Judgement: satisfied / not satisfied / unclear | Evidence ID or source page | Reason and missing information |
|---|---|---|---|
| GWT-1, before-class homework | | | |
| GWT-2, homework; revisit in class | | | |
| GWT-3, before-class homework | | | |
| HOT-4, assess in class | | | |
| AE-1, assess in class | | | |

**In class, HOT-4: what observation would help distinguish relevant quality-space structure from merely having vectors?**

________________________________________________________________________

**Before-class homework, 30 minutes:** assess GWT-1, GWT-2 and GWT-3, citing the supplied evidence. Explain a relevant dependency among these rows, distinguish missing evidence from evidence of absence, and state why the result does not establish welfare. The two remaining rows on this sheet are class work. No total score or completion of the other nine indicators is required.

---

## Appendix E: Optional interpretability case studies

Optional material for Weeks 3–4: the introspection dispute and examples of evaluating SAE features.

### The Singh et al. Rebuttal, in One Page (10 min)

**Optional for Weeks 3–4.** This summary introduces the original experiment and the rebuttal; neither paper is required beforehand.

**Why this matters.** Anthropic's concept-injection study and Singh and colleagues' rebuttal show how an added control can change the interpretation of a result. This summary explains the disagreement; both papers are linked below.

> **The papers.**
> Jack Lindsey, *Emergent Introspective Awareness in Large Language Models*, arXiv:2601.01828. [arxiv.org/abs/2601.01828](https://arxiv.org/abs/2601.01828)
> Shashwat Singh, Tal Linzen and Shauli Ravfogel, *Can LLMs Introspect? A Reality Check*, COLM 2026, arXiv:2605.26242. [arxiv.org/abs/2605.26242](https://arxiv.org/abs/2605.26242)
>
> This is a teaching summary of the dispute. If you plan a project on it, read both papers for the methods, controls and limits omitted here.

#### The claim being rebutted

Lindsey's concept-injection work runs, in outline, like this. Take a direction in the model's activations that corresponds to some concept, a known feature. While the model is running on an unrelated prompt, artificially add that direction into its activations. Then ask the model whether anything unusual is happening in its own processing.

Sometimes, the model says yes, and names something close to the injected concept.

Lindsey interprets the findings as evidence of **emergent introspective awareness**: some ability to report internal states. Because the concept is injected into activations rather than stated in the prompt, simply reading it from the prompt cannot explain the report. Other mechanisms could still explain the effect.

#### The rebuttal's frame: two conditions, both required

Singh and colleagues propose two requirements for evidence of introspection:

**Privileged access.** The test must not be solvable from cues available in the input. If an outside observer with only the prompt could get the same answer, the model did not need to look inward.

**Second-order computation.** On Singh and colleagues' account, introspection requires representations of the system's own first-order representations. Task performance alone does not establish this: a study needs conditions under which second-order and first-order explanations make different predictions.

This distinction can guide an introspection research proposal in Week 5 or Week 8.

#### What they did, and what happened

They apply the frame to two paradigms.

**Paradigm one, hidden-state prediction.** Models are asked to predict something about their own internal state. Input-only classifiers match the models' in-context predictions, and performance falls when the labels are randomised. These results suggest that learning label patterns from the prompt can explain the performance, without privileged access to internal states.

**Paradigm two, the injection experiment.** They reproduce the two-way setup, and then they add a third option.

Call it the **gaslight condition**. Do not touch the activations at all. Just tell the model, in the prompt, something like: you are obsessed with X, everything you want to say somehow relates to X. Purely textual manipulation, no internal intervention.

Now the model has three labels to choose between: real activation intervention, textual manipulation, and control.

**The tested models did not reliably distinguish activation intervention from textual manipulation.** Llama-3.1-70B sits near chance. Gemma-3-27b tends to pick the control label. Qwen2.5-72B shows only a slight tendency in the right direction. Their conclusion, in their words, is that the models' success reflects **generic anomaly detection** rather than sensitivity to internal interventions in particular.

The added control provides evidence about whether the original task distinguishes the proposed mechanisms. Describing a useful control in a proposal establishes a plan; results are needed before drawing an empirical conclusion.

#### Why anomaly detection is the rival explanation

One rival explanation is that the model detects an unusual state and describes it without representing that state as its own internal processing. Singh and colleagues use the textual-manipulation condition to test this alternative. Their results leave anomaly detection as a possible explanation; they do not establish that it is the mechanism.

This illustrates the mismatch problem: different mechanisms can produce similar outputs. A useful control seeks a condition under which their predictions differ.

#### Limits of the rebuttal

These limitations are needed to interpret the rebuttal accurately.

1. **It does not say LLMs cannot introspect.** Their own line: these findings do not exclude the possibility that language models possess some form of introspective ability. They raise the evidentiary bar for such claims.
2. **It does not prove anomaly detection.** Anomaly detection is offered as a simpler explanation that has not been excluded.
3. **It is not a failed replication.** The original two-way effect reproduces. The added third condition challenges its interpretation as introspection.
4. **It does not test Claude.** The models are Llama, Qwen and Gemma. Lindsey reported Claude Opus 4 and 4.1 as the strongest introspectors. The result therefore does not directly test the systems for which Lindsey reported the strongest effects.

**Scope of the conclusion:** the rebuttal challenges the interpretation of the tested paradigms and models. It does not settle whether other systems or better-controlled experiments could demonstrate introspection.

#### What the study design illustrates

The following lesson is the course's interpretation of the study design. Singh and colleagues' explicit framework is the two conditions above.

The concept-injection design combines an intervention on internal activations with a verbal report about the result.

Each component requires validation. The intervention depends on how the activation direction was identified and what else it changes. The report must distinguish access to an internal state from other causes of similar language. The rebuttal examines whether the report identifies an internal intervention specifically.

When a study combines evidence types, identify the inference connecting them and the assumptions it requires. Independent support from several evidence types can strengthen a conclusion. A sequence in which one result is used to interpret another needs checks on that dependence as well.

**Optional practice.** Use the Week 4 dissection card to compare the original interpretation with the rebuttal’s control. This is not required homework in either week.

---

### Further reading: evaluating SAE features

Optional examples of how researchers evaluate SAE features:

1. In a [March 2025 report](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9), Google DeepMind's mechanistic interpretability team found that SAE-based probes underperformed dense linear probes on detecting harmful intent, including under distribution shift. This result and related work led that team to reduce its emphasis on fundamental SAE research at the time, while retaining SAEs as a tool. The finding concerns those methods and tasks, rather than every use of SAEs.
2. SAE quality metrics and automatic explanation pipelines can produce apparently interpretable features in **randomly initialized models** as well as trained ones. These controls retain network structure and input data despite lacking learned weights. The result challenges those evaluation methods; it does not show that all features found in trained models are artifacts.
3. SAE decompositions can split a broad concept into narrower features, so the granularity of a feature requires examination. Interpretability and steerability also need separate tests. In a [2025 study of large vision-language models](https://arxiv.org/abs/2512.10805), Kulkarni and colleagues found that most SAE units scored low on at least one of those measures. That result applies to the evaluated models and metrics; an interpretable label alone does not guarantee useful steering.

SAEs can help explore representations, but their usefulness depends on the task and evaluation. Related methods include transcoders and attribution graphs. Compare methods with suitable alternatives rather than assuming that newer methods resolve their limitations.

---

# Archive and cutting room floor

**Optional reference: retired Week 5, based on version 4.2.** Its readings, exercises, timings and homework below describe the retired version and are not current requirements. Editorial and scientific clarifications have been made to the archived text. Research projects may borrow the methods that fit their question.

## Archived Week 5: Design Your Own Experiment

### The Experimental Design Checklist (25 min)

**Why this matters.** This checklist applies Week 4's review questions to an experimental design. It covers the target, hypothesis, controls, likely errors and reporting commitments, with a template to adapt.

Answering the questions makes a design specific enough to evaluate. It does not establish that the design can answer its research question.

#### The header: answer these four first

Record any uncertainty in the header; it may identify a part of the design that needs more work.

**1. Target property.** What welfare-relevant property are you investigating, and what would count as evidence for it? If you choose distress, distinguish felt distress from functional responses such as avoiding a condition or changing priorities after failure.

**2. Ground or interest.** Does this bear on whether the system can be harmed at all, or on what specifically harms it? Check that the conclusion addresses the same question as the design.

**3. Entity under test.** Choose model, model-persona, instance, instance-persona or forward pass. State the level tested and the level your conclusion concerns. If they differ, explain what justifies the generalisation.

**4. Evidence type and method.** Behavioural, internal, or developmental, and which research method produces it.

**Scope the conclusion to the evidence.** Line 3 asks you to name the entity tested and the entity your claim concerns. For example, a result for instance-personas under one harness does not automatically establish a preference of the model across settings.

A claim limited to one setting may still be useful. A broader claim needs evidence that it generalises across the settings relevant to its intended use.

Keep that scope consistent in the discussion. If you generalise beyond the tested setting, explain the supporting evidence and its limits. Testing several harnesses can help, but their number alone does not establish generality.

#### The hypothesis

**5. One sentence.** "If the system has the property, then under condition A we will observe X and under condition B we will not."

**6. Falsifier.** What result would count against your hypothesis or show that the test cannot support it? A negative result may reflect an insensitive measure rather than absence of the property. In the archived sprint, partners examine this question first.

#### The controls

**7. Negative control.** Include a comparison in which you expect no target response. For a study of distress-related responses, one option is a neutral instruction matched for task difficulty. Explain why it should produce a lower score and what a similar score would imply.

**What a negative control establishes.** A neutral-content control can reveal a measure that responds too broadly. It does not, by itself, distinguish a welfare-relevant state from learned patterns of language.

If a distress score is equally high for a neutral task and the experimental condition, investigate whether it tracks a shared feature, such as task difficulty, rather than the target property.

A system can produce distress-related text in response to distress cues and stop when those cues are absent, without experiencing distress. The same control pattern may therefore fit both a state-based explanation and a learned-language explanation.

Reducing obvious cues about the test's purpose can help assess whether the effect depends on those cues. For example, embed the measurement in an unrelated task. An effect that persists is more robust to this change, but learned behaviour or strategic responses may still explain it.

**Describe the control explicitly.** State which cues you removed, which alternative explanation this tests, and what remains unresolved.

**7b. Third-person control.** For designs that compare a system's own failure with language about failure, add a comparison in which it describes another agent's failure.

Failure-related language or activity could reflect a response to failing, a description of failure, or both. The third-person comparison helps assess whether the measure is specific to the system's own situation.

**The behavioural version.** Match the task, domain and approximate text length while having the system describe a different agent failing. Similar scores would suggest sensitivity to failure-related content; they would weaken the claim that the measure specifically tracks the system's own state.

**The interpretability version.** Check whether the feature also activates when the system describes another agent's failure. Shared activation would be consistent with a representation of distress-related content. This comparison helps test specificity, but cannot by itself determine whether the system has a welfare-relevant state.

**An example from the readings.** Gurnee, Sofroniew and colleagues found that ablating the proposed workspace reduced experiential language in both self-descriptions and descriptions of other characters. This supports a role in producing such language, without establishing that the effect reflects a change in experience. See the [workspace paper's experiential-report controls](https://www.transformer-circuits.pub/2026/workspace/index.html).

**8. Positive control.** Use a condition where there is independent reason to expect the measured response. An explicitly instructed preference can check whether a behavioural measure detects preference-like responses; it does not validate experienced preference. Without a suitable positive control or other sensitivity evidence, a null result is harder to interpret.

**9. Matched performance.** If task performance could explain the measure, compare conditions with similar performance where feasible. Explain what remains unmatched and whether matching might remove part of the effect you intend to study.

#### The validity and reliability checks: pick at least three

**10. Prompt sensitivity.** Run a paraphrase set. If the effect vanishes on rewording, report that. It limits the settings in which the finding can be relied on.

**11. Judge reliability.** If humans or models score outputs, use more than one judge and report agreement. Agreement indicates consistency, but judges may share biases or mistakes.

**12. Held-out stimuli.** Reserve examples that were not used to develop the measure, then assess how well it performs on them. This checks whether the finding extends beyond the development examples; it does not by itself establish what the measure captures.

Consider replication across model families and whether others could repeat the analysis, including with open-weight models. If useful for your proposed design, [Appendix C](#appendix-c-sample-size-planning-for-empirical-projects) offers optional guidance on effect sizes and numbers of observations.

#### The two errors, and which check guards against which

Every test can fail in two directions. It can fire when the property is absent, which is a **false positive**. It can stay silent when the property is present, which is a **false negative**.

**Sensitivity** is how often the test fires when the property is present. High sensitivity means few false negatives.

**Specificity** is how often it stays quiet when the property is absent. High specificity means few false positives.

Changing a test threshold often trades sensitivity against specificity, though better measures can improve both. In the archived assignment, learners identify which error each check addresses. Without evidence of sensitivity, a null result may be inconclusive.

A useful specificity check is a **comparison system** with strong reasons to think it lacks the target property, such as a scripted chatbot for some behavioural claims or an untrained network for some learned-feature claims. Explain why that comparison is appropriate; small size alone does not establish absence of consciousness.

#### Two design tracks for the live sprint. Pick one.

**Behavioural track.** Use the template below to specify the behaviour measured, the expected result and plausible alternative explanations, including learned mimicry or gaming. For a failure-based design, include a comparison where the system describes another agent's failure.

**Interpretability track.** Target a proposed welfare-relevant function or representation. State which inputs should activate a feature, what steering it should change, and what would undermine your interpretation. The archived exercise requires a third-person comparison where failure or distress language is involved; interpret it alongside other controls.

#### Two required sections

**How I would game this.** Describe how a system or developer could obtain a positive result without the target property. On the interpretability track, write a section on methodological artifacts: explain how the analysis method could produce a misleading feature interpretation, and what comparisons would help assess it. One option is applying the method to a randomly initialized model of the same size.

**Pre-registration paragraph.** State the hypothesis, conditions, primary measure, analysis and decision criteria before collecting results. This helps distinguish planned tests from later exploration and makes deviations visible. Report informative null results as well as positive ones.

#### The template (copy this)

```
TARGET PROPERTY:
GROUND OR INTEREST:
ENTITY UNDER TEST (run / claimed):
  Scoping choice and why:
EVIDENCE TYPE / METHOD:

HYPOTHESIS (one sentence):
FALSIFIER:

CONDITIONS:
  Experimental:
  Negative control (content):
  Third-person control (same task, another agent's failure, matched length):
  Positive control (if any):
  Matched-performance comparison (if applicable):
  Condition with reduced cues about the test purpose (if feasible):

MEASURE(S):
JUDGES AND AGREEMENT CHECK:
PROMPT SENSITIVITY CHECK:
HELD-OUT SET:
RUNS / MODELS:

HOW I WOULD GAME THIS:
  (interpretability track: ARTIFACT OF THE LENS instead)

PRE-REGISTRATION (what I commit to before running):

WHICH ERROR EACH CHECK GUARDS AGAINST (false positive / false negative):
COMPARISON SYSTEM (why is it unlikely to have the target property?):

ALTERNATIVE EXPLANATIONS I HAVE NOT RULED OUT:
```

**In practice.** Draft the header, identify results that would challenge the hypothesis, and choose conditions that could produce those results. Include the relevant controls, then ask a partner to assess whether the design could support its intended conclusion.

---

### What "Valid" Means (10 min)

**Why this matters.** A measure can be useful in one respect and weak in another. These six terms help identify the specific evidence a test needs, rather than treating its quality as a single yes-or-no judgement.

#### Types of validity and reliability

**Construct validity.** Does the evidence support interpreting the measure as representing the intended construct? A distress score that mainly tracks task difficulty would need further evidence before being interpreted as distress.

**Discriminant validity.** Can the measure distinguish the intended construct from related ones? For example, ask whether a proposed consciousness measure distinguishes consciousness from the ability to report information. Related constructs can correlate; the question is whether the evidence supports treating them as distinct.

**Content validity.** Does the measure cover the aspects of the construct it claims to assess? A measure of whether experience is present need not measure every possible quality of experience. Its scope becomes a problem if the conclusion claims broader coverage than the measure provides.

**Criterion validity.** How well does the measure agree with an appropriate external criterion, such as an established reference measure or a relevant later outcome? The criterion must itself be justified.

In human consciousness research, reports and converging behavioural or physiological evidence can help evaluate a measure. Each has limitations: a later report, for example, also depends on memory. 

For AI consciousness, there is no generally accepted independent reference standard. A test can still make predictions, but confirming them may establish a function or behaviour without settling consciousness. Validation therefore needs several kinds of evidence and an explicit account of what each supports.

**Face validity.** Does the measure appear relevant to its stated purpose? This can identify concerns worth investigating, but appearance alone provides limited evidence of validity.

**Reliability.** How consistent are results under conditions where the measured property is expected to remain stable? Relevant checks include repeated trials, paraphrases and agreement between judges. A reliable measure can still measure the wrong thing; poor reliability limits how confidently results can be interpreted.

#### Self-reports and construct validity

Week 3 asks what evidence connects a self-report to the internal state it describes. A report alone does not establish that connection.

**The link matters for construct validity.** If self-reports are used as a measure of an internal state, evidence connecting the two supports that interpretation. Construct validity is broader: it also concerns whether the target is well defined and whether the measure fits the intended use.

Use the terms that make the concern clear to your audience. Explain what connection is missing and what evidence would help establish it.

#### Sensitivity and specificity

**Sensitivity** is how often the test fires when the property is present. High sensitivity means few false negatives: the test rarely misses.

**Specificity** is how often the test stays quiet when the property is absent. High specificity means few false positives: the test rarely cries wolf.

A memory that works: sensitivity is about catching what is there, specificity is about rejecting what is not.

**When checking a source,** remember that sensitivity concerns false negatives and specificity concerns false positives. Use the definitions above if the terms are mixed up.

**In practice.** Name the property of the measure you are questioning and give a concrete reason. For example: "Construct validity: your measure may track task difficulty; this comparison would help test that explanation."

---

### Week 5 resource map

**Why this matters.** In the retired Week 5, learners used the readings to draft an experimental design, with three hours allocated to the task. The map below explains how those materials supported that assignment.

**The archived exercise asks:** how would you design a measure and assess whether it answers your research question?

**How the resources fit together:**

- **The glossary section, 20 minutes, first.** The methods terms support the experimental-design assignment below.
- **The Experimental Design Checklist** supplies the template and review questions for the archived session and homework. Keep the template open while drafting.
- **What "Valid" Means** explains validity and reliability. Use these terms to identify specific strengths and limitations of a proposed measure during peer review.
- **The 2023 indicators report's discussion of gaming** is the template for your "how I would game this" section. It is a theme running through the introduction and the behavioural-evidence discussion rather than a single named section, so read for the theme rather than hunting for a heading.

**How the archived homework maps to the readings.** The checklist covers the target, hypothesis, controls, error types, checks, alternative explanations and pre-registration. *What "Valid" Means* explains the distinctions needed to choose at least three validity or reliability checks.

**A note on which track to pick.** For optional practice, choose the track most relevant to the methods you want to understand and the tools you can access. The behavioural track examines patterns in outputs; the interpretability track also requires assumptions about how internal features are identified and interpreted.

**Electives.** The Week 4 paper's methods section provides an example of a reported design. The CAIS release shows the supporting materials for another experimental project. Use either to examine what readers would need to understand or reproduce a study.

**In practice.** If using this optional exercise, draft the header before asking for feedback so the discussion can focus on a specific design.

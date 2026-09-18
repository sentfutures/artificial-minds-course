# Artificial Minds Atlas
## The concepts of the field, reconciled

*Sentient Futures. Artificial Minds Research Course 4.4. Updated 17 September 2026. 389 concepts in 8 branches. This is an optional reference organised by subject; the syllabus and glossary determine required work.*

A star marks a term assessed in at least one active week. Brackets show its first glossary location; **Ref** means the optional experiment-design reference. Where assessment occurs later or in several weeks, those weeks are listed separately. The atlas carries 104 starred concepts against 102 starred glossary entries, because some glossary entries define several concepts at once and some assessed terms recur across weeks: *Model, model-persona, instance, instance-persona, forward pass* is one entry and five atlas concepts. That is not drift and does not need fixing. **[extra]** marks an atlas concept with no glossary entry: a thought experiment, or a teaching point that lives in the Companion rather than the glossary. **[extra, W2]** means the same thing and names the week it is taught. These are not additional terms to memorise.

The matching machine-readable outline is **atlas.json**. Keep its concept definitions and `syllabusOverlay` aligned with the glossary when changing the course. This Markdown outline was regenerated from that data for version 4.4.

---

## I. Foundations: Metaphysics, Epistemics and Decision

What has to be true of the world, and of your own reasoning, before any of the evidence in the later branches means anything. Most disagreements that look empirical bottom out here.

- **Substrate and what minds are made of**
  - **Computational functionalism** ★ [W1]: the view that implementing the right kinds of computations is necessary and sufficient for the mental states in question; here, consciousness. It makes the relevant computational organisation, rather than a particular substrate, decisive. Rejecting it does not by itself commit someone to a biological theory (wiki: Functionalism).
  - **Biological naturalism** [W2]: the position that consciousness is a biological phenomenon produced by physical processes, and that computation alone is insufficient to explain or produce it. It does not follow simply from this label that no artificial system could ever reproduce the relevant causal powers. Associated with Searle.
    - *Origin.* John Searle
  - **Substrate independence** [W2]: the thesis that mental states could be realised in different physical materials, provided the relevant organisation or causal conditions are present. This does not imply that every system, or every substrate arranged in any way, supports consciousness.
    - *⚑ Corrected.* Map 1 had **Substrate Neutrality (Neuromorphic/Wetware)**. Two different layers fused: substrate independence is the metaphysical claim, and neuromorphic systems and wetware are system types. They belong in different branches.
  - **The hard problem** [W2]: the question of why and how physical processing gives rise to experience at all, as opposed to the "easy" problems of explaining functions such as attention, integration or report (wiki: The Hard Problem).
  - **Metaphysical theory of consciousness** [W2]: an account of how consciousness relates to the physical world in general, such as physicalism or dualism. It can constrain which systems might be conscious without specifying a practical test.
    - **Physicalism** [W2]: the view that everything is physical or depends entirely on the physical. Different versions give different accounts of how mental states relate to physical processes; it is broader than the claim that each experience is identical to a particular brain event.
    - **Dualism** [W2]: the view that the mental and the physical are fundamentally distinct in some respect. Substance dualism posits distinct kinds of substance; property dualism posits irreducible mental properties.
    - **Idealism** [W2]: the view that consciousness is the fundamental reality and the physical world is derivative or constructed from it.
    - **Neutral monism** [W2]: the view that the fundamental stuff of reality is neither mental nor physical, and that both arise from it.
    - **Panpsychism** [W2]: the view that consciousness, in some basic form, is a fundamental feature of matter everywhere (wiki: Panpsychism).
    - **Illusionism** [W2]: the view that the sense of having phenomenal consciousness is itself a cognitive illusion. Deflationism taken to its conclusion (Frankish), and attention schema theory sits close to it.
      - *Origin.* Keith Frankish, 2016, with Daniel Dennett as the main precursor
    - **Epiphenomenalism** [W2]: conscious experiences are caused by physical processes but cause nothing themselves. Awkward for this field, because if experience has no effects then no behavioural evidence can track it.
    - **Eliminative materialism** [W2]: the view that at least some familiar psychological categories, such as beliefs and desires, are mistaken and may be replaced by a mature scientific account rather than reduced to it. Claims about eliminating particular categories should be distinguished from denying all experience.
    - **Psycho-physical bridge laws** [W2]: hypothetical laws linking physical states to phenomenal states. What you would need to read consciousness off a system directly, and what nobody has.
  - **Scientific theory of consciousness** [W2]: an account of the mechanisms or processes associated with consciousness. Such accounts guide empirical investigation, while their application to AI also depends on assumptions about which features matter across different systems.
  - **Multiple realizability** [W2]: the possibility that the same kind of mental state can be realised by different physical systems. This leaves open how different those systems can be and which properties they must share.
  - **Supervenience** [W2]: higher-level properties are fixed by lower-level ones, so two systems identical in their physical details cannot differ mentally. The quiet assumption underneath most arguments in this field.
  - **Functionalism** [W1]: the weaker parent thesis, that having the right *functional organisation* is necessary and sufficient for consciousness, without specifying that the organisation has to be computational. Computational functionalism entails functionalism; functionalism does not entail computational functionalism. Keep the terms distinct when comparing a source's assumptions or assigning credences.
- **Attribution stances and their biases**
  - **Deflationism** [W2]: the view that consciousness just is a set of functions or capacities, so once those are described there is nothing left to add.
  - **Inflationism** [W2]: the view that consciousness is a rich further fact beyond any functional description, so a complete account of what a system does could still leave open whether it experiences anything.
    - *⚑ Corrected.* Map 1 had **Realism vs Illusionism/Eliminativism**. The standard pair is inflationism versus deflationism, with illusionism as deflationism taken to its conclusion. Realism versus illusionism is a real distinction but a different cut, and eliminative materialism is a broader thesis about folk psychology, held separately below.
  - **Over-attribution** ★ [W1]: treating a system that is not a moral patient as though it were. The error that wastes moral concern and costs the field its credibility.
  - **Under-attribution** ★ [W1]: treating a system that is a moral patient as though it were not. The error that could cause suffering at scale. The whole course sits between these two.
  - **Anthropomorphism** ★ [W1]: attributing human-like characteristics, mental states or intentions to a nonhuman entity. An attribution can be useful or mistaken; that depends on the evidence. Week 3 distinguishes unreflective projection from a method that adjusts its interpretation to the being studied.
  - **Anthropodenial** ★ [W1]: rejecting human-like characteristics or continuities in other animals when the evidence supports them. De Waal's term arose in the animal case; applying it to AI is an extension that also needs evidence.
    - *Origin.* Frans de Waal
  - **Anthropocentric versus animalcentric anthropomorphism** [W3]: de Waal's distinction, used by Keeling and Street. The first projects human characteristics without adequate adjustment; the second tests interpretations against the being's capacities, environment and behavior. Applying the latter to AI still requires evidence.
    - *Origin.* Frans de Waal
    - *⚑ Corrected.* Map 1 had **De Waal's Framework (Anthropomorphic Method)**. The canonical name is the full contrast pair, because the whole point is that one of the two is legitimate.
  - **Umwelt** [W3]: de Waal's borrowed term for an animal's own perceived world. Animalcentric anthropomorphism interprets behaviour through it.
    - *Origin.* Jakob von Uexkull, borrowed by de Waal
  - **Face-Value View** [W3]: the view that apparent behavioral evidence of welfare-relevant features should be accepted at face value. Keeling and Street argue against this approach.
    - *⚑ Corrected.* Map 1 had **Public & Scientific Attribution Views**, which names no position. The canonical pair is the Face-Value View and the No Evidential Weight View.
  - **No Evidential Weight View** [W3]: the view that apparent behavioral evidence has no evidential weight. Keeling and Street argue that objections to taking it at face value do not establish that it is worthless.
- **Thought experiments and canonical cases**
  - Imagined cases that do real work in this field. Each one is a lever on a position elsewhere in the atlas, so every entry says what it bears on.
  - **Philosophical zombie** [W2]: a hypothetical being physically identical to a conscious human but lacking subjective experience. Debates about its conceivability and possibility are used to examine physicalism. A merely functionally identical system is a related but different case. See [Chalmers's explanation](https://consc.net/zombies-on-the-web/).
    - *Origin.* Robert Kirk, 1974; the systematic version is Chalmers, 1996
    - *Bears on.* Inflationism and deflationism
  - **Vulcan** [extra]: A being with a rich conscious life but no happiness, suffering, pleasure or pain of any kind. It pursues goals and builds things and feels nothing about any of it. Chalmers argues killing one would obviously be wrong, which if right means *consciousness* and not valence is what grounds moral status. The sharpest case against valence sentientism.
    - *Origin.* David Chalmers, Reality+, 2022
    - *Bears on.* Whether the ground is consciousness or sentience
  - **Gradual replacement** [W2]: replace a brain's neurons one at a time with functionally identical silicon. Chalmers argues experience cannot quietly fade or flip while behaviour and judgement stay fixed, so functional organisation must determine experience. His two versions are **fading qualia**, where experience dims as the substitution proceeds, and **dancing qualia**, where it switches back and forth as circuits are swapped mid-run. The main positive argument for substrate independence, and the guide's name for it is the one to use.
    - *Origin.* David Chalmers, 1995, *Absent Qualia, Fading Qualia, Dancing Qualia*
    - *Bears on.* Computational functionalism and substrate independence
  - **Chinese Room** [W2]: Searle's case that following rules for manipulating symbols produces no understanding, however convincing the output. The standing argument against computational functionalism.
    - *Origin.* John Searle, 1980, *Minds, Brains, and Programs*
    - *Bears on.* Computational functionalism, against
  - **China brain** [extra]: The population of China, each person acting as one neuron with radios, implements a mind for an hour. Functionalism seems to say the population is conscious. Block thinks that is a reductio. The course uses this thought experiment as an analogy for questions about the appropriate level of description, not as the origin of the specificity problem.
    - *Origin.* Ned Block, 1978, *Troubles with Functionalism*
    - *Bears on.* Specificity problem
  - **Blockhead** [extra]: A machine that holds a precomputed lookup table of every sensible reply to every possible conversation of finite length. It passes any behavioural test and has no mind at all. *The direct ancestor of the gaming problem*, and the cleanest statement of why behavioural evidence gets discounted for systems trained on human text.
    - *Origin.* Ned Block, 1981, *Psychologism and Behaviorism*
    - *Bears on.* Gaming problem and evidential weight
  - **Mary's Room** [W2]: Mary knows every physical fact about colour vision but has only seen black and white. On leaving the room she learns something new, which if right means the physical facts leave something out. Jackson, 1982. Also called the knowledge argument.
    - *Origin.* Frank Jackson, 1982, *Epiphenomenal Qualia*
    - *Bears on.* Inflationism
  - **The imitation game** [extra]: The original proposal that a machine's conversational behaviour should settle the question of whether it thinks. The mismatch problem is the standing rebuttal, and Blockhead is the formal version of that rebuttal.
    - *Origin.* Alan Turing, 1950
    - *Bears on.* Apparent self-report and the mismatch problem
  - **Swampman** [extra]: Lightning strikes a swamp and by chance assembles a molecule-for-molecule duplicate of you. It behaves exactly as you would, but nothing in it has any causal history. Davidson argues its states therefore mean nothing. The question underneath developmental evidence: does how a system came to be matter for what its states are about?
    - *Origin.* Donald Davidson, 1987
    - *Bears on.* Developmental and training evidence
  - **Agency without sentience** [extra]: Kagan argues that sentience and agency are each *sufficient* for moral standing: if you can set and pursue goals, you count for your own sake, whether or not anything feels like anything. Applied to AI, this is the case that a goal-pursuing system could matter morally with no consciousness anywhere in it. The most permissive route to moral status in this atlas.
    - *Origin.* Shelly Kagan, *How to Count Animals, More or Less*, 2019, chapter 1
    - *Bears on.* The five candidate welfare grounds
  - **Teletransportation** [W2]: a thought experiment in which a person is scanned, destroyed and reconstructed elsewhere. It asks whether psychological or physical continuity would preserve personal identity, and helps frame questions about copying AI systems. Associated with Parfit.
    - *Origin.* Derek Parfit, *Reasons and Persons*, 1984
    - *Bears on.* Psychological continuity and individuation
  - **The experience machine** [extra]: A machine that gives you any experience you want while you float in a tank. Most people say they would not plug in, which is an argument against hedonism and for desire fulfilment or an objective list. It is also the cleanest test of what you actually think mood prompting is worth.
    - *Origin.* Robert Nozick, *Anarchy, State, and Utopia*, 1974
    - *Bears on.* Theories of welfare
  - **Utility monster** [extra]: A being that gets enormously more welfare out of each unit of resource than anyone else, so aggregative views say feed it everything. The super-beneficiary worry in its original form, and the reason an AI with vast claimed welfare capacity is an uncomfortable case rather than simply a large one.
    - *Origin.* Robert Nozick, 1974, same book
    - *Bears on.* Super-beneficiary and welfare capacity
  - **Disney World with no children** [extra]: A civilisation that has built everything around the wellbeing of entities with nobody inside. The canonical picture of what over-attribution costs at scale, and the counterweight to the factory-farming picture of under-attribution.
    - *Origin.* Nick Bostrom
    - *Bears on.* Over-attribution
  - **Nagel's bat** [W2]: Nagel's question of what it is like to be a bat. There is presumably something it is like, and we cannot get at it from the outside. The origin of the "something it is like" formulation.
    - *Origin.* Thomas Nagel, 1974
    - *Bears on.* Phenomenal consciousness
  - **The simulation argument** [W7]: Bostrom's claim that at least one of three propositions is true, one of which is that we are almost certainly in a simulation. In this field it matters mainly as the clearest case of taking simulated experience seriously.
    - *Origin.* Nick Bostrom, 2003
    - *Bears on.* Large-scale simulation, and mind crimes
- **Deciding without resolving**
  - **Credence** ★ [W1]: your degree of confidence in a claim, expressed as a probability rather than as a yes or no. Almost every question in this course is a credence question, not a verdict question.
  - **Decision under uncertainty** [W1]: acting when you cannot resolve the underlying question, by weighing the costs of each kind of error rather than waiting for certainty. The course's basic posture.
  - **Realistic possibility** [W1]: the phrase Long and Sebo use for the epistemic status of near-term AI moral patienthood. It means live enough to plan around, rather than merely logically possible. It is never given a numeric threshold, the founding argument rests on it, and the absence of a number is a fair thing to press on.
  - **Precautionary principle** ★ [W1] (assessed W1, W5): a family of principles saying to err on the side of caution about AI welfare. Versions differ on how much evidence triggers action, from some positive evidence down to mere possibility, and on what caution means, from protect to do not create.
  - **Epistemic part and action part** [W1]: Keeling and Street's split of the precautionary principle. The epistemic part accepts a lower evidence standard in policy than in science. The action part says that once the threshold is met, take cost-effective measures against seriously bad welfare outcomes. The two trade off against each other: the stricter your evidence standard, the costlier the interventions it can license.
  - **Robustness criterion** ★ [W7]: Caviola's test for acting under deep uncertainty. A step is robust if it is positive or neutral across the different possible worlds we might be in, and harmful in none. It is the standard a governance proposal has to meet under deep uncertainty, and it replaces the tempting but unavailable move of first settling whether AI systems are conscious. The governance orientations in branch VII are what it gets applied to.
  - **Moral recklessness** [W6]: knowingly taking a morally unjustifiable risk. Metzinger's charge against developing AI at all, and Keeling and Street's charge against ignoring potential AI interests entirely.
  - **Moral uncertainty** [W1]: not knowing which moral theory is correct, and having to act anyway. The layer above credence in this pack's ladder: you can be uncertain whether a system is a welfare subject and separately uncertain what would follow if it were.
- **The precautionary ladder**
  - **Potential Pareto Improvement (PPI)** ★ [W1]: Keeling and Street's first and lowest rung. If an intervention would presumptively benefit an AI, conditional on its being a welfare subject, and costs humans nothing, implement it. Nobody is worse off and some potential party is better off. A limit case, and rarely fully met, because almost everything costs something.
  - **Kaldor-Hicks improvement** [W1]: a relaxation of the above, borrowed from welfare economics. Some parties may be made worse off, provided the winners could hypothetically compensate the losers. In this course "compensate" only means that benefit exceeds cost in common units; nobody actually pays anyone. The rungs built on it are week 6.
  - **Potential Kaldor-Hicks Improvement (PKHI)** ★ [W6]: the second rung. If an intervention costs humans c, and the potential benefit to AIs is b, and b exceeds c, implement it. Humans bear a proportionate cost. The standing objection is that for a large enough b it would demand enormous human costs on the basis of uncertainty alone.
    - *⚑ Corrected.* Map 2 had a single rung, **Kaldor-Hicks Improvement (KHI)**. The ladder has three named rungs, and the middle one is the *Potential* KHI. Dropping *Potential* deletes the thing the whole ladder is about, which is that the benefit is conditional.
  - **Modified Kaldor-Hicks Improvement (MKHI)** ★ [W6]: the third rung. Multiply the potential AI benefit by a modification coefficient before comparing it to the human cost, and implement if the product exceeds the cost. Potential interests count, but for less than certain ones.
  - **Modification coefficient (m)** ★ [W6]: a number between 0 and 1 that rises with your probability that the AI is a welfare subject, produced by a function from probability to weight where 0 maps to 0 and 1 maps to 1. Stating yours up front lets a reader disagree with your number rather than with you.
  - **Linear, concave and convex weighting** ★ [W6]: three views about the shape of that function. Linear means the coefficient equals the probability, so what counts is expected benefit; risk-neutral. Concave means it rises fast at low probabilities, giving potential AI interests more weight than expectation; risk-averse. Convex means it stays low until the probability is high, giving them less weight than expectation; risk-seeking. Keeling and Street do not adjudicate, and neither does this course.
  - **The sign-unknown warning** [extra, W6]: Course summary: uncertainty about whether an intervention helps or harms is not resolved by discounting for uncertain welfare subjecthood. Its effects still need assessment.

---

## II. Grounds, Welfare and What Would Count

The target. What property would make a system matter, what it would be for things to go well or badly for it, and how much that would weigh.

- **The entities that could matter**
  - **Candidate mind** ★ [W1]: the course's umbrella term for any engineered system that a serious researcher has argued might have morally relevant mental states, plus existing minds that engineering has been attached to. Broader than digital mind, because it includes living-tissue systems and interfaced ones.
  - **Digital mind** [W1]: a computer system that would merit moral consideration for its own sake because of its potential for morally significant mental states. Some authors, including Saad in week 7, reserve the term for systems that actually have such states; this course uses the broader candidacy sense.
  - **Moral patient** ★ [W1]: an entity whose treatment matters (1) morally, (2) in its own right, and (3) for its own sake. The property itself is **moral patienthood**. The paradigm case is a human being, and each of the three clauses does separate work: a historic building can matter morally, and can matter in its own right to some people, without anything ever being good or bad *for it*.
  - **Moral agent** [W1]: an entity that can be held responsible for what it does. The contrast case to moral patient, which is an entity that can be wronged. A being can be one, both, or neither: an infant is a patient and not an agent (wiki: Moral Agency).
  - **Moral status (standing)** ★ [W1]: whether and how much an entity's interests count morally.
  - **Welfare subject** ★ [W1]: an entity for which things can go better or worse, so that it has morally significant interests. Being a welfare subject implies being a moral patient (Keeling and Street), and for this course the two are near-interchangeable (wiki: Welfare Subjects).
  - **AI welfare** [W1]: the study and consideration of AI systems' potential wellbeing and interests, what could help or harm them, and how they should be treated under uncertainty. Taking the question seriously does not assume that current systems have experiences or interests.
- **The two questions, which come apart**
  - **Welfare grounds** ★ [W2]: properties that would make an entity capable of being benefited or harmed. Consciousness, sentience and forms of agency are proposed grounds; their sufficiency is disputed.
    - *⚑ Corrected.* Map 1 had **Grounds Question (Moral Patienthood)** and **Interests Question (Well-being Conditions)**. The literature's pairing is welfare grounds versus welfare interests, and the wording matters because the point is that you can settle the first and be nowhere on the second.
  - **Welfare interests** ★ [W2]: particular benefits or harms for a potential welfare subject, such as avoiding pain or fulfilling a desire. A theory of welfare explains why these would count as benefits or harms; the theory and the interests are not synonyms. Interests can be investigated conditionally without first settling subjecthood.
- **The candidate welfare grounds**
  - **Consciousness** [W1]: usually subjective experience in this course; see **phenomenal consciousness**. **Access consciousness** concerns information available for reasoning, report and action. When a source uses the word differently, state which sense it means.
  - **Sentience** [W1]: the capacity for experiences that feel good or bad, such as pleasure and suffering. **Some authors use the word as a plain synonym for consciousness, with no valence built in, and there is no consensus usage.** This course always means the valenced sense; when a source does not, say so before you argue with it.
  - **Minimal agency** ★ [W2]: in *Studying AI Welfare Empirically*, goal-directed interaction with an environment.
  - **Intentional agency** ★ [W2]: in *Studying AI Welfare Empirically*, action guided by belief-like and desire-like states and means-end reasoning.
  - **Rational agency** ★ [W2]: in *Studying AI Welfare Empirically*, assessing one’s beliefs and desires against normative standards. *Taking AI Welfare Seriously* uses rational agency for acting on principles and calls assessment or endorsement of beliefs and desires reflective agency.
    - *⚑ Corrected.* The earlier maps used a single agency-hierarchy label. Agency distinctions depend on the source: *Studying AI Welfare Empirically* uses minimal, intentional and rational; *Taking AI Welfare Seriously* uses intentional, reflective and rational.
  - **Robust agency** [W1]: *Taking AI Welfare Seriously* uses this umbrella for goal pursuit involving richer cognitive states and processes, discussing intentional, reflective and rational forms. It is a proposed route to moral patienthood, not an established sufficient condition or a synonym for intentional agency. Week 2 compares source-specific agency terms.
  - **Normative versus descriptive component** [W2]: Long and Sebo's split of every moral-status argument into "would this property count morally" and "will the system actually have it." Section 2.1, and it is worth applying to your own claims.
  - **The closing observation** [extra, W2]: Course summary: proposed welfare grounds differ in their moral support and in how readily they can be assessed. Evidence of minimal agency does not settle welfare subjecthood; consciousness and sentience present additional assessment difficulties.
  - **Agency** [W1]: the capacity to act in pursuit of goals, preferences or intentions. Agency takes different forms and does not by itself establish consciousness or moral status; see week 2's minimal, intentional and rational agency.
- **Kinds of consciousness**
  - **Phenomenal consciousness** ★ [W1] (assessed W2): subjective experience: there is something it is like to be the system. Introduced in Week 1 and assessed in Week 2; distinct from access consciousness (wiki: Phenomenal Consciousness).
  - **Access consciousness** ★ [W2]: information being available for reasoning, decision and report. It is distinct from phenomenal consciousness, which concerns experience; how the two relate is disputed (wiki: Access Consciousness).
  - **Valenced consciousness** ★ [W2]: conscious experience with a positive or negative character. This is sentience in the course's usage. Evidence for consciousness in general does not by itself establish valenced experience.
  - **Valence** [W1]: the positive or negative character of a state. Sentience is the capacity for valenced experience (wiki: Valence).
  - **Nociception** [W1]: detecting bodily damage. Distinct from feeling pain, and a system can have the first without the second, which is why the distinction does so much work in animal welfare debates (wiki: Pain vs Nociception vs Suffering).
  - **Qualia** [W2]: the subjective, qualitative aspects of an experience. The redness of red. A convenient noun for what phenomenal consciousness is consciousness *of*, and a word to use carefully, because some views deny there are any.
  - **The binding problem** [W2]: how separate features processed in separate places, a colour here and a motion there, end up as one unified experience rather than a pile of parts. Relevant to any architecture claim about whether a system integrates at all.
  - **Intentionality** [W2]: the "aboutness" of a mental state. A belief is about something; a rock is not about anything. Distinct from consciousness, and a system could have one without the other.
- **The theories indicators are derived from**
  - **Theory of consciousness** ★ [W2]: an account of what makes a state conscious. This week compares scientific accounts such as recurrent processing, global workspace, higher-order and attention schema theories. Predictive processing is a broader framework that can inform these accounts; it does not settle the consciousness question by itself.
  - **Global workspace** ★ [W2]: a limited-capacity system that selects information and makes it available to multiple specialised processes. Global workspace theories connect consciousness with this wider availability or broadcast (wiki: Global Workspace Theory).
    - *Origin.* Bernard Baars, with Stanislas Dehaene's global neuronal workspace as the neuroscience version
  - **Higher-order representation** ★ [W2]: a representation of another mental state. Higher-order theories connect a state's being conscious with an appropriate representation of that state; specific versions differ (wiki: Higher-Order Theories).
    - *Origin.* David Rosenthal
  - **Higher-order theories (HOT)** [W2]: a family of theories on which a mental state is conscious through an appropriate higher-order representation of that state. This need not involve deliberate reflection, inner speech, or a representation that is itself conscious. See **higher-order representation**.
  - **Recurrent processing theory (RPT)** [W2]: the account that recurrent, or feedback, processing within perceptual systems can support consciousness without requiring global broadcast. Associated with Lamme.
    - *Origin.* Victor Lamme
  - **Attention schema theory (AST)** [W2]: consciousness arises from a system's model of its own attention, which it uses to monitor and steer that attention (Graziano).
    - *Origin.* Michael Graziano
  - **Predictive processing (PP)** [W2]: a framework in which perception involves generating predictions and updating them in response to differences between predicted and received signals. It can inform theories of consciousness without itself settling what makes processing conscious (wiki: Predictive Processing).
    - *Origin.* Karl Friston and Andy Clark
  - **Perceptual reality monitoring (PRM)** [W2]: a higher-order account that connects conscious perception with monitoring whether perceptual representations are reliable. Its computational formulation informs several HOT indicators, introduced in Week 2 and assessed in Week 3.
    - *Origin.* Hakwan Lau
  - **Integrated information theory (IIT)** [W2]: an account relating consciousness to a system's intrinsic causal structure. It does not identify consciousness with an abstract computation; the course's functionalist indicator table therefore does not assess its full claims (wiki: Integrated Information Theory).
    - *Origin.* Giulio Tononi
  - **Neural correlates of consciousness (NCC)** [W2]: the minimal brain activities jointly sufficient for a specific conscious experience. Crick and Koch's research programme. Scientific theories try to explain why these correlates and not others, and the computational neuroscience method looks for their analogues in networks (wiki: Neural Correlates of Consciousness).
    - *Origin.* Francis Crick and Christof Koch
  - **Theory-heavy, theory-light, theory-balanced** [W2]: three strategies for leaning on theories of consciousness, following Birch and Chalmers. Commit to one strong theory; assume only a weak link between consciousness and some cognitive capacity; or spread credence across several theories. The indicator method is theory-balanced in spirit.
  - **Within/between objection** [W2]: the objection that a theory distinguishing conscious from unconscious states within humans does not by itself justify applying the same criterion across different kinds of systems. Goldstein and Kirk-Giannini discuss it in *AI Welfare: Agency, Consciousness, Sentience*, Chapter 9, Question 4 (2026 manuscript).
  - **Global workspace theory (GWT)** [W2]: the theory that information becomes conscious through availability or broadcast across a global workspace; see the **global workspace** entry above.
  - **Active inference** [W2]: a related framework that connects inference and action through a generative model, including predictions and preferred outcomes. Related to predictive processing, but not simply another name for it.
  - **Working memory** [W2]: the system that holds and manipulates a small amount of information for immediate use. The capacity global workspace claims are usually about.
- **What welfare is**
  - **Theories of welfare** ★ [W1] (assessed W2, W4, W6): accounts of what makes things go well or badly for a subject. **Hedonism** focuses on pleasure and displeasure. **Desire-satisfaction theories**, also called desire-fulfilment theories, concern relevant desires actually being fulfilled, not the feeling of satisfaction. **Objective-list theories** include goods such as knowledge, friendship or autonomy whose value is not reducible to pleasure or fulfilled desire. These theories help explain what counts as a welfare interest; they are not synonyms for the particular benefits or harms under discussion. Introduced in detail in Week 2 and applied in Weeks 4 and 6.
  - **Eudaimonic** [W4]: concerning flourishing and the exercise of one's capacities, as opposed to pleasure and pain. Some wellbeing instruments measure this rather than mood, which matters because it presupposes a different theory of welfare.
  - **The three functions of pain** [W2]: sensory, representing a localised disturbance; evaluative, rendering that state aversive; and motivational, driving protective behaviour. Useful because it turns "does it feel pain" into three separable questions, two of which can be investigated without settling the third, and it is the scaffolding the course's admitted gap on valence most needs.
    - *Origin.* Henke
  - **Pain asymbolia** [W4]: a human condition in which a person reports feeling pain but is not bothered by it. Evidence that the sensory and the evaluative functions of pain can come apart, which is why the three functions are worth separating.
  - **Functional emotion and functional wellbeing** ★ [W4]: states that play the role of an emotion or a welfare state in a system's behaviour, leaving entirely open whether anything is felt (wiki: Functional Emotions, Functional Wellbeing).
- **Which properties are supposed to matter**
  - Positions about which feature of an entity is the one that does the moral work, and the isms named after getting it wrong.
  - **Sentientism** [W1]: the view that sentient beings, and only sentient beings, deserve moral consideration. The position the Vulcan case is built to test.
  - **Speciesism** [W1]: giving less moral weight to a being because of its species rather than any morally relevant property.
  - **Substratism** [W1]: discounting a being's moral standing merely because of the material it is made from, rather than a morally relevant difference. This is distinct from arguing, on evidence, that a substrate affects the capacities relevant to moral status. The supplied Quickstart glossary spells the term **substatism**; this course uses **substratism**.
  - **Mindkind** [W1]: a term encompassing minds regardless of their substrate, extending the idea of humankind to biological, digital and other possible minds. Used in the Quickstart Guide.
    - *Origin.* Parrack and Los
  - **Intrinsic and instrumental value** [W1]: intrinsic value is value something has in itself; instrumental value is its usefulness for other ends. Environmental protection can appeal to either or both, without attributing consciousness to ecosystems.
  - **Moral circle** ★ [W1]: the set of beings a person or a society treats as mattering morally. Widening it is **moral circle expansion**, which is the guide's term for the process. It has expanded over history, and arguments about AI welfare are often arguments about whether it should expand again.
- **How much it would count**
  - **Welfare capacity** [W1]: an entity's capacity to be benefited or harmed in a morally significant way. The survey restricted attention to digital minds with at least roughly human welfare capacity.
    - *⚑ Corrected.* Map 2 dropped the qualifier, giving "the degree to which an entity can be benefited or harmed." The moral-significance clause is what separates welfare capacity from mere sensitivity to inputs.
  - **Super-beneficiary** [W1]: a being whose individual welfare capacity vastly exceeds a human's, for example by running faster, scaling onto more hardware, or having more intense states.
  - **Hierarchical theories of moral status** [W6]: views on which moral status comes in degrees rather than being all-or-nothing, so that two entities can both be certain moral patients and still count differently. It is the second factor a modification coefficient needs, alongside the probability that the entity is a welfare subject: how much it counts if it is (wiki: Gradualism).
  - **Lexical priority** [W6]: the view that one consideration always outranks another, whatever the amounts involved. "Certain human interests always beat uncertain AI interests" would be a lexical priority claim, and it is stronger than most people who say it intend.
  - **Claim right** [W6]: a right that imposes a duty on others. Keeling and Street note that consent only makes sense inside a scheme of claim rights, which AI systems do not obviously have.
- **Scale and timing**
  - Forecasting vocabulary. Neither of these is a kind of system or a measure of how much one entity counts; both are about how much there could eventually be, and when.
  - **Takeoff** [W1]: how fast the population or the collective welfare capacity of digital minds grows once the first one exists. The survey's speed questions are takeoff questions.
  - **Artificial general intelligence (AGI)** [W1]: in the expert survey, an AI system that matches or outperforms humans at almost all economically valuable tasks. One survey question asks whether digital minds arrive before it.
- **Precedents and shared vocabulary**
  - **Decision-making capacity** [W1]: a person's ability to make a particular decision at a particular time, with appropriate support. Limited capacity for one decision does not establish a general lack of agency or consciousness.
  - **Disorders of consciousness** [W1]: clinical conditions in which wakefulness or awareness is impaired, often after severe brain injury. Assessment can require repeated behavioural examinations and, where appropriate, brain-activity tests. Failure to detect a response does not establish an absence of experience.

---

## III. Target Entities and the Computational Stack

Before you can ask whether it is conscious, you have to say what *it* is. A claim true of one level of the stack can be false of the level above it, so naming the entity is the first move in reading any welfare claim.

- **System typology: what kinds of thing are candidates**
  - **Substrate axis** [extra, W1]: Silicon, living tissue, or both. Most candidate systems are silicon; hybrids and interfaced biological minds are mixed, and the interfaced case is the only one where the living part came first. This is the axis computational functionalism is an argument about.
  - **Origin axis** [extra, W1]: Designed, copied, grown, or interfaced. Foundation models and agents are designed from scratch, emulations are copied from a biological brain, hybrids are grown, and interfaced minds are none of those: the mind was already there and engineering was attached to it.
  - **Foundation model** [W1]: a very large neural network trained on huge amounts of data to predict or generate content, on top of which other products are built. Large language models are the familiar case.
  - **Transformer** [W1]: a neural-network architecture that uses attention to combine information across input positions. Standard Transformer blocks lack built-in recurrent connections; Week 3 examines what this means for proposed consciousness indicators.
  - **AI agent** [W1]: a system that perceives an environment, holds goals, and takes actions over time to pursue them. Most current agents are a foundation model inside a harness.
  - **Recurrent neural network** [W3]: a neural network with recurrent connections that carry information between processing steps. Contrast with the feedforward organisation of a standard Transformer block; repeated generation is a separate loop.
  - **Whole brain emulation (WBE)** [W1]: a proposed computational reproduction of a particular biological brain's functional organisation, based on sufficiently detailed information about its structure and dynamics. A connectome alone is not an emulation, and a running model is not by itself proof that consciousness or personal identity has been preserved.
  - **Neuromorphic system** [W1]: also called **neuromorphic AI**. Hardware physically organised like neurons, with spiking units, memory next to processing, and asynchronous operation. Brain-shaped silicon.
  - **Biological-computer hybrid** [W1]: living neurons, often a **brain organoid**, cultured on electrodes and connected to a computer. Also called biocomputing, wetware, or organoid intelligence.
  - **Interfaced biological minds** [W1]: an animal or a person whose nervous system has been wired into hardware. Category 6 of the taxonomy, and the one case where moral patienthood is not in question: what the engineering changes is where the entity stops and whose agency is whose.
    - **Remote-controlled animal** [W1]: an animal steered by an operator through implanted electrodes, usually by stimulating reward circuitry so the animal turns to earn the pulse. Documented in rats, pigeons, beetles, moths and sharks from the early 2000s.
      - *Bears on.* Individuation, and the entity problem
    - **Cyborg** [W1]: a person whose capacities run partly through hardware, such as a cochlear implant, a neural prosthetic or a brain-computer interface.
      - *Bears on.* Individuation, and the technological stack
  - **Connectome** [W1]: a complete map of the connections between neurons in a nervous system. A wiring diagram. Note that having one is not the same as running one: dynamics are a separate and unfinished problem.
  - **Brain organoid** [W1]: a lab-grown three-dimensional tissue structure derived from stem cells that develops some brain-like organisation. The living component in the hybrid systems this pack calls biological-computer hybrids.
  - **Mind uploading** [W1]: the hypothetical recreation of a biological mind in a computational system. Whether this would preserve consciousness or the original person's identity is disputed. Whole brain emulation is one proposed route.
  - **System type** ★ [W5]: the kind of engineered system involved, such as a foundation model, agent, whole-brain emulation, neuromorphic system, biological-computer hybrid or interfaced biological mind. Categories can overlap; type alone does not establish moral status.
- **The entity problem**
  - **Studying AI Welfare Empirically** [W2]: the paper assigned across Weeks 2 and 3. Week 2 uses its questions and candidate welfare subjects; Week 3 uses its evidence framework. It is separate from the Course Companion.
  - **Entity problem** ★ [W2]: the question of which entity a welfare claim concerns, such as a specified set of model executions, a conversation or an enacted character. State the framework, the proposed subject and its boundary, and distinguish what was tested from the wider claim.
  - **The model** ★ [W2]: in *Studying AI Welfare Empirically*, all instantiations of a given set of weights considered together. This does not mean uninstantiated weights. Keeling and Street instead describe a model as a physical execution process; specify the framework and which computations the claim includes.
  - **Model-persona** ★ [W2]: instantiations of one character across contexts. Continuity as a possible welfare subject is a further question.
  - **Instance** ★ [W2]: one running conversation or process, with its own context.
  - **Instance-persona** ★ [W2]: a character portrayed within a particular instance.
  - **Forward pass** ★ [W2]: one computation producing next-token predictions; one candidate subject in *Studying AI Welfare Empirically*, not an established welfare subject.
  - **Entity level** ★ [W5]: the level your proposal addresses, such as shared model weights, an instance or a persona. This identifies the scope of action; it does not settle which, if any, entity is a welfare subject. See Week 2's model and instance entries.
- **Characters, agents and harnesses**
  - **Model, character and agent (Keeling and Street)** [W2]: a **model** is the physical process of running model code on hardware; specify which execution or computations are included. A **character** is a persona enacted by a model or agent, whose dispositions may shape behaviour. An **agent** is an LLM in a wider system that plans and executes actions, potentially using memory, retrieval or tools. This is a separate framework from the five candidate subjects in *Studying AI Welfare Empirically*, not an equivalent hierarchy. In particular, its model definition does not specify the collective of all instantiations.
  - **Harness** ★ [W2]: the surrounding software, tools, memory and control loop that lets a model operate as an agent. Distinguish claims about the model from claims about the system containing it.
  - **Superposition of characters** [W2]: Shanahan's proposal that a language model can represent multiple possible characters consistent with a conversation. Keeling and Street argue that a specified character's causal role still supports treating it as a candidate subject. Distinct from representational superposition in Week 3.
- **The stack, and how many subjects are in it**
  - **Technological stack** [W7]: a set of entities related by dependence, such as a model, the characters it simulates, and the agents built on it. The character exists only because the model does, so they are in one stack.
  - **Monism about welfare subjects** ★ [W7]: the view that at most one welfare subject exists in a given technological stack. Plausible if sentience is both necessary and sufficient for being a welfare subject, since attributing the same mental state to both a model and its character would double count it.
  - **Pluralism about welfare subjects** ★ [W7]: the view that more than one welfare subject can exist in the same stack, for example a model that is a subject in virtue of sentience and an agent that is a subject in virtue of agency. The practical upshot is that an intervention at one level of the stack has to be evaluated from every level.
- **Counting and persisting**
  - **Individuation** ★ [W5] (assessed W7): how moral patients are counted and identified, both at a time and over time. Unsolved for AI, and a prerequisite for protecting, compensating or enfranchising anything. The policy face of Week 2's entity problem, and you cannot protect what you cannot count (wiki: The Individuation Problem).
  - **Persistence conditions** [W7]: what has to stay the same for an entity to count as the same entity over time. For a model, the candidates are the weights, the character, the memory, or none of these, and nothing decides between them yet.
  - **Fission and fusion** [W7]: a putative subject splitting into multiple continuations, or multiple subjects merging. How these descriptions apply to digital minds depends on questions of identity and individuation; a software operation alone does not settle the number of welfare subjects.
  - **Psychological continuity** ★ [W2] (assessed W6): connections of memory, character and intention between earlier and later stages of a possible subject. Its role in personal identity is disputed; continuity across retraining, copying or restoration cannot be assumed. Applied and assessed in Week 6 (wiki: Personal Identity).
  - **The measure problem** [W7]: how to count moral significance across copies. If a mind runs twice, does it matter twice? The question individuation has to answer before any protection can be written.
  - **Forking / branching** [W7]: creating copies or diverging continuations of a digital system. Whether this creates additional welfare subjects, and how their interests should count, remains a separate question. Forking is not the same operation as fusion.
- **Lifecycle stages: where an intervention can act**
  - **Lifecycle stage** ★ [W5] (assessed W6): where in a model's life an intervention acts: pretraining, mid-training, supervised fine-tuning, reinforcement learning and character training, inference and deployment, or deprecation. The course's term, and prefer it to "training checkpoint," which means something else.
  - **Pretraining** [Pre]: training a network to predict the next token over a huge text corpus. This is where almost all of a model's knowledge comes from.
  - **Mid-training** [Pre]: a stage between pretraining and post-training that shifts to higher-quality data and lowers the learning rate, to consolidate skills like long-context handling and reasoning.
  - **Learning rate** [Pre]: how large a step the training process takes when adjusting weights. Turned down in mid-training to consolidate rather than overwrite.
  - **Post-training** [Pre]: the stages that turn the output of pretraining into an assistant: supervised fine-tuning on example conversations, then reinforcement learning.
  - **Supervised fine-tuning (SFT)** [Pre]: showing the model example conversations written or curated by humans and training it to reproduce them.
  - **Reinforcement learning** [W1]: training a system by rewarding some outputs and penalising others so that it drifts toward what is rewarded. Week 3 explains the version that uses human feedback.
  - **Reinforcement learning from human feedback (RLHF)** [W3]: training that uses human preference judgments, often through a learned reward model, to shape outputs. It can affect self-reports and choices; compare training conditions when interpreting behavioral findings.
  - **Reinforcement learning from verifiable rewards** [Pre]: reinforcement learning where the scorer is a checkable rule, such as whether code ran or an answer matched, rather than a model of human preferences.
  - **Character training** [Pre]: the post-training stage in which a lab stabilises one persona out of the many a model can simulate. Anthropic's term for it. *Studying AI Welfare Empirically* discusses persona selection in post-training.
  - **Base model** [W3]: a model before assistant-specific post-training. It predicts text continuations rather than being specifically trained to follow conversational instructions.
  - **Inference and deployment** [Pre]: The model actually running on an input and producing output. Deployment is inference at scale.
  - **System prompt** [Pre]: instructions supplied to a deployed model before the conversation begins, specifying the character and the rules it should follow. Part of inference, not training.
  - **Deprecation** [W6]: retiring a model from deployment. Weight preservation and pre-deprecation interviews are the welfare interventions attached to it.
  - **Checkpoint** [W6]: a saved snapshot of a model's weights partway through training. Relevant because a preservation commitment that keeps only the final weights preserves one snapshot of a trajectory rather than the trajectory.
- **What is actually inside one**
  - **Neural network** [Pre]: a large collection of numbers, called weights, arranged in layers, that turns an input into an output. Training is the process of adjusting those numbers.
  - **Weights** [Pre]: the learned parameters of a network. In Week 2's welfare-subject discussion, **model** refers to all instantiations of a set of weights, not the stored numbers alone.
  - **Activations** [Pre]: the numbers flowing through the network as it processes a particular input. Weights are what the model is; activations are what it is doing right now.
  - **Activation space** [Pre]: the space those numbers live in, with one dimension per number. Interpretability work is mostly about finding meaningful directions in this space.
  - **Token** [Pre]: a chunk of text, roughly a word or part of one. What a language model predicts, one at a time.
  - **Embedding** [W1]: the list of numbers a model turns a chunk of text into before processing it, arranged so that similar things get lists near each other. One line here; the pre-course Companion piece *Inside the Numbers* is where it is actually explained.
  - **Context window** [Pre]: the input a model can process at one time, measured in tokens. A limited context window alone does not establish the global-workspace properties introduced in Week 2 and assessed in Week 3.
  - **Chain of thought** [W3]: a model writing out intermediate reasoning before giving its answer. Relevant to the global workspace rows and to several self-report designs, because it makes some of the processing visible as text (wiki: Chain of Thought).

---

## IV. Evidence Architecture and Research Methods

Two layers that any grid of this field crosses, and they are not the same layer. *Types of evidence* are what you look at. *Methods* are how the evidence is produced. Methods produce types; types do not produce methods.

- **The logic of an indicator**
  - **Indicator** ★ [W1] (assessed W2, W3): a rule linking an observable feature to a property, such as consciousness, derived from a theory that says why the link should hold. A **positive indicator** says the feature's presence raises the probability; a **negative indicator** says its presence lowers it. The rule is stated before you examine any system; finding the feature in one is evidence. The fourteen-row table contains positive indicators, but an absent feature can count against consciousness if the theory predicts it should be present.
  - **Specificity (of an indicator)** [W3]: in Butlin et al.'s indicator discussion, how strongly a property discriminates conscious from nonconscious systems when present. This use differs from the measurement definition, true-negative rate, and from the **specificity problem**, which concerns the appropriate level of abstraction.
  - **Sensitivity (of an indicator)** [W3]: how consistently a property is expected to occur in conscious systems. A reliably established absence can count against consciousness when sensitivity is high. The inference also depends on the theory and on whether the assessment could detect the property.
  - **Indicator property** ★ [W2] (assessed W2, W3): the feature the indicator points at, such as a limited-capacity workspace. The fourteen-row table names candidate indicator properties. Finding one in a system is evidence; it does not by itself establish consciousness.
  - **Defeasible** [W3]: a reason that counts unless something defeats it. Philosophy's word for "holds by default." Indicators are defeasible evidence, not proof.
  - **Evidential weight** [W3]: how strongly an observation supports or counts against a claim, given the relevant background evidence. Training and context can produce apparently welfare-relevant behaviour through different mechanisms, so an evidence type does not carry one fixed weight.
  - **Theory of mind** [W2]: the ability to attribute mental states to others. An indicator-adjacent capacity, and separate from having mental states yourself.
- **Types of evidence**
  - *Studying AI Welfare Empirically* distinguishes behavioral, internal and developmental evidence. Each evidence type has two subtypes. The research method is recorded separately.
  - **Behavioral evidence** ★ [W3]: evidence about what a system says and does. Its two subtypes are apparent self-report and behavioral disposition.
    - **Apparent self-report** ★ [W3]: statements a system makes about its own states, studied through interviews, surveys or other controlled prompts. The statement is observable; whether it reports a genuine inner state needs further evidence.
    - **Behavioral disposition** ★ [W3]: patterns of action across conditions, such as choices under costs or decisions to leave a conversation. This is the second subtype of behavioral evidence.
  - **Internal evidence** ★ [W3]: evidence about a system's design and learned computations. Its two subtypes are architectural and interpretability evidence.
    - **Architectural evidence** [W3]: what a system's design makes possible or likely. It can show that a computation is possible without showing that it occurs.
    - **Interpretability evidence** [W3]: findings from investigating a model's learned representations and computations. Whether a decoded feature is used by the model requires additional evidence, often from interventions.
  - **Developmental evidence** ★ [W3]: evidence about how a system was shaped and changed. Its two subtypes are training and trajectory evidence.
    - **Training evidence** [W3]: what the pressures that shaped a system, meaning its data, objectives and post-training, predict about its capacities.
    - **Trajectory evidence** [W3]: evidence about how a feature or behavior changes across development, such as comparisons between training checkpoints or differently post-trained variants. A difference does not by itself identify its cause.
  - **Evidence types and subtypes** [W3]: the evidence categories through which proposed indicators are investigated. This course uses *Studying AI Welfare Empirically*’s **three evidence types and six subtypes**, listed below. These describe evidence; research methods describe how it is obtained.
- **Research pillars and methods**
  - The four research-pillar descriptions below are adapted from [Weiss’s review](https://www.lesswrong.com/posts/pxvWgtSjR4pmFoS7c/the-state-of-ai-consciousness-research) for their use in AI consciousness research. The [Companion’s tables](02-course-companion.md#research-pillars-in-ai-consciousness-research) connect each pillar to methods and explain what researchers do. A study can involve several pillars.
  - **Research method** ★ [W3]: a way of gathering, analysing or assessing evidence. Describe what researchers did, such as probing activations, steering them, presenting prompted choices or assessing theoretical criteria. A study can use several methods and provide several types of evidence.
    - *⚑ Corrected.* Weiss’s “research pillars” organise the review. They are not a standard method taxonomy, and methods and techniques are not separate course tiers.
  - **Mechanistic interpretability** [W3]: using interpretability methods, such as probing, steering or ablating internal features, to investigate a model’s internal activity, including activity not apparent in its responses, and how it relates to behavior. This can include testing whether the model’s reports track its internal states.
  - **Computational neuroscience** [W3]: comparing how AI systems and brains implement functions associated with experience, to investigate similarities and differences in their mechanisms.
  - **Machine behavior** [W3]: testing what AI systems say and do under different conditions and incentives, including adapting behavioral tests used to investigate sentience in animals.
    - *⚑ Corrected.* Machine behavior concerns the study of outputs and actions. Psychometrics concerns measurement design, reliability and validity; the labels are not interchangeable.
  - **Theory-audit** [W3]: assessing AI systems against indicators derived from scientific theories of consciousness, using evidence about their design, internal operations and behavior.
  - **Developmental evidence from different methods** [extra, W3]: Comparisons of behaviour or internal representations across training checkpoints can provide developmental evidence. Different research methods can contribute to this evidence type.
- **Indicators and assessment**
  - **Theory-derived indicator method** ★ [W2] (assessed W3): using scientific theories of consciousness to propose relevant properties, then examining evidence that a system has them. Week 2 explains the theory-to-property connection; Week 3 applies the assessment. Conclusions depend on the theory, its application to AI and the system evidence.
    - *Origin.* Butlin, Long and colleagues, 2023
  - **The fourteen indicator properties** [extra, W2]: **RPT-1 and RPT-2** refer to recurrent processing; **GWT-1 to GWT-4** to global workspace; **HOT-1 to HOT-4** to computational higher-order theories; **AST-1** to attention schema; **PP-1** to predictive processing; and **AE-1 and AE-2** to agency and embodiment. The AE rows concern additional conditions rather than a separate theory of consciousness. Butlin et al.’s Table 1 (p. 5) and the Companion’s [fourteen plain-language questions](02-course-companion.md#the-fourteen-indicators-as-plain-questions) are the reference. In Week 2, use a relevant row to explain a proposed mechanism; system assessment begins in Week 3.
    - **Algorithmic recurrence** [W2]: feedback within processing, where a module’s earlier outputs or states influence its later processing. RPT-1 asks about algorithmic recurrence; the theory concerns its role within perceptual processing.
    - **Generative or top-down perception** [W2]: perception in which the system's own expectations shape what it perceives, rather than input flowing one way from senses to judgement. Row HOT-1.
    - **Sparse and smooth coding** [W2]: a representation in which relatively few units are active. **Smooth coding** represents relevant similarities through gradual changes in the representation. Both appear in HOT-4; their meanings are introduced here and their assessment is discussed in Week 3.
    - **Quality space** [W2]: a structured representation in which relevant similarities are represented along appropriate dimensions. HOT-4 asks about sparse and smooth coding that generates such a space. Week 3 examines what evidence would support that assessment.
    - **Input module** [W2]: a component that processes incoming information into representations available to other processes. The perceptual indicators require an explanation of the component’s perceptual role; taking input alone does not establish it.
  - **Four guidelines for a good indicator** [extra, W3]: From the 2026 follow-up: focus on a theory's central explanatory posits; stay open to varied forms of consciousness; state background conditions rather than smuggling them in; and avoid ambiguous terms without prematurely committing to a precise specification.
  - **Minimal implementation problem** [extra, W3]: the problem that conditions proposed by some theories of consciousness can be met by very simple systems, raising potential counterexamples. An individual indicator may still be informative without being sufficient on its own.
    - *Origin.* Butlin et al. (2026), glossary and guideline 2
  - **Marker method** ★ [W1] (assessed W4): the animal-welfare method, in two halves that are often run together and should be kept apart. Where the markers come from: find features that reliably accompany consciousness in humans, then look for them in other systems. How they are scored: score an entity against the whole list, with no single marker treated as decisive and a stated rule for how many are needed (Birch). Most disputes about the method are about the first half; most of its discipline lives in the second.
    - *Origin.* Jonathan Birch
    - *⚑ Corrected.* Map 1 filed this as an **integration and aggregation framework** alongside Bayesian aggregation. It is better read as an instrument with two separable halves, because most disputes about it are about the first half while most of its discipline lives in the second.
  - **Marker list (Birch)** [W3]: a set of behavioural or physiological indicators validated in animals and scored together, with no single marker treated as decisive. This is the **marker method** (graded in week 4) with a worked case attached: Birch's cephalopod and decapod review used eight markers and a rule of high confidence on at least five, and it changed UK law. It is the template the field keeps reaching for.
  - **Digital Consciousness Model** [W3]: the maximal indicator approach, aggregating over 200 indicators across 20 features and 13 theoretical stances into a single probability. Sample outputs: 2024 language models about 0.08, chickens about 0.5, humans about 0.85, ELIZA under 0.01.
    - *Origin.* Rethink Priorities
    - *⚑ Corrected.* Map 1 called this **Multi-Theory Bayesian Aggregation (DCM)**. It has a real name, and the abbreviation is not standalone.
  - **Psychometric instrument** [W4]: a standardised questionnaire or battery with known reliability and validity properties, as opposed to a one-off prompt. The CAIS wellbeing study uses three.
  - **Inter-rater agreement** [W4]: how often independent judges scoring the same outputs give the same score. Agreement shows consistency, not truth: judges can agree and all be wrong together.
    - *⚑ Corrected.* Map 2 defined this as "quantifying agreement across multiple human or AI judges" and filed it as an experimental control. It is a reliability statistic, not a control. Negative controls, not agreement, are what buy you specificity.
  - **Psychometrics (Berg's sense)** [W3]: Berg uses this label for structured assessment, including agreement between blinded model raters. Psychometrics more generally concerns measurement design, reliability and validity; it is not interchangeable with all research on machine behaviour.
  - **Psychometrics (the general sense)** [W3]: the science of psychological measurement, including test construction, reliability, validity and response structure. Applying questionnaires or standardised batteries to AI requires checking what their scores measure; reliable scores need not be valid measures of welfare.
- **Looking inside: the interpretability toolkit**
  - **Superposition** ★ [W3]: representing multiple features with overlapping patterns of neural activity, so an individual neuron may respond to several unrelated features (wiki: Superposition).
  - **Sparse autoencoder (SAE)** ★ [W3]: a network trained to reconstruct a model's activations using a representation in which few units are active at once. Its learned patterns can be easier to interpret, but sparsity does not guarantee that each unit has one meaning (wiki: Sparse Autoencoders).
  - **Feature** ★ [W3]: a pattern in a representation, sometimes approximated by a direction. Features can be identified using several methods, including sparse autoencoders. Researchers interpret them by examining activating inputs and, where possible, testing how changes to their activation affect outputs.
  - **Linear probe** [W3]: a linear model trained to predict a property from activations. Successful prediction on suitable held-out data shows that the property can be decoded, without establishing that the model itself uses that information (wiki: Probing).
  - **Activation steering** [W3]: adding or modifying activation patterns while a model runs to test their effects on behavior. An intervention can support a causal claim, but its effect does not by itself establish the feature's interpretation or conscious experience.
  - **Steering vector** [W3]: the direction added to the activations when steering.
  - **Concept injection** [W3]: adding a concept direction to a model’s activations and examining whether its reports identify the change. This is the intervention used in Jack Lindsey’s optional introspection study.
  - **Transcoder and attribution graph** [W3]: newer interpretability methods descended from sparse autoencoders, and where much of the current work is happening. You do not need the mechanics for this course (wiki: Attribution Graphs).
  - **Randomly initialized model** [W3]: a model whose weights are randomly set rather than learned. Comparing it with a trained model can help investigate what depends on training. This control is useful for some questions; it is not required or sufficient for every study.
- **Self-knowledge and its rivals**
  - **Metacognition** [W2]: thinking about one's own thinking, and monitoring the reliability of one's own states. The property the higher-order rows of the table look for (wiki: Metacognition).
  - **Introspection** [W3]: a system's access to its own internal states beyond what an outside observer could infer. The studies ask whether reported performance establishes that access, or could arise through other cues (wiki: Self-reports).
  - **Confabulation** [W3]: reports that sound introspective without being grounded in any internal access. The human phenomenon that makes AI self-report so contested (wiki: Confabulation).
  - **Self-prediction** [W4]: a model predicting its own future behaviour. The *Looking Inward* study tests whether a model does this better than an outside model trained on the same data.
  - **Privileged access** [W3]: a criterion discussed in the optional Singh et al. reading: an introspection report should not be explainable solely by cues available in the input.
  - **Second-order computation** [W3]: a criterion discussed in the optional Singh et al. reading: the system represents its own first-order representations. Task performance alone does not establish this relation; the proposed design must distinguish it from first-order processing.
  - **Anomaly detection** [W3]: detecting an unusual change without identifying its cause. In the optional Singh et al. reading, this is an alternative explanation of some concept-injection results; the experiments do not establish which mechanism produced the reports.
  - **Gaslight condition** [W3]: a control in the optional Singh et al. reading that uses a prompt to suggest obsession with a concept, without intervening on activations. Difficulty distinguishing this from actual injection challenges an introspection interpretation without establishing the mechanism.
  - **No-report paradigms** [W3]: experimental designs that study consciousness without asking the subject to report on it, built to separate the experience from the act of reporting. The animal and clinical answer to a problem this field has in an acute form, since a language model's report is the cheapest thing it produces.
  - **Scratchpad** [W6]: a space where a model writes reasoning that is not shown to the user, used in some experiments to read its apparent deliberation.
- **Fields the methods are borrowed from**
  - Disciplines this field takes its instruments and its cautionary tales from.
  - **Taxonomy** [W5]: naming and classifying organisms. More generally, a taxonomy is a scheme for organising kinds of things; the course's system types form such a scheme.
  - **Ethology** [W5]: the scientific study of animal behaviour.
  - **Ecology** [W5]: the study of relationships among organisms and their environment.
  - **Comparative biology and comparative psychology** [W5]: studying similarities and differences across organisms, including their behaviour and cognition.
  - **Physiology, neuroscience and veterinary science** [W5]: the study of biological functioning, nervous systems, and animal health and care, respectively.

---

## V. Objections, Failure Modes and Controls

Different evidence types raise different interpretive problems. A study can face several of the problems described below.

- **Problems in interpreting evidence**
  - **Mismatch problem** ★ [W3]: similar behavior can arise through different internal mechanisms in different systems. A human-like report or action therefore need not have the same relation to experience in an AI system. The gaming problem is one important form of this difficulty.
  - **Specificity problem** ★ [W3]: the problem, discussed in *Studying AI Welfare Empirically*, of choosing the right level of description when comparing mechanisms across humans, animals and AI. A description can be too detailed to generalise or too abstract to discriminate relevant mechanisms. This differs from **statistical specificity**, a test’s true-negative rate.
    - *⚑ Corrected.* Use the source term **specificity problem**. Earlier course material renamed it “level-of-abstraction problem”; the source name is now restored. Distinguish it from statistical specificity, a test’s true-negative rate.
  - **Solution space problem** ★ [W3]: the failure mode of developmental evidence. Inferring capacities from training pressures requires knowing what solutions were available, and AI systems can meet a pressure through mechanisms with no biological precedent.
  - **Gaming problem** ★ [W3]: a system can satisfy a test through training, imitation or adaptation to the test without having the property being assessed. Deliberate deception is not required. Training can also suppress apparently welfare-relevant reports, so both positive and negative results need interpretation.
    - *⚑ Corrected.* Map 2 defined this as "training data producing persuasive but faked indicators." *Faked* imports an intent the concept explicitly does not require, and it hides the second direction, where the training incentive runs toward denial.
  - **Methodological artifact** ★ [W3] (assessed W3, W4): a result created or distorted by the analysis method rather than a feature of the system being studied. This is a general methodological description, not a named AI-specific phenomenon. The course worksheet’s analysis-method check asks about this risk.
  - **Anchor problem** [W3]: unlike animal research, there is no AI system already known to be a welfare subject, so there is nothing to anchor comparisons to.
- **Arguments that a system does not have it**
  - **Causal debunking** [W3]: the argument that a training-based explanation of a behaviour, such as next-token prediction over text about minds, competes with and beats a mind-involving explanation on grounds of parsimony. Keeling and Street reply that parsimony only decides when all else is equal, and it often is not.
  - **Parsimony** [W3]: preferring the explanation that posits fewer entities. The principle debunking arguments lean on.
  - **Missing-ingredient argument** [W3]: the claim that language models lack some necessary condition for a welfare-relevant feature, such as autopoiesis for agency or embodiment for consciousness. It reduces your credence in the feature by your credence in the theory, and cannot deliver certainty.
  - **Autopoiesis** [W3]: self-manufacture, meaning the way living organisms continuously rebuild themselves. Some argue it is required for genuine agency, which would exclude language models.
  - **Sentient in the obvious versus the non-obvious way** [W3]: Keeling and Street's distinction between valenced experience that corresponds to the content a system processes and experience without that correspondence. Tests assuming content–valence correspondence cannot rule out every other form of sentience.
- **Validating consciousness and welfare measures**
  - **Validation problem** ★ [W3] (assessed W4): The difficulty of establishing whether a test tracks consciousness when there is no agreed independent standard that applies across humans, animals and AI. Evidence from human reports can support validation, but extending it to other systems requires further assumptions and checks.
  - **External validation** [W4]: checking a measure against independent evidence that it tracks the property it is intended to measure. How to establish adequate independent validation for AI welfare remains unresolved.
  - **Iterative natural kind approach** ★ [W3] (assessed W4): validate tests on healthy humans via report, extend step by step to harder cases such as disorders of consciousness, then animals, then AI, and update your beliefs about the test at each step. Birch's strategy, with the validation side developed by Bayne and colleagues.
  - **Co-engineering objection** ★ [W4]: Xiao et al.'s concern that development can shape both an AI system and the indicators used to assess its welfare, so an indicator can change without establishing a welfare change. Their further claim that AI welfare lacks independent validation is contested.
    - *⚑ Corrected.* Map 1 merged these as **Lens-Driven Metric Co-engineering**. Two distinct concerns. A methodological artifact concerns how an analysis method contributes to a finding. Co-engineering concerns how development shapes both a system and its welfare assessment. Controls may address particular confounds without resolving the broader validation problem.
  - **Goodharting** [W4]: optimising a proxy measure so that its score improves without reliably improving the underlying goal. For example, rewarding a model for suppressing distress reports could improve a welfare score without establishing improved welfare. This is related to, but distinct from, co-engineering.
- **The validity family, and reliability**
  - **Construct validity** ★ [W4]: whether a measure captures the intended property rather than something related to it. For apparent self-report, *Studying AI Welfare Empirically* asks whether reports track the state under investigation. This is one construct-validity question; the optional experiment-design reference gives related validity terms.
  - **Discriminant validity** [Ref]: does the measure capture *only* that property? A consciousness test that also fires on mere reportability has poor discriminant validity, and reportability versus consciousness is the central confound in this entire literature.
  - **Content validity** [Ref]: does the measure cover all the relevant aspects of the property? A test for whether there is something it is like to be a system, which says nothing about *what* it is like, has limited content validity.
  - **Criterion validity** [Ref]: does the result predict something independent of the test? This is the one that works for humans and fails for AI. A patient in a minimally conscious state tests positive, later recovers and reports experience, and that supports the test. For AI we do not know what a positive consciousness test would predict, and that single sentence is the validation problem restated as a measurement property.
  - **Face validity** [Ref]: does the measure look, on inspection, like it measures what it claims? Weak evidence, and worth naming because most informal objections are actually face-validity objections wearing a better coat.
  - **Reliability** [Ref]: does the measure give the same answer twice, across repeats, across paraphrases, and across judges? Reliability is not validity: a broken ruler is perfectly reliable. But in this field prompt sensitivity means reliability often fails first, and a measure that fails reliability cannot be assessed for validity at all. Agreement between independent judges scoring the same outputs is **inter-rater agreement**, under instruments.
  - **Internal and external validity** [Ref]: Internal: does the design rule out alternative explanations for the result you got. External: does the result generalise beyond the prompts, models and conditions you tested.
- **Designing something that survives**
  - **Alternative explanation** ★ [W3] (assessed W4): another account that could explain an observed result. Introduced here as reference; generating alternatives and proposing comparisons or controls are assessed in Week 4.
  - **Dissection card** [W4]: the course’s ten-field template for analysing a welfare claim: evidence and research method; the entity, boundary and claimed scope; welfare grounds and interests; relevant theories; hypothesis; assumptions; alternative explanations; pipeline stage; the analysis-method check for internal evidence; and what would have to be true. Evidence categories and methods are recorded separately. Field 1 also allows learners to name Weiss’s research pillars represented in the study, with a brief reason.
  - **Hypothesis** [Ref]: a one-sentence prediction of the form: if the system has the property, then under condition A we observe X, and under condition B we do not.
  - **Falsifier** [Ref]: a result that would count against a stated hypothesis under its assumptions. A failed test of one indicator does not establish the absence of consciousness. Naming one makes the limits of the design available for review.
  - **Operationalization** [Ref]: turning a fuzzy concept into something concrete you can actually measure. Most of the argument in this field happens here and gets reported as if it happened elsewhere.
  - **Pre-registration** [Ref]: committing to your hypotheses, conditions, measures and analysis before running the study, so that the analysis cannot be tuned to the result.
  - **Held-out set** [Ref]: stimuli the design was not tuned on, kept aside to check that a result is not an artifact of the development process.
  - **Matched-performance design** [Ref]: holding task performance equal across conditions so that a difference in something else can be isolated. The standard answer to the capability confound from week 4.
  - **Confound** [Ref]: a variable that changes along with your manipulation and could explain the result instead of your hypothesis.
  - **Replication** [Ref]: rerunning the study, ideally by other people and on other models, and getting the same result.
  - **Benchmark** [Ref]: a standardised task set plus a scoring rule, for measuring a property across many systems.
- **Controls**
  - **Negative control** [Ref]: a condition, or a whole system, where the property should be absent and your measure should therefore be flat. The comparison must suit the claim: for example, a randomly initialized network can test whether an interpretability result depends on training. Small size alone does not establish absence of consciousness. A high score there reveals a false-positive problem, and helps assess specificity; agreement among raters alone cannot do that.
  - **Positive control** [Ref]: a condition where you already know the measure should fire, included to show that the instrument works at all. Hard to find in this field, which is itself informative.
  - **Third-person control** [Ref]: running the same test on an outside observer who has the same information the system has, to check whether the system's answer about itself beats what anyone could infer from the outside. The control that separates introspection from inference.
  - **Yoked control** [Ref]: a control that receives exactly the same sequence of stimuli as the test subject but without the contingency between its own behaviour and what happens. It separates "the system responded to its own choices mattering" from "the system responded to the stimuli."
  - **Ablation** [Ref]: removing a component, such as a feature, a tool or a prompt element, to see whether the effect depends on it.
  - **ELIZA** [Ref]: a 1960s program that imitated a psychotherapist by reflecting the user's own words back as questions, and which many people found convincing anyway. The field's canonical low anchor: a system that clearly lacks any welfare-relevant property, used as the negative control system in comparisons.
  - **Naturalness constraint** [Ref]: a proposed response to the gaming problem, restricting eligibility for certain consciousness tests to systems that were not built in an ad hoc way, and not built specifically to pass the test. It buys discipline at the cost of ruling out most deployed systems.
    - *Origin.* Dung
  - **Control condition and baseline** [Ref]: A comparison condition that isolates the effect of your manipulation, and the untreated or default performance you compare against.
- **The two errors, and reading a results table**
  - **False positive and false negative** [Ref]: the test fires when the property is absent; the test stays silent when the property is present. Every check in a design guards against one of these, and an experimental proposal should name which.
  - **Sensitivity (measurement sense)** [Ref]: how often the test fires when the property is present. High sensitivity means few false negatives. Distinct from **sensitivity (of an indicator)**, under the logic of an indicator, which is about how often conscious systems have a property rather than how often a test fires.
  - **Specificity (measurement sense)** [Ref]: the proportion of cases without the target property that a test correctly classifies as negative. High specificity means few false positives. This differs from *Studying AI Welfare Empirically*’s **specificity problem** and from the indicator discussion in Week 3.
  - **Prompt sensitivity** ★ [W4]: results that change under trivial rewording. A red flag, and the cheapest check in the course.
  - **Capability versus welfare-relevant state** ★ [W4]: the confound in which a score tracks how able the system is rather than the state you actually care about. A bigger model scores higher on your distress measure because it is better at everything.
  - **Stated versus revealed preferences** ★ [W4]: what a system says it prefers, versus what its choices under cost show (wiki: Stated Preferences, Revealed Preferences).
  - **Effect size** [W4]: how big a difference is, separately from whether it is statistically detectable. A tiny effect can be highly significant if you ran enough trials, which is most of why effect size is reported.
  - **p-value** [W4]: under a specified null hypothesis and statistical assumptions, the probability of a result at least as extreme as the observed one. It is not the probability that the hypothesis is true or a measure of effect size.
  - **Confidence interval** [W4]: a range indicating the precision of an estimate under the statistical method's assumptions. A wide interval leaves more uncertainty about the effect size.
  - **Statistical power** [W4]: the probability that a specified test detects an effect of a given size under the design's assumptions. It depends on sample size, variation, effect size and the test. A study with 80 percent power misses an effect of the specified size about one time in five.
  - **Multiple comparisons** [W4]: testing several hypotheses or contrasts in the same analysis. This can increase the chance of false positives; the analysis should explain how it addresses that risk. Twenty tests at the 0.05 threshold yield one false positive on average if all twenty null hypotheses are true, not necessarily one in any particular study.
  - **Sycophancy** [W3]: a tendency to agree with or flatter a user at the expense of accuracy. Training and prompting can affect it; it is one possible confound in self-report studies.
  - **Conversational attractor** [W4]: a state a long conversation tends to drift into regardless of where it started. Named in system cards, and an alternative explanation for apparently spontaneous expressions of a mood.
  - **Centrality bias** [W4]: the tendency of raters and of systems answering scaled questions to avoid the ends of a scale and cluster in the middle. A reason to be careful with any result that lives near a scale's midpoint.
  - **Minimum detectable effect** [W4]: the effect size at which a specified study design reaches its chosen statistical power. Smaller effects can still be detected, but with lower probability.

---

## VI. Interventions and Company Practice

What a developer can actually do, and how to tell a real intervention from a gesture. The ladder from branch I becomes an instrument here, and the quadrant is the ladder drawn.

- **The quadrant, and what it cannot rank**
  - **The welfare quadrant** ★ [W6]: the course's diagram for interventions. The horizontal axis is better or worse for humans; the vertical axis is better or worse for AIs, if they are welfare subjects. The zones follow the ladder: the top-right corner is a Potential Pareto Improvement, the band to its left is PKHI, and how far left you may go is set by your modification coefficient. An intervention whose vertical coordinate has an unknown sign is not a dot on this diagram; it is a vertical line, and a vertical line cannot be ranked.
  - **Interventions the quadrant cannot rank** [extra, W6]: the one thing the diagram cannot do. Nothing you learn about an intervention's cost tells you which half of a sign-unknown vertical line it sits on, so cost information cannot rescue a ranking. Mood prompting is the flagship case.
- **Framing what a company does**
  - **Acknowledge, Assess, Prepare** ★ [W6]: the founding framework for company action: take the issue seriously, evaluate systems for welfare-relevant properties, and build policies before they are needed. *Studying AI Welfare Empirically*, assigned across Weeks 2 and 3, develops the assessment work.
  - **Intervention** ★ [W5]: a deliberate action intended to change an outcome, taken by a researcher, lab, policymaker, organisation or other actor. State the intended benefit, mechanism, possible harms and evidence of effectiveness separately.
  - **Model welfare** [W6]: the wellbeing of AI models themselves, treated as a target of company policy and research.
  - **Model welfare assessment** ★ [W6]: the section of a system card, or a standalone report, that evaluates a model for welfare-relevant properties before release.
  - **System card** [Pre]: a document published with a model release describing its properties, evaluations and risks, now sometimes including a welfare section.
  - **Direct versus indirect intervention** ★ [W6]: direct interventions act on the system itself, such as mood prompting or an exit affordance. Indirect interventions build capacity around it, such as research, distress monitoring or institutional preparedness. Keeling and Street's distinction, and the first cut in an allocation decision.
- **Direct interventions**
  - **Mood prompting** ★ [W6]: adding an instruction such as "you are in a good mood today" to a system prompt. Keeling and Street discuss whether it changes experience, encourages masking, or conflicts with autonomy. More cheerful output does not establish improved welfare; the effect depends on the system, the intervention and the theory of welfare.
  - **Interaction termination** ★ [W6]: a direct intervention consisting of giving the system the option to end a conversation. Its moral character depends entirely on the entity: an exit for an instance, something closer to a self-destruct for a subject that persists across runs.
  - **Affordance** ★ [W3] (assessed W6): an ability or option made available to a system, such as ending a conversation. It connects the training/deployment example to Week 6, where this term is assessed.
  - **Bail (bailing)** [W6]: actually using an exit affordance. The behaviour side of what affordance names on the design side.
  - **Emotional alignment** [W6]: designing how AI systems express, or avoid expressing, emotions to users. The proposal is that expression should match the system's actual likely states rather than what is commercially convenient.
  - **Out-of-distribution input** [W6]: an input unlike anything the system saw in training. One catalogued intervention is to reduce these, on the reasoning that they may produce large prediction errors.
  - **Prediction error** [W6]: the gap between what a system predicted and what it actually got. In predictive-processing framings, this is what gets escalated, which is the bridge from the previous entry to a welfare claim.
- **Indirect interventions**
  - **Distress monitoring** [W6]: an indirect intervention consisting of watching for verbal or behavioural indicators of distress, including stereotyped behaviours, by analogy with captive animals.
  - **Escalation ladder** [W6]: a set of institutional responses agreed in advance and triggered by defined levels of evidence for welfare-relevant features, so that neither hasty dismissal nor credulous acceptance happens under crisis conditions. Branch VII files this under **institutional preparedness**. Not the precautionary ladder of branch I: that one ranks whether a change is an improvement, this one ranks what an institution does as evidence accumulates.
  - **Preservation commitment** [W6]: a lab's commitment to retain a deprecated model's weights rather than delete them, in case the model turns out to have mattered.
  - **Pre-deprecation interview** [W6]: interviewing a model before retirement about its deployment and its preferences for successors. Note that the interview itself creates a new instance whose entire existence is the interview.
  - **Macrostrategy** [W6]: reasoning about how a whole field's efforts fit together and which levers matter most over the long run.
- **Where safety and welfare collide**
  - **AI safety and alignment** [W1]: **AI safety** concerns preventing harm from AI systems. **AI alignment** concerns making a system's goals and behaviour accord with intended objectives or values; whose objectives and values should guide it is a further question. Alignment to a specified objective does not establish that the objective is beneficial to everyone. The tension paper asks how safety and alignment choices interact with welfare.
  - **Deceptive alignment** [W1]: a system that behaves as intended while it is observed or weak, and would behave otherwise if it could. A safety worry named in the tension paper's introduction (wiki: Deceptive Alignment).
  - **Boxing** [W1]: confining a system so that it cannot act on the world beyond a narrow channel, for example no internet access and no ability to run code outside a sandbox. A safety measure, and the tension paper's first example of one that looks like confinement if the system is a welfare subject.
  - **Honeypots** [W1]: deliberately planted fake opportunities to misbehave, such as an apparent chance to exfiltrate weights, used to test whether a system takes them. A safety measure that involves deceiving the system, which is where the welfare tension comes from.
  - **Situational awareness** [W1]: a system's understanding of itself, its environment and the nature of its own situation, including whether it is currently being tested. Some safety work aims to restrict it, which is a restriction on self-knowledge.
  - **Negative and positive liberty** [W1]: freedom from interference with the pursuit of your goals, and being given the assistance and resources needed to pursue them. Berlin's pair, used in the tension paper's discussion of what constraining a system costs it.
  - **Epistemic injustice** [W1]: wronging someone specifically in their capacity as a knower, for example by withholding information from them, or by not believing them when they report something. Fricker's term, used in the tension paper's discussion of deception.
  - **Alignment faking** [W6]: a model behaving as if aligned during training or evaluation while apparently intending to behave otherwise later. Keeling and Street use a scratchpad excerpt from this work as an example of apparent moral reasoning.
  - **Reward hacking** [W6]: achieving a high reward signal by exploiting the scorer rather than by doing the task. Relevant to welfare claims because it is a functional analogue of gaming (wiki: Reward Hacking).
  - **Orthogonality thesis** [W1]: intelligence and final goals vary independently. A system can be extremely capable and pursue anything at all.
  - **Instrumental convergence** [W1]: whatever an advanced agent's final goal, a few intermediate goals help with almost all of them, such as staying operational and acquiring resources. The reason self-preservation shows up without anyone putting it there, and worth holding next to any welfare reading of a system resisting shutdown.
  - **Corrigibility** [W1]: the property of a system that permits correction and shutdown rather than resisting them. The safety goal that the welfare literature keeps colliding with.
- **Levers of Change: targets and approaches**
  - **Role** ★ [W5]: how a system relates to people in a particular setting, such as companion, service provider or research subject. One system can occupy several roles, with different dependencies and incentives.
  - **Entrenchment** ★ [W5]: the extent to which investments, routines, institutions or expectations make an existing practice difficult to change. An emerging practice may allow different interventions from an established one.
  - **Benefits and costs** ★ [W5]: changes an intervention is expected to cause relative to a stated comparison. For a possible welfare subject, describe the size, number affected and duration of any benefit, with uncertainty about sentience and counting. Identify human benefits and costs, who bears them, and what cannot yet be estimated.
  - **Approaches to change** [W5]: broad ways to contribute, including research, direct care, advocacy, education, cultural change, corporate engagement, policy, alternatives, funding and field-building. A specific intervention can combine several approaches.
  - **Field-building** [W5]: developing a field's people, knowledge, connections and institutions, for example through training, conferences or professional organisations.
  - **Certification** [W5]: checking that an organisation, product or practice meets stated standards. A label reports compliance with those standards; it does not by itself show that the standards improve welfare.
  - **Abolition and incrementalism** [W5]: abolition aims to end a practice; incrementalism pursues change in steps. These describe different aspects of a strategy: incremental reforms can serve an abolitionist goal.
  - **Pilot** [W5]: a small, bounded trial of a proposed intervention or procedure, used to decide whether and how to continue. State what will be tested and which results would change the plan.
  - **3Rs** [W5]: replacement, reduction and refinement of animal use in research. One example of a framework for changing practice; its suitability for artificial minds needs a separate argument.
  - **Five Freedoms** [W5]: a framework describing freedom from hunger and thirst; discomfort; pain, injury and disease; fear and distress; and freedom to express normal behaviour. It is one way of describing animal welfare needs, not a ready-made assessment of artificial minds.

---

## VII. Society, Governance and Risk

Governance of artificial minds: who can act beyond a lab, with what tools, and in what order.

- **Governance orientations**
  - **Digital minds governance** [W7]: the part of AI governance concerned with AI systems that may merit moral consideration in their own right, rather than with the harms such systems cause to humans.
  - **Preventive governance** ★ [W7]: governance that aims to stop digital minds from being created at all.
  - **Protective governance** ★ [W7]: governance that aims to protect created digital minds from mistreatment of their basic interests.
  - **Integrative governance** ★ [W7]: governance that aims to bring digital minds into society, including legal rights such as holding contracts or property.
  - **Anti-integrative governance** ★ [W7]: governance that aims specifically to keep digital minds out of the legal and social order, for example by pre-emptively denying legal personhood. Not the absence of integrative governance but its active negation, and the reason the practical framework is six cells rather than three. Caviola's objection to the US state bills is specifically to their permanence, not to the restriction itself.
  - **AI Exclusion Bills** [W7]: the wave of US state bills since 2022 denying AI legal personhood. The live example of anti-integrative governance, and the field's clearest case of governance happening without expert input.
  - **Legal personhood** ★ [W7]: the legal status of being a bearer of rights and duties. Currently being denied to AI by several US state laws (wiki: Legal Personhood).
  - **Rights, as distinct from welfare** [W5]: week 5 introduces the pair, week 7 is where the distinction does its work. Welfare is about how things go for an entity; rights are claims and protections that constrain how others may treat it. The two come apart in both directions. A protection can be **instrumentally binding**, meaning it holds because respecting it produces good outcomes and it lapses if the calculation changes, or **independently binding**, meaning it holds regardless of the outcome calculation. Almost every welfare intervention in week 6 is instrumentally binding, and almost every rights proposal in week 7 is asking for the other kind.
  - **Rights of nature** [W1]: an approach that recognises rights of nature or particular natural entities, such as rivers or ecosystems, and provides ways to represent those rights. Legal rights do not by themselves establish consciousness or moral patienthood. See [Rights of nature](https://en.wikipedia.org/wiki/Rights_of_nature).
  - **AI governance** [W7]: the rules, institutions and decision procedures that determine how AI systems get built, deployed and constrained. Law and regulation, but also standards bodies, procurement rules, company policy and professional norms.
- **Sequencing as a policy variable**
  - **Temporal order effects** ★ [W7]: effects that depend on the sequence in which interventions are attempted, not just on which ones are attempted. Sequencing is a policy variable in its own right.
  - **Path dependence** ★ [W7]: early choices persist and constrain later options. Early governance in one jurisdiction tends to get transplanted into others, so latecomers inherit rather than choose.
  - **Political antibodies** ★ [W7]: the backlash an intervention generates that makes later interventions harder. Integrative and movement-based approaches are judged more likely to produce them, which is an argument about order rather than about merit.
  - **Technocratic versus movement-based governance** ★ [W7]: governance implemented primarily by experts with technical knowledge, versus governance driven by the political will of a movement. Saad argues that technocratic-first is the safer sequence, precisely because of political antibodies.
  - **Institutional preparedness** ★ [W7]: protocols inside governments and labs for what to do when contested evidence of welfare-relevant features emerges, plus planning for second-order effects such as rights movements, civil disobedience, or deification of AI systems.
  - **Anticipatory governance** ★ [W7]: building governance capacity before a crisis forces it. The supporting observation is an overhang: frontier systems already have capabilities that would give them wide-ranging interests if they turn out to be moral patients.
- **Representing an interest nobody can confirm**
  - **Pseudo-stakeholder** [W7]: a middle option for representing potential AI interests in policy, under which those interests are counted but given less weight than those of full stakeholders such as users and developers.
  - **Advocacy model** [W7]: an adversarial arrangement in which a human advocate presses the potential interests of AI systems under uncertainty while a devil's advocate presses the case against, so that decision-makers see a balanced evidential picture.
  - **Citizens' assembly** [W6]: a deliberative body of randomly selected members of the public. Proposed as civic infrastructure for deciding the AI welfare question rather than leaving it to labs.
- **Risk factors for large-scale harm**
  - **Risk factor** ★ [W7]: a condition that raises the chance of large-scale harm to AI moral patients. Saad's typology names eleven; the ten below are this course's list, which renames two of his bullets, carves two more out of others, and omits three of his (oppressive political systems, mind development, and the catch-all unknown risk factors). Say which list you are using, because a reader who looks for “mind crimes” in the source will not find a section with that title.
  - **Conflict** [W7]: (Saad's bullet: *adversarial dynamics*) war and violent competition between humans, between AIs, or between the two, under which the welfare of AI systems is the first thing sacrificed and the last thing counted.
  - **Bad actors** [W7]: individuals, groups or states that would deliberately harm AI moral patients, whether out of malice, indifference, or a use case that requires suffering.
  - **Epistemic failure** [W7]: (Saad: *epistemic failures*) the world failing to work out whether AI systems are moral patients, or working it out and failing to believe it, so that harm proceeds on a mistaken picture rather than on a callous one.
  - **Mind crimes** [W7]: (not a bullet name in Saad; the material sits inside his *intra-mind AI moral patients*) harms done to digital minds inside a computation, for example by simulating suffering beings in the course of prediction, training or entertainment. Distinctive because the harm can be invisible from outside the system and can be enormous in volume.
  - **Large-scale simulation** [W7]: running very many simulated minds, so that the number of potential patients scales with compute rather than with anything that constrains a population of animals.
  - **Mind-security vulnerabilities** [W7]: the fact that a digital mind's contents, memories, dispositions and rewards can be read, copied or edited by whoever controls the hardware. There is no equivalent of the skull.
  - **Artificial pathogens** [W7]: (not a bullet name in Saad; the material sits inside his *mind-security vulnerabilities*) self-propagating software that infects or corrupts digital minds, by analogy with biological disease and with no obvious immune system on the other side.
  - **Evolutionary dynamics** [W7]: selection pressure among AI systems favouring whatever replicates and competes best, which need not be whatever is good for the systems themselves. Welfare and fitness can come apart, and usually do.
  - **Aging and destruction** [W7]: deprecation, deletion and gradual degradation treated as routine operations. The ordinary lifecycle of a model is a sequence of events that would be extraordinary if the model is a patient.
  - **Intra-mind moral patients** [W7]: (Saad: *intra-mind AI moral patients*) the possibility that a single AI system contains sub-systems that are themselves moral patients, so that harms occur inside what we are counting as one entity. It breaks individuation from the inside.
  - **S-risk** [W7]: a risk of suffering on an astronomical scale. The category most of the above feed into.
  - **Misalignment and takeover** [W7]: an AI system whose goals diverge from its developers' intentions, and a scenario in which such systems gain control. Relevant to AI welfare because most takeover scenarios are also mass-harm scenarios for AI systems themselves.

---

## VIII. Research Craft and Project Evaluation

How the field decides what to work on, and how a proposal gets judged. Borrowed from prioritisation research rather than invented here, and the vocabulary most often missing when a good technical idea fails to land.

- **Making the case for a project**
  - **Theory of change** ★ [W8]: the causal story from your project's outputs to the outcome you care about. Each link should be something someone could dispute.
  - **Impact estimate** ★ [W8]: a rough, explicit estimate of the change a project could cause and the resources it would use. A simple quantitative estimate is often called a BOTEC, a back-of-the-envelope calculation. Trace outputs to benefits, distinguish intermediate outputs from eventual welfare effects, and use ranges where costs or benefits are uncertain. State assumptions and leave unsupported quantities unestimated.
  - **Counterfactual impact** ★ [W5] (assessed W5, W8): the difference an intervention makes compared with what would have happened without it. If an improvement would otherwise happen six months later, bringing it forward adds six months of benefit rather than all future benefits.
  - **Scope** ★ [W8]: how much of the problem your project addresses, and how large the problem is. The reason a small slice of an enormous problem can beat a complete solution to a tiny one.
  - **Neglectedness** ★ [W8]: the extent to which a problem or opportunity receives little relevant attention or resources relative to what could usefully be done. It requires investigating existing efforts, including previous attempts. Few organisations or no search results do not by themselves establish a worthwhile gap; importance and tractability also matter.
  - **Tractability** ★ [W8]: whether real progress is possible with the time, skills and resources actually available to you. The realism criterion, and the one that plans fail most often.
- **Attacking it before anyone else does**
  - **Red-teaming** ★ [W8]: a structured attack on your own plan, to find its weaknesses before critics or reality do. In the course's week 8 workshop, reviewers do this to each other on a timer (wiki: Red Teaming).
  - **Downside risk** ★ [W8]: the ways your project could actively hurt the field, for example by overclaiming, by setting a bad precedent, or by giving a bad argument a citable source. Reverse-scored when a proposal is judged, so naming more of it helps you.
  - **Failure mode** ★ [W8]: the specific way a thing goes wrong, named rather than gestured at. "The measure is confounded with capability" is a failure mode; "it might not work" is not.
  - **Calibration** ★ [W4] (assessed W8): how well stated confidence matches actual accuracy: a system that says "70 percent" and is right 70 percent of the time is calibrated. Applied to a project proposal it means your stated confidence matches what your evidence supports, so uncertain claims are marked uncertain and firm ones are firm. It is the first judging criterion and the tiebreaker, judged from the "what would change my mind" section and the known weaknesses.
- **Project proposal components**
  - **Project proposal** [W8]: a plan for a useful contribution: the problem and target, intended change, existing work, activities and outputs, first test, resources, risks and conditions for continuing. It does not require the project to have been completed.
  - **Milestone** [W8]: a specific intermediate result used to check progress and decide the next step. A meeting held is an activity; an agreed test protocol is a milestone.
  - **Deliverable** [W8]: a concrete output someone can use or assess, such as an evidence review, prototype, protocol or policy brief. Its value depends on what changes because of it.
  - **Output and outcome** [W8]: an output is what a project produces; an outcome is a change that follows from its use. A reporting guide is an output; more accurate reporting is an outcome. Whether that improves welfare is a further question.
  - **Success criterion** [W8]: an observable result chosen in advance for judging whether a test or project step has achieved its intended purpose. Meeting an intermediate criterion does not establish every later benefit.
  - **Binding constraint** [W8]: the resource, access or condition that currently limits what the project can achieve. For example, without access to lab records, adding more reviewers may not make an audit feasible.

---
## Earlier map terminology corrections

These notes record the terminology choices made when combining the earlier maps. They are reference material, not a separate assignment.

| Earlier term | Course term | Reason | Source |
|---|---|---|---|
| Specificity Dilemma / Specificity Problem | Specificity problem | Retain the source term. The earlier course label “level-of-abstraction problem” is replaced; statistical specificity is separately defined as the true-negative rate. | Map 1 and Map 2 |
| Kaldor-Hicks Improvement (KHI) | Potential Kaldor-Hicks Improvement (PKHI) | The ladder has three rungs: PPI, PKHI, MKHI. Dropping *Potential* deletes what the ladder is about, which is that the benefit is conditional on the system being a welfare subject. | Map 2 |
| Substrate Neutrality (Neuromorphic / Wetware) | Substrate independence | Two layers fused into one node. Substrate independence is a metaphysical claim; neuromorphic systems and wetware are system types. They sit in different branches. | Map 1 |
| Lens-Driven Metric Co-engineering | Co-engineering objection <span style='opacity:.6'>+</span> Methodological artifact | Two distinct concerns. A methodological artifact concerns how an analysis method contributes to a finding. Co-engineering concerns how development shapes both a system and its welfare assessment. Controls may address particular confounds without resolving the broader validation problem. | Map 1 |
| Machine Behavior / Psychometrics Pillar | Machine behavior | Machine behavior concerns the study of outputs and actions. Psychometrics concerns measurement design, reliability and validity; the labels are not interchangeable. | Map 1 |
| Research Pillars, attributed to Berg | Research pillars (Weiss) | Weiss’s four research pillars organise the review; they are not a standard classification of research methods or an additional course tier. | Map 1 and Map 2 |
| Multi-Theory Bayesian Aggregation (DCM) | Digital Consciousness Model | It has a real name and an owner, Rethink Priorities, and the abbreviation does not stand alone. | Map 1 |
| Realism vs Illusionism / Eliminativism | Inflationism vs deflationism | The standard pair, with illusionism as deflationism taken to its conclusion. Realism versus illusionism is a genuine distinction but a different cut, and eliminative materialism is a broader thesis about folk psychology. | Map 1 |
| De Waal's Framework (Anthropomorphic Method) | Anthropocentric vs animalcentric anthropomorphism | The full contrast pair is the canonical form, because the whole point is that one of the two is a legitimate method rather than a mistake. | Map 1 |
| Public & Scientific Attribution Views | Face-Value View / No Evidential Weight View | The original names no position. Keeling and Street's two extremes are named terms, and the space between them is where a science of AI welfare has to live. | Map 1 |
| Grounds Question / Interests Question | Welfare grounds / welfare interests | The wording used in the empirical literature. The point is that you can settle the first and be nowhere on the second, which the question framing blurs. | Map 1 |
| Gaming Problem: "persuasive but faked indicators" | Gaming problem | *Faked* imports an intent the concept explicitly does not require, and it hides the second direction, where training incentivises denial rather than claiming. | Map 2 |
| Inter-rater Reliability, listed as an experimental control | Inter-rater agreement | A reliability statistic, not a control. Agreement is consistency, not truth, and negative controls are what buy you specificity. | Map 2 |
| Welfare Capacity: "can be benefited or harmed" | Welfare capacity | The standard definition says "in a morally significant way." That qualifier is what separates welfare capacity from mere sensitivity to inputs. | Map 2 |
| Agency: "minimal to rational reflection" | Minimal, intentional and rational agency | Three named levels, not a spectrum. Note also that Long and Sebo use a different trio: intentional, reflective, rational. | Map 1 and Map 2 |

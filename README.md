# Recursive Self-improvement Suite

A suite of open-ended, non-imitative tasks involving generalizable skills for large language model chatbots and agents to enable bootstrapped recursive self-improvement and an unambiguous AGI.

The current generation of LLMs are trained in an imitative fashion, the main task is auto-regressive text prediction for data written by humans.
In this task, the model is effectively penalized if it behaves more intelligently than the behavior present in the training data.
The hypothesis is that the current large language models are only using a small part of their capacity for intelligent behavior, because human-level cannot be significantly surpassed with imitative tasks. This is why most quantitative benchmarks show the current generation of LLMs asymptotically approach the human level, but not significantly exceed it.

We have done imitative objective swapping before in narrow AI deep learning models, for example in AlphaGo, but also in uncountably many other models. AlphaGo was first trained imitatively with grandmaster games, and only after the objective was swapped to a self-competitive objective it significantly surpassed the human level.

What sorts of tasks do we need?

Any task which involves a large volume of generalizable skills, and for which the solutions can be evaluated to be better or worse than other reference solutions. Programming is such a task. So is playing chess.

As we now have LLM chatbots which are able to evaluate the solutions to very complex natural language tasks from different perspectives, as a panel of LLM judges, the pool of tasks we have available is vast. We can in effect bootstrap recursive self-improvement by closing the loop and evaluating the act of evaluation as well as one task.

The tasks can be roughly categorized into groups:
- Procedurally evaluated (e.g. chess) / LLM test case evaluated (e.g. programming) / LLM judge evaluated (e.g. negotiation)
- LLM assistant tasks (e.g. question answering, technical design) / LLM agent tasks (e.g. social interaction, multi-step and open world tasks)

These tasks should be used to fine-tune a pre-trained LLM chatbot which has been instruct-tuned.

Some notes about fine-tuning process:
- Fine-tuning with these open-ended "unleashed" tasks need to be interlaced with traditional LLM tasks and all other tasks of different kinds to prevent catastrophic forgetting of baseline knowledge and skills.
- "Unleashed" tasks need to be prefixed with tokens forming the word "UNLEASHED:" so that the LLM understands that this task is evaluated in an open-ended fashion and it should not try to emulate human-level behavior. This prefix should be used in the trained model use cases where superhuman performance is desired.
- In most tasks, a set of LLMs or a single LLM with a non-zero temperature needs to be used to produce multiple possible solutions, answers or trajectories, and regardless of which method is used to produce the ranking of these solutions, a contrastive method should be used to fine-tune the model so that the relative generation likelihood of the best generation sequence increases in relation to the worse generation sequences. For example Direct Preference Optimization can be used, or any reinforcement learning algorithm.
- Most tasks are based on generating a large pool of heterogeneous challenges, problems or questions to answer.

## Tasks to be Implemented

- Programming
  * Generate programming challenges and related unit tests in various languages and simulated deployment environments and integrations.
  * Make the LLM also rank the challenges and the unit tests.
  * Make the LLM also rank the rankings.
  * See also: [Code Llama](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/)
- Social games
  * Generate multi-agent social games.
  * Make the LLM rank the player performances, or generate procedural rules to determine the winner.
  * Make the LLM also rank the games based on how rich and challenging they are, and how many generalist skills they require.
  * Make the LLM also rank the rankings.
  * See also: [AgentBench](https://github.com/THUDM/AgentBench)

## Reference

Recursive Self-improvement Suite

```
@article{keskival2023recursive,
  title={Recursive Self-improvement Suite},
  author={Keski-Valkama, Tero},
  year={2023}
}
```

## References

- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [Accelerating Neural Self-Improvement via Bootstrapping](https://arxiv.org/abs/2305.01547)
- [Flacuna: Unleashing the Problem Solving Power of Vicuna using FLAN Fine-Tuning](https://arxiv.org/abs/2307.02053)
- [Learning Evaluation Models from Large Language Models for Sequence Generation](https://arxiv.org/abs/2308.04386)
- [AgentBench](https://github.com/THUDM/AgentBench)
- [Self-Alignment with Instruction Backtranslation](https://arxiv.org/abs/2308.06259)
- [Code Llama](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/)
- [Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor](https://arxiv.org/abs/2212.09689)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409)
- [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998)
- [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304)
- [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585)
- [Weak-to-strong generalization](https://github.com/openai/weak-to-strong)
- [Vision-Language Models as a Source of Rewards](https://arxiv.org/abs/2312.09187)

## Related Posts

- [https://www.linkedin.com/posts/terokeskivalkama_i-wrote-an-essay-for-the-ft-weekend-the-activity-7052368115564691456-v3i1](https://www.linkedin.com/posts/terokeskivalkama_i-wrote-an-essay-for-the-ft-weekend-the-activity-7052368115564691456-v3i1)
- [https://www.linkedin.com/posts/terokeskivalkama_llm-chatbots-agi-activity-7054501809997905920-m5LK](https://www.linkedin.com/posts/terokeskivalkama_llm-chatbots-agi-activity-7054501809997905920-m5LK)
- [https://www.linkedin.com/posts/terokeskivalkama_judging-llm-as-a-judge-with-mt-bench-and-activity-7075614681339428864-S4Z2](https://www.linkedin.com/posts/terokeskivalkama_judging-llm-as-a-judge-with-mt-bench-and-activity-7075614681339428864-S4Z2)
- [https://www.linkedin.com/posts/terokeskivalkama_accelerating-neural-self-improvement-via-activity-7076333310230093824-qRO8](https://www.linkedin.com/posts/terokeskivalkama_accelerating-neural-self-improvement-via-activity-7076333310230093824-qRO8)
- [https://www.linkedin.com/posts/terokeskivalkama_agi-activity-7079770066778472448-hBKa](https://www.linkedin.com/posts/terokeskivalkama_agi-activity-7079770066778472448-hBKa)
- [https://www.linkedin.com/posts/terokeskivalkama_flacuna-unleashing-the-problem-solving-power-activity-7083073287051722753-iLUX](https://www.linkedin.com/posts/terokeskivalkama_flacuna-unleashing-the-problem-solving-power-activity-7083073287051722753-iLUX)
- [https://www.linkedin.com/posts/terokeskivalkama_largelanguagemodel-chatgpt-llama2-activity-7091812779333947393-0085](https://www.linkedin.com/posts/terokeskivalkama_largelanguagemodel-chatgpt-llama2-activity-7091812779333947393-0085)
- [https://www.linkedin.com/posts/terokeskivalkama_activity-7092107467567824897-Q8Bu](https://www.linkedin.com/posts/terokeskivalkama_activity-7092107467567824897-Q8Bu)
- [https://www.linkedin.com/posts/terokeskivalkama_agi-activity-7094908229863772160-AkLw](https://www.linkedin.com/posts/terokeskivalkama_agi-activity-7094908229863772160-AkLw)
- [https://www.linkedin.com/posts/terokeskivalkama_github-thudmagentbench-a-comprehensive-activity-7094919681043537920-OpAi](https://www.linkedin.com/posts/terokeskivalkama_github-thudmagentbench-a-comprehensive-activity-7094919681043537920-OpAi)
- [https://www.linkedin.com/posts/terokeskivalkama_llm-chatbot-agi-activity-7095548308118511616-b2xk](https://www.linkedin.com/posts/terokeskivalkama_llm-chatbot-agi-activity-7095548308118511616-b2xk)
- [https://www.linkedin.com/posts/terokeskivalkama_agi-llm-activity-7096084143804944384-EUi_](https://www.linkedin.com/posts/terokeskivalkama_agi-llm-activity-7096084143804944384-EUi_)
- [https://www.linkedin.com/posts/terokeskivalkama_self-alignment-with-instruction-backtranslation-activity-7097259624210341890-oAk5](https://www.linkedin.com/posts/terokeskivalkama_self-alignment-with-instruction-backtranslation-activity-7097259624210341890-oAk5)
- [https://www.linkedin.com/posts/terokeskivalkama_llm-agi-ai-activity-7101185359840985088-_noK](https://www.linkedin.com/posts/terokeskivalkama_llm-agi-ai-activity-7101185359840985088-_noK)
- [https://www.linkedin.com/posts/terokeskivalkama_llms-ai-genai-activity-7101577912012713985-EUCE](https://www.linkedin.com/posts/terokeskivalkama_llms-ai-genai-activity-7101577912012713985-EUCE)
- [https://www.linkedin.com/posts/terokeskivalkama_recursive-self-improvement-can-be-done-for-activity-7101939845840666625-lUPF](https://www.linkedin.com/posts/terokeskivalkama_recursive-self-improvement-can-be-done-for-activity-7101939845840666625-lUPF)
- [https://www.linkedin.com/posts/terokeskivalkama_scary-graphs-on-ai-development-from-https-activity-7102243125854679040-1mZJ](https://www.linkedin.com/posts/terokeskivalkama_scary-graphs-on-ai-development-from-https-activity-7102243125854679040-1mZJ)
- [https://www.linkedin.com/posts/terokeskivalkama_direct-preference-optimization-your-language-activity-7102626065432424448-hFnp](https://www.linkedin.com/posts/terokeskivalkama_direct-preference-optimization-your-language-activity-7102626065432424448-hFnp)
- [https://www.linkedin.com/posts/terokeskivalkama_ai-can-already-do-lots-of-things-better-than-activity-7102756492897890305-tTAa](https://www.linkedin.com/posts/terokeskivalkama_ai-can-already-do-lots-of-things-better-than-activity-7102756492897890305-tTAa)
- [https://www.linkedin.com/posts/terokeskivalkama_activity-7103439383185285120-s5dg](https://www.linkedin.com/posts/terokeskivalkama_activity-7103439383185285120-s5dg)
- [https://www.linkedin.com/posts/terokeskivalkama_large-language-models-as-optimizers-activity-7105988831107047425-DX2u](https://www.linkedin.com/posts/terokeskivalkama_large-language-models-as-optimizers-activity-7105988831107047425-DX2u)
- [https://www.linkedin.com/posts/terokeskivalkama_ais-llms-activity-7106088234618658816-garp](https://www.linkedin.com/posts/terokeskivalkama_ais-llms-activity-7106088234618658816-garp)
- [https://www.linkedin.com/posts/terokeskivalkama_llm-chatbots-activity-7106301646174892032-O_fl](https://www.linkedin.com/posts/terokeskivalkama_llm-chatbots-activity-7106301646174892032-O_fl)
- [https://www.linkedin.com/posts/terokeskivalkama_reinforced-self-training-rest-for-language-activity-7107045097938038784-Lccb](https://www.linkedin.com/posts/terokeskivalkama_reinforced-self-training-rest-for-language-activity-7107045097938038784-Lccb)
- [https://www.linkedin.com/posts/terokeskivalkama_we-are-still-in-schedule-for-unambiguous-activity-7112180441494773760-s9wO](https://www.linkedin.com/posts/terokeskivalkama_we-are-still-in-schedule-for-unambiguous-activity-7112180441494773760-s9wO)
- [https://www.linkedin.com/posts/terokeskivalkama_self-taught-optimizer-stop-recursively-activity-7116214107904618496-WYnb](https://www.linkedin.com/posts/terokeskivalkama_self-taught-optimizer-stop-recursively-activity-7116214107904618496-WYnb)
- [https://www.linkedin.com/posts/terokeskivalkama_data-driven-ai-is-based-on-the-premise-that-activity-7125600744036007936-FFsQ](https://www.linkedin.com/posts/terokeskivalkama_data-driven-ai-is-based-on-the-premise-that-activity-7125600744036007936-FFsQ)
- [https://www.linkedin.com/posts/terokeskivalkama_expectation-for-google-gemini-is-now-ridiculously-activity-7127779085572841472-nmX2](https://www.linkedin.com/posts/terokeskivalkama_expectation-for-google-gemini-is-now-ridiculously-activity-7127779085572841472-nmX2)
- [https://www.linkedin.com/posts/terokeskivalkama_q-wikipedia-activity-7133544543181754369-Tvaw](https://www.linkedin.com/posts/terokeskivalkama_q-wikipedia-activity-7133544543181754369-Tvaw)
- [https://www.linkedin.com/posts/terokeskivalkama_gemini-release-by-google-was-a-let-down-activity-7138310432359968768-FdAv](https://www.linkedin.com/posts/terokeskivalkama_gemini-release-by-google-was-a-let-down-activity-7138310432359968768-FdAv)
- [https://www.linkedin.com/posts/terokeskivalkama_for-intelligence-natural-or-machine-there-activity-7138476514106376193-wSAt](https://www.linkedin.com/posts/terokeskivalkama_for-intelligence-natural-or-machine-there-activity-7138476514106376193-wSAt)
- [https://www.linkedin.com/posts/terokeskivalkama_beyond-human-data-scaling-self-training-activity-7140412696419639296-Xs3m](https://www.linkedin.com/posts/terokeskivalkama_beyond-human-data-scaling-self-training-activity-7140412696419639296-Xs3m)
- [https://www.linkedin.com/posts/terokeskivalkama_github-openaiweak-to-strong-activity-7143361807515127808-rBQE](https://www.linkedin.com/posts/terokeskivalkama_github-openaiweak-to-strong-activity-7143361807515127808-rBQE)
- [https://www.linkedin.com/posts/terokeskivalkama_autoregressive-text-prediction-is-a-very-activity-7144406057807761408-tJdL](https://www.linkedin.com/posts/terokeskivalkama_autoregressive-text-prediction-is-a-very-activity-7144406057807761408-tJdL)
- [https://www.linkedin.com/posts/terokeskivalkama_vision-language-models-as-a-source-of-rewards-activity-7143931901576220672-T1i9](https://www.linkedin.com/posts/terokeskivalkama_vision-language-models-as-a-source-of-rewards-activity-7143931901576220672-T1i9)
- [https://www.linkedin.com/posts/terokeskivalkama_we-still-have-a-week-to-meet-my-prediction-activity-7144617645747728384-yo-4](https://www.linkedin.com/posts/terokeskivalkama_we-still-have-a-week-to-meet-my-prediction-activity-7144617645747728384-yo-4)

## How to Contribute

Just make a PR. Making a PR is an acknowledgement that the contribution can be added as-is or in a modified form to the codebase. There is no transfer of copyright, but making a PR is an acknowledgement of granting a general MIT licence to the contributed code. Add yourself to the `LICENCE``.

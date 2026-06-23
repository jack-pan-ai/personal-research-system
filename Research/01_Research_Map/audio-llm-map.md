# Audio LLM Research Map

This map is public-safe and intentionally focuses on open literature, public repos, and high-level research judgment.

The ranking rule for this system is:

```text
interesting and useful first; rigor supports decisions when needed
```

## Big Questions

- What can an audio LLM do that cannot be reduced to ASR plus a text LLM?
- Which capabilities require native audio representations rather than text transcripts?
- What is the practical path from impressive demos to reliable, low-latency audio products?
- Which bottleneck is most worth attacking now: data, tokenizer/codec, architecture, training recipe, evaluation, inference cost, or interaction design?
- How should audio LLMs represent paralinguistic information such as emotion, speaker traits, prosody, turn-taking, hesitation, and environmental context?

## Research Taste

Prefer directions that are both:

- **Interesting:** reveal a non-obvious capability, failure mode, representation, or scaling behavior.
- **Useful:** can improve a product, model capability, evaluation signal, deployment path, or research decision.

Avoid over-investing in work that is only a benchmark leaderboard move unless it changes what we believe or what we can build.

## Important Directions

### 1. Native Speech/Audio Interfaces

Core question: when does the model need to listen directly instead of reading transcripts?

Representative work:

- AudioPaLM
- SpeechGPT
- SALMONN
- Qwen-Audio

Interesting gap:

- Many systems are still hybrids of audio encoders plus text LLMs. It is not always clear which behavior comes from audio understanding versus transcript-like content transfer.

Useful problem:

- Build tasks that isolate what native audio adds: prosody-aware intent, speaker state, conversational timing, overlapping speech, acoustic scene cues, and non-verbal signals.

### 2. Audio Tokenization and Codec Design

Core question: what audio representation is cheap enough for LLM-style modeling while preserving useful information?

Representative work:

- EnCodec
- Low Frame-rate Speech Codec
- Codec-SUPERB

Interesting gap:

- Tokenizers are often optimized for reconstruction or perceptual quality, but audio LLMs may need different information: semantic content, speaker identity, prosody, timing, and controllable generation.

Useful problem:

- Compare codec/tokenizer choices by downstream LLM behavior, not only audio reconstruction metrics.

### 3. Compression and Efficient Inference

Core question: how can audio LLMs become cheap, low-latency, and deployable without killing the behaviors that make them useful?

Subdirections:

- Low frame-rate audio tokens
- Quantization-aware inference
- Distillation from large audio LLMs
- Streaming-friendly architectures
- KV cache and context compression for long audio
- Speculative decoding for audio generation or speech interaction

Interesting gap:

- Compression may change more than quality: it may remove prosody, timing, speaker cues, or rare acoustic events. That makes audio compression different from text-only LLM compression.

Useful problem:

- Define compression evals that measure retained usefulness: latency, cost, speech understanding, paralinguistic preservation, and interaction quality.

### 4. Evaluation and Benchmarks

Core question: what should count as progress for audio LLMs?

Representative work:

- Dynamic-SUPERB
- AudioBench
- Codec-SUPERB

Interesting gap:

- Benchmarks can measure isolated task skill, but audio products depend on interaction loops: interruption, latency, clarification, memory, tool use, and user trust.

Useful problem:

- Design evals around realistic spoken workflows rather than only static audio-question pairs.

### 5. Product-Relevant Interaction

Core question: what makes an audio LLM feel useful in real life?

Important behaviors:

- Low-latency turn-taking
- Robustness to noisy input
- Graceful clarification
- Memory over spoken interaction
- Tool use from speech
- Voice UX that does not require perfect prompts

Interesting gap:

- The best research problem may be at the boundary of model behavior and interaction design, not inside the model alone.

Useful problem:

- Create a taxonomy of spoken-agent failure modes and map each failure to model, data, inference, or UX causes.

## Things I Believe

- Audio LLMs need evals that reward useful interaction, not only static recognition accuracy.
- Tokenizer/codec design is a central bottleneck for both capability and inference cost.
- Low-latency streaming behavior is a first-class research problem, not a deployment detail.
- The most interesting opportunities are likely where audio carries information that text discards.
- Public research should separate product-safe high-level insights from confidential implementation details.

## Things I Am Unsure About

- Whether general audio understanding and speech-first interaction should be unified in one model or handled by specialized components.
- How much native audio reasoning is needed for most valuable products versus strong ASR plus a strong text LLM.
- Which compression methods preserve the most useful non-text information.
- Whether current audio benchmarks predict real user-perceived usefulness.
- How to evaluate long-context spoken interaction without building overly artificial tasks.

## Interesting Gaps

- Native-audio value beyond transcripts is still under-specified.
- Compression for audio LLMs needs behavior-level evaluation, not just bitrate or WER.
- Codec/tokenizer design should be evaluated as an LLM interface, not just as signal reconstruction.
- Spoken-agent evaluation should include latency, interruption, repair, and tool-use loops.
- Paralinguistic information is often acknowledged but weakly operationalized.

## Useful Problems

- Build a public reading map of audio LLM architectures, tokenizers, and evals.
- Track papers by "interesting/useful" scores and decision: ignore, skim, deep read, reproduce, or build on.
- Define a small suite of public-safe audio LLM product scenarios for qualitative evaluation.
- Compare public codec/tokenizer papers by what they preserve for downstream LLM behavior.
- Maintain a list of audio LLM failure modes that could become research ideas.

## Next Actions

- Add 8-12 representative papers to the dashboard.
- Write one memo on "What does native audio add beyond ASR?"
- Create an idea note on compression evals for useful spoken behavior.
- Create a weekly review habit around the dashboard.

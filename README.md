# ITAI2376-Portfolio

## Overview
This repository is the comprehensive portfolio for ITAI 2376 — Deep Learning in Artificial Intelligence. It showcases my learning journey across key modules and my capstone project. It includes code, reports, tests, and a 10‑slide presentation summarizing outcomes and reflections.

### Highlights include:

Capstone: Educational Content Process Automation Agent using hybrid reasoning (ReAct, Chain‑of‑Thought, Planning), multi‑tool integration, memory systems, and a robust safety framework.
Generative AI: Diffusion model implementation on MNIST with U‑Net architecture, time/class conditioning, and CLIP‑based evaluation.
Frameworks Study: Comparative analysis of TensorFlow vs PyTorch with practical takeaways for research vs production.


## Projects Overview
### Capstone: Educational Content Process Automation Agent

  Goal: Automate educational workflows and personalize learning at scale.
  Architecture: Hybrid reasoning (ReAct/CoT/Planning), tool adapters, episodic/semantic/procedural memory, safety layer (input validation, bias detection, privacy).
  Notable features: LMS/document/academic search integrations (simulated), adaptive content generation, RL‑based strategy optimization.
  Results: 87.5% task success, ~0.4s avg response time, 100% safety violation detection in tests.
  Reports: Proposal and Final Report in capstone_educational_agent/docs/.


### Generative AI: Diffusion Model on MNIST

Model: U‑Net with time and class conditioning.
Process: 100‑step denoising; forward/reverse diffusion analysis; CLIP‑based evaluation.
Findings: Clear emergence phases during denoising; recommendations for DDIM, classifier‑free guidance, and progressive resolution training.

### Frameworks Comparison: TensorFlow vs PyTorch

Focus: Practical differences for research vs production.
Takeaway: PyTorch excels in research flexibility; TensorFlow strong in deployment tooling and scalability.

### Key Results and Metrics

Capstone agent: 87.5% success rate; average response ~0.4s; robust safety compliance.
Diffusion: Converged MSE ≈ 0.02; consistent digit quality with class‑conditioning; proposed accelerations (DDIM) for 5–10x faster sampling.

# Amodal Segmentation through Out-of-Task and Out-of-Distribution Generalization with a Bayesian Model
Total Score: 11 – Decision: Include
Methods Used: CNN features + Bayesian generative model, evaluated across explicit occlusion levels
Data Type: Images with varying occlusion (OccludedVehicles, COCOA cls, KINS)
Justification: Directly analyzes amodal segmentation performance as a function of occlusion level, reporting results across multiple occlusion bins and showing larger gains at high occlusion 1.1. Strong domain/method relevance and detailed metrics make it central for the review.
# Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images
Total Score: 10 – Decision: Include
Methods Used: Conditional 3D generative model with mask‑weighted and occlusion‑aware attention
Data Type: Synthetic and real occluded object images, single‑view to 3D
Justification: Focuses on reconstructing full 3D objects from partial observations, explicitly designing occlusion-aware attention and comparing to 2D-amodal-then-3D baselines that degrade under occlusion 2.1. Highly method- and domain-relevant to amodal completion under occlusion.
# Stable Diffusion-Based Approach for Human De-Occlusion
Total Score: 10 – Decision: Include
Methods Used: Two-stage pipeline (mask completion then RGB completion) using diffusion priors, VQA/CLIP conditioning
Data Type: Human images with real and synthetic occlusions (AHP, COCOA)
Justification: Tackles amodal mask and appearance completion for severely occluded humans, and reports superior performance, especially in occluded regions and in-the-wild occlusions 3.1. Very relevant for understanding performance under different occlusion severities.
# TACO: Taming Diffusion for in-the-wild Video Amodal Completion
Total Score: 10 – Decision: Include
Methods Used: Conditional video diffusion model, progressive fine-tuning over synthetic occlusion difficulty levels
Data Type: Synthetic videos with systematically imposed occlusions; in-the-wild videos
Justification: Directly addresses Video Amodal Completion using data with multiple occlusion difficulty levels and shows generalization to complex real occlusions 4.1. Highly informative about how occlusion level impacts model training and performance.
# Sequential Amodal Segmentation via Cumulative Occlusion Learning
Total Score: 10 – Decision: Include
Methods Used: Diffusion model with cumulative occlusion learning for sequential amodal segmentation and layer prediction
Data Type: Multiple amodal datasets with layered occlusions
Justification: Explicitly models multiple layers of occlusion and tests robustness as occlusion complexity increases, highlighting advantages in heavily occluded, multi-layer scenes . Strong fit to the occlusion-level/completion question.
# Amodal Scene Analysis via Holistic Occlusion Relation Inference and Generative Mask Completion
Total Score: 9 – Decision: Include
Methods Used: Holistic Occlusion Relation Inference + diffusion-based Generative Mask Completion
Data Type: Large-scale amodal segmentation dataset with mutual occlusions
Justification: Jointly reasons about occlusion relations and amodal mask completion, handling mutual occlusions and providing benchmarks showing advantages over prior work 6.1. Useful for understanding performance in complex occlusion patterns.
# Unseen Object Amodal Instance Segmentation via Hierarchical Occlusion Modeling
Total Score: 9 – Decision: Include
Methods Used: Hierarchical Occlusion Modeling within UOAIS-Net; large synthetic RGB‑D dataset
Data Type: Photorealistic RGB‑D with diverse occlusion scenes; tabletop/indoors/bin benchmarks
Justification: Defines a task that jointly predicts visible masks, amodal masks, and occlusions and shows state-of-the-art performance under cluttered occlusions 7.1. Highly relevant for amodal completion in robotics contexts.
# Perceiving the Invisible: Proposal-Free Amodal Panoptic Segmentation
Total Score: 8 – Decision: Include
Methods Used: Proposal-free amodal panoptic network (PAPS) with layered occlusion ordering and amodal mask refiner
Data Type: Driving datasets with significant occlusions (BDD100K-APS, KITTI-360-APS)
Justification: Introduces relative occlusion ordering layers and studies their number’s effect on performance, directly tying model accuracy to occlusion complexity 8.1. Good for understanding structural modeling of occlusion level.
# Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark
Total Score: 8 – Decision: Include
Methods Used: Point-supervised amodal instance segmentation with layer priors
Data Type: 267K+ synthetic images with intra-class occlusions, amodal masks, dual order relations, appearance
Justification: Provides large-scale amodal completion benchmarks with explicit intra-class occlusion scenarios, enabling systematic study of performance under heavy intra-class occlusion 9.1. Valuable for controlled occlusion-level analyses.
# Unveiling the Invisible: Reasoning Complex Occlusions Amodally with AURA
Total Score: 8 – Decision: Maybe
Methods Used: Amodal reasoning segmentation model integrating language-based reasoning and spatial designs
Data Type: New dataset of daily-life scenes with diverse real-world occlusions
Justification: Defines amodal reasoning segmentation for complex occlusions and introduces a dataset focused on diverse occlusion patterns 10.1. Conceptually aligned, though less explicit about quantitative dependence on occlusion level, so marked as “Maybe”.
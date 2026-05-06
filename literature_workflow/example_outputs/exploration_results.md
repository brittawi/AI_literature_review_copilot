I’m pulling the note file into view so I can anchor the recommendations to exactly what’s in the extracted methods.

I have the core method themes pinned down: structural priors, synthetic occlusion training, and occlusion-aware architectures. I’m now mapping them to fields where those exact method families are already common, then I’ll add search queries and safer alternatives.

Thought for 38s

Based on the notes, the recurring method families are structural priors (multi-view, 3D shape, and semantic/VLM priors), synthetic or paired occlusion training, and occlusion-aware architectural components; the notes also say performance drops when occlusion is extreme and structural cues are missing.

# 1) Other research fields
## A. Medical imaging

These methods fit well for anatomical completion, segmentation, and reconstruction when structures are partially hidden or missing. 3D priors and attention over visible regions are especially relevant when scans are incomplete or noisy.

### Search queries

"medical imaging" "3D shape prior" differentiable rendering occlusion completion
"medical image segmentation" mask-weighted attention visible regions
"self-supervised" synthetic occlusion paired clean occluded medical images

### Example papers

Use search queries above to identify relevant papers.
## B. Autonomous driving / robotics

Occlusion is central in road scenes and robot perception, where objects are blocked by cars, pedestrians, or scene layout. Multi-view supervision, 3D reconstruction, and occlusion-aware attention are directly useful for inferring hidden geometry and object extent.

### Search queries

"autonomous driving" multi-view 3D shape prior occlusion reasoning
"robotics" occlusion-aware attention visible regions object completion
"self-supervised" synthetic occlusion multi-view supervision autonomous driving

### Example papers

MV3D: Multi-View 3D Object Detection Network for Autonomous Driving (Chen et al., 2017)
Frustum PointNets for 3D Object Detection from RGB-D Data (Qi et al., 2018)
## C. Remote sensing / earth observation

Aerial and satellite imagery often contains partial visibility from clouds, shadows, and scene clutter. That makes multi-view consistency, synthetic occlusion, and structural priors useful for reconstructing hidden regions or improving robustness.

### Search queries

"remote sensing" multi-view 3D reconstruction occlusion-aware fusion
"earth observation" synthetic occlusion training visible occluded regions
"remote sensing" differentiable rendering shape prior completion

### Example papers

Use search queries above to identify relevant papers.
# 2) Alternative approaches
## 1. Probabilistic generative completion

Use a probabilistic model or diffusion-based inpainting setup that predicts multiple plausible completions instead of a single deterministic output. This is a good fit because the notes show that heavy occlusion creates ambiguity and that structural cues can be insufficient.

## 2. Uncertainty-aware modeling

Add Bayesian uncertainty estimates or deep ensembles so the model can express where it is relying on weak evidence. That would help diagnose failure cases when masks are inaccurate or when occlusion is too severe for the available priors.

## 3. Relation-based scene reasoning

Represent objects and parts as a graph and infer missing regions from object-object and part-whole relations. This differs from the noted 3D/multi-view/VLM priors and could be useful when local visual evidence is too sparse but contextual relations remain informative.
1. Themes
Theme 1: Use of Structural Priors (2D/3D/Multi-view) for Amodal Completion
Focus on incorporating geometric or structural knowledge to recover occluded regions.
Theme 2: Handling and Simulation of Occlusion in Training Data
Strategies for generating, annotating, or leveraging occluded vs. unoccluded data.
Theme 3: Performance Under Varying Occlusion Levels
Observations about model robustness, especially under heavy occlusion.
Theme 4: Architectural Mechanisms for Occlusion Awareness
Model components explicitly designed to reason about visible vs. occluded regions.

2. Grouping Notes into Themes
Theme 1: Structural Priors (2D/3D/Multi-view)
Paper C (DeOcc-1-to-3)
Multi-view pseudo ground truth generation (6 views)
Highlights limitation of 2D models lacking 3D priors → geometric inconsistency 
Paper D (A3D)
3D shape prior reconstruction from 2D input
Differentiable rendering to obtain amodal mask
ShapeDict (2D priors) and cross-view consistency assumptions 
Paper B (Know3D)
Uses VLM + diffusion + structural priors (latent/image/DINO features)
Multi-view (front/back) supervision via text annotations 

Theme 2: Handling and Simulation of Occlusion in Training Data


Paper A (Amodal3R)


Synthetic dataset with 3D-consistent occlusions


Requires visible mask + occluder mask 




Paper C (DeOcc-1-to-3)


Self-supervised setup with synthetically generated occlusions


Paired occluded/unoccluded images


Limited real data with heavy occlusions 




Paper B (Know3D)


Uses paired front/back views and text annotations (not explicit occlusion but related to missing views) 





Theme 3: Performance Under Varying Occlusion Levels


Paper C (DeOcc-1-to-3)


Struggles under extremely heavy occlusion due to missing structural cues


Notes scarcity of high-occlusion data 




Paper A (Amodal3R)


Claims good real-world performance despite synthetic training


Relies on accurate masks → potential sensitivity to occlusion complexity 




Paper B (Know3D)


Failure cases when model misinterprets spatial structure → indirectly linked to missing/ambiguous information 





Theme 4: Architectural Mechanisms for Occlusion Awareness


Paper A (Amodal3R)


Mask-weighted cross-attention focusing on visible regions


Occlusion-aware attention distinguishing occluders vs. background 




Paper D (A3D)


Two-branch architecture (shape + viewpoint)


Region-specific refinement for amodal mask 




Paper B (Know3D)


Multimodal fusion (image + text) for semantic guidance


Intermediate latent representations guide generation 





3. Connections
Similarities Across Papers


Reliance on priors to compensate for missing information


Papers B, C, and D all incorporate structural or semantic priors (3D shapes, multi-view, or VLM knowledge).




Use of synthetic or constructed data


Papers A and C explicitly generate occlusions synthetically.


Paper B constructs paired views and annotations to simulate missing perspectives.




Recognition of limitations in purely 2D approaches


Paper C explicitly states 2D completion lacks multi-view reasoning.


Paper D bridges 2D → 3D to overcome this.





Key Differences


Type of prior used


Paper D: explicit 3D shape priors


Paper C: multi-view diffusion-based priors


Paper B: semantic + multimodal (VLM) priors


Paper A: attention-based, mask-driven reasoning (less explicit geometric prior)




Handling of occlusion information


Paper A: explicitly models occluders via masks


Paper C: learns from synthetic occlusion pairs


Paper B: does not explicitly model occlusion but addresses missing views


Paper D: infers occlusion via projection from reconstructed 3D shapes




Behavior under high occlusion


Paper C explicitly reports degradation under heavy occlusion


Paper A depends on availability of accurate masks


Paper B failures tied to semantic/spatial ambiguity rather than occlusion level per se





Overall Insight
Across papers, higher occlusion levels increase reliance on strong priors (3D, multi-view, or semantic). However, performance degrades when structural cues are insufficient, especially in extreme occlusion scenarios or when models lack explicit mechanisms to reason about occluders.
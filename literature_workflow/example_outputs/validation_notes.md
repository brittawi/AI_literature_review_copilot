# Identification of papers

- Used prompt in Consensus: How does the occlusion level affect amodal appearance completion? => How does occlusion level influence the performance of machine learning models on amodal completion tasks? 
- with Deep Search
- 50 papers were included in review 
- All papers are saved in Zotero

Litmaps:
- added 4 papers to Litmaps based on how relevant Consensus thought they were + area (psycology):
    - Modal and Amodal Completion Generate Different Shapes
    - Variational Amodal Object Completion
    - Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images
    - Amodal Ground Truth and Completion in the Wild

=> got a total of 21 there (some might be double)

added 4 very recent articles that I found on arxiv

=> after removing duplicates => 63 papers

=> Initial results were biased toward psychology literature due to ambiguous terminology (e.g., "amodal completion"), highlighting the importance of domain-specific query formulation.

# Screening
- after year: 7 papers are from the year 2025
- citation Count: 
    - One paper from 2025 got 30 citations already
- AI-based screening:

=> returned 10 papers

# Exploration
Notes from the papers (very high level):
- Bayesian generative models
- Diffusion models
- Conditional 3D reconstruction
- occlusion-aware attention layer to differentiate between foreground occluders and background
- DINO to extract features from the occluded image
- Layered occlusion modeling
- Diffusion-based human body prior (provides comprehensive information about the
human body) and occluded joint heatmap (to explicitly inform the network about
occluded regions) for the mask completion
- produce human-centric descriptions using VQA model; CLIP might include background info that is not directly related to the human subject
- mostly synthetic datasets => real world data is missing
- MLLMs used to guide the inpainting process

=> got 3 papers from this:
Denoising Diffusion Probabilistic Models — Ho et al., 2020
DINO: Emerging Properties in Self-Supervised Vision Transformers — Caron et al., 2021
NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis — Mildenhall et al., 2020

# Extraction of Claims
Paper A: Amodal3R (Wu et al., 2025)
Notes:
- mask-weighted cross-attention to focus on visible parts of the object
- occlusion-aware attention layer to differentiate between foreground occluders and background => this identifies the potential regions requiring completion
- Training data is synthetic but they claim that this model still works well on real-world data
- Use DINO to extract features from the occluded image (I think it is used on the visible part of the object of interest only)
- based on Trellis
- Limitation: needs both visible mask and also mask of occluders
- Dataset: somehow they create 3D consistent occlusions

Paper B: Know3D: Prompting 3D Generation with Knowledge from Vision-Language Models
Notes:
utilize VLM-diffusion-based model (Qwen Image Edit) => VLM is responsible for semantic understanding + provides guidelines for image generation => diffusion model is responsible for generating images
    
- **Qwen-Image-Edit => two notable shortcomings:**
    
    - often misinterprets spatiat orientation => failing to accurately generate a back-view
        
    - frequently alters the subjetcs original pose/action in the output
        
    - => fine-tune Qwen-Image-Edit to „improve the spatial awareness for better stability“ (Chen et al., 2026, p. 3)
        
    - „annotate the corresponding textual description of the back-view“ (Chen et al., 2026, p. 3) => for training
        
- Evaluated the following strategies for using **image-space structural priors** as an intermediate medium:
    
    - „fully denoised VAE latent from MMDiT“ (Chen et al., 2026, p. 4)
        
    - „decoding this fully denoised VAE latent into an image and then extracting features via DINOv3 [41]“ (Chen et al., 2026, p. 4)
        
    - „directly using the hidden states from the intermediate layers of MMDiT during the denoising process“ (Chen et al., 2026, p. 4)
        
- Dataset used for validation: Hy3d
    
- **Text annotation pipeline** => use paired front + back views => VLM generates intitial part-level descriptions => could this be used in our context?! => when using both occluded and fully visible image?
    
- **Method**:
    
    - Input: Input image + text describing back view of image
        
    - fine-tune Qwen-Image-Edit on paired front-back view data
        
    - Know3D => „knowledge-guided 3D generation framework“ (Chen et al., 2026, p. 5)
        
- **Stochastic Prompt Construction!**
    
- MMDiT = Multimodal Diffusion Transformer
        
- LoRA = Low-Rank Adaptation
    
- Failure cases => when multimodal foundation model misinterprets instructions
**Architecture:**
    
    - Qwen2.5-VL encodes image + text prompt into high-level semantic features
        
    - VAE encoder extracts visual features from the front-view input
        
    - => these representations guide the MMDiT through the iterative denoising process
        
    - => intermediate latent hidden states are extracted from MMDiT layers
        
    - 3D model generation is build upon Trellis

Paper C: DeOcc-1-to-3: 3D De-Occlusion from a Single Image via Self-Supervised Multi-View Diffusion
Notes:
use paired unoccluded and occluded images for self-supervised training. They create the occlusions themselves, then they create pseudo GT for the unoccluded image by using a pretrained multi-view generation model => generate 6 pseudo GT
- "2D completion models are inherently limited by their lack of multi-view reasoning and may produce geometrically inconsistent outputs when extended to 3D."
2D inpainting lacks 3D priors => fails to ensure multi-view consistency
    
- „view synthesis is unaware of uncertainties in hallucinated content, leading to artifacts;“ (Qu et al., 2025, p. 2)
    
- two stages => prevents joint optimization => error accumulation
    
- self-supervised training => paired occluded and unoccluded images => synthetic!
    
    - for each unoccluded image, pretrained multi-view generation model generates six-view pseudo-ground-truths
        
- „2D completion models are inherently limited by their lack of multi-view reasoning and may produce geometrically inconsistent outputs when extended to 3D.“ (Qu et al., 2025, p. 3)
    
- very little data with high occlusions
    
- „still struggles under extremely heavy occlusions where structural cues are severely missing.“ (Qu et al., 2025, p. 9)

Paper D: 2D Amodal Instance Segmentation Guided by 3D Shape Prior (ECCV 2022)
Notes:
2 Observations:
    
    - 2D amodal mask is the projection of a 3D complete model
        
    - 3D complete model can be recovered + reconstructed from the occluded 2D object instances
        
- ShapeDict:
    
    - Dictionary of 2D shape priors
        
    - used kmeans to cluster them and then during inference find closest shape
        
    - problematic for generalization to new views/objects
        
- Amodal 3D Network (A3D) => coarse to fine architecture
    
    1) obtain visible mask
    
    2) two branch structure: Encoder-Decoder-Network for Category specific 3D shape prior reconstruction; Viewpoint estimator
    
    3) Differentiable Render => projects 3D shape prior model according to the predicted viewpoint to the 2D amodal mask
    
    4) Region-specific edge refine module => refine amodal mask
    
- single-view unsupervised 3D reconstruction methods
    
- pretrain the network on the 3D reconstruction dataset in an unsupervised manner; then finetune on 2D AIS dataset
    
- Different approaches for overlapping and non-overlapping categories
    
- Cross-view technique => 2 objects with different viewpoints should produce similar 3D model
# Literature Review Report

## Top Papers
- Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark (Score: 6)
- Image Amodal Completion: A Survey (Score: 6)
- Amodal Ground Truth and Completion in the Wild (Score: 6)
- Open-World Amodal Appearance Completion (Score: 6)
- Hyper-Transformer for Amodal Completion (Score: 6)

## Most recent papers
- PHAC: Promptable Human Amodal Completion (2026)
- Integrating Multimodal Large Language Model Knowledge into Amodal Completion (2026)
- Training for X-Ray Vision: Amodal Segmentation, Amodal Content Completion, and View-Invariant Object Representation from Multi-Camera Video (2025)
- Open-World Amodal Appearance Completion (2024)
- Hyper-Transformer for Amodal Completion (2024)

## Key Themes
### Amodal Datasets and Benchmarks
- The paper introduces two new amodal datasets (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- A new evaluation benchmark is constructed (Source: Amodal Ground Truth and Completion in the Wild)
- MOVi-MC-AC is the largest amodal segmentation and first amodal content dataset to date (Source: Training for X-Ray Vision: Amodal Segmentation, Amodal Content Completion, and View-Invariant Object Representation from Multi-Camera Video)

### Performance and Evaluation
- The approach outperforms fully supervised methods (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- Layer priors design exhibits remarkable performance improvements (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- Our method exhibits improved photorealistic completion results (Source: Amodal Completion via Progressive Mixed Context Diffusion)

### Challenges and Solutions
- Previous work relied on manual annotation for amodal segmentation ground truth (Source: Amodal Ground Truth and Completion in the Wild)
- Traditional methods often rely on two-stage processes or additional information, leading to inefficiencies and potential error accumulation. (Source: Hyper-Transformer for Amodal Completion)
- The authors propose to tackle these issues by building upon advances in object recognition and using recently created large-scale datasets. (Source: Amodal Completion and Size Constancy in Natural Scenes)

### Applications and Future Directions
- Image amodal completion aims to equip computers with human-like amodal completion functions (Source: Image Amodal Completion: A Survey)
- PHAC introduces a new task that completes occluded human images while satisfying both visible appearance constraints and multiple user prompts (Source: PHAC: Promptable Human Amodal Completion)

### Techniques and Approaches
- The framework uses a hyper transformer equipped with a dynamic convolution head to directly learn shape priors and accurately predict amodal masks. (Source: Hyper-Transformer for Amodal Completion)
- Our method harnesses the real-world knowledge of Multimodal Large Language Models to guide amodal completion (Source: Integrating Multimodal Large Language Model Knowledge into Amodal Completion)
- Focal length prediction can be used to overcome inherent scaling ambiguities by exploiting scene recognition. (Source: Amodal Completion and Size Constancy in Natural Scenes)

## Sample Claims
- The paper introduces two new amodal datasets (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- The approach outperforms fully supervised methods (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- Layer priors design exhibits remarkable performance improvements (Source: Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark)
- Image amodal completion aims to equip computers with human-like amodal completion functions (Source: Image Amodal Completion: A Survey)
- Previous work relied on manual annotation for amodal segmentation ground truth (Source: Amodal Ground Truth and Completion in the Wild)
- A new evaluation benchmark is constructed (Source: Amodal Ground Truth and Completion in the Wild)
- reasoning amodal completion (Source: Open-World Amodal Appearance Completion)
- Traditional methods often rely on two-stage processes or additional information, leading to inefficiencies and potential error accumulation. (Source: Hyper-Transformer for Amodal Completion)
- The framework uses a hyper transformer equipped with a dynamic convolution head to directly learn shape priors and accurately predict amodal masks. (Source: Hyper-Transformer for Amodal Completion)
- We overcome two technical challenges (Source: Amodal Completion via Progressive Mixed Context Diffusion)

## Notes
## Summaries
### Amodal Intra-class Instance Segmentation: Synthetic Datasets and Benchmark
This paper introduces two new amodal datasets for image amodal completion tasks, which contain a total of over 267K images of intra-class occlusion scenarios, annotated with multiple masks, amodal bounding boxes, dual order relations and full appearance for instances and background. It also presents a point-supervised scheme with layer priors for amodal instance segmentation specifically designed for intra-class occlusion scenarios.

### Image Amodal Completion: A Survey
Existing computer vision systems can compete with humans in understanding the visible parts of objects, but still fall short when it comes to depicting the invisible parts of partially occluded objects. The survey aims to provide an intuitive understanding of research hotspots, key technologies and future trends in image amodal completion.

### Amodal Ground Truth and Completion in the Wild
The paper studies amodal image segmentation by establishing an automatic pipeline to determine authentic ground truth amodal masks for partially occluded objects in real images. It constructs a new evaluation benchmark, MP3D-Amodal, and explores two architecture variants for better handling the task.

### Open-World Amodal Appearance Completion
The paper introduces Open-World Amodal Appearance Completion, a training-free framework that reconstructs the full appearance of queried objects based on images and language queries. The approach generalizes to arbitrary objects specified by direct terms or abstract queries.

### Hyper-Transformer for Amodal Completion
A novel framework named the Hyper-Transformer Amodal Network (H-TAN) is introduced for amodal object completion, which directly learns shape priors and predicts amodal masks.

### Amodal Completion via Progressive Mixed Context Diffusion
Our brain can effortlessly recognize objects even when partially hidden from view. We propose a method to achieve this amodal completion task in generative AI, sidestepping two-step processes and using pre-trained diffusion inpainting models.

### PHAC: Promptable Human Amodal Completion
Conditional image generation methods are increasingly used in human-centric applications, yet existing human amodal completion (HAC) models offer users limited control over the completed content. To address these limitations, we introduce promptable human amodal completion (PHAC), a new task that completes occluded human images while satisfying both visible appearance constraints and multiple user prompts.

### Integrating Multimodal Large Language Model Knowledge into Amodal Completion
With the widespread adoption of autonomous vehicles and robotics, amodal completion reconstructs the occluded parts of people and objects in an image. Existing approaches lack physical knowledge about real-world entities. The paper proposes AmodalCG, a framework that harnesses Multimodal Large Language Models to guide amodal completion.

### Amodal Completion and Size Constancy in Natural Scenes
The paper proposes methods to enrich object detection systems with veridical object sizes and relative depth estimates from a single image, tackling challenges like occlusions, lack of calibration data, and scale ambiguity.

### Training for X-Ray Vision: Amodal Segmentation, Amodal Content Completion, and View-Invariant Object Representation from Multi-Camera Video
The paper introduces MOVi-MC-AC, the largest amodal segmentation and first amodal content dataset to date. The dataset consists of multi-camera video with simulated cluttered scenes of generic household objects. It includes two new contributions: multiple camera settings for object tracking between unique perspectives and amodal content completion.

- Generated using AI-assisted literature copilot

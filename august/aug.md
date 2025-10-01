- August
    
    8.26
    
    8.27
    
    - Tensor Parallelism
        
        Tensor parallelism is a technique used in distributed deep learning to train large neural networks by splitting individual model weights, gradients, and optimizer states across multiple devices. This method, also known as intra-layer model parallelism, is particularly useful when a single layer or parameter of a neural network is too large to fit into the memory of a single device, such as a GPU.
        
        **Key aspects of tensor parallelism:**
        
        - **Splitting within layers:**
            
            Unlike pipeline parallelism, which partitions the model across layers, tensor parallelism focuses on distributing computations within specific operations, modules, or layers of the model, such as large matrix multiplications in fully-connected or convolutional layers.
            
        - **Memory efficiency:**
            
            By distributing the large tensors (weights, gradients, and optimizer states) across devices, tensor parallelism significantly reduces the memory footprint on each individual device, enabling the training of models with billions or even trillions of parameters.
            
        - **Communication overhead:**
            
            While reducing memory load, tensor parallelism often requires frequent communication between devices to ensure the correctness of computations. This necessitates high-speed interconnects like NVLink or specialized hardware like TPUs for efficient operation.
            
        - **No pipeline bubbles:**
            
            Unlike pipeline parallelism, which can suffer from "pipeline bubbles" (idle time for devices), tensor parallelism allows all devices to work on the same batch of data simultaneously, potentially leading to better computational efficiency.
            
        - **Examples:**
            
            Frameworks like Megatron-LM utilize tensor parallelism to efficiently train large transformer models by parallelizing operations within their layers.
            
    - extract PRD prompt
        
        ```bash
        You are an AI that extracts structured data from product requirement documents.
        
        Extract the following fields from the document:
        - Title
        - Summary
        - Feature List
        - Priority
        - Stakeholders
        - Dependencies
        - Acceptance Criteria
        
        Output the result as structured JSON.
        
        Here is the document:
        """
        <insert raw PRD>
        """
        
        ```
        
    - json examples
        
        Example Input:
        <some real PRD>
        
        Expected Output:
        {
        "title": "User login",
        "summary": "Support email/password login for all users",
        ...
        }
        
        Now extract from the following:
        """
        <new PRD>
        """
        
    
    8.29 thinkin bout that time i got cline set up… (you mean 2 days ago? lol) 
    
    8.31  INTERNAL AUDIT of Bill Gates-founded company Microsoft's digital cloud system for being used by Chinese Nationals to hack the DoD systems

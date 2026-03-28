# **Homework 2 Instructions**

---

## 🧰 1. Required Libraries

The following libraries will be used in this assignment:

```python
pip install numpy matplotlib scipy opencv-python
```

> ⚠️ **Notice:**  
> `cv2` should only be used for image conversion (e.g., `BGR2RGB`, `BGR2GRAY`).  
> It **must not** be used directly for the required code in this assignment (e.g., `cv2.Sobel`, `cv2.Laplacian`, `cv2.cornerHarris`).

---

## 📄 2. Python Files

- `hw2.py` — Main execution file  
- `Harris_Corner_Detection.py` — Function implementation file
**The program will automatically:**
1. Load the input image
2. Perform Harris Corner Detection
3. Save all intermediate and final results

---

## ▶️ 3. Running the Program

To execute the program and generate output images, run:

```bash
python hw2.py
```

---

## ⚙️ 4. Functions Included

The following functions are implemented and required:

- `gaussian_smooth()`  
- `sobel_edge_detection()`  
- `structure_tensor()`  
- `NMS()` — Non-Maximum Suppression  
- `rotate()`

---

## 📁 5. Contents of the `results` Folder

The `results/` directory contains five subfolders, each corresponding to an output stage:

---

### 📂 (1) `Gaussian smooth results`

**Contains 2 images:**
- Gaussian smoothing with **σ = 5**, kernel size = **5**
![Gaussian Smoothing Results K=5](./results/Gaussian%20smooth%20results/gaussian_smooth_of_sigma_and_kernal_size_5.jpg)
*Figure 1. Gaussian Smoothing Results (Kernel size = 5)*
- Gaussian smoothing with **σ = 5**, kernel size = **10**
![Gaussian Smoothing Results K =10](./results/Gaussian%20smooth%20results/gaussian_smooth_of_sigma_and_kernal_size_10.jpg)
*Figure 2. Gaussian Smoothing Results (Kernel size = 10)*
---

### 📂 (2) `Sobel edge detection results`

**Contains 4 images:**
- **Gradient Magnitude** using Gaussian kernel size 5 and 10 → 2 images
![Gradient Magnitude K=5](./results/Sobel%20edge%20detection%20results/magnitude_of_gradient_kernel_size_5.jpg)
*Figure 3. Gradient Magnitude (Kernel size = 5)*
![Gradient Magnitude K=10](./results/Sobel%20edge%20detection%20results/magnitude_of_gradient_kernel_size_10.jpg)  
*Figure 4. Gradient Magnitude (Kernel size = 10)*
- **Gradient Direction** using Gaussian kernel size 5 and 10 → 2 images
![Gradient Direction K=5](./results/Sobel%20edge%20detection%20results/direction_of_gradient_kernel_size_5.jpg)
*Figure 5. Gradient Direction (Kernel size = 5)*
![Gradient Direction K=10](./results/Sobel%20edge%20detection%20results/direction_of_gradient_kernel_size_10.jpg)
*Figure 6. Gradient Direction (Kernel size = 10)*
---

### 📂 (3) `Structure tensor + NMS results`

**Contains 2 images:**
- Structure tensor with window size **3×3**
![NMS WS=3](./results/Structure%20tensor%20+%20NMS%20results/NMS_window_size_3.jpg)
*Figure 7. NMS WS=3*
- Structure tensor with window size **30×30**
![NMS WS=30](./results/Structure%20tensor%20+%20NMS%20results/NMS_window_size_30.jpg)
*Figure 8. NMS WS=30*
---

### 📂 (4) `Final results of rotating`
**Contains 1 image:**
- Image rotated by **30°**
![Rotate](./results/Final%20results%20of%20rotating/Rotate_30.jpg)
*Figure 9. Rotate*
---

### 📂 (5) `Final results of scaling`

**Contains 1 image:**
- Image scaled to **0.5×**
![Scale](./results/Final%20results%20of%20scaling/Scaling.jpg)
*Figure 10. Scaling*

---

## 🖼️ 6. Workflow Summary
**The Harris corner detection pipeline in this homework follows these steps:**

Input Image
   ↓
Gaussian Smoothing
   ↓
Gradient Computation (Sobel)
   ↓
Structure Tensor
   ↓
Harris Response
   ↓
Non-Maximum Suppression (NMS)
   ↓
Final Corner Points

- This workflow is also applied to the rotated and scaled versions of the original image.

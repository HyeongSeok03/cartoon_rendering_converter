import cv2
import numpy as np

# 이미지 경로
img_path = '/Users/fluor/Documents/Workspace/Unity/Unity Projects/cartoon_rendering_converter/assignment_image2.jpg'

# 이미지 불러오기
img_color = cv2.imread(img_path)
if img_color is None:
    raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {img_path}")

# 1. 색상 면 처리 (color quantization using k-means)
Z = img_color.reshape((-1, 3)).astype(np.float32)
K = 8  # 색상 수 (줄일수록 더 카툰 느낌)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
quantized = centers[labels.flatten()].reshape(img_color.shape)

# 2. 윤곽선 검출 (adaptive threshold + bilateral filter)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)
edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

# 3. 윤곽선 반전 → 마스크로 사용
edge_mask = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # 3채널로 변환
cartoon = cv2.bitwise_and(quantized, edge_mask)

# 결과 출력
cv2.imshow("Original", img_color)
cv2.imshow("Cartoon Rendered", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 저장하려면
# cv2.imwrite("cartoon_rendered_output.jpg", cartoon)

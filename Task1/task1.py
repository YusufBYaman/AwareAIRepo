#OpenCV kütüphanesini kullanarak herhangi bir fotoğraf (PNG/JPG) açın. Açılan fotoğrafı farklı bir isimle aynı dizine kaydedin.

import cv2

resim = cv2.imread("Gemini_Generated_Image.png")

if resim is not None:
    cv2.imshow("Resim", resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("kaydedilen_resim.png", resim)
    print("Resim başarıyla kaydedildi.")

else:
    print("Resim yüklenemedi.")
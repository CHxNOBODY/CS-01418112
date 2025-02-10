def generate_bigrams(word):
    
    word = word.lower()
    
    # สร้าง bigrams
    bigrams = set()  # ใช้ set เพื่อไม่ให้มี bigram ซ้ำ
    for i in range(len(word) - 1):
        bigram = word[i:i+2]  # สร้าง bigram จากตัวอักษรสองตัวติดกัน
        bigrams.add(bigram)   # เพิ่ม bigram ลงใน set

    # แปลง set เป็น list และเรียงลำดับ
    sorted_bigrams = sorted(bigrams)

    # แสดงผล bigrams
    for bigram in sorted_bigrams:
        print(bigram)


input_word = input()
generate_bigrams(input_word)
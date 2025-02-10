def remove_duplicates(t):
    seen = set() #สร้างเซ็ตว่างเพื่อใช้ติดตามสิ่งที่เราได้เห็นไปแล้ว
    result = []
    for item in t:
        if item not in seen:
            seen.add(item) #.add คือการที่เราจะเพิ่มข้อมูลนั้นเข้าไปแต่ถ้าเกิดว่าเจอตัวซ้ำจะไม่ทำการเพิ่มเข้าไป
            result.append(item)
    return result
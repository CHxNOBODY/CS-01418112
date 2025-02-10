original_text = input()  
search_word = input()     
replace_word = input()    
start_pos = int(input())  
replace_count = int(input())  

sub_text = original_text[start_pos:]

modified_sub_text = sub_text.replace(search_word, replace_word, replace_count)

result_text = original_text[:start_pos] + modified_sub_text

print(result_text)
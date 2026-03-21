import re

def clean_name(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
    
    cleaned = name.replace(" ", "").lower()
    
    if not re.fullmatch(r"[a-z]+", cleaned):
        raise ValueError("Names should contain only alphabets.")
    
    return cleaned


def calculate_flames(name1, name2):
    cleaned_name1 = clean_name(name1)
    cleaned_name2 = clean_name(name2)
    
    len1 = len(cleaned_name1)
    len2 = len(cleaned_name2)
    
    list1 = list(cleaned_name1)
    list2 = list(cleaned_name2)
    
    for char in cleaned_name1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    
    count = len(list1) + len(list2)
    
    if count == 0:
        return {
            "name1": cleaned_name1,
            "name2": cleaned_name2,
            "length1": len1,
            "length2": len2,
            "result": "Both names are identical."
        }
    
    flames = ["F", "L", "A", "M", "E", "S"]
    
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames.pop()
    
    result_map = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    
    return {
        "name1": cleaned_name1,
        "name2": cleaned_name2,
        "length1": len1,
        "length2": len2,
        "result": result_map[flames[0]]
    }
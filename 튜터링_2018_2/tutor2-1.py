A = {1,3,5,6,7,9}
B = {2,3,5,7,10}

intersection = A&B
union = A|B
print("intersection :",intersection,
      "\nintersection의 개수:",len(intersection),
      "\nunion :", union,
      '\nunion의 개수:',len(union))
print("max :",max(intersection) + max(union))
print("min :",min(intersection) + min(union))
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
# Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
# Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
# Test.assert_equals(move_zeros(["a","b"]),["a","b"])
# Test.assert_equals(move_zeros(["a"]),["a"])
# Test.assert_equals(move_zeros([0,0]),[0,0])
# Test.assert_equals(move_zeros([0]),[0])
# Test.assert_equals(move_zeros([False]),[False])
# Test.assert_equals(move_zeros([]),[])

def move_zeros(array, idx=-1, rec_count=-1):
    idx += 1
    rec_count += 1 
    if len(array)-1 <= rec_count:
        return array
    if array[idx] == 0 and array[idx] is not False: 
        array.append(array.pop(idx))
        idx-=1       
    return move_zeros(array, idx=idx, rec_count=rec_count)

print('output: ',move_zeros([False,1,0,1,2,0,1,3,"a"]))
print('output: ',move_zeros([1,2,0,1,0,1,0,3,0,1]))
print('output: ',move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print('output: ',move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print('output: ',move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print('output: ',move_zeros([0,1,None,2,False,1,0]))
print('output: ',move_zeros(["a","b"]))
print('output: ',move_zeros(["a"]))
print('output: ',move_zeros([0,0]))
print('output: ',move_zeros([0]))
print('output: ',move_zeros([False]))
print('output: ',move_zeros([9, 0.0, 9, 1, 2, 1, 1, 0.0, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0]))
print('output: ',move_zeros(['a', 0, 'b', 'c', 'd', 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
print('output: ',move_zeros(['a', 0, 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, 0, {}, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
print('output: ',move_zeros([1,2,3,4,5,6,7,8,9,0,1]))
print('output: ',move_zeros([1]))
print('output: ',move_zeros([]))
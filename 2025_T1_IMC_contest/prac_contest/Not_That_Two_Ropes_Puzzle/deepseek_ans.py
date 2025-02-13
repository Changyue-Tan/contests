'''
Okay, let's see. The problem is about finding two ropes whose sum equals T. But wait, the ropes are all distinct, right? Because the input says they are distinct. So each ti is unique, and we need to choose exactly two different ropes. So the sum of two different ropes' burn times should be exactly T.

Hmm. So the approach here is to find two numbers in the list that add up to T. That's a classic two-sum problem. But the twist here is that we can't use the same rope twice. But since all the ropes are distinct, as long as the two values are present in the list, their sum is T, then we're good.

So how to approach this efficiently? For n up to 1e5, a naive O(n^2) approach would be way too slow. So we need a better method. The standard way to handle two-sum is using a hash set, which allows O(1) lookups. Or, alternatively, sorting the array and using two pointers.

Wait, but there's a possible issue. For example, if T is even and there's a rope of T/2, but only one occurrence. Then trying to find two ropes would fail. But in this problem, since all ropes are distinct, T/2 can't appear twice. So if T is even and a rope of T/2 exists, but there's only one, then we can't use it. So the two-sum approach of checking if (current element) and (T - current element) exist in the set, but ensuring they are different elements.

Wait, no. Because if a is the current element, then T - a must be a different element. Because even if T is even and a is T/2, there's only one such rope. So in that case, even if T is even, the required pair can't be two copies of T/2 because there aren't two. So the two elements must be different, so the approach of using a hash set to check for presence of T - a is okay, but we need to make sure that a is not equal to T - a. Because if a is T - a, then that implies T is 2a, but since the list has only one occurrence of a, we can't pair it with itself.

So the correct approach is to loop through each element a in the list, check if (T - a) exists in the set, and also ensure that a and (T - a) are two different elements (i.e., T - a != a, or if T - a == a, then there must be at least two occurrences of a, but in our problem, the input has all distinct elements, so this is impossible). So in our problem, when checking for T - a, we can just check if it's present and also that it's not the same as a. Wait, but since the input has distinct elements, the T - a can't be a unless T is 2a, and since there's only one occurrence of a, we can't have two a's. So in such a case, even if T is 2a, but there's only one a, then the pair (a, a) is invalid.

So the correct condition is: for each a, check if (T - a) exists in the set, and (T - a) is not equal to a. Wait, no. Because the same element can't be used twice. So when a is in the list, and T - a is also in the list, but they are two different elements (since all elements are distinct). So if a and T - a are different, then it's okay. But if a and T - a are the same, but the list has only one occurrence, then it's not okay.

So for example, if T is 100, and the list has 50 once. Then 50 +50 = 100, but there's only one 50, so it's invalid.

So in our code, when we check for (T - a) in the set, we need to ensure that either (T - a) is a different value, or if it's the same value (i.e., T is even and a is T/2), then that value must appear at least twice. But in our problem, since all the input t_i are distinct, that can't happen. So, for the problem's constraints, all elements are distinct, so when a is T - a, then there's no other a to pair with. Hence, we can ignore such cases.

Therefore, the approach would be:

- For each a in the list, check if (T - a) exists in the set, and (T - a) != a.

But wait, how? Because in the problem, the elements are distinct. So if a is in the list, then T - a can only be a if T is 2a, but since there's only one a, the pair (a, a) is invalid. So in the code, after checking that (T - a) is present, we need to make sure that a is not equal to (T - a). Because if they are equal, then the pair is invalid.

Wait, but the problem says the ropes are distinct. So in the list, there are no duplicates. So if a is present, then T - a can be present or not. If T - a is present and different from a, then the pair is valid. If T - a is present and equal to a (i.e., T is 2a), but that's impossible because all elements are distinct. So T - a can't be a in the same list. Therefore, when a is in the list, T - a can only be a if T is 2a and the list contains a, but the list has only one occurrence. Hence, in that case, the pair (a, a) is invalid. So, in code, we can proceed as follows:

Create a hash set of all elements.

For each element a in the list:

compute b = T - a

check if b is present in the set.

if b is present and a != b, then output the pair (a, b).

But wait, in this case, if we have a and b, where b is in the set and a != b, then we can output them. But since the list is a set, we can have cases where a and b are two different elements. For example, in the first sample input, T=60. The list has 10, 20, 30, 40. When a is 20, b is 40. Since 40 is in the set and 20 !=40, so it's valid.

But how to avoid checking a and then checking b again later, which would find a and output the same pair in reverse. For example, in the first sample, when a is 40, b is 20, which is in the set, and a !=b. So we would find that and output 40 and 20. But the problem allows the output in any order. So the code would output either 20 40 or 40 20, which are both correct. However, if we process the elements in order, then the first occurrence where a and b are found would be the output. So we can break early once we find a pair.

But in the case where a and b are the same, but it's impossible here, so we don't have to worry about that.

So the algorithm steps:

1. Read n and T.

2. Read the list of t_i's.

3. Create a hash set (or a dictionary) for O(1) lookups.

4. Iterate through each t_i in the list:

a. Compute complement = T - t_i.

b. Check if complement exists in the set.

c. If exists and complement != t_i, then output YES and the two numbers (t_i, complement).

d. Since the problem allows any pair, once such a pair is found, we can exit immediately.

5. If after checking all elements no pair is found, output NO.

But wait, what about when the same pair is considered in reverse? For example, when a is t_i and the complement is found. Then when processing the complement element, the code would again find t_i as the complement and output again. But in the code, since we are iterating through all elements and checking, the first occurrence would trigger the output. So for example, in the first sample, when processing 20, we find 40. So we output 20 and 40. When processing 40, we find 20, which is in the set. But since the code is iterating through the elements in order, once the first pair is found, the code would output and exit. So no problem.

But how to make sure that we don't process the same pair again. Well, since the problem allows any order, the first occurrence is sufficient.

So the code's approach is correct.

But what about the sample 3?

Sample 3:

Input:

4 50

10 20 30 40

So possible pairs are 10+40=50, 20+30=50.

So during iteration, when processing 10, the complement is 40, which exists. So output 10 and 40. Correct.

Alternatively, if the code processes 40 first, then 10 is the complement and exists. So output 40 and 10.

Either is correct.

So the code's approach would work.

But in the code samples provided in the problem statement, the sample code in C++ uses a set, but there's a bug. Let's look at that.

In the C++ sample code:

The code inserts all ropes into a set (which is a sorted set). Then for each a in the set (which is the elements in order), checks if (target - a) is present. But the problem is that the elements in the list are stored in the set, but the original list may have duplicates (but according to the problem statement, the input ti are distinct). Wait, the problem says the input ti are distinct. So the set would have all the elements. But in the code, when iterating through the set, a and b can be the same. Wait, no, because the problem says all ti are distinct. So for example, if T is 20, and there's a rope of 10. Then the complement is 10. But since 10 is present once, the code would check if (10 != 10). Which is false, so it would not output anything. So that's correct.

But the code in the sample (Listing 3) has a problem. Let's see. Suppose the code is given the fourth sample input:

3 40

10 20 40

The list is [10,20,40]. The set is {10,20,40}. Target is 40. For each a in the set:

a=10: complement is 30, not present.

a=20: complement is 20. present? yes. But a equals complement. So code checks if ropes.count(b) (which is 20) exists. Yes, but a and b are the same. So the code outputs 20 and 20, but the problem requires two different ropes. So this code would output YES 20 20, which is incorrect.

But in the sample input 4, the output is NO. So the code in Listing 3 is incorrect because it doesn't check whether a and b are different elements.

Ah, right! So the code in Listing 3 has a bug. Because when a is 20 and T is 40, the complement is 20. The set has 20, so ropes.count(b) returns 1, which is true. But since the problem requires two different ropes, this would be invalid. So the code would output YES 20 20, but the correct answer is NO.

So the code's logic is wrong. Therefore, in the code, when checking for the complement, we need to make sure that either a and b are different elements, or that the element occurs more than once. But in this problem, since all elements are distinct, the only way for a and b to be same is if T is 2a. But since each a appears exactly once, that's impossible. So the code should check that a and b are different.

So the correct approach is, for each a, check if (T - a) exists in the set and (T - a) is not equal to a.

So in the code, the line:

if (ropes.count(b)) { ... }

needs to be:

if (ropes.count(b) && a != b) { ... }

In the sample input 4, when a is 20, b is 20. So a == b, so the condition is false, so the code doesn't output anything. So the code would correctly output NO.

So the code in Listing 3 has a bug where it doesn't check that a and b are different.

So the correct code would include that check.

Similarly, in the Python code (Listing 4), which uses binary search. Let's see. Suppose the code checks for the presence of T - a. But the code has a binary search function that returns True if the value is present. However, in the code, after finding a, it checks if (binary_search(0, n-1, b)), but doesn't check whether a and b are the same. So again, in the case where T is 40 and a is 20, and the list has only one 20, the code would output (20,20), which is invalid.

Therefore, the code needs to check that a and b are different, but since the list is sorted, how to do that. For example, if a is 20, and there is another 20 in the list, but according to the problem statement, the input has distinct elements, so this can't happen. So in the code, when a is 20, and T - a is 20, the binary search will find the same element. So in the code, the line:

if binary_search(0, n-1, b):

would return True if 20 is present. But since a and b are the same, the code would output (20,20), which is invalid. So the code in Listing 4 is also incorrect.

Thus, the correct code must check that a and b are different. So in both approaches (hash set and binary search), after finding that the complement exists, we need to check that it is not the same element as a.

So how to handle this in code.

For the hash set approach:

We can create a set (like a hash set) of all the elements. Then, for each a in the list, compute b = T - a. If b is in the set and b != a, then return a and b.

But in the code, since the elements are unique, when we check b in the set and b != a, that's sufficient.

But wait, what if the list contains a and b where b is present once and a is present once, and a + b = T, but a and b are different. Then the code will find them.

So the correct code must check for the existence of b and that a != b.

In the sample input 4, when a is 40, T - a is 0, which is not present. So no. When a is 20, T - a is 20. So checking if 20 is in the set. Yes. But a and b are the same. So invalid. So code must check for that.

Thus, the code in both Listings 3 and 4 are incorrect because they don't check if a and b are different.

So the solution is to add this check.

Now, considering that, let's think about the code.

In Python, for the binary search approach:

We have a sorted list. For each a in the list, compute b = T - a. Then check if b exists in the list (via binary search). Also, check that a != b.

But wait, in the list, since all elements are distinct, the same element can't appear again. So if a is 20, then if T - a is 20, and the list contains 20, then since the list is sorted, the binary search will find it. But since a is part of the list (since we are iterating through each a), then a and b are same. So the code needs to ensure that a != b.

So in the code:

if (binary_search finds b) and (a != b), then output.

But how to handle the case when a is present once and T is 2a. Then b is a, but since the list has only one occurrence, the pair (a, a) is invalid. So even if the code finds b in the list, it must check that a != b.

Thus, in the code, after finding that b is present, check whether a and b are different.

So in the code, the loop:

for a in ropes:

b = T - a

if binary_search finds b:

if a != b:

then output (a, b) and exit.

Thus, the code should have this check.

But in the sample code (Listing 4), the code does not check whether a and b are different. So that's a bug.

So the correct code would:

Once the binary search finds b in the list, check that a is not equal to b.

In the problem's fourth sample, when a is 20, T is 40. Then b is 20. The binary search finds 20. But a is 20, so the check a != b would be false, so the code skips that. Thus, the code would not output (20,20), which is correct.

Another example: if T is 50, and the list is [10,20,30,40]. When a is 10, b is 40. Check if 40 is present (yes), and 10 !=40 (yes). So output.

Similarly, when a is 40, b is 10. The binary search finds 10, which is present, and 40 !=10. So output.

But if the code checks all elements, the first occurrence (10) would trigger the output.

So the code in Python with binary search would need to check for a != b.

Similarly, in the hash set approach, the code must check that a and b are different.

Thus, the correct code for the problem requires that the complement is present and different from a.

Now, considering that, how to implement this.

Possible approaches:

1. Use a hash set (like a Python set), and for each a in the list, check if (T - a) is in the set and (T - a) != a.

But in the code, we can process the list as follows:

Read the list into a set.

For each a in the original list (not the set):

compute b = T - a.

if b in the set and a != b:

output YES and a, b.

exit.

If no such pair is found after all elements, output NO.

But why not process the set? Because the set may have elements in a different order. But in the code, the order in which we process the elements doesn't matter. As long as we find any pair (a, b) where a is in the list, and b is in the set, and a !=b, then we can output.

But wait, the list is the original list, which may have elements in any order. So for example, if the list is [20,40,10,30], and T=60, then processing the first element (20) would find 40 in the set, and output.

Yes.

But when creating the set, inserting all elements, the set will contain all the elements. So for each a in the original list, check if the complement exists and is different.

Thus, the code is:

Read n and T.

Read the list.

Create a set S of the list elements.

For each a in the list:

b = T - a.

if b in S and a != b:

print YES and a, b.

exit.

Print NO.

But wait, in the original list, when a is processed, and b is in the set, but b is in the list and is processed later, but the code will find the pair when a is processed and output. So the code will exit early.

But in this approach, the code may process elements in any order, but the first a for which (T - a) is present and a != b will be output.

But what about if the list has a pair (a, b) where a appears after b in the list. For example, list is [40,20, ...]. When processing 40, T -40 is 20. If 20 is in the set, then output 40 and 20. So it's correct.

But what if the set contains both a and b, but when a is processed first, the code outputs a and b. But in the list, maybe b is present. So the code will find the pair.

Yes.

Thus, this approach is correct.

So the code would work.

Testing the fourth sample input:

Sample 4:

Input:

3 40

10 20 40

Set S is {10,20,40}.

Processing each element:

10: b = 40-10=30. Not in S.

20: b =40-20=20. In S. But a == b (20 ==20). So condition a != b is false. So skip.

40: b=40-40=0. Not in S.

Thus, no pairs found. Output NO.

Which is correct.

Another test case: when T is 50, and list is [10,20,30,40].

Processing 10: b=40. 40 is in S, and 10 !=40. So output 10 and 40.

Which is correct.

Another case: T=60, list [20,40,10,30].

Processing 20: b=40. 40 is in S, 20 !=40. Output.

Thus, correct.

Thus, the code would work.

Now, considering the time constraints.

For n=1e5, the set approach in Python (using a built-in set) would have O(n) time for creating the set, and O(n) time for iterating through the list, with each lookup being O(1). So total time O(n), which is acceptable.

In Python, sets are hash tables, so lookups are O(1) average case.

Thus, the code would work for n=1e5.

But the code in the sample (Listing 4) uses binary search. Let's see.

If the list is sorted, and for each a in the list, compute b = T -a, then perform a binary search for b. But in this case, even if b is present, but is the same as a (i.e., T=2a and a is present once), then the code would output (a, a), which is wrong.

Thus, in the binary search approach, after finding that b is present, we need to check that a != b.

Thus, in the code:

for a in ropes:

b = target - a

if binary_search(b) and a != b:

output and exit.

Thus, that would be correct.

But binary search for each a would take O(n log n) time. For n=1e5, O(n log n) is acceptable, but the hash set approach is O(n), which is faster.

Thus, the hash set approach is better.

Thus, the correct code would be:

Read the list, create a set.

For each element in the original list:

compute complement = T - a.

if complement in the set and a != complement:

output the pair and exit.

If none found, output NO.

Thus, this approach is correct.

Now, considering the code in Python:

But wait, in Python, for the list, when you have a for loop over the elements, you process them in the order of the list. So the code would find the first element a for which (T -a) is present and a != (T -a). Thus, the first such pair found would be output.

So the code would look like:

n, T = map(int, input().split())

ropes = list(map(int, input().split()))

s = set(ropes)

for a in ropes:

b = T - a

if b in s and a != b:

print("YES")

print(a, b)

exit()

print("NO")

But wait, what if the complement is in the set but appears after a in the list? For example, the list is [10, 30, 20, 40], T=50. The code would process 10, then 30, then 20, then 40.

Processing 10: b =40. 40 is in the set. 10 !=40: output 10 and 40. Correct.

Yes.

Another example: list is [20,40,10,30], T=60. Processing 20: b=40. 40 is in the set. 20 !=40: output 20 and 40.

Thus, correct.

Thus, this code would work correctly.

Now, let's test the fourth sample input.

Sample 4:

3 40

10 20 40

s = {10,20,40}

Processing elements:

10: b=30. Not in s.

20: b=20. 20 is in s, but 20 ==20. So condition fails.

40: b=0. Not in s.

Thus, output NO. Correct.

Thus, the code is correct.

Thus, this is the correct solution.

Now, edge cases.

Test case where T is 2a, but a appears once. For example, n=2, T=20. Ropes are [10, 10]. But according to the problem statement, the input has distinct ropes. So this case is invalid. So the code would not have such a case.

Another edge case: n=2, T = a + b. So ropes are [a, b], and T = a +b. So code outputs YES.

Another edge case: n=2, T is not a +b. Output NO.

Another case: T is larger than the sum of the two largest ropes. So output NO.

Thus, the code should handle all cases.

Therefore, the correct solution is to use a hash set and check for the complement and whether a != b.

To solve this problem, we need to determine if we can measure exactly T minutes by burning two different ropes together. The solution involves checking if there exists a pair of ropes whose combined burning time equals T.

Approach
Problem Analysis: We need to find two distinct ropes such that their sum of burning times equals T. Since all ropes have distinct burning times, we can use a hash set to efficiently check for the existence of the required complement for each rope's burning time.

Hash Set for Efficient Lookup: By storing all rope burning times in a hash set, we can check in constant time whether the complement (T - current rope's burning time) exists in the set.

Check for Distinct Ropes: For each rope, compute the complement and ensure it is different from the current rope to avoid using the same rope twice.

Solution Code
python
Copy
'''
n, T = map(int, input().split())
ropes = list(map(int, input().split()))
s = set(ropes)
for a in ropes:
    b = T - a
    if b in s and a != b:
        print("YES")
        print(a, b)
        exit()
print("NO")

'''
Explanation
Reading Input: The input consists of the number of ropes n and the target time T, followed by the list of rope burning times.

Hash Set Initialization: Convert the list of rope burning times into a hash set for O(1) average time complexity lookups.

Iterate Through Ropes: For each rope's burning time a, compute the required complement b such that a + b = T.

Check Validity: Check if b exists in the set and ensure a and b are different to form a valid pair.

Output Result: If a valid pair is found, print "YES" followed by the pair and exit. If no valid pair is found after checking all ropes, print "NO".

This approach efficiently checks each rope's complement in linear time, making it suitable for large input sizes up to 100,000 ropes.

'''
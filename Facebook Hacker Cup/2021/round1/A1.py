input_file_name = "weak_typing_chapter_1_sample_input.txt"
output_file_name = "weak_typing_chapter_1_sample_output.txt"
input_file = open(input_file_name)
output_file = open(output_file_name, 'w')

t = int(input_file.readline())
for case in range(1, t+1):
    n = int(input_file.readline())
    w = input_file.readline().strip()
    ans = 0
    cur = None
    for c in w:
        if c == 'X' or c == 'O':
            if not cur:
                cur = c
            elif cur != c:
                ans += 1
                cur = c
    output_file.write(f"Case #{case}: {ans}\n")

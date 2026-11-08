# Inline source #026 — Char Arrays

Origin: third inline transcript in the user message dated 8 November 2026. This is an editorial inventory, not a verbatim archive; the original uncorrected body remains in the conversation. No URL/timestamps supplied.

Opening anchor: «احنا الحديث عن الوان في الاخر شكل من الاشكال ... في فيديو اليوم راح ن نتعامل مع على هيئه كتاب».
Closing anchor: «كل واحده فيهم الها مميزاتها ولها عيوبها ... السلام عليكم».

1. char[] declaration and initialization: characters use single quotes, same zero-based indices as numeric arrays. Can loop to print, but println(char[]) directly prints contents.
2. Declaration without initializer, allocate and assign elements such as H/N (exact second character unclear); preserve the process, label sample text as illustrative.
3. Numeric character codes: 97 -> a, 98 -> b, A -> 65, B -> 66, '0' -> 48. Consecutive English letters have consecutive codes. Type conversion with (char)66. Consult ASCII chart; distinguish Unicode/UTF-16 as an accuracy correction.
4. C char buffers may reserve a terminator; Java tracks array length and does not require a final dedicated null terminator. Unwritten Java char elements remain U+0000; do not claim they disappear or are Spaces.
5. Scanner.next().toCharArray() reads one token; spaces stop the default token. Scanner.nextLine().toCharArray() reads whole line. Can first store a String and then convert, but temporary String variable is not always needed.
6. Sort char[] using Arrays.sort. Sorting follows character code values, so A(65), B(66), C(67), then a(97). Do not claim natural-language sorting for all Unicode.
7. Construct a String from a char[] subrange using offset and count; start 0 count 2, start 2 count 3 yields CDE for illustrative ABCDE. Asking beyond bounds produces an Exception. Exceptions are deferred to their dedicated unit.
8. Discuss why char[] may be useful compared with String: source suggests speed/security. Correct overgeneralization: String immutable, char[] mutable and wipeable; char[] is not automatically encrypted and is not universally faster. Explain only within these points.

Exact array names, some text examples, and the demonstrated call spelling are garbled; do not present illustrative reconstruction as verbatim code.

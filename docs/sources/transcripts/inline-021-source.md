# Inline source #021 — Method Overloading

Origin: user message dated 8 November 2026 in the Java Learning Library conversation. This file is a source inventory, not a verbatim transcript. The original uncorrected inline text is preserved in that conversation; no timestamp or URL was supplied. Preserve this limitation when continuing work.

Source opening anchor: «في هذا بيده راح نتكلم عن الميت او دين باختصار البدايات عرفوا انه راح يكون فيه اكثر من ما راح يشتركوا بنفس الاسم».
Source closing anchor: «الفكره انك تعرف انه اي ما ترد ممكن انه نعمل لها ... شوفكم في اخر موضوع السلام عليكم».

1. Several Methods share a name, but differ in Signature. Parameter lists discriminate them. Existing Math/abs overloads motivate the idea.
2. Initial integer sum of two arguments, illustrative 10 and 50. Passing fractional values to int Parameters fails. Changing parameter and return types can make decimal addition work, but preserve the original integer Method and add an overload instead.
3. Same name with int/int, float/float, int/float and float/int; argument type, count and ordering select the call.
4. A three-argument sum differentiates by arity. Same parameter types with renamed variables are duplicate signatures. Return type, access modifiers, static differences alone do not overload. Renaming Method is not overloading the original name.
5. Fractional 1.5 may be rejected because its literal type is double rather than float; clarify f suffix and widening only as necessary.
6. Restaurant Order example: dine-in total, delivered total + delivery fee, and app/promo total + delivery minus 2. Explicit numerical example: 15 + 3 - 2 = 16. Exact identifiers and promo text are garbled and not recoverable; use transparent illustrative names.
7. One Method calling another: nested call completes then caller prints x = 15.
8. main itself may be overloaded. Conventional launcher calls main(String[] args); explicit main(500) call executes main(int) and prints 500. Do not teach that only one method named main can exist.

Uncertainty: The source does not provide complete clean declarations or the literal promo code; the book labels reconstructions as illustrative.

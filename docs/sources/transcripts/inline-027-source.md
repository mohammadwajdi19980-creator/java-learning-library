# Inline source #027 — editorial inventory, not verbatim

Original: full user message dated 2026-11-08 in this conversation. This archive does not reproduce the transcript verbatim. The original opening is «بسم الله الرحمان الرحيم.»; final anchor is «وفرقنا بين الكون باي فاليوم والكل لهون نوصل نهاية هذا الفيديو نشوفكم الجاي. السلام عليكم.»

## Array Parameters

- Separate Methods by task: fill, print, sort and search
- Array Parameter syntax int[] x or int x[] and compatible element types
- Call passes Array name without brackets; argument and parameter names can differ
- Loop over length internally; separate whole-array size argument is unnecessary
- Reuse print Method with different Arrays and lengths

## Anonymous Arrays

- Pass new int[]{1,2,3} directly without a named caller Variable

## Returning an Array

- Array Return Type and local Array returned by reference value
- Return anonymous Array directly
- Capture returned reference and read indexed elements; direct create()[1]

## Printing a Reference

- Printing int[] or array-returning Method shows Object representation, not elements; distinguish println(char[])
- Representation is not a guaranteed physical Memory address

## Assignment and Aliasing

- a=b copies Reference rather than Elements; initial Arrays 1,2,3 and 40,50,60
- Mutations to100 then500 visible through both names
- Three or more aliases share Elements; setting zero visible across all

## Java Is Always Pass-by-Value

- Method mutates Element to50 visible at Caller
- Primitive y=5 remains5 despite assigning10 to local Parameter
- Correct inaccurate call-by-reference claim: Java copies Reference value
- Parameter reassignment does not reassign caller Variable; no Java & parameter syntax

Uncertain source details: exact original identifiers and some literal values are garbled or absent in speech-to-text. Runnable programs are editorial reconstructions of the same concepts. The claim that arrays are call-by-reference is corrected to Java pass-by-value of a reference. No audiovisual frame was supplied.

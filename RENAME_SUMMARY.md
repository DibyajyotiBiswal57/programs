# Program Files Rename Summary

## Completed Renames

### Total Files Renamed: 67

#### Python (61 files)
All Python files with valid question number comments have been renamed from their original names to the standardized format based on questions.md. The renaming applied a -1 offset to question numbers in comments (e.g., #Q40 → Q39 → 0039_vowel_consonant.py).

**Examples:**
- `vowel.py` (#Q40) → `0039_vowel_consonant.py`
- `perimeter.py` (#Q25) → `0024_perimeter.py`
- `leap_year.py` (#Q32) → `0031_leap_year.py`
- `sum.py` (#Q56) → `0055_continue_example.py`
- `range.py` (#Q18) → `0017_reverse_number.py`

#### Other Languages (6 files)
- Go: `1_hello_world.go` → `0021_name_triangle.go`
- Haskell: `1_hello_world.hs` → `0021_name_triangle.hs`
- C: `1_hello_world.c` → `0001_hello_world.c`
- C++: `1_hello_world.cpp` → `0001_hello_world.cpp`
- Perl: `1_hello_world.pl` → `0001_hello_world.pl`
- C#: `1_hello_world.cs` → `0001_hello_world.cs`

## Files Requiring Manual Review

### Python (2 files)
1. **add_3_numbers.py** - Has comment `#Q1` which with -1 offset maps to Q0 (doesn't exist). Content appears to implement Q2 (sum of 3 numbers).
2. **smallest_no.py** - No question number comment in file.

### Java (33 files)
All Java files lack question number comments. Need to analyze file content to determine correct question mapping:
- 1_hello_world.java
- add_3_numbers.java
- add_subtract_multiply.java
- area.java
- average_score.java
- child_or_adult.java
- cube_or_square.java
- digits_finder.java
- discount.java
- divisible_by_7_or_3.java
- even_or_odd.java
- greater_than_or_equal.java
- is_it_complementary_or_supplementary.java
- largest_number.java
- leap_year.java
- neons_number.java
- number_teller.java
- perimeter.java
- positive_or_negative.java
- profit_and_loss.java
- rectangle_or_cylinder.java
- reversed_number.java
- simple_interest.java
- smaller_number.java
- swapping.java
- swapping_without_3rd_var.java
- volume.java
- voting_eligibility.java
- vowel_or_consonant.java
- weird_operations.java
- weird_operations2.java
- weird_operations3.java
- weird_operations4.java

### QBasic (25 files)
All QBasic files lack question number comments:
- 1_hello_world.bas
- add_3_numbers.bas
- area&vol.bas
- child_or_adult.bas
- descending_order.bas
- even_number_printer.bas
- even_or_odd.bas
- greater.bas
- is_it_prime.bas
- is_it_supplementary_or_complementary.bas
- marks_average.bas
- multiplication_table.bas
- number_printer.bas
- odd_nos_bw2nos.bas
- perimeter.bas
- positive_or_negative.bas
- profit&loss.bas
- reversed_number.bas
- simple_interest.bas
- sum_difference_and_product.bas
- swapping.bas
- swapping_without_3rd_var.bas
- voting_eligibility.bas
- weird_operations.bas
- weird_operations2.bas

## Notes

1. **-1 Offset**: The question numbers in Python file comments were systematically off by 1 (e.g., #Q40 in the file corresponds to Q39 in questions.md). This offset has been applied during renaming.

2. **Content Verification**: Some files may have content that doesn't match their question number. The README.md note states: "The question numbers and status do not match with the code." Manual verification is recommended.

3. **Standardized Format**: All renamed files follow the format `NNNN_descriptive_name.ext` where NNNN is a 4-digit zero-padded question number and descriptive_name matches questions.md.

4. **Next Steps**: For files without comments (Java, QBasic, and 2 Python files), analyze the code content and compare with questions.md descriptions to determine the correct question number, then rename accordingly.

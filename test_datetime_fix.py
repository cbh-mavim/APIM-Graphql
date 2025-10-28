#!/usr/bin/env python3
"""
Test script for datetime formatting fixes.
Tests the problematic datetime format that was causing Power BI errors.
"""

from gql.utils.datetime import normalize_datetime_format

def test_datetime_formats():
    """Test various datetime formats that might cause issues."""
    
    test_cases = [
        # The problematic format from your error
        "2020-01-28 09:47:43.0000000 +00:00",
        
        # Other common formats
        "2020-01-28T09:47:43.000Z",
        "2020-01-28T09:47:43Z",
        "2020-01-28 09:47:43",
        "2020-01-28",
        None,
        "",
        
        # Edge cases
        "2020-12-31T23:59:59.999999+05:30",
        "invalid-date",
    ]
    
    print("🧪 Testing DateTime Format Normalization")
    print("=" * 60)
    
    for i, test_value in enumerate(test_cases, 1):
        print(f"\n{i}. Testing: {repr(test_value)}")
        
        try:
            # Test the normalization function
            normalized = normalize_datetime_format(test_value)
            print(f"   Result: {repr(normalized)}")
            
            if normalized:
                print("   ✅ Successfully normalized")
            elif test_value is None or test_value == "":
                print("   ✅ Correctly handled empty/null value")
            else:
                print("   ⚠️  Returned None (invalid input)")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 Key Test: The problematic format")
    
    problematic_format = "2020-01-28 09:47:43.0000000 +00:00"
    result = normalize_datetime_format(problematic_format)
    
    print(f"Input:  {problematic_format}")
    print(f"Output: {result}")
    
    if result and not result.endswith(".0000000 +00:00"):
        print("✅ SUCCESS: Problematic format fixed!")
        print("   This should now work with Power BI and other consumers.")
        print(f"   The format changed from excessive precision to: {result}")
    else:
        print("❌ FAILED: Still has problematic format.")
    
    return result

if __name__ == "__main__":
    test_datetime_formats()